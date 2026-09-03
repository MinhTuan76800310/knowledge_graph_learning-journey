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
| OWL 2 Profiles (EL, QL, RL) | 2 | Recommendation | 2012-12-11 | https://www.w3.org/TR/owl2-profiles/ | Stable baseline; EL grammar (Sec 2, BNF Sec 6.1) admits property chains |
| Overview of the Rule Interchange Format (RIF) | 1.0 | Recommendation | 2010-06-22 | https://www.w3.org/TR/rif-overview/ | Stable; RIF-Core = Datalog; RL interop anchor |
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
| The Description Logic Handbook (2nd ed.) | Baader, Calvanese, McGuinness, Nardi, Patel-Schneider (Cambridge UP, 2007) | ACADEMIC | https://www.cambridge.org/9780521876254 | Canonical DL formal-semantics reference behind OWL's design | 4 (EN) |
| FaCT++ Description Logic Reasoner | Tsarkov & Horrocks, IJCAR 2006 | RESEARCH_PAPER | https://doi.org/10.1007/11814771_26 | Classic optimized-tableau DL reasoner | 4 (EN) |
| Hypertableau Reasoning for Description Logics (HermiT) | Motik, Shearer & Horrocks, JAIR 2009 | RESEARCH_PAPER | https://www.cs.ox.ac.uk/isg/tools/HermiT/ | OWL 2 DL reasoner; Direct Semantics conformance | 4 (EN) |
| Konclude: System Description | Steigmiller, Liebig & Glimm, JWS 2014 | RESEARCH_PAPER | https://doi.org/10.1016/j.websem.2014.06.003 | State-of-the-art OWL 2 DL reasoner | 4 (EN) |
| Creating Semantic Web Contents with Protégé-2000 | Noy et al., IEEE Intelligent Systems 2001 | RESEARCH_PAPER | https://protegeproject.github.io/protege/ | The OWL editor where Ch4 axioms are authored | 4 (EN) |
| The DL-Lite Family and Relations | Artale, Calvanese, Kontchakov & Zakharyaschev, JAIR 2009 | RESEARCH_PAPER | https://arxiv.org/abs/1401.3487 | Tractable DL family underlying OWL 2 QL | 4 (EN) |
| Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | Lewis et al., 2020 | RESEARCH_PAPER | https://arxiv.org/abs/2005.11401 | NeurIPS 2020 paper; RAG origin | 9 |
| Dense Passage Retrieval for Open-Domain Question Answering | Karpukhin et al., 2020 | RESEARCH_PAPER | https://arxiv.org/abs/2004.04906 | EMNLP 2020 paper; dual-encoder dense retrieval | 9 |
| From Local to Global: A Graph RAG Approach to Query-Focused Summarization | Edge et al., 2024 | RESEARCH_PAPER | https://arxiv.org/abs/2404.16130 | Microsoft GraphRAG primary paper; one implementation family | 9 |
| The Probabilistic Relevance Framework: BM25 and Beyond | Robertson & Zaragoza, 2009 | RESEARCH_PAPER | https://doi.org/10.1561/1500000019 | Foundations and Trends in IR 3(4); BM25 primary survey | 9 |
| Introduction to Information Retrieval | Manning, Raghavan & Schütze, 2008 | ACADEMIC | https://nlp.stanford.edu/IR-book/ | Standard IR textbook (open online edition) | 9 |
| Cumulated gain-based evaluation of IR techniques | Järvelin & Kekäläinen, 2002 | RESEARCH_PAPER | https://doi.org/10.1145/582415.582418 | ACM TOIS 20(4); nDCG primary source | 9 |
| Reciprocal rank fusion outperforms condorcet and individual rank learning methods | Cormack, Clarke & Buettcher, 2009 | RESEARCH_PAPER | https://doi.org/10.1145/1571941.1572114 | SIGIR 2009; RRF primary source | 9 |
| Passage Re-ranking with BERT | Nogueira & Cho, 2019 | RESEARCH_PAPER | https://arxiv.org/abs/1901.04085 | Two-stage retrieval; cross-encoder re-ranking | 9 |
| Lost in the Middle: How Language Models Use Long Contexts | Liu et al., 2023 | RESEARCH_PAPER | https://arxiv.org/abs/2307.03172 | TACL 2023; context-position effects | 9 |
| Measuring Attribution in Natural Language Generation Models | Rashkin et al., 2021 | RESEARCH_PAPER | https://arxiv.org/abs/2112.12870 | AIS criterion; attribution vs truth | 9 |
| Enabling Large Language Models to Generate Text with Citations | Gao, Yen, Yu & Chen, 2023 | RESEARCH_PAPER | https://arxiv.org/abs/2305.14627 | EMNLP 2023; ALCE citation benchmark | 9 |
| Introduction to Neural Network based Approaches for Question Answering over Knowledge Graphs | Chakraborty et al., 2019 | RESEARCH_PAPER | https://arxiv.org/abs/1907.09361 | KGQA survey; paradigms and subproblems | 9 |
| Unifying Large Language Models and Knowledge Graphs: A Roadmap | Zhu et al., 2023 | RESEARCH_PAPER | https://arxiv.org/abs/2306.08302 | Survey paper; DOI 10.1109/TKDE.2024.3352100; used in Chapter 9 only | 9 |
| Soufflé: On Synthesis of Program Analyzers | Jordan, Scholz & Subotić, CAV 2016 | RESEARCH_PAPER | https://doi.org/10.1007/978-3-319-41540-6_23 | LNCS 9779:422–430; Datalog→parallel C++; industrial forward-chaining fixpoint | 5 (EN) |
| Datalog and Recursive Query Processing | Green, Huang, Loo & Zhou, 2013 | RESEARCH_PAPER | https://doi.org/10.1561/1900000017 | Foundations and Trends in Databases 6(2–3):105–195; Datalog fixpoint semantics survey | 5 (EN) |
| On Closed World Data Bases | Reiter, 1978 | RESEARCH_PAPER | https://doi.org/10.1007/978-1-4684-3384-5_3 | Logic and Data Bases (Gallaire & Minker eds.) pp. 55–76; formalizes the CWA | 5 (EN) |
| A Logic for Default Reasoning | Reiter, 1980 | RESEARCH_PAPER | https://doi.org/10.1016/0004-3702(80)90014-4 | Artificial Intelligence 13(1–2):81–132; non-monotonic default logic | 5 (EN) |
| Semantics and Complexity of SPARQL | Pérez, Arenas & Gutiérrez, 2009 | RESEARCH_PAPER | https://doi.org/10.1145/1567274.1567278 | ACM TODS 34(3):16:1–16:45; formal SPARQL relational algebra (join, left join, filter, union) and evaluation complexity | 2 (EN) |
| An Introduction to Graph Data Management | Angles & Gutiérrez, 2018 | RESEARCH_PAPER | https://doi.org/10.1007/978-3-319-96193-4_1 | Springer LNCS 11510, pp. 1–32; formal attributed property-graph model | 2 (EN) |

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
| SNOMED CT — What is SNOMED CT? | SNOMED International | CASE_STUDY | https://www.snomed.org/what-is-snomed-ct | 4 (EN) |
| ELK Reasoner | Live Ontologies Project | OFFICIAL_DOCUMENTATION | https://github.com/liveontologies/elk-reasoner | 4 (EN) |
| Snorocket DL Classifier | CSIRO Australian e-Health Research Centre | OFFICIAL_DOCUMENTATION | https://github.com/aehrc/snorocket | 4 (EN) |
| Gene Ontology Documentation | Gene Ontology Consortium | CASE_STUDY | https://geneontology.org/docs/ontology-documentation/ | 4 (EN) |
| UBERON Multi-Species Anatomy Ontology | OBO Foundry / Uberon project | CASE_STUDY | https://github.com/obophenotype/uberon | 4 (EN) |
| Ontop Virtual Knowledge Graph System | Ontop project | OFFICIAL_DOCUMENTATION | https://ontop-vkg.org/guide/ | 4 (EN) |
| RDFox | Oxford Semantic Technologies | CASE_STUDY | https://www.cs.ox.ac.uk/isg/tools/RDFox/ | 4 (EN) |
| Apache Jena Inference Engine | Apache Software Foundation | OFFICIAL_DOCUMENTATION | https://jena.apache.org/documentation/inference/ | 4 (EN) |
| OWL-RL (RDF Closure Rules) | RDFLib project | OFFICIAL_DOCUMENTATION | https://github.com/RDFLib/OWL-RL | 5 (EN) |
| pySHACL (SHACL validator) | RDFLib project | OFFICIAL_DOCUMENTATION | https://github.com/RDFLib/pySHACL | 5 (EN) |
| SHACL Test Suite | W3C Data Shapes WG | OFFICIAL_DOCUMENTATION | https://w3c.github.io/data-shapes/data-shapes-test-suite/ | 5 (EN) |

## Python Libraries Evaluated

| Library | Latest Version | Last Release | Purpose | Decision |
|---|---|---|---|---|
| RDFLib | 7.6.0 | 2026-02-13 | RDF manipulation, Turtle, SPARQL | ✅ Selected |
| pySHACL | 0.40.1 | 2026-07-28 | SHACL validation | ✅ Selected |
| owlrl | 7.6.2 | 2026-07-08 | RDFS/OWL reasoning | ✅ Selected |
| NetworkX | 3.6.1 | 2025+ | Graph analytics, centrality, community detection | ✅ Selected |
| PyKEEN | 1.11.1 | 2025-04-24 | KG embeddings (TransE, DistMult, ComplEx, RotatE) | ✅ Selected (verify before Ch8) |
| Neo4j Community Edition | Docker | Ongoing | Property graph database | ✅ Selected (Docker) |

