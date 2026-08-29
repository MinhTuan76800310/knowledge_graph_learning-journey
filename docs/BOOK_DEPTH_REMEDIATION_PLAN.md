# Book Depth Remediation Plan

**Baseline:** HEAD `2a8123c` | **PDF:** `artifacts/depth-audit-baseline/` (124 pages) | **Date:** 2026-08-29
**Chapters:** 1–6 | **Concepts audited:** 112 | **Findings:** 57 (5 P0, 24 P1, 19 P2, 9 P3)

---

## Part 1: Top 15 Depth Gaps

Ranked by: (1) impact on understanding, (2) importance to Mechanism Knowledge System, (3) dependency on later chapters, (4) probability of reader misconception.

| Rank | Gap | Chapter | Why Critical | MechKG Criticality |
|------|-----|---------|--------------|---------------------|
| 1 | **Context (1/3 of KG = DG+S+C model) scores 2/5, no precise definition** | Ch1 | The book's core model has one placeholder pillar from the start | Blocking: epistemic management (§6) is impossible without a defined Context |
| 2 | **Knowledge Graph (central concept of the book) has zero MechKG application** | Ch1 | The concept the whole book is about is never instantiated on the capstone domain | Critical: defines what the book is about |
| 3 | **Ch2 answers 0 of 7 key MechKG questions** | Ch2 | Data models and query languages never touch the capstone domain | Critical: no bridge from representation to capstone |
| 4 | **Ch4 formal machinery (interpretation/model/entailment) never applied to mechanisms** | Ch4 | Reader can build interpretations for cities but not mechanisms | Critical: formal semantics must transfer |
| 5 | **Ch6 §6.17 is the sole capstone section, containing one example** | Ch6 | Capstone payoff never delivered | Critical: epistemic layer absent for mechanisms |
| 6 | **Temporal validity for mechanisms completely absent (score 0)** | Ch6 | No mechanism validity example (Newtonian→relativistic) | High: canonical temporal example for science knowledge |
| 7 | **Bitemporal is INTUITION only; no Turtle, no query** | Ch6 | Formal two-axis model + retrospective query missing | High: retrospective queries are a core epistemic feature |
| 8 | **Existential restriction flaw stated in a warning box but never formally demonstrated for mechanisms** | Ch4 | Reader must trust the warning; no two-model proof | High: the most common ontology modeling error |
| 9 | **DerivativeApplication never given DL axioms; sketch abandoned after Ch4** | Ch4 | The corrected model is never formalized, never promoted to Ch3 n-ary | High: reader is left without a correct working model |
| 10 | **SHACL shapes for CandidateMechanism exist only as exercise prompt** | Ch5 | Validation cannot be learned for the capstone domain | High: validation is a required capstone skill |
| 11 | **Graph repair has no MechKG scenario and no operational model** | Ch5 | All repair examples use Hanoi/name; no decision procedure | High: realistic maintenance scenario missing |
| 12 | **Ch5 §5.18 naming break: `MechanismOperation` vs Ch4 `DerivativeOperation`; `Condition` used untaught** | Ch5 | Cross-chapter object discontinuity + ungrounded vocabulary | High: breaks the evolving-scenario thread |
| 13 | **Ch3 conceptual identity never demonstrated** | Ch3 | All evidence types are geographic (population, label similarity); no definitional-equivalence case | High: the hardest identity cases (concepts, mechanisms) untouched |
| 14 | **Ch3 schema alignment shows the result, not the process** | Ch3 | Reader cannot perform alignment on a new source pair | High: integration pipeline is the Ch3 goal |
| 15 | **FILTER/OPTIONAL in Ch2 score 2/5 — evaluation semantics missing** | Ch2 | Common SPARQL pitfalls (unbound vars, left-outer-join) never taught | Medium: reader will write wrong queries |

---

## Part 2: All Findings Grouped by Severity

### P0 — BLOCKING UNDERSTANDING (5)

