# Chapter 2: Data Models and Query Languages

## Core Question

How does the choice of graph representation change what we can express, query, infer, exchange, and maintain?

## Learning Objectives

- Understand the RDF abstract data model (triples, IRIs, literals, blank nodes)
- Distinguish RDF model from Turtle serialization
- Understand SPARQL graph pattern matching and solution mappings
- Understand Labeled Property Graph model (deferred to next slice)
- Compare same domain knowledge across representations (deferred to next slice)

## Experiments

| ID | Title | Difficulty | Status | File |
|----|-------|-----------|--------|------|
| 2-1 | RDF from first principles / RDFLib | ★★ | ✅ | `exp_2_1_rdf_first_principles.py` |
| 2-2 | Turtle serialization round-trip | ★★ | ✅ | `exp_2_2_turtle_serialization.py` |
| 2-3 | SPARQL Basic Graph Patterns | ★★ | ✅ | `exp_2_3_sparql_basic_patterns.py` |
| 2-4 | Mechanism RATE_OF_CHANGE via RDF + SPARQL (capstone thread) | ★★ | ✅ | `exp_2_4_mechanism_turtle_sparql.py` |
| 2-5 | Labeled Property Graph / Neo4j | ★★ | 🔲 Deferred | taught conceptually in chapter text |
| 2-6 | Cypher traversal | ★★ | 🔲 Deferred | taught conceptually in chapter text |
| 2-7 | Same knowledge — RDF vs Property Graph | ★★★ | 🔲 Deferred | taught conceptually in chapter text |

## Domain

Two domains, intentionally:

- The city domain for continuity (same as Chapter 1): Hanoi → capitalOf → Vietnam,
  Paris → capitalOf → France, Hanoi → sisterCity → Paris.
- The **mechanism domain** (capstone thread, `exp_2_4`): the running dataset at
  `datasets/mechanism_kg/rate_of_change.ttl` — `RATE_OF_CHANGE` and friends.

## Running Experiments

```bash
uv run python chapter02/exp_2_1_rdf_first_principles.py
uv run python chapter02/exp_2_2_turtle_serialization.py
uv run python chapter02/exp_2_3_sparql_basic_patterns.py
uv run python chapter02/exp_2_4_mechanism_turtle_sparql.py
```

## Running Tests

```bash
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 uv run pytest chapter02/test_ch2_experiments.py -v
```

Note: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` is required due to ROS jazzy launch_testing plugin conflict with pytest 9.x.

## Semantic Contracts

See `docs/CHAPTER02_SEMANTIC_CONTRACTS.md` for formal definitions of what each experiment teaches.

## Key Distinctions

- **RDF model ≠ Turtle syntax.** Turtle is one concrete syntax for serializing RDF graphs.
- **SPARQL ≠ SQL for graphs.** SPARQL matches graph patterns; SQL queries relational tables.
- **Same knowledge ≠ same graph structure.** Representation choice alters identity, metadata, relationships, interoperability, and query ergonomics.
