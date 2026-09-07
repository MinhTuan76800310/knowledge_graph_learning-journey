"""Experiment 2-6: Cypher Pattern Matching and Graph Traversal.

Question: "How does declarative Cypher graph pattern matching traverse paths
and query property graphs compared to SPARQL BGPs?"

Demonstrates:
  1. Directed relationship matching: (c:City)-[:CAPITAL_OF]->(cntry:Country)
  2. Property filtering (WHERE clause): c.population > 8000000
  3. Undirected relationship matching: (c1:City)-[:SISTER_CITY]-(c2:City)
     where symmetry allows matching in both directions regardless of storage arrow
  4. Variable-length path traversal: (m:Mechanism)-[:REQUIRES*1..3]->(dep)
     tracing transitive dependency chains

Semantic contracts: N4J-06 (Cypher Manual), GQL-02 (Cypher/GQL alignment),
docs/CHAPTER02_SEMANTIC_CONTRACTS.md §5.
Difficulty: ★★
Status: ✅ Independently runnable
"""

from __future__ import annotations

import sys
from collections.abc import Callable
from typing import Any

try:
    from exp_2_5_labeled_property_graph import (
        Edge,
        Node,
        SimplePropertyGraph,
        build_city_graph,
        build_mechanism_graph,
    )
except ImportError:
    from chapter02.exp_2_5_labeled_property_graph import (
        Edge,
        Node,
        SimplePropertyGraph,
        build_city_graph,
        build_mechanism_graph,
    )

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class CypherPatternEngine:
    """In-memory declarative pattern matching engine executing Cypher-equivalent semantics."""

    def __init__(self, graph: SimplePropertyGraph) -> None:
        self.graph = graph

    def match_hop(
        self,
        source_label: str | None = None,
        rel_type: str | None = None,
        target_label: str | None = None,
        direction: str = "OUT",  # 'OUT' (->), 'IN' (<-), or 'BOTH' (-)
        where: Callable[[Node, Edge, Node], bool] | None = None,
    ) -> list[dict[str, Any]]:
        """Match a single-hop pattern (s)-[r]->(t), (s)<-[r]-(t), or (s)-[r]-(t)."""
        results: list[dict[str, Any]] = []

        # Find candidate source nodes
        candidate_sources = (
            self.graph.nodes_with_label(source_label)
            if source_label
            else list(self.graph.nodes.values())
        )

        for src in candidate_sources:
            # Collect candidate edges based on direction
            candidate_edges: list[tuple[Edge, Node]] = []

            if direction in ("OUT", "BOTH"):
                for edge in self.graph.outgoing_edges(src.id, rel_type):
                    tgt = self.graph.get_node(edge.target)
                    if tgt and (target_label is None or tgt.has_label(target_label)):
                        candidate_edges.append((edge, tgt))

            if direction in ("IN", "BOTH"):
                for edge in self.graph.incoming_edges(src.id, rel_type):
                    tgt = self.graph.get_node(edge.source)
                    if tgt and (target_label is None or tgt.has_label(target_label)):
                        candidate_edges.append((edge, tgt))

            for edge, tgt in candidate_edges:
                if where is None or where(src, edge, tgt):
                    results.append(
                        {
                            "source": src,
                            "relationship": edge,
                            "target": tgt,
                        }
                    )
        return results

    def find_paths(
        self,
        start_node_id: str,
        rel_type: str,
        min_hops: int = 1,
        max_hops: int = 3,
    ) -> list[list[str]]:
        """Find all variable-length paths from start_node: (s)-[:rel_type*min..max]->(t)."""
        paths: list[list[str]] = []

        def dfs(current_id: str, current_path: list[str]) -> None:
            depth = len(current_path) - 1
            if min_hops <= depth <= max_hops:
                paths.append(list(current_path))
            if depth >= max_hops:
                return

            for edge in self.graph.outgoing_edges(current_id, rel_type):
                nxt = edge.target
                if nxt not in current_path:  # avoid cycles in simple paths
                    dfs(nxt, current_path + [nxt])

        dfs(start_node_id, [start_node_id])
        return paths


def main() -> None:
    print("=" * 60)
    print("EXPERIMENT 2-6: CYPHER PATTERN MATCHING & TRAVERSAL")
    print("=" * 60)

    g_city = build_city_graph()
    engine_city = CypherPatternEngine(g_city)

    # --- Query 1: Directed Pattern Match ---
    print("\n--- Query 1: MATCH (c:City)-[:CAPITAL_OF]->(cntry:Country) ---")
    print("Cypher query:")
    print("  MATCH (c:City)-[:CAPITAL_OF]->(cntry:Country)")
    print("  RETURN c.name AS city, cntry.name AS country\n")

    res1 = engine_city.match_hop("City", "CAPITAL_OF", "Country", direction="OUT")
    for r in res1:
        c = r["source"]
        cntry = r["target"]
        edge = r["relationship"]
        print(f"  Matched: {c.get('name')} -> {cntry.get('name')} (since: {edge.get('since')})")

    # --- Query 2: Filtering (WHERE clause) ---
    print("\n--- Query 2: MATCH (c:City) WHERE c.population > 8000000 ---")
    print("Cypher query:")
    print("  MATCH (c:City)")
    print("  WHERE c.population > 8000000")
    print("  RETURN c.name, c.population\n")

    res2 = [n for n in g_city.nodes_with_label("City") if n.get("population", 0) > 8000000]
    for n in res2:
        print(f"  Matched: {n.get('name')} (population: {n.get('population')})")

    # --- Query 3: Undirected Pattern Match ---
    print("\n--- Query 3: MATCH (c1:City)-[:SISTER_CITY]-(c2:City) ---")
    print("Cypher query:")
    print("  MATCH (c1:City)-[:SISTER_CITY]-(c2:City)")
    print("  RETURN c1.name, c2.name\n")

    res3 = engine_city.match_hop("City", "SISTER_CITY", "City", direction="BOTH")
    for r in res3:
        print(f"  Symmetric pair: {r['source'].get('name')} <-> {r['target'].get('name')}")

    # --- Query 4: Variable-length path on Mechanism KG ---
    g_mech = build_mechanism_graph()
    engine_mech = CypherPatternEngine(g_mech)

    print("\n--- Query 4: MATCH p = (m:Mechanism)-[:REQUIRES*1..2]->(dep) ---")
    print("Cypher query:")
    print("  MATCH p = (m:Mechanism {name: 'NewtonCooling'})-[:REQUIRES*1..2]->(dep)")
    print("  RETURN nodes(p), length(p)\n")

    paths = engine_mech.find_paths("newtonCooling_1", "REQUIRES", min_hops=1, max_hops=2)
    for p in paths:
        path_names = [g_mech.get_node(nid).get("name") for nid in p]  # type: ignore[union-attr]
        print(f"  Path length {len(p) - 1}: {' -> '.join(path_names)}")


if __name__ == "__main__":
    main()