| # | Chapter/Section | Concept | Problem | Why Shallow | Missing Mechanism | Exact MechKG Example | Cross-Domain Example | Counterexample | Diagram | Reader Capability After Fix | Size |
|---|------------------|---------|---------|-------------|-------------------|----------------------|----------------------|----------------|---------|----------------------------|------|
| P0-1 | Ch1 §1.2/§1.6 Step 5 | Context | 1/3 of core model has no precise definition; Step 5 is ~3 lines | Label-only introduction despite Major status | How context is attached, queried, reasoned over; what is NOT context | Annotate `(ex:newtonCooling_1, ex:hasOperation, ex:DerivativeOperation)` with source + confidence + timestamp | Geo: `(Hanoi, capitalOf, Vietnam)` with provenance | Without context: cannot evaluate two conflicting mechanism claims | Data→Semantics→Context flow with mechanism triple | Distinguishes context from metadata/provenance | medium |
| P0-2 | Ch1 §1.6 | Knowledge Graph | Central concept has zero MechKG application | City-only worked example for the book's core concept | How KG structure supports mechanism reasoning end-to-end | Build a mini KG: mechanism → operation → application → quantity + taxonomy + source | Bio pathway KG | Treating a data graph as a KG (repeat §1.2 Case A/B for mechanisms) | Layered KG with mechanism at center | Builds a tiny MechKG from scratch | medium |
| P0-3 | Ch2 §2.1–§2.4 | RDF/SPARQL/LPG/Cypher | 0 of 7 key MechKG questions answered | Examples restricted to city/country | Bridge data-model teaching to capstone domain | Turtle + SPARQL + Cypher on RATE_OF_CHANGE; BGP chain Mechanism→hasApplication→DerivativeApplication→differentiand→Quantity; IRI-vs-literal policy; blank-node fragility note; RDF vs LPG tradeoff paragraph | Social network query patterns | What SPARQL returns when no mechanism has an operation | RDF and LPG side-by-side on the same mechanism data | Represents and queries mechanisms in both models | large |
| P0-4 | Ch4 §4.13 | Interpretation/Model for Mechanism-KG | Builds formal machinery for cities, never applies it to mechanisms | Self-contained geography examples | Δ^I, class extensions, property relations for mechanism entities | Δ^I = {m₁, d₁, q₁, r₁}; DerivativeOperation^I = {⟨m₁,d₁⟩}; Quantity^I = {q₁}; show satisfaction of RateOfChangeMechanism equivalence | Employee/Manager interpretation | An interpretation satisfying city axioms but not mechanism axioms | Parallel to City/Country figure | Constructs mechanism interpretations | large |
| P0-5 | Ch6 §6.17 | Full Epistemic Pipeline for Mechanisms | Single example in the sole capstone section | Insufficient depth for capstone payoff | Observation→Assertion→Claim→Evidence→Accepted for a mechanism | Walk `ex:newtonCooling_1` through all five stages with Turtle at each stage; ≥3 claims with full metadata | Clinical trial claim pipeline | Candidate claim that fails evidence check | Five-stage pipeline with mechanism instantiation | Manages mechanism knowledge epistemically | large |

### P1 — MAJOR DEPTH GAP (24)

