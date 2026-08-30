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
| R2RML-01 | `w3c-r2rml` | R2RML: RDB to RDF Mapping Language |
| DIRECT-MAP-01 | `w3c-direct-mapping` | A Direct Mapping of Relational Data to RDF |
| CSVW-01 | `w3c-tabular-data-model` | Model for Tabular Data and Metadata on the Web |
| RL-01 | `fellegi-sunter-1969` | A Theory for Record Linkage |
| SM-01 | `rahm-bernstein-2001` | A Survey of Approaches to Automatic Schema Matching |
| DI-01 | `lenzerini-2002` | Data Integration: A Theoretical Perspective |
| HOGAN-CREATE-01 | `hogan-creation-enrichment` | Knowledge Graphs (Hogan et al.), Creation and Enrichment |
| HOGAN-IND-01 | `hogan-inductive` | Knowledge Graphs (Hogan et al.), Inductive Knowledge |
| TRANSE-01 | `bordes-transe-2013` | Translating Embeddings for Modeling Multi-relational Data (TransE) |
| DISTMULT-01 | `yang-distmult-2015` | Embedding Entities and Relations for Learning and Inference in Knowledge Bases (DistMult) |
| COMPLEX-01 | `trouillon-complex-2016` | Complex Embeddings for Simple Link Prediction (ComplEx) |
| RGCN-01 | `schlichtkrull-rgcn-2018` | Modeling Relational Data with Graph Convolutional Networks (R-GCN) |
| AMIE-01 | `galarraga-amie-2015` | Fast Rule Mining in Ontological Knowledge Bases with AMIE+ |
| GRAIL-01 | `teru-grail-2020` | Inductive Relation Prediction by Subgraph Reasoning (GraIL) |
| NICKEL-01 | `nickel-relational-ml-2016` | A Review of Relational Machine Learning for Knowledge Graphs |
| NEGSAMP-01 | `mikolov-negativesampling-2013` | Distributed Representations of Words and Phrases and their Compositionality |
| OVERSMOOTH-01 | `li-oversmoothing-2018` | Deeper Insights into Graph Convolutional Networks for Semi-Supervised Learning |
| SHORTCUT-01 | `geirhos-shortcut-2020` | Shortcut Learning in Deep Neural Networks |
| CALIB-01 | `guo-calibration-2017` | On Calibration of Modern Neural Networks |
| COLLAPSE-01 | `shumailov-collapse-2024` | AI models collapse when trained on recursively generated data |
| GRLBOOK-01 | `hamilton-grl-2020` | Graph Representation Learning (Hamilton) |

## Rules

- One canonical source has exactly one internal ID and one bibliography key.
- Prose in `book/` cites with `[@bibliography-key]` only; never raw internal IDs or URLs.
- Engineering docs (`docs/`) may continue to use internal IDs.
- Emerging standards (RDF 1.2, SPARQL 1.2) are cited only inside clearly marked
  "Current Developments" callouts.
