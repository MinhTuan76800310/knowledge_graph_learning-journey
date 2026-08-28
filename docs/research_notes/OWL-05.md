# OWL-05: OWL 2 Profiles

- **URL:** https://www.w3.org/TR/owl2-profiles/
- **Status:** FETCHED_AND_VERIFIED
- **Used in:** Chapter 4
- **Document status:** W3C Recommendation (2012-12-11)

## Key findings for Chapter 4

### Three profiles (§1)
OWL 2 EL, OWL 2 QL, OWL 2 RL. None is a subset of another. Each trades expressivity for specific tractability properties.

### OWL 2 EL (§2)
Targets ontologies with very large numbers of properties/classes. Core reasoning (consistency, subsumption, instance checking) is PTIME-complete. However, conjunctive query answering is in EXPTIME — so "polynomial-time reasoning" applies only to core tasks, NOT all reasoning. Restrictions: no universal quantification, cardinality, disjunction/union/complement, inverse/symmetric/asymmetric properties, functional/inverse-functional properties.

### OWL 2 QL (§3)
Targets large volumes of instance data where query answering is primary. Conjunctive query answering can be implemented via SQL query rewriting; data complexity is in AC0. Combined query answering is NP-complete. Excludes SameIndividual, functional properties, keys (which would break first-order rewritability), self-restrictions, value restrictions, enumerations, universal/cardinality/disjunction constructs, property chains, transitive roles.

### OWL 2 RL (§4)
Targets scalable reasoning without sacrificing too much expressivity. Axiomatized by OWL 2 RL/RDF rules (first-order implications over generalized RDF triples). Can run on arbitrary RDF graphs but **completeness is then not guaranteed**. Core consistency/subsumption/instance checking are PTIME for taxonomic/data complexity, co-NP-complete combined. Disallows DisjointUnion and ReflexiveObjectProperty.

### Complexity table (§5)
- Full OWL 2 Direct Semantics: N2EXPTIME-complete for core problems
- Full OWL 2 RDF-Based Semantics: undecidable
- Profiles trade expressivity for tractability

## What this source establishes for Ch4
- Profile design rationales and restrictions
- Complexity guarantees per profile
- No profile is universally better than another
- RL completeness limitation on arbitrary RDF

## Safe simplifications
- Summarizing each profile's target use case in one line is safe.
- Omitting detailed syntactic restrictions per profile is safe for Ch4 scope.

## Dangerous simplifications
- Saying EL is "polynomial-time" without qualifying "for core reasoning tasks."
- Saying RL is "compatible with rule engines" without noting completeness limitations.
- Implying any profile is universally faster/better.

## What this source does NOT justify
- Claims about which profile to choose for a specific application (context-dependent).
- Claims about practical performance (complexity ≠ wall-clock time).
