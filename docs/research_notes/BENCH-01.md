# BENCH-01: Do ImageNet Classifiers Generalize to ImageNet?

- **Primary reference:** Recht, B., Roelofs, R., Schmidt, L., Shankar, V. (2019). "Do ImageNet Classifiers Generalize to ImageNet?" *Proceedings of the 36th International Conference on Machine Learning (ICML 2019)*, PMLR 97.
- **URL:** https://proceedings.mlr.press/v97/recht19a.html
- **Status:** FETCHED_AND_VERIFIED (PMLR page fetched, abstract verified, 2026-08-31)
- **Used in:** Chapter 10

## Key Points

- Constructed new test sets for ImageNet and CIFAR-10 using the original dataset-creation procedure.
- Found accuracy drops of 11–14% (ImageNet) and 3–15% (CIFAR-10) across many models.
- Argues drops are not due to overfitting to the original test set but to models failing to generalize to slightly harder images.

## Semantic Contract

- The book uses this to demonstrate benchmark decay as a separate problem from knowledge degradation.
- A benchmark score is not the same as system quality.
- MUST NOT: claim this shows KG benchmark decay specifically; the lesson is analogical.