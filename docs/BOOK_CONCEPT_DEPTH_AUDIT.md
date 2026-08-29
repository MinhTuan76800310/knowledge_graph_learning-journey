# Book Concept Depth Audit

**Baseline:** HEAD `2a8123c` | **PDF:** `artifacts/depth-audit-baseline/knowledge-graph-book-depth-audit-baseline.pdf` (124 pages) | **Total lines:** 5,452 | **Date:** 2026-08-29
**Chapters audited:** 1–6 | **Concepts audited:** 112 (66 Major, 42 Supporting, 4 Incidental)

---

## 1. Summary Matrix

Legend: ✓ = present, ✗ = missing, ~ = partial. Score: 0–5 (see §7 of BOOK_PEDAGOGY.md). Severity: P0/P1/P2/P3.

### Chapter 1 (16 concepts)

| Concept | Class | Score | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | D11 | D12 | Sev | Action |
|---------|-------|-------|----|----|----|----|----|----|----|----|----|-----|-----|-----|-----|--------|
| Graph | M | 3 | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | P1 | Add eng. consequence + MechKG triple |
| Triple | M | 3 | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | P1 | Add failure mode (n-ary) + MechKG |
| Entity | M | 4 | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ | ~ | ✗ | ✓ | ✗ | P2 | Add MechKG entity resolution sketch |
| Relation | S | 2 | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | P2 | Distinguish from property/predicate |
| Data Graph | M | 3 | ✓ | ✓ | ✓ | ✗ | ~ | ~ | ✓ | ✗ | ✗ | ✗ | ~ | ✗ | P1 | Add eng. consequence + non-geo example |
| Taxonomy | S | 3 | ✓ | ✓ | ✓ | ✗ | ✓ | ~ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | P3 | Adequate for supporting |
| Ontology | M | 3 | ✓ | ✓ | ✓ | ~ | ✓ | ~ | ✓ | ✗ | ✗ | ✗ | ~ | ✗ | P1 | Add eng. consequence + MechKG link |
| Knowledge Graph | M | 4 | ✓ | ✓ | ✓ | ~ | ✓ | ✗ | ✓ | ~ | ~ | ✗ | ✓ | ✗ | P1 | NO MECHKG FOR CENTRAL CONCEPT |
| Semantics | M | 3 | ✓ | ✓ | ~ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | P1 | Needs standalone precise definition |
| Context | M | 2 | ✓ | ✓ | ~ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | P0 | Weakest Major; 1/3 of core model |
| Identity | S | 3 | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ | ~ | ✗ | ✓ | ✗ | P3 | Adequate for supporting |
| Constraint | S | 2 | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ~ | ✗ | ✗ | ✗ | ✗ | ✗ | P2 | Heavy forward-ref debt to Ch5 |
| Inference | S | 2 | ✓ | ✓ | ✗ | ✗ | ✗ | ~ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | P2 | Heavy forward-ref debt to Ch4 |
| Assertion | S | 3 | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ | P3 | Good within §1.8 |
| Property | I | 1 | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | P2 | Never independently defined |
| Schema | S | 2 | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | P2 | Never precisely defined |

### Chapter 2 (17 concepts)

