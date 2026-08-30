# SHORTCUT-01: Shortcut Learning in Deep Neural Networks

- **Primary reference:** Geirhos, R., Jacobsen, J.-H., Michaelis, C., Zemel, R., Brendel, W., Bethge, M., Wichmann, F. A. (2020). "Shortcut Learning in Deep Neural Networks." *Nature Machine Intelligence*, 2(11), 665–673 (arXiv:2004.07780).
- **URL:** https://arxiv.org/abs/2004.07780
- **Status:** FETCHED_AND_VERIFIED (arXiv abstract page, 2026-08-30)
- **Used in:** Chapter 8

## Key Points (fetched)

- Many deep-learning problems share a common source: **shortcut learning** — decision strategies that "succeed on typical benchmarks yet break down under harder, real-world conditions".
- Shortcuts are decision rules that "capitalize on superficial or incidental cues instead of the intended, generalizable features of a task".
- Models can "attain high scores on standard benchmarks while still relying on unintended, brittle mechanisms" — strong benchmark performance does not prove the model learned the intended reasoning.
- The authors connect the phenomenon to comparative psychology, education, and linguistics, and propose interpretation and benchmarking recommendations to improve robustness and transfer.

## Semantic Contract

- High in-domain/benchmark accuracy can coexist with wrong mechanism understanding (spurious correlation is the statistical form of shortcut learning).
- Benchmark scores are conditional on the dataset's cues; cross-domain held-out evaluation is needed to expose shortcut reliance.
- MUST NOT: claim high validation accuracy implies the model learned the mechanism; claim a good benchmark proves cross-domain generalization; treat shortcut cues (e.g., physics vocabulary "d/dt") as the mechanism.