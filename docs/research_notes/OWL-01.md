# OWL-01: OWL 2 Web Ontology Language Document Overview

- **Canonical URL:** https://www.w3.org/TR/owl2-overview/
- **Status:** W3C Recommendation (2012-12-11)
- **Fetched:** 2026-08-25, HTTP 200
- **Used in:** Chapters 4, 5

## Key Points

- OWL 2 is the current stable ontology language for the Semantic Web.
- Defines classes, properties, individuals, and axioms with formal semantics based on description logics.
- Property characteristics include SymmetricProperty, TransitiveProperty, InverseFunctionalProperty, etc.
- Correct representation: `(prop, rdf:type, owl:SymmetricProperty)` — NOT `(prop, owl:symmetricProperty, true)`.
- Supports reasoning via entailment regimes defined in OWL 2 Direct Semantics and RDF-Based Semantics.

## Semantic Contract

OWL property declarations are assertions about the property itself, not boolean flags. A symmetric property is declared by asserting that the property is an instance of `owl:SymmetricProperty`.