| # | Chapter/Section | Concept | Problem | Why Shallow | Missing Mechanism | Exact MechKG Example | Cross-Domain Example | Counterexample | Diagram | Reader Capability After Fix | Size |
|---|------------------|---------|---------|-------------|-------------------|----------------------|----------------------|----------------|---------|----------------------------|------|
| P1-1 | Ch1 §1.3 | Semantics | Umbrella term never given a standalone precise definition | Defined only via its components (ontology/schema/constraint) | What semantics is as a layer, separate from its components | "Adding semantics" = giving `hasInput` domain/range so a reasoner can derive `:Quantity` type | DB NOT NULL vs RDFS domain | Two graphs with same structure, different semantics | Layer diagram with meaning pipeline | States what semantics adds over structure | small |
| P1-2 | Ch1 §1.5 | Graph | Formal model exists but no engineering consequence | D6/D7/D8 missing (no worked build, no failure counterexample, no consequence) | What changes in design decisions because graphs are formal | `(ex:newtonCooling_1, ex:requires, ex:heatTransfer)` as second worked graph beside Hanoi | Service dependency graph | Multi-edge/attribute limitation that G=(V,E) can't express | — | Justifies representation choice formally | small |
| P1-3 | Ch1 §1.3/§1.5 | Triple | No failure mode shown; n-ary deferred to §1.12/Ch3 | D7/D8 missing | When triple representation fails and why | Show n-ary gap with a mechanism expression (`dX/dt` needs >2 participants) | Purchase order with 3+ participants | Flat triple implying co-participation it cannot express | Binary vs n-ary comparison | Recognizes triple limits | small |
| P1-4 | Ch1 §1.6 | Data Graph | No engineering consequence; treated as "not yet KG" only | D8/D9 missing | What design decision changes when you know you have only a data graph | §1.6 Step 2: mechanism nodes in labeled-but-meaningless graph | Failed system treated as KG when only a data graph | System that queried labels as if they were semantics | — | Knows what a data graph can and cannot answer | small |
| P1-5 | Ch1 §1.6 | Ontology | No engineering consequence of adding an ontology | Step 4 compressed; no "how having one changes your architecture" | Mechanism-level domain/range inference | `hasOperation` domain/range on mechanism classes; swapped domain/range warning repeated for mechanisms | — | RDFS inferring wrong type from swapped domain/range | — | States what an ontology changes in a system | small |
| P1-6 | Ch2 §2.1.6 | FILTER | Score 2/5; evaluation semantics missing | FILTER defined only by example | FILTER applies to already-bound solution mappings after BGP; unbound variable behavior | FILTER `?rate > 0.05` on mechanism property | SQL WHERE | Unbound variable in FILTER silently eliminating results | Evaluation-order diagram | Avoids SPARQL filter pitfalls | small |
| P1-7 | Ch2 §2.1.6 | OPTIONAL | Score 2/5; left-outer-join never named | OPTIONAL defined only by example | Left-outer-join semantics; unbound variable handling; OPTIONAL+FILTER interaction | OPTIONAL mechanism label | SQL LEFT JOIN | FILTER inside vs outside OPTIONAL block giving different results | Inner vs outer join result tables | Writes correct optional patterns | small |
| P1-8 | Ch2 §2.1.6 | BGP | No counterexample for pattern sets | D7 missing | Cross-product when patterns share no variables; empty result when no consistent binding | Two BGPs with no shared variables over mechanism data | — | Accidental combinatorial explosion | Cross-product diagram | Predicts BGP join behavior | small |
| P1-9 | Ch3 §3.4 | Schema Alignment | Shows result (ex:capitalOf ↔ wdt:P36), not process | No criteria for discovering/validating/rejecting a mapping | How to detect, score, and reject candidate schema mappings | Align `ex:hasOperation` (textbook A) with `textbookB:performs` (textbook B) | — | Accepting a plausible-but-wrong mapping | Alignment decision flow | Performs alignment on new sources | medium |
| P1-10 | Ch3 §3.2 | Conceptual Identity | Identity evidence types are geographic-only | No worked example for abstract entities (concepts, mechanisms) | Definitional equivalence, shared derivation role, identical mathematical structure as evidence | `ex:newtonCooling` vs `tb:newton_1692`: candidate → definitional evidence → reviewed owl:sameAs | Two definitions of a software API | "rate of change" conflated with "average rate of change" (similar ≠ same) | Evidence-type checklist | Resolves conceptual identity safely | medium |
| P1-11 | Ch3 §3.3 | N-ary Relation / DerivativeApplication | 4-ary+ multi-participant relation never demonstrated; reification term never introduced | CapitalStatus is binary-at-core; Alice self-check is 3-ary person-centric | Genuinely multi-participant relation; reified edge does not assert | **Promote Ch4 §4.13 sketch to Ch3**: DerivativeApplication(differentiand, withRespectTo, operation) as 4-ary | Employment with role | Reified quadruple from which original triple is NOT entailed | 4-ary participant diagram | Models multi-participant relations | medium |
| P1-12 | Ch4 §4.3 | Mechanism Interpretation (parallel) | Interpretation taught exclusively on City/Country | No Δ^I with mechanism elements in the core section | Class extensions and property relations for mechanisms from the start | Add one non-geographic interpretation in §4.3: prove m₁ : RateOfChangeMechanism | — | — | Parallel figure to City/Country | Builds mechanism interpretations in §4.3 | medium |
| P1-13 | Ch4 §4.13 | Existential Restriction Binding | Warning stated, no formal demonstration | Reader must trust the warning box | Two-model demonstration of scattered vs coherent fillers | Model (a) fillers bound via DerivativeApplication witness; Model (b) fillers scattered across unrelated individuals — both satisfy the flat definition, only (a) intended | Project team membership | Flat ontology implying co-participation when it does not | Side-by-side model diagrams | Identifies when ∃R.C is insufficient | medium |
| P1-14 | Ch4 §4.13 | DerivativeApplication Axioms | Corrected model not formalized | Only prose sketch in a warning box | Full DL axiom set with intermediate node | `RateOfChangeMechanism ⊑ Mechanism ⊓ ∃hasApplication.(DerivativeApplication ⊓ ∃differentiand.Quantity ⊓ ∃withRespectTo.ReferenceVariable)`; show it blocks the scattered-filler countermodel | Purchase-order reification | Reified model that still scatters bindings | Reified structure diagram | Writes n-ary relation ontologies | medium |
| P1-15 | Ch4 §4.8/§4.9 | OWA + Consistency for Mechanisms | OWA consequences and inconsistency only shown for geography | No mechanism-domain application | What remains unknown under OWA; what mechanism inconsistency looks like | `DerivativeOperation ⊓ Quantity ≡ ⊥` → all mechanisms unsatisfiable (consistent-but-unsatisfiable); mechanism with no named operation under OWA | — | Unsatisfiable but consistent mechanism ontology | Reasoner report snippet | Debugs mechanism ontologies | small |
| P1-16 | Ch5 §5.2 | Forward Chaining for Mechanisms | Abstract mention; no concrete rule | Reader cannot instantiate | Full rule with body/head and θ over mechanism IRIs | `(?m ex:requires ?m2), (?m2 ex:requires ?m3) → (?m ex:requires ?m3)` with θ trace over ex:newtonCooling, ex:heatTransfer | Dependency resolution | Rule that fires but produces a wrong transitive closure | Fixpoint derivation trace | Derives transitive mechanism dependencies | medium |
| P1-17 | Ch5 §5.6 | CandidateMechanism SHACL Shape | Body text has no worked MechKG shape | Exercise prompt only | target→focus→path→value→constraint→result walkthrough | `ex:CandidateMechanismShape` requiring ≥1 definition, hasOperation, hasInput; full validation report on a mechanism data graph | PersonShape | Shape that passes but the candidate is semantically wrong | Shape-evaluation trace | Validates candidate mechanisms | medium |
| P1-18 | Ch5 §5.9/§5.12 | Consistency×Validation + Graph Repair for Mechanisms | No MechKG scenario for either concept | 2×2 matrix generic; repair examples use Hanoi/name | Operational repair model (ADD/DELETE/SHAPE-CHANGE, cost, revalidation) | CandidateMechanism missing `referenceVariable`: 5 candidate repairs (add link, reclassify, delete, flag Contested, accept exception) with semantic consequences; mechanism data for both off-diagonal 2×2 cells | — | Repair that makes the graph valid but factually wrong | Repair decision tree | Evaluates repair strategies | medium |
| P1-19 | Ch6 §6.7 | Temporal Validity for Mechanisms | Score 0 — completely absent | No mechanism-domain example | Valid time on mechanism claims; assertion time ≠ event time | Newtonian mechanics valid until 1905, relativistic correction from 1905; algorithm validity window per version | CEO tenure; law validity | Treating assertion time as event time | Mechanism validity timeline | Applies temporal clocks to scientific claims | medium |
| P1-20 | Ch6 §6.7 | Bitemporal Mechanism + Query | INTUITION only | No Turtle, no query | valid_time × system_time model with retrospective query | Turtle with OWL-Time valid_time + xsd datetime system_time; "What did the system believe about Newton's second law on 2025-01-01?" | Financial audit bitemporal | Confusing valid time with system time | Two-axis grid | Writes retrospective bitemporal SPARQL | medium |
| P1-21 | Ch6 §6.6 | Contradiction Taxonomy (all 5 types) | Only scope disagreement shown for mechanisms | 4 of 5 types never applied | Context alignment (4 dimensions) before declaring contradiction; per-type mapping | Logical (contradictory preconditions), value (different rate constants), temporal (Newtonian vs relativistic), scope (different reference variables), source (two textbooks disagree) | Drug-trial contradictions | Context disagreement vs true contradiction | Contradiction type matrix | Classifies mechanism contradictions | medium |
| P1-22 | Ch6 §6.1/§6.12/§6.16 | Observation + Governance FSM + Promotion Gates | Observation INTUITION only; states static; no CandidateMechanism promotion criteria | Pipeline stages uninstantiated | Observation→Assertion structure; state transitions; promotability gates | Raw benchmark log → `ex:measurement_42` assertion; Candidate→Accepted→Contested→Superseded for a mechanism claim; LLM extraction as CandidateMechanism with 4-step verification | Sensor ingestion; software bug lifecycle | Invalid transition: Rejected → Accepted without review | FSM diagram | Manages governance transitions | medium |
| P1-23 | Ch6 §6.17 | Epistemic Pipeline for Mechanism Claims | One claim only, referencing external source, not prior chapter objects | No continuity with Ch4/Ch5 objects | Mechanism claims anchored to book's own canonical objects | Expand §6.17: 3 mechanism claims with PROV-O, evidence graph linking claims ↔ textbook passages ↔ proofs | — | Claim with provenance but no evidence | Pipeline instantiated with mechanism claim | Runs epistemic pipeline end-to-end | medium |
| P1-24 | Book-wide | Object Naming + Dependency Fix | `MechanismOperation` vs `DerivativeOperation`; `Condition` untaught (Ch5 §5.18) | Cross-chapter discontinuity | Canonical object set; dependency invariant enforcement | Adopt `DerivativeOperation`; `MechanismOperation` as generalization note; gloss or ground `Condition` locally | — | — | Canonical object diagram | Names capstone objects consistently | small |