| Concept | Class | Score | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | D11 | D12 | Sev | Action |
|---------|-------|-------|----|----|----|----|----|----|----|----|----|-----|-----|-----|-----|--------|
| RDF Triple | M | 4 | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P1 | Add MechKG RDF representation |
| IRI | M | 4 | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P1 | Add MechKG IRI policy |
| Literal | S | 3 | ✓ | ✓ | ✓ | ~ | ✗ | ✓ | ✗ | ✗ | ~ | ✗ | ~ | ~ | P2 | Add typed literals + MechKG usage |
| Blank Node | M | 3 | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ~ | ~ | ✗ | ✓ | ✓ | P1 | Add MechKG identity fragility note |
| Serialization | S | 3 | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ~ | ✗ | ✓ | ✓ | P3 | Adequate |
| Turtle | S | 3 | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ | ✓ | P3 | Adequate |
| Graph Isomorphism | M | 3 | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ~ | ✗ | ✗ | ✗ | ~ | P2 | Add LPG equivalence comparison |
| SPARQL Triple Pattern | M | 3 | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ~ | ~ | ✗ | ~ | ✓ | P1 | Add MechKG SPARQL pattern |
| BGP | M | 3 | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✗ | ~ | ~ | ✗ | ~ | ✓ | P1 | Add cross-product counter + MechKG BGP |
| Solution Mapping | M | 3 | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ~ | ✗ | ✗ | ~ | ✓ | P2 | Answer self-check question in-text |
| Join | S | 3 | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✗ | ~ | ✗ | ✗ | ~ | P3 | Adequate for supporting |
| FILTER | S | 2 | ✓ | ✓ | ~ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ~ | P1 | Missing evaluation semantics |
| OPTIONAL | S | 2 | ✓ | ✓ | ~ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ~ | P1 | Missing left-outer-join semantics |
| LPG | M | 4 | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ~ | ✓ | ✓ | ✗ | ✓ | ✓ | P1 | Add MechKG LPG representation |
| Cypher | S | 3 | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ~ | ~ | ✗ | ~ | ✓ | P3 | Adequate for supporting |
| Internal ID | S | 4 | ✓ | ✓ | ✓ | ✓ | ✗ | ~ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Strong treatment |
| RDF vs LPG Tradeoffs | M | 4 | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ~ | ✓ | ✓ | ✗ | ✓ | ✓ | P1 | Add MechKG-specific tradeoff analysis |

### Chapter 3 (17 concepts)

| Concept | Class | Score | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | D11 | D12 | Sev | Action |
|---------|-------|-------|----|----|----|----|----|----|----|----|----|-----|-----|-----|-----|--------|
| Schema | M | 3 | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ~ | ✓ | ✓ | ✗ | ✓ | ✓ | P1 | Add MechKG schema alignment |
| Schema Alignment | S | 2 | ✓ | ✓ | ~ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | P1 | Outcome shown, process missing |
| Identity | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ✗ | ✓ | ✓ | P2 | Strong; add MechKG identity case |
| Identifier | S | 3 | ✓ | ✓ | ✓ | ~ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Adequate |
| Denotation | S | 2 | ✓ | ✓ | ~ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | P2 | One-sentence definition only |
| Entity Resolution | M | 3 | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | P1 | Geographic-only evidence; no conceptual identity |
| Record Linkage | I | 1 | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | P3 | Synonym mention only |
| Canonical Identifier | S | 2 | ✓ | ✓ | ~ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | P2 | No selection criteria or lifecycle |
| Alias | S | 2 | ✓ | ✓ | ~ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | P3 | Adequate for supporting |
| owl:sameAs | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ✗ | ✓ | ✓ | P1 | Add conceptual-identity danger example |
| UNA | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Strong treatment |
| RDF Dataset | S | 3 | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Adequate |
| Named Graph | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ✗ | ✓ | ✓ | P2 | Add MechKG source separation |
| N-ary Relation | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ✗ | ✓ | ✓ | P1 | Add DerivativeApplication as 4-ary |
| Reification | S | 3 | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✗ | ✓ | ✓ | ✗ | ~ | ✓ | P2 | Term never formally introduced |
| Qualifier | S | 2 | ✓ | ✓ | ~ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | P2 | Wikidata-only; no general mechanism |
| Provenance-Context | M | 3 | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | P2 | No multi-dimensional provenance demo |

### Chapter 4 (20 concepts)

