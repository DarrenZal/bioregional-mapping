<!-- workstream: spore -->

> **Stream scope:** Spore + related canons (IC, PM, koi-processor, BKC, bioregional-coordination, bioregional-mapping). Cross-stream recommendations require operator opt-in. See `~/CLAUDE.md` "Stream-scope discipline" for rule.

# Project Context for Claude — bioregional-mapping

**Project**: bioregional-mapping — canon-bearing repository for bioregional mapping practice (multi-layer mapping-as-coordination: relational, cultural, ecological, economic, governance, geospatial).

**Status**: Minimal skeleton (created 2026-05-04); grows organically as substrate-pressure surfaces.

**Your Role**: AI coding assistant helping with canon-bearing work in this repo + cross-repo coordination with bioregional-coordination (nearest upstream peer) and Spore (transitively upstream root).

---

## Repo identity (read this before authoring)

**This repo is a canon-bearing peer specializing bioregional-coordination at the mapping sub-domain.** It is the explicit Q5 admission from [`bioregional-coordination:ADR-0001`](https://github.com/DarrenZal/bioregional-coordination/blob/main/docs/research/canon-decisions/0001-repo-identity-and-spore-relationship.md) §Parking-lot — admission triggered by the Regenerate Cascadia Landscape Hub Cultivator Phase 2 program (April–July 2026) and the wider practitioner-field signal (Tijn Tjoelker LinkedIn thread 2026-05-04, BioKulture blue paper, Joe Brewer mapping webinar).

**Cross-citations:**
- Upstream nearest peer: bioregional-coordination — cite by `bioregional-coordination.<doc-id>` and ADR number
- Upstream root: Spore — cite by `spore:ADR-NNNN-<slug>` (transitively via bioregional-coordination, directly when bioregional-coordination's specialization is silent)
- Peer instance-family: BKC, SalishOakSeeds — cross-cite at peer level (no alignment ADRs)

**Conceptual frame**: bioregional mapping as multi-layer practice, situated within "agentic bioregionalism" (canonized at Spore via [`spore.positioning.agentic-bioregionalism`](https://github.com/DarrenZal/spore/blob/main/docs/positioning/agentic-bioregionalism.md)).

---

## Project-id namespace (operator-ratified 2026-05-04)

**Namespace**: `bioregional-mapping` — matches the repo-name choice; deliberately verbose; parallels `bioregional-coordination` namespace.

doc_ids use `bioregional-mapping.<slug>` (e.g., `bioregional-mapping.project-vision`, `bioregional-mapping.canon-decision.repo-identity-and-bregion-coord-relationship`, `bioregional-mapping.connection.rc-phase-2-program-guide`).

**Project_id in cross-project learning field**: `bioregional-mapping` (full namespace, mirroring bioregional-coordination's registration on regen-prod). Bridge-note filenames use slug-only form (`<slug>.md`); doc_id form is `bioregional-mapping.connection.<slug>` (matching bioregional-coordination's connection convention; the parser reads `source_document` from the doc_id, not the filename).

---

## Method discipline (carry-forward from Spore + bioregional-coordination canon work)

1. **NEVER use `git add -A` or `git add .`** — explicit staging only
2. **NEVER hard-reset** — preflight is scoped
3. **READ-ONLY for sibling repos** when authoring here; verify zero-change at any state-check
4. **Cross-repo citations by ADR number** (`spore:ADR-NNNN-<slug>` or `bioregional-coordination:ADR-NNNN-<slug>`), not commit SHA
5. **Inherit, don't redefine** — Spore + bioregional-coordination own grammar; this repo specializes only when mapping-specific operational pressure surfaces
6. **Audit-then-propose at Step 0.5** of any planning work — don't pre-bake recommendations
7. **Sandbox-plan-file contingency** — if plan dir denied, write to `tmp/`
8. **Future-doctrine markers held** — local foundation docs / patterns / ADRs admit only when operational pressure surfaces; do NOT direct-edit canon to formalize candidates without earning-test
9. **Cascade-miss discipline** — when softening / amending claims in one location, grep broader than edit surface (4-layer: canon edits / memo amendments / handoff state-baseline / handoff technical-claims)
10. **Honest-rigor cluster-counting verdict-neutral** — admit AND decline are both legitimate

These disciplines transfer from Spore's canon-rebuild arc method retrospective (`spore:docs/research/connections/canon-rebuild-arc-method-retrospective.md`) and bioregional-coordination's CLAUDE.md.

---

## Frontmatter conventions

Inherits Spore + bioregional-coordination conventions, adapted for `bioregional-mapping` namespace:

```yaml
---
doc_id: bioregional-mapping.<slug>
doc_kind: <foundation|decision-record|connection|positioning|pattern|spec|architecture|research|planning|vision>
status: <draft|active|superseded|archived|deprecated>
depends_on:
  - bioregional-mapping.<slug>             # local canonical refs
  - bioregional-coordination.<slug>        # nearest-upstream peer refs
  - spore.<slug>                            # upstream-root refs (transitive or direct)
relates_to:
  - <other doc_ids>
date: YYYY-MM-DD
author: darren-zal
---
```

Concepts-yaml: NOT yet admitted (per `spore:ADR-0080` precedent followed by IC, PM, and bioregional-coordination). Admit later if cross-repo translation pressure fires. Frozen-vocabulary.yaml in `docs/research/connections/` is a separate artifact (Spore intake protocol §2a) — not the same as concepts-yaml.

---

## Bridge-note schema (Spore intake protocol §3)

Bridge notes in `docs/research/connections/` follow the schema documented in [`spore:docs/research/planning/learning-field-intake-protocol-v1.md`](https://github.com/DarrenZal/spore/blob/main/docs/research/planning/learning-field-intake-protocol-v1.md). See also `docs/research/connections/README.md` in this repo for the local digest.

**Filename:** `<slug>.md` (slug-only; mirrors bioregional-coordination convention)

**Frontmatter**: `doc_id: bioregional-mapping.connection.<slug>`, `doc_kind: connection`, `status`, `disposition` (human form per parser's `DISPOSITION_SLUG`: `clarify existing term | candidate primitive | candidate pattern | implementation hypothesis | unresolved tension | no change`), `concepts` (entries from frozen-vocabulary.yaml), `sources` (with title, url_or_path, accessed), `date`, `author`.

**Body**: section heading `## Claim Register` (the parser searches for this exact heading; optionally numbered like `## 1. Claim Register`); source claims `**C1** [confidence: ...] [anchor: §...] Statement.`; review claims under `## Review Claims` heading with format `**R1** [review claim] [target: doc.id] [concept: slug]\\nStatement.\\n*R1 is supported by C1, C2.*` (target MUST be in r-claim-allowlist.yaml).

**Opposition discipline**: ≥2 `no-change` opposition notes per ≥10 total bridge-note intake. Tracked by `convergence_export.py` opposition-rate metric.

---

## Cross-project learning-field wiring

This repo participates in the cross-project learning field as project_id `bioregional-mapping`. Wiring lives in:

- `~/projects/RegenAI/koi-processor/scripts/project_bridge_notes.py` PROJECTS dict (entry `"bioregional-mapping"`)
- `~/projects/RegenAI/koi-processor/api/convergence_export.py` (consumes `source_document LIKE 'bioregional-mapping.%%'`)

After authoring or amending bridge notes:

```bash
cd ~/projects/regenai/koi-processor
python3 scripts/project_bridge_notes.py --dry-run    # preview
python3 scripts/project_bridge_notes.py --apply      # register claims in KOI
python3 api/convergence_export.py                    # refresh field-family rollup
```

Or invoke `/convergence-board` skill for the visual cross-project board.

---

## Parking items (deferred per ratified plan; do NOT execute without operator-gate)

- **License (ADR-0002 target)**: not yet ratified. Default: all-rights-reserved by author. License decision is its own concern. Target within 4 weeks of repo creation; coordinate with bioregional-coordination's eventual license ADR so the two repos align.

- **Future foundation docs**: this repo will likely admit local foundation docs / patterns / ADRs as mapping-specific operational concerns surface. Currently zero local foundation docs (minimal skeleton). Foundation-doc admission requires `ready_convergent` or `ready_with_tension` state from `convergence_export.py`.

- **GitHub-sensor RAG ingest**: personal_koi `github_repos` table is not present locally (migration 043 not applied). The RAG-ingest path for canon-repo content into personal KOI is deferred. The convergence-export path (bridge notes → claims) is unaffected and is the primary learning-field integration.

- **Workshop facilitation packets**: `docs/workshops/` empty initially; populate when a real mapping workshop earns canonical articulation (e.g., Victoria workshop after RC Phase 2 launch).

- **Six-layer rubric canonization**: currently a heading set in project-vision.md; admit as foundation doc only after multi-bridge-note convergence (≥3 bridge notes ratifying or refining).

---

## What this repo is NOT

- **Not a fork of bioregional-coordination**: that repo (`~/projects/bioregional-coordination/`) remains separate; this repo is its mapping-specialization peer.
- **Not a fork of Spore**: Spore is upstream root; this repo cites Spore transitively via bioregional-coordination.
- **Not a fork of BKC or SalishOakSeeds**: those are sibling instance-family members; cross-citation at peer level.
- **Not a federation participant**: the convergence-export pipeline integration is the cross-project surface; KOI-net federation is not in scope.
- **Not a publisher of bioregional-mapping content**: this is canon infrastructure, not content. Content lives in instance-deployments (BKC pilots, Greater Victoria mapping via SalishOakSeeds, future hub repos).
- **Not a host for the RC Bioregional Mapping Field Guide**: RC's Field Guide is canonical RC content; this repo bridge-notes it.
- **Not redefining grammar**: Spore + bioregional-coordination own the grammar; this repo specializes by citing upstream.
- **Not committed to a license yet**: see parking item above.

---

## Canon-decisions are first-class

Even at minimal skeleton phase, canon decisions get recorded as ADRs in `docs/research/canon-decisions/`. ADR-0001 establishes repo identity + relationship to bioregional-coordination. Future canon decisions follow Spore's ADR template conventions (see `spore:docs/research/canon-decisions/`).

## Recent ecosystem cross-refs (2026-05-04 admission context)

- **bioregional-coordination ADR-0001 §Parking-lot Q5** — anticipated this repo's admission as the mapping sub-domain canon repo
- **RC LHC Phase 2 Program Guide** (private; local snapshot at `~/projects/SalishOakSeeds/docs/rc-phase-2-program-guide.md`) — primary day-1 source claim contributor
- **Tijn Tjoelker LinkedIn thread (2026-05-04)** — wider practitioner field signal; tooling-map source candidate
- **BioKulture blue paper** (Zenodo 10.5281/zenodo.16656790) — Indigenous-led BioKulture engineering frame
- **BKC mapping foundations** (`bioregional-mapping-model-v0.1.md`, `bioregional-mapping-intake-contract-v0.1.md`) — operational ontology + intake contract that this repo's canon framing rides above
