# Experiment Status — Knowledge Graph Book

Tracks the execution status of all experiments. An experiment is only marked ✅ after it has been run and output verified.

Last updated: 2026-08-25

## Chapter 1: From Graph to Knowledge

| ID | Title | Difficulty | Status | Last Run | Evidence Summary |
|----|-------|-----------|--------|----------|------------------|
| 1-1 | Plain graph without semantics | ★ | ✅ | 2026-08-25 | Ran successfully. Output shows identical topology for city/social graphs, confirming semantics-free nature. |
| 1-2 | Data graph vs taxonomy | ★ | ✅ | 2026-08-25 | Ran successfully. Taxonomy correctly returns transitive instances (CapitalCity ⊑ City). Data graph query returns only direct matches. |
| 1-3 | Progressive transformation to KG | ★★ | ✅ | 2026-08-25 | Ran successfully. All 5 stages execute. Inference produces symmetric, subclass, and domain/range triples as expected. |
| 1-4 | Data graph → simple KG | ★★ | ✅ | 2026-08-25 | Ran successfully. Forward-chaining infers 8 new triples. Region/City queries work only after semantics added. |
| 1-5 | Define semantics of a relation | ★★★ | ✅ | 2026-08-25 | Ran successfully. Symmetry, transitivity, and inverse inference all produce correct triples. 3 inferred triples total. |

## Test Results

All 20 pytest tests pass (2026-08-25):
- TestExp11: 6/6 passed
- TestExp12: 5/5 passed
- TestExp13: 3/3 passed
- TestExp14: 3/3 passed
- TestExp15: 3/3 passed

Note: Tests require `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` due to ROS jazzy launch_testing plugin conflict with pytest 9.x on this system.

## Chapters 2–10

Not yet implemented. Experiments will be added as each chapter is drafted.

</content>