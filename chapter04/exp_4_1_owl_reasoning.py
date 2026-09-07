"""Experiment 4-1: OWL 2 DL Entailment & Subsumption Reasoning.

Demonstrates Description Logic reasoning over the Mechanism Knowledge Graph:
1. TBox Subsumption: RateOfChangeMechanism ⊑ ChangeMechanism ⊑ Mechanism.
2. Property Restrictions & Domain/Range: hasApplication domain Mechanism,
   range MechanismApplication.
3. Deductive Closure vs. Graph Immutability: Entailment is a semantic consequence relation,
   not an in-place mutation of the source RDF graph.

Semantic Contracts:
- Direct Semantics §2.3, §2.5: SubClassOf(C, D) iff C^I ⊆ D^I; O ⊨ α iff all models satisfy α.
- docs/CHAPTER04_SEMANTIC_CONTRACTS.md: SubClassOf (§SubClassOf), Entailment (§Entailment),
  Entailment ≠ Materialization (§Entailment ≠ Materialization).
"""

from __future__ import annotations

import copy
from typing import Any

import owlrl
from rdflib import RDF, RDFS, Graph, Namespace, URIRef
from rdflib.namespace import OWL

# Domain namespace for the Mechanism Knowledge Graph
EX = Namespace("http://example.org/mechanism#")


def build_mechanism_ontology() -> Graph:
    """Build the base asserted Mechanism Knowledge Graph ontology (TBox + ABox).

    TBox Axioms:
      - RateOfChangeMechanism ⊑ ChangeMechanism
      - ChangeMechanism ⊑ Mechanism
      - DerivativeApplication ⊑ MechanismApplication
      - hasApplication: domain Mechanism, range MechanismApplication
      - appliesOperation: domain MechanismApplication, range Operation

    ABox Assertions:
      - rateOfChange_1 a RateOfChangeMechanism
      - rateOfChange_1 hasApplication derivApp_1
      - derivApp_1 a DerivativeApplication
    """
    g = Graph()
    g.bind("ex", EX)
    g.bind("owl", OWL)
    g.bind("rdfs", RDFS)

    # --- TBox: Class Declarations & Subsumption ---
    g.add((EX.Mechanism, RDF.type, OWL.Class))
    g.add((EX.ChangeMechanism, RDF.type, OWL.Class))
    g.add((EX.RateOfChangeMechanism, RDF.type, OWL.Class))
    g.add((EX.MechanismApplication, RDF.type, OWL.Class))
    g.add((EX.DerivativeApplication, RDF.type, OWL.Class))
    g.add((EX.Operation, RDF.type, OWL.Class))
    g.add((EX.DerivativeOperation, RDF.type, OWL.Class))

    # Subsumption hierarchy: RateOfChangeMechanism ⊑ ChangeMechanism ⊑ Mechanism
    g.add((EX.ChangeMechanism, RDFS.subClassOf, EX.Mechanism))
    g.add((EX.RateOfChangeMechanism, RDFS.subClassOf, EX.ChangeMechanism))
    g.add((EX.DerivativeApplication, RDFS.subClassOf, EX.MechanismApplication))
    g.add((EX.DerivativeOperation, RDFS.subClassOf, EX.Operation))

    # --- TBox: Object Property Declarations & Domain/Range ---
    g.add((EX.hasApplication, RDF.type, OWL.ObjectProperty))
    g.add((EX.hasApplication, RDFS.domain, EX.Mechanism))
    g.add((EX.hasApplication, RDFS.range, EX.MechanismApplication))

    g.add((EX.appliesOperation, RDF.type, OWL.ObjectProperty))
    g.add((EX.appliesOperation, RDFS.domain, EX.MechanismApplication))
    g.add((EX.appliesOperation, RDFS.range, EX.Operation))

    # --- ABox: Assertional Individuals ---
    g.add((EX.rateOfChange_1, RDF.type, EX.RateOfChangeMechanism))
    g.add((EX.rateOfChange_1, EX.hasApplication, EX.derivApp_1))
    g.add((EX.derivApp_1, RDF.type, EX.DerivativeApplication))
    g.add((EX.derivApp_1, EX.appliesOperation, EX.derivOp_1))
    g.add((EX.derivOp_1, RDF.type, EX.DerivativeOperation))

    return g


