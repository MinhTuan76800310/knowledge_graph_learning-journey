# Chapter 4: Ontologies and Formal Meaning

## Core Question

How do ontologies provide formal model-theoretic semantics, enable decidable Description Logic reasoning, and allow First-Order query rewriting without relational data materialization?

## Learning Objectives

- Formulate TBox subsumption hierarchies and property domain/range constraints over the Mechanism Knowledge Graph using Description Logics.
- Understand the foundational mechanics of the DL-Lite family and OWL 2 QL: backward-chaining query rewriting of Conjunctive Queries (CQ) into SQL Union of Conjunctive Queries (UCQ) with $\text{AC}^0$ data complexity (OBDA pattern).
- Contrast Open World Assumption (OWA) tri-state valuation (`ENTAILED`, `REFUTED`, `UNKNOWN`) with Closed World Assumption (CWA) binary negation (`True` vs. `False`).
- Differentiate SQL NULL (3-valued relational logic over missing values) from OWL OWA (epistemic openness regarding the domain of discourse).
- Detect formal ontology inconsistency ($\text{Models}(\mathcal{O}) = \emptyset$) triggered by disjoint class clashes ($C \sqcap D \equiv \bot$) and understand the principle of *Ex Falso Quodlibet*.
- Distinguish Class Unsatisfiability (empty class extension in all models) from Ontology Inconsistency (absence of any valid models).

## Experiments

| ID | Title | Difficulty | Status | File |
|---|---|:---:|:---:|---|
| 4-1 | OWL 2 DL Entailment & Subsumption Reasoning | ★★ | ✅ | `exp_4_1_owl_reasoning.py` |
| 4-2 | DL-Lite & First-Order Query Rewriting to SQL | ★★★ | ✅ | `exp_4_2_dl_lite_query_rewriting.py` |
| 4-3 | Open World Assumption (OWA) vs. Disjointness Inconsistency | ★★ | ✅ | `exp_4_3_owa_and_inconsistency.py` |

## Domain

The recurring capstone is the **Mechanism Knowledge Graph**:
- TBox Classes: `Mechanism`, `ChangeMechanism`, `RateOfChangeMechanism`, `AggregationMechanism`, `ReversibleMechanism`, `DissipativeMechanism`.
- ABox Assertions: Differential and aggregation operations, dynamical system properties, and kinetic characteristics.

## Running Experiments

```bash
uv run python chapter04/exp_4_1_owl_reasoning.py
uv run python chapter04/exp_4_2_dl_lite_query_rewriting.py
uv run python chapter04/exp_4_3_owa_and_inconsistency.py
```

## Running Tests

```bash
uv run pytest chapter04/test_ch4_experiments.py -v
```

## Semantic Contracts

See `docs/CHAPTER04_SEMANTIC_CONTRACTS.md` for authoritative formal definitions and constraints against W3C OWL 2 Direct Semantics and DL-Lite literature.
