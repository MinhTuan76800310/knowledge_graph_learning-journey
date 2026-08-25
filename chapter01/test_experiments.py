"""Tests for Chapter 1 experiments.

Verifies that all experiment modules produce correct outputs and
that the core data structures behave as documented.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

CHAPTER01_DIR = Path(__file__).parent


# ---------------------------------------------------------------------------
# Experiment 1-1 tests
# ---------------------------------------------------------------------------


class TestExp11:
    """Tests for exp_1_1_plain_graph.py."""

    def test_plain_graph_nodes_and_edges(self) -> None:
        sys.path.insert(0, str(CHAPTER01_DIR))
        from exp_1_1_plain_graph import PlainGraph

        g = PlainGraph()
        g.add_edge("A", "r", "B")
        g.add_edge("B", "r", "C")
        assert g.nodes == {"A", "B", "C"}
        assert len(g.edges) == 2

    def test_plain_graph_neighbors(self) -> None:
        sys.path.insert(0, str(CHAPTER01_DIR))
        from exp_1_1_plain_graph import PlainGraph

        g = PlainGraph()
        g.add_edge("A", "r1", "B")
        g.add_edge("A", "r2", "C")
        neighbors = g.neighbors("A")
        assert ("r1", "B") in neighbors
        assert ("r2", "C") in neighbors

    def test_plain_graph_bfs_path(self) -> None:
        sys.path.insert(0, str(CHAPTER01_DIR))
        from exp_1_1_plain_graph import PlainGraph

        g = PlainGraph()
        g.add_edge("A", "x", "B")
        g.add_edge("B", "x", "C")
        g.add_edge("C", "x", "D")
        path = g.find_path_bfs("A", "D")
        assert path == ["A", "B", "C", "D"]

    def test_plain_graph_no_path(self) -> None:
        sys.path.insert(0, str(CHAPTER01_DIR))
        from exp_1_1_plain_graph import PlainGraph

        g = PlainGraph()
        g.add_node("A")
        g.add_node("Z")
        assert g.find_path_bfs("A", "Z") is None

    def test_city_and_social_same_topology(self) -> None:
        sys.path.insert(0, str(CHAPTER01_DIR))
        from exp_1_1_plain_graph import build_city_graph, build_social_graph

        city = build_city_graph()
        social = build_social_graph()
        assert len(city.nodes) == len(social.nodes)
        assert len(city.edges) == len(social.edges)

    def test_experiment_runs(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CHAPTER01_DIR / "exp_1_1_plain_graph.py")],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert result.returncode == 0
        assert "Plain Graph Without Semantics" in result.stdout


# ---------------------------------------------------------------------------
# Experiment 1-2 tests
# ---------------------------------------------------------------------------


class TestExp12:
    """Tests for exp_1_2_data_graph_vs_taxonomy.py."""

    def test_data_graph_query(self) -> None:
        sys.path.insert(0, str(CHAPTER01_DIR))
        from exp_1_2_data_graph_vs_taxonomy import DataGraph

        g = DataGraph()
        g.add_relation("A", "type", "X")
        g.add_relation("B", "type", "Y")
        results = g.query("type")
        assert ("A", "X") in results
        assert ("B", "Y") in results

    def test_taxonomy_ancestors(self) -> None:
        sys.path.insert(0, str(CHAPTER01_DIR))
        from exp_1_2_data_graph_vs_taxonomy import Taxonomy

        t = Taxonomy()
        t.add_subclass("Dog", "Mammal")
        t.add_subclass("Mammal", "Animal")
        ancestors = t.ancestors("Dog")
        assert ancestors == {"Mammal", "Animal"}

    def test_taxonomy_all_instances_includes_subclasses(self) -> None:
        sys.path.insert(0, str(CHAPTER01_DIR))
        from exp_1_2_data_graph_vs_taxonomy import Taxonomy

        t = Taxonomy()
        t.add_subclass("CapitalCity", "City")
        t.add_instance("Hanoi", "CapitalCity")
        t.add_instance("HCMC", "City")
        instances = t.all_instances_of("City")
        assert "Hanoi" in instances
        assert "HCMC" in instances

    def test_taxonomy_transitive_instances(self) -> None:
        sys.path.insert(0, str(CHAPTER01_DIR))
        from exp_1_2_data_graph_vs_taxonomy import Taxonomy

        t = Taxonomy()
        t.add_subclass("City", "Place")
        t.add_subclass("Region", "Place")
        t.add_instance("Hanoi", "City")
        t.add_instance("RedRiverDelta", "Region")
        all_places = t.all_instances_of("Place")
        assert all_places == {"Hanoi", "RedRiverDelta"}

    def test_experiment_runs(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CHAPTER01_DIR / "exp_1_2_data_graph_vs_taxonomy.py")],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert result.returncode == 0
        assert "Data Graph vs Taxonomy" in result.stdout


# ---------------------------------------------------------------------------
# Experiment 1-3 tests
# ---------------------------------------------------------------------------


class TestExp13:
    """Tests for exp_1_3_sister_city_kg.py."""

    def test_experiment_runs(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CHAPTER01_DIR / "exp_1_3_sister_city_kg.py")],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert result.returncode == 0
        assert "Progressive Transformation" in result.stdout

    def test_symmetric_inference_present(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CHAPTER01_DIR / "exp_1_3_sister_city_kg.py")],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert "symmetric" in result.stdout.lower() or "INFERRED" in result.stdout

    def test_subclass_inference_present(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CHAPTER01_DIR / "exp_1_3_sister_city_kg.py")],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert "subclass" in result.stdout.lower() or "Settlement" in result.stdout


# ---------------------------------------------------------------------------
# Experiment 1-4 tests
# ---------------------------------------------------------------------------


class TestExp14:
    """Tests for exp_1_4_data_graph_to_kg.py."""

    def test_experiment_runs(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CHAPTER01_DIR / "exp_1_4_data_graph_to_kg.py")],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert result.returncode == 0
        assert "Data Graph" in result.stdout

    def test_inference_produces_new_triples(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CHAPTER01_DIR / "exp_1_4_data_graph_to_kg.py")],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert "INFERRED" in result.stdout or "Inferred" in result.stdout

    def test_region_query_works_after_semantics(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CHAPTER01_DIR / "exp_1_4_data_graph_to_kg.py")],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert "Region" in result.stdout


# ---------------------------------------------------------------------------
# Experiment 1-5 tests
# ---------------------------------------------------------------------------


class TestExp15:
    """Tests for exp_1_5_relation_semantics.py."""

    def test_experiment_runs(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CHAPTER01_DIR / "exp_1_5_relation_semantics.py")],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert result.returncode == 0
        assert "Semantics of a Relation" in result.stdout

    def test_inverse_inference(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CHAPTER01_DIR / "exp_1_5_relation_semantics.py")],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert "hasCapital" in result.stdout

    def test_transitive_inference(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CHAPTER01_DIR / "exp_1_5_relation_semantics.py")],
            capture_output=True,
            text=True,
            timeout=30,
        )
        # RedRiverDelta partOf Vietnam should be inferred transitively
        assert "Vietnam" in result.stdout
