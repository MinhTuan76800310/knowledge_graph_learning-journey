# NELL-01: Never-Ending Learning (NELL)

- **Primary reference:** Mitchell, T., Cohen, W., Hruschka, E., Talukdar, P., Betteridge, J., Carlson, A., Dalvi, B., Gardner, M., Kisiel, B., Krishnamurthy, J., Lao, N., Mazaitis, K., Mohamed, T., Nakashole, N., Platanios, E., Ritter, A., Samadi, G., Settles, B., Wang, R., Wijaya, D., Gupta, A., Chen, M., Saparov, A., Greaves, M., Welling, J. (2018). "Never-Ending Learning." *Communications of the ACM* 61(5):103–115.
- **DOI:** 10.1145/3191513
- **URL:** https://dl.acm.org/doi/10.1145/3191513
- **Status:** FETCHED_AND_VERIFIED (Crossref metadata verified, 2026-08-31)
- **Used in:** Chapter 10

## Key Points

- Presents the NELL system (Never-Ending Language Learner), which runs continuously to extract knowledge from the web.
- Coupling of learning (extraction) with governance (candidate selection, validation).
- Addresses drift, stale knowledge, and self-training feedback loops.

## Semantic Contract

- Never-ending = continuous operation + self-updating + self-monitoring is the closest existing system to the book's Living Knowledge System concept.
- The book uses NELL to show a deployed continuous-learning system, not as a template (NELL is language-extraction only, not full KG lifecycle).
- MUST NOT: claim NELL implements the book's monitoring loop; NELL's self-validation is limited.