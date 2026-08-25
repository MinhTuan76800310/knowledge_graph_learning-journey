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
| 2-4 | Labeled Property Graph / Neo4j | ★★ | 🔲 Designed | *(next slice)* |
| 2-5 | Cypher traversal | ★★ | 🔲 Designed | *(next slice)* |
| 2-6 | Same knowledge — RDF vs Property Graph | ★★★ | 🔲 Designed | *(next slice)* |

## Domain

All experiments use the same domain for continuity:

- Hanoi → capitalOf → Vietnam
- Paris → capitalOf → France
- Hanoi → sisterCity → Paris

This is the same domain introduced in Chapter 1.

## Running Experiments

```bash
uv run python chapter02/exp_2_1_rdf_first_principles.py
uv run python chapter02/exp_2_2_turtle_serialization.py
uv run python chapter02/exp_2_3_sparql_basic_patterns.py
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
