# KGQA-01: Neural Question Answering over Knowledge Graphs (Chakraborty et al., 2019)

- **Primary reference:** Chakraborty, N., Lukovnikov, D., Maheshwari, G., Trivedi, P., Lehmann, J. & Fischer, A. (2019). Introduction to Neural Network based Approaches for Question Answering over Knowledge Graphs. arXiv:1907.09361.
- **URL:** https://arxiv.org/abs/1907.09361
- **Status:** FETCHED_AND_VERIFIED (paper content read, 2026-08-30)
- **Used in:** Chapter 9
- **Canonical topic:** KGQA — answering questions over a knowledge graph via query construction or retrieval

## Key Points

- KGQA pipeline: question understanding (entity linking + relation linking) -> query generation (SPARQL or path) -> answer over the KG.
- Paradigms: semantic parsing (symbolic), information-retrieval-based, and embedding-based methods.
- Entity linking and relation linking are core subproblems; errors there propagate downstream.
- KGQA answers by executing/querying a structured store — different mechanism from text retrieval or generative synthesis.

## Semantic Contract

- KGQA != GraphRAG: KGQA answers via structured query/reasoning over the graph; GraphRAG uses graph structure to retrieve/assemble context for generation.
- Exact structured facts are better answered by graph query than by generative RAG.
- MUST NOT: conflate KGQA with RAG; route exact graph queries through an LLM needlessly; skip entity-linking evaluation.
