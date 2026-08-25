# TOOL-01: RDFLib Documentation

- **Canonical URL:** https://rdflib.readthedocs.io/
- **Status:** Official documentation (stable)
- **Fetched:** 2026-08-25, HTTP 200
- **Installed version in this project:** 7.6.0

## Key Points

- RDFLib is a pure Python package for working with RDF.
- Core classes:
  - `Graph` — main graph interface (single or named-graph datasets)
  - `URIRef` — an IRI reference term
  - `Literal` — an RDF literal term
  - `BNode` — a blank node term
  - `Namespace` — namespace management
- Serialization formats supported for parsing and serializing:
  RDF/XML, N3, N-Triples, N-Quads, Turtle, TriG, TriX, JSON-LD, HexTuples,
  RDFa, Microdata.
- Includes a SPARQL 1.1 query and update engine.
- Versioning follows semantic versioning.

## Semantic Contract for Chapter 2

- RDFLib is the implementation vehicle, not the specification.
- All semantic claims in Chapter 2 derive from W3C specifications, not RDFLib behavior.
- RDFLib's SPARQL engine implements SPARQL 1.1 (stable baseline).

## Used In

- Chapter 2 (Experiments 2-1, 2-2, 2-3)
- Chapter 3+ (RDF operations throughout)
