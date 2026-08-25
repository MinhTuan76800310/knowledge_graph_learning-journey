"""Experiment 2-2: Turtle Serialization Round-Trip.

Demonstrates that Turtle is a concrete syntax for RDF, not the data model
itself. An RDF graph can be serialized to Turtle text and parsed back into
a graph-equivalent structure.

Semantic contracts: R11-04 (Turtle 1.1), RL-01 (RDFLib).
Difficulty: ★★
Status: ✅ Independently runnable
"""

from __future__ import annotations


def main() -> None:
    print("=" * 60)
    print("EXPERIMENT 2-2: Turtle Serialization Round-Trip")
    print("=" * 60)

    from rdflib import RDF, RDFS, Graph, Literal, Namespace

    EX = Namespace("http://example.org/")

    # --- Step 1: Build an RDF graph programmatically ---
    print("\n--- Step 1: Build RDF Graph ---")
    g1 = Graph()
    g1.bind("ex", EX)

    g1.add((EX.Hanoi, RDF.type, EX.City))
    g1.add((EX.Hanoi, RDFS.label, Literal("Hà Nội")))
    g1.add((EX.Hanoi, EX.capitalOf, EX.Vietnam))
    g1.add((EX.Hanoi, EX.population, Literal(8418883)))
    g1.add((EX.Paris, RDF.type, EX.City))
    g1.add((EX.Paris, RDFS.label, Literal("Paris")))
    g1.add((EX.Paris, EX.capitalOf, EX.France))
    g1.add((EX.Hanoi, EX.sisterCity, EX.Paris))
    g1.add((EX.Vietnam, RDF.type, EX.Country))
    g1.add((EX.France, RDF.type, EX.Country))

    print(f"Graph 1 triples: {len(g1)}")

    # --- Step 2: Serialize to Turtle ---
    print("\n--- Step 2: Serialize to Turtle ---")
    turtle_text = g1.serialize(format="turtle")
    print(turtle_text)

    # --- Step 3: Parse Turtle back into a new graph ---
    print("--- Step 3: Parse Turtle Back ---")
    g2 = Graph()
    g2.parse(data=turtle_text, format="turtle")
    print(f"Graph 2 triples: {len(g2)}")

    # --- Step 4: Verify graph equivalence ---
    print("\n--- Step 4: Verify Graph Equivalence ---")
    # Compare as sets of triples (graph isomorphism for ground graphs)
    triples_1 = set(g1)
    triples_2 = set(g2)

    if triples_1 == triples_2:
        print("✅ GRAPHS ARE EQUIVALENT: round-trip preserved all triples.")
    else:
        only_in_g1 = triples_1 - triples_2
        only_in_g2 = triples_2 - triples_1
        print("❌ GRAPHS DIFFER:")
        if only_in_g1:
            print(f"  Only in original: {only_in_g1}")
        if only_in_g2:
            print(f"  Only in parsed:   {only_in_g2}")

    # --- Step 5: Show that Turtle is just ONE syntax ---
    print("\n--- Step 5: Same Graph, Different Syntaxes ---")
    ntriples = g1.serialize(format="nt")
    print("N-Triples (first 3 lines):")
    for line in ntriples.strip().split("\n")[:3]:
        print(f"  {line}")

    xml_rdf = g1.serialize(format="xml")
    print(f"\nRDF/XML length: {len(xml_rdf)} chars")
    print("(RDF/XML is verbose but was the original W3C standard syntax)")

    # --- Key Observations ---
    print("\n" + "=" * 60)
    print("KEY OBSERVATIONS")
    print("=" * 60)
    print("1. Turtle is a CONCRETE SYNTAX for RDF, not the data model.")
    print("2. The same RDF graph can be serialized as Turtle, N-Triples,")
    print("   RDF/XML, JSON-LD, etc. — the graph semantics are identical.")
    print("3. Round-trip serialization preserves graph equivalence.")
    print("4. Prefix declarations (@prefix) are syntactic sugar; they do")
    print("   not change the underlying IRIs in the graph.")
    print("5. Comparing raw Turtle strings is WRONG — compare parsed graphs.")

    print("\n--- Thought Questions ---")
    print("★ Why might you choose N-Triples over Turtle for machine processing?")
    print("★★ How does JSON-LD differ from Turtle in its relationship to RDF?")
    print("★★★ Can two syntactically different Turtle documents represent the")
    print("    same RDF graph? Give an example.")


if __name__ == "__main__":
    main()
