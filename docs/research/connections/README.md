# docs/research/connections/

Bridge notes for cross-repo coordination and external-work intake.

Bridge notes serve three purposes (mirroring bioregional-coordination's connections/):

1. **Cross-citation with peer instance-family members** (BKC, SalishOakSeeds, future hub repos)
2. **Comparative intake of external practitioner work** (RC LHC Phase 2 Program Guide, Tijn-thread tooling-map, BioKulture blue paper, Joe Brewer mapping webinar, regenatlas, Felt, QGIS, Kumu, Restor, Open Impact, OMNI-Mapping, MAP, Speak for the Trees, water-bioregion, etc.)
3. **Reciprocal-citation closure** with bioregional-coordination + Spore (when bioregional-mapping canon objects are cited from upstream-side and the reciprocal direction needs articulation)

## Current bridge notes

- [`bm.connection.rc-phase-2-program-guide.md`](./bm.connection.rc-phase-2-program-guide.md) — Day-1 seed: claims extracted from RC Phase 2 Program Guide

## Bridge-note schema (Spore intake protocol §3)

Authoritative reference: [`spore:docs/research/planning/learning-field-intake-protocol-v1.md`](https://github.com/DarrenZal/spore/blob/main/docs/research/planning/learning-field-intake-protocol-v1.md). The local digest below is for quick reference; cite the authoritative source by doc_id.

**Filename:** `bm.connection.<slug>.md`

**Frontmatter (YAML):**

```yaml
---
doc_id: bioregional-mapping.connection.<slug>
doc_kind: research
research_subkind: bridge_note
disposition: <clarify | propose-primitive | propose-pattern |
              hypothesize | resolve-tension | no-change>
concepts: [<concept-slug-1>, <concept-slug-2>, ...]
                              # entries MUST appear in frozen-vocabulary.yaml
sources:
  - title: <human-readable title>
    url_or_path: <canonical URL or local snapshot path>
    accessed: <YYYY-MM-DD>
status: draft                 # draft → review → ratified
---
```

**Claim format (in body):**

Source claims — what the external work contributes:

```
**C1** [confidence: high|medium|low] [anchor: §<ref>] <Statement.>
**C2** [confidence: medium] [anchor: §<ref>] <Statement.>
```

Review claims — proposed canon changes (targets MUST appear in `r-claim-allowlist.yaml`):

```
**R1** [target: <doc.id>] [concept: <concept-slug>] <Statement.>
```

**Disposition vocabulary:**

- `clarify` — records existing canon more precisely; no canon change
- `propose-primitive` — surface a candidate primitive specialization
- `propose-pattern` — surface a candidate pattern (named recurring shape)
- `hypothesize` — speculative; needs more sources to converge
- `resolve-tension` — propose resolution of a documented tension
- `no-change` — opposition note; R-claims rejected, argues against a candidate change or for status-quo

**Opposition discipline:** ≥2 `no-change` opposition notes per ≥10 total bridge-note intake. Tracked by `convergence_export.py` opposition-rate metric.

**Convergence readiness states** (computed by `convergence_export.py`):

- `ready_convergent` — 2+ source claims aligned, no `no-change` opposition
- `ready_with_tension` — 2+ source claims, has documented opposition
- `needs_more_sources` — 1 source claim
- `insufficient` — 0 source claims

A specialization is eligible for foundation-doc admission only at `ready_convergent` or `ready_with_tension`. This is how the "grow organically" discipline is enforced.

## Authoring conventions

- Cite Spore canon by ADR number (`spore:ADR-NNNN-<slug>`), not commit SHA
- Cite bioregional-coordination canon by ADR number or doc_id (`bioregional-coordination:ADR-NNNN-<slug>` or `bioregional-coordination.<slug>`)
- Cite peer-repo canon by their canonical doc_ids
- Surface mapping is selective (load-bearing only); does NOT merge bounded contexts
- Bridge notes are NOT alignment ADRs — they don't track upstream evolution; they articulate cross-repo relationships at a moment in time
- Concepts in `concepts:` frontmatter MUST appear in `frozen-vocabulary.yaml`
- R-claim targets MUST appear in `r-claim-allowlist.yaml`

## Workflow

After authoring or amending bridge notes:

```bash
cd ~/projects/regenai/koi-processor
python3 scripts/project_bridge_notes.py --dry-run    # preview
python3 scripts/project_bridge_notes.py --apply      # register claims in KOI
python3 api/convergence_export.py                    # refresh field-family rollup
```

Or invoke `/convergence-board` skill for the visual cross-project board. Use `/comparative-intake` skill for processing new external artifacts into bridge notes (handles artifact profiling, subsystem mapping, claim generation, disposition assignment).