### P2 — SUPPORTING DEPTH GAP (19)

| # | Chapter/Section | Concept | Problem | Missing Mechanism | Exact MechKG Example | Counterexample | Size |
|---|------------------|---------|---------|-------------------|----------------------|----------------|------|
| P2-1 | Ch1 §1.3 | Property vs Relation | Property (Incidental, 1/5) never independently defined; never distinguished from relation | Definition + RDF-properties-are-predicates note | `ex:name` is a property; `ex:requires` is a relation | Relation treated as property | small |
| P2-2 | Ch1 §1.4/§1.5 | Constraint/Inference/Schema | Heavy forward-ref debt; no precise local labels | One-line local definitions with chapter pointers | Schema = expected structure; constraint = validation; inference = derivation | — | small |
| P2-3 | Ch2 §2.1.3 | Literal | No typed-literal discussion; no MechKG usage | xsd types, language tags, type-coercion pitfalls | `"0.05"^^xsd:decimal` as threshold literal vs IRI | String "8000000" vs integer comparison pitfall | small |
| P2-4 | Ch2 §2.1.5 | Graph Isomorphism | No LPG equivalence comparison; no complexity note | Practical limits (NP-complete, heuristics); LPG identity | Merging two textbook mechanism graphs | Raw set comparison fails | small |
| P2-5 | Ch2 §2.1.6 | Solution Mapping | Self-check question never answered in text | Local sufficiency fix | Why SPARQL returns mappings not lists (answer in-text) | — | small |
| P2-6 | Ch2 §2.1.6 | Join | No failed-join counterexample; implicit vs SQL JOIN not noted | Join failure + cross-product note | Join over shared `?mech` variable; failed join when no common binding | — | small |
| P2-7 | Ch3 §3.2.1 | Denotation | One-sentence definition; no mechanism for establishing/contesting | How denotation is asserted and can fail | Two IRIs denoting same mechanism contested by new evidence | — | small |
| P2-8 | Ch3 §3.2.5 | Canonical Identifier | No selection criteria, conflict resolution, lifecycle | Canonical identifier policy process | Choosing one mechanism IRI as canonical on merge | — | small |
| P2-9 | Ch3 §3.3.6 | Qualifier | Wikidata-only; no decision rule for qualifier vs n-ary vs named graph | Decision procedure | Mechanism claim with condition qualifier vs DerivativeApplication node | — | small |
| P2-10 | Ch3 §3.3.3 | Reification | Term never formally introduced (registry says mechanism-level in Ch3) | Name the pattern; reified ≠ asserted | Show the reification quadruple and why original triple is not entailed | — | small |
| P2-11 | Ch4 §4.7 | Property Semantics | List-like catalog; no reflexivity/irreflexivity/asymmetry/chains | Completeness + reasoning scenario | `requires` transitive chain; is `hasOperation` functional? | Reflexive `requires` self-loop | small |
| P2-12 | Ch4 §4.3 | Class Extension | C^I used throughout but never named | Name "class extension" explicitly | C^I for Mechanism = {m₁, m₂, …} in the parallel interpretation | — | small |
| P2-13 | Ch4 §4.10 | DL Intuition | Naming-level only; no subsumption-check intuition | One paragraph: check C ⊑ D via C ⊓ ¬D satisfiability | How a reasoner checks RateOfChangeMechanism ⊑ Mechanism | — | small |
| P2-14 | Ch4 §4.12 | OWL Profiles | Complexity claims without concrete constructs | Classify the chapter's own ontology under EL | CapitalCity/mechanism ontology under EL; which axiom forces leaving EL | Claiming RL always complete | small |
| P2-15 | Ch5 §5.2 | Grounding | Only implied by substitution; no standalone definition | Ground term = no variables; grounding as separate step | Grounding a mechanism rule's body before matching | Non-ground rule matched against ground facts | small |
| P2-16 | Ch5 §5.4 | Materialization | Comparison table without worked execution | Store closure; trace invalidation | Materialize mechanism type classifications; one update invalidating one triple | — | small |
| P2-17 | Ch5 §5.14 | SPARQL Entailment Regime | Regime table without demonstration | Two regimes on same graph give different answers | Same §5.3 graph under Simple vs RDFS regimes | — | small |
| P2-18 | Ch6 §6.11 | Confidence Semantics | Taxonomy only; `compositeConfidence ???` uncomputable | One concrete declared policy (weighted combination), labeled system policy | Confidence type for source vs claim vs extraction on a mechanism claim | Treating all confidence as probability | small |
| P2-19 | Ch6 §6.x | Source Reliability | Intuition only | Formal reliability scale storage on prov:Agent | Peer-reviewed > textbook > LLM extraction policy for mechanism claims | — | small |