| Concept | Class | Score | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | D11 | D12 | Sev | Action |
|---------|-------|-------|----|----|----|----|----|----|----|----|----|-----|-----|-----|-----|--------|
| Ontology | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | P2 | Strengthen MechKG ontology commitment |
| Axiom | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Strong |
| Interpretation | M | 5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P1 | Add MechKG interpretation (parallel to City) |
| Model | M | 5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Exemplary |
| Satisfaction | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Strong |
| Entailment | M | 5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Exemplary |
| Necessary Condition | M | 5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Exemplary |
| Sufficient Condition | M | 5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Exemplary |
| Equivalence | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Strong |
| Disjointness | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Strong |
| Existential Restriction | M | 5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P1 | Add MechKG ∃R.C worked example |
| Universal Restriction | M | 5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Exemplary two-level treatment |
| Cardinality | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Strong |
| Property Semantics | M | 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P2 | Missing reflexivity/irreflexivity/chains |
| OWA | M | 5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P1 | Add MechKG OWA consequences |
| Consistency | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P2 | Add MechKG inconsistency scenario |
| Satisfiability | M | 5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P2 | Add MechKG unsatisfiability analysis |
| DL Intuition | S | 3 | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | P2 | Add subsumption-check intuition |
| OWL Profiles | S | 3 | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | P2 | Classify CapitalCity under EL |
| Class Extension | S | 3 | ✓ | ✓ | ✓ | ~ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✓ | P2 | Never named explicitly |

### Chapter 5 (24 concepts)

| Concept | Class | Score | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | D11 | D12 | Sev | Action |
|---------|-------|-------|----|----|----|----|----|----|----|----|----|-----|-----|-----|-----|--------|
| Rule | M | 3 | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | P2 | Distinguish rule/axiom/shape |
| Substitution θ | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P1 | Add MechKG θ binding |
| Grounding | S | 2 | ✓ | ✓ | ~ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✓ | P2 | No standalone definition |
| Forward Chaining | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P1 | Add MechKG rule chain |
| Fixpoint | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P2 | Add MechKG classification fixpoint |
| Closure | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Strong |
| Monotonicity | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Strong |
| Termination | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Strong |
| RDFS Entailment | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Strong |
| Materialization | M | 3 | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ | ✓ | P2 | No worked execution of either strategy |
| Query-Time Reasoning | S | 3 | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ | ✓ | P3 | Adequate |
| Backward Chaining | S | 3 | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ | ✓ | P3 | Adequate |
| Soundness | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Strong |
| Completeness | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Strong |
| SHACL Shape | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P1 | Add CandidateMechanism shape |
| Target/Focus/Path/Value | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Strong pipeline walkthrough |
| Constraint | M | 3 | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | P2 | Feature-list; lacks decision procedure |
| Validation Report | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Strong |
| OWL vs SHACL Independence | M | 5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Exemplary 2×2 |
| Effective Validation Graph | M | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Strong |
| Graph Repair | M | 2 | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | P1 | No repair algorithm or cost model |
| OWL RL | S | 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | P3 | Strong; Theorem PR1 cited |
| SWRL/RIF | I | 1 | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | P3 | Adequate context |
| SPARQL Entailment Regime | S | 3 | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ | ✓ | P2 | No two-regime comparison demo |

### Chapter 6 (18 concepts)

