# TikZ Pilot Comparison Report

**Date:** 2026-08-29
**Baseline commit:** 103432b (tag: book-preview-v0.4-baseline-pre-tikz)
**Experiment branch:** exp/tikz-pilot

---

## Summary

| Metric | Baseline | TikZ Pilot | Delta |
|--------|----------|------------|-------|
| Total pages | 97 | 100 | +3 |
| Ch4 page range | 37–68 | 45–72 | shifted by front matter |
| Ch5 page range | 69–97 | 65–100 | shifted |
| Formal diagrams (Ch4+Ch5) | 0 | 8 | +8 |
| Mermaid blocks (Ch4+Ch5) | 0 | 0 | 0 |
| Tables (Ch4+Ch5) | 20 | 20 | 0 |
| Code blocks (Ch4+Ch5) | 42 | 42 | 0 |
| Build success | ✅ | ✅ | — |
| LaTeX errors | 0 | 0 | — |
| Missing glyph warnings | ✅ (U+2705 only) | ✅ (same) | — |
| Tests | 18 passed | 18 passed | — |

## Figure-by-figure comparison

| Figure ID | Old renderer | New renderer | Pedagogical purpose | Improvement observed | Regression |
|-----------|-------------|-------------|---------------------|---------------------|------------|
| ch04-interpretation-domain | None (text+code) | TikZ | Syntax→interpretation→denotation | **Major**: visual subset relations, domain elements, class extensions make abstract concept concrete | None |
| ch04-model-entailment | None (ASCII pipeline) | TikZ | O ⊨ α as "true in all models" | **Major**: Venn-like diagram makes model-theoretic entailment intuitive | None |
| ch04-exists-vs-forall | None (text+callout) | TikZ | ∃R.C vs ∀R.C side-by-side | **Major**: side-by-side layout with vacuous truth case is far clearer than text | None |
| ch05-forward-fixpoint | None (text walkthrough) | TikZ | G₀→G₁→G₂→fixpoint with θ | **Major**: iterative rounds with substitution annotations are visually traceable | None |
| ch05-shacl-mechanism | None (numbered steps) | TikZ | Target→Focus→Path→Value→Constraint→Result | **Major**: operational flow makes SHACL feel mechanistic, not syntactic | None |
| ch05-consistency-vs-validation | Markdown table | TikZ | 2×2 matrix of independent axes | **Moderate**: annotated quadrants with examples are more memorable than plain table | Table retained alongside |
| ch05-repair-pipeline | ASCII code fence | TikZ | Violation→Candidates→Evaluate→Select→Revalidate | **Major**: fan-out/fan-in structure shows decision problem nature | ASCII pipeline retained alongside |
| ch05-soundness-completeness | Text+formulas | TikZ | A⊆E, E⊆A set relations | **Major**: three-case Venn diagram makes sound/complete/both instantly graspable | None |

## Evaluation

### 1. Did TikZ improve formal clarity?

**Yes, significantly.** All 8 figures teach a mechanism that was previously conveyed only through text, code blocks, or tables. The most impactful improvements:

- **Interpretation/domain** (§4.3): The subset nesting (City^I ⊂ Place^I = Δ^I) is immediately visible rather than requiring mental construction from code blocks.
- **Forward chaining** (§5.2): The iterative G₀→G₁→G₂→fixpoint progression with θ annotations is the strongest pedagogical figure in the pilot.
- **SHACL mechanism** (§5.6): The 6-step operational flow transforms SHACL from a syntax listing into a mechanistic process.

### 2. Did TikZ improve print quality?

**Yes.** Vector PDFs scale cleanly at any resolution. No rasterization artifacts. Grayscale-safe (tested: all figures use fill opacity and line weight, not color-only distinctions). Line widths ≥0.4pt for main elements.

### 3. Did TikZ improve math/notation consistency?

**Yes.** Using the same font stack (Times New Roman + Cambria Math via unicode-math) as the book ensures math symbols in figures match inline math exactly. θ, Δ^I, ⊆, ⊨, ∃, ∀ all render identically.