### P3 — POLISH (9)

| # | Chapter/Section | Concept | Problem | Suggested Polish |
|---|------------------|---------|---------|-----------------|
| P3-1 | Ch1 §1.2 | Mermaid Diagram | Cross-layer arrows never explained | Add numbered annotations showing a triple flowing through layers |
| P3-2 | Ch1 §1.4 | Layer Stack | Visual implies hierarchy; text denies it | Show one triple transformed at each layer, or label as non-rigid |
| P3-3 | Ch1 §1.5 | KSE Notation | Orphan notation, never used again | Use KSE in Ch2/Ch6, or explicitly retire it |
| P3-4 | Ch3 §3.1.6 | Schema Strategies | Catalog without decision criteria | One-paragraph mini-case per strategy on the ex:/wd: sources |
| P3-5 | Ch4 §4.13 | Vague forward pointer | "capstone cuối sách" with no chapter number | Point to specific chapter number(s) |
| P3-6 | Ch6 §6.15 | Claim Ledger | No inter-layer data flow | Add one SPARQL traversing the three layers (governance → epistemic → data) |
| P3-7 | Ch6 §6.18 | Contradiction Pipeline | Steps never executed | Walk claim_A/claim_B through alignment→comparison→contextualization→flagging |
| P3-8 | Ch6 §6.14 | Temporal Entity | Never defined standalone | Define temporal entity with temporal extent |
| P3-9 | Book-wide | Concept Registry | Drift: subclass→Ch2 (untouched), domain_range→Ch2 (actual Ch1), claim/evidence first_mentioned:3 (actual Ch1 §1.8) | Correct entries; invariants tests will otherwise mask future debt |

