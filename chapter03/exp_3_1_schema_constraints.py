"""Experiment 3-1: RDFS Entailment vs. Property Graph Schema Constraints.

Question: "How does deductive typing in RDFS differ from prescriptive validation
in Property Graph schemas?"

Demonstrates the fundamental architectural divergence:
  1. RDFS Semantics (Deductive Typing):
     - rdfs:domain and rdfs:range are inference rules, NOT validation checks.
     - Asserting (:MysteryNode, :capitalOf, :Vietnam) infers (:MysteryNode, a, :City).
     - RDFS never rejects data; even mismatched data produces new type entailments.
  2. Property Graph Schema (Prescriptive Validation):
     - LPG schemas define strict validation constraints (required properties,
       allowed labels, target types).
     - Missing properties or invalid target nodes immediately raise validation exceptions.

Semantic contracts: R11-03 (RDF Schema 1.1 §5), RDF-MT-01 (RDF 1.1 Semantics §7),
docs/CHAPTER03_SEMANTIC_CONTRACTS.md §RDFS Semantics.
Difficulty: ★★
Status: ✅ Independently runnable
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from typing import Any

from rdflib import RDF, RDFS, Graph, Namespace, URIRef

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

EX = Namespace("http://example.org/")


# ============================================================================
# 1. RDFS Deductive Typing Engine
# ============================================================================


def run_rdfs_deductive_typing() -> tuple[Graph, set[tuple[str, str, str]]]:
    """Demonstrates how RDFS domain and range declarations infer types deductively."""
    g = Graph()
    g.bind("ex", EX)
    g.bind("rdfs", RDFS)
    g.bind("rdf", RDF)

    # TBox (Schema / Ontology definitions)
    g.add((EX.capitalOf, RDF.type, RDF.Property))
    g.add((EX.capitalOf, RDFS.domain, EX.City))
    g.add((EX.capitalOf, RDFS.range, EX.Country))
    g.add((EX.City, RDFS.subClassOf, EX.GeographicArea))

    # ABox: An untyped node (:MysteryNode) is asserted to be capitalOf Vietnam
    g.add((EX.MysteryNode, EX.capitalOf, EX.Vietnam))

    # Simple forward-chaining RDFS reasoner implementing domain/range/subclass rules:
    # Rule rdfs2: (?p rdfs:domain ?c) & (?x ?p ?y) -> (?x rdf:type ?c)
    # Rule rdfs3: (?p rdfs:range ?c) & (?x ?p ?y) -> (?y rdf:type ?c)
    # Rule rdfs9: (?c1 rdfs:subClassOf ?c2) & (?x rdf:type ?c1) -> (?x rdf:type ?c2)
    inferred: set[tuple[URIRef, URIRef, URIRef]] = set()

    # Apply domain
    for p, _, domain_cls in g.triples((None, RDFS.domain, None)):
        for s, _, _ in g.triples((None, p, None)):
            triple = (s, RDF.type, domain_cls)
            if triple not in g:
                inferred.add(triple)

    # Apply range
    for p, _, range_cls in g.triples((None, RDFS.range, None)):
        for _, _, o in g.triples((None, p, None)):
            if isinstance(o, URIRef):
                triple = (o, RDF.type, range_cls)
                if triple not in g:
                    inferred.add(triple)

    for t in inferred:
        g.add(t)

    # Apply subClassOf closure
    subclass_inferred: set[tuple[URIRef, URIRef, URIRef]] = set()
    for sub, _, sup in g.triples((None, RDFS.subClassOf, None)):
        for inst, _, _ in g.triples((None, RDF.type, sub)):
            triple = (inst, RDF.type, sup)
            if triple not in g:
                subclass_inferred.add(triple)

    for t in subclass_inferred:
        g.add(t)
        inferred.add(t)

    short_inferred = {
        (str(s).split("/")[-1], str(p).split("#")[-1], str(o).split("/")[-1])
        for s, p, o in inferred
    }
    return g, short_inferred


# ============================================================================
# 2. LPG Prescriptive Validation Engine
# ============================================================================


class SchemaViolationError(Exception):
    """Raised when an LPG node or edge violates prescriptive schema constraints."""


@dataclass
class NodeConstraint:
    label: str
    required_properties: set[str]
    property_types: dict[str, type]


@dataclass
class EdgeConstraint:
    rel_type: str
    allowed_source_labels: set[str]
    allowed_target_labels: set[str]
    required_properties: set[str] = None  # type: ignore[assignment]


class LPGPrescriptiveSchema:
    """A prescriptive schema validator for Property Graphs."""

    def __init__(self) -> None:
        self.node_constraints: dict[str, NodeConstraint] = {}
        self.edge_constraints: dict[str, EdgeConstraint] = {}

    def add_node_constraint(
        self,
        label: str,
        required_properties: set[str],
        property_types: dict[str, type],
    ) -> None:
        self.node_constraints[label] = NodeConstraint(
            label=label,
            required_properties=required_properties,
            property_types=property_types,
        )

    def add_edge_constraint(
        self,
        rel_type: str,
        allowed_source_labels: set[str],
        allowed_target_labels: set[str],
        required_properties: set[str] | None = None,
    ) -> None:
        self.edge_constraints[rel_type] = EdgeConstraint(
            rel_type=rel_type,
            allowed_source_labels=allowed_source_labels,
            allowed_target_labels=allowed_target_labels,
            required_properties=required_properties or set(),
        )

    def validate_node(self, node_id: str, labels: set[str], properties: dict[str, Any]) -> None:
        for lbl in labels:
            if lbl in self.node_constraints:
                c = self.node_constraints[lbl]
                missing = c.required_properties - set(properties.keys())
                if missing:
                    raise SchemaViolationError(
                        f"Node '{node_id}' with label '{lbl}' is missing required properties: "
                        f"{sorted(missing)}"
                    )
                for prop_name, expected_type in c.property_types.items():
                    if prop_name in properties and not isinstance(
                        properties[prop_name], expected_type
                    ):
                        actual = type(properties[prop_name]).__name__
                        raise SchemaViolationError(
                            f"Node '{node_id}' property '{prop_name}' expected "
                            f"{expected_type.__name__}, got {actual}"
                        )

    def validate_edge(
        self,
        edge_id: str,
        rel_type: str,
        source_labels: set[str],
        target_labels: set[str],
        properties: dict[str, Any],
    ) -> None:
        if rel_type in self.edge_constraints:
            c = self.edge_constraints[rel_type]
            if not (source_labels & c.allowed_source_labels):
                raise SchemaViolationError(
                    f"Edge '{edge_id}' type '{rel_type}' requires source with label in "
                    f"{sorted(c.allowed_source_labels)}, but source has {sorted(source_labels)}"
                )
            if not (target_labels & c.allowed_target_labels):
                raise SchemaViolationError(
                    f"Edge '{edge_id}' type '{rel_type}' requires target with label in "
                    f"{sorted(c.allowed_target_labels)}, but target has {sorted(target_labels)}"
                )
            missing = c.required_properties - set(properties.keys())
            if missing:
                raise SchemaViolationError(
                    f"Edge '{edge_id}' type '{rel_type}' missing required edge properties: "
                    f"{sorted(missing)}"
                )


def main() -> None:
    print("=" * 60)
    print("EXPERIMENT 3-1: RDFS ENTAILMENT VS. LPG SCHEMA CONSTRAINTS")
    print("=" * 60)

    # 1. RDFS Deductive Typing
    print("\n--- 1. RDFS Deductive Typing (Open-World Inference) ---")
    _, inferred = run_rdfs_deductive_typing()
    print("Asserted: (MysteryNode, capitalOf, Vietnam)")
    print("RDFS Inferred facts without any prior type assertion on MysteryNode:")
    for s, p, o in sorted(inferred):
        print(f"  + ({s}, {p}, {o})")

    # 2. LPG Prescriptive Validation
    print("\n--- 2. LPG Prescriptive Validation (Closed-World Guardrails) ---")
    schema = LPGPrescriptiveSchema()
    schema.add_node_constraint(
        label="City",
        required_properties={"name", "population"},
        property_types={"name": str, "population": int},
    )
    schema.add_edge_constraint(
        rel_type="CAPITAL_OF",
        allowed_source_labels={"City"},
        allowed_target_labels={"Country"},
        required_properties={"since"},
    )

    # Case A: Valid node
    print("Inserting valid city node: 'Hanoi' ...")
    schema.validate_node("Hanoi", {"City"}, {"name": "Hà Nội", "population": 8418883})
    print("  [PASSED] Valid node accepted.")

    # Case B: Invalid node (missing population)
    print("Inserting invalid city node without 'population' ...")
    try:
        schema.validate_node("MysteryNode", {"City"}, {"name": "Unknown"})
        print("  [UNEXPECTED] Node accepted!")
    except SchemaViolationError as e:
        print(f"  [REJECTED] SchemaViolationError caught: {e}")

    # Case C: Invalid edge (source is not a City)
    print("Inserting invalid CAPITAL_OF edge where source is Company ...")
    try:
        schema.validate_edge(
            "e_bad",
            "CAPITAL_OF",
            source_labels={"Company"},
            target_labels={"Country"},
            properties={"since": 2020},
        )
    except SchemaViolationError as e:
        print(f"  [REJECTED] SchemaViolationError caught: {e}")

    print("\n[KEY TAKEAWAY]:")
    print("  - RDFS declarations are GENERATIVE: they deduce missing types.")
    print("  - LPG schemas are VALIDATIVE: they enforce constraints and reject malformed data.")


if __name__ == "__main__":
    main()
