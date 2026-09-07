# Chapter 3: Schema, Identity, and Context

## Core Question

How do we establish formal schema constraints, resolve persistent entity identity, and isolate contextual assertions across graphs without logical contradiction?

## Learning Objectives

- Distinguish RDFS deductive typing (generative entailment) from Property Graph schema validation (prescriptive constraints).
- Understand entity identity propagation via `owl:sameAs` and the catastrophic collapse hazard under No Unique Name Assumption (No-UNA).
- Partition quad datasets using Named Graphs and TriG syntax to isolate conflicting observations.
- Model multi-participant relationships using W3C N-ary Relation Pattern 1, RDF Reification, and RDF-star.
- Allow divergent experimental measurements to coexist stably in the Mechanism Knowledge Graph without graph mutation.
- Construct a deterministic Entity Resolution pipeline combining Blocking, Inverse Functional Properties (IFP), and the Fellegi–Sunter 3-zone decision boundary.

## Experiments

| ID | Title | Difficulty | Status | File |
|---|---|:---:|:---:|---|
| 3-1 | RDFS Entailment vs. LPG Schema Constraints | ★★ | ✅ | `exp_3_1_schema_constraints.py` |
| 3-2 | Entity Identity & `owl:sameAs` Information Merging | ★★ | ✅ | `exp_3_2_entity_identity.py` |
| 3-3 | Named Graphs & TriG Quad Datasets | ★★ | ✅ | `exp_3_3_named_graphs.py` |
| 3-4 | N-ary Relations & Reification Patterns | ★★ | ✅ | `exp_3_4_nary_reification.py` |
| 3-5 | Contextual Knowledge Coexistence (Mechanism KG) | ★★ | ✅ | `exp_3_5_context_coexistence.py` |
| 3-6 | Deterministic Entity Resolution Pipeline | ★★★ | ✅ | `exp_3_6_identity_resolution.py` |

## Domain

Two domains:
- The **City/Country domain**: Hanoi, Vietnam, Paris, France, Da Nang.
- The **Mechanism Knowledge Graph** (capstone thread): `datasets/mechanism_kg/rate_of_change.ttl` — physical parameters, thermal conductivity measurements, and operating contexts.

## Running Experiments

```bash
uv run python chapter03/exp_3_1_schema_constraints.py
uv run python chapter03/exp_3_2_entity_identity.py
uv run python chapter03/exp_3_3_named_graphs.py
uv run python chapter03/exp_3_4_nary_reification.py
uv run python chapter03/exp_3_5_context_coexistence.py
uv run python chapter03/exp_3_6_identity_resolution.py
```

## Running Tests

```bash
uv run pytest chapter03/test_ch3_experiments.py -v
```

## Semantic Contracts

See `docs/CHAPTER03_SEMANTIC_CONTRACTS.md` for authoritative formal definitions and constraints.
