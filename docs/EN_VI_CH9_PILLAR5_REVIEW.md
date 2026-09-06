# Review Brief — v0.3 Pillar 5: Chapter 9 (VI + EN, 100% parity)

**Audience:** domain reviewer (knowledge-graph / retrieval / complexity).
**PR:** #78 (draft) · **Issue:** #77 · **Branch:** `en-vi-ch9-pillar5`
**Commits:** `fa9b962` (main work, 35 files) · `34c8676` (source registration)
**Base:** `main` @ `2ccaa1a` (post Ch8 Pillar-4 merge)

---

## 1. Scope & intent

Pillar 5 of `docs/BOOK_V0_3_MILESTONE.md` ("Combinatorial RAG Bounds & Evidence Packet
Architecture"). Chapter 9 (Retrieval, QA & GraphRAG) is upgraded in the Vietnamese
canonical text and mirrored into a brand-new English edition file, at 100% structural,
conceptual, and pedagogical parity. Reader baseline is calculus + basic linear algebra;
the recurring Mechanism Knowledge Graph (`RATE_OF_CHANGE`, velocity/current/population
applications) is the running example.

Three deliverables (A/B/C in the milestone):

- **A — Path-explosion bounding:** combinatorial blow-up, error cascading, symbolic
  pruning, Personalized PageRank, Steiner-tree approximation.
- **B — GraphRAG vs long-context Pareto frontier.**
- **C — Evidence Packet as a 3-compartment dossier + closed-world prompting + abstention.**

---

## 2. File map (what to open, and why)

| File | Δ | What to review |
|---|---|---|
| `book/chapter09.md` | +401 / −10 | VI canonical deepening — 9 new subsections (§9.36.1, §9.39.1, §9.55.1–.6, §9.70.1) |
| `book-en/chapter09.md` | +2895 (new) | Full EN translation of all 79 sections + terms + references |
| `book/references.bib` | +32 | 3 new entries: `page-pagerank-1999`, `haveliwala-ppr-2002`, `karp-reducibility-1972` |
| `book/concept_registry.yaml` | +32 | 4 concepts: `personalized_pagerank`, `steiner_tree_approximation`, `multi_hop_error_cascading`, `graphrag_vs_long_context` |
| `book/glossary.md` | +8 | 4 terms: Error cascading, Long-context vs GraphRAG, Personalized PageRank, Steiner tree |
| `tests/test_chapter09_integrity.py` | +11 / −2 | figures +2, citekeys +3, glossary terms +4, Ch9 concept count 77→81 |
| `scripts/verify_book_pdf.sh` | +1 | EN `EXPECTED_TITLES` += Ch9 title |
| `book-en/book-manifest.yaml` | +3 / −2 | EN build now includes `chapter09.md` |
| `docs/BOOK_STATUS.md` | +5 / −4 | Ch8 EN → MERGED (#76); Ch9 EN → in PR; Pillar 4 → MERGED; Pillar 5 → in PR |
| `docs/CITATION_MAP.md` | +3 | register the 3 new source IDs (see §7) |
| `book/figures/tikz/ch09-{path-explosion,pareto-graphrag}.tex` | new | 2 new VI figures |
| `book-en/figures/tikz/ch09-*.tex` | 11 new | EN mirrors of all 11 Ch9 figures |

**VI anchors** (line numbers in `book/chapter09.md`): §9.55.1 @1784, §9.55.2 @1824,
§9.55.3 @1859, §9.55.4 @1885, §9.55.5 @1946, §9.55.6 @1994, §9.70.1 @2432,
§9.36.1 @1227, §9.39.1 @1352. **EN anchors** are ~30 lines later (same order).

---

## 3. How to read the prose (house pattern)

Every upgraded section follows: intuition → mechanism → **Formal meaning:** →
**In this book:** → worked example → **Dangerous simplification:** → **MUST NOT infer:**.
Callouts are `> ⚠️` / `> ℹ` / `> 🖊` blockquotes. Figures are grayscale-safe (color **and**
text annotation). VI uses `**Trong sách:**` / `**Nguy hiểm khi đơn giản hóa:**` /
`**MUST NOT suy ra:**`; EN renders these as `**In this book:**` /
`**Dangerous simplification:**` / `**MUST NOT infer:**` (Ch9 is the only chapter using
these markers — the EN convention was established here).

---

## 4. Substantive claims to verify (the core of the review)

Please check the mathematics and that each citation actually supports the claim it is
attached to. Formulas are LaTeX `$…$` / `$$…$$`.

**§9.55.1 — Path counting $O(\bar{d}^k)$.**
Claim: number of length-$k$ walks from an anchor grows like $\bar{d}^{\,k}$ for average
degree $\bar{d}$. Bridge: the adjacency-matrix power $A^k$ counts $k$-walks (ties back to
Ch5 transitive closure). Table 9.3 tabulates $\bar{d}\in\{4,10,50\}\times k\in\{1..4\}$.
*Verify:* the table arithmetic and that the "walks vs simple paths" distinction is stated
honestly (the bound is on walks; simple paths are fewer).

**§9.55.2 — Multi-hop error cascading $P=\prod_i p_i = p^k$.**
Claim: with per-hop precision $p$, an independent-hop path is correct with probability $p^k$;
worked $0.8^3=0.512$, $0.8^4=0.41$. *Verify:* the independence assumption is flagged as an
idealization (real hops are correlated), and that "precision per hop" is defined, not hand-waved.

**§9.55.3 — Symbolic constraint pruning.**
Claim: ontology typing (Ch4) + SHACL shapes (Ch5) remove mistyped edges before traversal,
reducing $\bar{d}\to\bar{d}'\ll\bar{d}$. *Verify:* no overclaim that pruning is complete
(it bounds, does not solve).

**§9.55.4 — Personalized PageRank.**
$$\mathbf{p}=(1-\alpha)\,\tilde{A}\,\mathbf{p}+\alpha\,\mathbf{s}$$
$\tilde{A}$ = degree-normalized **column-stochastic** transition ($\tilde A_{ij}=A_{ij}/\deg(j)$);
$\alpha\in(0.1,0.2)$ restart prob; power iteration $\mathbf{p}^{(t+1)}=(1-\alpha)\tilde A\mathbf{p}^{(t)}+\alpha\mathbf{s}$;
converges because spectral radius $\le(1-\alpha)<1$ (contraction); closed form
$\mathbf{p}=\alpha(I-(1-\alpha)\tilde A)^{-1}\mathbf{s}$; hub penalty via the $1/\deg(j)$ factor.
Sources: `page-pagerank-1999`, `haveliwala-ppr-2002`.
*Verify:* column- vs row-stochastic convention is consistent with the $\tilde A_{ij}$ definition;
the "power iteration = Ch8 embedding technique" bridge is fair; the hub-penalty claim is the
normalization, not an extra heuristic.

**§9.55.5 — Steiner Tree.**
Claim: Steiner Tree in Graphs is NP-complete (Karp 1972, `karp-reducibility-1972`); a
**2-approximation** via metric closure (all-pairs shortest paths over terminals) + MST
(Prim/Kruskal). *Verify:* the 2-approx bound is the standard metric-closure+MST result
(actually ≤2−1/t for t terminals; "2-approx" is the conventional loose statement — confirm
the text doesn't claim it's tight), and that Steiner nodes vs terminals are distinguished.

**§9.70.1 — GraphRAG vs long-context Pareto frontier.**
Table 9.4, four axes: (1) per-query cost $O(N^2)$ self-attention ($N\times N$ dot products
$\mathbf{q}_i\!\cdot\!\mathbf{k}_j$) vs $O(|E_{\text{sub}}|)$ subgraph; (2) lost-in-the-middle
(`liu-lostmid-2023`); (3) epistemic anchoring via Claim Ledger IDs; (4) global sensemaking via
Leiden/Louvain community summaries (`edge-graphrag-2024`). ROI boundary where GraphRAG's
relative advantage crosses zero. *Verify:* $O(N^2)$ is stated as attention cost (not total
inference), and the "when long-context wins" list is genuinely non-strawmanned.

**§9.36.1 — Evidence Packet, 3 compartments.**
(1) raw evidence/citations (verbatim fragments, doc hashes, URI spans, line numbers);
(2) epistemic statuses (Claim IDs, governance, bi-temporal); (3) verification/lineage
(PROV-O, model version, evaluator signature, confidence). *Verify:* compartment boundaries
don't overlap the Ch6 Claim Ledger / Ch7 governance definitions inconsistently.

**§9.39.1 / §9.43 — Closed-world prompting + abstention.**
Constrained prompt: cite only Compartment 1–2 IDs, else emit "Unknown"/"Evidence missing".
*Verify:* abstention is presented as unlocked by the closed-world prompt, not as a free
model behavior.

---

## 5. Bilingual parity evidence (already machine-checked)

- Section numbers: `diff` of `^#{2,3} <num>` between VI and EN → **identical** (79 sections + 9 subsections).
- Citekeys: 24 unique, `diff` VI vs EN → **identical**.
- Figures: 11 `ch09-*` referenced in both, paths byte-identical.
- Marker counts VI↔EN: `Formal meaning` 15/15, `Trong sách`→`In this book` 5/5,
  `Nguy hiểm`→`Dangerous simplification` 3/3, `MUST NOT suy ra`→`MUST NOT infer` 65/65.
- Vietnamese-exclusive-codepoint scan of `book-en/chapter09.md` → **0 hits** (no untranslated leakage).
- Part dividers: 8 `# Phần A–H` → `# Part A–H`.

---

## 6. Validation gates (all green)

```
python -m pytest                 → 106 passed
python -m ruff check .           → clean
python -m ruff format --check .  → 238 files formatted
bash scripts/build_book.sh && bash scripts/verify_book_pdf.sh            → VI GATE PASSED (431 pp)
LANG=en bash scripts/build_book.sh && LANG=en bash scripts/verify_book_pdf.sh → EN GATE PASSED (376 pp)
```
EN gate confirms: Ch9 title present, no unresolved `[@…]`, no raw caption leaks, no U+FFFD.

---

## 7. Things I want scrutinized / known issues

1. **Pre-existing VI inconsistency (NOT introduced here, faithfully mirrored):** the
   orientation blockquote (`book/chapter09.md` L53 / `book-en` L53) says **"Q01–Q50"**, but
   §9.76 is titled and populated **Q01–Q56** (56 questions). Misconception count (34) is
   consistent everywhere. The EN translation kept "Q01–Q50" to preserve parity. **Decision
   needed:** fix the VI orientation to Q01–Q56 (and EN) as a follow-up, or leave for the
   Ch9 checkpoint pass? I did not silently "correct" it to avoid diverging the editions.
2. **Cosmetic LaTeX quirk, identical in VI:** §9.55.4 power-iteration norm is written
   `$\|\mathbf{p}^{(t+1)}-\mathbf{p}^{(t)\|}$` — the closing `\|` sits inside the superscript
   group. It compiles (both PDFs build) and VI has the exact same string (L1920), so EN
   mirrors it for parity. Fix in both editions together if you want it cleaned.
3. **Source registration:** the 3 new bib entries were cited + in `references.bib` but were
   **not** in `docs/CITATION_MAP.md` until commit `34c8676`. Note that Ch8 Pillar-4's new
   keys are also absent from CITATION_MAP — the per-chapter registration convention has
   drifted. I registered Ch9's to satisfy CLAUDE.md ("traceable to registered sources");
   consider whether Ch8 needs a backfill.
4. **Faithful-translation caveat (standing lesson from the Ch1–2 audit):** a translation
   propagates upstream errors. I verified the new math against the cited sources, but a
   second pair of eyes on §9.55.4 (stochastic convention) and §9.55.5 (approx ratio) is the
   highest-value check.
5. **No release cut.** v0.3 milestone still open (Pillar 6 / Ch10 + glossary). This PR is
   content-only.

---

## 8. Suggested review order

1. Read VI §9.55.1–.6 and §9.70.1 first (the substance).
2. Diff one section VI↔EN (e.g. §9.55.4) to confirm parity is real, not padded.
3. Check the 3 bib entries' metadata (authors/venue/DOI) against the actual papers.
4. Confirm the 4 registry concepts + 4 glossary terms read correctly.
5. Decide on items 1–2 of §7.
