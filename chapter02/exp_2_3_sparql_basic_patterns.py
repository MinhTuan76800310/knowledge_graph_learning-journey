"""Experiment 2-3: SPARQL Basic Graph Patterns.

Demonstrates how SPARQL graph pattern matching answers questions about
an RDF graph. Covers SELECT, variables, triple patterns, and solution mappings.

Semantic contracts: SP11-01 (SPARQL 1.1 Overview), SP11-02 (SPARQL 1.1 Query).
Difficulty: ★★
Status: ✅ Independently runnable
"""

from __future__ import annotations


def main() -> None:
    print("=" * 60)
    print("EXPERIMENT 2-3: SPARQL Basic Graph Patterns")
    print("=" * 60)

    from rdflib import RDF, RDFS, Graph, Literal, Namespace

    EX = Namespace("http://example.org/")

    # Build the same domain graph as experiments 2-1 and 2-2
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

    print(f"\nGraph contains {len(g)} triples.")

    # --- Query 1: Simple triple pattern ---
    print("\n--- Query 1: Find all cities ---")
    q1 = """
        PREFIX ex: <http://example.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT ?city
        WHERE {
            ?city rdf:type ex:City .
        }
    """
    results1 = list(g.query(q1))
    print(f"Solution mappings ({len(results1)}):")
    for row in results1:
        print(f"  ?city = {row.city}")

    # --- Query 2: Two-variable pattern ---
    print("\n--- Query 2: Cities and their labels ---")
    q2 = """
        PREFIX ex: <http://example.org/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT ?city ?label
        WHERE {
            ?city rdf:type ex:City .
            ?city rdfs:label ?label .
        }
        ORDER BY ?city
    """
    results2 = list(g.query(q2))
    print(f"Solution mappings ({len(results2)}):")
    for row in results2:
        city_name = str(row.city).split("/")[-1]
        print(f"  ?city = {city_name}, ?label = '{row.label}'")

    # --- Query 3: Multi-triple pattern (join) ---
    print("\n--- Query 3: Capitals of countries ---")
    q3 = """
        PREFIX ex: <http://example.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT ?capital ?country
        WHERE {
            ?capital ex:capitalOf ?country .
            ?country rdf:type ex:Country .
        }
    """
    results3 = list(g.query(q3))
    print(f"Solution mappings ({len(results3)}):")
    for row in results3:
        cap = str(row.capital).split("/")[-1]
        cty = str(row.country).split("/")[-1]
        print(f"  ?capital = {cap}, ?country = {cty}")

    # --- Query 4: Filter with literal comparison ---
    print("\n--- Query 4: Cities with population > 5,000,000 ---")
    q4 = """
        PREFIX ex: <http://example.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT ?city ?pop
        WHERE {
            ?city rdf:type ex:City .
            ?city ex:population ?pop .
            FILTER (?pop > 5000000)
        }
    """
    results4 = list(g.query(q4))
    print(f"Solution mappings ({len(results4)}):")
    for row in results4:
        city_name = str(row.city).split("/")[-1]
        print(f"  ?city = {city_name}, ?pop = {row.pop}")

    # --- Query 5: Optional pattern ---
    print("\n--- Query 5: All entities with optional labels ---")
    q5 = """
        PREFIX ex: <http://example.org/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?entity ?label
        WHERE {
            ?entity a ?type .
            OPTIONAL { ?entity rdfs:label ?label }
        }
        ORDER BY ?entity
    """
    results5 = list(g.query(q5))
    print(f"Solution mappings ({len(results5)}):")
    for row in results5:
        entity = str(row.entity).split("/")[-1]
        label = row.label if row.label is not None else "(no label)"
        print(f"  ?entity = {entity}, ?label = {label}")

    # --- Key Observations ---
    print("\n" + "=" * 60)
    print("KEY OBSERVATIONS")
    print("=" * 60)
    print("1. SPARQL matches GRAPH PATTERNS, not rows in tables.")
    print("2. Variables (?x) bind to graph nodes in solution mappings.")
    print("3. A Basic Graph Pattern (BGP) is a set of triple patterns.")
    print("4. Multiple triple patterns join on shared variables.")
    print("5. FILTER restricts solutions; OPTIONAL extends them.")
    print("6. SPARQL is NOT 'SQL for graphs' — it operates on graph")
    print("   structure, not relational tables.")

    print("\n--- Thought Questions ---")
    print("★ How does SPARQL's variable binding differ from SQL's column")
    print("  selection?")
    print("★★ What happens when an OPTIONAL pattern has no match? Does the")
    print("   entire solution disappear?")
    print("★★★ Can you write a SPARQL query that finds sister-city pairs")
    print("    where both cities are capitals?")


if __name__ == "__main__":
    main()