| Concept | Class | Score | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | D11 | D12 | Sev | Action |
|---------|-------|-------|----|----|----|----|----|----|----|----|----|-----|-----|-----|-----|--------|
| Claim | M | 4 | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✗ | ✓ | ✓ | ~ | ✓ | ✓ | P2 | Add malformed claim counterexample |
| Evidence | M | 4 | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✗ | ✓ | ✓ | ~ | ✓ | ✓ | P2 | Add ambiguous classification boundary |
| Provenance | M | 4 | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✗ | ✓ | ✓ | ~ | ✓ | ✓ | P2 | Add broken chain counterexample |
| Proposition | S | 3 | ✓ | ✓ | ✓ | ~ | ✗ | ✓ | ✗ | ✓ | ~ | ✗ | ✓ | ✓ | P2 | Add MechKG proposition |
| Assertion | S | 3 | ✓ | ✓ | ✓ | ~ | ✗ | ✓ | ✗ | ✓ | ~ | ✗ | ✓ | ✓ | P2 | Show as bare triple vs reified Claim |
| Epistemic Model | M | 4 | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ~ | ✓ | ✓ | P1 | Add full MechKG pipeline walkthrough |
| Governance State | S | 3 | ✓ | ✓ | ✓ | ~ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | P1 | Add FSM diagram + MechKG transitions |
| Contradiction Taxonomy | M | 4 | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✗ | ✓ | ✓ | ~ | ✓ | ✓ | P1 | Map all 5 types to MechKG |
| Valid Time | S | 3 | ✓ | ✓ | ✓ | ~ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ | ✓ | P1 | Add mechanism temporal validity |
| Bitemporal | S | 2 | ✓ | ✓ | ~ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | P1 | INTUITION only; needs Turtle + query |
| Supersession | S | 3 | ✓ | ✓ | ✓ | ~ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | P2 | Add algorithm version supersession |
| Confidence Semantics | S | 3 | ✓ | ✓ | ✓ | ~ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | P2 | Add computable policy example |
| PROV-O Core | M | 4 | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✗ | ✓ | ✓ | ~ | ✓ | ✓ | P2 | Add LLM/Reasoner as Agent |
| Temporal Entity | I | 1 | ✗ | ✗ | ~ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ~ | P2 | Never defined standalone |
| Observation | S | 2 | ✓ | ✓ | ~ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | P1 | INTUITION only; needs structure |
| Candidate Knowledge | S | 3 | ✓ | ✓ | ✓ | ~ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | P1 | Add promotion criteria for MechKG |
| Accepted Knowledge | S | 3 | ✓ | ✓ | ✓ | ~ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | P2 | Add query semantics for Accepted |
| Source Reliability | S | 2 | ✓ | ✓ | ~ | ✗ | ✗ | ✗ | ✗ | ✗ | ~ | ✗ | ✗ | ✓ | P2 | INTUITION only; needs model |

---

## 2. Depth Distribution Summary

| Score | Count | % | Description |
|-------|-------|---|-------------|
| 5 | 10 | 9% | SYSTEM INTEGRATION — exemplary |
| 4 | 39 | 35% | TRANSFER — strong mechanism + application |
| 3 | 42 | 38% | MECHANISM — adequate but missing transfer |
| 2 | 17 | 15% | INTUITION — insufficient for stated classification |
| 1 | 4 | 4% | LABEL ONLY — never properly introduced |
| 0 | 0 | 0% | — |

**By Classification:**

| Class | Total | ≥4 | <4 | % Below Threshold |
|-------|-------|----|----|-------------------|
| Major (M) | 66 | 48 | 18 | 27% |
| Supporting (S) | 42 | 2 | 40 | 95% |
| Incidental (I) | 4 | 0 | 4 | 100% |

**Critical finding:** 18 Major concepts score below 4. The primary depth ceiling is D10 (Mechanism-KG application) — absent in every chapter. Secondary ceiling: D9 (engineering consequence) missing in Ch1 and thin in Ch3.

---

## 3. Explanation Theater Findings

Sections with pedagogical apparatus that do not execute the underlying mechanism:

