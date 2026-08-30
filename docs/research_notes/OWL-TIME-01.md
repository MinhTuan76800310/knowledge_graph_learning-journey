# OWL-TIME-01: Time Ontology in OWL

- **Canonical URL:** https://www.w3.org/TR/owl-time/
- **Status:** W3C Recommendation (First Edition, 2017-10-19) — **stable baseline**
- **Current revision:** Candidate Recommendation Draft 2022-11-15 (revision in progress; NOT a Second Edition)
- **Editors (Recommendation):** Simon Cox (CSIRO), Chris Little (Met Office)
- **Note:** Hobbs and Pan edited the 2006 Working Draft, not the Recommendation.
- **Fetched:** 2026-08-30, HTTP 200
- **Used in:** Chapter 6

## Key Points

- Core classes: TemporalEntity, Instant, Interval. Allen's interval algebra relations.
- hasTime links any resource to a TemporalEntity.
- Valid time vs assertion time modeled as separate temporal facts.
- Duration via Duration, DurationDescription, or TemporalUnit.

## Semantic Contract

OWL-Time provides the vocabulary for representing temporal knowledge in RDF/OWL. For Ch6, use it to model multiple temporal dimensions of claims (valid time, assertion time, observation time). Emphasize that OWL-Time is a representation vocabulary, not a temporal reasoning engine.

Stable baseline is the 2017 First Edition Recommendation; the 2022-11-15 CR Draft is a revision in progress and must not be cited as a current Recommendation.
