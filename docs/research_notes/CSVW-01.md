# CSVW-01: Model for Tabular Data and Metadata on the Web

- **Canonical URL:** https://www.w3.org/TR/tabular-data-model/
- **Status:** W3C Recommendation (2015-12-17)
- **Fetched:** 2026-08-30, HTTP 200
- **Used in:** Chapter 7

## Key Points

- Defines a model for tabular data on the Web and how to publish it with metadata.
- A **table** is composed of rows and columns; a **cell** holds a value; a **column** has a
  name and a declared datatype.
- **Annotations** (metadata) describe the table, its columns, and its cells, e.g. which
  column is the primary key, how values are typed.
- Tabular data carries implicit structure (headers, rows, data types) that must be made
  explicit before the data can be turned into RDF.
- Companion specification: *Generating RDF from Tabular Data on the Web* (csv2rdf,
  W3C Recommendation 2015-12-17).

## Semantic Contract

- CSVW is the stable W3C baseline for turning tabular sources (CSV/TSV) into RDF.
- Use it to teach the concept: tabular data is *structured* but not *semantic*; a mapping
  step is required to give cells meaning in RDF.
- Do NOT conflate CSVW (tabular → RDF) with R2RML (relational DB → RDF) or Direct
  Mapping (relational DB → RDF, default shape).
