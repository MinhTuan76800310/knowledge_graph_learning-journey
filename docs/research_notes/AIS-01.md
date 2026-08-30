# AIS-01: Measuring Attribution in Natural Language Generation Models (Rashkin et al., 2021)

- **Primary reference:** Rashkin, H., et al. (2021). Measuring Attribution in Natural Language Generation Models. arXiv:2112.12870.
- **URL:** https://arxiv.org/abs/2112.12870
- **Status:** FETCHED_AND_VERIFIED (paper content read, 2026-08-30)
- **Used in:** Chapter 9
- **Canonical topic:** Attribution — is generated content supported by identified sources? (AIS)

## Key Points

- AIS (Attributable to Identified Sources): a piece of generated text about the external world is attributable to an identified source if the source provides support for it.
- Two-stage human annotation: (1) identify spans that make claims about the external world, (2) judge whether the cited source supports the claim.
- Applied to conversational QA, summarization, and table-to-text.
- Attribution (to a source) is distinct from factual correctness (the claim is true in the world).

## Semantic Contract

- Groundedness/attribution is a property of the answer-source relationship, not the answer-world relationship.
- A faithfully summarized wrong source is still wrong — grounded != true.
- MUST NOT: treat attribution as truth; skip citation when source supports only part of a claim.