---

## Part 3: Chapter Verdicts

| Chapter | Strongest Mechanism | Avg Depth | P0 | P1 | P2 | P3 | MechKG Coverage % | Verdict |
|---------|---------------------|-----------|----|----|----|----|--------------------|---------|
| Ch1 | Entity/KG (4) — four-layer model + formal K ⊆ V×L×V | 2.7 | 2 | 5 | 2 | 3 | 0% | **MAJOR GAPS** — central concept unanchored |
| Ch2 | RDF Triple/IRI/LPG/Internal ID/Tradeoffs (4) | 3.1 | 1 | 3 | 4 | 0 | 0% | **MAJOR GAPS** — no capstone bridge, 0/7 MechKG questions |
| Ch3 | Identity/sameAs/UNA/NamedGraph/N-ary (4) | 2.9 | 0 | 3 | 4 | 1 | 0% | **MAJOR GAPS** — identity is geographic-only; no MechKG transfer |
| Ch4 | Interpretation/Model/Entailment/Necessary-Sufficient/OWA (5) | 4.3 | 1 | 4 | 4 | 1 | ~10% | **TARGETED REMEDIATION** — formal excellence, MechKG transfer missing |
| Ch5 | OWL vs SHACL Independence (5) | 3.5 | 0 | 3 | 3 | 0 | ~5% | **TARGETED REMEDIATION** — rules/shapes strong, no capstone examples |
| Ch6 | Claim/Evidence/Epistemic Model/PROV-O (4) | 3.1 | 1 | 5 | 2 | 3 | ~8% | **MAJOR GAPS** — temporal validity absent (score 0), §6.17 underdeveloped |

