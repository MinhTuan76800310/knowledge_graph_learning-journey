# Mechanism-KG Teaching Coverage Analysis

**Baseline:** HEAD `2a8123c` | **PDF:** 124 pages | **Date:** 2026-08-29
**Chapters covered:** 1–6 | **Transfer cells audited:** 31 | **Missing or superficial:** 29 of 31

---

## Executive Summary

The Mechanism Knowledge Graph — the book's stated capstone differentiator — has **NO continuous presence** across chapters 1–6. It appears as **three isolated bridge sections** (Ch4 §4.13, Ch5 §5.18, Ch6 §6.17) that do not reference each other, use **inconsistent object naming** (`DerivativeOperation` in Ch4 vs `MechanismOperation` in Ch5), and are each self-contained introductions rather than evolutionary steps. Chapter 1, 2, and 3 contain **zero** mechanism-domain examples.

**Coverage by chapter:**

| Chapter | Coverage % | Presence Type | Key Question Answered? |
|---------|-----------|---------------|------------------------|
| Ch1 | 0% | None | N/A — 0 MechKG questions posed in audit |
| Ch2 | 0% | None | **0 of 7 answered** |
| Ch3 | 0% | None (city/country only) | 0 of 4 fully (4 partial) |
| Ch4 | ~10% | Single bridge subsection (§4.13) | 2 of 7 partial, 5 missing |
| Ch5 | ~5% | Single bridge subsection (§5.18) | 0 of 7 answered |
| Ch6 | ~8% | Single example (§6.17), one claim | 1 of 5 partial |

---

## Chapter 1 — Recognize Mechanism as Domain Entity

| Concept | Current MechKG Example | Quality | Missing Transfer | Proposed MechKG Example |
|---------|----------------------|---------|------------------|------------------------|
| Graph | NONE | none | No mechanism node shown as graph vertex | 2–3 mechanism nodes with `requires` edges beside city graph |
| Triple | NONE | none | No mechanism assertion as triple | `(ex:newtonCooling_1, ex:hasOperation, ex:DerivativeOperation)` beside Hanoi triple |
| Entity | NONE | none | Mechanism not in four-layer entity model | Real-world mechanism → graph node → IRI → label, parallel to Hà Nội row |
| Data Graph | NONE | none | Mechanism graph not shown as "meaningless structure" | Add mechanism nodes to §1.6 Step 2 labeled-but-meaningless graph |
| Taxonomy | NONE | none | No mechanism class hierarchy | `Mechanism ⊑ Process`; `RateOfChangeMechanism ⊑ Mechanism` in Step 3 |
| Ontology | NONE | none | No mechanism axiom | §1.6 Step 4: `hasOperation` domain/range on mechanism classes |
| Knowledge Graph | NONE | none | **CENTRAL CONCEPT has zero MechKG** | Step 5: mechanism triple annotated with source + confidence + timestamp as full KG |
| Semantics | NONE | none | Mechanism semantics never demonstrated | Domain/range on `hasInput` deriving `:Quantity` type |
| Context | NONE | none | Mechanism claim context never shown | Attach provenance to mechanism assertion in Step 5 |
| Identity | NONE | none | Same mechanism, two textbooks, different IRIs | Self-check: can `ex:newtonCooling` and `wd:Q12345` denote same mechanism? |
| Assertion | NONE | none | Mechanism claim ≠ mechanism fact | §1.8 Misconception 4: textbook asserting RATE_OF_CHANGE ≠ accepted mechanism knowledge |

**Chapter 1 requirement:** Reader recognizes Mechanism as a first-class KG entity. **Currently absent entirely.**

---

## Chapter 2 — Represent Mechanism in RDF / Query Structure

