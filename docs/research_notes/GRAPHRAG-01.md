# GRAPHRAG-01: From Local to Global: A Graph RAG Approach (Edge et al., 2024)

- **Primary reference:** Edge, D., et al. (2024). From Local to Global: A Graph RAG Approach to Query-Focused Summarization. arXiv:2404.16130.
- **URL:** https://arxiv.org/abs/2404.16130
- **Status:** FETCHED_AND_VERIFIED (paper content read, 2026-08-30)
- **Used in:** Chapter 9
- **Canonical topic:** GraphRAG — one implementation family of graph-structured retrieval-augmented generation (Microsoft)

## Key Points

- Pipeline: split text into TextUnits -> LLM extracts entities, relationships, and claims -> entity/relation/claim graph -> Leiden community detection -> bottom-up community summaries -> query-time retrieval.
- Two query modes: Global Search (map-reduce over community summaries; for global sensemaking questions) and Local Search (entity-centric fan-out over the graph neighborhood; for entity-specific questions).
- Motivation: conventional RAG fails on global "sensemaking" questions (e.g., "what are the main themes across this corpus?") because those answers require structure across many chunks.
- Community summaries are LLM-generated, derived artifacts; they are NOT the source text.

## Semantic Contract

- GraphRAG is a FAMILY of architectures that use explicit graph structure in retrieval/context construction — NOT one standardized algorithm.
- Microsoft GraphRAG is one concrete implementation; its community-summary approach is one design choice.
- A community summary is a generated/derived artifact with provenance; summary != source truth.
- Graph structure organizes retrieval; it does not guarantee correct entity linking, complete retrieval, or truthful answers.
- MUST NOT: present Microsoft GraphRAG as the definition of GraphRAG; claim GraphRAG eliminates hallucination; treat community summaries as canonical knowledge.
