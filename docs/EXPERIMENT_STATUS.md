# Experiment Status — Knowledge Graph Book

Tracks the execution status of all experiments. An experiment is only marked ✅ after it has been run and output verified.

Last updated: 2026-09-07 (v0.3.0 Release Milestone)

## Overview & Integrity Architecture

The repository maintains an automated verification suite combining runnable empirical labs, semantic contract verification, and structural manuscript integrity checks:

- **Total Automated Tests:** **106 passed** (`python -m pytest` / `uv run pytest`)
- **Lint & Code Format:** Clean (`ruff check .`, `ruff format --check .`)
- **Publication PDF Gates:**
  - Vietnamese edition: 434 print pages (passed `scripts/verify_book_pdf.sh`)
  - English edition: 412 print pages (passed `LANG=en scripts/verify_book_pdf.sh`)

## Test Suite Breakdown (106 tests)

| Test Module | Test Focus | Count | Status |
|---|---|:---:|:---:|
| `chapter01/test_experiments.py` | Topology, taxonomy, relation semantics, RDFS domain/range | 25 | ✅ PASS |
| `chapter02/test_ch2_experiments.py` | RDF first principles, Turtle round-trip, SPARQL BGPs, Mechanism dataset | 30 | ✅ PASS |
| `tests/test_chapter08_integrity.py` | Ch8 structure, 1-WL expressiveness, RotatE, citations, glossary | 4 | ✅ PASS |
| `tests/test_chapter09_integrity.py` | Ch9 structure, GraphRAG retrieval bounds, PPR, citations, glossary | 13 | ✅ PASS |
| `tests/test_chapter10_integrity.py` | Ch10 structure, closed-loop cybernetics, model collapse, citations | 11 | ✅ PASS |
| `tests/test_book_integrity.py` | Cross-chapter structure, manuscript completeness, LaTeX fences | 8 | ✅ PASS |
| `tests/test_book_concept_dependencies.py` | Concept ordering graph, forward-reference prevention | 8 | ✅ PASS |
| `tests/test_repo_integrity.py` | Source index consistency, research notes, no leaked markers | 7 | ✅ PASS |
| **Total** | | **106** | **✅ 100% PASS** |

## Chapter 1: From Graph to Knowledge

| ID | Title | Difficulty | Status | Last Run | Evidence Summary |
|----|-------|-----------|--------|----------|------------------|
| 1-1 | Plain graph without semantics | ★ | ✅ | 2026-09-07 | Ran successfully. Demonstrates identical topology for city/social graphs, confirming semantics-free nature. |
| 1-2 | Data graph vs taxonomy | ★ | ✅ | 2026-09-07 | Ran successfully. Taxonomy correctly returns transitive instances (CapitalCity ⊑ City). Data graph query returns only direct matches. |
| 1-3 | Progressive transformation to KG | ★★ | ✅ | 2026-09-07 | Ran successfully. All 5 stages execute. Inference produces symmetric, subclass, and domain/range triples as expected. |
| 1-4 | Data graph → simple KG | ★★ | ✅ | 2026-09-07 | Ran successfully. Forward-chaining infers 8 new triples. Region/City queries work only after semantics added. |
| 1-5 | Define semantics of a relation | ★★★ | ✅ | 2026-09-07 | Ran successfully. Symmetry, transitivity, and inverse inference all produce correct triples. 3 inferred triples total. |

## Chapter 2: Data Models and Query Languages

| ID | Title | Difficulty | Status | Last Run | Evidence Summary |
|----|-------|-----------|--------|----------|------------------|
| 2-1 | RDF from first principles / RDFLib | ★★ | ✅ | 2026-09-07 | Pure-Python triple store and RDFLib both produce correct triples, subjects, predicates. SPARQL query returns 2 cities. |
| 2-2 | Turtle serialization round-trip | ★★ | ✅ | 2026-09-07 | Graph → Turtle → parse back yields identical triple set. N-Triples and RDF/XML round-trips also verified. |
| 2-3 | SPARQL Basic Graph Patterns | ★★ | ✅ | 2026-09-07 | Five queries (BGP, shared vars, FILTER, OPTIONAL) return correct solution mappings. |
| 2-4 | Mechanism KG SPARQL queries | ★★ | ✅ | 2026-09-07 | Executed against `datasets/mechanism_kg/rate_of_change.ttl`. BGP, filter thresholds, and optional clauses verified. |
| 2-5 | Labeled Property Graph / Neo4j | ★★ | 📖 | — | Static Cypher code verified; live database execution documented in `docs/LAB_BACKLOG.md`. |
| 2-6 | Same knowledge — RDF vs Property Graph | ★★★ | 📖 | — | Dual representation analyzed; runnable comparison documented in `docs/LAB_BACKLOG.md`. |

## Chapters 3–10: Semantic Integrity & Runnable Backlog

Chapters 3 through 10 have completed full semantic acceptance audits, depth reviews, and automated integrity test suites (including concept dependencies, citation checks against `docs/source_index.json`, and TikZ vector figure rendering).

Standalone interactive Docker-based experiments for Chapters 3–10 are tracked in [`docs/LAB_BACKLOG.md`](LAB_BACKLOG.md). Manuscript chapters are completely self-contained and verifiable without external services.

