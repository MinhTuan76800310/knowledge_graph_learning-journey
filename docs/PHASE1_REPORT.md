# Phase 1 Report — knowledge-graph-book

**Date:** 2026-08-25  
**Milestone:** Chapter 1 complete, repository scaffolded, research artifacts produced

---

## Files Created

### Research & Documentation
- `docs/SOURCES.md` — Comprehensive source inventory with W3C spec status verification
- `docs/SOURCE_MATRIX.md` — Topic-to-source mapping with authority justification
- `docs/RESEARCH_LOG.md` — Chronological research decisions and findings
- `docs/CURRICULUM_RATIONALE.md` — Pedagogical sequencing rationale for all 10 chapters
- `docs/GLOSSARY.md` — Chapter 1 terminology (Vietnamese + English)
- `docs/LEARNING_PATH.md` — Reader progression guide
- `docs/DESIGN_DECISIONS.md` — Architecture and tooling decisions with rationale
- `docs/EXPERIMENT_STATUS.md` — Execution evidence for all Chapter 1 experiments

### Repository Infrastructure
- `README.md` — Project overview, setup instructions, contribution guidelines
- `CLAUDE.md` — AI assistant context and conventions
- `AGENTS.md` — Agent development rules and verification checklist
- `pyproject.toml` — Python project configuration with verified dependencies
- `uv.lock` — Reproducible dependency lock file
- `docker-compose.yml` — Neo4j Community Edition service definition

### Book Content
- `book/introduction.md` — Full introduction in Vietnamese
- `book/chapter01.md` — Complete Chapter 1 draft (~400 lines, Vietnamese)

### Chapter 1 Experiments
- `chapter01/exp_1_1_plain_graph.py` + `chapter01/exp_1_1/README.md`
- `chapter01/exp_1_2_data_graph_vs_taxonomy.py` + `chapter01/exp_1_2/README.md`
- `chapter01/exp_1_3_sister_city_kg.py` + `chapter01/exp_1_3/README.md`
- `chapter01/exp_1_4_data_graph_to_kg.py` + `chapter01/exp_1_4/README.md`
- `chapter01/exp_1_5_relation_semantics.py` + `chapter01/exp_1_5/README.md`
- `chapter01/test_experiments.py` — 20 pytest tests covering all experiments

---

## Sources Researched

### W3C Standards (Status Verified 2026-08-25)
| Specification | Status | Date |
|--------------|--------|------|
| RDF 1.1 Concepts | ✅ Recommendation | 2014-02-25 |
| RDF 1.2 Concepts | 🔄 Candidate Recommendation | 2026-04-07 |
| SPARQL 1.1 Query | ✅ Recommendation | 2013-03-21 |
| SPARQL 1.2 Query | 🔄 Working Draft | 2026-08-20 |
| SHACL 1.0 | ✅ Recommendation | 2017-07-20 |
| SHACL 1.2 Core | 🔄 Working Draft | 2026-08-03 | https://www.w3.org/TR/shacl12-core/ |
| OWL 2 Overview | ✅ Recommendation | 2012-12-11 |
| PROV-O | ✅ Recommendation | 2013-04-30 |

### Academic Sources
- Stanford CS520: Knowledge Graphs (web.stanford.edu/class/cs520)
- Hogan et al., *Knowledge Graphs* (kgbook.org) — used as reference only, no copied content
- Stanford CS224W: Machine Learning with Graphs (snap.stanford.edu)
- Stanford Ontology Development 101 (protege.stanford.edu)

### Industry Documentation
- Wikidata Data Model, Statements, Qualifiers, References
- Neo4j Fundamentals, Cypher, Graph Data Modeling
- Microsoft GraphRAG documentation (deferred to Chapter 9)

### Libraries Verified
| Library | Version | Last Release | Status |
|---------|---------|--------------|--------|
| RDFLib | 7.6.0 | 2026-02-13 | ✅ Active |
| pySHACL | 0.40.1 | 2026-07-28 | ✅ Active |
| owlrl | 7.6.2 | 2026-07-08 | ✅ Active |
| NetworkX | 3.6.1 | Recent | ✅ Active |
| PyKEEN | 1.11.1 | 2025-04-24 | ⚠️ Slower cadence but maintained |

---

## Decisions Made

1. **Language policy:** Book content in Vietnamese; code/docs/configs in English. Technical terms kept in English on first occurrence.

2. **Standards baseline:** RDF 1.1 and SPARQL 1.1 are the stable curriculum baseline. RDF 1.2 and SPARQL 1.2 are clearly marked as emerging material in dedicated callouts.

3. **Dependency strategy:** Core dependencies (rdflib, pyshacl, owlrl, networkx) installed by default. ML dependencies (pykeen, torch) moved to optional `[ml]` group to keep initial setup lightweight.

4. **Experiment architecture:** Pure Python implementations for Chapter 1 to demonstrate concepts from first principles without library dependencies. RDFLib introduced in Chapter 2.

