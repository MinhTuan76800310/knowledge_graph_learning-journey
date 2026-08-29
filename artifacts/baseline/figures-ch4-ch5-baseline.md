# Baseline Figure Inventory — Chapters 4 & 5

**Date:** 2026-08-29
**Commit:** 103432b (book-preview-v0.4-baseline-pre-tikz)

## Summary

Chapters 4 and 5 contain **zero formal diagrams** (no Mermaid, no TikZ, no images).
All visual concepts are conveyed through:
- Text descriptions with inline math ($...$)
- Code blocks (Turtle, pseudo-code)
- Tables (Markdown)
- ASCII-art pipeline sketches in code fences

## Chapter 4 — Potential figure locations

| Location | Concept | Current format | TikZ candidate? |
|----------|---------|---------------|-----------------|
| §4.3 Interpretation | Domain Δ^I, class extensions, individual denotations | Text + code block | YES — interpretation/domain diagram |
| §4.3 Model/Entailment | Models(O), O ⊨ α | Text description + ASCII pipeline | YES — model/entailment diagram |
| §4.6 Existential vs Universal | ∃R.C vs ∀R.C side-by-side | Text + callout boxes | YES — restriction comparison |
| §4.4 Subclass | City ⊑ Place subset relation | Text only | NO — simple enough as text |
| §4.8 OWA | Three states of knowledge | Text + table | NO — table works well |

## Chapter 5 — Potential figure locations

| Location | Concept | Current format | TikZ candidate? |
|----------|---------|---------------|-----------------|
| §5.2 Forward chaining | G₀→G₁→G₂→fixpoint with θ | Text walkthrough + formula | YES — forward chaining rounds |
| §5.13 Soundness/Completeness | A⊆E, E⊆A set relations | Text + formulas | YES — Venn/set diagram |
| §5.9 Consistency vs Validation | 2×2 matrix | Markdown table | YES — annotated 2×2 matrix |
| §5.6 SHACL mechanism | Target→Focus→Path→Value→Constraint→Result | Numbered text steps | YES — operational flow diagram |
| §5.12 Repair pipeline | Violation→Candidates→Select→Revalidate | ASCII pipeline in code fence | YES — repair pipeline flow |
| §5.4 Materialization vs Query-time | Comparison | Table | NO — table works well |
| §5.5 Forward vs Backward | Two strategies | Text comparison | NO — text suffices |

## Pilot selection (8 figures)

### Chapter 4 (3 figures)
1. ch04-interpretation-domain — Interpretation I = (Δ^I, ·^I) with class extensions
2. ch04-model-entailment — Multiple interpretations, models, entailment
3. ch04-exists-vs-forall — ∃R.C vs ∀R.C side-by-side

### Chapter 5 (5 figures)
4. ch05-forward-fixpoint — Forward chaining rounds with θ substitutions
5. ch05-soundness-completeness — Set relationship A vs E
6. ch05-consistency-vs-validation — 2×2 annotated matrix
7. ch05-shacl-mechanism — Target→Focus→Path→Value→Constraint→Result
8. ch05-repair-pipeline — Violation→Candidates→Evaluate→Select→Revalidate
