# CALIB-01: On Calibration of Modern Neural Networks

- **Primary reference:** Guo, C., Pleiss, G., Sun, Y., Weinberger, K. Q. (2017). "On Calibration of Modern Neural Networks." *Proceedings of the 34th International Conference on Machine Learning (ICML 2017)* (arXiv:1706.04599).
- **URL:** https://arxiv.org/abs/1706.04599
- **Status:** FETCHED_AND_VERIFIED (arXiv abstract page, 2026-08-30)
- **Used in:** Chapter 8

## Key Points (fetched)

- Defines confidence calibration as "predicting probability estimates representative of the true correctness likelihood".
- Finds that "modern neural networks, unlike those from a decade ago, are poorly calibrated" and often overconfident even when accuracy is high; depth, width, weight decay and Batch Normalization affect calibration.
- Introduces Expected Calibration Error (ECE): bins predictions by confidence and compares predicted confidence with observed accuracy within each bin.
- **Temperature scaling** — a single-parameter variant of Platt scaling applied to logits — "surprisingly effective at calibrating predictions", with little or no change to accuracy.

## Semantic Contract

- A model's self-reported score (logit, softmax, ranking score, or calibrated probability) is not automatically the probability of truth.
- The book distinguishes: logit → ranking score → model probability → calibrated probability → epistemic claim confidence (Ch6). Only after an explicit Assessment object with defined score semantics may a score be used.
- Calibration is a property of the model's error statistics on a dataset; it does not turn predictions into truths.
- MUST NOT: use an ML score as Chapter 6 confidence without an Assessment object; claim a 0.9 softmax means 90% truth probability; say calibration proves correctness.