5. **Capstone domain:** Mechanism Knowledge Graph chosen as recurring thread. All examples use Vietnamese geography/domain to maintain consistency and cultural relevance.

6. **Testing approach:** Tests verify both structural correctness AND pedagogical intent (e.g., "symmetric inference present", "transitive inference produces expected triple").

7. **pytest isolation:** System pytest has ROS plugin conflicts. All testing uses `uv run pytest` to ensure isolated venv execution.

---

## Experiments Executed

All 5 Chapter 1 experiments ran successfully with captured output:

| Experiment | Status | Key Output Verified |
|-----------|--------|---------------------|
| 1-1 Plain Graph | ✅ | Same topology, different interpretations demonstrated |
| 1-2 Data Graph vs Taxonomy | ✅ | Transitive subclass queries work; flat graph cannot infer |
| 1-3 Sister City KG | ✅ | 4-stage progressive transformation; symmetric + subclass inference |
| 1-4 Data Graph → KG | ✅ | 8 triples inferred from domain/range/transitivity rules |
| 1-5 Relation Semantics | ✅ | Symmetry, transitivity, inverse properties all demonstrated |

**Test results:** 20/20 passed (`uv run pytest`)  
**Lint results:** All checks passed (`uv run ruff check . && uv run ruff format --check .`)

---

## Evidence of Execution

- All experiment outputs captured in terminal history during this session
- `docs/EXPERIMENT_STATUS.md` contains status markers with execution dates
- Test suite provides automated regression coverage
- Lint/format checks confirm code quality standards met

---

## Limitations

1. **No browser verification:** This is a textbook repository, not a web app. Browser verification N/A.

2. **Diagrams not yet rendered:** Chapter 1 references Mermaid diagrams in markdown but no SVG/PNG exports generated yet. Diagrams render in GitHub/markdown viewers.

3. **Neo4j not tested:** Docker Compose file created but Neo4j experiments deferred to Chapter 2. No container startup verified in Phase 1.

4. **External links validated in Phase 0.5:** Source URLs were HTTP-checked during the Phase 0.5 Semantic & Evidence Audit (2026-08-25). See `docs/source_index.json` for fetch evidence and `docs/PHASE0_5_AUDIT_REPORT.md` for results. The original Phase 1 statement that links were not checked is superseded.

5. **Chapter 1 README files:** Individual experiment READMEs created under `chapter01/exp_1_X/` directories but main `chapter01/README.md` index not yet written.

---

## Unresolved Questions

1. **Mechanism ontology design:** How to formally represent "mechanism" as a reusable cross-domain pattern remains open. Chapter 4 will explore this deeply.

2. **RDF 1.2 triple terms:** Candidate Recommendation as of April 2026. Should Chapter 3 teach RDF 1.1 reification first, then introduce triple terms as emerging alternative? Current plan: yes, but needs validation when RDF 1.2 reaches Recommendation status.

3. **PyKEEN maintenance cadence:** Last release April 2025. Acceptable for Chapter 8 but may need replacement evaluation before writing that chapter.

4. **Bilingual glossary scaling:** Current glossary covers Chapter 1 terms. Need consistent process for adding terms in subsequent chapters without duplication or inconsistency.

---

## Recommended Chapter 2 Plan

Chapter 2 ("Data Models and Query Languages") should:

1. Introduce RDFLib as the primary RDF library (already installed, verified active)
2. Cover Turtle serialization with hands-on parsing/serialization exercises
3. Teach SPARQL basic graph patterns using RDFLib's built-in SPARQL engine
4. Introduce Neo4j via Docker Compose (verify container startup first)
5. Teach Cypher traversal fundamentals
6. **Mandatory comparison experiment (2-6):** Represent identical knowledge in RDF and Property Graph, document trade-offs in query expressiveness, schema flexibility, and tooling maturity
7. Update GLOSSARY.md with Chapter 2 terms
8. Write tests before marking experiments complete

**Key risk:** Neo4j Docker image download size (~500MB). Verify disk space and network before starting Chapter 2 work.

**Estimated effort:** Similar to Phase 1 (~4-6 hours of focused work).

---

## Quality Gate Verification

- [x] All Chapter 1 experiments actually run
- [x] Setup instructions work from clean environment (`uv sync` succeeds)
- [x] Every important external claim has a source (see SOURCE_MATRIX.md)
- [x] No major claim depends solely on SEO/blog source
- [x] No copied textbook prose (all content original)
- [x] Formal notation internally consistent (set theory, triple notation)
- [x] Diagrams use Mermaid syntax (render in markdown viewers)
- [x] Code passes tests (20/20) and lint (clean)
- [x] Glossary contains all Chapter 1 terms
- [x] Chapter 1 closes with unanswered questions motivating Chapter 2

**Phase 1 is COMPLETE.** Ready to proceed to Chapter 2 upon user approval.

