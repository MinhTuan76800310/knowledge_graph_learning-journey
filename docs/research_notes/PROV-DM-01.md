# PROV-DM-01: PROV Data Model

- **Canonical URL:** https://www.w3.org/TR/prov-dm/
- **Status:** W3C Recommendation (2013-04-30)
- **Fetched:** 2026-08-29, HTTP 200
- **Used in:** Chapter 6

## Key Points

- PROV-DM is the conceptual data model for provenance; PROV-O is its OWL/RDF mapping.
- Core classes: Entity ("thing with fixed aspects"), Activity ("something that occurs over time"), Agent ("bears responsibility").
- Core relationships: used, wasGeneratedBy, wasInformedBy, wasDerivedFrom, wasAttributedTo, wasAssociatedWith.
- Provenance descriptions form directed graphs rooted at the entity whose history is described, pointing backward to dependencies.
- Activities and entities are disjoint. Generation precedes usage. Influence underlies all relations.
- Generation, usage, invalidation, start, end are instantaneous events; activities have temporal extent.

## Semantic Contract

PROV-DM provides the abstract provenance model; PROV-O provides the RDF vocabulary. When teaching provenance in Ch6, use PROV-O as the concrete vocabulary but ground it in PROV-DM's conceptual distinctions (Entity vs Activity vs Agent, generation vs usage vs derivation).
