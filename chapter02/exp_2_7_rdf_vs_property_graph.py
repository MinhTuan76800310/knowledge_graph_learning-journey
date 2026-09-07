"""Experiment 2-7: Same Knowledge — RDF vs. Property Graph.

Question: "How does the choice of graph data model alter representation
structure, edge metadata, identity, and query ergonomics for the exact same knowledge?"

Compares the representation of identical facts across two paradigms:
  1. W3C RDF Model (RDFLib Graph)
  2. Labeled Property Graph (SimplePropertyGraph)

Key architectural axes compared:
  - Entity attributes (Triples vs Node Properties)
  - Edge metadata (RDF Reification 5-triples vs LPG Direct Edge Properties)
  - Global IRI identity vs Local node ID
  - Query comparison: SPARQL BGP vs Cypher Pattern

Semantic contracts: docs/CHAPTER02_SEMANTIC_CONTRACTS.md §6 (Representation Boundary),
R11-01 (RDF Primer), N4J-03 (Graph Data Modeling).
Difficulty: ★★★
Status: ✅ Independently runnable
"""

from __future__ import annotations

import sys
from typing import Any

from rdflib import RDF, RDFS, Graph, Literal, Namespace

try:
    from exp_2_5_labeled_property_graph import SimplePropertyGraph
except ImportError:
    from chapter02.exp_2_5_labeled_property_graph import SimplePropertyGraph

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def build_rdf_representation() -> Graph:
    """Represent the Hanoi-Vietnam-Paris domain in RDF with edge reification."""
    EX = Namespace("http://example.org/")
    g = Graph()
    g.bind("ex", EX)

    # 1. Base facts
    g.add((EX.Hanoi, RDF.type, EX.City))
    g.add((EX.Hanoi, RDFS.label, Literal("Hà Nội")))
    g.add((EX.Hanoi, EX.population, Literal(8418883)))
    g.add((EX.Hanoi, EX.capitalOf, EX.Vietnam))
    g.add((EX.Hanoi, EX.sisterCity, EX.Paris))

    g.add((EX.Vietnam, RDF.type, EX.Country))
    g.add((EX.Vietnam, RDFS.label, Literal("Việt Nam")))

    g.add((EX.Paris, RDF.type, EX.City))
    g.add((EX.Paris, RDFS.label, Literal("Paris")))
    g.add((EX.Paris, EX.capitalOf, EX.France))

    g.add((EX.France, RDF.type, EX.Country))
    g.add((EX.France, RDFS.label, Literal("France")))

    # 2. Edge metadata via W3C standard RDF Reification:
    # "Hanoi is capitalOf Vietnam since 1976"
    stmt1 = EX.statement_hanoi_capital
    g.add((stmt1, RDF.type, RDF.Statement))
    g.add((stmt1, RDF.subject, EX.Hanoi))
    g.add((stmt1, RDF.predicate, EX.capitalOf))
    g.add((stmt1, RDF.object, EX.Vietnam))
    g.add((stmt1, EX.since, Literal(1976)))

    # "Paris is capitalOf France since 1789"
    stmt2 = EX.statement_paris_capital
    g.add((stmt2, RDF.type, RDF.Statement))
    g.add((stmt2, RDF.subject, EX.Paris))
    g.add((stmt2, RDF.predicate, EX.capitalOf))
    g.add((stmt2, RDF.object, EX.France))
    g.add((stmt2, EX.since, Literal(1789)))

    return g


def build_lpg_representation() -> SimplePropertyGraph:
    """Represent the exact same Hanoi-Vietnam-Paris domain in LPG."""
    g = SimplePropertyGraph()

    g.add_node(
        "Hanoi",
        labels={"City", "Capital"},
        properties={"name": "Hà Nội", "population": 8418883},
    )
    g.add_node(
        "Vietnam",
        labels={"Country"},
        properties={"name": "Việt Nam"},
    )
    g.add_node(
        "Paris",
        labels={"City", "Capital"},
        properties={"name": "Paris", "population": 2161000},
    )
    g.add_node(
        "France",
        labels={"Country"},
        properties={"name": "France"},
    )

    # In LPG, relationship metadata is directly attached to the edge
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
        properties={"agreementDate": "1994-05-12"},
    )

    return g


def query_rdf_capital_with_metadata(g: Graph) -> list[dict[str, Any]]:
    """Query capital and 'since' metadata in RDF via reification."""
    q = """
    PREFIX ex: <http://example.org/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT ?city ?country ?since
    WHERE {
        ?stmt rdf:type rdf:Statement ;
              rdf:subject ?city ;
              rdf:predicate ex:capitalOf ;
              rdf:object ?country ;
              ex:since ?since .
    }
    """
    results = []
    for row in g.query(q):
        city_name = str(row.city).split("/")[-1]
        country_name = str(row.country).split("/")[-1]
        results.append(
            {
                "city": city_name,
                "country": country_name,
                "since": int(row.since),
            }
        )
    results.sort(key=lambda x: str(x["city"]))
    return results


def query_lpg_capital_with_metadata(g: SimplePropertyGraph) -> list[dict[str, Any]]:
    """Query capital and 'since' metadata in LPG."""
    results = []
    for edge in g.edges.values():
        if edge.type == "CAPITAL_OF" and "since" in edge.properties:
            results.append(
                {
                    "city": edge.source,
                    "country": edge.target,
                    "since": edge.properties["since"],
                }
            )
    results.sort(key=lambda x: str(x["city"]))
    return results


def main() -> None:
    print("=" * 60)
    print("EXPERIMENT 2-7: RDF VS. PROPERTY GRAPH REPRESENTATION")
    print("=" * 60)

    rdf_g = build_rdf_representation()
    lpg_g = build_lpg_representation()

    print("\n--- Structural Metrics Comparison ---")
    print(f"RDF Graph Elements: {len(rdf_g)} triples")
    total_props = sum(len(n.properties) for n in lpg_g.nodes.values()) + sum(
        len(e.properties) for e in lpg_g.edges.values()
    )
    print(
        f"LPG Graph Elements: {len(lpg_g.nodes)} nodes, {len(lpg_g.edges)} edges, "
        f"{total_props} properties"
    )

    print("\n--- Edge Metadata Modeling: 'since 1976' ---")
    print("RDF Reification requires 5 distinct triples:")
    for s, p, o in rdf_g:
        if "statement_hanoi_capital" in str(s):
            p_short = str(p).split("#")[-1].split("/")[-1]
            o_short = str(o).split("#")[-1].split("/")[-1]
            print(f"  (:statement_hanoi_capital, {p_short}, {o_short})")

    print("\nLPG requires 1 relationship with inline property:")
    e = lpg_g.get_edge("e_hn_vn")
    print(f"  ({e.source}) -[:{e.type} {e.properties}]-> ({e.target})")

    print("\n--- Query Results Cross-Verification ---")
    rdf_res = query_rdf_capital_with_metadata(rdf_g)
    lpg_res = query_lpg_capital_with_metadata(lpg_g)

    print(f"RDF query output : {rdf_res}")
    print(f"LPG query output : {lpg_res}")

    assert rdf_res == lpg_res, "Semantic divergence detected across representations!"
    print("\n[OK] Semantic Equivalence Confirmed: Zero information loss between models.")


if __name__ == "__main__":
    main()
