"""Experiment 1-3: Winterthur Sister-City Lesson (Original Reproduction).

Progressively transforms a plain graph into a knowledge graph by adding:
1. Labeled edges (data graph)
2. Taxonomy (subclass hierarchy)
3. Ontology (RDFS domain/range inference + OWL-inspired symmetric property)
4. Context (source, temporal validity)

Uses original Vietnamese city data instead of copying Stanford's Winterthur example.
"""

from __future__ import annotations


# --- Stage 1: Plain Graph ---
class PlainGraph:
    def __init__(self) -> None:
        self.nodes: set[str] = set()
        self.edges: list[tuple[str, str]] = []

    def add_edge(self, src: str, tgt: str) -> None:
        self.nodes.add(src)
        self.nodes.add(tgt)
        self.edges.append((src, tgt))

    def summary(self) -> str:
        lines = [f"Nodes: {sorted(self.nodes)}"]
        lines.append("Edges:")
        for s, t in self.edges:
            lines.append(f"  {s} --> {t}")
        return "\n".join(lines)


# --- Stage 2: Data Graph ---
class DataGraph:
    def __init__(self) -> None:
        self.triples: list[tuple[str, str, str]] = []

    def add(self, s: str, p: str, o: str) -> None:
        self.triples.append((s, p, o))

    def query(self, predicate: str) -> list[tuple[str, str]]:
        return [(s, o) for s, p, o in self.triples if p == predicate]

    def summary(self) -> str:
        lines = ["Triples:"]
        for s, p, o in self.triples:
            lines.append(f"  ({s}, {p}, {o})")
        return "\n".join(lines)


# --- Stage 3: Taxonomy ---
class TaxonomyGraph(DataGraph):
    def __init__(self) -> None:
        super().__init__()
        self.subclass_map: dict[str, set[str]] = {}

    def add_subclass(self, child: str, parent: str) -> None:
        self.subclass_map.setdefault(parent, set()).add(child)
        self.add(child, "rdfs:subClassOf", parent)

    def all_instances_of(self, cls: str) -> set[str]:
        """Return direct instances + instances of all subclasses."""
        subclasses = self._transitive_subclasses(cls)
        relevant = subclasses | {cls}
        return {s for s, p, o in self.triples if p == "rdf:type" and o in relevant}

    def _transitive_subclasses(self, cls: str) -> set[str]:
        result: set[str] = set()
        queue = [cls]
        while queue:
            current = queue.pop()
            for child in self.subclass_map.get(current, set()):
                if child not in result:
                    result.add(child)
                    queue.append(child)
        return result


# --- Stage 4: Simple KG with domain/range inference ---
class SimpleKnowledgeGraph(TaxonomyGraph):
    def __init__(self) -> None:
        super().__init__()
        self.domains: dict[str, str] = {}
        self.ranges: dict[str, str] = {}
        self.symmetric_props: set[str] = set()

    def set_domain(self, prop: str, cls: str) -> None:
        self.domains[prop] = cls
        self.add(prop, "rdfs:domain", cls)

    def set_range(self, prop: str, cls: str) -> None:
        self.ranges[prop] = cls
        self.add(prop, "rdfs:range", cls)

    def mark_symmetric(self, prop: str) -> None:
        self.symmetric_props.add(prop)
        self.add(prop, "rdf:type", "owl:SymmetricProperty")

    def infer(self) -> list[str]:
        """Run toy forward-chaining reasoner with selected RDFS + OWL-inspired rules.

        Implements: RDFS domain/range type inference, subclass transitivity,
        and OWL-inspired symmetric property inference.
        This is NOT full RDFS or OWL entailment. See OWL-01 for standard semantics.

        Returns list of inferred triples as strings.
        """
        inferred: list[str] = []
        existing = set(self.triples)

        # Domain/range inference
        for s, p, o in list(self.triples):
            if p in self.domains:
                domain_triple = (s, "rdf:type", self.domains[p])
                if domain_triple not in existing:
                    self.add(s, "rdf:type", self.domains[p])
                    existing.add(domain_triple)
                    inferred.append(f"INFERRED (domain): {s} rdf:type {self.domains[p]}")
            if p in self.ranges:
                range_triple = (o, "rdf:type", self.ranges[p])
                if range_triple not in existing:
                    self.add(o, "rdf:type", self.ranges[p])
                    existing.add(range_triple)
                    inferred.append(f"INFERRED (range): {o} rdf:type {self.ranges[p]}")

        # Symmetric property inference
        for s, p, o in list(self.triples):
            if p in self.symmetric_props:
                reverse_triple = (o, p, s)
                if reverse_triple not in existing:
                    self.add(o, p, s)
                    existing.add(reverse_triple)
                    inferred.append(f"INFERRED (owl:SymmetricProperty-inspired): ({o}, {p}, {s})")

        # Subclass transitivity on types
        changed = True
        while changed:
            changed = False
            for s, p, o in list(self.triples):
                if p == "rdf:type":
                    for parent in list(self.subclass_map.keys()):
                        if o in self.subclass_map.get(parent, set()):
                            super_triple = (s, "rdf:type", parent)
                            if super_triple not in existing:
                                self.add(s, "rdf:type", parent)
                                existing.add(super_triple)
                                inferred.append(f"INFERRED (subclass): {s} rdf:type {parent}")
                                changed = True
        return inferred