| Concept | Current MechKG Example | Quality | Missing Transfer | Proposed MechKG Example |
|---------|----------------------|---------|------------------|------------------------|
| RDF Triple | NONE | none | RATE_OF_CHANGE never represented as RDF | Turtle: `ex:rateOfChange_1 rdf:type ex:Mechanism ; ex:hasOperation ex:DerivativeOperation .` |
| IRI | NONE | none | Which mechanism elements deserve IRIs vs literals | Mechanisms get IRIs (shared, referenced); thresholds `"0.05"^^xsd:decimal` are literals |
| Literal | NONE | none | When is a literal appropriate for mechanism properties | Rate constant as IRI vs threshold value as literal — when each is correct |
| Blank Node | NONE | none | Blank nodes break mechanism identity across merges | Warning: blank-node intermediate structures lose identity on import — use IRIs for DerivativeApplication |
| Graph Isomorphism | NONE | none | Merging mechanism KGs from two sources | Two textbook graphs describing same mechanism, checked for isomorphism |
| SPARQL Triple Pattern | NONE | none | No mechanism-domain pattern | `(?mech, ex:hasOperation, ?op)` finding all mechanisms with derivative operations |
| BGP | NONE | none | No multi-hop mechanism traversal | BGP chain: Mechanism → hasApplication → DerivativeApplication → differentiand → Quantity |
| LPG | NONE | none | No mechanism nodes in property graph | `(:Mechanism {name:"RATE_OF_CHANGE"})-[:hasOperation]->(:DerivativeOperation)` |
| Cypher | NONE | none | No mechanism query | `MATCH (m:Mechanism)-[:hasOperation]->(o:DerivativeOperation) RETURN m, o` |
| RDF vs LPG Tradeoffs | NONE | none | No mechanism-specific tradeoff analysis | RATE_OF_CHANGE as IRI (interoperable, needs reification for metadata) vs LPG node (properties natural, loses interop) |

**Ch2 requirement:** Reader can serialize and query mechanism structures in both paradigms. **Currently absent entirely — 0 of 7 key MechKG questions answered.**

---

## Chapter 3 — Identity + Contextualize Mechanism Claims

| Concept | Current MechKG Example | Quality | Missing Transfer | Proposed MechKG Example |
|---------|----------------------|---------|------------------|------------------------|
| Schema | NONE (city/country only) | none | No mechanism schema | `ex:hasOperation`, `ex:hasInput`, `ex:hasReferenceVariable` declarations |
| Schema Alignment | NONE | none | No mechanism schema alignment | Align `ex:hasOperation` (textbook A) with `textbookB:performs` (textbook B) |
| Identity Resolution | NONE (Hanoi vs wd:Q1858 only) | none | **No conceptual identity demonstration** | Two sources using different IRIs for Newton's law of cooling: `ex:newtonCooling` vs `tb:newton_1692` — evidence is definitional equivalence, not structural (population, label similarity) |
| owl:sameAs | NONE for concepts | none | **Similar-but-distinct concepts erroneously merged never shown** | "rate of change" vs "average rate of change" — the conceptual-identity danger case |
| Named Graph | NONE (ex:sourceA only) | none | Mechanism claims not separated by source | Named graph per textbook: `ex:textbookAGraph { ... mechanism assertions ... }` |
| N-ary Relation | NONE (CapitalStatus only) | none | DerivativeApplication not introduced as n-ary | **Promote Ch4 §4.13 warning-box sketch to Ch3**: DerivativeApplication as reified 4-ary relation binding differentiand + withRespectTo + operation |
| Qualifier | NONE (Wikidata only) | none | No general mechanism for when to use qualifiers vs n-ary | Mechanism claim with condition qualifier vs DerivativeApplication node |
| Integration Pipeline | NONE | none | No mechanism-source integration | Mini-case: two textbook mechanism KGs → schema alignment → identity → context → integrated mechanism graph |

**Ch3 requirement:** Reader can integrate mechanism knowledge from multiple sources. **Currently absent — all evidence types are geographic (population magnitude, label similarity); conceptual identity (definitional equivalence, shared derivation role) never demonstrated.**

---

## Chapter 4 — Formal Ontology / Classification

