#!/usr/bin/env python3
"""Export this repo's canonical knowledge subgraph as JSON-LD (hybrid model).

GENERATED-ARTIFACT PRODUCER. The file it writes (graph/<project>.jsonld) is a
generated snapshot — do NOT hand-edit it; re-run this script instead. Per
docs/research/canon-decisions/0003-published-knowledge-graph-subset.md the
directionality is hybrid:
  - bridge notes (markdown+YAML) are hand-authored truth → project INTO the backend
  - this JSON-LD is GENERATED from the backend (claim identities + RIDs) plus the
    repo's own bridge-note frontmatter (concept links, disposition, sources)

Dependency-light on purpose (stdlib + `psql` only) so a fork can regenerate
without the full koi-processor stack. Consumers only need the committed .jsonld.

Privacy gate: only published bridge-note claims + frozen-vocabulary concepts are
emitted (all are canon meant for publication). Backend entities flagged
node_private are never referenced here. Widen with care.

Usage:
  python3 scripts/export_subgraph.py \
    [--project bioregional-economics] \
    [--db postgresql://localhost:5432/personal_koi] \
    [--out graph/bioregional-economics.jsonld]
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def fetch_claims(db: str, project: str) -> list[dict]:
    """Pull projected claims for this project from the personal-koi backend."""
    q = (
        "SELECT json_agg(row_to_json(t)) FROM ("
        "SELECT claim_rid, statement, claim_type, source_document, claimant_uri, "
        "metadata->>'c_id' AS c_id, metadata->>'confidence' AS confidence, "
        "metadata->>'evidence_anchor' AS anchor "
        f"FROM claims WHERE source_document LIKE '{project}.%' "
        "ORDER BY source_document, (metadata->>'c_id')) t;"
    )
    out = subprocess.run(["psql", db, "-tAc", q], capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit(f"psql failed: {out.stderr.strip()}")
    rows = out.stdout.strip()
    return json.loads(rows) if rows and rows != "" else []


def parse_frontmatter(md: str) -> dict:
    """Minimal, dependency-free parse of the bridge-note YAML frontmatter we author."""
    if not md.startswith("---"):
        return {}
    end = md.find("\n---", 3)
    fm = md[3:end] if end != -1 else ""
    lines = fm.splitlines()
    out: dict = {"concepts": [], "source_titles": []}
    i = 0
    while i < len(lines):
        ln = lines[i]
        m = re.match(r"^(doc_id|disposition|date|status):\s*(.+)$", ln)
        if m:
            out[m.group(1)] = m.group(2).strip()
        elif re.match(r"^concepts:\s*$", ln):
            i += 1
            while i < len(lines) and re.match(r"^\s*-\s+", lines[i]):
                out["concepts"].append(re.sub(r"^\s*-\s+", "", lines[i]).strip())
                i += 1
            continue
        elif re.match(r"^sources:\s*$", ln):
            i += 1
            while i < len(lines) and (lines[i].startswith(" ") or lines[i].startswith("\t")):
                t = re.match(r"^\s*-?\s*title:\s*(.+)$", lines[i])
                if t:
                    out["source_titles"].append(t.group(1).strip().strip('"'))
                i += 1
            continue
        i += 1
    # H1 title from the body
    body = md[end + 4:] if end != -1 else md
    h1 = re.search(r"^#\s+(.+)$", body, re.M)
    out["title"] = h1.group(1).strip() if h1 else out.get("doc_id", "")
    return out


def parse_frozen_vocab(path: Path) -> list[dict]:
    if not path.is_file():
        return []  # frozen-vocabulary is optional; concepts still come from note frontmatter
    concepts = []
    slug = None
    for ln in path.read_text().splitlines():
        m = re.match(r"^-\s*slug:\s*(.+)$", ln)
        d = re.match(r"^\s+description:\s*(.+)$", ln)
        if m:
            slug = m.group(1).strip()
        elif d and slug:
            concepts.append({"slug": slug, "description": d.group(1).strip()})
            slug = None
    return concepts


def build_jsonld(project: str, claims: list[dict], notes: list[dict], concepts: list[dict]) -> dict:
    ns = f"{project}."
    ctx = {
        "@vocab": f"https://w3id.org/koi/{project}#",
        "schema": "https://schema.org/",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "prov": "http://www.w3.org/ns/prov#",
        "name": "schema:name",
        "description": "schema:description",
        "statement": "schema:text",
        "title": "schema:name",
        "disposition": "schema:creativeWorkStatus",
        "claimType": "schema:additionalType",
        "anchor": "schema:citation",
        "sourceTitle": "prov:wasDerivedFrom",
        "attributedTo": {"@id": "prov:wasAttributedTo", "@type": "@id"},
        "about": {"@id": "schema:about", "@type": "@id"},
        "isPartOf": {"@id": "schema:isPartOf", "@type": "@id"},
        "hasClaim": {"@id": "schema:hasPart", "@type": "@id"},
    }
    graph: list[dict] = []
    # Union frozen-vocabulary concepts with every concept referenced by a note,
    # so concept @ids are never dangling even if frozen-vocabulary is partial/absent.
    desc_by_slug = {c["slug"]: c["description"] for c in concepts}
    referenced = {s for n in notes for s in n.get("concepts", [])}
    for slug in sorted(set(desc_by_slug) | referenced):
        node = {"@id": f"{ns}concept.{slug}", "@type": "skos:Concept", "name": slug}
        if desc_by_slug.get(slug):
            node["description"] = desc_by_slug[slug]
        graph.append(node)
    by_doc: dict[str, list[dict]] = {}
    for cl in claims:
        by_doc.setdefault(cl["source_document"], []).append(cl)
    for n in notes:
        doc_id = n.get("doc_id")
        if not doc_id:
            continue
        concept_ids = [f"{ns}concept.{s}" for s in n["concepts"]]
        graph.append({
            "@id": doc_id,
            "@type": "Connection",
            "title": n.get("title", doc_id),
            "disposition": n.get("disposition", ""),
            "about": concept_ids,
            "sourceTitle": n["source_titles"],
            "hasClaim": [c["claim_rid"] for c in by_doc.get(doc_id, [])],
        })
        for cl in by_doc.get(doc_id, []):
            graph.append({
                "@id": cl["claim_rid"],
                "@type": "Claim",
                "identifier": cl.get("c_id"),
                "statement": cl["statement"],
                "schema:confidence": cl.get("confidence"),
                "anchor": cl.get("anchor"),
                "claimType": cl.get("claim_type"),
                "attributedTo": cl.get("claimant_uri"),
                "about": concept_ids,
                "isPartOf": doc_id,
            })
    return {
        "@context": ctx,
        "@id": f"{ns}graph.canonical-subgraph",
        "@type": "schema:Dataset",
        "name": f"{project} — canonical knowledge subgraph",
        "description": (
            "Generated JSON-LD projection of this repo's curated canon: bridge-note "
            "claims (from the personal-koi backend) linked to concepts (frozen-vocabulary) "
            "and their source connections. Hybrid model; see ADR-0003. Do not hand-edit."
        ),
        "prov:wasGeneratedBy": "scripts/export_subgraph.py",
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "counts": {
            "concepts": len([g for g in graph if g["@type"] == "skos:Concept"]),
            "connections": len([g for g in graph if g["@type"] == "Connection"]),
            "claims": len([g for g in graph if g["@type"] == "Claim"]),
        },
        "@graph": graph,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=None, help="repo root (default: this script's repo)")
    ap.add_argument("--project", default=None, help="namespace / project_id (default: repo dir name)")
    ap.add_argument("--db", default="postgresql://localhost:5432/personal_koi")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    repo = Path(args.repo).expanduser().resolve() if args.repo else REPO
    project = args.project or repo.name

    conn_dir = repo / "docs" / "research" / "connections"
    notes = []
    for md_path in sorted(conn_dir.glob("*.md")):
        if md_path.name == "README.md":
            continue
        notes.append(parse_frontmatter(md_path.read_text()))
    concepts = parse_frozen_vocab(conn_dir / "frozen-vocabulary.yaml")
    claims = fetch_claims(args.db, project)

    doc = build_jsonld(project, claims, notes, concepts)
    out = Path(args.out) if args.out else (repo / "graph" / f"{project}.jsonld")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
    c = doc["counts"]
    print(f"wrote {out} — {c['claims']} claims, "
          f"{c['connections']} connections, {c['concepts']} concepts")


if __name__ == "__main__":
    main()
