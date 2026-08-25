# Chapter 2 RDF Checkpoint Report

**Date:** 2026-08-25
**Scope:** RDF/SPARQL half of Chapter 2 (Experiments 2-1, 2-2, 2-3)
**Status:** Checkpoint passed — ready for Property Graph side

## Sources Fetched

| ID | Title | Status | Used In |
|----|-------|--------|---------|
| R11-01 | RDF 1.1 Primer | FETCHED_AND_VERIFIED | Ch2 contracts, book draft |
| R11-02 | RDF 1.1 Concepts and Abstract Syntax | FETCHED_AND_VERIFIED | Ch2 contracts, book draft |
| R11-05 | RDF 1.1 Turtle | FETCHED_AND_VERIFIED | Exp 2-2, contracts |
| SP11-01 | SPARQL 1.1 Overview | FETCHED_AND_VERIFIED | Exp 2-3, contracts |
| SP11-02 | SPARQL 1.1 Query Language | FETCHED_AND_VERIFIED | Exp 2-3, contracts |
| TOOL-01 | RDFLib documentation | FETCHED_AND_VERIFIED | All RDF experiments |
| R12-01 | RDF 1.2 Concepts | FETCHED_AND_VERIFIED | Current Developments callout |
| SP12-01 | SPARQL 1.2 Query | FETCHED_AND_VERIFIED | Current Developments callout |
| N4J-05 | Neo4j Data Modeling | FETCHED_AND_VERIFIED | Designed for 2-4/2-5/2-6 |
| N4J-06 | Neo4j Cypher Manual | FETCHED_AND_VERIFIED | Designed for 2-4/2-5/2-6 |
| N4J-07 | Neo4j Python Driver Manual | FETCHED_AND_VERIFIED | Designed for 2-4/2-5 |
| N4J-08 | Neo4j Docker documentation | FETCHED_AND_VERIFIED | ADR-002 |
| GQL-01 | ISO/IEC 39075:2024 GQL | FETCHED_METADATA_ONLY (403) | Contracts GQL callout |
| GQL-02 | Neo4j Cypher GQL conformance | FETCHED_AND_VERIFIED | Contracts GQL callout |
| GQL-03 | GQL Standards | FETCHED_AND_VERIFIED | Contracts GQL callout |
| S04 | What Are Graph Data Models? | FETCHED_AND_VERIFIED | Background research |

All sources recorded in `docs/source_index.json`. Research notes exist at documented paths.

## Semantic Contracts Established

`docs/CHAPTER02_SEMANTIC_CONTRACTS.md` defines contracts for:

1. **RDF abstract data model** — triples, IRIs, literals, blank nodes, graph-as-set
2. **Turtle** — concrete syntax, not the data model; prefix abbreviation
3. **SPARQL** — graph patterns, BGP, variables, solution mappings
4. **Labeled Property Graph** — node, relationship, label, property, identity (for future implementation)
5. **Cypher** — MATCH, variables, relationship patterns, RETURN (for future implementation)
6. **GQL callout** — ISO standard vs Cypher conformance distinction
7. **Representation boundary** — same knowledge does not imply same graph structure

## Experiments Implemented

| ID | Title | File | Tests | Status |
|----|-------|------|-------|--------|
| 2-1 | RDF from first principles / RDFLib | `chapter02/exp_2_1_rdf_first_principles.py` | 11 | Pass |
| 2-2 | Turtle serialization round-trip | `chapter02/exp_2_2_turtle_serialization.py` | 6 | Pass |
| 2-3 | SPARQL Basic Graph Patterns | `chapter02/exp_2_3_sparql_basic_patterns.py` | 7 | Pass |

**Total Chapter 2 tests: 24** — all passing.

Tests assert exact graph content, round-trip equivalence, and exact SPARQL query result bindings. No stdout substring matching.

## Decisions Made

| Decision | Record | Summary |
|----------|--------|---------|
| Neo4j version pinning | `docs/decisions/ADR-002-neo4j-version.md` | Pinned to neo4j:5.26.0-community; no APOC required for basic experiments |
| RDFLib namespace convention | `pyproject.toml` | Added N806 to ruff ignore list; uppercase EX is standard RDFLib convention |
| Stable baseline | Semantic contracts | RDF 1.1 / SPARQL 1.1 are teaching baseline; RDF 1.2 / SPARQL 1.2 marked as emerging |
| Domain continuity | Experiment plan | Same Hanoi/Vietnam/Paris/France domain flows through all experiments |

## Quality Gate Results

| Check | Result |
|-------|--------|
| Chapter 1 tests (25) | All pass |
| Repository integrity tests (7) | All pass |
| Chapter 2 RDF tests (24) | All pass |
| Total test count | **56 passed** |
| ruff check | Clean |
| ruff format --check | Clean |
| source_index.json paths | All research note paths exist |
| Wrapper artifacts scan | None found |
| Stable/draft standards conflation | RDF 1.2/SPARQL 1.2 clearly marked as emerging |

## Documentation Created/Updated

- `book/chapter02.md` — RDF/SPARQL half draft (Vietnamese prose with English technical terms)
- `chapter02/README.md` — Chapter overview, experiment index, run instructions
- `docs/CHAPTER02_SEMANTIC_CONTRACTS.md` — Formal semantic contracts
- `docs/CHAPTER02_EXPERIMENT_PLAN.md` — Full design for all 6 experiments
- `docs/decisions/ADR-002-neo4j-version.md` — Neo4j version decision record
- `docs/EXPERIMENT_STATUS.md` — Updated with Chapter 2 entries and new total (56 tests)
- `docs/SOURCE_MATRIX.md` — Fixed RDF 1.2 reification wording
- `docs/source_index.json` — Already contained all Chapter 2 sources from prior session

## Unresolved Questions for Property Graph Side

These must be addressed when implementing Experiments 2-4, 2-5, 2-6:

1. **Neo4j instance management:** How will experiments start/stop Neo4j? Docker Compose with pinned image (ADR-002) is planned but not yet wired into experiment scripts.
2. **Test isolation:** Property graph tests need a running Neo4j instance. Should tests skip gracefully when Neo4j is unavailable, or require it?
3. **Domain mapping:** The RDF domain uses IRIs (http://example.org/Hanoi). Property graph equivalent needs node labels and properties. Exact mapping must preserve comparability for Experiment 2-6.
4. **Relationship metadata:** RDF requires reification for n-ary relationships. Property graphs support properties on relationships natively. Experiment 2-6 must demonstrate this asymmetry concretely.
5. **Cypher vs GQL terminology:** Experiments should use Cypher syntax but note GQL alignment where relevant per contracts.

## Readiness Assessment for Experiments 2-4, 2-5, 2-6

| Experiment | Design Complete | Implementation Ready | Blockers |
|-----------|----------------|---------------------|----------|
| 2-4 Labeled Property Graph | Yes | Yes | Neo4j Docker setup needed |
| 2-5 Cypher traversal | Yes | Yes | Depends on 2-4 infrastructure |
| 2-6 Same knowledge comparison | Yes | Partially | Depends on 2-4 + 2-5 completion |

All three experiments have complete designs in `docs/CHAPTER02_EXPERIMENT_PLAN.md`. Implementation can proceed once Neo4j infrastructure is set up.

## What This Checkpoint Does NOT Claim

- Chapter 2 is **not** complete. Only the RDF/SPARQL half is implemented.
- Property Graph experiments are designed but not implemented.
- The cross-representation comparison (2-6) cannot be executed until both sides exist.
- No browser verification was performed (this chapter has no web UI).