| Concept | Current MechKG Example | Quality | Missing Transfer | Proposed MechKG Example |
|---------|----------------------|---------|------------------|------------------------|
| Ontology | §4.13 RateOfChangeMechanism axiom (labeled "pedagogical toy") | superficial | What "ontology commitment" means for mechanism entities | Show what committing to the RateOfChangeMechanism definition commits you to |
| Interpretation | NONE for mechanisms (City/Country only) | none | **No Δ^I containing mechanism elements** | Parallel worked interpretation: Δ^I = {m₁, d₁, q₁, r₁}; DerivativeOperation^I = {⟨m₁,d₁⟩}; show satisfaction |
| Model | NONE for mechanisms | none | Which interpretations are models of mechanism axioms | One satisfying and one non-satisfying interpretation of the mechanism ontology |
| Entailment | Generic classification statement only | superficial | Concrete classification proof for mechanism individual | Given m with ∃hasOperation.DerivativeOperation, ∃hasInput.Quantity, ∃hasReferenceVariable.ReferenceVariable → m : RateOfChangeMechanism, step by step |
| Existential Restriction | Warning box only | adequate (warning) | **Formal two-model demonstration of scattered vs coherent fillers** | Model (a): fillers bound via DerivativeApplication witness; Model (b): fillers scattered across unrelated individuals — both satisfy flat definition, only (a) intended |
| OWA | NONE for mechanisms | none | What remains unknown about mechanisms under OWA | If m : Mechanism and ∃hasOperation.DerivativeOperation asserted but no operation named — what does OWA say? Can two mechanisms share one application? |
| Cardinality | NONE for mechanisms | none | Cardinality on mechanism properties | `hasOperation max 1` on a mechanism requiring multiple operations → apparent violation resolved by identity merging under no-UNA |
| Consistency/Satisfiability | NONE for mechanisms | none | Mechanism-specific inconsistency scenario | `DerivativeOperation ⊓ Quantity ≡ ⊥` accidentally asserted → all mechanisms unsatisfiable |
| OWL Profiles | NONE | none | Which profile suits Mechanism-KG | EL (class hierarchy + existential) fits mechanism classification; RL if rule-based materialization needed |

**Ch4 requirement:** Reader can construct interpretations and prove classification for mechanism individuals. **§4.13 exists but is isolated, labeled a toy, and never deploys the chapter's own machinery (interpretation, model, entailment) on the domain.**

---

## Chapter 5 — Infer + Validate CandidateMechanism

| Concept | Current MechKG Example | Quality | Missing Transfer | Proposed MechKG Example |
|---------|----------------------|---------|------------------|------------------------|
| Forward Chaining | §5.18 mentions transitive `requires` abstractly | superficial | No actual rule written with body/head over mechanism predicates | Rule: `(?m ex:requires ?m2), (?m2 ex:requires ?m3) → (?m ex:requires ?m3)` with multi-round θ trace |
| Substitution θ | NONE (Hanoi only) | none | **Zero substitution on capstone entities** | θ = {?m ↦ ex:newtonCooling, ?m2 ↦ ex:heatTransfer} applied to mechanism rule |
| Fixpoint | NONE | none | No mechanism-classification closure | Rounds: derive transitive requires, then RateOfChangeMechanism type, show fixpoint reached |
| Materialization | NONE (design question gestured) | superficial | No recommendation for mechanism domain | Materialize mechanism type classifications (small, stable); query-time for transitive requires (large, changing) |
| SHACL Shape | §5.20 Q3 exercise prompt only | superficial | No worked shape for MechKG structure in body text | CandidateMechanismShape: `sh:targetClass ex:CandidateMechanism; sh:property [sh:path ex:hasDefinition; sh:minCount 1]` with full target→focus→path→value→constraint→result walkthrough |
| Consistency vs Validation | NONE (City/Country only) | none | No MechKG scenario for two-axis independence | Ontology consistent but candidate mechanism graph violates ingestion policy (missing referenceVariable); converse case |
| Graph Repair | NONE (Hanoi/name only) | none | No mechanism repair scenario | CandidateMechanism missing `referenceVariable`: 5 candidate repairs (add link, reclassify, delete, flag Contested, accept exception) with semantic consequences |
| Soundness/Completeness | NONE | none | No mechanism reasoning guarantee analysis | OWL RL on mechanism classification: sound, complete under PR1 conditions |

