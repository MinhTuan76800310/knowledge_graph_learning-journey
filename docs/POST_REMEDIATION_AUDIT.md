# Post-Remediation Audit — Whole-Book Depth Remediation (Chapters 1–6)

**Date:** 2026-08-30
**Baseline audit:** `docs/BOOK_CONCEPT_DEPTH_AUDIT.md` (112 concepts: 66 Major, 42
Supporting, 4 Incidental; baseline 0%–10% Mechanism-KG transfer coverage)
**Remediation plan:** `docs/BOOK_DEPTH_REMEDIATION_PLAN.md`
**Canonical model:** `docs/MECHANISM_KG_CANONICAL_MODEL.md` (frozen object vocabulary)

## Scope

Every action item in the baseline audit for Chapters 1–6 was remediated in this pass.
No chapter was rewritten from scratch; all strong existing explanations were preserved.
Chapter 7 was NOT started (per plan constraint).

## Verification Results

| Check | Result | Evidence |
|-------|--------|----------|
| Ch1 audit rows remediated | ✅ | mechanism triple beside Hanoi (§1.3); Step 2/5 mechanism nodes + annotated mechanism triple (§1.6); assertion ≠ accepted knowledge (§1.8) |
| Ch2 audit rows remediated | ✅ | mechanism Turtle (§2.1.5); mechanism BGP query (§2.1.6); LPG mechanism domain (§2.2.4); tradeoff analysis (§2.4) |
| Ch3 audit rows remediated | ✅ | RDFS schema table (§3.1.7); sameAs evidence-based resolution (§3.2.5); n-ary DerivativeApplication (§3.3.3); integration mini-case (§3.4) |
| Ch4 audit rows remediated | ✅ | interpretation Δ^I over mechanisms (§4.3); DL axioms for DerivativeApplication (§4.9); consistency/satisfiability on mechanism ontology (§4.9); EL profile classification (§4.12) |
| Ch5 audit rows remediated | ✅ | forward chaining θ trace on mechanism IRIs (§5.2); CandidateMechanismShape (§5.6); mechanism 2×2 (§5.9); repair decision (§5.12); two-regime SPARQL (§5.14); Condition grounded via ex:uniformEnv_1 (§5.18) |
| Ch6 audit rows remediated | ✅ | all 18 rows mapped: epistemic walkthrough (§6.1), Proposition/Assertion/Claim (§6.2), PROV-O chain + broken chain (§6.4), ambiguous evidence (§6.5), 5-type taxonomy (§6.6), temporal validity Newtonian→relativistic + bitemporal query (§6.7), malformed claim (§6.10), confidence policy (§6.11), governance FSM + lifecycle (§6.12), algorithm supersession (§6.13), LLM→CandidateMechanism protocol (§6.16), full pipeline (§6.17), query semantics of Accepted (§6.12) |
| Mechanism-KG transfer anchors | ✅ | all planned transfer cells verified present in chapter text (per-chapter spot checks + term presence scan) |
| Explanation theater | ✅ | zero token "also applies" sentences found (grep sweeps across 6 chapters) |
| Capability ladders | ✅ | all 6 chapters use the canonical "Mechanism Knowledge System — Năng lực đạt được" format (Ch2 standardized this pass) |
| Internal section references | ✅ | 287/287 `§N.M` references resolve (self + cross-chapter) |
| Citation integrity | ✅ | 37/37 citation keys used in chapters exist in `book/references.bib`; 39/39 bib keys mapped in `docs/CITATION_MAP.md`; RDF 1.2/SPARQL 1.2 only inside "Current developments" callouts |
| Concept registry | ✅ | `book/concept_registry.yaml`: 84 concepts (Ch1–6); invariants enforced by tests |
| Semantic contracts | ✅ | contract docs now exist for ALL chapters (Ch1 and Ch3 created this pass) |
| Test suite | ✅ | 18/18 pass (`pytest -q`: concept dependencies 9, book integrity 2, repo integrity 7) |
| Figure sources ↔ outputs | ✅ | 13/13 TikZ `.tex` sources pair 1:1 with generated PDFs |
| PDF build | ✅ | 167 pages (baseline 124 — remediation added ~43 pages), LuaLaTeX clean, 0 undefined citations; 13 vector figures + 9 mermaid diagrams all embedded |

## Build Fixes Applied This Pass

1. `scripts/build_book.sh`: copy `book/figures/generated/*.pdf` → `build/figures/generated/`
   before Pandoc (chapters reference `figures/generated/...`; nothing previously staged
   the PDFs for the build, so generated figures silently failed to embed).
2. `book/chapter05.md` §5.2: removed backticks embedded inside inline math
   (`$G_1 = G_0 \cup \{ \text{`...`} \}$` → `\text{...}`) — two LuaLaTeX "Missing $
   inserted" failures at the $G_1$/$G_2$ lines.
3. `book/chapter06.md`: figure paths `../figures/generated/` → `figures/generated/`
   (5 references resolved outside the book/ tree).

## Chapter Status After Remediation

All of Chapters 1–6 remain **ACCEPTED** (see `docs/BOOK_STATUS.md`). Per-chapter
checkpoints: `docs/CHAPTER0{2,3,4,5,6}_BOOK_CHECKPOINT.md` and the readability checkpoint
`docs/BOOK_DEEP_READABILITY_CHECKPOINT.md`.

## Constraints Honored

- Chapter 7 (Knowledge Acquisition and Integration) NOT started — new session.
- No new breadth added; no deferred labs resumed; Neo4j not installed.
- All strong existing explanations preserved; remediation added depth and transfer, not
  rewrites.