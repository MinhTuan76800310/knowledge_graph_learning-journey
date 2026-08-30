# HOGAN-IND-01: Knowledge Graphs — Chapter 5 "Inductive Knowledge"

- **Primary reference:** Hogan, A., et al. (2021). *Knowledge Graphs*. Springer. Chapter 5: Inductive Knowledge.
- **URL:** https://kgbook.org/ — chapter source verified via the open HTML edition (raw.githubusercontent.com/Knowledge-Graphs-Book/HTML-Book/main/chapters/05-inductive.php)
- **Status:** FETCHED_AND_VERIFIED (chapter content fetched and read, 2026-08-30)
- **Used in:** Chapter 8
- **Canonical topic:** Inductive knowledge — generalized patterns and their predictions, as opposed to deductive consequences

## Key Points (fetched from the chapter)

- Deductive knowledge is characterized by precise logical consequences; inductive learning "involves generalising patterns from a given set of input observations", yielding "novel but potentially imprecise predictions" assigned confidence levels.
- Inductive knowledge is defined as "both the models used to encode patterns, as well as the predictions made by those models". It is fallible but can be highly valuable.
- The chapter groups techniques by representation and paradigm:
  - **Numeric, unsupervised/self-supervised:** graph analytics and knowledge-graph embeddings (latent feature models).
  - **Numeric, supervised:** graph neural networks.
  - **Symbolic, self-supervised:** symbolic learning, which extracts explicit rules or axioms (observable pattern mining).
- Link prediction: completing missing edge components; embeddings can "complete edges with missing nodes/edge labels for the purposes of link prediction".
- Formal embedding definition: "a knowledge graph embedding of G is a pair of mappings (ε,ρ)"; a "plausibility scoring function is a partial function φ : T × T × T → R". "Edges with higher scores are considered more plausible"; training maximizes scores for positive edges and minimizes them for negative examples.
- Embedding families covered: translational (TransE, TransH, TransR, TransD, RotatE), tensor decomposition (RESCAL, DistMult, HolE, ComplEx, SimplE, TuckER), neural (SME, NTN, MLP, ConvE, HypER).
- Caution example: a capital-city rule with confidence 187/195 ≈ 0.959 still has a counterexample (Vaduz) — "predictions drawn from this pattern do not hold for certain". High confidence is not truth.

## Semantic Contract

- Induction generalizes from observations; its outputs are *candidate* generalizations/predictions, never certain consequences (contrast with deduction).
- A scoring function assigns plausibility only; a high score justifies a candidate, not an assertion.
- Embeddings are one representation family; rule mining is a complementary symbolic family; both are inductive knowledge and both are fallible.
- MUST NOT: equate inductive predictions with entailment; treat a model's confidence as a guarantee; claim embeddings encode the entity's full meaning.