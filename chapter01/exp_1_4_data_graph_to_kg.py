"""Experiment 1-4: Turn a Data Graph into a Simple Knowledge Graph.

Demonstrates the minimal transformation from a flat data graph to a KG
by adding: (1) typed entities, (2) defined relation semantics, and
(3) simple forward-chaining inference.

The reader observes what new queries become possible ONLY after semantics
are added — queries that were impossible on the raw data graph.
"""

from __future__ import annotations


class DataGraphToKG:
    """Minimal system showing the transition from data graph to KG."""

    def __init__(self) -> None:
        # Raw triples (data graph layer)
        self.triples: list[tuple[str, str, str]] = []
        # Schema definitions (semantics layer)
        self.relation_defs: dict[str, dict[str, str]] = {}
        # Inferred triples (knowledge layer)
        self.inferred: list[tuple[str, str, str]] = []

    def add_triple(self, s: str, p: str, o: str) -> None:
        self.triples.append((s, p, o))

    def define_relation(
        self,
        name: str,
        domain: str | None = None,
        range_: str | None = None,
        symmetric: bool = False,
        transitive: bool = False,
    ) -> None:
        self.relation_defs[name] = {
            "domain": domain or "",
            "range": range_ or "",
            "symmetric": str(symmetric),
            "transitive": str(transitive),
        }

    def run_inference(self) -> int:
        """Forward-chaining inference. Returns number of new triples inferred."""
        all_triples = set(self.triples)
        changed = True
        new_count = 0
        while changed:
            changed = False
            additions: list[tuple[str, str, str]] = []
            for s, p, o in list(all_triples):
                rdef = self.relation_defs.get(p, {})
                # Domain inference
                if rdef.get("domain") and (s, "rdf:type", rdef["domain"]) not in all_triples:
                    additions.append((s, "rdf:type", rdef["domain"]))
                # Range inference
                if rdef.get("range") and (o, "rdf:type", rdef["range"]) not in all_triples:
                    additions.append((o, "rdf:type", rdef["range"]))
                # Symmetric inference
                if rdef.get("symmetric") == "True" and (o, p, s) not in all_triples:
                    additions.append((o, p, s))
                # Transitive inference
                if rdef.get("transitive") == "True":
                    for s2, p2, o2 in list(all_triples):
                        if p2 == p and o == s2 and (s, p, o2) not in all_triples:
                            additions.append((s, p, o2))
            for t in additions:
                if t not in all_triples:
                    all_triples.add(t)
                    self.inferred.append(t)
                    new_count += 1
                    changed = True
        return new_count

    def query_type(self, type_name: str) -> set[str]:
        """Return all entities of a given type (asserted + inferred)."""
        result: set[str] = set()
        for s, p, o in self.triples + self.inferred:
            if p == "rdf:type" and o == type_name:
                result.add(s)
        return result

    def query_relation(self, rel: str, entity: str) -> set[str]:
        """Return all objects connected to entity via relation (asserted + inferred)."""
        result: set[str] = set()
        for s, p, o in self.triples + self.inferred:
            if p == rel and s == entity:
                result.add(o)
        return result


def main() -> None:
    print("=" * 60)
    print("EXPERIMENT 1-4: Data Graph → Simple Knowledge Graph")
    print("=" * 60)

    kg = DataGraphToKG()

    # --- Step 1: Raw data graph (no semantics) ---
    print("\n--- STEP 1: Raw Data Graph ---")
    kg.add_triple("Hanoi", "locatedIn", "RedRiverDelta")
    kg.add_triple("HCMC", "locatedIn", "Southeast")
    kg.add_triple("DaNang", "locatedIn", "SouthCentralCoast")
    kg.add_triple("RedRiverDelta", "partOf", "NorthernVietnam")
    kg.add_triple("Southeast", "partOf", "SouthernVietnam")
    kg.add_triple("Hanoi", "type", "City")
    kg.add_triple("HCMC", "type", "City")

    print(f"Triples: {len(kg.triples)}")
    for t in kg.triples:
        print(f"  {t}")
    print(f"\nQuery: entities of type 'Region'? → {kg.query_type('Region')}")
    print("  (Empty! The graph has no way to know RedRiverDelta is a Region.)")
    print(f"Query: where is DaNang located? → {kg.query_relation('locatedIn', 'DaNang')}")
    print("Query: is DaNang in NorthernVietnam? → Cannot answer without transitive reasoning.")

    # --- Step 2: Add semantics ---
    print("\n--- STEP 2: Adding Semantics (Schema Definitions) ---")
    kg.define_relation("locatedIn", domain="City", range_="Region")
    kg.define_relation("partOf", domain="Region", range_="GeographicArea", transitive=True)
    kg.define_relation("type")  # No constraints, just registered

    print("Defined relations:")
    for name, rdef in kg.relation_defs.items():
        print(f"  {name}: {rdef}")

    # --- Step 3: Run inference ---
    print("\n--- STEP 3: Running Forward-Chaining Inference ---")
    n = kg.run_inference()
    print(f"Inferred {n} new triples:")
    for t in kg.inferred:
        print(f"  [INFERRED] {t}")

    # --- Step 4: New queries now possible ---
    print("\n--- STEP 4: Queries Now Possible After Semantics ---")
    print(f"Entities of type 'Region': {kg.query_type('Region')}")
    print(f"Entities of type 'City': {kg.query_type('City')}")
    print(f"Entities of type 'GeographicArea': {kg.query_type('GeographicArea')}")
    print(f"Where is DaNang located? → {kg.query_relation('locatedIn', 'DaNang')}")
    in_south = "SouthernVietnam" in kg.query_relation("partOf", "SouthCentralCoast")
    print(f"Is DaNang in SouthernVietnam? → {'Yes' if in_south else 'No'}")
    print(f"RedRiverDelta partOf chain: {kg.query_relation('partOf', 'RedRiverDelta')}")

    print("\n--- Key Observation ---")
    print("BEFORE semantics: 'Region', 'GeographicArea', transitive partOf did not exist.")
    print("AFTER semantics + inference: these concepts emerge automatically from rules.")
    print("The SAME raw triples now support richer queries because meaning was ADDED,")
    print("not because more data was stored.")
    print("This is the fundamental shift from Data Graph to Knowledge Graph.")


if __name__ == "__main__":
    main()
