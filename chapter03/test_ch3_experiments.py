"""Direct semantic tests for Chapter 3 experiments.

Tests assert:
  - Exp 3-1: RDFS deductive typing (domain/range/subclass) vs. LPG prescriptive validation.
  - Exp 3-2: owl:sameAs equivalence closure, property unification, and No-UNA collapse.
  - Exp 3-3: Named Graphs & TriG dataset isolation across temporal contexts.
  - Exp 3-4: N-ary relations: Qualified Relation vs. RDF Reification semantic equivalence.
  - Exp 3-5: Contextual measurement coexistence in the Mechanism domain.
  - Exp 3-6: Deterministic Entity Resolution pipeline with IFP and 3-zone classification.

Semantic contracts: R11-03, RDF-MT-01, OWL-01, OWL-02, R11-02, SP11-02, NARY-01.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

rdflib = pytest.importorskip("rdflib")

CHAPTER03_DIR = Path(__file__).parent
if str(CHAPTER03_DIR) not in sys.path:
    sys.path.insert(0, str(CHAPTER03_DIR))


# ---------------------------------------------------------------------------
# Experiment 3-1: RDFS Entailment vs. Property Graph Schema Constraints
# ---------------------------------------------------------------------------


class TestExp31SchemaConstraints:
    """Semantic tests for exp_3_1_schema_constraints.py."""

    def test_rdfs_domain_range_deductive_typing(self) -> None:
        from exp_3_1_schema_constraints import run_rdfs_deductive_typing

        _, inferred = run_rdfs_deductive_typing()
        assert ("MysteryNode", "type", "City") in inferred
        assert ("MysteryNode", "type", "GeographicArea") in inferred
        assert ("Vietnam", "type", "Country") in inferred

    def test_lpg_schema_validation_accepts_valid_node(self) -> None:
        from exp_3_1_schema_constraints import LPGPrescriptiveSchema

        schema = LPGPrescriptiveSchema()
        schema.add_node_constraint(
            label="City",
            required_properties={"name", "population"},
            property_types={"name": str, "population": int},
        )
        # Should not raise
        schema.validate_node("Hanoi", {"City"}, {"name": "Hà Nội", "population": 8418883})

    def test_lpg_schema_validation_rejects_missing_property(self) -> None:
        from exp_3_1_schema_constraints import LPGPrescriptiveSchema, SchemaViolationError

        schema = LPGPrescriptiveSchema()
        schema.add_node_constraint(
            label="City",
            required_properties={"name", "population"},
            property_types={"name": str, "population": int},
        )
        with pytest.raises(SchemaViolationError, match="missing required properties"):
            schema.validate_node("MysteryNode", {"City"}, {"name": "Unknown"})

    def test_lpg_schema_validation_rejects_invalid_edge_endpoints(self) -> None:
        from exp_3_1_schema_constraints import LPGPrescriptiveSchema, SchemaViolationError

        schema = LPGPrescriptiveSchema()
        schema.add_edge_constraint(
            rel_type="CAPITAL_OF",
            allowed_source_labels={"City"},
            allowed_target_labels={"Country"},
        )
        with pytest.raises(SchemaViolationError, match="requires source with label in"):
            schema.validate_edge(
                "e_bad",
                "CAPITAL_OF",
                source_labels={"Company"},
                target_labels={"Country"},
                properties={},
            )


# ---------------------------------------------------------------------------
# Experiment 3-2: Entity Identity & owl:sameAs Information Merging
# ---------------------------------------------------------------------------


class TestExp32EntityIdentity:
    """Semantic tests for exp_3_2_entity_identity.py."""

    def test_same_as_closure_unifies_properties(self) -> None:
        from exp_3_2_entity_identity import (
            EX,
            WD,
            SameAsClosureEngine,
            build_federated_identity_graph,
        )
        from rdflib import OWL

        g = build_federated_identity_graph()
        g.add((EX.Hanoi, OWL.sameAs, WD.Q1858))

        engine = SameAsClosureEngine(g)
        props = engine.get_unified_properties(EX.Hanoi)

        # Assert local facts present
        assert "8053663" in props["population"]
        assert "Hanoi" in props["label"]
        assert "http://example.org/Vietnam" in props["capitalOf"]

        # Assert external Wikidata facts transferred via sameAs
        assert "8246540" in props["P1082"]
        assert "Hà Nội" in props["label"]
        assert "16" in props["elevationAboveSeaLevel"]

    def test_no_una_catastrophic_merge_collapse(self) -> None:
        from exp_3_2_entity_identity import (
            EX,
            SameAsClosureEngine,
            build_federated_identity_graph,
        )
        from rdflib import OWL

        g = build_federated_identity_graph()
        # Erroneous linkage
        g.add((EX.DaNang, OWL.sameAs, EX.Hanoi))

        engine = SameAsClosureEngine(g)
        props = engine.get_unified_properties(EX.DaNang)

        # Both populations and features collapse into the same entity
        assert "8053663" in props["population"]
        assert "1220190" in props["population"]
        assert "Dragon Bridge" in props["famousBridge"]
        assert "http://example.org/Vietnam" in props["capitalOf"]


# ---------------------------------------------------------------------------
# Experiment 3-3: Named Graphs & TriG Quad Datasets
# ---------------------------------------------------------------------------


class TestExp33NamedGraphs:
    """Semantic tests for exp_3_3_named_graphs.py."""

    def test_quad_dataset_contains_multiple_contexts(self) -> None:
        from exp_3_3_named_graphs import load_quad_dataset

        ds = load_quad_dataset()
        graphs = list(ds.graphs())
        assert len(graphs) >= 2

    def test_isolated_contexts_no_collision(self) -> None:
        from exp_3_3_named_graphs import EX, load_quad_dataset, query_specific_graph

        ds = load_quad_dataset()
        res_2019 = query_specific_graph(ds, str(EX.graph_census_2019))
        res_2023 = query_specific_graph(ds, str(EX.graph_census_2023))

        assert len(res_2019) == 1
        assert res_2019[0]["population"] == 8053663
        assert res_2019[0]["year"] == 2019

        assert len(res_2023) == 1
        assert res_2023[0]["population"] == 8418883
        assert res_2023[0]["year"] == 2023

    def test_query_all_contexts(self) -> None:
        from exp_3_3_named_graphs import load_quad_dataset, query_all_contexts

        ds = load_quad_dataset()
        all_res = query_all_contexts(ds)
        assert len(all_res) == 2
        years = {r["year"] for r in all_res}
        assert years == {2019, 2023}


# ---------------------------------------------------------------------------
# Experiment 3-4: N-ary Relations & Reification Patterns
# ---------------------------------------------------------------------------


class TestExp34NaryReification:
    """Semantic tests for exp_3_4_nary_reification.py."""

    def test_qualified_relation_pattern1(self) -> None:
        from exp_3_4_nary_reification import (
            build_pattern1_qualified_relation,
            query_qualified_relation,
        )

        g1 = build_pattern1_qualified_relation()
        res = query_qualified_relation(g1)
        assert len(res) == 1
        assert res[0] == {
            "city": "Hanoi",
            "country": "Vietnam",
            "validFrom": 1976,
            "status": "Official",
        }

    def test_standard_reification_pattern2(self) -> None:
        from exp_3_4_nary_reification import (
            build_pattern2_standard_reification,
            query_standard_reification,
        )

        g2 = build_pattern2_standard_reification()
        res = query_standard_reification(g2)
        assert len(res) == 1
        assert res[0] == {
            "city": "Hanoi",
            "country": "Vietnam",
            "validFrom": 1976,
            "status": "Official",
        }

    def test_pattern1_and_pattern2_exact_semantic_equivalence(self) -> None:
        from exp_3_4_nary_reification import (
            build_pattern1_qualified_relation,
            build_pattern2_standard_reification,
            query_qualified_relation,
            query_standard_reification,
        )

        res1 = query_qualified_relation(build_pattern1_qualified_relation())
        res2 = query_standard_reification(build_pattern2_standard_reification())
        assert res1 == res2


# ---------------------------------------------------------------------------
# Experiment 3-5: Contextual Knowledge Coexistence
# ---------------------------------------------------------------------------


class TestExp35ContextCoexistence:
    """Semantic tests for exp_3_5_context_coexistence.py."""

    def test_contextual_measurements_coexist(self) -> None:
        from exp_3_5_context_coexistence import (
            build_contextual_mechanism_graph,
            query_measurement_by_temperature,
        )

        g = build_contextual_mechanism_graph()
        res_room = query_measurement_by_temperature(g, 293.15)
        res_elev = query_measurement_by_temperature(g, 353.15)

        assert len(res_room) == 1
        assert res_room[0]["value"] == 0.598
        assert res_room[0]["temperature"] == 293.15

        assert len(res_elev) == 1
        assert res_elev[0]["value"] == 0.670
        assert res_elev[0]["temperature"] == 353.15


# ---------------------------------------------------------------------------
# Experiment 3-6: Deterministic Entity Resolution Pipeline
# ---------------------------------------------------------------------------


class TestExp36IdentityResolution:
    """Semantic tests for exp_3_6_identity_resolution.py."""

    def test_exact_ifp_matching(self) -> None:
        from exp_3_6_identity_resolution import EntityRecord, EntityResolutionPipeline

        pipeline = EntityResolutionPipeline()
        r1 = EntityRecord("a1", "Ha Noi City", "Vietnam", iso_code="VN-HN")
        r2 = EntityRecord("b1", "Hà Nội", "Vietnam", iso_code="VN-HN")

        decision, score, rationale = pipeline._evaluate_pair(r1, r2)
        assert decision == "MATCH"
        assert score == 1.0
        assert "Exact IFP Match" in rationale

    def test_fellegi_sunter_3_zones(self) -> None:
        from exp_3_6_identity_resolution import EntityRecord, EntityResolutionPipeline

        pipeline = EntityResolutionPipeline(match_threshold=0.85, non_match_threshold=0.50)

        # Non-match case
        r1 = EntityRecord("a1", "Paris", "France")
        r2 = EntityRecord("b1", "Hanoi", "Vietnam")
        decision, score, _ = pipeline._evaluate_pair(r1, r2)
        assert decision == "NON_MATCH"
        assert score <= 0.50

        # Review zone case
        r3 = EntityRecord("a3", "Da Nang", "Vietnam")
        r4 = EntityRecord("b3", "Hà Nội", "Vietnam")
        decision, score, _ = pipeline._evaluate_pair(r3, r4)
        assert decision == "CLERICAL_REVIEW"
        assert 0.50 < score < 0.85
