# OWL-06: OWL 2 RDF-Based Semantics

- **URL:** https://www.w3.org/TR/owl2-rdf-based-semantics/
- **Status:** FETCHED_AND_VERIFIED
- **Used in:** Chapter 4
- **Document status:** W3C Recommendation (2012-12-11)

## Key findings for Chapter 4

### High-level distinction
RDF-Based Semantics extends D-Entailment and gives formal meaning directly to RDF graphs. Direct Semantics is description-logic-style semantics applied to OWL structural objects. These are two different semantic regimes, NOT determined by serialization format.

### Semantics on RDF graphs
"The OWL 2 RDF-Based Semantics gives a formal meaning to every RDF graph." Unlike Direct Semantics which operates on structural constructs, RDF-Based operates directly on triples.

### Serialization ≠ semantic regime
An OWL 2 DL ontology serialized in RDF/Turtle can be mapped back to structural form via the OWL 2 RDF Mapping and interpreted using Direct Semantics. The choice of semantics depends on the reasoning task, not the file format.

### Annotations ARE semantically meaningful under RDF-Based
Unlike Direct Semantics where annotations are completely ignored, under RDF-Based Semantics annotations are "semantically weak" but still assigned truth values. Adding an annotation may change ontology meaning under RDF-Based. This is a key difference between the two regimes.

### Punning handled differently
Under RDF-Based, universe parts need not be disjoint — same IRI can simultaneously denote a class and a property. Direct Semantics requires separation (punning is restricted).

### Correspondence with Direct Semantics
Direct Semantics conclusions are reflected by RDF-Based ("Direct Semantics can be viewed as a semantics subset of RDF-Based"). But RDF-Based may derive additional conclusions.

### OWL 2 Full undecidability
OWL 2 Full under RDF-Based Semantics is undecidable. OWL 2 DL under Direct Semantics is decidable.

## What this source establishes for Ch4
- RDF-Based gives semantics to RDF graphs directly
- Serialization format does not determine semantic regime
- Annotations have different status under RDF-Based vs Direct
- Correspondence relationship between the two semantics

## Safe simplifications
- Not teaching RDF-Based semantics in detail is safe; Ch4 focuses on Direct Semantics.
- Mentioning it exists and differs is sufficient for Ch4 scope.

## Dangerous simplifications
- Saying "RDF files use RDF-Based Semantics" — wrong, serialization ≠ semantics.
- Saying annotations never affect reasoning — true only under Direct Semantics.

## What this source does NOT justify
- Specific Direct Semantics satisfaction conditions (use OWL-04).
- Profile complexity claims (use OWL-05).