**Whole-book summary:**
- Total concepts audited: 112 (66 Major, 42 Supporting, 4 Incidental)
- Mean depth score: 3.3
- Score distribution: 5 (9%), 4 (35%), 3 (38%), 2 (15%), 1 (4%), 0 (0%)
- Findings: 57 (P0 5, P1 24, P2 19, P3 9)
- Major concepts without MechKG application: **18 of 66** (27%); Supporting without: 40 of 42
- MechKG transfer cells missing/superficial: **29 of 31** (94%)
- Continuous MechKG scenario: **NONE** — isolated snippets only; object naming inconsistent

---

## Part 4: Whole-Book Verdict

**Verdict:** `TARGETED_REMEDIATION_REQUIRED`

**Rationale:**
- Formal foundations in Ch4 (4.3 avg) and Ch5 (3.5 avg) are strong and well-cited. The interpretation→model→entailment pipeline, OWA trichotomy, forward-chaining recurrence, and SHACL walkthrough are textbook-quality.
- Ch1–Ch3 and Ch6 fail to provide capstone continuity: 0% MechKG coverage in the first three chapters, 94% of transfer cells missing or superficial.
- The central concept (Knowledge Graph) and the central object set (Mechanism-KG) are absent from exactly the chapters where they should be introduced (Ch1) and reinforced (Ch2–Ch3).
- The single largest structural problem is that the book's own formal machinery (interpretations in Ch4, rules/shapes in Ch5, epistemic pipeline in Ch6) is never deployed on the mechanism domain the book promises to teach.

