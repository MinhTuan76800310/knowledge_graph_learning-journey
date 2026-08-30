# MAGRAPH-01: Microsoft GraphRAG Documentation

- **Primary reference:** Microsoft Research. Microsoft GraphRAG Documentation.
- **URL:** https://microsoft.github.io/graphrag/
- **Status:** FETCHED_AND_VERIFIED (documentation read, 2026-08-30)
- **Used in:** Chapter 9
- **Canonical topic:** One concrete GraphRAG implementation family (indexing + query modes)

## Key Points

- Indexing: TextUnits -> LLM extracts entities, relationships, claims -> graph -> Leiden community detection -> bottom-up community summaries.
- Query modes: Global Search (community summaries), Local Search (entity fan-out), DRIFT Search (community context), Basic Search (vector RAG).
- Open-source; documented as a structured, hierarchical approach to RAG.

## Semantic Contract

- This is documentation of ONE implementation family; it does not define universal GraphRAG semantics.
- Indexing produces derived artifacts (community summaries) that need provenance; summary != source.
- MUST NOT: present Microsoft GraphRAG as the standard GraphRAG; claim its community approach is mandatory; treat its summaries as canonical knowledge.
