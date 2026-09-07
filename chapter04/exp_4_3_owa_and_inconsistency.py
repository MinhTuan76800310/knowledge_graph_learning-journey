"""Experiment 4-3: Open World Assumption (OWA) vs. Disjointness Inconsistency.

Demonstrates core model-theoretic and epistemological concepts in OWL 2:
1. OWA Tri-State Entailment vs. CWA Binary Negation:
   - ENTAILED: True in all models (O ⊨ α).
   - REFUTED: False in all models (O ⊨ ¬α).
   - UNKNOWN: True in some models, False in others (absence ≠ negation).
   - Distinction from SQL NULL (relational missing value ≠ model-theoretic open world).
2. DisjointClasses & Consistency:
   - DisjointClasses(C, D) entails C^I ∩ D^I = ∅.
   - Asserting x ∈ C and x ∈ D yields Models(O) = ∅ (Ontology Inconsistency).
   - Ex Falso Quodlibet: in an inconsistent ontology, all propositions are vacuously entailed.
3. Class Satisfiability vs. Ontology Consistency:
   - An unsatisfiable class (C ⊑ ⊥) does NOT make the ontology inconsistent
     as long as no individual is asserted to belong to C.

Manuscript Line Anchors:
- book/chapter04.md:650-820, 1725-1726
Semantic Contracts:
- docs/CHAPTER04_SEMANTIC_CONTRACTS.md: Open World Assumption (§OWA),
  DisjointClasses (§DisjointClasses), Consistency (§Consistency),
  Class Satisfiability (§Class Satisfiability), Three Entailment States (§Three Entailment States).
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any

from rdflib import RDF, RDFS, Graph, Namespace, URIRef
from rdflib.namespace import OWL

EX = Namespace("http://example.org/mechanism#")


class TriState(Enum):
    """Tri-state valuation under Open World Assumption (OWA)."""

    ENTAILED = "ENTAILED"  # True in all models: O ⊨ α
    REFUTED = "REFUTED"  # False in all models: O ⊨ ¬α
    UNKNOWN = "UNKNOWN"  # True in some models, False in others


class OntologyInconsistencyError(Exception):
    """Raised when an ontology has no models (Models(O) = ∅)."""

    def __init__(self, message: str, conflicting_axiom: str | None = None) -> None:
        super().__init__(message)
        self.conflicting_axiom = conflicting_axiom


@dataclass
class OWAInconsistencyInspector:
    """Evaluates tri-state OWA queries, checks class satisfiability, and detects inconsistency."""

    graph: Graph

    def __post_init__(self) -> None:
        self.disjoint_pairs: set[frozenset[URIRef]] = set()
        self._load_disjoint_axioms()

    def _load_disjoint_axioms(self) -> None:
        """Extract explicit and symmetric owl:disjointWith axioms."""
        for c1, _, c2 in self.graph.triples((None, OWL.disjointWith, None)):
            if isinstance(c1, URIRef) and isinstance(c2, URIRef):
                self.disjoint_pairs.add(frozenset([c1, c2]))

    def get_individual_types(self, individual: URIRef) -> set[URIRef]:
        """Compute all asserted and subsumed types for an individual."""
        types = set(self.graph.objects(individual, RDF.type))
        # Expand via rdfs:subClassOf
        expanded = set(types)
        frontier = list(types)
        while frontier:
            current = frontier.pop(0)
            for super_cls in self.graph.objects(current, RDFS.subClassOf):
                if isinstance(super_cls, URIRef) and super_cls not in expanded:
                    expanded.add(super_cls)
                    frontier.append(super_cls)
        return expanded

    def check_ontology_consistency(self) -> tuple[bool, str | None]:
        """Verify if Models(O) ≠ ∅ under disjointness axioms.

        Returns:
            (is_consistent, error_message_if_any)
        """
        # Find all individuals
        individuals = set(self.graph.subjects(RDF.type, None))

        for ind in individuals:
            types = self.get_individual_types(ind)
            for c1, c2 in [tuple(p) for p in self.disjoint_pairs]:
                if c1 in types and c2 in types:
                    err = (
                        f"Inconsistency detected! Individual <{ind}> belongs to disjoint classes "
                        f"<{c1}> and <{c2}>. "
                        "Their intersection is empty (C intersection D == bottom)."
                    )
                    return False, err

        return True, None

    def validate_or_raise(self) -> None:
        """Raise OntologyInconsistencyError if the ontology has no models."""
        is_consistent, err = self.check_ontology_consistency()
        if not is_consistent:
            raise OntologyInconsistencyError(err or "Ontology is inconsistent")

    def is_class_satisfiable(self, cls: URIRef) -> bool:
        """Check if class extension can be non-empty in at least one model (C^I ≠ ∅).

        A class is unsatisfiable if it is a subclass of two disjoint classes.
        Note: An unsatisfiable class does NOT make the ontology inconsistent
        as long as no individual is an instance of it.
        """
        super_classes = set()
        frontier = [cls]
        while frontier:
            curr = frontier.pop(0)
            for s in self.graph.objects(curr, RDFS.subClassOf):
                if isinstance(s, URIRef) and s not in super_classes:
                    super_classes.add(s)
                    frontier.append(s)

        # Check if any disjoint pair is contained within superclasses
        for c1, c2 in [tuple(p) for p in self.disjoint_pairs]:
            if c1 in super_classes and c2 in super_classes:
                return False
        return True

    def query_membership_owa(self, individual: URIRef, target_class: URIRef) -> TriState:
        """Evaluate class membership under Open World Assumption.

        Precondition: Ontology must be consistent.
        """
        self.validate_or_raise()

        types = self.get_individual_types(individual)
        if target_class in types:
            return TriState.ENTAILED

        # Check if individual has a type disjoint with target_class
        for t in types:
            if frozenset([t, target_class]) in self.disjoint_pairs:
                return TriState.REFUTED

        # If neither entailed nor refuted, OWA valuation is UNKNOWN
        return TriState.UNKNOWN

    def query_membership_cwa(self, individual: URIRef, target_class: URIRef) -> bool:
        """Evaluate class membership under Closed World Assumption (relational baseline)."""
        types = self.get_individual_types(individual)
        return target_class in types


def run_experiment() -> dict[str, Any]:
    """Execute Experiment 4-3 and return results."""
    # -----------------------------------------------------------------------
    # Part 1: Consistent Ontology with OWA Tri-State Evaluation
    # -----------------------------------------------------------------------
    g_consistent = Graph()
    g_consistent.bind("ex", EX)
    g_consistent.bind("owl", OWL)
    g_consistent.bind("rdfs", RDFS)

    # Classes: ReversibleMechanism, DissipativeMechanism, CatalyticMechanism
    g_consistent.add((EX.ReversibleMechanism, RDF.type, OWL.Class))
    g_consistent.add((EX.DissipativeMechanism, RDF.type, OWL.Class))
    g_consistent.add((EX.CatalyticMechanism, RDF.type, OWL.Class))

    # Disjointness Axiom: ReversibleMechanism ⊓ DissipativeMechanism ≡ ⊥
    g_consistent.add((EX.ReversibleMechanism, OWL.disjointWith, EX.DissipativeMechanism))

    # ABox Individuals:
    # 1. harmonic_oscillator is a ReversibleMechanism
    g_consistent.add((EX.harmonic_oscillator, RDF.type, EX.ReversibleMechanism))
    # 2. enzyme_catalyst is a CatalyticMechanism (no statement about reversibility)
    g_consistent.add((EX.enzyme_catalyst, RDF.type, EX.CatalyticMechanism))

    inspector_1 = OWAInconsistencyInspector(g_consistent)

    # Q1: Is harmonic_oscillator a ReversibleMechanism?
    q1_owa = inspector_1.query_membership_owa(EX.harmonic_oscillator, EX.ReversibleMechanism)
    q1_cwa = inspector_1.query_membership_cwa(EX.harmonic_oscillator, EX.ReversibleMechanism)

    # Q2: Is harmonic_oscillator a DissipativeMechanism?
    # OWA: REFUTED (due to disjointness). CWA: False.
    q2_owa = inspector_1.query_membership_owa(EX.harmonic_oscillator, EX.DissipativeMechanism)
    q2_cwa = inspector_1.query_membership_cwa(EX.harmonic_oscillator, EX.DissipativeMechanism)

    # Q3: Is enzyme_catalyst a DissipativeMechanism?
    # OWA: UNKNOWN (absence ≠ negation). CWA: False (missing tuple = False).
    q3_owa = inspector_1.query_membership_owa(EX.enzyme_catalyst, EX.DissipativeMechanism)
    q3_cwa = inspector_1.query_membership_cwa(EX.enzyme_catalyst, EX.DissipativeMechanism)

    # -----------------------------------------------------------------------
    # Part 2: Unsatisfiable Class vs. Ontology Consistency
    # -----------------------------------------------------------------------
    # Define class PerpetualDissipator ⊑ ReversibleMechanism ⊓ DissipativeMechanism
    g_consistent.add((EX.PerpetualDissipator, RDF.type, OWL.Class))
    g_consistent.add((EX.PerpetualDissipator, RDFS.subClassOf, EX.ReversibleMechanism))
    g_consistent.add((EX.PerpetualDissipator, RDFS.subClassOf, EX.DissipativeMechanism))

    inspector_unsat = OWAInconsistencyInspector(g_consistent)
    is_perp_satisfiable = inspector_unsat.is_class_satisfiable(EX.PerpetualDissipator)
    is_ontology_still_consistent, _ = inspector_unsat.check_ontology_consistency()

    # -----------------------------------------------------------------------
    # Part 3: Contradiction & Inconsistency Detection
    # -----------------------------------------------------------------------
    g_inconsistent = Graph()
    g_inconsistent.add((EX.ReversibleMechanism, OWL.disjointWith, EX.DissipativeMechanism))
    # Add individual asserted to both disjoint classes
    g_inconsistent.add((EX.contradictory_oscillator, RDF.type, EX.ReversibleMechanism))
    g_inconsistent.add((EX.contradictory_oscillator, RDF.type, EX.DissipativeMechanism))

    inspector_inconsistent = OWAInconsistencyInspector(g_inconsistent)
    inconsistent_status, inconsistency_msg = inspector_inconsistent.check_ontology_consistency()

    inconsistency_raised = False
    try:
        inspector_inconsistent.validate_or_raise()
    except OntologyInconsistencyError:
        inconsistency_raised = True

    return {
        "q1_owa": q1_owa.value,
        "q1_cwa": q1_cwa,
        "q2_owa": q2_owa.value,
        "q2_cwa": q2_cwa,
        "q3_owa": q3_owa.value,
        "q3_cwa": q3_cwa,
        "class_perpetual_dissipator_satisfiable": is_perp_satisfiable,
        "ontology_with_unsatisfiable_class_consistent": is_ontology_still_consistent,
        "inconsistent_ontology_status": inconsistent_status,
        "inconsistent_message": inconsistency_msg,
        "inconsistency_error_raised": inconsistency_raised,
    }


def main() -> None:
    """Execute Experiment 4-3 demonstration."""
    print("=" * 70)
    print("EXP-4-3: Open World Assumption (OWA) vs. Inconsistency Detection")
    print("=" * 70)

    res = run_experiment()

    print("\n--- Section 1: OWA Tri-State Valuation vs. CWA Binary Evaluation ---")
    print(
        f"Q1 (harmonic_oscillator in Reversible):    OWA = {res['q1_owa']} | CWA = {res['q1_cwa']}"
    )
    print(
        f"Q2 (harmonic_oscillator in Dissipative):   OWA = {res['q2_owa']}  | CWA = {res['q2_cwa']}"
    )
    print(
        f"Q3 (enzyme_catalyst in Dissipative):       OWA = {res['q3_owa']}  | CWA = {res['q3_cwa']}"
    )
    print(
        "  -> Critical Insight: In Q3, CWA asserts False; "
        "OWA correctly yields UNKNOWN (absence != negation)."
    )

    print("\n--- Section 2: Class Satisfiability vs. Ontology Consistency ---")
    perp_sat = res["class_perpetual_dissipator_satisfiable"]
    print(f"Is 'PerpetualDissipator' Satisfiable?           {perp_sat} (extension == empty set)")
    ont_cons = res["ontology_with_unsatisfiable_class_consistent"]
    print(f"Is Ontology with Unsatisfiable Class Consistent?{ont_cons} (Models(O) != empty set)")

    print("\n--- Section 3: Disjointness Clash & Inconsistency Detection ---")
    print(f"Consistent Status for Contradictory Graph:     {res['inconsistent_ontology_status']}")
    print(f"OntologyInconsistencyError Raised:             {res['inconsistency_error_raised']}")
    print(f"Diagnostic Error:\n  {res['inconsistent_message']}")


if __name__ == "__main__":
    main()
