# RAG-01: Retrieval-Augmented Generation (Lewis et al., NeurIPS 2020)

- **Primary reference:** Lewis, P., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. NeurIPS 2020.
- **URL:** https://arxiv.org/abs/2005.11401
- **Status:** FETCHED_AND_VERIFIED (abstract + paper content read, 2026-08-30)
- **Used in:** Chapter 9
- **Canonical topic:** Retrieval-augmented generation (RAG) — combining a parametric seq2seq generator with a non-parametric dense vector index

## Key Points

- RAG models "combine pre-trained parametric and non-parametric memory for language generation".
- Non-parametric memory = a dense vector index of Wikipedia passages accessed via a neural retriever (DPR-style dual encoders).
- Two formulations: RAG-Sequence (same retrieved passages for the whole sequence) and RAG-Token (re-sample per token).
- Retrieval is treated as a latent variable; the retriever is trained jointly with the generator via the marginal likelihood.
- Evaluated on knowledge-intensive tasks: open-domain QA (Natural Questions, WebQuestions, TriviaQA), fact verification (FEVER), etc.

## Semantic Contract

- RAG is one architecture family for grounding generation in retrieved text; it is NOT the only form of retrieval-augmented generation, and retrieval quality bounds the generator.
- The retriever ranks passages by similarity to the query; a top-k passage is a candidate, not evidence.
- MUST NOT: equate RAG output with entailment; claim retrieval scores are truth probabilities; treat RAG as synonymous with reasoning.
