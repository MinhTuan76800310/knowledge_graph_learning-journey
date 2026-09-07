"""Experiment 3-4: N-ary Relations & Reification Patterns.

Question: "How do we represent relations that require metadata, roles, or temporal
qualifiers when RDF natively supports only binary relations (s, p, o)?"

Compares three architectural patterns for qualifying relations:
  1. W3C N-ary Relation Pattern 1 (Qualified Relation / Event Entity):
     Introduces a domain concept (:CapitalStatusAssignment) linking Hanoi, Vietnam,
     time interval, and legal status.
  2. W3C Standard Reification (rdf:Statement):
     Treats the triple itself as a statement object with rdf:subject, rdf:predicate,
     rdf:object, plus custom metadata.
  3. RDF-star / Quoted Triples:
     Direct assertion on a statement: << :Hanoi :capitalOf :Vietnam >> :validFrom 1976.

Semantic contracts: NARY-01 (W3C Working Group Note on N-ary Relations),
R11-02 (RDF 1.1 Concepts §3.3), docs/CHAPTER03_SEMANTIC_CONTRACTS.md §N-ary Relation.
Difficulty: ★★
Status: ✅ Independently runnable
"""

from __future__ import annotations

import sys
from typing import Any

from rdflib import RDF, Graph, Literal, Namespace

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

EX = Namespace("http://example.org/")


def build_pattern1_qualified_relation() -> Graph:
    """Builds W3C N-ary Relation Pattern 1 (Relation as an Entity / Event Node)."""
    g = Graph()
    g.bind("ex", EX)

    # Individual entity nodes
    g.add((EX.Hanoi, RDF.type, EX.City))
    g.add((EX.Vietnam, RDF.type, EX.Country))

    # Intermediate relation instance
    status_node = EX.hanoi_capital_status_1976
    g.add((EX.Hanoi, EX.hasCapitalStatus, status_node))
    g.add((status_node, RDF.type, EX.CapitalStatusAssignment))
    g.add((status_node, EX.forCountry, EX.Vietnam))
    g.add((status_node, EX.validFrom, Literal(1976)))
    g.add((status_node, EX.officialStatus, Literal("Official")))

    return g


def build_pattern2_standard_reification() -> Graph:
    """Builds W3C Standard RDF Reification (rdf:Statement)."""
    g = Graph()
    g.bind("ex", EX)
    g.bind("rdf", RDF)

    # Base statement asserted directly
    g.add((EX.Hanoi, EX.capitalOf, EX.Vietnam))

    # Reified statement describing the assertion
    stmt = EX.statement_hanoi_capital
    g.add((stmt, RDF.type, RDF.Statement))
    g.add((stmt, RDF.subject, EX.Hanoi))
    g.add((stmt, RDF.predicate, EX.capitalOf))
    g.add((stmt, RDF.object, EX.Vietnam))
    g.add((stmt, EX.validFrom, Literal(1976)))
    g.add((stmt, EX.officialStatus, Literal("Official")))

    return g


def build_pattern3_quoted_statement() -> Graph:
    """Builds Pattern 3: Statement Quotation using Notation3 (N3) Quoted Formula."""
    g = Graph()
    g.bind("ex", EX)

    n3_data = """
    @prefix ex: <http://example.org/> .

    { ex:Hanoi ex:capitalOf ex:Vietnam }
        ex:validFrom 1976 ;
        ex:officialStatus "Official" .
    """
    g.parse(data=n3_data, format="n3")
    return g


def query_qualified_relation(g: Graph) -> list[dict[str, Any]]:
    """Query Pattern 1 (Qualified Relation)."""
    q = """
    PREFIX ex: <http://example.org/>
    SELECT ?city ?country ?year ?status
    WHERE {
        ?city ex:hasCapitalStatus ?rel .
        ?rel ex:forCountry ?country ;
             ex:validFrom ?year ;
             ex:officialStatus ?status .
    }
    """
    results = []
    for row in g.query(q):
        results.append(
            {
                "city": str(row.city).split("/")[-1],
                "country": str(row.country).split("/")[-1],
                "validFrom": int(row.year),
                "status": str(row.status),
            }
        )
    return results


def query_standard_reification(g: Graph) -> list[dict[str, Any]]:
    """Query Pattern 2 (Standard Reification)."""
    q = """
    PREFIX ex: <http://example.org/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT ?city ?country ?year ?status
    WHERE {
        ?stmt rdf:type rdf:Statement ;
              rdf:subject ?city ;
              rdf:predicate ex:capitalOf ;
              rdf:object ?country ;
              ex:validFrom ?year ;
              ex:officialStatus ?status .
    }
    """
    results = []
    for row in g.query(q):
        results.append(
            {
                "city": str(row.city).split("/")[-1],
                "country": str(row.country).split("/")[-1],
                "validFrom": int(row.year),
                "status": str(row.status),
            }
        )
    return results


def main() -> None:
    print("=" * 60)
    print("EXPERIMENT 3-4: N-ARY RELATIONS & REIFICATION PATTERNS")
    print("=" * 60)

    g1 = build_pattern1_qualified_relation()
    g2 = build_pattern2_standard_reification()
    g3 = build_pattern3_quoted_statement()

    print(f"\nPattern 1 (Qualified Relation):   {len(g1)} triples")
    print(f"Pattern 2 (RDF Reification):       {len(g2)} triples")
    print(f"Pattern 3 (N3 Quoted Statement):   {len(g3)} statements")

    print("\n--- Query Output for Pattern 1 (Qualified Relation) ---")
    res1 = query_qualified_relation(g1)
    print(f"  Result: {res1}")

    print("\n--- Query Output for Pattern 2 (Standard Reification) ---")
    res2 = query_standard_reification(g2)
    print(f"  Result: {res2}")

    assert res1 == res2, "Semantic divergence between Pattern 1 and Pattern 2!"
    print("\n[OK] Semantic Equivalence Confirmed between Qualified Relation & Reification.")

    print("\n--- Structural Comparison ---")
    print("  1. Qualified Relation (W3C Pattern 1):")
    print("     - Clear domain modeling (e.g., CapitalStatusAssignment).")
    print("     - First-class citizen in OWL DL reasoners.")
    print("  2. Standard Reification:")
    print("     - Generic vocab (rdf:Statement), but high triple bloat (5 triples/fact).")
    print("     - No built-in entailment connecting the reification to the asserted triple.")
    print("  3. RDF-star:")
    print("     - Compact syntax; avoids proliferating intermediate node IRIs.")


if __name__ == "__main__":
    main()