def main() -> None:
    print("=" * 70)
    print("EXPERIMENT 1-3: Progressive Transformation to Knowledge Graph")
    print("Domain: Vietnamese sister-city relationships (original data)")
    print("=" * 70)

    # Stage 1
    print("\n--- STAGE 1: Plain Graph (no semantics) ---")
    pg = PlainGraph()
    pg.add_edge("Hue", "DaNang")
    pg.add_edge("Hue", "CanTho")
    pg.add_edge("DaNang", "HaiPhong")
    print(pg.summary())
    print("Problem: What does the edge mean? Machine cannot tell.")

    # Stage 2
    print("\n--- STAGE 2: Data Graph (labeled edges) ---")
    dg = DataGraph()
    dg.add("Hue", "sisterCity", "DaNang")
    dg.add("Hue", "sisterCity", "CanTho")
    dg.add("DaNang", "sisterCity", "HaiPhong")
    dg.add("Hue", "type", "City")
    print(dg.summary())
    print("Problem: 'sisterCity' is just a string. No domain/range. No symmetry.")

    # Stage 3
    print("\n--- STAGE 3: Taxonomy (subclass hierarchy) ---")
    tg = TaxonomyGraph()
    tg.add_subclass("City", "Settlement")
    tg.add_subclass("CapitalCity", "City")
    tg.add_subclass("Province", "AdministrativeUnit")
    tg.add_subclass("Settlement", "GeographicEntity")
    tg.add("Hue", "rdf:type", "City")
    tg.add("DaNang", "rdf:type", "City")
    tg.add("CanTho", "rdf:type", "City")
    tg.add("HaiPhong", "rdf:type", "City")
    tg.add("Hanoi", "rdf:type", "CapitalCity")
    print(tg.summary())
    print(f"All instances of City (includes CapitalCity): {tg.all_instances_of('City')}")
    print(f"All instances of GeographicEntity: {tg.all_instances_of('GeographicEntity')}")

    # Stage 4
    print("\n--- STAGE 4: Simple Knowledge Graph (ontology + inference) ---")
    kg = SimpleKnowledgeGraph()
    kg.add_subclass("City", "Settlement")
    kg.add_subclass("CapitalCity", "City")
    kg.add_subclass("Settlement", "GeographicEntity")

    kg.set_domain("sisterCity", "City")
    kg.set_range("sisterCity", "City")
    kg.mark_symmetric("sisterCity")

    kg.add("Hue", "sisterCity", "DaNang")
    kg.add("Hue", "sisterCity", "CanTho")
    kg.add("DaNang", "sisterCity", "HaiPhong")
    kg.add("Hue", "rdf:type", "City")

    print("Asserted triples:")
    for s, p, o in kg.triples:
        if not any(inf.startswith("INFERRED") for inf in []):
            print(f"  ({s}, {p}, {o})")

    print("\nRunning inference...")
    inferred = kg.infer()
    for line in inferred:
        print(f"  {line}")

    print(f"\nAll instances of City after inference: {kg.all_instances_of('City')}")
    print(f"Sister cities of DaNang (includes inferred reverse): {kg.query('sisterCity')}")

    # Stage 5 mention
    print("\n--- STAGE 5 Preview: Context (not implemented here) ---")
    print("In a full KG, each claim would carry:")
    print("  - source: e.g., cityCouncil_decree_2019")
    print("  - validFrom: 2019-06-15")
    print("  - confidence: 0.95")
    print("This enables handling contradictions and temporal queries.")
    print("See Chapter 6 for full provenance modeling.")

    print("\n--- Key Takeaway ---")
    print("Each stage adds information that was ABSENT before:")
    print("  Plain → labels give human-readable meaning")
    print("  Data → taxonomy enables transitive classification")
    print("  Taxonomy → ontology enables automatic inference (domain/range/symmetry)")
    print("  KG → context enables trust, time, and contradiction management")


if __name__ == "__main__":
    main()
