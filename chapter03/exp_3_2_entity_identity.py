"""Experiment 3-2: Entity Identity & owl:sameAs Information Merging.

Question: "How does identity propagation work under owl:sameAs, and why is the
No Unique Name Assumption (No-UNA) a catastrophic hazard when misused?"

Demonstrates:
  1. Identity propagation: Merging independent assertions about Hanoi across
     a local graph (ex:Hanoi) and a Wikidata excerpt (wd:Q1858).
  2. Complete role interchangeability: under OWL semantics, if a owl:sameAs b,
     every property and class assertion on b transfers to a.
  3. Catastrophic Merge Hazard (Misusing owl:sameAs for similarity):
     When a flawed heuristic asserts DaNang owl:sameAs Hanoi, No-UNA silently
     collapses distinct geographic entities into one entity, destroying data veracity.

Semantic contracts: OWL-01, OWL-02 (OWL 2 Primer §5.3, No-UNA),
docs/CHAPTER03_SEMANTIC_CONTRACTS.md §owl:sameAs.
Difficulty: ★★
Status: ✅ Independently runnable
"""

from __future__ import annotations

import sys
from collections import defaultdict
from typing import Any

from rdflib import OWL, RDF, RDFS, Graph, Literal, Namespace, URIRef

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

EX = Namespace("http://example.org/")
WD = Namespace("http://www.wikidata.org/entity/")
WDT = Namespace("http://www.wikidata.org/prop/direct/")


class SameAsClosureEngine:
    """Computes reflexive, symmetric, and transitive closure of owl:sameAs statements

    and projects unified entity views across identity equivalence classes.
    """

    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.parent: dict[URIRef, URIRef] = {}
        self._build_index()

    def _find(self, x: URIRef) -> URIRef:
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self._find(self.parent[x])
        return self.parent[x]

    def _union(self, x: URIRef, y: URIRef) -> None:
        root_x = self._find(x)
        root_y = self._find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

    def _build_index(self) -> None:
        """Find all owl:sameAs assertions in the graph and build disjoint sets."""
        for s, _, o in self.graph.triples((None, OWL.sameAs, None)):
            if isinstance(s, URIRef) and isinstance(o, URIRef):
                self._union(s, o)

    def get_unified_properties(self, entity_iri: URIRef) -> dict[str, set[Any]]:
        """Return all properties for entity_iri and all its owl:sameAs aliases."""
        root = self._find(entity_iri)
        # Collect all terms in the same equivalence class
        synonyms = {term for term in self.parent if self._find(term) == root} | {entity_iri}

        properties: dict[str, set[Any]] = defaultdict(set)
        for syn in synonyms:
            for _, p, o in self.graph.triples((syn, None, None)):
                if p != OWL.sameAs:
                    p_name = str(p).split("#")[-1].split("/")[-1]
                    properties[p_name].add(str(o))
        return dict(properties)


def build_federated_identity_graph() -> Graph:
    """Builds two independent knowledge sources about Hanoi and links them via owl:sameAs."""
    g = Graph()
    g.bind("ex", EX)
    g.bind("wd", WD)
    g.bind("wdt", WDT)
    g.bind("owl", OWL)

    # Source 1: Local Knowledge Graph
    g.add((EX.Hanoi, RDF.type, EX.City))
    g.add((EX.Hanoi, RDFS.label, Literal("Hanoi", lang="en")))
    g.add((EX.Hanoi, EX.population, Literal(8053663)))
    g.add((EX.Hanoi, EX.capitalOf, EX.Vietnam))

    # Source 2: External Open Data (Wikidata extract)
    g.add((WD.Q1858, RDF.type, WD.Q515))  # Q515 = city
    g.add((WD.Q1858, RDFS.label, Literal("Hà Nội", lang="vi")))
    g.add((WD.Q1858, WDT.P1082, Literal(8246540)))  # P1082 = population
    g.add((WD.Q1858, EX.elevationAboveSeaLevel, Literal(16)))

    # Source 3: Distinct city Da Nang
    g.add((EX.DaNang, RDF.type, EX.City))
    g.add((EX.DaNang, RDFS.label, Literal("Đà Nẵng", lang="vi")))
    g.add((EX.DaNang, EX.population, Literal(1220190)))
    g.add((EX.DaNang, EX.famousBridge, Literal("Dragon Bridge")))

    return g


def main() -> None:
    print("=" * 60)
    print("EXPERIMENT 3-2: ENTITY IDENTITY & OWL:SAMEAS PROPAGATION")
    print("=" * 60)

    g = build_federated_identity_graph()

    # Step 1: Query before linking
    print("\n--- 1. Querying Local ex:Hanoi Before Identity Linking ---")
    engine1 = SameAsClosureEngine(g)
    props_before = engine1.get_unified_properties(EX.Hanoi)
    for p, vals in sorted(props_before.items()):
        print(f"  {p}: {sorted(vals)}")

    # Step 2: Assert legitimate identity link
    print("\n--- 2. Asserting: ex:Hanoi owl:sameAs wd:Q1858 ---")
    g.add((EX.Hanoi, OWL.sameAs, WD.Q1858))
    engine2 = SameAsClosureEngine(g)
    props_after = engine2.get_unified_properties(EX.Hanoi)
    print("Unified Entity View for ex:Hanoi (Information Merged):")
    for p, vals in sorted(props_after.items()):
        print(f"  + {p}: {sorted(vals)}")

    # Step 3: Catastrophic Merge Hazard (Violating Unique Name Assumption)
    print("\n--- 3. Catastrophic Merge Hazard (Misusing owl:sameAs) ---")
    print("Simulating erroneous linkage: asserting ex:DaNang owl:sameAs ex:Hanoi ...")
    g.add((EX.DaNang, OWL.sameAs, EX.Hanoi))

    engine3 = SameAsClosureEngine(g)
    props_collapsed = engine3.get_unified_properties(EX.DaNang)
    print("\nCatastrophic Consequence under No-UNA (Hanoi and Da Nang collapsed into one):")
    for p, vals in sorted(props_collapsed.items()):
        print(f"  ! {p}: {sorted(vals)}")

    print("\n[CRITICAL LESSON]:")
    print("  - owl:sameAs means STRICT MATHEMATICAL IDENTITY, not similarity.")
    print("  - Because OWL has No Unique Name Assumption (No-UNA), erroneous links")
    print("    will silently collapse distinct real-world entities into a single entity.")


if __name__ == "__main__":
    main()
