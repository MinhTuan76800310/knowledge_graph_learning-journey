"""Experiment 1-1: Plain Graph Without Semantics.

Demonstrates that a directed labeled graph stores topology and labels
but cannot enforce meaning, constraints, or inference without external semantics.
"""

from __future__ import annotations


class PlainGraph:
    """Minimal directed labeled graph with no schema or semantics."""

    def __init__(self) -> None:
        self.nodes: set[str] = set()
        self.edges: list[tuple[str, str, str]] = []  # (source, label, target)

    def add_node(self, node: str) -> None:
        self.nodes.add(node)

    def add_edge(self, source: str, label: str, target: str) -> None:
        self.nodes.add(source)
        self.nodes.add(target)
        self.edges.append((source, label, target))

    def neighbors(self, node: str) -> list[tuple[str, str]]:
        """Return outgoing (label, target) pairs for a node."""
        return [(label, target) for src, label, target in self.edges if src == node]

    def find_path_bfs(self, start: str, end: str) -> list[str] | None:
        """BFS shortest path ignoring edge labels."""
        from collections import deque

        if start not in self.nodes or end not in self.nodes:
            return None
        visited: set[str] = {start}
        queue: deque[tuple[str, list[str]]] = deque([(start, [start])])
        while queue:
            current, path = queue.popleft()
            if current == end:
                return path
            for _, neighbor in self.neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None

    def summary(self) -> str:
        lines = [f"Nodes ({len(self.nodes)}): {sorted(self.nodes)}"]
        lines.append(f"Edges ({len(self.edges)}):")
        for src, label, tgt in self.edges:
            lines.append(f"  {src} --[{label}]--> {tgt}")
        return "\n".join(lines)


def build_city_graph() -> PlainGraph:
    """Interpretation A: cities connected by roads."""
    g = PlainGraph()
    for city in ["Hanoi", "HaiPhong", "DaNang", "HCMC", "CanTho"]:
        g.add_node(city)
    g.add_edge("Hanoi", "road", "HaiPhong")
    g.add_edge("Hanoi", "road", "DaNang")
    g.add_edge("DaNang", "road", "HCMC")
    g.add_edge("HCMC", "road", "CanTho")
    g.add_edge("HaiPhong", "road", "DaNang")
    return g


def build_social_graph() -> PlainGraph:
    """Interpretation B: people connected by friendships — same topology."""
    g = PlainGraph()
    mapping = {
        "Hanoi": "Alice",
        "HaiPhong": "Bob",
        "DaNang": "Carol",
        "HCMC": "Dave",
        "CanTho": "Eve",
    }
    for person in mapping.values():
        g.add_node(person)
    for src, label, tgt in build_city_graph().edges:
        g.add_edge(mapping[src], "friend", mapping[tgt])
    return g


def main() -> None:
    print("=" * 60)
    print("EXPERIMENT 1-1: Plain Graph Without Semantics")
    print("=" * 60)

    print("\n--- Interpretation A: Cities & Roads ---")
    city = build_city_graph()
    print(city.summary())
    print(f"\nNeighbors of Hanoi: {city.neighbors('Hanoi')}")
    path = city.find_path_bfs("Hanoi", "CanTho")
    print(f"Path Hanoi -> CanTho: {path}")

    print("\n--- Interpretation B: People & Friendships (same topology) ---")
    social = build_social_graph()
    print(social.summary())
    print(f"\nNeighbors of Alice: {social.neighbors('Alice')}")
    path2 = social.find_path_bfs("Alice", "Eve")
    print(f"Path Alice -> Eve: {path2}")

    print("\n--- Key Observation ---")
    print("Both graphs have identical topology (5 nodes, 5 edges, same shape).")
    print("The graph engine treats 'road' and 'friend' as opaque strings.")
    print("No constraint prevents adding ('CanTho', 'flyTo', 42) — no type checking.")
    print("Meaning exists ONLY in the human reader's mind, not in the data structure.")


if __name__ == "__main__":
    main()