### 4. Did TikZ make any page layout worse?

**No regressions observed.** Figures fit within A4 margins. No clipping, no overlapping text, no excessive whitespace. The +3 page increase is proportional to the 8 figures added (~0.4 pages per figure on average).

### 5. Is the maintenance burden acceptable?

**Yes, with caveats.** Each figure is a standalone .tex file (~50-80 lines) that compiles independently. The render script handles compilation automatically. Total TikZ source: ~600 lines across 8 files. Maintenance cost is moderate — changes to manuscript content may require figure updates, but figures are self-contained and don't affect other parts of the build.

**Caveat:** MiKTeX package downloads on first compile add ~2-3 minutes to initial build. Subsequent builds are fast (cached packages).

### 6. Which diagram types should definitely move to TikZ?

- Set/subset relationships (interpretation domains, soundness/completeness)
- Logic/entailment structures (models, O ⊨ α)
- Iterative algorithms with state transitions (forward chaining rounds)
- Operational pipelines with labeled steps (SHACL mechanism, repair pipeline)
- Side-by-side comparisons with shared notation (∃ vs ∀)
- Annotated matrices/quadrants (consistency × validation)

### 7. Which diagram types should remain Mermaid or other renderers?

- Conceptual flow diagrams where precise math alignment is not needed
- Graph topology diagrams (use Graphviz)
- Quantitative plots (use matplotlib)
- Simple process flows without mathematical notation

### 8. Should Chapters 1–3 be retrofitted later?

**Potential candidates** (not done in this session):
- Ch1: KG = Data Graph + Semantics + Context mental model diagram
- Ch2: RDF triple structure, SPARQL BGP pattern matching
- Ch3: Identity resolution pipeline, named graph structure

These would benefit from TikZ but are lower priority than Ch4-5 formal diagrams.

### 9. Should Chapter 6 use TikZ by default for formal diagrams?

**Yes.** Chapter 6 covers provenance (PROV-O), temporal knowledge, and contradiction handling — all of which involve formal structures that benefit from precise TikZ rendering.

## Recommendation

**ADOPT TikZ selectively for formal diagrams from Chapter 6 onward.**

Exact scope:
- Use TikZ for: set/logic/inference/validation diagrams, algorithm state transitions, annotated matrices
- Continue using Mermaid for: conceptual flows without math alignment needs
- Continue using tables for: comparison data, regime listings, constraint catalogs
- Continue using code blocks for: Turtle/SPARQL examples, pseudo-code

Do NOT retrofit Chapters 1–3 in this session. Consider a future migration pass if explicitly requested.

## Future retrofit candidates (if requested later)

| Chapter | Figure | Priority |
|---------|--------|----------|
| Ch1 | KG mental model (Data Graph + Semantics + Context) | Medium |
| Ch2 | RDF triple structure | Low |
| Ch2 | SPARQL BGP pattern matching | Medium |
| Ch3 | Identity resolution pipeline | Medium |
| Ch3 | Named graph structure | Low |

## Quality gates

| Check | Result |
|-------|--------|
| Concept dependency tests (9) | ✅ 9/9 passed |
| Full test suite | ✅ 18 passed |
| PDF build | ✅ 100 pages, no LaTeX errors |
| Unresolved citations | ✅ None |
| Leftover Mermaid blocks | ✅ None |
| U+FFFD replacement chars | ✅ None |
| Wrapper artifacts | ✅ None |
| Missing glyph warnings | ✅ Only U+2705 (known false positive) |
| Broken image references | ✅ None |
| Figure clipping/overflow | ✅ None observed |

## Known remaining limitations

1. MiKTeX "major issue" warnings about updates — cosmetic, does not affect output
2. U+2705 (✅) missing glyph warning — known false positive, emoji renders via fallback
3. Verify script "title missing" failures — known false positive from Vietnamese diacritics in PDF text extraction
4. TikZ figures are static — no interactivity (acceptable for print PDF)
