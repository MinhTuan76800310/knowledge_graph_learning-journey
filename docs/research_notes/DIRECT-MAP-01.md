# DIRECT-MAP-01: A Direct Mapping of Relational Data to RDF

- **Canonical URL:** https://www.w3.org/TR/rdb-direct-mapping/
- **Status:** W3C Recommendation (2012-09-27)
- **Fetched:** 2026-08-30, HTTP 200
- **Used in:** Chapter 7

## Key Points

- Defines a **default** mapping from a relational database to an RDF dataset — no
  user-written mapping rules required.
- Each table becomes a class; each row becomes a resource whose IRI is derived from the
  table name and the row's primary key.
- Each column becomes a predicate; the cell value becomes the object (typed per the
  column's SQL type).
- Because it is fully automatic, the resulting RDF shape follows the database schema
  rather than a target ontology.

## Semantic Contract

- Direct Mapping and R2RML are the two W3C Recommendation options for RDB → RDF:
  Direct Mapping is the automatic default; R2RML is the customizable mapping language.
- Use it to teach the concept: a mapping can be *implicit/default* or *explicit/custom*;
  both are decisions that shape the RDF output.
- Do NOT present Direct Mapping's RDF shape as semantically ideal — it is a mechanical
  default, not a target-ontology-optimized mapping.
- Do NOT conflate Direct Mapping (RDB → RDF) with CSVW (tabular → RDF).
