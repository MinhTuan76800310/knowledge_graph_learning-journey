"""Direct semantic tests for Chapter 4 experiments.

Tests assert:
  - Exp 4-1: Description Logic subsumption, existential restrictions,
    and deductive closure immutability.
  - Exp 4-2: DL-Lite backward-chaining query rewriting (OBDA), AC^0 data complexity,
    and SQL UCQ equivalence with RDF materialization.
  - Exp 4-3: Open World Assumption (OWA) tri-state logic, disjointness clash detection,
    and class satisfiability vs. ontology consistency.

Semantic Contracts:
  - W3C OWL 2 Direct Semantics §2.2, §2.3, §2.4, §2.5
  - Calvanese et al. (2007) DL-Lite / FO-rewritability
  - docs/CHAPTER04_SEMANTIC_CONTRACTS.md
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

rdflib = pytest.importorskip("rdflib")
owlrl = pytest.importorskip("owlrl")

CHAPTER04_DIR = Path(__file__).parent
if str(CHAPTER04_DIR) not in sys.path:
    sys.path.insert(0, str(CHAPTER04_DIR))


# ---------------------------------------------------------------------------
# Experiment 4-1: OWL 2 DL Entailment & Subsumption Reasoning
# ---------------------------------------------------------------------------


class TestExp41OwlReasoning:
    """Semantic tests for exp_4_1_owl_reasoning.py."""

    def test_subsumption_transitive_closure(self) -> None:
        from exp_4_1_owl_reasoning import (
            EX,
            build_mechanism_ontology,
            compute_deductive_closure,
            query_individual_types,
        )

        asserted = build_mechanism_ontology()
        closure, _ = compute_deductive_closure(asserted)

        inferred_types = query_individual_types(closure, EX.rateOfChange_1)

        # 1-hop subsumption: RateOfChangeMechanism ⊑ ChangeMechanism
        assert EX.ChangeMechanism in inferred_types
        # 2-hop subsumption: ChangeMechanism ⊑ Mechanism
        assert EX.Mechanism in inferred_types
        # Direct asserted type
        assert EX.RateOfChangeMechanism in inferred_types

    def test_tbox_subclass_transitivity(self) -> None:
        from exp_4_1_owl_reasoning import EX, build_mechanism_ontology, compute_deductive_closure
        from rdflib import RDFS

        asserted = build_mechanism_ontology()
        closure, _ = compute_deductive_closure(asserted)

        assert (EX.RateOfChangeMechanism, RDFS.subClassOf, EX.Mechanism) in closure

    def test_domain_and_range_typing(self) -> None:
        from exp_4_1_owl_reasoning import (
            EX,
            build_mechanism_ontology,
            compute_deductive_closure,
            query_individual_types,
        )

        asserted = build_mechanism_ontology()
        closure, _ = compute_deductive_closure(asserted)

        deriv_types = query_individual_types(closure, EX.derivApp_1)
        assert EX.MechanismApplication in deriv_types

    def test_entailment_preserves_source_graph_immutability(self) -> None:
        """Adheres to Contract: 'Entailment ≠ Materialization'.

        Entailment is a semantic relation; computing closure does not mutate source graph.
        """
        from exp_4_1_owl_reasoning import (
            EX,
            build_mechanism_ontology,
            compute_deductive_closure,
            query_individual_types,
        )

        asserted = build_mechanism_ontology()
        initial_triple_count = len(asserted)

        closure, _ = compute_deductive_closure(asserted)

        assert len(asserted) == initial_triple_count
        assert len(closure) > initial_triple_count
        # Asserted graph does not contain inferred triple
        assert EX.Mechanism not in query_individual_types(asserted, EX.rateOfChange_1)


# ---------------------------------------------------------------------------
# Experiment 4-2: DL-Lite & First-Order Query Rewriting to SQL
# ---------------------------------------------------------------------------


class TestExp42DLLiteQueryRewriting:
    """Semantic tests for exp_4_2_dl_lite_query_rewriting.py."""

    def test_ucq_expansion_backward_chaining(self) -> None:
        from exp_4_2_dl_lite_query_rewriting import DLLiteQueryRewriter

        rewriter = DLLiteQueryRewriter()
        rewriter.add_subclass_axiom("RateOfChangeMechanism", "ChangeMechanism")
        rewriter.add_subclass_axiom("ChangeMechanism", "Mechanism")
        rewriter.add_subclass_axiom("AggregationMechanism", "Mechanism")
        rewriter.add_role_domain_axiom("hasSubPart", "Mechanism")

        atoms = rewriter.rewrite_concept_query("Mechanism")

        expected_atoms = {
            "Mechanism",
            "ChangeMechanism",
            "RateOfChangeMechanism",
            "AggregationMechanism",
            "exists_hasSubPart",
        }
        assert set(atoms) == expected_atoms

    def test_naive_sql_misses_subclasses_while_ucq_captures_all(self) -> None:
        from exp_4_2_dl_lite_query_rewriting import run_experiment

        res = run_experiment()

        # Naive query misses 4 out of 5 mechanisms
        assert res["naive_count"] == 1
        assert res["rewritten_count"] == 5
        assert res["naive_has_false_negatives"] is True
        assert res["naive_missed_ids"] == ["mech_01", "mech_02", "mech_03", "mech_04"]

    def test_exact_semantic_equivalence_with_materialized_rdf(self) -> None:
        """Asserts that DL-Lite FO-rewritten SQL yields 100% identical answers
        to RDF materialization.
        """
        from exp_4_2_dl_lite_query_rewriting import run_experiment

        res = run_experiment()
        assert res["is_equivalent_to_materialization"] is True

    def test_zero_in_place_db_materialization(self) -> None:
        from exp_4_2_dl_lite_query_rewriting import SQLiteMechanismStore

        db = SQLiteMechanismStore()
        db.initialize_schema_and_data()

        cur = db.connection.cursor()
        cur.execute("SELECT COUNT(*) FROM mechanisms;")
        base_count_before = cur.fetchone()[0]

        # Execute rewritten query
        cur.execute("""
            SELECT id FROM mechanisms
            UNION
            SELECT id FROM rate_of_change_mechanisms
        """)
        results = cur.fetchall()
        assert len(results) == 3

        # Base table must remain unchanged
        cur.execute("SELECT COUNT(*) FROM mechanisms;")
        base_count_after = cur.fetchone()[0]
        assert base_count_before == base_count_after == 1


# ---------------------------------------------------------------------------
# Experiment 4-3: Open World Assumption (OWA) vs. Inconsistency Detection
# ---------------------------------------------------------------------------


class TestExp43OWAAndInconsistency:
    """Semantic tests for exp_4_3_owa_and_inconsistency.py."""

    def test_owa_tri_state_behavior(self) -> None:
        from exp_4_3_owa_and_inconsistency import (
            EX,
            OWAInconsistencyInspector,
            TriState,
        )
        from rdflib import Graph
        from rdflib.namespace import OWL

        g = Graph()
        g.add((EX.ReversibleMechanism, OWL.disjointWith, EX.DissipativeMechanism))
        g.add((EX.mech_rev, rdflib.RDF.type, EX.ReversibleMechanism))
        g.add((EX.mech_unknown, rdflib.RDF.type, EX.CatalyticMechanism))

        inspector = OWAInconsistencyInspector(g)

        # 1. Asserted fact -> ENTAILED
        assert (
            inspector.query_membership_owa(EX.mech_rev, EX.ReversibleMechanism) == TriState.ENTAILED
        )

        # 2. Fact contradictory to disjointness -> REFUTED
        assert (
            inspector.query_membership_owa(EX.mech_rev, EX.DissipativeMechanism) == TriState.REFUTED
        )

        # 3. Missing fact with no refutation -> UNKNOWN (absence != false)
        assert (
            inspector.query_membership_owa(EX.mech_unknown, EX.DissipativeMechanism)
            == TriState.UNKNOWN
        )

    def test_cwa_binary_negation_contrast(self) -> None:
        """CWA treats missing knowledge as False, whereas OWA treats it as UNKNOWN."""
        from exp_4_3_owa_and_inconsistency import EX, OWAInconsistencyInspector, TriState
        from rdflib import Graph

        g = Graph()
        g.add((EX.mech_unknown, rdflib.RDF.type, EX.CatalyticMechanism))
        inspector = OWAInconsistencyInspector(g)

        # CWA gives False
        cwa_result = inspector.query_membership_cwa(EX.mech_unknown, EX.DissipativeMechanism)
        assert cwa_result is False

        # OWA gives UNKNOWN
        owa_result = inspector.query_membership_owa(EX.mech_unknown, EX.DissipativeMechanism)
        assert owa_result == TriState.UNKNOWN

    def test_disjointness_causes_inconsistency_when_instantiated(self) -> None:
        """Asserting an individual into two disjoint classes makes Models(O) = ∅."""
        from exp_4_3_owa_and_inconsistency import (
            EX,
            OntologyInconsistencyError,
            OWAInconsistencyInspector,
        )
        from rdflib import Graph
        from rdflib.namespace import OWL

        g = Graph()
        g.add((EX.ReversibleMechanism, OWL.disjointWith, EX.DissipativeMechanism))
        g.add((EX.bad_individual, rdflib.RDF.type, EX.ReversibleMechanism))
        g.add((EX.bad_individual, rdflib.RDF.type, EX.DissipativeMechanism))

        inspector = OWAInconsistencyInspector(g)
        is_consistent, msg = inspector.check_ontology_consistency()

        assert is_consistent is False
        assert msg is not None
        assert "Inconsistency detected" in msg

        with pytest.raises(OntologyInconsistencyError):
            inspector.validate_or_raise()

    def test_unsatisfiable_class_does_not_make_ontology_inconsistent_if_uninstantiated(
        self,
    ) -> None:
        """Adheres to Contract: 'Class Satisfiability' (§Class Satisfiability).

        An unsatisfiable class (C ⊑ ⊥) does NOT make the ontology inconsistent
        as long as no individual belongs to it.
        """
        from exp_4_3_owa_and_inconsistency import EX, OWAInconsistencyInspector
        from rdflib import Graph
        from rdflib.namespace import OWL, RDFS

        g = Graph()
        g.add((EX.ReversibleMechanism, OWL.disjointWith, EX.DissipativeMechanism))

        # PerpetualHarmonicDissipator is unsatisfiable
        g.add((EX.PerpetualHarmonicDissipator, rdflib.RDF.type, OWL.Class))
        g.add((EX.PerpetualHarmonicDissipator, RDFS.subClassOf, EX.ReversibleMechanism))
        g.add((EX.PerpetualHarmonicDissipator, RDFS.subClassOf, EX.DissipativeMechanism))

        inspector = OWAInconsistencyInspector(g)

        # 1. Class is unsatisfiable
        assert inspector.is_class_satisfiable(EX.PerpetualHarmonicDissipator) is False

        # 2. BUT ontology is STILL consistent!
        is_consistent, _ = inspector.check_ontology_consistency()
        assert is_consistent is True

    def test_instantiating_unsatisfiable_class_triggers_inconsistency(self) -> None:
        from exp_4_3_owa_and_inconsistency import (
            EX,
            OntologyInconsistencyError,
            OWAInconsistencyInspector,
        )
        from rdflib import Graph
        from rdflib.namespace import OWL, RDFS

        g = Graph()
        g.add((EX.ReversibleMechanism, OWL.disjointWith, EX.DissipativeMechanism))
        g.add((EX.PerpetualHarmonicDissipator, RDFS.subClassOf, EX.ReversibleMechanism))
        g.add((EX.PerpetualHarmonicDissipator, RDFS.subClassOf, EX.DissipativeMechanism))

        # Instantiating the unsatisfiable class
        g.add((EX.impossible_machine, rdflib.RDF.type, EX.PerpetualHarmonicDissipator))

        inspector = OWAInconsistencyInspector(g)
        is_consistent, _ = inspector.check_ontology_consistency()
        assert is_consistent is False

        with pytest.raises(OntologyInconsistencyError):
            inspector.validate_or_raise()
