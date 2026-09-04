# Source Matrix — Knowledge Graph Book

Maps every major topic to its primary and secondary authoritative sources.
Primary sources are preferred; secondary sources supplement or provide alternative perspectives.

Last verified: 2026-09-04

| Topic | Primary source | Secondary source | Source type | Stable/draft | Why authoritative | Chapters |
|---|---|---|---|---|---|---|
| What is a Knowledge Graph | Stanford CS520 Lecture 1 | Hogan et al., *Knowledge Graphs* Ch.1 | ACADEMIC | Stable | University course + peer-reviewed textbook define the field's conceptual boundaries | 1, introduction |
| Graph data models (RDF vs Property Graph) | W3C RDF 1.1 Concepts | Neo4j Graph Data Modeling Fundamentals | STANDARD / OFFICIAL_DOCUMENTATION | Stable | W3C defines RDF; Neo4j defines property graph model | 1, 2 |
| RDF triples, IRIs, literals, blank nodes | W3C RDF 1.1 Primer | W3C RDF 1.2 Concepts (CR) | STANDARD | Stable baseline + Emerging CR | RDF 1.1 is stable REC; 1.2 CR introduces triple terms | 2, 3, 6 |
| RDF 1.2 triple terms & reification | W3C RDF 1.2 Concepts (CR 2026-04-07) | W3C RDF 1.2 Primer (WD) | STANDARD | Candidate Recommendation | Introduces triple-term-based reification (rdf:reifies) as preferred modern mechanism; RDF 1.1 reification vocabulary remains as legacy for compatibility | 3, 6 |
| SPARQL 1.1 query language | W3C SPARQL 1.1 Overview / Query (REC 2013) | Stanford CS520 SPARQL lectures | STANDARD / ACADEMIC | Stable Recommendation | Official query language for RDF graphs | 2, 5, 9 |
| SPARQL 1.2 query language | W3C SPARQL 1.2 Query (WD 2026-08-27) | — | STANDARD | Working Draft | Emerging update; not yet stable — label clearly in text | 2 (callout) |
| Turtle serialization | W3C Turtle REC 2014 | RDFLib documentation | STANDARD / OFFICIAL_DOCUMENTATION | Stable | Canonical human-readable RDF syntax | 2 |
| RDFS semantics & entailment | W3C RDF 1.1 Semantics (REC 2014) + W3C RDF Schema 1.1 (REC 2014) | Hogan et al. Ch.4 Deductive Knowledge | STANDARD / ACADEMIC | Stable | RDF-MT defines normative model-theoretic semantics and entailment patterns; RDFS spec defines vocabulary. Appendix A covers rule-based operationalization completeness nuances. | 4, 5 |
| OWL 2 ontology language | W3C OWL 2 Overview (REC 2012) | Stanford Ontology Development 101 | STANDARD / TUTORIAL | Stable | Formal ontology language with description logic semantics | 4, 5 |
| OWL 2 structural specification & functional-style syntax | W3C OWL 2 Structural Specification (REC 2012) | — | STANDARD | Stable | Defines abstract syntax and structural constraints of OWL 2 | 4 |
| OWL 2 direct semantics | W3C OWL 2 Direct Semantics (REC 2012) | — | STANDARD | Stable | Model-theoretic semantics for OWL 2 DL; interpretations, satisfiability, entailment | 4 |
| OWL 2 profiles (EL, QL, RL) | W3C OWL 2 Profiles (REC 2012) | — | STANDARD | Stable | Tractable fragments: EL (poly-time), QL (query rewriting), RL (rule-based) | 4 |
| Deductive knowledge & Description Logics | Hogan et al. Ch.6 Deductive Knowledge | — | ACADEMIC | Stable | Ontology-based reasoning, DL interpretations, models, entailment, TBox/ABox | 4 |
| Description Logic theory & reasoners (Ch4 enrichment) | Baader et al., *The Description Logic Handbook* (2nd ed.) | FaCT++ (Tsarkov & Horrocks), HermiT (Motik et al.), Konclude (Steigmiller et al.), Protégé (Noy et al.), Horrocks/Sattler/Tobies SROIQ (KR 2006) | ACADEMIC / OFFICIAL_DOCUMENTATION / RESEARCH_PAPER | Stable | Formal-semantics foundation + production reasoner lineage behind OWL's entailment machinery; SROIQ paper fixes OWL 2 DL = SROIQ(D) and its N2EXPTIME combined complexity | 4 |
| OWL 2 EL real-world ontologies & reasoners (Ch4 enrichment) | W3C OWL 2 Profiles (REC 2012) | SNOMED CT, ELK (Kazakov et al.), Snorocket, Gene Ontology, UBERON | STANDARD / CASE_STUDY / OFFICIAL_DOCUMENTATION | Stable (Snorocket: Emerging) | Flagship EL terminology + polynomial-time EL classifiers grounding the EL profile | 4 |
| OWL 2 QL OBDA & DL-Lite (Ch4 enrichment) | W3C OWL 2 Profiles (REC 2012) | Ontop (VKG/OBDA), DL-Lite family (Artale et al., JAIR 2009), Calvanese et al. DL-Lite (JAR 2007) | STANDARD / OFFICIAL_DOCUMENTATION / RESEARCH_PAPER | Stable | Query-rewriting-to-SQL profile and its tractable logical basis; DL-Lite paper establishes FO-rewritability → AC0 data complexity | 4 |
| OWL 2 RL rule engines & Datalog (Ch4 enrichment) | W3C OWL 2 Profiles (REC 2012) | RDFox, Apache Jena GenericRuleReasoner, W3C RIF | STANDARD / OFFICIAL_DOCUMENTATION / CASE_STUDY | Stable | Rule-based scalable reasoning over RDF; Datalog-compatible interchange | 4 |
| SHACL validation | W3C SHACL (REC 2017) | pySHACL documentation | STANDARD / OFFICIAL_DOCUMENTATION | Stable | Constraint validation for RDF graphs; SHACL 1.2 Core WD 2026-08-03 is emerging | 5 |
| SPARQL entailment regimes | W3C SPARQL 1.1 Entailment Regimes (REC 2013) | — | STANDARD | Stable | Defines standard regime IRIs; regimes via Service Description, not FROM | 5 |
| Forward chaining & Datalog engines (Ch5 enrichment) | Hogan et al. Ch.5 Rules and Reasoning | Soufflé (Jordan et al., CAV 2016), Datalog survey (Green et al. 2013), OWL-RL | ACADEMIC / RESEARCH_PAPER / OFFICIAL_DOCUMENTATION | Stable | Industrial fixpoint evaluation grounding the θ + fixpoint mechanism | 5 (EN) |
| SHACL tooling & conformance (Ch5 enrichment) | W3C SHACL (REC 2017) | pySHACL, W3C SHACL Test Suite | OFFICIAL_DOCUMENTATION / STANDARD | Stable | Concrete validator + conformance suite for the target→result pipeline | 5 (EN) |
| Closed World Assumption & non-monotonic reasoning (Ch5 enrichment) | Reiter, "On Closed World Data Bases" (1978) | Reiter, "A Logic for Default Reasoning" (1980) | RESEARCH_PAPER | Stable | Precise origin of the CWA flavor SHACL evokes; contrast with monotonic forward chaining | 5 (EN) |
| PROV-O provenance | W3C PROV-O (REC 2013) | Hogan et al. Ch.7 Context | STANDARD / ACADEMIC | Stable | Standard ontology for provenance, agents, activities | 6 |
| Identity & entity resolution | Hogan et al. Ch.3 Identity | Stanford CS520 Creating KGs from structured data | ACADEMIC | Stable | Comprehensive treatment of IRI identity, sameAs, disambiguation | 3 |
| N-ary relations & reification | W3C "Defining N-ary Relations on the Semantic Web" (Note) | Hogan et al. Ch.2 Data Graphs; W3C RDF 1.2 Concepts (CR) | STANDARD / ACADEMIC | Stable Note + Emerging CR | N-ary relations are a separate modeling problem (patterns: reification, named graphs, blank node clusters). RDF 1.2 triple terms support referencing propositions/reifiers/annotations but do not by themselves solve general n-ary relation modeling. Distinction clarified for Chapter 3. | 3, 6 |
| Named graphs & datasets | W3C RDF 1.1 Concepts § Datasets | W3C SPARQL 1.1 § Named Graphs | STANDARD | Stable | Mechanism for contextualizing triples within named scopes | 3, 6 |
| Ontology engineering methodology | Stanford Ontology Development 101 | Hogan et al. Ch.4 | TUTORIAL / ACADEMIC | Stable | Step-by-step methodology for building ontologies | 4 |
| Knowledge Graph embeddings | Stanford CS224W KG Embeddings lecture | PyKEEN documentation | ACADEMIC / OFFICIAL_DOCUMENTATION | Stable | TransE, DistMult, ComplEx, RotatE foundations | 8 |
| Link prediction & graph learning | Stanford CS224W Reasoning over KGs | NetworkX documentation | ACADEMIC / OFFICIAL_DOCUMENTATION | Stable | Classical and neural approaches to inductive reasoning | 8 |
| Wikidata data model & statements | Wikidata Help:Statements / Qualifiers / References | Wikidata SPARQL Tutorial | CASE_STUDY / TUTORIAL | Stable | Real-world contextualized claims with qualifiers, ranks, sources | 6 |
| Property graph modeling | Neo4j Graph Data Modeling Fundamentals | Neo4j Cypher Fundamentals | OFFICIAL_DOCUMENTATION | Stable | Industry-standard property graph database | 2, 10 |
| Building KGs with LLMs | Neo4j Building KGs with LLMs | Microsoft GraphRAG docs | OFFICIAL_DOCUMENTATION | Stable | Practical LLM-to-graph extraction patterns | 7, 9 |
| GraphRAG architecture | Microsoft GraphRAG indexing architecture | "Unifying LLMs and KGs: A Roadmap" | OFFICIAL_DOCUMENTATION / RESEARCH_PAPER | Stable | Community retrieval augmentation via graph structure | 9 |
| Knowledge acquisition pipeline | Hogan et al. Ch.6 Creation & Enrichment | Stanford CS520 Creating KGs from text | ACADEMIC | Stable | Extraction → resolution → validation pipeline | 7 |
| Knowledge quality assessment | Hogan et al. Ch.7 Quality Assessment | Stanford CS520 KG Evolution | ACADEMIC | Stable | Completeness, consistency, accuracy metrics | 5, 7, 10 |
| Mechanism abstraction (capstone) | Original synthesis | Hogan et al. Ch.4 Deductive Knowledge | ORIGINAL / ACADEMIC | N/A | Cross-domain mechanism recognition as research problem | 4, 10 |
| RDB→RDF mapping (custom) | W3C R2RML (REC 2012) | — | STANDARD | Stable | Triples Map / Subject Map / Predicate-Object Map for custom RDB-to-RDF mapping | 7 |
| RDB→RDF mapping (default) | W3C Direct Mapping (REC 2012) | — | STANDARD | Stable | Automatic table→class, row→resource, column→predicate; shape follows DB schema | 7 |
| Tabular→RDF (CSV/TSV) | W3C Model for Tabular Data + csv2rdf (REC 2015) | — | STANDARD | Stable | Table/row/column/cell model + annotations for generating RDF from tabular data | 7 |
| Record linkage / entity resolution | Fellegi & Sunter (JASA 1969) | Hogan et al. Ch.6 Creation & Enrichment | RESEARCH_PAPER / ACADEMIC | Stable | Comparison vector γ, m/u probabilities, two-threshold decision rule | 7 |
| Schema matching | Rahm & Bernstein (VLDB J 2001) | — | RESEARCH_PAPER | Stable | Element vs structure level; schema/instance/hybrid matchers | 7 |
| SPARQL relational algebra (Ch1-2 enrichment) | Pérez, Arenas & Gutiérrez, "Semantics and Complexity of SPARQL" (ACM TODS 2009) | W3C SPARQL 1.1 Query Language (REC 2013) | RESEARCH_PAPER / STANDARD | Stable | Formal compositional algebra for solution mappings (join, left join, filter, union); NP-complete combined complexity proof | 2 (EN) |
| Property graph formal model (Ch1-2 enrichment) | Angles & Gutiérrez, "An Introduction to Graph Data Management" (Springer 2018) | Neo4j Graph Data Modeling Fundamentals | RESEARCH_PAPER / OFFICIAL_DOCUMENTATION | Stable | Attributed graph tuple formalization grounding the Ch2 7-tuple LPG definition | 2 (EN) |
| Data integration theory | Lenzerini (PODS 2002) | — | RESEARCH_PAPER | Stable | Data integration system (G, S, M); GAV/LAV; sound/complete/exact mappings | 7 |

## Source type legend

- **STANDARD**: W3C Recommendation, Candidate Recommendation, or Working Draft
- **ACADEMIC**: University course material or peer-reviewed textbook
- **OFFICIAL_DOCUMENTATION**: Vendor-maintained docs for tools/platforms
- **RESEARCH_PAPER**: Peer-reviewed conference/journal paper
- **CASE_STUDY**: Real-world system documentation (Wikidata, DBpedia)
- **TUTORIAL**: Educational guide from authoritative organization
- **ORIGINAL**: Synthesis created specifically for this book

## Stability classification rules

- **Stable baseline**: W3C Recommendation or well-established academic textbook edition. Used as main curriculum content.
- **Emerging / Current development**: W3C Candidate Recommendation or Working Draft. Clearly labeled in callout boxes. Never taught as if stable.
- **Experimental**: Pre-standard proposals or active research without consensus. Only mentioned in "Current developments" sections with explicit caveats.

