# DPR-01: Dense Passage Retrieval (Karpukhin et al., EMNLP 2020)

- **Primary reference:** Karpukhin, V., et al. (2020). Dense Passage Retrieval for Open-Domain Question Answering. EMNLP 2020.
- **URL:** https://arxiv.org/abs/2004.04906
- **Status:** FETCHED_AND_VERIFIED (abstract + paper content read, 2026-08-30)
- **Used in:** Chapter 9
- **Canonical topic:** Dense/vector passage retrieval via dual encoders

## Key Points

- Dual-encoder architecture: query encoder E_Q and passage encoder E_P map texts to d-dimensional vectors; relevance = dot product (or cosine).
- Training: in-batch negatives plus one BM25 hard negative per example; contrastive loss.
- DPR outperforms BM25 by large margins on open-domain QA benchmarks once trained; but BM25 remains a strong lexical baseline, especially for exact terminology.
- Retrieval is decoupled from the reader: retrieve top-k, then a reader (extractive or generative) produces the answer.

## Semantic Contract

- Dense retrieval recovers paraphrase/semantic similarity that lexical matching misses, but embedding similarity is a ranking signal, not a relevance guarantee and not truth.
- The dual-encoder embeddings are learned representations (Ch8: Entity != Embedding applies to passages and queries too).
- MUST NOT: claim dense retrieval always beats lexical retrieval; treat dot-product score as epistemic confidence; conflate query embedding with query meaning.
