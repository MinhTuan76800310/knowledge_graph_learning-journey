"""Experiment 1-2: Data Graph vs Taxonomy.

Demonstrates the difference between a flat data graph (entities + relations)
and a taxonomy (hierarchical classification with subclass relationships).
Shows that taxonomies add structural meaning through is-a hierarchies.
"""

from __future__ import annotations


class DataGraph:
    """Flat data graph: entities with typed relations, no hierarchy."""

    def __init__(self) -> None:
        self.entities: set[str] = set()
        self.relations: list[tuple[str, str, str]] = []

    def add_entity(self, entity: str) -> None:
        self.entities.add(entity)

    def add_relation(self, subject: str, predicate: str, obj: str) -> None:
        self.entities.add(subject)
        self.entities.add(obj)
        self.relations.append((subject, predicate, obj))

    def query(self, predicate: str) -> list[tuple[str, str]]:
        """Return all (subject, object) pairs for a given predicate."""
        return [(s, o) for s, p, o in self.relations if p == predicate]

    def summary(self) -> str:
        lines = [f"Entities ({len(self.entities)}): {sorted(self.entities)}"]
        lines.append(f"Relations ({len(self.relations)}):")
        for s, p, o in self.relations:
            lines.append(f"  {s} --[{p}]--> {o}")
        return "\n".join(lines)


class Taxonomy:
    """Hierarchical taxonomy with subclass relationships."""

    def __init__(self) -> None:
        self.classes: set[str] = set()
        self.subclass_of: list[tuple[str, str]] = []
        self.instances: list[tuple[str, str]] = []

    def add_class(self, cls: str) -> None:
        self.classes.add(cls)

    def add_subclass(self, child: str, parent: str) -> None:
        self.classes.add(child)
        self.classes.add(parent)
        self.subclass_of.append((child, parent))

    def add_instance(self, instance: str, cls: str) -> None:
        self.classes.add(cls)
        self.instances.append((instance, cls))

    def ancestors(self, cls: str) -> set[str]:
        """Return all transitive superclasses of a class."""
        result: set[str] = set()
        queue = [cls]
        while queue:
            current = queue.pop()
            for child, parent in self.subclass_of:
                if child == current and parent not in result:
                    result.add(parent)
                    queue.append(parent)
        return result

    def all_instances_of(self, cls: str) -> set[str]:
        """Return direct instances plus instances of all subclasses."""
        sub = self._all_subclasses(cls)
        relevant_classes = sub | {cls}
        return {inst for inst, c in self.instances if c in relevant_classes}

    def _all_subclasses(self, cls: str) -> set[str]:
        """Return all transitive subclasses of a class."""
        result: set[str] = set()
        queue = [cls]
        while queue:
            current = queue.pop()
            for child, parent in self.subclass_of:
                if parent == current and child not in result:
                    result.add(child)
                    queue.append(child)
        return result

    def summary(self) -> str:
        lines = [f"Classes ({len(self.classes)}): {sorted(self.classes)}"]
        lines.append("Subclass relationships:")
        for child, parent in self.subclass_of:
            lines.append(f"  {child} rdfs:subClassOf {parent}")
        lines.append("Instances:")
        for inst, cls in self.instances:
            lines.append(f"  {inst} rdf:type {cls}")
        return "\n".join(lines)


def build_data_graph() -> DataGraph:
    """Build a flat data graph about Vietnamese cities."""
    g = DataGraph()
    g.add_relation("Hanoi", "type", "City")
    g.add_relation("HCMC", "type", "City")
    g.add_relation("DaNang", "type", "City")
    g.add_relation("Hanoi", "capitalOf", "Vietnam")
    g.add_relation("Hanoi", "locatedIn", "RedRiverDelta")
    g.add_relation("HCMC", "locatedIn", "Southeast")
    g.add_relation("DaNang", "locatedIn", "SouthCentralCoast")
    g.add_relation("RedRiverDelta", "type", "Region")
    g.add_relation("Southeast", "type", "Region")
    g.add_relation("SouthCentralCoast", "type", "Region")
    return g


def build_taxonomy() -> Taxonomy:
    """Build a taxonomy of geographic entities."""
    t = Taxonomy()
    t.add_subclass("City", "GeographicEntity")
    t.add_subclass("Region", "GeographicEntity")
    t.add_subclass("CapitalCity", "City")
    t.add_subclass("Province", "GeographicEntity")

    t.add_instance("Hanoi", "CapitalCity")
    t.add_instance("HCMC", "City")
    t.add_instance("DaNang", "City")
    t.add_instance("RedRiverDelta", "Region")
    t.add_instance("Southeast", "Region")
    t.add_instance("SouthCentralCoast", "Region")
    return t


def main() -> None:
    print("=" * 60)
    print("EXPERIMENT 1-2: Data Graph vs Taxonomy")
    print("=" * 60)

    print("\n--- Flat Data Graph ---")
    dg = build_data_graph()
    print(dg.summary())
    print(f"\nQuery 'type': {dg.query('type')}")
    print(f"Query 'locatedIn': {dg.query('locatedIn')}")

    print("\n--- Taxonomy ---")
    tax = build_taxonomy()
    print(tax.summary())
    print(f"\nAncestors of CapitalCity: {tax.ancestors('CapitalCity')}")
    print(f"All instances of GeographicEntity: {tax.all_instances_of('GeographicEntity')}")
    print(f"All instances of City (includes CapitalCity): {tax.all_instances_of('City')}")

    print("\n--- Key Observation ---")
    print("Data graph: 'type' is just another relation label. No inference.")
    print("  Querying for 'City' returns only direct matches, not subclasses.")
    print("Taxonomy: subclass relationships enable transitive queries.")
    print("  Asking for all 'City' instances automatically includes 'CapitalCity' instances.")
    print("  This is STRUCTURAL MEANING encoded in the graph itself.")


if __name__ == "__main__":
    main()