def compute_deductive_closure(
    asserted_graph: Graph,
) -> tuple[Graph, set[tuple[str, str, str]]]:
    """Compute the OWL RL deductive closure without mutating the input graph.

    Adheres to Semantic Contract: 'Entailment ≠ Materialization'.
    The asserted graph remains immutable; reasoning produces an expanded closure graph.

    Returns:
        tuple[Graph, set[tuple[str, str, str]]]: (closure_graph, newly_entailed_triples)
    """
    closure_graph = copy.deepcopy(asserted_graph)
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(closure_graph)

    # Identify triples present in closure but absent in the asserted graph
    asserted_triples = set(asserted_graph)
    newly_entailed_raw = set(closure_graph) - asserted_triples

    # Format triples as simplified string tuples for inspection
    newly_entailed = {(str(s), str(p), str(o)) for (s, p, o) in newly_entailed_raw}

    return closure_graph, newly_entailed


def query_individual_types(graph: Graph, individual: URIRef) -> set[URIRef]:
    """Retrieve all asserted or inferred types of an individual."""
    return set(graph.objects(individual, RDF.type))


def verify_entailment_contracts(asserted: Graph, closure: Graph) -> dict[str, Any]:
    """Verify core semantic entailment contracts on Mechanism Knowledge Graph."""
    # 1. 2-hop subsumption: rateOfChange_1 is indirectly a Mechanism
    # RateOfChangeMechanism ⊑ ChangeMechanism ⊑ Mechanism
    roc_types_asserted = query_individual_types(asserted, EX.rateOfChange_1)
    roc_types_closure = query_individual_types(closure, EX.rateOfChange_1)

    has_direct_asserted = EX.RateOfChangeMechanism in roc_types_asserted
    has_implicit_subsumption_1 = EX.ChangeMechanism in roc_types_closure
    has_implicit_subsumption_2 = EX.Mechanism in roc_types_closure

    # 2. TBox transitive subsumption: RateOfChangeMechanism ⊑ Mechanism
    subclass_entailed = (
        EX.RateOfChangeMechanism,
        RDFS.subClassOf,
        EX.Mechanism,
    ) in closure

    # 3. Domain & Range typing verification
    deriv_types_closure = query_individual_types(closure, EX.derivApp_1)
    has_range_typing = EX.MechanismApplication in deriv_types_closure

    # 4. Source immutability check
    source_triple_count = len(asserted)
    closure_triple_count = len(closure)
    immutability_preserved = (
        source_triple_count < closure_triple_count and EX.Mechanism not in roc_types_asserted
    )

    return {
        "direct_type_asserted": has_direct_asserted,
        "subsumption_hop1_inferred": has_implicit_subsumption_1,
        "subsumption_hop2_inferred": has_implicit_subsumption_2,
        "tbox_transitivity_inferred": subclass_entailed,
        "range_typing_inferred": has_range_typing,
        "immutability_preserved": immutability_preserved,
        "asserted_triple_count": source_triple_count,
        "closure_triple_count": closure_triple_count,
    }


def main() -> None:
    """Execute Experiment 4-1 demonstration."""
    print("=" * 70)
    print("EXP-4-1: OWL 2 DL Entailment & Subsumption Reasoning (Mechanism KG)")
    print("=" * 70)

    asserted = build_mechanism_ontology()
    print(f"Asserted Graph Triples: {len(asserted)}")

    closure, entailed = compute_deductive_closure(asserted)
    print(f"Deductive Closure Triples: {len(closure)} (+{len(entailed)} inferred)")

    results = verify_entailment_contracts(asserted, closure)
    print("\n--- Semantic Contract Verification ---")
    for key, val in results.items():
        print(f"  {key}: {val}")

    print("\nSample Inferred Triples on ex:rateOfChange_1:")
    for t in sorted(query_individual_types(closure, EX.rateOfChange_1)):
        status = (
            "(Asserted)"
            if t in query_individual_types(asserted, EX.rateOfChange_1)
            else "(Inferred)"
        )
        print(f"  rdf:type -> {t} {status}")


if __name__ == "__main__":
    main()
