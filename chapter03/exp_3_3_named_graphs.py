"""Experiment 3-3: Named Graphs & TriG Quad Datasets.

Question: "How do Named Graphs partition knowledge into quads (s, p, o, g),
and how does SPARQL query across graph boundaries?"

Demonstrates:
  1. TriG serialization: grouping triples under named graph IRIs.
  2. Quad storage in RDFLib Dataset: separating conflicting temporal claims
     (e.g., Census 2019 vs. Census 2023) without graph mutation or clash.
  3. SPARQL graph pattern matching:
     - Querying inside a specific named graph (GRAPH <uri> { ... })
     - Querying across all named graphs dynamically (GRAPH ?g { ... })
     - Default graph vs. named graph isolation
  4. Crucial boundary: A graph IRI is a syntactic grouping mechanism; it does NOT
     inherently assert epistemic truth, authority, or provenance (bridge to Ch6).

Semantic contracts: R11-02 (RDF 1.1 Concepts §4), SP11-02 (SPARQL 1.1 Dataset),
docs/CHAPTER03_SEMANTIC_CONTRACTS.md §Named Graph / RDF Dataset.
Difficulty: ★★
Status: ✅ Independently runnable
"""

from __future__ import annotations

import sys
from typing import Any

from rdflib import Dataset, Namespace

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

EX = Namespace("http://example.org/")

TRIG_DATA = """
@prefix ex: <http://example.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

# Default graph: Core entity existence and canonical labels
ex:Hanoi a ex:City ;
         ex:name "Hà Nội" .

# Named Graph 1: 2019 National Census Context
ex:graph_census_2019 {
    ex:Hanoi ex:population 8053663 ;
             ex:censusYear 2019 ;
             ex:source "GSO_Census_2019" .
}

# Named Graph 2: 2023 Statistical Yearbook Context
ex:graph_census_2023 {
    ex:Hanoi ex:population 8418883 ;
             ex:censusYear 2023 ;
             ex:source "GSO_Yearbook_2023" .
}
"""


def load_quad_dataset() -> Dataset:
    """Parse TriG data into an RDFLib Dataset."""
    ds = Dataset()
    ds.parse(data=TRIG_DATA, format="trig")
    return ds


def query_specific_graph(ds: Dataset, graph_iri: str) -> list[dict[str, Any]]:
    """Query population specifically within one named graph context."""
    q = f"""
    PREFIX ex: <http://example.org/>
    SELECT ?city ?pop ?year
    WHERE {{
        GRAPH <{graph_iri}> {{
            ?city ex:population ?pop ;
                  ex:censusYear ?year .
        }}
    }}
    """
    results = []
    for row in ds.query(q):
        results.append(
            {
                "city": str(row.city).split("/")[-1],
                "population": int(row.pop),
                "year": int(row.year),
            }
        )
    return sorted(results, key=lambda x: x["year"])


def query_all_contexts(ds: Dataset) -> list[dict[str, Any]]:
    """Query all contexts simultaneously, binding the graph IRI as a variable."""
    q = """
    PREFIX ex: <http://example.org/>
    SELECT ?g ?city ?pop ?year
    WHERE {
        GRAPH ?g {
            ?city ex:population ?pop ;
                  ex:censusYear ?year .
        }
    }
    """
    results = []
    for row in ds.query(q):
        results.append(
            {
                "graph": str(row.g).split("/")[-1],
                "city": str(row.city).split("/")[-1],
                "population": int(row.pop),
                "year": int(row.year),
            }
        )
    return sorted(results, key=lambda x: x["year"])


def query_default_graph(ds: Dataset) -> list[dict[str, Any]]:
    """Query the default graph (unnamed triples)."""
    q = """
    PREFIX ex: <http://example.org/>
    SELECT ?city ?name
    WHERE {
        ?city a ex:City ;
              ex:name ?name .
    }
    """
    results = []
    for row in ds.query(q):
        results.append(
            {
                "city": str(row.city).split("/")[-1],
                "name": str(row.name),
            }
        )
    return results


def main() -> None:
    print("=" * 60)
    print("EXPERIMENT 3-3: NAMED GRAPHS & TRIG QUAD DATASETS")
    print("=" * 60)

    ds = load_quad_dataset()
    print(f"\nDataset loaded with {len(list(ds.graphs()))} active graph contexts.")

    # 1. Default graph query
    print("\n--- 1. Default Graph Query (Identity & Canonical Name) ---")
    default_res = query_default_graph(ds)
    for r in default_res:
        print(f"  Entity: {r['city']}, Canonical Name: {r['name']}")

    # 2. Specific named graph query
    print("\n--- 2. Isolated Context Query: Census 2019 vs 2023 ---")
    res_2019 = query_specific_graph(ds, str(EX.graph_census_2019))
    res_2023 = query_specific_graph(ds, str(EX.graph_census_2023))
    print(f"  In ex:graph_census_2019: {res_2019}")
    print(f"  In ex:graph_census_2023: {res_2023}")

    # 3. Cross-context variable graph query
    print("\n--- 3. Multi-Context Dynamic Query: GRAPH ?g { ... } ---")
    all_res = query_all_contexts(ds)
    for r in all_res:
        print(f"  Context [{r['graph']}]: {r['city']} population = {r['population']} ({r['year']})")

    print("\n[KEY ARCHITECTURAL INSIGHT]:")
    print("  - Quads (s, p, o, g) prevent conflicting observations from colliding.")
    print("  - Graph IRIs partition statements; epistemic trust (source credibility,")
    print("    signature, timestamp) must be modeled explicitly (see Chapter 6).")


if __name__ == "__main__":
    main()
