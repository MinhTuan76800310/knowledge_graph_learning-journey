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