**Not `MAJOR_DEPTH_REWORK_REQUIRED` because:**
- Existing formal content is sound; no chapter needs structural reorganization.
- The gaps are primarily **additive** (new MechKG examples, bridge sections, parallel worked interpretations, counterexamples) rather than corrective (rewriting incorrect content).
- All P0 items are expansion tasks, not repairs of broken pedagogy.

---

## Part 5: Recommended Remediation Order

### Phase 1 — Critical MechKG Foundations (Weeks 1–2)
1. **Create infrastructure:** `datasets/mechanism_kg/` + `capstone/mechanism_knowledge_system/` with canonical Turtle; freeze canonical object set (`DerivativeOperation`, `CandidateMechanism`, persistent individuals)
2. **Ch1 §1.6 (P0-1, P0-2):** Add mechanism triples to running example; annotate with context in Step 5
3. **Ch2 §2.1 & §2.4 (P0-3):** Add parallel mechanism-domain Turtle, SPARQL, BGP, and Cypher examples

### Phase 2 — Formal Transfer (Weeks 3–4)
4. **Ch4 §4.3 & §4.13 (P0-4, P1-13, P1-14):** Parallel mechanism interpretation; formalize DerivativeApplication; two-model demonstration
5. **Ch5 §5.2 & §5.6 (P1-16, P1-17):** Mechanism forward-chaining θ trace + CandidateMechanism SHACL shape in body text
6. **Ch5 §5.9/§5.12 (P1-18):** Mechanism repair scenario + 2×2 instantiation

### Phase 3 — Epistemic Layer (Weeks 5–6)
7. **Ch6 §6.17 (P0-5, P1-23):** Expand 3–5x with full pipeline, ≥3 mechanism claims, provenance, governance transitions
8. **Ch6 §6.7 (P1-19, P1-20):** Mechanism temporal validity (Newtonian→relativistic) + bitemporal query
9. **Ch6 §6.6 (P1-21):** Apply all 5 contradiction types to mechanisms

### Phase 4 — Integration & Polish (Week 7)
10. **Ch3 (P1-9, P1-10, P1-11):** Conceptual identity + schema alignment process + DerivativeApplication promoted to n-ary section
11. **Cross-chapter (P1-24):** Standardize object names; fix §5.18 `Condition`/`MechanismOperation`; add explicit forward/backward references between MechKG sections
12. **All chapters:** Add diagrams from Visual-Explanation Audit; resolve explanation-theater items T1–T14
13. **Registry (P3-9):** Correct concept_registry.yaml entries
14. **Review:** Re-run depth matrix; target all Major concepts ≥4 and all MechKG transfers ≥ adequate

---

## Part 6: Go/No-Go for Next Chapter

**Recommendation:** `CONDITIONAL_GO`

**Conditions:**
- Before starting Chapter 7, complete Phase 1 (items 1–3) and at minimum the Ch6 §6.17 expansion (item 7). Otherwise later chapters will build on a capstone foundation that does not yet exist.
- Ch7 (entity resolution algorithms) must open by referencing the canonical object set and the identity pipeline taught in Ch3.
- New chapters must continue the Mechanism-KG thread: every chapter adds at least one mechanism-domain worked example.

**No-Go if:**
- Any P0 gap remains unaddressed after the remediation period.
- New chapters continue to use city/country as the sole example without mechanism-domain transfer.
- The naming break (`MechanismOperation` vs `DerivativeOperation`) is not reconciled before Ch7 depends on it.