| # | Location | Apparatus | What's Missing | Severity |
|---|----------|-----------|----------------|----------|
| T1 | Ch1 §1.2 Mermaid diagram | Three-subgraph KG model with cross-layer arrows | Arrows (E→S, R→M, P→C, I→SR, M→T) never explained | Medium |
| T2 | Ch1 §1.4 Layer Stack | Seven-layer ASCII stack | Visual implies hierarchy; text denies it; no transformation shown per layer | Medium |
| T3 | Ch1 §1.5 KSE Model | KSE = (K, T, C) notation | Introduced then never referenced again in any chapter | Medium |
| T4 | Ch2 §2.4.1 Comparison Table | 12-row RDF vs LPG table | §2.4.2 executes only 3 of 12 rows; remaining 9 are claim-only | Low |
| T5 | Ch3 §3.1.6 Three Schema Strategies | upfront/incremental/emergent catalog | No mechanism for any strategy; emergent never even sketched | Medium |
| T6 | Ch3 §3.4 Step 1 Schema Alignment | Result shown (ex:capitalOf ↔ wdt:P36) | Process of discovering/validating/rejecting mapping absent | Medium |
| T7 | Ch4 §4.13 MechKG Bridge | OWL equivalence + "toy" warning | DerivativeApplication fix sketched then abandoned; no formalization | High |
| T8 | Ch4 §4.12 OWL Profiles | EL/QL/RL complexity table | No ontology classified under any profile; no mechanism for claims | Medium |
| T9 | Ch5 §5.4 Materialization vs Query-Time | Comparison table + hybrid strategy | Zero worked execution of either strategy on running graph | Medium |
| T10 | Ch5 §5.18 MechKG Bridge | "Forward chaining and SHACL will be used" | No concrete rule, shape, or worked example | High |
| T11 | Ch5 §5.14 Entailment Regimes | Regime table + Service Description | No demonstration that two regimes give different answers | Low |
| T12 | Ch6 §6.15 Claim Ledger | Three-layer ASCII architecture | No query traversing layers; pointer mechanism unexplained | Medium |
| T13 | Ch6 §6.18 Contradiction Pipeline | Four-step bullets | Steps never executed; explicitly disclaims completeness | Medium |
| T14 | Ch6 §6.11 Confidence | 5-type table + `compositeConfidence ???` | No computable mechanism; taxonomy only | Low |

**Genuinely NOT theater (executed mechanisms):** Ch2 §2.1.5 isomorphism, Ch4 §4.3 interpretation walkthrough, Ch4 §4.5 two model-theoretic proofs, Ch5 §5.2 three-round θ trace, Ch5 §5.6 six-step SHACL walkthrough, Ch5 §5.9 two worked 2×2 cases, Ch6 §6.2–6.3 distinctions with Turtle.

---

## 4. Formalism Audit

### Formulas That Are EXPLANATORY (load-bearing)

| Location | Formula | Role |
|----------|---------|------|
| Ch1 §1.5 | K ⊆ V × L × V | Defines triple structure; justifies rejecting G=(V,E,λ) |
| Ch4 §4.3 | I = (Δ^I, ·^I) | Defines interpretation; every subsequent example depends on it |
| Ch4 §4.5 | O ⊨ α iff ∀I: I ⊨ O → I ⊨ α | Central entailment definition; proof walkthrough follows |
| Ch5 §5.2 | G_{i+1} = G_i ∪ {θ(head) \| θ(body) ⊆ G_i} | Forward chaining recurrence; multi-round trace instantiates |
| Ch5 §5.2 | G_{n+1} = G_n | Fixpoint termination; distinguished from closure |
| Ch5 §5.8 | G ⊆ G' → Consequences(G) ⊆ Consequences(G') | Monotonicity over KB; four NOT clarifications |

### Formulas That Are DECORATIVE (could be removed without loss)

| Location | Formula | Issue |
|----------|---------|-------|
| Ch1 §1.5 | KSE = (K, T, C) | Never referenced after introduction; orphan notation |

### Missing Formalisms (should be added)

| Concept | Where Needed | What's Missing |
|---------|-------------|----------------|
| RDF Graph | Ch2 §2.1 | G ⊆ (I ∪ B) × I × (I ∪ L ∪ B) |
| BGP Join | Ch2 §2.1.6 | Formal join semantics for shared variables |
| FILTER | Ch2 §2.1.6 | Evaluation order: post-binding on solution mappings |
| OPTIONAL | Ch2 §2.1.6 | Left-outer-join semantics with unbound variable handling |
| DerivativeApplication | Ch4 §4.13 | Complete DL axiom set for reified intermediate entity |
| Bitemporal | Ch6 §6.7 | Two-axis model (valid_time × system_time) with query pattern |
| Grounding | Ch5 §5.2 | Standalone definition: ground term = no variables |

