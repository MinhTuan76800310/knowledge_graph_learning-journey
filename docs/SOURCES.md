# Sources — Knowledge Graph Book

This document lists all authoritative sources consulted for this book.
Every factual or formal claim that depends on an external definition is traceable to one of these sources.

Last verified: 2026-08-25

## W3C Standards

| Specification | Version | Status | Date | URL | Notes |
|---|---|---|---|---|---|
| RDF 1.1 Primer | 1.1 | Recommendation | 2014-02-25 | https://www.w3.org/TR/rdf11-primer/ | Stable baseline for introductory RDF |
| RDF 1.1 Concepts and Abstract Syntax | 1.1 | Recommendation | 2014-02-25 | https://www.w3.org/TR/rdf11-concepts/ | Stable baseline |
| RDF 1.2 Concepts and Abstract Data Model | 1.2 | Candidate Recommendation Snapshot | 2026-04-07 | https://www.w3.org/TR/rdf12-concepts/ | Emerging: triple terms, reification improvements |
| RDF 1.2 Primer | 1.2 | Working Draft | 2026 | https://www.w3.org/TR/rdf12-primer/ | Emerging companion to RDF 1.2 Concepts |
| SPARQL 1.1 Overview | 1.1 | Recommendation | 2013-03-21 | https://www.w3.org/TR/sparql11-overview/ | Stable baseline |
| SPARQL 1.1 Query Language | 1.1 | Recommendation | 2013-03-21 | https://www.w3.org/TR/sparql11-query/ | Stable baseline |
| SPARQL 1.2 Query Language | 1.2 | Working Draft | 2026-08-20 | https://www.w3.org/TR/sparql12-query/ | Emerging; not yet stable |
| OWL 2 Web Ontology Language Document Overview (Second Edition) | 2 | Recommendation | 2012-12-11 | https://www.w3.org/TR/owl2-overview/ | Stable baseline |
| OWL 2 Primer (Second Edition) | 2 | Recommendation | 2012-12-11 | https://www.w3.org/TR/owl2-primer/ | Stable baseline |
| Shapes Constraint Language (SHACL) | 1.0 | Recommendation | 2017-07-20 | https://www.w3.org/TR/shacl/ | Stable baseline; SHACL 1.2 Core exists as Working Draft (2026-08-03) |
| PROV-O: The PROV Ontology | 1.0 | Recommendation | 2013-04-30 | https://www.w3.org/TR/prov-o/ | Stable baseline for provenance |
| Turtle 1.1 | 1.1 | Recommendation | 2014-02-25 | https://www.w3.org/TR/turtle/ | Stable baseline |

### Version-awareness legend

- **Stable baseline**: W3C Recommendation. Used as main curriculum material.
- **Current development**: Candidate Recommendation or Working Draft. Clearly labeled in the book as emerging material.
- **Experimental / emerging**: Editor's Draft or unofficial community work. Referenced only with explicit caveats.

## Academic Sources

| Source | Authors / Organization | Type | URL | License / Notes | Chapters |
|---|---|---|---|---|---|
| Stanford CS520 — Knowledge Graphs | Stanford University | ACADEMIC | https://web.stanford.edu/class/cs520 | Course materials; research reference only | 1, 2, 3, 4, 5, 6, 7, 10 |
| Knowledge Graphs (Springer, 2021) | Aidan Hogan et al. | ACADEMIC | https://kgbook.org | Copyrighted Springer book. Research reference only; no copied prose or figures | All chapters |
| Stanford CS224W — Machine Learning with Graphs | Stanford University / Jure Leskovec | ACADEMIC | https://snap.stanford.edu/class/cs224w/ | Course materials; KG embeddings and reasoning sections only | 8 |
| Ontology Development 101 | Natalya F. Noy & Deborah L. McGuinness, Stanford / Protégé team | TUTORIAL | https://protege.stanford.edu/publications/ontology_development/ontology101.pdf | Foundational ontology engineering methodology | 4 |
| Unifying Large Language Models and Knowledge Graphs: A Roadmap | Zhu et al., 2023 | RESEARCH_PAPER | https://arxiv.org/abs/2306.08302 | Survey paper; DOI 10.1109/TKDE.2024.3352100; used in Chapter 9 only | 9 |

## Official Documentation & Case Studies

| Source | Organization | Type | URL | Chapters |
|---|---|---|---|---|
| Wikidata Data Model | Wikimedia Foundation | OFFICIAL_DOCUMENTATION | https://www.mediawiki.org/wiki/Wikibase/DataModel | 3, 6 |
| Wikidata Help:Statements | Wikimedia Foundation | OFFICIAL_DOCUMENTATION | https://www.wikidata.org/wiki/Help:Statements | 6 |
| Wikidata Help:Qualifiers | Wikimedia Foundation | OFFICIAL_DOCUMENTATION | https://www.wikidata.org/wiki/Help:Qualifiers | 6 |
| Wikidata SPARQL Tutorial | Wikimedia Foundation | TUTORIAL | https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial | 2, 6 |
| Neo4j Fundamentals | Neo4j, Inc. | OFFICIAL_DOCUMENTATION | https://neo4j.com/docs/getting-started/ | 2 |
| Neo4j Cypher Fundamentals | Neo4j, Inc. | OFFICIAL_DOCUMENTATION | https://neo4j.com/docs/cypher-manual/current/ | 2 |
| Neo4j Graph Data Modeling Fundamentals | Neo4j, Inc. | OFFICIAL_DOCUMENTATION | https://neo4j.com/docs/modeling/ | 2, 3 |
| Building Knowledge Graphs with LLMs | Neo4j, Inc. | TUTORIAL | https://neo4j.com/docs/genai/ | 7, 9 |
| Microsoft GraphRAG Documentation | Microsoft Research | OFFICIAL_DOCUMENTATION | https://microsoft.github.io/graphrag/ | 9 |
| Microsoft GraphRAG Indexing Architecture | Microsoft Research | OFFICIAL_DOCUMENTATION | https://microsoft.github.io/graphrag/index/architecture/ | 9 |

## Python Libraries Evaluated

| Library | Latest Version | Last Release | Purpose | Decision |
|---|---|---|---|---|
| RDFLib | 7.6.0 | 2026-02-13 | RDF manipulation, Turtle, SPARQL | ✅ Selected |
| pySHACL | 0.40.1 | 2026-07-28 | SHACL validation | ✅ Selected |
| owlrl | 7.6.2 | 2026-07-08 | RDFS/OWL reasoning | ✅ Selected |
| NetworkX | 3.6.1 | 2025+ | Graph analytics, centrality, community detection | ✅ Selected |
| PyKEEN | 1.11.1 | 2025-04-24 | KG embeddings (TransE, DistMult, ComplEx, RotatE) | ✅ Selected (verify before Ch8) |
| Neo4j Community Edition | Docker | Ongoing | Property graph database | ✅ Selected (Docker) |

