# Book Pedagogy Policy — Knowledge Graph Book

> **Canonical authoring policy.** Every chapter draft, revision, and review MUST comply with this document. It supersedes ad-hoc terminology rules and governs all pedagogical decisions for Chapters 1–10.
>
> Last updated: 2026-08-28

---

## 1. Local Sufficiency Principle

A reader must never encounter a term, acronym, symbol, or syntax element without enough **local** understanding to use it in the current reasoning step.

"Local" means: within the same section, or at most the immediately preceding section. Cross-chapter forward references are permitted only when the concept is **incidental** (see §3) and a minimum usable gloss is provided inline.

**Test:** Could a reader who has read only up to this point explain the concept well enough to follow the next paragraph? If no, the text violates Local Sufficiency.

---

## 2. Defer Depth, Never Required Understanding

Depth of treatment can be deferred to a later chapter. Required understanding for the current argument cannot.

| Permitted | Forbidden |
|-----------|-----------|
| "We will formalize this in Chapter 4" after giving an intuitive working definition | Using `⊑` without explaining what subset-inclusion means here |
| Mentioning OWL exists when discussing schema layers | Writing Turtle syntax before teaching Turtle syntax |
| Naming "Description Logic" as the family OWL belongs to | Using DL notation (`⊓`, `∃R.C`) without local explanation |

**Rule:** If removing a forward reference would make the current section incomprehensible, the concept must be taught locally, not deferred.

---

## 3. Required vs Incidental Concepts

### Required concept
The reader **must** understand this to follow the current argument. Must receive full local introduction (intuition → mechanism → example).

### Incidental concept
Mentioned for context, naming, or bridging to future chapters. The reader does **not** need to understand its internals to follow the current argument. Requires only a minimum usable gloss (one sentence + pointer).

**Decision test:** Remove the concept from the paragraph. Does the argument still hold?
- No → Required. Teach it locally.
- Yes → Incidental. Gloss and move on.

---

## 4. Three-Level Concept Introduction

Every required concept receives three levels, in this order:

1. **Intuition** — What is this thing? Why does it exist? One paragraph, no formalism.
2. **Mechanism** — How does it work? Formal model, algorithm, or structural description. Includes worked example.
3. **Application** — What follows from it? Concrete consequence in the running example domain.

Levels may span multiple paragraphs or subsections, but the ordering is fixed. Never show mechanism before intuition. Never show application before mechanism.

---

## 5. Acronym First-Use Rule

On first occurrence in the entire book:

```
Full Name (ACRONYM — short Vietnamese gloss)
```

Example: `Resource Description Framework (RDF — khung mô tả tài nguyên)`

On subsequent occurrences within the same chapter: acronym alone is sufficient.
On first occurrence in a new chapter after initial introduction: acronym with brief reminder if more than two chapters have passed.

**Exception:** Universally known acronyms (API, URL, HTTP) need expansion only once in the entire book, in the Introduction or Chapter 1.

---

## 6. Mathematics Must Explain Mechanisms

Mathematical notation is a tool for expressing mechanisms precisely, not a substitute for explanation.

For every mathematical expression:

1. State the intuition in prose first.
2. Show the expression.
3. Map each symbol to its meaning in the running example.
4. State what follows from the expression.
5. State what does NOT follow (common misreading).

**Never** present a formula without steps 1 and 3 at minimum.

**Sidebar requirement:** Each chapter that uses non-trivial mathematics must include a sidebar titled "Toán học tối thiểu cho chương này" listing the mathematical prerequisites and where they were introduced.

---

## 7. Major Concept Depth Rubric

Major concepts (entity, relation, graph, RDF triple, SPARQL BGP, ontology, interpretation, model, entailment, provenance, claim, embedding) require:

- [ ] Intuitive motivation (why this concept exists)
- [ ] Formal or semi-formal definition
- [ ] Worked example using the running dataset
- [ ] At least one counterexample or boundary case
- [ ] Connection to at least one other major concept already taught
- [ ] Common misconception callout (if applicable)

Minor/incidental concepts need only items 1 and 3.

---

## 8. Forward Reference Policy

Forward references are permitted under these conditions:

1. The referenced concept is **incidental** to the current argument (§3).
2. A minimum usable gloss is provided inline (one sentence sufficient for the reader to continue).
3. The forward reference includes the target chapter number.
4. No more than **three** forward references appear in any single paragraph.

**Forbidden patterns:**
- Forward reference chains (A references B which references C)
- Forward references to concepts that are required for the current section's comprehension
- "We will learn about X later" without any local gloss

---

## 9. Glossary Is Recall Support, Not Teaching

The end-of-book glossary supports recall of previously taught concepts. It is **not** a substitute for in-text teaching.