---

## 5. Visual-Explanation Audit

Concepts requiring new or improved diagrams:

| Concept | Current Visual | Gap | Recommended Visual |
|---------|---------------|-----|-------------------|
| Context (Ch1) | None | 1/3 of core model unvisualized | Annotated triple with context metadata |
| BGP Cross-Product (Ch2) | None | Counterexample missing | Two patterns, no shared vars → cartesian product |
| OPTIONAL Semantics (Ch2) | None | Left-outer-join never shown | Inner vs outer join result tables side-by-side |
| N-ary Escalation (Ch3) | Mermaid for CapitalStatus | No 4+-ary example | DerivativeApplication with 4 participants |
| Mechanism Interpretation (Ch4) | City/Country figure only | No mechanism-domain figure | Δ^I = {m₁,d₁,q₁,r₁} with class extensions |
| OWL Profile Expressiveness (Ch4) | Table only | No concrete constructs | Three columns: one defining construct per profile |
| Governance State Machine (Ch6) | None | States listed statically | FSM: Candidate→Accepted→Contested→Superseded |
| Bitemporal Grid (Ch6) | None | Most underdeveloped concept | Two-axis grid with retrospective query arrow |
| Epistemic Pipeline (Ch6) | Labels only | No instantiated example | Same flowchart with mechanism claim at each stage |
| Claim Ledger Layers (Ch6) | ASCII boxes | No inter-layer flow | Directional arrows: assertion→claim→governance |

---

## 6. Cross-Chapter Dependency Flags

| # | Location | Problem | Severity |
|---|----------|---------|----------|
| D1 | Ch1 §1.8 | Five-term epistemic chain; Observation/Claim/Evidence unglossed | Minor |
| D2 | Ch5 §5.18 | `Condition`, `MechanismOperation` used without prior teaching; naming break with Ch4 | Moderate |
| D3 | Ch1 §1.7 | induction/deduction named without gloss | Minor |
| D4 | Ch3 §3.2.5 | blocking/matching/ML named without gloss | Minor |
| D5 | Registry | `claim`/`evidence` first_mentioned_chapter: 3 but actual Ch1 §1.8 | Registry accuracy |
| D6 | Registry | `subclass.first_explained_chapter: 2` but Ch2 never teaches rdfs:subClassOf | Registry accuracy |

---

## 7. Per-Chapter Summary

| Ch | Concepts | Score 5 | Score 4 | Score 3 | Score 2 | Score 1 | Strongest | Weakest |
|----|----------|---------|---------|---------|---------|---------|-----------|---------|
| 1 | 16 | 0 | 2 | 8 | 5 | 1 | Entity/KG (4) | Context (2) |
| 2 | 17 | 0 | 5 | 10 | 2 | 0 | RDF Triple/IRI/LPG/Internal ID/Tradeoffs (4) | FILTER/OPTIONAL (2) |
| 3 | 17 | 0 | 5 | 6 | 5 | 1 | Identity/sameAs/UNA/NamedGraph/N-ary (4) | Record Linkage (1) |
| 4 | 20 | 9 | 7 | 4 | 0 | 0 | Interpretation/Model/Entailment/OWA (5) | Property Semantics/DL Intuition/Profiles (3) |
| 5 | 24 | 1 | 14 | 6 | 2 | 1 | OWL vs SHACL Independence (5) | Graph Repair (2)/SWRL (1) |
| 6 | 18 | 0 | 6 | 8 | 3 | 1 | Claim/Evidence/PROV-O/Epistemic (4) | Bitemporal/Observation/Source Reliability (2) |
