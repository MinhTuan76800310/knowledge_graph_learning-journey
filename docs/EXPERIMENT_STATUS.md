# Experiment Status — Knowledge Graph Book

Tracks the execution status of all experiments. An experiment is only marked ✅ after it has been run and output verified.

Last updated: 2026-08-25

## Chapter 1: From Graph to Knowledge

| ID | Title | Difficulty | Status | Last Run | Evidence Summary |
|----|-------|-----------|--------|----------|------------------|
| 1-1 | Plain graph without semantics | ★ | ✅ | 2026-08-25 | Ran successfully. Output shows identical topology for city/social graphs, confirming semantics-free nature. |
| 1-2 | Data graph vs taxonomy | ★ | ✅ | 2026-08-25 | Ran successfully. Taxonomy correctly returns transitive instances (CapitalCity ⊑ City). Data graph query returns only direct matches. |
| 1-3 | Progressive transformation to KG | ★★ | ✅ | 2026-08-25 | Ran successfully. All 5 stages execute. Inference produces symmetric, subclass, and domain/range triples as expected. |
| 1-4 | Data graph → simple KG | ★★ | ✅ | 2026-08-25 | Ran successfully. Forward-chaining infers 8 new triples. Region/City queries work only after semantics added. |
| 1-5 | Define semantics of a relation | ★★★ | ✅ | 2026-08-25 | Ran successfully. Symmetry, transitivity, and inverse inference all produce correct triples. 3 inferred triples total. |

## Test Results

**Current canonical count: 56 tests** (as of Chapter 2 RDF checkpoint, 2026-08-25):
- Chapter 1 experiment tests: 25 (TestExp11: 6, TestExp12: 5, TestExp13: 3, TestExp14: 3, TestExp15: 8)
- Chapter 2 RDF/SPARQL tests: 24 (TestExp21: 11, TestExp22: 6, TestExp23: 7)
- Repository integrity tests: 7 (`tests/test_repo_integrity.py`)

Historical note: Earlier phase reports referenced 20 tests (Phase 0.5), then 25 (Phase 0.6), then 32 (Phase 0.7). Current count is 56 after adding Chapter 2 semantic tests.

Note: Tests require `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` due to ROS jazzy launch_testing plugin conflict with pytest 9.x on this system.

## Chapter 2: Data Models and Query Languages (RDF/SPARQL checkpoint)

| ID | Title | Difficulty | Status | Last Run | Evidence Summary |
|----|-------|-----------|--------|----------|------------------|
| 2-1 | RDF from first principles / RDFLib | ★★ | ✅ | 2026-08-25 | Ran successfully. Pure-Python triple store and RDFLib both produce correct triples, subjects, predicates. SPARQL query returns 2 cities. |
| 2-2 | Turtle serialization round-trip | ★★ | ✅ | 2026-08-25 | Ran successfully. Graph → Turtle → parse back yields identical triple set. N-Triples and RDF/XML round-trips also verified. |
| 2-3 | SPARQL Basic Graph Patterns | ★★ | ✅ | 2026-08-25 | Ran successfully. Five queries (BGP, shared vars, FILTER, OPTIONAL) return correct solution mappings. |
| 2-4 | Labeled Property Graph / Neo4j | ★★ | 🔲 | — | Designed; not yet implemented. |
| 2-5 | Cypher traversal | ★★ | 🔲 | — | Designed; not yet implemented. |
| 2-6 | Same knowledge — RDF vs Property Graph | ★★★ | 🔲 | — | Designed; not yet implemented. |

### Chapter 2 Test Results

**Chapter 2 semantic tests: 24 tests** (`chapter02/test_ch2_experiments.py`):
- TestExp21RdfFirstPrinciples: 11 tests
- TestExp22TurtleSerialization: 6 tests
- TestExp23SparqlBasicPatterns: 7 tests

All 24 pass as of 2026-08-25.

## Chapters 3–10

Not yet implemented. Experiments will be added as each chapter is drafted.

