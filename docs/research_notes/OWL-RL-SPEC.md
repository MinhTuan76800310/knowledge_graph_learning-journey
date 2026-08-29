# OWL-RL-SPEC: OWL 2 RL Profile — Rule Tables and Completeness

- **Canonical URL:** https://www.w3.org/TR/owl2-profiles/#OWL_2_RL
- **Status:** W3C Recommendation (2012-12-11)
- **Fetched:** 2026-08-29, HTTP 200
- **Used in:** Chapter 5
- **Document status:** Stable W3C Recommendation
- **Note:** Supplements OWL-05.md which covers all three profiles at overview level. This note focuses specifically on RL rule table details needed for Ch5.

## Key Points

### Design Philosophy
OWL 2 RL targets "applications that require scalable reasoning without sacrificing too much expressive power." It achieves this by:
1. Defining a syntactic subset of OWL 2 amenable to rule-based implementation
2. Providing a **partial axiomatization** of OWL 2 RDF-Based Semantics as first-order implications

Inspired by Description Logic Programs (DLP) and pD*.

### The Rule Tables (§4.3)
The OWL 2 RL/RDF rules are organized into six tables of first-order implications:

| Table | Category | Example Rules | Purpose |
|-------|----------|---------------|---------|
| 4 | Equality | eq-ref, eq-sym, eq-trans, replacement | owl:sameAs reasoning |
| 5 | Properties | prp-dom, prp-rng, prp-fp, prp-ifp, prp-trp, prp-spo1/2, prp-key | Property domain/range, functionality, transitivity, chains |
| 6 | Classes | cls-thing, cls-nothing, cls-int, cls-uni, cls-com, cls-svf, cls-avf | Class intersection/union/complement, restrictions |
| 7 | Class Axioms | cax-sco, cax-eqc, cax-dw, cax-adc | Subclass, equivalence, disjointness |
| 8 | Datatypes | dt-type, dt-eq, dt-diff, dt-not-type | Datatype reasoning |
| 9 | Schema Vocabulary | scm-cls, scm-sco, scm-op, scm-dom, scm-rng | Self-contained schema reasoning |

**Teaching-critical rules:**
- `prp-dom`: If P rdfs:domain C and x P y → x rdf:type C (RDFS domain as INFERENCE rule)
- `prp-rng`: If P rdfs:range C and x P y → y rdf:type C (RDFS range as INFERENCE rule)
- `cax-sco`: If A rdfs:subClassOf B and x rdf:type A → x rdf:type B
- `prp-spo1`: If P1 rdfs:subPropertyOf P2 and x P1 y → x P2 y

These are exactly the rules that demonstrate "RDFS domain/range are inference rules, NOT validation constraints."

### Completeness Theorem (Theorem PR1)
For OWL 2 RL ontologies meeting specific syntactic conditions:
- Entailment under OWL 2 Direct Semantics ↔ first-order entailment of rule-annotated RDF graph
- This is a **conditional** completeness result

### Critical Limitation: Arbitrary RDF
When RL rules are applied to arbitrary RDF graphs (not guaranteed to be valid OWL 2 RL ontologies):
- **"It is no longer possible to guarantee that all correct answers can be returned"**
- However, the implementation **"will still produce only correct entailments"** (soundness preserved)

This is the precise formulation of: "OWL RL designed for rule-oriented reasoning but completeness not guaranteed on arbitrary RDF."

### Syntactic Restrictions Making RL Tractable
Constructors restricted to specific positions (Table 2):
- Subclass expressions: named classes, enumerations, intersections/unions, existential restrictions, has-value
- Superclass expressions: named classes, intersection, complement, universal restriction, has-value, 0/1 max-cardinality
- Disallows: DisjointUnion, ReflexiveObjectProperty
- DataRange limited to datatypes and intersections

These restrictions serve two purposes:
1. **Avoid inferring existence of unknown individuals** (no unbounded existential introduction)
2. **Avoid nondeterministic reasoning** (no disjunctive branching needed)

Both are exactly what makes forward chaining applicable: no need for tableau-style case splitting or Skolemization.

## Semantic Contract

OWL 2 RL provides a **sound** rule-based approximation of OWL 2 RDF-Based Semantics. For valid RL ontologies, it is also complete. For arbitrary RDF, it remains sound but may miss some entailments. This is fundamentally different from SHACL validation: RL rules ADD information (inference), while SHACL shapes CHECK information (validation).

## Teaching Relevance for Ch5

### Primary Source For
1. **Concrete rule tables** — actual first-order implications students can read and trace
2. **Domain/range as inference** — prp-dom and prp-rng are the definitive examples
3. **Conditional completeness** — Theorem PR1 with its preconditions
4. **Soundness on arbitrary RDF** — always correct, sometimes incomplete
5. **Why restrictions matter** — connecting syntactic limits to algorithmic properties

### Two Pipelines Reinforcement
The RL rule tables make the inference pipeline concrete:
- Input: RDF graph + OWL 2 RL ontology
- Process: Apply Tables 4-9 as forward chaining rules
- Output: Extended graph with all derivable triples
- Contrast: SHACL takes graph + shapes → validation report

### Connection to Forward Chaining Fixpoint
The RL rules are designed to be applied via forward chaining to fixpoint. Each table entry is a Horn-like implication suitable for the G_{i+1} = G_i ∪ consequences(G_i) algorithm from HOGAN-CH5. The syntactic restrictions ensure termination (no existential introduction of new individuals).

## Safe Simplifications
- Listing representative rules rather than all ~50 rules is safe.
- Saying "RL rules can run on any RDF graph" is safe (with completeness caveat).
- Summarizing restriction rationale as "avoid new individuals and nondeterminism" is safe.

## Dangerous Simplifications
- Saying "OWL RL is complete for all OWL reasoning" — only for valid RL ontologies.
- Saying "RL rules are the same as RDFS rules" — RL extends far beyond RDFS.
- Omitting the soundness-preserved-on-arbitrary-RDF point (this is a key practical advantage).
- Implying RL rules handle negation or full cardinality reasoning.

## What This Source Does NOT JUSTIFY
- Full OWL 2 DL reasoning capabilities (use OWL-05 for profile comparison).
- SHACL validation semantics (use SH-01).
- Specific forward chaining algorithm details (use HOGAN-CH5).
- SWRL rule syntax or decidability (use SWRL-01).
