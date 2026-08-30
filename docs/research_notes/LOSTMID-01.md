# LOSTMID-01: Lost in the Middle: How Language Models Use Long Contexts (Liu et al., 2024)

- **Primary reference:** Liu, N.F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F. & Liang, P. (2024). Lost in the Middle: How Language Models Use Long Contexts. TACL 12, 157-173.
- **URL:** https://arxiv.org/abs/2307.03172
- **Status:** FETCHED_AND_VERIFIED (paper content read, 2026-08-30)
- **Used in:** Chapter 9
- **Canonical topic:** Context-position effects in long-context LLMs

## Key Points

- LLMs (even long-context models) use relevant information at the START and END of the context more reliably than information in the middle.
- Performance drops substantially when the relevant passage is placed in the middle of a long context.
- Implication: context assembly is a reasoning interface — order/placement matters — not mere concatenation.

## Semantic Contract

- Findings are empirical on specific models/tasks; do not overstate as a universal law, but the engineering consequence is real: assembly order affects answer quality.
- MUST NOT: claim all models suffer equally; use the paper to justify arbitrary reordering claims; treat placement as a correctness mechanism rather than a reliability factor.
