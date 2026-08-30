# NEGSAMP-01: Negative Sampling — Distributed Representations of Words and Phrases and their Compositionality

- **Primary reference:** Mikolov, T., Sutskever, I., Chen, K., Corrado, G., Dean, J. (2013). "Distributed Representations of Words and Phrases and their Compositionality." *Advances in Neural Information Processing Systems 26 (NIPS 2013)* (arXiv:1310.4546).
- **URL:** https://arxiv.org/abs/1310.4546
- **Status:** FETCHED_AND_VERIFIED (arXiv abstract page, 2026-08-30)
- **Used in:** Chapter 8

## Key Points (fetched)

- Extends the continuous Skip-gram model to learn better word vectors more quickly, and introduces a method for finding and representing phrases.
- Introduces **negative sampling** as "a simple alternative to the hierarchical softmax": a training objective that "tells observed word-context pairs apart from randomly drawn negative pairs".
- Subsamples frequent words, giving "significant speedup and also learn more regular word representations".
- Origin of the term: negative sampling comes from representation learning (word2vec); the book teaches it as the standard training device for embeddings, and KGE models adopt the same idea (corrupt/randomly draw negatives).

## Semantic Contract

- Negative sampling is a *training procedure*: it constructs assumed-negative examples to shape the decision boundary. It is not a claim that the sampled negatives are false in the world.
- Under OWA a missing triple is not a false triple; using missing triples as sampled negatives is an ML approximation, not a logical negation.
- MUST NOT: say a sampled negative is a verified false statement; say the absence of a triple in the training graph is evidence of falsity (OWA); conflate training negatives with known counterexamples.