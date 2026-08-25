# Knowledge Graph Book — Direct Source Pack

Prepared/checked: **2026-08-25**

Purpose: give Claude Code exact canonical URLs so Phase 0 research does **not** depend on a search engine.

## Non-negotiable fetch policy

1. Fetch the exact URL directly with HTTP (`curl -L`, `wget`, Python `httpx/requests`, or the environment's URL fetcher).
2. If an authoritative URL fails, mark it `FETCH_FAILED`; do **not** silently fill the gap from model memory.
3. Record retrieval timestamp, HTTP status, final URL after redirects, page title, document version/status, and SHA256 when practical.
4. For W3C, extract the **Status of This Document** and publication/version history. Stable Recommendations are the teaching baseline; CR/WD/drafts are emerging material.
5. For copyrighted books/papers/course notes, store metadata + research notes + short necessary excerpts only. Write original prose and cite.
6. Do not bulk-download YouTube videos/transcripts. Video is supplemental.
7. `knowledgegraphs.org` is optional. It is a portal, not the source-of-truth backbone.

### Suggested direct-fetch commands

```bash
curl -L --fail --retry 3 --retry-delay 2 -A 'Mozilla/5.0 knowledge-graph-book-research' 'URL'

# PDF
curl -L --fail --retry 3 -A 'Mozilla/5.0 knowledge-graph-book-research' -o source.pdf 'URL'
pdftotext source.pdf source.txt

# Record a digest if caching a permitted local copy
sha256sum source.pdf
```

## Source manifest

| ID | Ch. | Priority | Type | Source | URL | Expected status / note |
|---|---|---|---|---|---|---|
| P01 | META | P0 | REFERENCE_REPO | ai-agent-book — pedagogical reference | https://github.com/bojieli/ai-agent-book | Repository. Study pedagogy/structure only; do not copy text/code. |
| P02 | META | P2 | PORTAL | knowledgegraphs.org | https://knowledgegraphs.org/ | Portal. Optional portal only; direct fetch may be unreliable. Not a curriculum backbone. |
| S01 | 1-10 | P0 | ACADEMIC_COURSE | Stanford CS520 — Knowledge Graphs | https://web.stanford.edu/class/cs520/ | Course site. Academic backbone. |
| S02 | 1-10 | P0 | ACADEMIC_NOTES | Stanford CS520 — Table of Contents | https://web.stanford.edu/class/cs520/2020/notes/Table_Of_Contents.html | Course notes. Use as curriculum map. |
| S03 | 1 | P0 | ACADEMIC_NOTES | What is a Knowledge Graph? | https://web.stanford.edu/class/cs520/2020/notes/What_is_a_Knowledge_Graph.html | Course notes. Core Chapter 1 source. |
| S04 | 2-3 | P0 | ACADEMIC_NOTES | What Are Graph Data Models? | https://web.stanford.edu/class/cs520/2020/notes/What_Are_Graph_Data_Models.html | Course notes. RDF vs property graph. |
| S05 | 3-4 | P0 | ACADEMIC_NOTES | How To Create A Knowledge Graph | https://web.stanford.edu/class/cs520/2020/notes/How_To_Create_A_Knowledge_Graph.html | Course notes. Schema/modeling/identity/reification. |
| S06 | 7 | P0 | ACADEMIC_NOTES | How To Create A Knowledge Graph From Structured Data | https://web.stanford.edu/class/cs520/2020/notes/How_To_Create_A_Knowledge_Graph_From_Data.html | Course notes. Structured acquisition/integration. |
| S07 | 7 | P0 | ACADEMIC_NOTES | How To Create A Knowledge Graph From Text | https://web.stanford.edu/class/cs520/2020/notes/How_To_Create_A_Knowledge_Graph_From_Text.html | Course notes. Entity/relation extraction. |
| S08 | 5,8 | P0 | ACADEMIC_NOTES | What Are Some Knowledge Graph Inference Algorithms? | https://web.stanford.edu/class/cs520/2020/notes/What_Are_Some_Inference_Algorithms.html | Course notes. Deductive and graph inference. |
| S09 | 9 | P1 | ACADEMIC_NOTES | How Do Users Interact With A Knowledge Graph? | https://web.stanford.edu/class/cs520/2020/notes/How_Do_Users_Interact_With_a_Knowledge_Graph.html | Course notes. Interaction/search/QA. |
| S10 | 6,10 | P0 | ACADEMIC_NOTES | How To Evolve A Knowledge Graph | https://web.stanford.edu/class/cs520/2020/notes/How_To_Evolve_A_Knowledge_Graph.html | Course notes. Evolution/truth maintenance. |
| S11 | 10 | P1 | ACADEMIC_NOTES | What Are Some High Value Use Cases Of Knowledge Graphs? | https://web.stanford.edu/class/cs520/2020/notes/What_Are_Some_High_Value_Use_Cases_Of_Knowledge_Graphs.html | Course notes. Application framing. |
| S12 | 8-10 | P1 | ACADEMIC_NOTES | How Do Knowledge Graphs Relate To AI? | https://web.stanford.edu/class/cs520/2020/notes/How_do_Knowledge_Graphs_Relate_To_AI.html | Course notes. KG + AI. |
| S13 | 1-10 | P2 | VIDEO_COURSE | Stanford CS520 YouTube playlist | https://www.youtube.com/playlist?list=PLDhh0lALedc7LC_5wpi5gDnPRnu1GSyRG | Supplemental video. Supplement only; do not bulk-download copyrighted video/transcripts. |
| H01 | 1-10 | P0 | ACADEMIC_BOOK | Knowledge Graphs — Aidan Hogan et al. | https://kgbook.org/ | Springer book site. Research/paraphrase/cite. Do not copy substantial text/figures. |
| O01 | 3-4 | P0 | ACADEMIC_GUIDE | Ontology Development 101 — Stanford/Protégé | https://protege.stanford.edu/publications/ontology_development/ontology101.pdf | PDF guide. Ontology engineering methodology. |
| O02 | 4 | P1 | OFFICIAL_DOCS | Protégé documentation | https://protegeproject.github.io/protege/ | Official docs. Optional hands-on ontology editor. |
| R11-01 | 2 | P0 | STANDARD | RDF 1.1 Primer | https://www.w3.org/TR/rdf11-primer/ | W3C Recommendation. Stable teaching baseline. |
| R11-02 | 2-3 | P0 | STANDARD | RDF 1.1 Concepts and Abstract Syntax | https://www.w3.org/TR/rdf11-concepts/ | W3C Recommendation. Formal data model. |
| R11-03 | 4-5 | P0 | STANDARD | RDF Schema 1.1 | https://www.w3.org/TR/rdf-schema/ | W3C Recommendation. RDFS vocabulary/semantics. |
| R11-04 | 5 | P1 | STANDARD | RDF 1.1 Semantics | https://www.w3.org/TR/rdf11-mt/ | W3C Recommendation. Formal entailment semantics. |
| R11-05 | 2 | P0 | STANDARD | RDF 1.1 Turtle | https://www.w3.org/TR/turtle/ | W3C Recommendation. Primary human-readable serialization for labs. |
| R11-06 | 2-3 | P1 | STANDARD | RDF 1.1 TriG | https://www.w3.org/TR/trig/ | W3C Recommendation. RDF datasets / named graphs. |
| R11-07 | 2 | P2 | STANDARD | JSON-LD 1.1 | https://www.w3.org/TR/json-ld11/ | W3C Recommendation. Optional web serialization/context lesson. |
| SP11-01 | 2,9 | P0 | STANDARD | SPARQL 1.1 Overview | https://www.w3.org/TR/sparql11-overview/ | W3C Recommendation. Stable baseline. |
| SP11-02 | 2,9 | P0 | STANDARD | SPARQL 1.1 Query Language | https://www.w3.org/TR/sparql11-query/ | W3C Recommendation. Primary SPARQL query reference. |
| SP11-03 | 5 | P1 | STANDARD | SPARQL 1.1 Entailment Regimes | https://www.w3.org/TR/sparql11-entailment/ | W3C Recommendation. SPARQL + entailment. |
| R12-01 | 2,3,6 | P1 | STANDARD_DRAFT | RDF 1.2 Concepts and Abstract Data Model | https://www.w3.org/TR/rdf12-concepts/ | Verify current W3C status at fetch time. Emerging material, including triple terms/reification. Do not teach as stable baseline. |
| R12-02 | META | P0 | STANDARD_HISTORY | RDF 1.2 Concepts publication history | https://www.w3.org/standards/history/rdf12-concepts/ | W3C publication history. Use to verify exact status/date. |
| R12-03 | 2,3,6 | P1 | STANDARD_DRAFT | RDF 1.2 Primer | https://www.w3.org/TR/rdf12-primer/ | Verify current W3C status at fetch time. Emerging primer. |
| R12-04 | 2 | P2 | STANDARD_DRAFT | RDF 1.2 Turtle | https://www.w3.org/TR/rdf12-turtle/ | Verify current W3C status at fetch time. Emerging syntax. |
| R12-05 | 3,6 | P2 | STANDARD_DRAFT | RDF 1.2 TriG | https://www.w3.org/TR/rdf12-trig/ | Verify current W3C status at fetch time. Emerging datasets syntax. |
| R12-06 | 5,6 | P2 | STANDARD_DRAFT | RDF 1.2 Semantics | https://www.w3.org/TR/rdf12-semantics/ | Verify current W3C status at fetch time. Emerging formal semantics. |
| R12-07 | 4-5 | P2 | STANDARD_DRAFT | RDF Schema 1.2 | https://www.w3.org/TR/rdf12-schema/ | Verify current W3C status at fetch time. Emerging RDFS. |
| SP12-01 | 2,9 | P1 | STANDARD_DRAFT | SPARQL 1.2 Query Language | https://www.w3.org/TR/sparql12-query/ | Verify current W3C status at fetch time. Emerging; stable curriculum remains SPARQL 1.1. |
| SP12-02 | META | P0 | STANDARD_HISTORY | SPARQL 1.2 Query publication history | https://www.w3.org/standards/history/sparql12-query/ | W3C publication history. Verify exact status/date. |
| SP12-03 | 2,9 | P2 | STANDARD_DRAFT | SPARQL 1.2 Protocol | https://www.w3.org/TR/sparql12-protocol/ | Verify current W3C status at fetch time. Emerging. |
| SP12-04 | 2,10 | P2 | STANDARD_DRAFT | SPARQL 1.2 Update | https://www.w3.org/TR/sparql12-update/ | Verify current W3C status at fetch time. Emerging. |
| SP12-05 | 5 | P2 | STANDARD_DRAFT | SPARQL 1.2 Entailment Regimes | https://www.w3.org/TR/sparql12-entailment/ | Verify current W3C status at fetch time. Emerging. |
| OWL-01 | 4-5 | P0 | STANDARD | OWL 2 Web Ontology Language — Document Overview | https://www.w3.org/TR/owl2-overview/ | W3C Recommendation. OWL family map. |
| OWL-02 | 4-5 | P0 | STANDARD | OWL 2 Primer | https://www.w3.org/TR/owl2-primer/ | W3C Recommendation. Primary pedagogical OWL source. |
| OWL-03 | 4-5 | P1 | STANDARD | OWL 2 Structural Specification and Functional-Style Syntax | https://www.w3.org/TR/owl2-syntax/ | W3C Recommendation. Formal model. |
| OWL-04 | 4-5 | P1 | STANDARD | OWL 2 Profiles | https://www.w3.org/TR/owl2-profiles/ | W3C Recommendation. EL/QL/RL trade-offs. |
| OWL-05 | 4-5 | P2 | STANDARD | OWL 2 Mapping to RDF Graphs | https://www.w3.org/TR/owl2-mapping-to-rdf/ | W3C Recommendation. OWL/RDF mapping. |
| OWL-06 | 4-5 | P2 | STANDARD | OWL 2 RDF-Based Semantics | https://www.w3.org/TR/owl2-rdf-based-semantics/ | W3C Recommendation. Advanced semantics. |
| PAT-01 | 3,6 | P1 | W3C_NOTE | Defining N-ary Relations on the Semantic Web | https://www.w3.org/TR/swbp-n-aryRelations/ | W3C Working Group Note. Model contextual/qualified relationships. |
| SKOS-01 | 1,3,4 | P2 | STANDARD | SKOS Simple Knowledge Organization System Reference | https://www.w3.org/TR/skos-reference/ | W3C Recommendation. Taxonomies/thesauri/controlled vocabularies. |
| TIME-01 | 6,10 | P1 | STANDARD | Time Ontology in OWL | https://www.w3.org/TR/owl-time/ | Verify current W3C status/version. Temporal modeling; record exact version/status. |
| SH-01 | 5,7,10 | P0 | STANDARD | Shapes Constraint Language (SHACL) | https://www.w3.org/TR/shacl/ | W3C Recommendation. Stable validation baseline. |
| SH-02 | 5,7,10 | P1 | STANDARD_DRAFT | SHACL 1.2 Core | https://www.w3.org/TR/shacl12-core/ | Verify current W3C status at fetch time. Emerging; clearly label. |
| SH-03 | META | P1 | STANDARD_HISTORY | SHACL 1.2 Core publication history | https://www.w3.org/standards/history/shacl12-core/ | W3C publication history. Verify exact status/date. |
| SH-04 | 5 | P2 | STANDARD_DRAFT | SHACL 1.2 SPARQL Extensions | https://www.w3.org/TR/shacl12-sparql/ | Verify current W3C status at fetch time. Optional advanced validation. |
| SH-05 | 5 | P2 | STANDARD_DRAFT | SHACL 1.2 Node Expressions | https://www.w3.org/TR/shacl12-node-expr/ | Verify current W3C status at fetch time. Optional advanced material. |
| PROV-01 | 6,10 | P0 | STANDARD | PROV-O: The PROV Ontology | https://www.w3.org/TR/prov-o/ | W3C Recommendation. Canonical RDF/OWL provenance model. |
| PROV-02 | 6,10 | P0 | W3C_NOTE | PROV Model Primer | https://www.w3.org/TR/prov-primer/ | W3C Working Group Note. Start here before PROV-O/DM. |
| PROV-03 | 6,10 | P1 | STANDARD | PROV-DM: The PROV Data Model | https://www.w3.org/TR/prov-dm/ | W3C Recommendation. Conceptual provenance model. |
| PROV-04 | META | P1 | W3C_NOTE | PROV Overview | https://www.w3.org/TR/prov-overview/ | W3C Working Group Note. Map of PROV family. |
| WD-01 | 3,6,9 | P0 | REAL_WORLD_KG | Wikidata Data Model | https://www.wikidata.org/wiki/Wikidata:Data_model/en | Living documentation. Real-world statement/claim model. |
| WD-02 | 6 | P0 | REAL_WORLD_KG | Wikidata Help: Statements | https://www.wikidata.org/wiki/Help:Statements/en | Living documentation. Statement anatomy. |
| WD-03 | 6 | P0 | REAL_WORLD_KG | Wikidata Help: Qualifiers | https://www.wikidata.org/wiki/Help:Qualifiers/en | Living documentation. Scope/time/context. |
| WD-04 | 6 | P0 | REAL_WORLD_KG | Wikidata Help: Ranking | https://www.wikidata.org/wiki/Help:Ranking | Living documentation. Preferred/normal/deprecated rank. |
| WD-05 | 2,6,9 | P0 | REAL_WORLD_KG | Wikidata SPARQL Tutorial | https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial/en | Living documentation. Hands-on public KG querying. |
| WD-06 | 3,6 | P1 | OFFICIAL_DOCS | Wikibase DataModel | https://www.mediawiki.org/wiki/Wikibase/DataModel | Official documentation. Underlying Wikibase data model. |
| WD-07 | 2,6 | P1 | MACHINE_READABLE_DATA | Wikidata Q42 JSON example | https://www.wikidata.org/wiki/Special:EntityData/Q42.json | Live machine-readable entity. Good reproducible parsing example. |
| WD-08 | 2,6 | P1 | MACHINE_READABLE_DATA | Wikidata Q42 Turtle example | https://www.wikidata.org/wiki/Special:EntityData/Q42.ttl | Live machine-readable entity. Compare with JSON representation. |
| WD-09 | 2,9 | P1 | QUERY_ENDPOINT | Wikidata Query Service | https://query.wikidata.org/ | Public service. Interactive SPARQL endpoint; rate limits apply. |
| WD-10 | 2,9 | P2 | QUERY_ENDPOINT | Wikidata SPARQL endpoint | https://query.wikidata.org/sparql | Public service. Use politely, cache tiny examples, respect rate limits. |
| N4J-01 | 2 | P0 | OFFICIAL_COURSE | Neo4j Fundamentals | https://graphacademy.neo4j.com/courses/neo4j-fundamentals/ | Official course. Property-graph lab. |
| N4J-02 | 2,9 | P0 | OFFICIAL_COURSE | Cypher Fundamentals | https://graphacademy.neo4j.com/courses/cypher-fundamentals/ | Official course. Query lab. |
| N4J-03 | 2-3 | P0 | OFFICIAL_COURSE | Graph Data Modeling Fundamentals | https://graphacademy.neo4j.com/courses/modeling-fundamentals/ | Official course. Modeling trade-offs. |
| N4J-04 | 7,9 | P1 | OFFICIAL_COURSE | Building Knowledge Graphs with LLMs | https://graphacademy.neo4j.com/courses/llm-knowledge-graph-construction/ | Official course. Use only after foundations. |
| N4J-05 | 2-3 | P0 | OFFICIAL_DOCS | Neo4j Data Modeling | https://neo4j.com/docs/getting-started/data-modeling/ | Official docs. Property graph design. |
| N4J-06 | 2,9 | P0 | OFFICIAL_DOCS | Neo4j Cypher Manual | https://neo4j.com/docs/cypher-manual/current/ | Official docs. Primary Cypher reference. |
| N4J-07 | 2,7,9 | P1 | OFFICIAL_DOCS | Neo4j Python Driver Manual | https://neo4j.com/docs/python-manual/current/ | Official docs. Python labs. |
| N4J-08 | 2 | P1 | OFFICIAL_DOCS | Neo4j Docker documentation | https://neo4j.com/docs/operations-manual/current/docker/ | Official docs. Local reproducible server. |
| GQL-01 | 2 | P1 | STANDARD | ISO/IEC 39075:2024 — GQL | https://www.iso.org/standard/76120.html | International Standard. Graph Query Language standard metadata. |
| GQL-02 | 2 | P1 | OFFICIAL_DOCS | Neo4j Cypher — GQL conformance | https://neo4j.com/docs/cypher-manual/current/appendix/gql-conformance/ | Official docs. Cypher/GQL relationship. |
| GQL-03 | 2 | P2 | COMMUNITY_STANDARD_INFO | GQL Standards | https://www.gqlstandards.org/ | Community standards site. Supplemental context. |
| TOOL-01 | 2-7 | P0 | OFFICIAL_DOCS | RDFLib documentation | https://rdflib.readthedocs.io/ | Official docs. Primary Python RDF lab library. |
| TOOL-02 | 2-7 | P1 | SOURCE_REPO | RDFLib GitHub | https://github.com/RDFLib/rdflib | Repository. Verify release/maintenance/license. |
| TOOL-03 | 5,7,10 | P0 | SOURCE_REPO | pySHACL | https://github.com/RDFLib/pySHACL | Repository. SHACL labs; verify current release. |
| TOOL-04 | 5 | P1 | SOURCE_REPO | OWL-RL | https://github.com/RDFLib/OWL-RL | Repository. RDFS/OWL RL reasoning experiments. |
| TOOL-05 | 4-5 | P2 | OFFICIAL_DOCS | Owlready2 documentation | https://owlready2.readthedocs.io/ | Official docs. Optional OWL reasoning path. |
| TOOL-06 | 8 | P0 | OFFICIAL_DOCS | PyKEEN documentation | https://pykeen.readthedocs.io/ | Official docs. KG embeddings. |
| TOOL-07 | 1,8 | P0 | OFFICIAL_DOCS | NetworkX documentation | https://networkx.org/documentation/stable/ | Official docs. Graph basics/analytics. |
| ML-01 | 8 | P0 | ACADEMIC_COURSE | Stanford CS224W — Machine Learning with Graphs | https://snap.stanford.edu/class/cs224w-2022/ | Course site. Focus on KG embeddings/reasoning lectures. |
| LLMKG-01 | 9-10 | P0 | RESEARCH_PAPER | Unifying Large Language Models and Knowledge Graphs: A Roadmap | https://arxiv.org/abs/2306.08302 | Research paper. Taxonomy: KG-enhanced LLM, LLM-augmented KG, synergized LLM+KG. |
| LLMKG-02 | 9-10 | P1 | RESEARCH_PAPER_PDF | Unifying LLMs and KGs — PDF | https://arxiv.org/pdf/2306.08302 | Research paper PDF. Read/paraphrase; do not reproduce substantial text. |
| GR-01 | 9 | P0 | OFFICIAL_DOCS | Microsoft GraphRAG documentation | https://microsoft.github.io/graphrag/ | Official docs. Case study/reference implementation, not curriculum foundation. |
| GR-02 | 9 | P0 | OFFICIAL_DOCS | GraphRAG indexing architecture | https://microsoft.github.io/graphrag/index/architecture/ | Official docs. Indexing architecture. |
| GR-03 | 9 | P1 | OFFICIAL_DOCS | GraphRAG default dataflow | https://microsoft.github.io/graphrag/index/default_dataflow/ | Official docs. Entities/relationships/claims/community reports pipeline. |
| GR-04 | 9 | P1 | OFFICIAL_DOCS | GraphRAG indexing methods | https://microsoft.github.io/graphrag/index/methods/ | Official docs. Method details. |
| GR-05 | 9 | P0 | OFFICIAL_DOCS | GraphRAG query overview | https://microsoft.github.io/graphrag/query/overview/ | Official docs. Local/global/DRIFT/baseline. |
| GR-06 | 9 | P1 | OFFICIAL_DOCS | GraphRAG local search | https://microsoft.github.io/graphrag/query/local_search/ | Official docs. Entity-centric local retrieval. |
| GR-07 | 9 | P1 | OFFICIAL_DOCS | GraphRAG global search | https://microsoft.github.io/graphrag/query/global_search/ | Official docs. Community-report/global retrieval. |
| GR-08 | 9 | P1 | OFFICIAL_DOCS | GraphRAG DRIFT search | https://microsoft.github.io/graphrag/query/drift_search/ | Official docs. DRIFT retrieval. |
| GR-09 | 9 | P1 | SOURCE_REPO | Microsoft GraphRAG GitHub | https://github.com/microsoft/graphrag | Repository. Check current maintenance/status notice before depending on implementation. |
| GR-10 | 9 | P0 | RESEARCH_PAPER | From Local to Global: A Graph RAG Approach to Query-Focused Summarization | https://arxiv.org/abs/2404.16130 | Research paper. GraphRAG paper. |
| GR-11 | 9 | P1 | RESEARCH_PAPER_PDF | From Local to Global — PDF | https://arxiv.org/pdf/2404.16130 | Research paper PDF. Read/paraphrase; do not reproduce substantial text. |

## Minimum Phase 0 reading order

If time/context is limited, fetch/read in this order first:

1. P01 — `ai-agent-book` (pedagogy only)
2. S02 → S03 → S04 → S05 → S07 → S08 → S10 — Stanford CS520 backbone
3. H01 — Hogan et al. as the field map
4. R11-01/02/03/05 + SP11-01/02 — stable RDF/RDFS/SPARQL baseline
5. OWL-01/02 + SH-01 + PROV-02/01 — semantics, validation, provenance
6. WD-01/02/03/04/05 — real-world claims/qualifiers/references/rank
7. N4J-03/05/06 — property-graph modeling/query lab
8. R12-01/02 + SP12-01/02 + SH-02/03 — current-development audit, clearly separated from stable baseline
9. ML-01 — inductive knowledge / embeddings
10. LLMKG-01 + GR-01/02/05/10 — LLM/KG and GraphRAG only after foundations

## Phase 0 cache/index recommendation

Create (gitignored) `.research/cache/` for fetched material that may legally be cached, and commit only:

```text
docs/SOURCES.md
docs/SOURCE_MATRIX.md
docs/RESEARCH_LOG.md
docs/CURRICULUM_RATIONALE.md
docs/source_index.json
```

Each `source_index.json` record should include:

```json
{
  "id": "R12-01",
  "canonical_url": "https://www.w3.org/TR/rdf12-concepts/",
  "fetched_at": "ISO-8601",
  "http_status": 200,
  "final_url": "...",
  "title": "...",
  "document_status": "...",
  "publication_date": "...",
  "sha256": "...",
  "used_in_chapters": ["2", "3", "6"],
  "notes": "..."
}
```