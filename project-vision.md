---
doc_id: bioregional-mapping.project-vision
doc_kind: vision
status: draft
depends_on:
  - bioregional-coordination.project-vision
  - bioregional-coordination.canon-decision.repo-identity-and-spore-relationship
  - spore.project-vision
  - spore.positioning.agentic-bioregionalism
relates_to:
  - spore.federation-protocol
  - spore.mycelial-holarchy-architecture
  - spore.maintenance-economics
  - spore.docs.research.planning.learning-field-protocol-v1
  - spore.docs.research.planning.learning-field-intake-protocol-v1
date: 2026-05-04
author: darren-zal
---

# bioregional-mapping — Project Vision

## Intended audience and scope

- **Audience**: contributors who already work with bioregional-coordination (or are willing to read it as upstream context, alongside Spore as upstream root) and who are working on bioregional mapping practice at the canon-bearing layer rather than the deployment layer
- **Prerequisites**: comfort reading canon docs across canon-bearing repos and following links between vision, foundations, protocols, and ADRs; familiarity with the bridge-note schema and convergence-export pipeline; this document assumes coordination + governance + mapping vocabulary rather than introducing it from first principles
- **Scope**: states what bioregional-mapping is for, names the multi-layer mapping rubric as the framing this repo specializes from upstream canon, articulates how upstream primitives apply at mapping practice, names BKC + SalishOakSeeds as peer instance-family members, and parks foundation-doc content per inherited discipline
- **Out of scope**: bioregional-mapping content (mapping data, workshop outputs, monitoring records, pilot deployments — those live in instance-deployments like BKC + SalishOakSeeds + future hub repos); foundation-doc content (admit only when operational pressure surfaces); deployment infrastructure; license decision (deferred to ADR-0002)

## What this repo is

A canon-bearing repository for **bioregional mapping practice** as multi-layer mapping-as-coordination. The practice spans at least six layers in active practitioner work:

- **Relational / warm data** — stakeholder networks, trust relationships, who's already gathering, attendance histories
- **Cultural / Indigenous** — sovereign territory, knowledge holders, ceremony, Story of Place, traditional ecological knowledge
- **Ecological** — watersheds, species, ecosystem function, remote sensing, ecological monitoring
- **Economic / financial** — commitments, flow funding, BioFi, capital stewardship, regional currencies
- **Governance** — boundaries, Rights of Nature, decision authority, polycentric governance, treaty-witnessing
- **Geospatial / cartographic** — the layer most external mapping tools focus on (Felt, QGIS, regenatlas, Kumu, etc.) but only one of six

