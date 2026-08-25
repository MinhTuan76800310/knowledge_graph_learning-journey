"""Experiment 1-5: Define the Semantics of a Relation.

Demonstrates that defining relation semantics (domain, range, symmetry,
transitivity, inverse) enables automatic inference via RDFS-style entailment.

IMPORTANT: Domain/range in this experiment produce TYPE INFERENCES (RDFS
semantics per W3C RDF Schema 1.1 S3.1-3.2), NOT validation violations.
For constraint checking / violation reporting, see SHACL in Chapter 5.

Difficulty: ★★★ Research/Design Challenge
Status: ✅ Independently runnable
"""

from __future__ import annotations


class RelationSemantics:
    """A system for defining and applying relation semantics via RDFS-style entailment."""

    def __init__(self) -> None:
        self.triples: list[tuple[str, str, str]] = []
        self.relation_defs: dict[str, dict[str, object]] = {}
        self.inferred: list[tuple[str, str, str]] = []

    def define_relation(
        self,
        name: str,
        domain: str | None = None,
        range_: str | None = None,
        symmetric: bool = False,
        transitive: bool = False,
        inverse_of: str | None = None,
    ) -> None:
        """Define semantic properties of a relation."""
        self.relation_defs[name] = {
            "domain": domain,
            "range": range_,
            "symmetric": symmetric,
            "transitive": transitive,
            "inverse_of": inverse_of,
        }

    def add_triple(self, s: str, p: str, o: str) -> None:
        """Add a triple and apply RDFS-style entailment for domain/range."""
        self.triples.append((s, p, o))
        self._apply_rdfs_domain_range(s, p, o)

    def _apply_rdfs_domain_range(self, s: str, p: str, o: str) -> None:
        """Apply RDFS domain/range entailment (W3C RDF Schema 1.1 S3.1-3.2).

        If P rdfs:domain C and (s, P, o), infer (s, rdf:type, C).
        If P rdfs:range C and (s, P, o), infer (o, rdf:type, C).

        This is INFERENCE, not validation. No data is rejected.
        Source contract: R11-03 (docs/research_notes/R11-03.md).
        """
        if p not in self.relation_defs:
            return
        defn = self.relation_defs[p]
        if defn["domain"]:
            type_triple = (s, "rdf:type", defn["domain"])
            if type_triple not in self.inferred:
                self.inferred.append(type_triple)
        if defn["range"]:
            type_triple = (o, "rdf:type", defn["range"])
            if type_triple not in self.inferred:
                self.inferred.append(type_triple)

    def infer(self) -> list[tuple[str, str, str]]:
        """Run forward-chaining inference based on relation definitions."""
        new_triples: list[tuple[str, str, str]] = []
        changed = True
        all_triples = set(self.triples)

        while changed:
            changed = False
            current = set(all_triples)

            for s, p, o in list(current):
                if p not in self.relation_defs:
                    continue
                defn = self.relation_defs[p]

                # Symmetry: if (s, p, o) then (o, p, s)
                if defn["symmetric"]:
                    rev = (o, p, s)
                    if rev not in all_triples:
                        all_triples.add(rev)
                        new_triples.append(rev)
                        changed = True

                # Transitivity: if (s, p, o) and (o, p, x) then (s, p, x)
                if defn["transitive"]:
                    for s2, p2, o2 in list(current):
                        if p2 == p and s2 == o:
                            trans = (s, p, o2)
                            if trans not in all_triples:
                                all_triples.add(trans)
                                new_triples.append(trans)
                                changed = True

                # Inverse: if (s, p, o) and p has inverse q, then (o, q, s)
                if defn["inverse_of"]:
                    inv_p = defn["inverse_of"]
                    inv_triple = (o, inv_p, s)
                    if inv_triple not in all_triples:
                        all_triples.add(inv_triple)
                        new_triples.append(inv_triple)
                        changed = True

        # Append symmetry/transitivity/inverse inferences (domain/range already added)
        self.inferred.extend(new_triples)
        return self.inferred

    def summary(self) -> str:
        lines = ["Asserted triples:"]
        for s, p, o in self.triples:
            lines.append(f"  ({s}, {p}, {o})")
        lines.append("\nRelation definitions:")
        for name, defn in self.relation_defs.items():
            props = []
            if defn["domain"]:
                props.append(f"domain={defn['domain']}")
            if defn["range"]:
                props.append(f"range={defn['range']}")
            if defn["symmetric"]:
                props.append("symmetric")
            if defn["transitive"]:
                props.append("transitive")
            if defn["inverse_of"]:
                props.append(f"inverseOf={defn['inverse_of']}")
            lines.append(f"  {name}: {', '.join(props) if props else '(no semantic properties)'}")
        if self.inferred:
            lines.append(f"\nInferred triples ({len(self.inferred)}):")
            for s, p, o in self.inferred:
                lines.append(f"  ({s}, {p}, {o})")
        return "\n".join(lines)


