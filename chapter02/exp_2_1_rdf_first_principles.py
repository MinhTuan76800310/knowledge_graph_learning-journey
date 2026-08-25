"""Experiment 2-1: RDF from First Principles.

Question: "What exactly exists in an RDF graph?"

Demonstrates the core RDF data model using both a pure-Python triple store
and RDFLib, showing how triples, IRIs, literals, and blank nodes work.

Domain (shared across all Chapter 2 experiments):
  - Hanoi capitalOf Vietnam
  - Paris capitalOf France
  - Hanoi sisterCity Paris

Semantic contracts: R11-01 (RDF Primer), R11-02 (RDF Concepts), TOOL-01 (RDFLib).
Difficulty: ★
Status: ✅ Independently runnable
"""

from __future__ import annotations


class SimpleTripleStore:
    """A minimal in-memory triple store built from first principles.

    This demonstrates the raw mechanism: an RDF graph is a SET of triples.
    No duplicates, no ordering semantics, no type system beyond strings.
    """

    def __init__(self) -> None:
        self.triples: list[tuple[str, str, str]] = []

    def add(self, s: str, p: str, o: str) -> None:
        """Add a triple (subject, predicate, object). Set semantics: no duplicates."""
        triple = (s, p, o)
        if triple not in self.triples:
            self.triples.append(triple)

    def query(
        self,
        s: str | None = None,
        p: str | None = None,
        o: str | None = None,
    ) -> list[tuple[str, str, str]]:
        """Pattern-match triples. None means wildcard."""
        results = []
        for ts, tp, to in self.triples:
            if (s is None or ts == s) and (p is None or tp == p) and (o is None or to == o):
                results.append((ts, tp, to))
        return results

    def subjects(self) -> set[str]:
        """Return all unique subjects."""
        return {t[0] for t in self.triples}

    def predicates(self) -> set[str]:
        """Return all unique predicates."""
        return {t[1] for t in self.triples}

    def objects(self) -> set[str]:
        """Return all unique objects."""
        return {t[2] for t in self.triples}

    def count(self) -> int:
        """Return number of triples."""
        return len(self.triples)


def demo_pure_python() -> None:
    """Demonstrate triple store without any library."""
    print("=" * 60)
    print("PART 1: Pure Python Triple Store (mechanism)")
    print("=" * 60)

    store = SimpleTripleStore()

    # Add triples using the shared Chapter 2 domain
    # In the pure-Python store, everything is a string — no type distinction.
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

    print(f"\nTotal triples: {store.count()}")
    print(f"Subjects: {sorted(store.subjects())}")
    print(f"Predicates: {sorted(store.predicates())}")

    # Query: find all cities
    cities = store.query(p="rdf:type", o=":City")
    print(f"\nCities (rdf:type :City): {sorted(c[0] for c in cities)}")

    # Query: what do we know about Hanoi?
    hanoi_facts = store.query(s=":Hanoi")
    print(f"\nFacts about :Hanoi ({len(hanoi_facts)} triples):")
    for s, p, o in hanoi_facts:
        print(f"  {s} --{p}--> {o}")

    # Demonstrate set semantics: adding a duplicate does nothing
    print("\n--- Set semantics demo ---")
    store.add(":Hanoi", "rdf:type", ":City")  # duplicate
    print(f"After re-adding :Hanoi rdf:type :City → count still = {store.count()}")


def demo_rdflib() -> None:
    """Demonstrate the same domain using RDFLib with proper RDF types."""
    print("\n" + "=" * 60)
    print("PART 2: RDFLib — proper RDF data model")
    print("=" * 60)

    from rdflib import RDF, RDFS, BNode, Graph, Literal, Namespace

    EX = Namespace("http://example.org/")

    g = Graph()
    g.bind("ex", EX)

    # Same domain, but now with proper RDF term types:
    # - EX.Hanoi is an IRI (URIRef)
    # - Literal("Hà Nội") is a literal with datatype xsd:string
    # - RDF.type is the IRI http://www.w3.org/1999/02/22-rdf-syntax-ns#type
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

    print(f"\nTotal triples: {len(g)}")

    # Demonstrate term types
    print("\n--- RDF term types ---")
    for s, p, o in sorted(g):
        print(f"  s={type(s).__name__:8s} p={type(p).__name__:8s} o={type(o).__name__:8s}")
        break  # show one example
    print(f"  Subject EX.Hanoi → IRI: {EX.Hanoi}")
    print(f"  Object Literal('Hà Nội') → Literal, datatype: {Literal('Hà Nội').datatype}")

    # Demonstrate blank node (existential, no global identity)
    print("\n--- Blank node demo ---")
    bnode = BNode()
    g.add((bnode, RDFS.label, Literal("a temporary annotation")))
    print(f"  Added triple with blank node: {bnode}")
    print("  Blank node has no global identity — it is graph-local.")
    print(f"  Graph now has {len(g)} triples.")

    # Graph membership check
    print("\n--- Graph membership ---")
    print(
        f"  (EX.Hanoi, EX.capitalOf, EX.Vietnam) in graph: "
        f"{(EX.Hanoi, EX.capitalOf, EX.Vietnam) in g}"
    )
    print(
        f"  (EX.Paris, EX.sisterCity, EX.Hanoi) in graph: "
        f"{(EX.Paris, EX.sisterCity, EX.Hanoi) in g}"
    )

    # SPARQL query
    print("\n--- SPARQL query ---")
    qres = g.query(
        """
        PREFIX ex: <http://example.org/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?city ?label
        WHERE {
            ?city a ex:City .
            ?city rdfs:label ?label .
        }
        ORDER BY ?city
        """
    )
    for row in qres:
        print(f"  {row.city.split('/')[-1]}: {row.label}")


def main() -> None:
    print("EXPERIMENT 2-1: RDF from First Principles")
    print("Question: What exactly exists in an RDF graph?")
    print()
    demo_pure_python()
    demo_rdflib()

    print("\n" + "=" * 60)
    print("KEY OBSERVATIONS")
    print("=" * 60)
    print("1. An RDF graph is a SET of triples — no duplicates, no ordering.")
    print("2. Each triple has: subject (IRI or blank node),")
    print("   predicate (IRI only), object (IRI, blank node, or literal).")
    print("3. The pure-Python store shows the raw mechanism: strings + set.")
    print("4. RDFLib adds proper term types (IRI, Literal, BNode),")
    print("   namespace management, serialization, and SPARQL.")
    print("5. The RDF data model is ABSTRACT — it is not Turtle, not JSON-LD,")
    print("   not RDF/XML. Those are serializations OF the model.")
    print()
    print("THOUGHT QUESTIONS:")
    print("★ Why can't a literal appear in subject position?")
    print("★★ What is the difference between ':Hanoi' in the pure-Python")
    print("   store and EX.Hanoi in RDFLib?")
    print("★★★ If two RDF graphs contain the same triples, are they the")
    print("    same graph? (See RDF 1.1 Concepts §1.3)")


if __name__ == "__main__":
    main()
