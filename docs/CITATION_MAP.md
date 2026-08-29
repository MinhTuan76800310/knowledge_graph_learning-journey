# Citation Map — Internal Source IDs to Bibliography Keys

Internal source IDs (used in `docs/source_index.json`, research notes, and engineering
docs) are deliberately kept out of printed prose. The manuscript uses Pandoc citations
(`[@key]`) that resolve against `book/references.bib`. This table maps the two.

| Internal ID | Bibliography key | Title |
|-------------|------------------|-------|
| S03 | `stanford-cs520-what-is-kg` | What is a Knowledge Graph? |
| S04 | `stanford-cs520-graph-data-models` | What Are Graph Data Models? |
| S05 | `stanford-cs520-create-kg` | How to Create a Knowledge Graph? |
| S06 | `stanford-cs520-kg-from-data` | How to Create a Knowledge Graph from Data? |
| H01 | `hogan-knowledge-graphs` | Knowledge Graphs (Hogan et al.) |
| HOGAN-CH6 | `hogan-deductive-knowledge` | Knowledge Graphs (Hogan et al.), Deductive Knowledge |
| HOGAN-CH5 | `hogan-rules-reasoning` | Knowledge Graphs (Hogan et al.), Rules and Reasoning |
| R11-01 | `w3c-rdf11-primer` | RDF 1.1 Primer |
| R11-02 | `w3c-rdf11-concepts` | RDF 1.1 Concepts and Abstract Syntax |
| R11-03 | `w3c-rdf-schema` | RDF Schema 1.1 |
| R11-05 | `w3c-rdf11-turtle` | RDF 1.1 Turtle |
| SP11-01 | `w3c-sparql11-overview` | SPARQL 1.1 Overview |
| SP11-02 | `w3c-sparql11-query` | SPARQL 1.1 Query Language |
| OWL-01 | `w3c-owl2-overview` | OWL 2 Web Ontology Language Overview |
| OWL-02 | `w3c-owl2-primer` | OWL 2 Web Ontology Language Primer |
| OWL-03 | `w3c-owl2-syntax` | OWL 2 Structural Specification and Functional-Style Syntax |
| OWL-04 | `w3c-owl2-direct-semantics` | OWL 2 Direct Semantics |
| OWL-05 | `w3c-owl2-profiles` | OWL 2 Profiles |
| OWL-06 | `w3c-owl2-rdf-semantics` | OWL 2 RDF-Based Semantics |
| SH-01 | `w3c-shacl` | Shapes Constraint Language (SHACL) |
| SH-02 | `w3c-shacl12-core` | SHACL 1.2 Core |
| SWRL-01 | `swrl-submission` | SWRL: Semantic Web Rule Language |
| RIF-01 | `w3c-rif-core` | RIF Core Dialect |
| NARY-01 | `w3c-nary-relations` | Defining N-ary Relations on the Semantic Web |
| WD-01 | `wikidata-statements` | Wikidata Help: Statements |
| WD-02 | `wikidata-qualifiers` | Wikidata Help: Qualifiers |
| PROV-01 | `prov-o` | The PROV Ontology |
| PROV-DM-01 | `prov-dm` | PROV Data Model (PROV-DM) |
| OWL-TIME-01 | `owl-time` | Time Ontology in OWL |
| TOOL-01 | `rdflib-docs` | RDFLib Documentation |
| N4J-03 | `neo4j-modeling-fundamentals` | Graph Data Modeling Fundamentals |
| N4J-05 | `neo4j-data-modeling` | Neo4j Data Modeling |
| N4J-06 | `neo4j-cypher-manual` | Neo4j Cypher Manual |
| GQL-01 | `iso-gql` | ISO/IEC 39075:2024 GQL |
| GQL-02 | `neo4j-cypher-gql-conformance` | Neo4j Cypher GQL conformance |
| R12-01 | `w3c-rdf12-concepts` | RDF 1.2 Concepts (emerging) |
| SP12-01 | `w3c-sparql12-query` | SPARQL 1.2 Query (emerging) |
| RDF-MT-01 | `w3c-rdf11-mt` | RDF 1.1 Semantics |
| SP11-ENT | `w3c-sparql11-entailment` | SPARQL 1.1 Entailment Regimes |

## Rules

- One canonical source has exactly one internal ID and one bibliography key.
- Prose in `book/` cites with `[@bibliography-key]` only; never raw internal IDs or URLs.
- Engineering docs (`docs/`) may continue to use internal IDs.
- Emerging standards (RDF 1.2, SPARQL 1.2) are cited only inside clearly marked
  "Current Developments" callouts.
