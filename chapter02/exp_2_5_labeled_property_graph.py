"""Experiment 2-5: Labeled Property Graph (LPG) Modeling and Ingestion.

Question: "How does the Labeled Property Graph (LPG) model represent entities,
labels, properties, and directed relationships?"

Demonstrates the formal 7-tuple LPG model:
    G = (V, E, L_V, L_E, rho, K, nu)
from first principles using a standalone pure-Python engine (SimplePropertyGraph).
Shows direct property attachment on both nodes and edges without intermediate
reification triples.

Domains covered:
  1. City domain: Hanoi, Vietnam, Paris, France with node labels, properties,
     and CAPITAL_OF / SISTER_CITY edges carrying relationship metadata.
  2. Mechanism domain: RateOfChange and physical quantities modeled as nodes
     connected by typed operations and dependency edges.

Semantic contracts: N4J-03 (Graph Data Modeling), N4J-05 (Neo4j Modeling),
docs/CHAPTER02_SEMANTIC_CONTRACTS.md §4.
Difficulty: ★★
Status: ✅ Independently runnable
"""

from __future__ import annotations

import sys
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


@dataclass
class Node:
    """A node in a Labeled Property Graph.

    Corresponds to an entity with:
      - A unique identifier in V
      - A set of labels from Sigma_V (node classifications)
      - A dictionary of properties (attribute-value pairs)
    """

    id: str
    labels: set[str] = field(default_factory=set)
    properties: dict[str, Any] = field(default_factory=dict)

    def has_label(self, label: str) -> bool:
        return label in self.labels

    def get(self, key: str, default: Any = None) -> Any:
        return self.properties.get(key, default)


@dataclass
class Edge:
    """A directed relationship in a Labeled Property Graph.

    Corresponds to a typed, directed connection with:
      - A unique identifier in E
      - A source node id and target node id: rho(e) = (source, target)
      - Exactly one relationship type from Sigma_E
      - A dictionary of properties directly attached to the edge
    """

    id: str
    source: str
    target: str
    type: str
    properties: dict[str, Any] = field(default_factory=dict)

    def get(self, key: str, default: Any = None) -> Any:
        return self.properties.get(key, default)


class SimplePropertyGraph:
    """An in-memory Labeled Property Graph implementation from first principles.

    Implements the formal 7-tuple LPG definition:
      V: set of node IDs
      E: set of edge IDs
      L_V: V -> 2^{Sigma_V} (node labels)
      L_E: E -> Sigma_E (edge type)
      rho: E -> V x V (incident endpoints)
      K: property keys
      nu: (V union E) x K -> Values (property mapping)
    """

    def __init__(self) -> None:
        self.nodes: dict[str, Node] = {}
        self.edges: dict[str, Edge] = {}
        self._out_edges: dict[str, list[str]] = defaultdict(list)
        self._in_edges: dict[str, list[str]] = defaultdict(list)

    def add_node(
        self,
        node_id: str,
        labels: set[str] | list[str] | None = None,
        properties: dict[str, Any] | None = None,
    ) -> Node:
        """Add or update a node in the graph."""
        lbl_set = set(labels) if labels else set()
        props = dict(properties) if properties else {}
        if node_id in self.nodes:
            node = self.nodes[node_id]
            node.labels.update(lbl_set)
            node.properties.update(props)
            return node
        node = Node(id=node_id, labels=lbl_set, properties=props)
        self.nodes[node_id] = node
        return node

    def add_edge(
        self,
        edge_id: str,
        source: str,
        target: str,
        rel_type: str,
        properties: dict[str, Any] | None = None,
    ) -> Edge:
        """Add a directed typed relationship between two existing nodes."""
        if source not in self.nodes:
            raise ValueError(f"Source node '{source}' does not exist in graph.")
        if target not in self.nodes:
            raise ValueError(f"Target node '{target}' does not exist in graph.")

        props = dict(properties) if properties else {}
        edge = Edge(
            id=edge_id,
            source=source,
            target=target,
            type=rel_type,
            properties=props,
        )
        self.edges[edge_id] = edge
        self._out_edges[source].append(edge_id)
        self._in_edges[target].append(edge_id)
        return edge

    def get_node(self, node_id: str) -> Node | None:
        return self.nodes.get(node_id)

    def get_edge(self, edge_id: str) -> Edge | None:
        return self.edges.get(edge_id)

    def outgoing_edges(self, node_id: str, rel_type: str | None = None) -> list[Edge]:
        """Return all outgoing edges from node_id, optionally filtered by relationship type."""
        edge_ids = self._out_edges.get(node_id, [])
        edges = [self.edges[eid] for eid in edge_ids]
        if rel_type is not None:
            edges = [e for e in edges if e.type == rel_type]
        return edges

    def incoming_edges(self, node_id: str, rel_type: str | None = None) -> list[Edge]:
        """Return all incoming edges to node_id, optionally filtered by relationship type."""
        edge_ids = self._in_edges.get(node_id, [])
        edges = [self.edges[eid] for eid in edge_ids]
        if rel_type is not None:
            edges = [e for e in edges if e.type == rel_type]
        return edges

    def nodes_with_label(self, label: str) -> list[Node]:
        """Find all nodes possessing a specific label."""
        return [n for n in self.nodes.values() if n.has_label(label)]

    def to_cypher_script(self) -> str:
        """Generate equivalent standard openCypher DDL/DML statements."""
        lines = ["// Generated openCypher script for Property Graph", ""]
        for n in self.nodes.values():
            labels_str = "".join(f":{lbl}" for lbl in sorted(n.labels))
            props = [f"{k}: {repr(v)}" for k, v in sorted(n.properties.items())]
            props_str = f" {{{', '.join(props)}}}" if props else ""
            lines.append(f"CREATE (:{n.id}{labels_str}{props_str});")

        for e in self.edges.values():
            props = [f"{k}: {repr(v)}" for k, v in sorted(e.properties.items())]
            props_str = f" {{{', '.join(props)}}}" if props else ""
            lines.append(
                f"MATCH (s {{id: '{e.source}'}}), (t {{id: '{e.target}'}}) "
                f"CREATE (s)-[:{e.type}{props_str}]->(t);"
            )
        return "\n".join(lines)


