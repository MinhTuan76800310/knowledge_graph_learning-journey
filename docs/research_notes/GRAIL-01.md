# GRAIL-01: GraIL — Inductive Relation Prediction by Subgraph Reasoning

- **Primary reference:** Teru, K. K., Denis, E., Hamilton, W. L. (2020). "Inductive Relation Prediction by Subgraph Reasoning." *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)* (arXiv:1911.06962).
- **URL:** https://arxiv.org/abs/1911.06962
- **Status:** FETCHED_AND_VERIFIED (arXiv API metadata + abstract, 2026-08-30)
- **Used in:** Chapter 8

## Key Points (fetched)

- Introduces GraIL, a graph neural network that infers relations from local subgraphs and learns relational semantics "without depending on specific entities".
- In contrast to embedding-based approaches, it "generalizes inductively to unseen entities and graphs" — exactly the inductive setting the Mechanism System needs for new applications/quantities/domains.
- Approach: for a candidate triple (h, r, t), extract the enclosing subgraph between h and t (bounded hops), label nodes by distance from h/t, and run a GNN that produces a score for the triple. Because node identity is not used (no per-entity embedding lookup), entirely new entities are handled at test time.
- Theoretical + empirical support that the subgraph model "captures a meaningful portion of first-order logic"; gains over rule-induction baselines in inductive settings, and improvements when ensembled with embedding methods.

## Semantic Contract

- Inductive (as in "inductive KG learning") = generalization to entities/subgraphs never seen in training. This is distinct from the *transductive* setting where test entities were present at training time.
- Entity-ID embeddings alone cannot represent unseen entities; structure/neighborhood-based encoders (subgraph GNNs) are one way to get representations for new entities.
- A model that works on unseen entities still produces candidate predictions, not facts.
- MUST NOT: call every KGE "inductive"; claim subgraph similarity proves identity or same mechanism.