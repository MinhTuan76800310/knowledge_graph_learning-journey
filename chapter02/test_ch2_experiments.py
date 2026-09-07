"""Direct semantic tests for Chapter 2 RDF/SPARQL experiments.

Tests assert graph content, round-trip equivalence, and exact SPARQL
query result bindings — not stdout substring matching.

Domain (shared across all Chapter 2 experiments):
  Hanoi capitalOf Vietnam, Paris capitalOf France, Hanoi sisterCity Paris.

Semantic contracts: R11-01, R11-02, R11-05, SP11-01, SP11-02, TOOL-01.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

rdflib = pytest.importorskip("rdflib")

CHAPTER02_DIR = Path(__file__).parent
if str(CHAPTER02_DIR) not in sys.path:
    sys.path.insert(0, str(CHAPTER02_DIR))


# ---------------------------------------------------------------------------
# Experiment 2-1: RDF from First Principles
# ---------------------------------------------------------------------------


class TestExp21RdfFirstPrinciples:
    """Semantic tests for exp_2_1_rdf_first_principles.py."""

    def _make_store(self):
        from exp_2_1_rdf_first_principles import SimpleTripleStore

        store = SimpleTripleStore()
        store.add(":Hanoi", "rdf:type", ":City")
        store.add(":Hanoi", "rdfs:label", "Hà Nội")
        store.add(":Hanoi", ":capitalOf", ":Vietnam")
        store.add(":Hanoi", ":sisterCity", ":Paris")
        store.add(":Paris", "rdf:type", ":City")
        store.add(":Paris", "rdfs:label", "Paris")
        store.add(":Paris", ":capitalOf", ":France")
        store.add(":Vietnam", "rdf:type", ":Country")
        store.add(":Vietnam", "rdfs:label", "Việt Nam")
        store.add(":France", "rdf:type", ":Country")
        store.add(":France", "rdfs:label", "France")
        return store

    def test_triple_count_exact(self) -> None:
        store = self._make_store()
        assert store.count() == 11

    def test_subjects_are_expected_set(self) -> None:
        store = self._make_store()
        assert store.subjects() == {":Hanoi", ":Paris", ":Vietnam", ":France"}

    def test_predicates_are_expected_set(self) -> None:
        store = self._make_store()
        assert store.predicates() == {
            "rdf:type",
            "rdfs:label",
            ":capitalOf",
            ":sisterCity",
        }

    def test_query_cities_returns_hanoi_and_paris(self) -> None:
        store = self._make_store()
        cities = store.query(p="rdf:type", o=":City")
        assert {c[0] for c in cities} == {":Hanoi", ":Paris"}

    def test_query_capitals_returns_two_pairs(self) -> None:
        store = self._make_store()
        capitals = store.query(p=":capitalOf")
        assert {(c[0], c[2]) for c in capitals} == {
            (":Hanoi", ":Vietnam"),
            (":Paris", ":France"),
        }

    def test_query_hanoi_facts_returns_four_triples(self) -> None:
        store = self._make_store()
        assert len(store.query(s=":Hanoi")) == 4

    def test_set_semantics_no_duplicates(self) -> None:
        """RDF graph = set of triples; re-adding an existing triple is a no-op."""
        store = self._make_store()
        store.add(":Hanoi", "rdf:type", ":City")
        assert store.count() == 11

    def test_rdflib_graph_has_exact_triples(self) -> None:
        from rdflib import RDF, RDFS, Graph, Literal, Namespace

        EX = Namespace("http://example.org/")
        g = Graph()
        g.add((EX.Hanoi, RDF.type, EX.City))
        g.add((EX.Hanoi, RDFS.label, Literal("Hà Nội")))
        g.add((EX.Hanoi, EX.capitalOf, EX.Vietnam))
        g.add((EX.Hanoi, EX.sisterCity, EX.Paris))
        g.add((EX.Paris, RDF.type, EX.City))
        g.add((EX.Paris, RDFS.label, Literal("Paris")))
        g.add((EX.Paris, EX.capitalOf, EX.France))
        g.add((EX.Vietnam, RDF.type, EX.Country))
        g.add((EX.Vietnam, RDFS.label, Literal("Việt Nam")))
        g.add((EX.France, RDF.type, EX.Country))
        g.add((EX.France, RDFS.label, Literal("France")))
        assert len(g) == 11
        # Exact graph membership assertions
        assert (EX.Hanoi, EX.capitalOf, EX.Vietnam) in g
        assert (EX.Hanoi, EX.sisterCity, EX.Paris) in g
        # Direction matters: sisterCity was only asserted Hanoi -> Paris
        assert (EX.Paris, EX.sisterCity, EX.Hanoi) not in g

    def test_rdflib_term_types_differ(self) -> None:
        """IRI, Literal, and BNode are distinct RDF term types."""
        from rdflib import BNode, Literal, URIRef

        assert isinstance(URIRef("http://example.org/Hanoi"), URIRef)
        assert not isinstance(Literal("Hà Nội"), URIRef)
        assert not isinstance(BNode(), URIRef)

    def test_rdflib_integer_literal_datatype(self) -> None:
        from rdflib import XSD, Literal

        assert Literal(8418883).datatype == XSD.integer

    def test_rdflib_sparql_returns_two_cities(self) -> None:
        from rdflib import RDF, Graph, Namespace

        EX = Namespace("http://example.org/")
        g = Graph()
        g.add((EX.Hanoi, RDF.type, EX.City))
        g.add((EX.Paris, RDF.type, EX.City))
        g.add((EX.Vietnam, RDF.type, EX.Country))
        qres = list(
            g.query(
                """
                PREFIX ex: <http://example.org/>
                SELECT ?city WHERE { ?city a ex:City }
                """
            )
        )
        assert len(qres) == 2
        assert {str(row.city).split("/")[-1] for row in qres} == {"Hanoi", "Paris"}


# ---------------------------------------------------------------------------
# Experiment 2-2: Turtle Serialization Round-Trip
# ---------------------------------------------------------------------------


class TestExp22TurtleSerialization:
    """Semantic tests for exp_2_2_turtle_serialization.py."""

    def _build_graph(self):
        from rdflib import RDF, RDFS, Graph, Literal, Namespace

        EX = Namespace("http://example.org/")
        g = Graph()
        g.bind("ex", EX)
        g.add((EX.Hanoi, RDF.type, EX.City))
        g.add((EX.Hanoi, RDFS.label, Literal("Hà Nội")))
        g.add((EX.Hanoi, EX.capitalOf, EX.Vietnam))
        g.add((EX.Hanoi, EX.population, Literal(8418883)))
        g.add((EX.Paris, RDF.type, EX.City))
        g.add((EX.Paris, RDFS.label, Literal("Paris")))
        g.add((EX.Paris, EX.capitalOf, EX.France))
        g.add((EX.Hanoi, EX.sisterCity, EX.Paris))
        g.add((EX.Vietnam, RDF.type, EX.Country))
        g.add((EX.France, RDF.type, EX.Country))
        return g

    def test_round_trip_preserves_triple_count(self) -> None:
        from rdflib import Graph

        g1 = self._build_graph()
        turtle_text = g1.serialize(format="turtle")
        g2 = Graph()
        g2.parse(data=turtle_text, format="turtle")
        assert len(g1) == len(g2) == 10

    def test_round_trip_preserves_exact_triples(self) -> None:
        """Semantic comparison of parsed graphs — never raw string comparison."""
        from rdflib import Graph

        g1 = self._build_graph()
        turtle_text = g1.serialize(format="turtle")
        g2 = Graph()
        g2.parse(data=turtle_text, format="turtle")
        assert set(g1) == set(g2)

    def test_ntriples_round_trip_preserves_graph(self) -> None:
        from rdflib import Graph

        g1 = self._build_graph()
        nt_text = g1.serialize(format="nt")
        g2 = Graph()
        g2.parse(data=nt_text, format="nt")
        assert set(g1) == set(g2)

    def test_xml_round_trip_preserves_graph(self) -> None:
        from rdflib import Graph

        g1 = self._build_graph()
        xml_text = g1.serialize(format="xml")
        g2 = Graph()
        g2.parse(data=xml_text, format="xml")
        assert set(g1) == set(g2)

    def test_literal_value_survives_round_trip(self) -> None:
        from rdflib import Graph

        g1 = self._build_graph()
        turtle_text = g1.serialize(format="turtle")
        g2 = Graph()
        g2.parse(data=turtle_text, format="turtle")
        pop_results = list(
            g2.query(
                """
                PREFIX ex: <http://example.org/>
                SELECT ?pop WHERE { ex:Hanoi ex:population ?pop }
                """
            )
        )
        assert len(pop_results) == 1
        assert int(pop_results[0].pop) == 8418883

    def test_different_prefixes_produce_equivalent_graph(self) -> None:
        """Two Turtle docs with different prefix names yield the same graph.

        Prefixes are syntactic sugar; they do not change the underlying IRIs.
        """
        from rdflib import Graph

        turtle_a = """
        @prefix ex: <http://example.org/> .
        @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        ex:Hanoi rdf:type ex:City .
        """
        turtle_b = """
        @prefix foo: <http://example.org/> .
        @prefix r: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        foo:Hanoi r:type foo:City .
        """
        ga = Graph()
        ga.parse(data=turtle_a, format="turtle")
        gb = Graph()
        gb.parse(data=turtle_b, format="turtle")
        assert set(ga) == set(gb)


# ---------------------------------------------------------------------------
# Experiment 2-3: SPARQL Basic Graph Patterns
# ---------------------------------------------------------------------------


class TestExp23SparqlBasicPatterns:
    """Semantic tests for exp_2_3_sparql_basic_patterns.py."""

    def _build_graph(self):
        from rdflib import RDF, RDFS, Graph, Literal, Namespace

        EX = Namespace("http://example.org/")
        g = Graph()
        g.bind("ex", EX)
        g.add((EX.Hanoi, RDF.type, EX.City))
        g.add((EX.Hanoi, RDFS.label, Literal("Hà Nội")))
        g.add((EX.Hanoi, EX.capitalOf, EX.Vietnam))
        g.add((EX.Hanoi, EX.population, Literal(8418883)))
        g.add((EX.Paris, RDF.type, EX.City))
        g.add((EX.Paris, RDFS.label, Literal("Paris")))
        g.add((EX.Paris, EX.capitalOf, EX.France))
        g.add((EX.Hanoi, EX.sisterCity, EX.Paris))
        g.add((EX.Vietnam, RDF.type, EX.Country))
        g.add((EX.France, RDF.type, EX.Country))
        g.add((EX.Vietnam, RDFS.label, Literal("Việt Nam")))
        g.add((EX.France, RDFS.label, Literal("France")))
        return g

    def test_q1_find_all_cities_returns_two(self) -> None:
        g = self._build_graph()
        results = list(
            g.query(
                """
                PREFIX ex: <http://example.org/>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                SELECT ?city WHERE { ?city rdf:type ex:City }
                """
            )
        )
        assert len(results) == 2
        cities = {str(row.city).split("/")[-1] for row in results}
        assert cities == {"Hanoi", "Paris"}

    def test_q2_city_labels_returns_correct_bindings(self) -> None:
        g = self._build_graph()
        results = list(
            g.query(
                """
                PREFIX ex: <http://example.org/>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                SELECT ?city ?label
                WHERE {
                    ?city rdf:type ex:City .
                    ?city rdfs:label ?label .
                }
                """
            )
        )
        assert len(results) == 2
        bindings = {str(row.city).split("/")[-1]: str(row.label) for row in results}
        assert bindings["Hanoi"] == "Hà Nội"
        assert bindings["Paris"] == "Paris"

    def test_q3_capitals_of_countries_returns_two(self) -> None:
        """Multi-triple BGP joins on the shared variable ?country."""
        g = self._build_graph()
        results = list(
            g.query(
                """
                PREFIX ex: <http://example.org/>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                SELECT ?capital ?country
                WHERE {
                    ?capital ex:capitalOf ?country .
                    ?country rdf:type ex:Country .
                }
                """
            )
        )
        assert len(results) == 2
        pairs = {(str(r.capital).split("/")[-1], str(r.country).split("/")[-1]) for r in results}
        assert pairs == {("Hanoi", "Vietnam"), ("Paris", "France")}

    def test_q3b_sister_city_returns_one_binding(self) -> None:
        g = self._build_graph()
        results = list(
            g.query(
                """
                PREFIX ex: <http://example.org/>
                SELECT ?sister WHERE { ex:Hanoi ex:sisterCity ?sister }
                """
            )
        )
        assert len(results) == 1
        assert str(results[0].sister).split("/")[-1] == "Paris"

    def test_q4_filter_population_above_5m(self) -> None:
        g = self._build_graph()
        results = list(
            g.query(
                """
                PREFIX ex: <http://example.org/>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                SELECT ?city ?pop
                WHERE {
                    ?city rdf:type ex:City .
                    ?city ex:population ?pop .
                    FILTER (?pop > 5000000)
                }
                """
            )
        )
        assert len(results) == 1
        assert str(results[0].city).split("/")[-1] == "Hanoi"
        assert int(results[0].pop) == 8418883

    def test_q5_optional_keeps_unmatched_solutions(self) -> None:
        """OPTIONAL extends solutions; entities without a match still appear."""
        from rdflib import RDF, RDFS, Graph, Literal, Namespace

        EX = Namespace("http://example.org/")
        g = Graph()
        g.add((EX.Hanoi, RDF.type, EX.City))
        g.add((EX.Saigon, RDF.type, EX.City))
        # Hanoi has a label, Saigon does not
        g.add((EX.Hanoi, RDFS.label, Literal("Hà Nội")))
        results = list(
            g.query(
                """
                PREFIX ex: <http://example.org/>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                SELECT ?city ?label
                WHERE {
                    ?city a ex:City .
                    OPTIONAL { ?city rdfs:label ?label }
                }
                """
            )
        )
        assert len(results) == 2
        labels = {str(row.city).split("/")[-1]: row.label for row in results}
        assert str(labels["Hanoi"]) == "Hà Nội"
        assert labels["Saigon"] is None  # unbound, not dropped

    def test_empty_pattern_returns_nothing(self) -> None:
        g = self._build_graph()
        results = list(
            g.query(
                """
                PREFIX ex: <http://example.org/>
                SELECT ?x WHERE { ?x ex:nonExistentPredicate ?y }
                """
            )
        )
        assert len(results) == 0


# ---------------------------------------------------------------------------
# Experiment 2-4: RATE_OF_CHANGE qua RDF + SPARQL (capstone thread)
# ---------------------------------------------------------------------------

EX_MK = "http://example.org/kgbook/mks#"


def _load_mechanism_graph():
    """Load the canonical running dataset (Ch1-6) from datasets/mechanism_kg/."""
    from rdflib import Graph

    dataset = (
        Path(__file__).resolve().parents[1] / "datasets" / "mechanism_kg" / "rate_of_change.ttl"
    )
    g = Graph()
    g.parse(dataset, format="turtle")
    g.bind("ex", EX_MK)
    return g


def _short(term) -> str:
    return str(term).rsplit("#", 1)[-1]


class TestExp24MechanismSparql:
    """Semantic tests for exp_2_4_mechanism_turtle_sparql.py.

    These assert the chapter's capstone result tables directly against the
    running dataset at datasets/mechanism_kg/rate_of_change.ttl.
    """

    def test_dataset_loads(self) -> None:
        g = _load_mechanism_graph()
        assert len(g) > 0

    def test_bgp_three_hop_reads_ndarry_application(self) -> None:
        """Chapter table in §2.1.6: mechanism -> application -> (differentiand, wrt)."""
        g = _load_mechanism_graph()
        results = list(
            g.query(
                f"""
                PREFIX ex: <{EX_MK}>
                SELECT ?mechanism ?applied ?quantity ?wrt
                WHERE {{
                    ?mechanism ex:hasApplication ?applied .
                    ?applied  ex:differentiand   ?quantity .
                    ?applied  ex:withRespectTo   ?wrt .
                }}
                """
            )
        )
        bindings = {
            (
                _short(r.mechanism),
                _short(r.applied),
                _short(r.quantity),
                _short(r.wrt),
            )
            for r in results
        }
        assert bindings == {
            ("rateOfChange_1", "derivativeApplication_1", "position_1", "time_1"),
            ("heatTransferRate_2", "derivativeApplication_2", "thermalEnergy_1", "time_1"),
        }

    def test_rdf_type_subclass_gap(self) -> None:
        """`?m a ex:Mechanism` matches nothing; the declared type matches 3."""
        g = _load_mechanism_graph()
        by_super = list(g.query(f"PREFIX ex: <{EX_MK}> SELECT ?m WHERE {{ ?m a ex:Mechanism }}"))
        by_declared = list(
            g.query(f"PREFIX ex: <{EX_MK}> SELECT ?m WHERE {{ ?m a ex:RateOfChangeMechanism }}")
        )
        assert len(by_super) == 0  # no subclass reasoning in plain RDF
        names = {_short(r.m) for r in by_declared}
        assert names == {"rateOfChange_1", "heatTransferRate_2", "newtonCooling_1"}

    def test_filter_on_value_threshold(self) -> None:
        """Chapter result: position_1 (12.5) and thermalEnergy_1 (300.0) pass >10."""
        g = _load_mechanism_graph()
        results = list(
            g.query(
                f"""
                PREFIX ex: <{EX_MK}>
                SELECT ?q ?v WHERE {{
                    ?q ex:hasValue ?v .
                    FILTER (?v > 10)
                }}
                """
            )
        )
        pairs = {(_short(r.q), str(r.v)) for r in results}
        assert pairs == {("position_1", "12.5"), ("thermalEnergy_1", "300.0")}

    def test_optional_behaves_like_left_join(self) -> None:
        """Only newtonCooling_1 has a condition; the other two stay unbound."""
        g = _load_mechanism_graph()
        results = list(
            g.query(
                f"""
                PREFIX ex: <{EX_MK}>
                SELECT ?m ?condition WHERE {{
                    ?m a ex:RateOfChangeMechanism .
                    OPTIONAL {{ ?m ex:hasCondition ?condition }}
                }}
                """
            )
        )
        assert len(results) == 3
        bound = {_short(r.m): _short(r.condition) for r in results if r.condition is not None}
        assert bound == {"newtonCooling_1": "uniformEnv_1"}
        no_cond = {_short(r.m) for r in results if r.condition is None}
        assert no_cond == {"rateOfChange_1", "heatTransferRate_2"}

    def test_requires_query_answers_dependency_question(self) -> None:
        """'Cơ chế nào phụ thuộc vào cơ chế nào' over the running dataset."""
        g = _load_mechanism_graph()
        results = list(
            g.query(
                f"""
                PREFIX ex: <{EX_MK}>
                SELECT ?m ?dependency WHERE {{ ?m ex:requires ?dependency }}
                """
            )
        )
        pairs = {(_short(r.m), _short(r.dependency)) for r in results}
        assert pairs == {
            ("newtonCooling_1", "rateOfChange_1"),
            ("newtonCooling_1", "heatTransferRate_2"),
        }


# ---------------------------------------------------------------------------
# Experiment 2-5: Labeled Property Graph (LPG) Modeling & Ingestion
# ---------------------------------------------------------------------------


class TestExp25LabeledPropertyGraph:
    """Semantic tests for exp_2_5_labeled_property_graph.py."""

    def test_node_creation_and_multilabel(self) -> None:
        from exp_2_5_labeled_property_graph import SimplePropertyGraph

        g = SimplePropertyGraph()
        n = g.add_node("Hanoi", labels={"City", "Capital"}, properties={"population": 8418883})
        assert n.id == "Hanoi"
        assert n.labels == {"City", "Capital"}
        assert n.has_label("City")
        assert n.has_label("Capital")
        assert not n.has_label("Country")
        assert n.get("population") == 8418883
        assert n.get("nonexistent", "default") == "default"

    def test_edge_creation_and_properties(self) -> None:
        from exp_2_5_labeled_property_graph import SimplePropertyGraph

        g = SimplePropertyGraph()
        g.add_node("Hanoi", labels={"City"})
        g.add_node("Vietnam", labels={"Country"})
        e = g.add_edge(
            "e1",
            "Hanoi",
            "Vietnam",
            "CAPITAL_OF",
            properties={"since": 1976, "status": "Official"},
        )
        assert e.id == "e1"
        assert e.source == "Hanoi"
        assert e.target == "Vietnam"
        assert e.type == "CAPITAL_OF"
        assert e.get("since") == 1976
        assert e.get("status") == "Official"

    def test_edge_creation_fails_on_missing_nodes(self) -> None:
        import pytest
        from exp_2_5_labeled_property_graph import SimplePropertyGraph

        g = SimplePropertyGraph()
        g.add_node("Hanoi", labels={"City"})
        with pytest.raises(ValueError, match="Target node 'Vietnam' does not exist"):
            g.add_edge("e1", "Hanoi", "Vietnam", "CAPITAL_OF")

    def test_city_graph_structure(self) -> None:
        from exp_2_5_labeled_property_graph import build_city_graph

        g = build_city_graph()
        assert len(g.nodes) == 4
        assert len(g.edges) == 3
        assert set(g.nodes.keys()) == {"Hanoi", "Vietnam", "Paris", "France"}

        # Outgoing edges from Hanoi: CAPITAL_OF and SISTER_CITY
        hn_out = g.outgoing_edges("Hanoi")
        assert len(hn_out) == 2
        types = {e.type for e in hn_out}
        assert types == {"CAPITAL_OF", "SISTER_CITY"}

        # Incoming edges to Vietnam: CAPITAL_OF from Hanoi
        vn_in = g.incoming_edges("Vietnam")
        assert len(vn_in) == 1
        assert vn_in[0].source == "Hanoi"

    def test_mechanism_graph_structure(self) -> None:
        from exp_2_5_labeled_property_graph import build_mechanism_graph

        g = build_mechanism_graph()
        assert len(g.nodes) == 6
        assert len(g.edges) == 5

        # Check derivative operation node wiring
        op_nodes = g.nodes_with_label("Operation")
        assert len(op_nodes) == 1
        op = op_nodes[0]
        assert op.get("type") == "Derivative"

        diff_edges = g.outgoing_edges(op.id, "DIFFERENTIAND")
        assert len(diff_edges) == 1
        assert diff_edges[0].target == "position_1"

        wrt_edges = g.outgoing_edges(op.id, "WITH_RESPECT_TO")
        assert len(wrt_edges) == 1
        assert wrt_edges[0].target == "time_1"


# ---------------------------------------------------------------------------
# Experiment 2-6: Cypher Pattern Matching & Graph Traversal
# ---------------------------------------------------------------------------


class TestExp26CypherTraversal:
    """Semantic tests for exp_2_6_cypher_traversal.py."""

    def test_directed_pattern_matching_capitals(self) -> None:
        from exp_2_5_labeled_property_graph import build_city_graph
        from exp_2_6_cypher_traversal import CypherPatternEngine

        g = build_city_graph()
        engine = CypherPatternEngine(g)
        matches = engine.match_hop("City", "CAPITAL_OF", "Country", direction="OUT")

        pairs = {(m["source"].id, m["target"].id) for m in matches}
        assert pairs == {("Hanoi", "Vietnam"), ("Paris", "France")}

        # Check edge metadata preserved in match
        for m in matches:
            assert "since" in m["relationship"].properties

    def test_undirected_matching_sister_cities(self) -> None:
        from exp_2_5_labeled_property_graph import build_city_graph
        from exp_2_6_cypher_traversal import CypherPatternEngine

        g = build_city_graph()
        engine = CypherPatternEngine(g)

        # Undirected match traverses in both directions
        matches = engine.match_hop("City", "SISTER_CITY", "City", direction="BOTH")
        pairs = {(m["source"].id, m["target"].id) for m in matches}
        assert pairs == {("Hanoi", "Paris"), ("Paris", "Hanoi")}

        # Directed match only traverses forward
        matches_out = engine.match_hop("City", "SISTER_CITY", "City", direction="OUT")
        pairs_out = {(m["source"].id, m["target"].id) for m in matches_out}
        assert pairs_out == {("Hanoi", "Paris")}

    def test_variable_length_path_traversal(self) -> None:
        from exp_2_5_labeled_property_graph import build_mechanism_graph
        from exp_2_6_cypher_traversal import CypherPatternEngine

        g = build_mechanism_graph()
        engine = CypherPatternEngine(g)

        # newtonCooling_1 requires rateOfChange_1 and heatTransferRate_2
        paths = engine.find_paths("newtonCooling_1", "REQUIRES", min_hops=1, max_hops=2)
        assert len(paths) == 2
        endpoints = {p[-1] for p in paths}
        assert endpoints == {"rateOfChange_1", "heatTransferRate_2"}


# ---------------------------------------------------------------------------
# Experiment 2-7: RDF vs. Property Graph Executable Benchmark
# ---------------------------------------------------------------------------


class TestExp27RdfVsPropertyGraph:
    """Semantic tests for exp_2_7_rdf_vs_property_graph.py."""

    def test_exact_semantic_equivalence(self) -> None:
        from exp_2_7_rdf_vs_property_graph import (
            build_lpg_representation,
            build_rdf_representation,
            query_lpg_capital_with_metadata,
            query_rdf_capital_with_metadata,
        )

        rdf_g = build_rdf_representation()
        lpg_g = build_lpg_representation()

        rdf_res = query_rdf_capital_with_metadata(rdf_g)
        lpg_res = query_lpg_capital_with_metadata(lpg_g)

        # Assert identical structured answers across completely different graph engines
        assert rdf_res == lpg_res
        assert len(rdf_res) == 2
        assert rdf_res[0] == {"city": "Hanoi", "country": "Vietnam", "since": 1976}
        assert rdf_res[1] == {"city": "Paris", "country": "France", "since": 1789}

    def test_structural_tradeoffs_edge_metadata(self) -> None:
        """Assert that RDF standard reification requires 5 triples per statement

        while LPG requires 1 relationship with inline property.
        """
        from exp_2_7_rdf_vs_property_graph import (
            build_lpg_representation,
            build_rdf_representation,
        )

        rdf_g = build_rdf_representation()
        lpg_g = build_lpg_representation()

        # RDF has 22 triples total (12 base triples + 10 reification triples for 2 statements)
        assert len(rdf_g) == 22

        # LPG has 4 nodes and 3 edges total
        assert len(lpg_g.nodes) == 4
        assert len(lpg_g.edges) == 3

        # In LPG, the edge 'e_hn_vn' directly holds since=1976 without any helper nodes
        edge = lpg_g.get_edge("e_hn_vn")
        assert edge is not None
        assert edge.properties["since"] == 1976