**Ch5 requirement:** Reader can write rules and shapes over the Ch4 mechanism ontology. **§5.18 identifies right categories but remains at label/intuition level. Additionally uses `MechanismOperation` (naming break with Ch4) and introduces `Condition` without prior grounding.**

---

## Chapter 6 — Claim / Evidence / Provenance / Time

| Concept | Current MechKG Example | Quality | Missing Transfer | Proposed MechKG Example |
|---------|----------------------|---------|------------------|------------------------|
| Claim | §6.17 forward-chaining termination claim (one claim) | superficial | Single example only | 3 mechanism claims with full epistemic metadata (source, time, confidence type, governance state) |
| Evidence | §6.17 one source (Hogan et al.) | superficial | Evidence graph for mechanisms | Evidence relations between mechanism claims and textbook passages / experimental results |
| Provenance | §6.17 wasDerivedFrom on claim | superficial | CandidateMechanism entity never modeled | PROV-O chain: mechanism claim → derived from textbook section → attributed to authors → generated by extraction activity |
| Epistemic Model Pipeline | §6.17 final stage only | superficial | Pipeline from observation to accepted never traced for mechanisms | Full walkthrough: mechanism observation in textbook → RDF assertion → Claim object → evidence attachment → Accepted status |
| Contradiction Taxonomy | §6.17 scope disagreement only | superficial | 4 of 5 types never applied to mechanisms | All five: logical (contradictory preconditions), value (different rate constants), temporal (Newtonian vs relativistic), scope (different reference variables), source (two textbooks disagree) |
| **Temporal Validity** | **COMPLETELY ABSENT** | none | **Score 0 — single largest gap** | Newtonian mechanics → relativistic supersession: when was a mechanism's validity claim true? |
| Governance States | §6.17 one "Accepted" state shown | superficial | No transitions demonstrated | Transition diagram: Candidate → Accepted → Contested (new evidence) → Superseded (better model) |
| Bitemporal | NONE | none | No mechanism bitemporal query | "What did the system believe about Newton's second law at date T?" — retrospective query |
| Supersession | NONE for mechanisms | none | Algorithm version supersession | Revised algorithm supersedes old without old being wrong (better ≠ wrong) |
| CandidateKnowledge | §6.16 LLM protocol general | superficial | **"CandidateMechanism" appears nowhere** | LLM-extracted mechanism as CandidateMechanism: 4-step handling with independent verification |
| Source Reliability | NONE for mechanisms | none | Textbook vs paper vs LLM reliability | Reliability policy: peer-reviewed source > textbook > LLM extraction for mechanism claims |

**Ch6 requirement:** Reader can manage mechanism knowledge epistemically end-to-end. **§6.17 contains exactly one example referencing an external source (`ex:Hogan_et_al_2021`) rather than building on Ch4/Ch5's own objects.**

---

## Continuous Scenario Proposal

**Problem:** Currently three isolated bridge sections with no continuity. No persistent individuals exist across chapters. The planned infrastructure directories `datasets/mechanism_kg/` and `capstone/mechanism_knowledge_system/` (listed in CLAUDE.md) do not exist in the repo.

### Canonical Object Set (standardize across all chapters)

```
Classes:   ex:Mechanism, ex:RateOfChangeMechanism,
           ex:DerivativeApplication, ex:DerivativeOperation,
           ex:Quantity, ex:ReferenceVariable, ex:Condition,
           ex:CandidateMechanism (Ch5+)
Properties: ex:hasOperation, ex:hasApplication, ex:hasInput,
            ex:hasReferenceVariable, ex:differentiand,
            ex:withRespectTo, ex:requires
Individuals: ex:newtonCooling_1, ex:heatTransferRate_2 (persistent across chapters)
```

