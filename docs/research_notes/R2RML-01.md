# R2RML-01: R2RML — RDB to RDF Mapping Language

- **Canonical URL:** https://www.w3.org/TR/r2rml/
- **Status:** W3C Recommendation (2012-09-27)
- **Fetched:** 2026-08-30, HTTP 200
- **Used in:** Chapter 7

## Key Points

- R2RML defines a language for expressing customized mappings from relational databases to RDF datasets.
- **Triples Map:** a rule that translates each row of a logical table into zero or more RDF triples.
- **Subject Map:** generates the subject URI for each row's triples (may be a template or constant).
- **Predicate-Object Map:** pairs predicate and object maps to generate each triple's predicate and object.
- Logical Table may be a base table, a view, or a SQL query.
- R2RML is designed for custom/shaped RDF output, not a default direct mapping.

## Semantic Contract

- R2RML is a stable W3C Recommendation (2012).
- Use R2RML to teach the concept: mapping is an explicit, versioned transformation specification.
- Do NOT present R2RML as the only or best approach for all source types.
- Do NOT conflate R2RML (RDB→RDF) with CSVW (tabular→RDF) or Direct Mapping (RDB→RDF default).