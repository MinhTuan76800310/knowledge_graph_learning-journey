"""Experiment 3-5: Contextual Knowledge Coexistence.

Question: "How do conflicting physical measurements and parameter values coexist
in the Mechanism Knowledge Graph without producing contradiction or requiring destructive mutation?"

Demonstrates:
  1. The Context Collision problem: In real physical systems, parameters
     (e.g., thermal conductivity, rate of change, viscosity) depend on operating conditions.
     Uncontextualized binary triples produce irreconcilable clashes.
  2. The Contextualization Pattern: Linking measurements to an explicit
     ex:MeasurementContext node specifying temperature, pressure, and measurement protocol.
  3. Condition-conditioned SPARQL queries: Retrieving parameter values valid for
     room temperature (293 K) vs. elevated temperature (353 K) from the same unmutated graph.

Semantic contracts: docs/CHAPTER03_SEMANTIC_CONTRACTS.md §Context,
MECHANISM_KG_CANONICAL_MODEL.md.
Difficulty: ★★
Status: ✅ Independently runnable
"""

from __future__ import annotations

import sys
from typing import Any

from rdflib import RDF, RDFS, XSD, Graph, Literal, Namespace

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

EX = Namespace("http://example.org/kgbook/mks#")


def build_contextual_mechanism_graph() -> Graph:
    """Constructs a mechanism graph where thermal conductivity measurements

    coexist peacefully under distinct experimental conditions.
    """
    g = Graph()
    g.bind("ex", EX)
    g.bind("xsd", XSD)

    # 1. Physical Quantity
    g.add((EX.water_sample_1, RDF.type, EX.PhysicalSubstance))
    g.add((EX.water_sample_1, RDFS.label, Literal("Pure H2O Specimen")))

    # 2. Context 1: Room Temperature (293.15 K, 1.0 atm)
    ctx1 = EX.context_room_temp
    g.add((ctx1, RDF.type, EX.ExperimentalContext))
    g.add((ctx1, EX.temperatureKelvin, Literal(293.15, datatype=XSD.double)))
    g.add((ctx1, EX.pressureAtm, Literal(1.0, datatype=XSD.double)))
    g.add((ctx1, EX.method, Literal("Transient Hot Wire")))

    meas1 = EX.meas_k_room
    g.add((meas1, RDF.type, EX.PhysicalMeasurement))
    g.add((meas1, EX.targetSubstance, EX.water_sample_1))
    g.add((meas1, EX.parameterName, Literal("ThermalConductivity")))
    g.add((meas1, EX.measuredValue, Literal(0.598, datatype=XSD.double)))
    g.add((meas1, EX.unit, Literal("W/(m*K)")))
    g.add((meas1, EX.conditionedOn, ctx1))

    # 3. Context 2: Elevated Temperature (353.15 K, 1.0 atm)
    ctx2 = EX.context_elevated_temp
    g.add((ctx2, RDF.type, EX.ExperimentalContext))
    g.add((ctx2, EX.temperatureKelvin, Literal(353.15, datatype=XSD.double)))
    g.add((ctx2, EX.pressureAtm, Literal(1.0, datatype=XSD.double)))
    g.add((ctx2, EX.method, Literal("Transient Hot Wire")))

    meas2 = EX.meas_k_elevated
    g.add((meas2, RDF.type, EX.PhysicalMeasurement))
    g.add((meas2, EX.targetSubstance, EX.water_sample_1))
    g.add((meas2, EX.parameterName, Literal("ThermalConductivity")))
    g.add((meas2, EX.measuredValue, Literal(0.670, datatype=XSD.double)))
    g.add((meas2, EX.unit, Literal("W/(m*K)")))
    g.add((meas2, EX.conditionedOn, ctx2))

    return g


def query_measurement_by_temperature(g: Graph, temp_kelvin: float) -> list[dict[str, Any]]:
    """Query conductivity value conditioned on a specific operating temperature."""
    q = f"""
    PREFIX ex: <http://example.org/kgbook/mks#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    SELECT ?substance ?param ?val ?unit ?temp
    WHERE {{
        ?meas a ex:PhysicalMeasurement ;
              ex:targetSubstance ?substance ;
              ex:parameterName ?param ;
              ex:measuredValue ?val ;
              ex:unit ?unit ;
              ex:conditionedOn ?ctx .
        ?ctx ex:temperatureKelvin ?temp .
        FILTER (abs(?temp - {temp_kelvin}) < 0.1)
    }}
    """
    results = []
    for row in g.query(q):
        results.append(
            {
                "substance": str(row.substance).split("#")[-1],
                "parameter": str(row.param),
                "value": float(row.val),
                "unit": str(row.unit),
                "temperature": float(row.temp),
            }
        )
    return results


def main() -> None:
    print("=" * 60)
    print("EXPERIMENT 3-5: CONTEXTUAL KNOWLEDGE COEXISTENCE")
    print("=" * 60)

    g = build_contextual_mechanism_graph()
    print(f"\nContextual Mechanism Graph loaded with {len(g)} triples.")

    # 1. Query room temperature context
    print("\n--- 1. Querying Measurement at Room Temperature (293.15 K) ---")
    res_room = query_measurement_by_temperature(g, 293.15)
    for r in res_room:
        print(
            f"  {r['substance']} {r['parameter']} = {r['value']} {r['unit']} "
            f"at T={r['temperature']} K"
        )

    # 2. Query elevated temperature context
    print("\n--- 2. Querying Measurement at Elevated Temperature (353.15 K) ---")
    res_elev = query_measurement_by_temperature(g, 353.15)
    for r in res_elev:
        print(
            f"  {r['substance']} {r['parameter']} = {r['value']} {r['unit']} "
            f"at T={r['temperature']} K"
        )

    print("\n--- 3. Verifying Non-Mutation & Coexistence ---")
    total_meas = len(list(g.triples((None, EX.measuredValue, None))))
    print(f"  Total measurements coexisting in graph: {total_meas}")
    assert len(res_room) == 1 and len(res_elev) == 1
    assert res_room[0]["value"] != res_elev[0]["value"]
    print("  [PASSED] Multiple divergent values coexist with explicit environmental scope.")


if __name__ == "__main__":
    main()
