"""Experiment 2-4: RATE_OF_CHANGE qua RDF + SPARQL.

Loads the canonical running dataset (datasets/mechanism_kg/rate_of_change.ttl)
and runs the four SPARQL queries that anchor Chapter 2's capstone thread:

  - BGP ba-mẫu: đọc ứng dụng n-ary của cơ chế (hasApplication -> differentiand
    / withRespectTo)
  - Bẫy rdf:type: vì sao `?m a ex:Mechanism` không khớp dù cơ chế tồn tại
  - FILTER trên hasValue (giá trị đo là literal có kiểu)
  - OPTIONAL với hasCondition (hành vi phép nối trái)

Console output is ASCII-safe (English) to match sibling experiments; the
pedagogical content lives in the chapter text. UTF-8 Vietnamese is fine in
the docstring.

Semantic contracts: SP11-01 (SPARQL 1.1 Overview), SP11-02 (SPARQL 1.1 Query).
Difficulty: ★★
Status: ✅ Independently runnable
"""

from __future__ import annotations

from pathlib import Path

EX = "http://example.org/kgbook/mks#"


def load_canonical_graph():
    from rdflib import Graph

    dataset = (
        Path(__file__).resolve().parents[1] / "datasets" / "mechanism_kg" / "rate_of_change.ttl"
    )
    g = Graph()
    g.parse(dataset, format="turtle")
    g.bind("ex", EX)
    return g


def main() -> None:
    print("=" * 60)
    print("EXPERIMENT 2-4: RATE_OF_CHANGE via RDF + SPARQL")
    print("=" * 60)

    g = load_canonical_graph()
    print(
        f"\nCanonical graph holds {len(g)} triples "
        f"(source: datasets/mechanism_kg/rate_of_change.ttl)."
    )

    # --- Query 1: n-ary mechanism application (three-pattern BGP) ---
    print("\n--- Query 1: what applications does each mechanism have? ---")
    q1 = f"""
        PREFIX ex: <{EX}>
        SELECT ?mechanism ?applied ?quantity ?wrt
        WHERE {{
            ?mechanism ex:hasApplication ?applied .
            ?applied  ex:differentiand   ?quantity .
            ?applied  ex:withRespectTo   ?wrt .
        }}
    """
    results1 = list(g.query(q1))
    for row in results1:
        print(
            f"  {str(row.mechanism).rsplit('#', 1)[-1]:<18} "
            f"differentiates {str(row.quantity).rsplit('#', 1)[-1]:<14} "
            f"wrt {str(row.wrt).rsplit('#', 1)[-1]}"
        )

    # --- Query 2: rdf:type subclass gap ---
    print("\n--- Query 2: `?m a ex:Mechanism` (expect: empty) ---")
    q2 = f"""
        PREFIX ex: <{EX}>
        SELECT ?m WHERE {{ ?m a ex:Mechanism }}
    """
    results2 = list(g.query(q2))
    print(
        f"  Result: {len(results2)} mappings. rateOfChange_1 is declared "
        f"a ex:RateOfChangeMechanism; plain RDF does no subclass reasoning."
    )
    q2b = f"""
        PREFIX ex: <{EX}>
        SELECT ?m WHERE {{ ?m a ex:RateOfChangeMechanism }}
    """
    results2b = list(g.query(q2b))
    names = sorted(str(row.m).rsplit("#", 1)[-1] for row in results2b)
    print(f"  Using the declared type: {len(results2b)} mechanisms -> {names}")

    # --- Query 3: FILTER over typed literals ---
    print("\n--- Query 3: quantities above the 10-unit threshold ---")
    q3 = f"""
        PREFIX ex: <{EX}>
        SELECT ?q ?v WHERE {{
            ?q ex:hasValue ?v .
            FILTER (?v > 10)
        }}
    """
    results3 = list(g.query(q3))
    for row in sorted(results3, key=lambda r: float(r.v), reverse=True):
        print(f"  {str(row.q).rsplit('#', 1)[-1]} = {float(row.v):g}")

    # --- Query 4: OPTIONAL as left join ---
    print("\n--- Query 4: every mechanism and its condition, if any ---")
    q4 = f"""
        PREFIX ex: <{EX}>
        SELECT ?m ?condition WHERE {{
            ?m a ex:RateOfChangeMechanism .
            OPTIONAL {{ ?m ex:hasCondition ?condition }}
        }}
    """
    results4 = list(g.query(q4))
    for row in results4:
        cond = str(row.condition).rsplit("#", 1)[-1] if row.condition is not None else "(none)"
        print(f"  {str(row.m).rsplit('#', 1)[-1]:<18}  condition: {cond}")

    # --- Key Observations ---
    print("\n" + "=" * 60)
    print("KEY OBSERVATIONS")
    print("=" * 60)
    print("1. A three-pattern BGP reads the whole n-ary application: mechanism ->")
    print("   reified node -> differentiand and withRespectTo. The join lives in the")
    print("   graph body, not in the query text.")
    print("2. `?m a ex:Mechanism` being empty is not a data bug: plain RDF does no")
    print("   subclass reasoning. Query the declared type, or let RDFS/OWL infer")
    print("   (Chapter 5).")
    print("3. FILTER works over typed literals - why hasValue uses xsd:double.")
    print("4. OPTIONAL keeps every left-side solution: a direct instance of LEFT JOIN.")

    print("\n--- Thought Questions ---")
    print("★ Why is hasValue a literal rather than an IRI? What breaks if a value")
    print("  needs history (measured by whom, when, with what error)?")
    print("★★ Adding `?mechanism ex:hasOutput ?output` to Query 1 - what column")
    print("   appears and what is the join key?")
    print("★★★ Which LPG design lets Cypher OPTIONAL MATCH return the same three")
    print("    mechanisms in Query 4 - and what does it cost vs. an intermediate node?")


if __name__ == "__main__":
    main()
