"""Experiment 4-2: DL-Lite & First-Order Query Rewriting to SQL (OWL 2 QL / OBDA).

Demonstrates the foundational principle of OWL 2 QL and the DL-Lite family:
1. First-Order Rewritability (FO-Rewritability): A Conjunctive Query (CQ) posed
   over an ontology can be rewritten against TBox axioms into a Union of
   Conjunctive Queries (UCQ) expressed as standard SQL.
2. AC^0 Data Complexity: Query answering requires zero ABox materialization;
   inference work is delegated to the relational database engine.
3. OBDA (Ontology-Based Data Access): Maps relational tables to ontology classes
   and evaluates rewritten queries over dynamic relational storage.

Manuscript Line Anchors:
- book/chapter04.md:1283, 1289-1294, 1308-1311, 1740
Semantic Contracts:
- docs/CHAPTER04_SEMANTIC_CONTRACTS.md: OWL Profiles (QL) (§OWL Profiles),
  OWL 2 DL = SROIQ(D) and the Complexity Spectrum (§Complexity Spectrum).
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass, field
from typing import Any

from rdflib import RDF, RDFS, Graph, Namespace

EX = Namespace("http://example.org/mechanism#")


@dataclass
class TBoxInclusion:
    """Represents an inclusion axiom in DL-Lite.

    Supports:
      - Concept Subsumption: sub_concept ⊑ super_concept
      - Role Domain: exists_role ⊑ super_concept (∃R ⊑ C)
    """

    sub_concept: str
    super_concept: str
    is_role_domain: bool = False  # If True, sub_concept is role R, meaning ∃R ⊑ super_concept


@dataclass
class RelationalMapping:
    """Maps an ontology concept or role to an SQL query over relational tables."""

    target_concept_or_role: str
    sql_select_id: str
    sql_from_table: str
    id_column: str
    label_column: str | None = None
    is_binary_role: bool = False
    source_col: str | None = None
    target_col: str | None = None


class DLLiteQueryRewriter:
    """A backward-chaining query rewriting engine for DL-Lite / OWL 2 QL."""

    def __init__(self) -> None:
        self.inclusions: list[TBoxInclusion] = []
        self.mappings: dict[str, RelationalMapping] = {}

    def add_subclass_axiom(self, sub_class: str, super_class: str) -> None:
        """Assert TBox axiom: SubClass ⊑ SuperClass."""
        self.inclusions.append(
            TBoxInclusion(sub_concept=sub_class, super_concept=super_class, is_role_domain=False)
        )

    def add_role_domain_axiom(self, role: str, super_class: str) -> None:
        """Assert TBox axiom: ∃Role ⊑ SuperClass."""
        self.inclusions.append(
            TBoxInclusion(sub_concept=role, super_concept=super_class, is_role_domain=True)
        )

    def register_mapping(self, mapping: RelationalMapping) -> None:
        """Register a mapping between relational table and ontology entity."""
        self.mappings[mapping.target_concept_or_role] = mapping

    def rewrite_concept_query(self, target_concept: str) -> list[str]:
        """Backward-chaining rewriting of target_concept(x) against TBox inclusions.

        Produces a Union of Conjunctive Queries (UCQ) represented as a list of concept/role atoms.
        """
        frontier = [target_concept]
        visited_atoms: set[str] = set()
        ucq_atoms: list[str] = []

        while frontier:
            current = frontier.pop(0)
            if current in visited_atoms:
                continue
            visited_atoms.add(current)
            ucq_atoms.append(current)

            # Find all TBox inclusions where current is the super_concept
            for inc in self.inclusions:
                if inc.super_concept == current:
                    if inc.is_role_domain:
                        role_atom = f"exists_{inc.sub_concept}"
                        if role_atom not in visited_atoms:
                            visited_atoms.add(role_atom)
                            ucq_atoms.append(role_atom)
                    else:
                        if inc.sub_concept not in visited_atoms:
                            frontier.append(inc.sub_concept)

        return ucq_atoms

    def generate_sql(self, target_concept: str) -> str:
        """Translate rewritten UCQ into an executable SQL UNION query."""
        ucq_atoms = self.rewrite_concept_query(target_concept)
        sql_selects: list[str] = []

        for atom in ucq_atoms:
            if atom.startswith("exists_"):
                role_name = atom[len("exists_") :]
                mapping = self.mappings.get(role_name)
                if mapping and mapping.is_binary_role and mapping.source_col:
                    sql_selects.append(
                        f"SELECT {mapping.source_col} AS id, "
                        f"'SubpartParent:' || {mapping.source_col} AS label "
                        f"FROM {mapping.sql_from_table}"
                    )
            else:
                mapping = self.mappings.get(atom)
                if mapping:
                    label_expr = mapping.label_column if mapping.label_column else f"'{atom}'"
                    sql_selects.append(
                        f"SELECT {mapping.id_column} AS id, {label_expr} AS label "
                        f"FROM {mapping.sql_from_table}"
                    )

        if not sql_selects:
            raise ValueError(f"No relational mappings found for concept {target_concept}")

        # Combine via SQL UNION (automatic set deduplication)
        return "\nUNION\n".join(sql_selects) + "\nORDER BY id;"


@dataclass
class SQLiteMechanismStore:
    """Manages an in-memory SQLite database simulating normalized relational storage."""

    connection: sqlite3.Connection = field(default_factory=lambda: sqlite3.connect(":memory:"))

    def initialize_schema_and_data(self) -> None:
        """Populate database with normalized Mechanism tables."""
        cur = self.connection.cursor()

        # 1. Base mechanisms table
        cur.execute("""
            CREATE TABLE mechanisms (
                id TEXT PRIMARY KEY,
                label TEXT NOT NULL
            );
        """)
        # 2. Rate of change mechanisms table (specialized subclass)
        cur.execute("""
            CREATE TABLE rate_of_change_mechanisms (
                id TEXT PRIMARY KEY,
                label TEXT NOT NULL,
                derivative_order INT NOT NULL
            );
        """)
        # 3. Aggregation mechanisms table (specialized subclass)
        cur.execute("""
            CREATE TABLE aggregation_mechanisms (
                id TEXT PRIMARY KEY,
                label TEXT NOT NULL,
                aggregation_op TEXT NOT NULL
            );
        """)
        # 4. Mechanism subparts table (binary relation)
        cur.execute("""
            CREATE TABLE mechanism_subparts (
                parent_id TEXT NOT NULL,
                child_id TEXT NOT NULL,
                PRIMARY KEY (parent_id, child_id)
            );
        """)

        # Insert sample rows
        cur.execute("INSERT INTO mechanisms VALUES ('mech_00', 'General Homeostasis');")
        cur.execute(
            "INSERT INTO rate_of_change_mechanisms VALUES ('mech_01', 'Velocity Differential', 1);"
        )
        cur.execute(
            "INSERT INTO rate_of_change_mechanisms VALUES "
            "('mech_02', 'Acceleration Differential', 2);"
        )
        cur.execute(
            "INSERT INTO aggregation_mechanisms VALUES "
            "('mech_03', 'Weighted Sum Aggregator', 'SUM');"
        )
        cur.execute("INSERT INTO mechanism_subparts VALUES ('mech_04', 'mech_01');")

        self.connection.commit()

    def query_naive_mechanisms(self) -> list[tuple[str, str]]:
        """Run un-rewritten naive query over the base table alone."""
        cur = self.connection.cursor()
        cur.execute("SELECT id, label FROM mechanisms ORDER BY id;")
        return cur.fetchall()

    def query_rewritten_sql(self, sql: str) -> list[tuple[str, str]]:
        """Run rewritten UCQ SQL query."""
        cur = self.connection.cursor()
        cur.execute(sql)
        return cur.fetchall()


def build_materialized_rdf_baseline() -> set[str]:
    """Compute materialized deductive closure using RDFLib to benchmark answers."""
    import owlrl

    g = Graph()
    g.add((EX.Mechanism, RDF.type, RDFS.Class))
    g.add((EX.ChangeMechanism, RDF.type, RDFS.Class))
    g.add((EX.RateOfChangeMechanism, RDF.type, RDFS.Class))
    g.add((EX.AggregationMechanism, RDF.type, RDFS.Class))

    g.add((EX.ChangeMechanism, RDFS.subClassOf, EX.Mechanism))
    g.add((EX.RateOfChangeMechanism, RDFS.subClassOf, EX.ChangeMechanism))
    g.add((EX.AggregationMechanism, RDFS.subClassOf, EX.Mechanism))

    g.add((EX.hasSubPart, RDF.type, RDF.Property))
    g.add((EX.hasSubPart, RDFS.domain, EX.Mechanism))

    # ABox facts matching database
    g.add((EX.mech_00, RDF.type, EX.Mechanism))
    g.add((EX.mech_01, RDF.type, EX.RateOfChangeMechanism))
    g.add((EX.mech_02, RDF.type, EX.RateOfChangeMechanism))
    g.add((EX.mech_03, RDF.type, EX.AggregationMechanism))
    g.add((EX.mech_04, EX.hasSubPart, EX.mech_01))

    # Compute closure
    owlrl.DeductiveClosure(owlrl.RDFS_OWLRL_Semantics).expand(g)

    # SPARQL query for all instances of Mechanism
    results = g.query("""
        PREFIX ex: <http://example.org/mechanism#>
        SELECT DISTINCT ?m WHERE {
            ?m a ex:Mechanism .
        }
    """)

    ids = set()
    for row in results:
        uri = str(row[0])  # type: ignore[index]
        if "#" in uri:
            ids.add(uri.split("#")[1])
    return ids


def run_experiment() -> dict[str, Any]:
    """Execute Experiment 4-2 end-to-end and assert semantic equivalence."""
    db = SQLiteMechanismStore()
    db.initialize_schema_and_data()

    rewriter = DLLiteQueryRewriter()

    # TBox Axioms:
    # RateOfChangeMechanism ⊑ ChangeMechanism ⊑ Mechanism
    # AggregationMechanism ⊑ Mechanism
    # ∃hasSubPart ⊑ Mechanism
    rewriter.add_subclass_axiom("RateOfChangeMechanism", "ChangeMechanism")
    rewriter.add_subclass_axiom("ChangeMechanism", "Mechanism")
    rewriter.add_subclass_axiom("AggregationMechanism", "Mechanism")
    rewriter.add_role_domain_axiom("hasSubPart", "Mechanism")

    # Mappings to SQLite tables:
    rewriter.register_mapping(
        RelationalMapping(
            target_concept_or_role="Mechanism",
            sql_select_id="id",
            sql_from_table="mechanisms",
            id_column="id",
            label_column="label",
        )
    )
    rewriter.register_mapping(
        RelationalMapping(
            target_concept_or_role="RateOfChangeMechanism",
            sql_select_id="id",
            sql_from_table="rate_of_change_mechanisms",
            id_column="id",
            label_column="label",
        )
    )
    rewriter.register_mapping(
        RelationalMapping(
            target_concept_or_role="AggregationMechanism",
            sql_select_id="id",
            sql_from_table="aggregation_mechanisms",
            id_column="id",
            label_column="label",
        )
    )
    rewriter.register_mapping(
        RelationalMapping(
            target_concept_or_role="hasSubPart",
            sql_select_id="parent_id",
            sql_from_table="mechanism_subparts",
            id_column="parent_id",
            is_binary_role=True,
            source_col="parent_id",
            target_col="child_id",
        )
    )

    # 1. Evaluate Naive Query
    naive_results = db.query_naive_mechanisms()
    naive_ids = {r[0] for r in naive_results}

    # 2. Perform DL-Lite Query Rewriting to SQL UCQ
    ucq_atoms = rewriter.rewrite_concept_query("Mechanism")
    generated_sql = rewriter.generate_sql("Mechanism")
    rewritten_results = db.query_rewritten_sql(generated_sql)
    rewritten_ids = {r[0] for r in rewritten_results}

    # 3. Ground Truth from RDF Materialization
    materialized_rdf_ids = build_materialized_rdf_baseline()

    # 4. Verify Equivalence
    is_equivalent_to_materialization = rewritten_ids == materialized_rdf_ids
    naive_has_false_negatives = naive_ids < materialized_rdf_ids

    return {
        "ucq_atoms": ucq_atoms,
        "generated_sql": generated_sql,
        "naive_count": len(naive_ids),
        "rewritten_count": len(rewritten_ids),
        "materialized_rdf_count": len(materialized_rdf_ids),
        "naive_missed_ids": sorted(materialized_rdf_ids - naive_ids),
        "is_equivalent_to_materialization": is_equivalent_to_materialization,
        "naive_has_false_negatives": naive_has_false_negatives,
        "all_retrieved_ids": sorted(rewritten_ids),
    }


def main() -> None:
    """Execute Experiment 4-2 demonstration."""
    print("=" * 70)
    print("EXP-4-2: DL-Lite & First-Order Query Rewriting to SQL (OWL 2 QL)")
    print("=" * 70)

    res = run_experiment()
    print("\n[1] Rewritten UCQ Concept/Role Atoms:")
    for atom in res["ucq_atoms"]:
        print(f"  - {atom}")

    print("\n[2] Generated SQL UCQ (delegated to RDBMS engine):")
    print(res["generated_sql"])

    print("\n[3] Comparison:")
    missed = res["naive_missed_ids"]
    print(f"  Naive SQL Query Matches:          {res['naive_count']} items (Missed: {missed})")
    retrieved = res["all_retrieved_ids"]
    print(f"  Rewritten SQL UCQ Matches:        {res['rewritten_count']} items {retrieved}")
    print(f"  Materialized RDF Baseline Matches:{res['materialized_rdf_count']} items")
    print(f"  100% Semantic Equivalence:        {res['is_equivalent_to_materialization']}")
    print("  Zero In-Place DB Materialization: True (Database schema remains unaltered)")


if __name__ == "__main__":
    main()
