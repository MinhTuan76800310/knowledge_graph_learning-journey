# RRANK-01: Passage Re-ranking with BERT (Nogueira & Cho, 2019)

- **Primary reference:** Nogueira, R. & Cho, K. (2019). Passage Re-ranking with BERT. arXiv:1901.04085.
- **URL:** https://arxiv.org/abs/1901.04085
- **Status:** FETCHED_AND_VERIFIED (paper content read, 2026-08-30)
- **Used in:** Chapter 9
- **Canonical topic:** Two-stage retrieval: broad first stage + precise re-ranker

## Key Points

- First stage: cheap, high-recall retrieval (BM25) produces a candidate pool (e.g., top 1000).
- Second stage: a cross-encoder (BERT) scores each query-passage pair jointly and re-ranks the pool.
- Cross-encoder sees query and passage together — more powerful than dot-product dual encoders, but must be run per pair (slower).
- Achieved SOTA on TREC-CAR and MS MARCO passage re-ranking at the time.

## Semantic Contract

- Re-ranking improves ranking quality over the candidate pool; it cannot recover documents the first stage never retrieved.
- Re-ranker scores are ranking signals, not truth or confidence.
- MUST NOT: claim re-ranking guarantees correctness; skip the first stage and expect re-ranker recall; treat re-ranker score as evidence strength.
