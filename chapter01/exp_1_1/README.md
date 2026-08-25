# Experiment 1-1: Plain Graph Without Semantics

**Difficulty:** ★ Beginner  
**Status:** ✅ Independently runnable

## Question

What is the minimal structure of a graph, and what information is missing when a graph has no semantics?

## Why This Experiment Exists

Before understanding Knowledge Graphs, we must understand what a plain graph *cannot* express. This experiment establishes the baseline: a graph as pure topology with no meaning attached to nodes or edges.

## Hypothesis

A plain directed labeled graph can represent connectivity but cannot distinguish between different *types* of relationships or entities without external interpretation. Two structurally identical graphs may represent completely different domains.

## Concepts Demonstrated

- Directed graph
- Labeled graph
- Node (vertex)
- Edge (arc)
- Path
- Topology vs semantics gap

## Architecture

Pure Python implementation using only built-in data structures. No external libraries required for this experiment.

```
nodes: set of strings
edges: list of (source, label, target) tuples
operations: find_neighbors, find_path, print_graph
```

## Setup

No dependencies beyond Python 3.12+.

## Run

```bash
cd chapter01
uv run python exp_1_1_plain_graph.py
```

## Expected Result

The script prints:
1. A graph with 5 nodes and 6 edges
2. Neighbors of a specified node
3. A path between two nodes (if one exists)
4. A demonstration that the same structure could represent cities+roads OR people+friendships

## What to Observe

- The graph stores *labels* on edges but does not define what those labels *mean*.
- There is no schema: nothing prevents adding an edge with any label between any nodes.
- The same topological structure is reusable across domains — which is both its strength and its limitation.

## Why the Result Happens

A plain graph is a mathematical structure `(V, E)` where `E ⊆ V × L × V`. The label set `L` is uninterpreted: the graph engine treats `"road"` and `"friend"` identically as opaque strings. Meaning exists only in the mind of the human reading the output.

## Failure Cases

- If you expected the graph to enforce that `"road"` only connects `"City"` nodes, it won't. There are no constraints.
- If you expected transitive inference (e.g., if A→B and B→C then A→C), the plain graph does not provide it automatically.

## Further Questions

1. What additional structure would be needed to distinguish entity types?
2. How would you encode "this edge means inheritance" vs "this edge means geographic adjacency"?
3. Can two graphs with identical topology but different label interpretations coexist in the same system?

## Sources

- Stanford CS520 Lecture 1: What is a Knowledge Graph? — https://web.stanford.edu/class/cs520/
- Hogan et al., *Knowledge Graphs*, Chapter 2: Data Graphs — https://kgbook.org/