If a reader needs to consult the glossary to understand a paragraph they are currently reading, the paragraph violates Local Sufficiency (§1). Fix the paragraph, do not rely on the glossary.

Chapter-end mini-glossaries serve the same recall-support function at chapter scope.

---

## 10. Worked Example Rule

Every mechanism-level explanation (§4, level 2) must include a worked example drawn from the running dataset (city/country/mechanism domain).

Worked examples must:
- Use concrete values from the dataset, not abstract placeholders
- Show the step-by-step application of the mechanism
- Produce a verifiable result the reader can check

Abstract examples (using generic A, B, C) are permitted only as supplementary illustrations after the concrete worked example.

---

## 11. Counterexample Rule

Every major concept (§7) should include at least one counterexample or boundary case showing:
- What the concept does NOT cover
- Where naive intuition fails
- A common misapplication

Counterexamples prevent overgeneralization and are especially important for concepts where database intuition conflicts with semantic-web semantics (e.g., open-world assumption, lack of UNA).

---

## 12. Reader Self-Explanation Checkpoints

Each chapter must include 2–4 self-explanation checkpoints. These are inline prompts asking the reader to pause and articulate understanding.

Format:
```markdown
> 🖊 **Tự kiểm tra:** [Question requiring articulation, not recall]
```

Checkpoints must:
- Ask the reader to explain a mechanism in their own words, not recall a definition
- Appear after a major concept's mechanism-level explanation
- Be answerable using only material presented so far
- Not introduce new information

---

## 13. No Padding

Every paragraph must advance understanding. Prohibited padding:

- Restating the same point in different words without adding precision
- Historical anecdotes that do not illuminate a mechanism
- Motivational prose ("this is very important", "as you can see")
- Redundant transitions between sections that already flow logically
- Lists of features/constructs without mechanism explanation

**Test:** Can the paragraph be removed without loss of understanding? If yes, remove it.

---

## 14. Reader-Friction Review

Before marking any chapter ACCEPTED, perform a reader-friction review:

1. Read the chapter linearly as a first-time reader.
2. At each point where you hesitate, reread, or look ahead: mark it.
3. Classify each friction point: missing local gloss, premature syntax, unclear mechanism, broken dependency chain.
4. Fix all friction points before acceptance.

This review is distinct from technical correctness review. A chapter can be technically correct and still fail the reader-friction review.

---

## 15. Figure Renderer Policy

Formal diagrams must teach a mechanism, not decorate a page. Every figure requires a caption, a meaningful filename, and at least one introductory sentence explaining how to read it.

### Renderer taxonomy

| Diagram class | Preferred renderer | Rationale |
|---------------|-------------------|-----------|
| Conceptual flow / process diagrams | Mermaid | Fast iteration, readable in Markdown preview |
| Formal semantic / logic / set / inference diagrams | TikZ | Precise math alignment, vector output, grayscale-safe |
| Graph topology diagrams | Graphviz or equivalent | Automatic layout for node-edge structures |
| Quantitative plots | Plotting tool (matplotlib, etc.) | Data-driven; TikZ only if clearly justified |
| Code / data examples | Native code blocks | Not diagrams |

### When TikZ is preferred

TikZ is preferred when the figure must align tightly with:
- Mathematical notation ($\Delta^I$, $\subseteq$, $\theta$, $\models$)
- Set semantics (Venn/Euler relationships)
- Logic structure (entailment, model relationships)
- Inference rounds (forward chaining steps with substitutions)
- Validation mechanics (SHACL operational flow)

### Figure quality requirements

All figures (regardless of renderer) must be:
- Grayscale-safe (no color-only distinctions)
- A4-readable at normal reading size
- Math symbols rendered correctly (matching manuscript notation)
- Labels not too dense, no overlapping text
- No clipped arrows or nodes
- Line widths readable in print (≥0.4pt for main lines)
- Terminology consistent with the manuscript

### Architecture

TikZ sources live in `book/figures/tikz/` as standalone `.tex` files that compile independently. Generated PDFs go to `book/figures/generated/`. Manuscripts include generated PDFs via `![caption](../figures/generated/name.pdf)`. The render script `scripts/render_tikz.sh` compiles all sources; the book build calls it automatically.

---

## Relationship to Other Documents

- **CLAUDE.md**: Project conventions (language, code style, build commands). This document governs pedagogy.
- **AGENTS.md**: Agent workflow rules. This document governs content quality.
- **TERMINOLOGY_GLOSS_MECHANISM.md**: Superseded by this document for pedagogical policy. Retained as historical reference for its specific gloss formatting examples.
- **docs/SOURCES.md / SOURCE_MATRIX.md**: Source citation discipline. Complementary to this document.
