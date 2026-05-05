---
doc_id: bioregional-mapping.canon-decision.repo-identity-and-bregion-coord-relationship
doc_kind: decision-record
status: active
decision: edit
depends_on:
  - bioregional-mapping.project-vision
  - bioregional-coordination.project-vision
  - bioregional-coordination.canon-decision.repo-identity-and-spore-relationship
  - spore.project-vision
relates_to:
  - spore.positioning.agentic-bioregionalism
  - spore.docs.research.planning.learning-field-protocol-v1
  - spore.docs.research.planning.learning-field-intake-protocol-v1
date: 2026-05-04
author: darren-zal
---

# ADR-0001 — Repo Identity and Bioregional-Coordination Relationship

## Context

This repository was created 2026-05-04 to host the canon-bearing structure for **bioregional mapping practice** as multi-layer mapping-as-coordination. Admission was triggered per [`bioregional-coordination:ADR-0001`](https://github.com/DarrenZal/bioregional-coordination/blob/main/docs/research/canon-decisions/0001-repo-identity-and-spore-relationship.md) §Parking-lot Q5 — *"should economics / finance / mapping / governance aspects of bioregional coordination get their own repos (e.g., `bioregional-economics`, `bioregional-mapping`)?"* — when cross-repo coordination pressure surfaced via:

- The Regenerate Cascadia Landscape Hub Cultivator Phase 2 program (April–July 2026, Field Guide target April 10, workshops June–July, TIBC presentation September 14–19), where Darren is in Victoria's Landscape Group via SalishOakSeeds
- The wider practitioner-field signal: Tijn Tjoelker LinkedIn thread 2026-05-04 (frustration with isolated tools and call for integration / interoperability across Felt, QGIS, regenatlas, Kumu, Miro, Notion, Hylo, Restor, Open Impact, etc.); Joe Brewer's bioregional-mapping webinar emphasis on social mapping beyond geospatial; BioKulture blue paper (WarīNkwī Flores et al, Zenodo 10.5281/zenodo.16656790); Sierra Nevada de Santa Marta BOT bioregional operating system work

The conceptual frame is canonized at Spore via [`spore.positioning.agentic-bioregionalism`](https://github.com/DarrenZal/spore/blob/main/docs/positioning/agentic-bioregionalism.md), specialized at bioregional-coordination's peer-canon repo, and now further specialized here for the mapping sub-domain.

Four structural questions required ratification at repo creation:

1. **Repo name + namespace** — the descriptive vs short-form tradeoff
2. **Upstream relationship** — bioregional-coordination as nearest peer; Spore as transitively-upstream root
3. **Initial canon structure** — minimal-skeleton + grow organically (mirroring bioregional-coordination)
4. **Cross-project learning-field registration** — wire as project_id `bm` from day 1 (mirroring spore / bioregional-coordination / ic / fc / pm)

This ADR records the operator-ratified resolutions and the load-bearing rationale.

## Decision

### (1) Repo name + doc_id namespace: `bioregional-mapping`

Repository directory: `~/projects/bioregional-mapping/`. GitHub: `DarrenZal/bioregional-mapping`. doc_id namespace: `bioregional-mapping.<slug>` (matches the verbose repo name; deliberate alignment of repo-name + namespace as parallel canonical-citation surfaces; parallels `bioregional-coordination.<slug>`).

Cross-project learning-field project_id: `bm` (two-letter shortname, parallel to `ic`, `fc`, `pm`). Bridge-note filenames use `bm.connection.<slug>.md` so source-document prefix matches PROJECTS-registry project_id.

GitHub home is the personal account `DarrenZal/` (mirroring `DarrenZal/spore` and `DarrenZal/bioregional-coordination`). Canon repos live in personal account by convention; instance repos use org accounts (`BioregionalKnowledgeCommons/bioregional-commons-web`, `BioregionalKnowledgeCommons/roadmap`).

### (2) Upstream relationship: bioregional-coordination as nearest peer; Spore as transitively-upstream root

bioregional-mapping specializes [`bioregional-coordination`](https://github.com/DarrenZal/bioregional-coordination) at the mapping sub-domain. bioregional-coordination is the nearest upstream peer; Spore is upstream root (cited transitively via bioregional-coordination, and directly when bioregional-coordination's specialization is silent on a primitive that the mapping practice exercises).

This repo does NOT redefine grammar from Spore or bioregional-coordination. It specializes by citing upstream and adding mapping-practice-specific specializations only when operational pressure earns admission per inherited discipline.

Cross-citation: by ADR number (`spore:ADR-NNNN-<slug>`, `bioregional-coordination:ADR-NNNN-<slug>`) or doc_id, never by commit SHA.

### (3) Peer instance-family relationships: BKC + SalishOakSeeds

[BKC](https://github.com/LinuxIsCool/BioregionKnwoledgeCommons) and SalishOakSeeds (`~/projects/SalishOakSeeds/`) are **peers at the instance-family layer** with bioregional-mapping. Neither downstream of this repo; this repo not downstream of either.

- BKC owns operational instance machinery: KOI graph, entity resolution, ontology (`bkc-ontology.jsonld`, 25 types + 39 predicates), federation runtime (Octo), capital-layer work (Hub Cultivator + TBFF + on-chain claims), and existing mapping-related docs (`bioregional-mapping-model-v0.1.md` and `bioregional-mapping-intake-contract-v0.1.md` at `BioregionalKnowledgeCommoning/docs/foundations/`). BKC retains its existing identity. bioregional-mapping bridge-notes BKC's mapping-related docs and adds the canon-framing layer they ride within.

- SalishOakSeeds owns Victoria-pilot-specific operational content (workshop-design-guide-v2.md, RC funding proposal, participant outreach, workshop logistics). bioregional-mapping bridge-notes SalishOakSeeds work; abstract methodology generalizes here when operational pressure surfaces.

Future hub repos (Boulder, Sierra Nevada de Santa Marta, etc.) will be additional instance-family peers as they emerge.

### (4) Initial canon structure: minimal skeleton + grow organically

Initial structure (2026-05-04):

```
~/projects/bioregional-mapping/
├── .gitignore
├── README.md
├── CLAUDE.md
├── project-vision.md        # bioregional-mapping.project-vision
└── docs/
    ├── README.md
    ├── foundations/         # placeholder; zero local foundation docs admitted
    │   └── README.md
    ├── research/
    │   ├── canon-decisions/
    │   │   ├── README.md
    │   │   └── 0001-repo-identity-and-bregion-coord-relationship.md (this doc)
    │   └── connections/
    │       ├── README.md
    │       ├── frozen-vocabulary.yaml      # Spore intake protocol §2a
    │       ├── r-claim-allowlist.yaml      # Spore intake protocol §2b
    │       └── bm.connection.rc-phase-2-program-guide.md  # day-1 seed bridge note
    └── workshops/
        └── README.md         # placeholder; zero packets at minimal skeleton
```

**Local foundation docs**: zero admitted at minimal-skeleton phase (mirrors bioregional-coordination ADR-0001 §Decision-(3)). Foundation-doc admission requires `ready_convergent` or `ready_with_tension` state from `convergence_export.py` per the Spore intake protocol convergence-readiness gate.

**Concepts-yaml**: NOT admitted (per `spore:ADR-0080` precedent followed by IC, PM, bioregional-coordination). May admit later if cross-repo translation pressure fires.

**Validator**: NOT implemented. Defer until pressure.

### (5) Cross-project learning-field registration

Wire as project_id `bm` in `~/projects/RegenAI/koi-processor/scripts/project_bridge_notes.py` PROJECTS dict from day 1, with `bridge_dir` pointing to this repo's `docs/research/connections/`. The `convergence_export.py` script automatically picks up `source_document LIKE 'bm.%%'` claims into field-family rollups.

Day-1 seed bridge note: `bm.connection.rc-phase-2-program-guide.md` — extracts source claims from RC Phase 2 Program Guide (local snapshot at `~/projects/SalishOakSeeds/docs/rc-phase-2-program-guide.md`).

GitHub-sensor RAG ingest path is **deferred**: personal_koi `github_repos` table is not present locally (migration 043 not applied). Cross-project integration via convergence-export pipeline is unaffected.

## Consequences

**Positive:**
- Clear identity: this is a peer canon repo specializing bioregional-coordination, not a fork or subordinate
- Resolves bioregional-coordination ADR-0001 §Parking-lot Q5 explicitly via operational-pressure earning-test
- Minimal-skeleton phase enables organic growth without premature canon ceremony
- Cross-citation at peer level preserves BKC's + SalishOakSeeds' existing identities
- Day-1 cross-project learning-field registration ensures bridge-note authorship participates in convergence rollup from start
- Future canon decisions follow Spore + bioregional-coordination ADR conventions

**Negative / open:**
- License is not yet decided (treat as all-rights-reserved by author until ADR-0002 ratifies; targeted within 4 weeks). Coordinate with bioregional-coordination's eventual license ADR so the two repos align.
- GitHub-sensor RAG ingest deferred — content of this repo will not appear in personal-KOI unified_search results until migration 043 applied locally. Bridge-note convergence path is unaffected.
- Cross-repo coordination machinery for bioregional-mapping ↔ BKC ↔ SalishOakSeeds is bridge-notes-and-operator-discretion. Steady-state machinery (per `spore:Thread-3 sibling-canon-coherence` parking) remains future work.
- Six-layer rubric is a heading set, not architectural commitment. RC's forthcoming Field Guide may use different layer names; layers re-cluster cheaply if RC framing wins out.

## Method-precedent contributions (preserved for future bioregional-mapping-side ADRs)

This ADR establishes:

1. **Q5-admission pattern**: parking-item-becomes-repo. bioregional-coordination ADR-0001 §Parking-lot anticipated this repo as one possible Q5 outcome; operational pressure (RC LHC Phase 2 + Tijn thread + practitioner-field signal) earned admission. Future bioregional-* sub-domain repos (e.g., bioregional-economics, bioregional-governance) follow the same pattern: anticipate-as-parking, admit-on-pressure.

2. **Day-1 cross-project learning-field registration as default**: unlike bioregional-coordination ADR-0001 which parked KOI integration (Q4), this repo wires the convergence-export integration on day 1 because the RC LHC Phase 2 timing makes bridge-note throughput operational from the start. Future canon repos with similar timing should default to day-1 learning-field registration.

3. **Source-snapshot pattern for private-source bridge notes**: when a bridge-note source is a private artifact (RC Mighty Network), local snapshot in a peer instance-family repo (SalishOakSeeds) becomes the cite-by-path canonical reference. This pattern lets bridge notes cite verifiable content even when canonical source is private.

## Parking lot (deferred per operator ratification)

- **License decision (ADR-0002 target)** — within 4 weeks; coordinate with bioregional-coordination license ADR
- **GitHub-sensor RAG ingest** — defer until migration 043 applied to personal_koi, OR until cross-project unified_search of canon-repo content earns admission
- **Workshop facilitation packets** — `docs/workshops/` empty until real workshop earns canonical articulation
- **Validator + concepts-yaml** — defer; admit when local citation discipline becomes load-bearing
- **Six-layer rubric canonization** — currently a heading set in project-vision.md; admit as foundation doc only after multi-bridge-note convergence (≥3 bridge notes ratifying or refining)
- **Layer-as-membrane / Story-of-Place / Workshop-as-Joint-Commitment / Field Guide as Reproduction specializations** — surfaced at vision layer; admit as foundation docs only when operational pressure earns admission
