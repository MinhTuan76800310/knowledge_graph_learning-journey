# OWL-TIME-01: Time Ontology in OWL

- **Canonical URL:** https://www.w3.org/TR/owl-time/
- **Status:** W3C Recommendation (2020-10-27, Second Edition)
- **Fetched:** 2026-08-29, HTTP 200
- **Used in:** Chapter 6

## Key Points

- Core classes: TemporalEntity, Instant, Interval. Allen's interval algebra relations.
- hasTime links any resource to a TemporalEntity.
- Valid time vs assertion time modeled as separate temporal facts.
- Duration via Duration, DurationDescription, or TemporalUnit.

## Semantic Contract

OWL-Time provides the vocabulary for representing temporal knowledge in RDF/OWL. For Ch6, use it to model multiple temporal dimensions of claims (valid time, assertion time, observation time). Emphasize that OWL-Time is a representation vocabulary, not a temporal reasoning engine.