def build_city_graph() -> SimplePropertyGraph:
    """Build the canonical Chapter 2 City domain as a Property Graph."""
    g = SimplePropertyGraph()

    # Nodes with labels and properties
    g.add_node(
        "Hanoi",
        labels={"City", "Capital"},
        properties={"name": "Hà Nội", "population": 8418883, "country": "Vietnam"},
    )
    g.add_node(
        "Vietnam",
        labels={"Country"},
        properties={"name": "Việt Nam", "iso": "VNM"},
    )
    g.add_node(
        "Paris",
        labels={"City", "Capital"},
        properties={"name": "Paris", "population": 2161000, "country": "France"},
    )
    g.add_node(
        "France",
        labels={"Country"},
        properties={"name": "France", "iso": "FRA"},
    )

    # Directed relationships with properties directly on edges
    g.add_edge(
        "e_hn_vn",
        source="Hanoi",
        target="Vietnam",
        rel_type="CAPITAL_OF",
        properties={"since": 1976, "status": "Official"},
    )
    g.add_edge(
        "e_pa_fr",
        source="Paris",
        target="France",
        rel_type="CAPITAL_OF",
        properties={"since": 1789, "status": "Official"},
    )
    g.add_edge(
        "e_hn_pa",
        source="Hanoi",
        target="Paris",
        rel_type="SISTER_CITY",
        properties={"agreementDate": "1994-05-12", "active": True},
    )

    return g


def build_mechanism_graph() -> SimplePropertyGraph:
    """Build the Mechanism capstone domain as a Property Graph."""
    g = SimplePropertyGraph()

    g.add_node(
        "rateOfChange_1",
        labels={"Mechanism", "RateOfChangeMechanism"},
        properties={"name": "RateOfChange", "formalDefinition": "dx/dt"},
    )
    g.add_node(
        "heatTransferRate_2",
        labels={"Mechanism"},
        properties={"name": "HeatTransferRate", "symbol": "dQ/dt"},
    )
    g.add_node(
        "newtonCooling_1",
        labels={"Mechanism"},
        properties={"name": "NewtonCooling", "condition": "uniformEnv_1"},
    )
    g.add_node(
        "op_derivative_1",
        labels={"Operation"},
        properties={"type": "Derivative", "order": 1},
    )
    g.add_node(
        "position_1",
        labels={"PhysicalQuantity"},
        properties={"symbol": "x", "hasValue": 12.5, "unit": "meter"},
    )
    g.add_node(
        "time_1",
        labels={"PhysicalQuantity"},
        properties={"symbol": "t", "unit": "second"},
    )

    # Relationships
    g.add_edge("m_rel1", "newtonCooling_1", "rateOfChange_1", "REQUIRES")
    g.add_edge("m_rel2", "newtonCooling_1", "heatTransferRate_2", "REQUIRES")
    g.add_edge(
        "m_rel3",
        "rateOfChange_1",
        "op_derivative_1",
        "APPLIES_OPERATION",
        properties={"order": 1},
    )
    g.add_edge("m_rel4", "op_derivative_1", "position_1", "DIFFERENTIAND")
    g.add_edge("m_rel5", "op_derivative_1", "time_1", "WITH_RESPECT_TO")

    return g


def main() -> None:
    print("=" * 60)
    print("EXPERIMENT 2-5: LABELED PROPERTY GRAPH (LPG) MODELING")
    print("=" * 60)

    g_city = build_city_graph()
    print(f"\nCity LPG built: {len(g_city.nodes)} nodes, {len(g_city.edges)} edges.")

    print("\n--- Node Multi-Label Inspection ---")
    for nid, node in g_city.nodes.items():
        print(f"Node '{nid}': labels={sorted(node.labels)}, props={node.properties}")

    print("\n--- Edge Property Inspection (Direct without reification) ---")
    for eid, edge in g_city.edges.items():
        print(f"Edge '{eid}': ({edge.source}) -[:{edge.type} {edge.properties}]-> ({edge.target})")

    g_mech = build_mechanism_graph()
    print(f"\nMechanism LPG built: {len(g_mech.nodes)} nodes, {len(g_mech.edges)} edges.")

    print("\n--- Mechanism Application Chain ---")
    for edge in g_mech.outgoing_edges("rateOfChange_1", "APPLIES_OPERATION"):
        op = g_mech.get_node(edge.target)
        if op:
            diff_edges = g_mech.outgoing_edges(op.id, "DIFFERENTIAND")
            wrt_edges = g_mech.outgoing_edges(op.id, "WITH_RESPECT_TO")
            diff = g_mech.get_node(diff_edges[0].target) if diff_edges else None
            wrt = g_mech.get_node(wrt_edges[0].target) if wrt_edges else None
            print(
                f"Mechanism rateOfChange_1 applies {op.properties.get('type')} "
                f"of {diff.properties.get('symbol') if diff else '?'} "
                f"w.r.t {wrt.properties.get('symbol') if wrt else '?'}"
            )

    print("\n--- Sample openCypher Output Preview ---")
    cypher = g_city.to_cypher_script()
    print("\n".join(cypher.splitlines()[:6]))
    print("...")


if __name__ == "__main__":
    main()
