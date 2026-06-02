# graph/ — published knowledge subgraph

**`bioregional-mapping.jsonld` is a GENERATED artifact. Do not hand-edit it.** Re-run the exporter instead.

This directory publishes this repo's curated canon as machine-readable JSON-LD, so the knowledge is portable, forkable, and RDF-native — not trapped in a single private KOI backend. It composes with (does not replace) the human-authored markdown+YAML in `docs/research/connections/`.

Originating canon decision: [`bioregional-economics:ADR-0003`](https://github.com/DarrenZal/bioregional-economics/blob/main/docs/research/canon-decisions/0003-published-knowledge-graph-subset.md) (this repo adopts the same pattern; a local ADR can ratify it here if/when this surface earns its own canon-decision).

## What's in it

A JSON-LD `@graph` of three node types:

- **`skos:Concept`** — frozen-vocabulary concepts + any referenced by notes (`@id: bioregional-mapping.concept.<slug>`)
- **`Connection`** — one per bridge note (`@id: bioregional-mapping.connection.<slug>`), with `disposition`, `about` (concepts), `sourceTitle`, and `hasClaim`
- **`Claim`** — one per projected source claim (`@id:` the KOI claim RID), with `statement`, `confidence`, `anchor`, `claimType`, `attributedTo`, `isPartOf`, and `about`

## Directionality (the rule that prevents drift)

One writer per artifact: bridge notes (markdown+YAML) are **hand-authored** and project INTO the personal-koi backend; `graph/*.jsonld` is **generated** from the backend (claim identities/RIDs) + this repo's frontmatter, and committed. Never hand-edit the JSON-LD.

## Regenerate

```bash
# requires: python3 (stdlib only) + psql reachable to personal_koi
python3 scripts/export_subgraph.py        # --project defaults to this repo's name
```

Regenerate after authoring/amending bridge notes (and after `project_bridge_notes.py --apply`). A consumer/fork needs only the committed `.jsonld`.

## Privacy gate

**This repo is public** — the export deliberately emits only published bridge-note claims + concepts (already public in `connections/*.md`) and **never** references backend entities flagged `node_private`. Keep that constraint: widen scope (e.g. to Person/Organization entity nodes) only after an explicit privacy review.
