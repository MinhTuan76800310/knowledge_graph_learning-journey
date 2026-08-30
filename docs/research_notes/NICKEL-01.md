# NICKEL-01: A Review of Relational Machine Learning for Knowledge Graphs

- **Primary reference:** Nickel, M., Murphy, K., Tresp, V., Gabrilovich, E. (2016). "A Review of Relational Machine Learning for Knowledge Graphs." *Proceedings of the IEEE*, 104(1), 11–33 (arXiv:1503.00759).
- **URL:** https://arxiv.org/abs/1503.00759
- **Status:** FETCHED_AND_VERIFIED (arXiv abstract page, 2026-08-30)
- **Used in:** Chapter 8

## Key Points (fetched)

- Relational machine learning studies statistical analysis of relational/graph-structured data; "training" statistical models on large knowledge graphs lets them "predict new facts about the world (which is equivalent to predicting new edges in the graph)".
- Two fundamentally different families of statistical relational models, both scalable:
  1. **Latent feature models** — tensor factorization and multiway neural networks (embeddings).
  2. **Observable pattern mining** — mining patterns directly from the graph.
- Combining the two gives "improved modeling power at decreased computational cost".
- Discusses combining such graph models with text-based information extraction for automatically constructing knowledge graphs from the Web (Google Knowledge Vault as an example).
- In the broader literature this review anchors the framing that link prediction = edge prediction, that evaluation compares a model's ranking against held-out triples, and that KGE training relies on negative sampling under the open-world assumption.

## Semantic Contract

- Statistical KG models predict edges; predictions are hypotheses about missing facts, not entailments.
- The two families (latent vs observable/pattern) map to the book's "embedding vs rule induction" pairing; both are inductive knowledge and both are fallible.
- Evaluation is dataset-relative: metrics and splits are conventions, and completeness of the KG is not assumed.
- MUST NOT: claim predictions are truths; claim statistical scores are logical probabilities; treat benchmark numbers as guarantees of knowledge-system quality.