The conceptual umbrella is **bioregional mapping practice**, situated within "agentic bioregionalism" (canonized at Spore via [`spore.positioning.agentic-bioregionalism`](https://github.com/DarrenZal/spore/blob/main/docs/positioning/agentic-bioregionalism.md)) and via the bioregional-coordination peer canon ([`bioregional-coordination.project-vision`](https://github.com/DarrenZal/bioregional-coordination/blob/main/project-vision.md)). This repo hosts the **canon-bearing structure** for the multi-layer mapping framing: doctrine that is mapping-practice-specific (when it earns admission), local patterns, instance-family registrations, and bridge-note indexes of external practitioner work.

This is canon, not content. Bioregional-mapping content (specific maps, specific workshop outputs, specific monitoring records) lives in instance-deployments — BKC pilots, SalishOakSeeds (Victoria), future hub repos. This repo holds the structural articulation that lets such content be coordinated across deployments.

## What this repo is *not*

- **Not Spore.** Spore is upstream root; this repo cites Spore transitively via bioregional-coordination, directly when bioregional-coordination's specialization is silent.
- **Not bioregional-coordination.** bioregional-coordination is the agentic-bioregionalism frame; this repo is the mapping-sub-domain specialization. Cross-citation is at peer level (within the same canon-citizenship layer); neither subsumes the other.
- **Not BKC.** BKC is the operational deployment of the seven-layer stack (workshop → graph → pool → flow-funding → AI agents → federation → BFFs) including mapping pipelines, knowledge-graph integration, and entity resolution. BKC retains its existing identity. Cross-citation at peer level — neither subsumes the other.
- **Not SalishOakSeeds.** SalishOakSeeds is the Victoria pilot instance applying mapping canon to a specific landscape. Pilot content stays there; canon stays here.
- **Not a content repo.** Bioregional-mapping content lives in instance-deployments.
- **Not a host for the RC Bioregional Mapping Field Guide.** RC's Field Guide (publication target April 10, 2026, Regenerate Cascadia / Department of Bioregion 501(c)(3)) is RC's canonical content; this repo bridge-notes the Program Guide and the Field Guide when published.
- **Not yet a federation participant.** Cross-project integration is via the convergence-export pipeline (bridge notes → claims); KOI-net federation is deferred.

## The conceptual frame: bioregional mapping as multi-layer practice

Joe Brewer (responding to Tijn Tjoelker's 2026-05-04 LinkedIn query about bioregional mapping platforms): *"When you think of bioregional mapping as so much more than geospatial, it begins to open up into social mapping processes that are much more intimate and place-specific."*

The **multi-layer mapping rubric** treats bioregional mapping as a coordination shape: a practice through which a community of stakeholders collectively makes a place legible to itself, across multiple ways of seeing, in service of place-based action and decision-making. The six layers above are not exhaustive and not architecturally hard — they are headings that organize ongoing practitioner work. RC's Phase 2 Program Guide names a similar set ("physical, ecological, social, cultural, economic, and regenerative"); BioKulture's blue paper (Zenodo 10.5281/zenodo.16656790) names yet another set centering Indigenous-led BioKulture engineering. **Layer naming is provisional; layer multiplicity is canonical.**

This repo's reason for existing is to host the canon-bearing structure of the multi-layer mapping framing at the layer where mapping-specific operational concerns earn local doctrine when bioregional-coordination's general grammar does not cover them.

## How upstream primitives specialize at mapping practice

This is meta-articulation; foundation-doc content for mapping-specific specialization admits only when operational pressure earns admission per inherited Spore + bioregional-coordination discipline. At meta-articulation level, the candidate specializations are:

**Layer-as-membrane.** Each of the six mapping layers is a permeable boundary that filters and admits different signal types — relational data into warm data (gossip, history, who-knows-whom); cultural data into ceremony-attentive surfaces (consent-gated, honor-the-source); ecological data into measurement-attentive surfaces (sensors, monitoring, GIS layers); etc. Spore's permeability + double-boundary distinction ([`spore:ADR-0053`](https://github.com/DarrenZal/spore/blob/main/docs/research/canon-decisions/0053-glossary-refinements-bundled.md)) covers this. Membranes are self-produced through stewardship labor (the workshop facilitator labor of holding a layer's container) and sometimes text-authoritative through declared workshop scope or charter agreements.

**Story-of-Place as Field manifestation.** RC's Phase 2 Program Guide treats Story of Place as the central output: *"the workshop you host opens a door to new/old ways of exploring 'right relationship' together. Who walks through that doorway, and what grows from the relationships and sharing of experience and knowledge, is the real work and the real 'output'."* In Spore terms: Story of Place is the persistent Field that the workshop's bounded process generates — a holon-attached coordination substrate that participants and future stewards can place themselves within, contribute to, and inherit. Field-as-Story-of-Place is co-presence-mode at the workshop and async-contribution-mode after.

**Workshop-as-Joint-Commitment.** A bioregional mapping workshop is a multi-party-simultaneous joint commitment: stakeholders (community, partner organizations, Indigenous knowledge holders, local officials, regional funders) commit jointly to attend to a shared place across their differences. Spore's joint-commitment primitive ([`spore:ADR-0050`](https://github.com/DarrenZal/spore/blob/main/docs/research/canon-decisions/0050-sociality-side-b-plus-primitive.md)) is paradigm-case-load-bearing here. Asymmetric-joint-commitment ([`spore:ADR-0061`](https://github.com/DarrenZal/spore/blob/main/docs/research/canon-decisions/0061-asymmetric-joint-commitment-slug-disposition.md)) is operationally common: workshops carry asymmetric vulnerability between Indigenous knowledge holders (whose knowledge is at risk of extraction) and other participants.

**Field Guide as Reproduction artifact.** RC's Field Guide for Landscape Stewards (training-the-trainers manual) is the Reproduction primitive in operation — the mechanism by which mapping practice transmits across LHC cohorts, hubs, and bioregions. Spore's reproduction-continuity primitive ([`spore:ADR-0049`](https://github.com/DarrenZal/spore/blob/main/docs/research/canon-decisions/0049-reproduction-continuity-primitive-admission.md)) covers this; bioregional-mapping context exercises it heavily because the practice is inherently multi-generational (Indigenous traditional ecological knowledge transmission spans generations, not workshop cycles).

**Holon at multi-scale mapping.** Sub-watershed → watershed → coastal zone → ecoregion → biogeographic realm operationally appear in mapping workshops. Indigenous nations are holons at their own scales, often spanning multiple bioregional polities. CommitmentPools (BKC) are smaller holons within these. Mapping workshops choose a focal holon (a Greater Victoria, a Boulder, a Sierra Nevada de Santa Marta) but compose with adjacent and nesting holons explicitly.

These specializations admit local doctrine here only when operational pressure surfaces gap that bioregional-coordination + Spore canon does not cover. At minimal-skeleton phase, the specializations are surfaced at vision layer; foundation-doc admission earns its way per inherited discipline.

## Peer relationship to BKC + SalishOakSeeds

Both BKC and SalishOakSeeds are **peers at the instance-family layer** with bioregional-mapping. Neither downstream of this repo; this repo not downstream of either.

**BKC** is the operational deployment of the seven-layer stack (workshop → graph → pool → flow-funding → AI agents → federation → BFFs). It includes mapping pipelines (entity resolution, KOI graph, ontology, federation runtime in Octo, on-chain claims) that *operate at the mapping practice* without owning the canon framing. BKC's existing canonical docs (`bioregional-mapping-model-v0.1.md` and `bioregional-mapping-intake-contract-v0.1.md` at `BioregionalKnowledgeCommoning/docs/foundations/`) own the *operational ontology and intake contract* layers. This repo bridge-notes them and adds the canon-framing layer they ride within.

**SalishOakSeeds** is Darren's Victoria Landscape Group operational arm for RC LHC Phase 2 — the workshop-prep and coordination layer for the Victoria bioregional mapping workshop (June–July 2026). SalishOakSeeds owns Victoria-specific operational content (workshop design v2, RC funding proposal, participant outreach, etc.). This repo bridge-notes SalishOakSeeds work and abstracts mapping methodology where it generalizes across hubs.

Cross-citation between the three repos is via bridge notes; no alignment ADRs.

## Aspects the broader frame holds

The mapping practice composes with adjacent practices held by sibling repos and external work:

- **Knowledge commoning** — BKC's primary aspect; mapping outputs become structured records that flow into BKC's KOI graph (entity resolution, claims, evidence)
- **Capital allocation** — Hub Cultivator + TBFF (BKC's capital-layer work); mapping outputs surface offers/needs/commitments that feed pool routing and flow funding
- **Indigenous-led governance** — BioKulture engineering (WarīNkwī Flores et al, blue paper Zenodo 10.5281/zenodo.16656790); mapping practice must defer to Indigenous-led data governance and FPIC at every layer that touches sovereign territory or knowledge holders
- **External tooling ecosystem** — Felt, QGIS, regenatlas.xyz, Kumu, Miro, PamPam, Notion, Hylo, Restor, Open Impact, OMNI-Mapping, MAP (Memetic Activation Platform), Speak for the Trees, water-bioregion (Aaron Neyer), and many others surfaced in the Tijn Tjoelker LinkedIn thread (2026-05-04). These compose at the geospatial layer (and adjacent) without subsuming the multi-layer practice.

## Coordination substrate (upstream)

The substrate this repo composes with comes from bioregional-coordination + Spore canon. Direct upstream dependencies (cited by ADR / doc_id, not by commit SHA):

| Surface | Why load-bearing |
|---|---|
| `bioregional-coordination.project-vision` | Nearest upstream peer; the agentic-bioregionalism frame this repo specializes |
| `bioregional-coordination.canon-decision.repo-identity-and-spore-relationship` | The ADR whose §Parking-lot Q5 triggers this repo's admission |
| [`spore.positioning.agentic-bioregionalism`](https://github.com/DarrenZal/spore/blob/main/docs/positioning/agentic-bioregionalism.md) | Conceptual frame canonized at Spore positioning layer |
| [`spore.federation-protocol`](https://github.com/DarrenZal/spore/blob/main/docs/foundations/federation-protocol.md) | Membrane semantics; permeability discipline applied at layer-as-membrane |
| [`spore.mycelial-holarchy-architecture`](https://github.com/DarrenZal/spore/blob/main/docs/foundations/holonic-network-architecture.md) | Multi-scale holon nesting in mapping workshops |
| [`spore.maintenance-economics`](https://github.com/DarrenZal/spore/blob/main/docs/foundations/maintenance-economics.md) | Care, provisioning, maintenance, translation labour categories that appear in mapping facilitation work |
| [`spore.docs.research.planning.learning-field-protocol-v1`](https://github.com/DarrenZal/spore/blob/main/docs/research/planning/learning-field-protocol-v1.md) | Authoritative learning-field protocol; this repo participates as project_id `bioregional-mapping` |
| [`spore.docs.research.planning.learning-field-intake-protocol-v1`](https://github.com/DarrenZal/spore/blob/main/docs/research/planning/learning-field-intake-protocol-v1.md) | Authoritative bridge-note intake protocol |

Other upstream primitives, doctrines, modes, properties, derived glossary slugs, patterns, and ADRs are available as substrate; this repo cites them as operational pressure surfaces specific concerns.

## Working method

This repo inherits Spore + bioregional-coordination canon-rebuild-arc method discipline:

- **Audit-then-propose** at Step 0.5 of any planning work
- **Earning-test discipline** for canon admission (parsimony at object level; elegance at canon-pattern level; honest-rigor cluster-counting verdict-neutral)
- **Decline-shapes catalogued** — admit, decompose-as-framing-note, decline-with-evidence-triggers, decline-inline-prose-only, scope-condition, sufficient-spec-prose-as-defer-rationale
- **Cascade-miss discipline** at four observed layers
- **Future-doctrine markers held** — local foundation docs / patterns / ADRs admit only when operational pressure surfaces

## Current state (2026-05-04)

- **Phase**: minimal skeleton (created 2026-05-04); zero local foundation docs admitted; ADR-0001 ratifies repo identity
- **Day-1 seed bridge note**: `bioregional-mapping.connection.rc-phase-2-program-guide` (RC LHC Phase 2 Program Guide; 10 source claims extracted)
- **Validator**: not yet implemented (defer until pressure)
- **Concepts-yaml**: not admitted (per `spore:ADR-0080` precedent followed by IC, PM, bioregional-coordination)
- **Frozen-vocabulary.yaml**: ~25 entries seeded from RC Phase 2 + Tijn thread + BKC ontology subset (Spore intake protocol §2a)
- **R-claim-allowlist.yaml**: `bioregional-mapping.project-vision` and ADR-0001 doc_id as initial targets
- **Cross-repo citations** all by ADR number / doc_id (not commit SHA)
- **License**: TBD (parked; ADR-0002 targeted within 4 weeks)
- **Cross-project learning-field**: registered as project_id `bioregional-mapping` in `koi-processor/scripts/project_bridge_notes.py` PROJECTS dict
- **GitHub-sensor RAG ingest**: deferred (personal_koi `github_repos` table not present locally)

## Sources + cross-references

- [`bioregional-coordination.project-vision`](https://github.com/DarrenZal/bioregional-coordination/blob/main/project-vision.md) — agentic-bioregionalism frame this repo specializes
- [`bioregional-coordination:ADR-0001`](https://github.com/DarrenZal/bioregional-coordination/blob/main/docs/research/canon-decisions/0001-repo-identity-and-spore-relationship.md) §Parking-lot Q5 — the parking item this repo's existence resolves
- [`spore.positioning.agentic-bioregionalism`](https://github.com/DarrenZal/spore/blob/main/docs/positioning/agentic-bioregionalism.md) — conceptual frame
- [`bioregional-mapping:ADR-0001`](./docs/research/canon-decisions/0001-repo-identity-and-bregion-coord-relationship.md) — repo identity + bioregional-coordination peer relationship ratification
- RC LHC Phase 2 Program Guide — local snapshot at `~/projects/SalishOakSeeds/docs/rc-phase-2-program-guide.md`; canonical source: Regenerate Cascadia Mighty Network (private)
- Tijn Tjoelker LinkedIn thread, 2026-05-04 — wider practitioner field signal
- BioKulture blue paper (WarīNkwī Flores et al), Zenodo 10.5281/zenodo.16656790 — Indigenous-led BioKulture engineering frame
- [BKC](https://github.com/LinuxIsCool/BioregionKnwoledgeCommons) — peer instance-family member; operational seven-layer stack
- SalishOakSeeds (`~/projects/SalishOakSeeds/`) — peer instance-family member; Victoria pilot operational arm
- [Spore](https://github.com/DarrenZal/spore) — upstream root coordination grammar
- [bioregional-coordination](https://github.com/DarrenZal/bioregional-coordination) — nearest upstream peer