**Naming reconciliation:** Adopt `DerivativeOperation` (Ch4's name) as canonical. Ch5's `MechanismOperation` is a naming break — rename or add explicit reconciliation note. Never introduce a new name without linking to the prior chapter's object.

### Per-Chapter Evolution

| Ch | Capability | Concrete Additions |
|----|-----------|-------------------|
| **Ch1** | Recognize Mechanism as domain entity | §1.3 mechanism triple beside Hanoi; §1.6 Step 2 mechanism nodes; Step 5 annotated mechanism triple; §1.8 mechanism assertion ≠ accepted knowledge |
| **Ch2** | Serialize + query mechanism in RDF and LPG | §2.1.4 mechanism triples in Turtle; §2.1.6 SPARQL/BGP over mechanism domain; §2.2.4 same domain in LPG; §2.4 tradeoff paragraph |
| **Ch3** | Integrate mechanism knowledge across sources | §3.2 mechanism identity resolution (definitional evidence); §3.3.3 DerivativeApplication as n-ary (promote Ch4 sketch here); §3.4 mini-case: two textbook mechanism KGs integrated |
| **Ch4** | Formal classification of mechanisms | §4.3 parallel interpretation Δ^I = {m₁, d₁, q₁, r₁} (not only §4.13); §4.13 formalize DerivativeApplication in DL; two-model demonstration; OWA/satisfiability for mechanisms |
| **Ch5** | Infer + validate CandidateMechanism | §5.2 forward chaining with θ over mechanism IRIs; §5.6 CandidateMechanismShape in body text; §5.9 mechanism 2×2 scenario; §5.12 mechanism repair |
| **Ch6** | Epistemic management end-to-end | §6.17 expansion 3–5x: full pipeline, ≥3 mechanism claims, temporal validity (Newtonian→relativistic), governance transitions, bitemporal query |

### Infrastructure Requirements

1. Create `datasets/mechanism_kg/` with canonical Turtle files shared across chapters
2. Create `capstone/mechanism_knowledge_system/` as the evolving capstone domain
3. Make §5.18 and §6.17 open by explicitly citing the previous chapter's objects
4. Introduce `CandidateMechanism` as the named Ch5→Ch6 bridge (§5.18's validation target = §6.16's CandidateKnowledge protocol instance)

---

## Missing Transfer Summary

| Transfer Category | Ch1 | Ch2 | Ch3 | Ch4 | Ch5 | Ch6 |
|-------------------|-----|-----|-----|-----|-----|-----|
| Structural representation | ✗ | ✗ | ✗ | ~ | ✗ | ✗ |
| Query/retrieval | — | ✗ | — | — | ✗ | ~ |
| Identity/integration | — | ✗ | ✗ | ✗ | — | ✗ |
| Formal semantics | — | — | — | ~ | ✗ | — |
| Inference/validation | — | — | — | — | ✗ | — |
| Epistemic management | — | — | ~ | — | — | ~ |
| Temporal validity | — | — | ~ | — | — | ✗ (score 0) |

**Total: 29 of 31 transfer cells missing or superficial.**

| Priority | Action | Impact |
|----------|--------|--------|
| P0 | Create canonical object set + datasets/mechanism_kg/ | Enables all per-chapter additions |
| P0 | Add mechanism examples to Ch1 (recognition) and Ch2 (representation) | Closes 0% coverage in earliest chapters |
| P1 | Formalize DerivativeApplication in Ch3 (n-ary) and Ch4 (DL axioms) | Resolves scattered-filler flaw |
| P1 | Add CandidateMechanism SHACL shape + forward chaining to Ch5 body text | Makes validation/inference learnable for capstone |
| P1 | Expand Ch6 §6.17 to full pipeline with temporal validity | Delivers epistemic capstone payoff |