def main() -> None:
    print("=" * 60)
    print("EXPERIMENT 1-5: Define the Semantics of a Relation")
    print("=" * 60)

    kg = RelationSemantics()

    # Define relation semantics
    kg.define_relation("sisterCity", symmetric=True, domain="City", range_="City")
    kg.define_relation("locatedIn", domain="City", range_="Region")
    kg.define_relation("partOf", transitive=True, domain="Region", range_="Region")
    kg.define_relation("capitalOf", inverse_of="hasCapital", domain="City", range_="Country")
    kg.define_relation("hasCapital", inverse_of="capitalOf", domain="Country", range_="City")

    # Add data
    kg.add_triple("Hanoi", "capitalOf", "Vietnam")
    kg.add_triple("Hanoi", "locatedIn", "RedRiverDelta")
    kg.add_triple("RedRiverDelta", "partOf", "NorthernVietnam")
    kg.add_triple("NorthernVietnam", "partOf", "Vietnam")
    kg.add_triple("Hue", "sisterCity", "DaNang")
    kg.add_triple("HCMC", "locatedIn", "Southeast")
    kg.add_triple("Southeast", "partOf", "SouthernVietnam")

    print("\n--- Before Inference ---")
    print(kg.summary())

    inferred = kg.infer()
    print(f"\n--- After Inference ({len(inferred)} new triples) ---")
    print(kg.summary())

    print("\n--- Key Observations ---")
    print("1. SYMMETRY: 'Hue sisterCity DaNang' automatically yields 'DaNang sisterCity Hue'.")
    print("   Without declaring symmetry, this reverse edge would be missing.")
    msg = "2. TRANSITIVITY: 'RedRiverDelta partOf NorthernVietnam'"
    msg += " + 'NorthernVietnam partOf Vietnam'"
    print(msg)
    print("   yields 'RedRiverDelta partOf Vietnam'. The chain emerges from the rule.")
    print("3. INVERSE: 'Hanoi capitalOf Vietnam' yields 'Vietnam hasCapital Hanoi'.")
    print("   Two relations are linked by definition, not by duplicate data entry.")
    print("4. DOMAIN/RANGE (RDFS semantics): These INFERENCE rules add type information.")
    print("   If (X, capitalOf, Y) and domain=City, then X rdf:type City is INFERRED.")
    print("   RDFS does NOT reject or validate data — that requires SHACL (Chapter 5).")
    print("5. SEMANTICS ARE EXPLICIT: The meaning is in the DEFINITION, not the label string.")
    print("   'sisterCity' could be called 'x7q' — if defined as symmetric, it behaves the same.")

    print("\n--- Thought Questions ---")
    print("★ If two systems define 'partOf' differently (one transitive, one not),")
    print("  can their graphs be merged safely? What must be negotiated first?")
    print("★★ How would you model a relation that is ALMOST symmetric but has exceptions?")
    print("★★★ Design a mechanism to detect conflicting relation definitions across sources.")


if __name__ == "__main__":
    main()
