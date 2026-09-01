# English edition — Ch1+Ch2 merged and audited (2026-09-01); next: Ch3, #33, or #28

## Current state

**Vietnamese book: complete.** Chapters 1–10 + Afterword + Glossary ACCEPTED; v0.1.0
released (PDF Release, 358 print pages, 226 glossary terms, 91 sources, 106 tests).

**English edition: active.** Parallel `book-en/` tree, incremental per-chapter translation.
Infrastructure (build scripts + Makefile LANG switch, metadata, verify gate) was built with
Chapter 1.

- Chapter 1 merged: PR #27, commit 887fb9d ("From Graph to Knowledge")
- Chapter 2 merged: PR #30, commit ed95d6c ("Data Models and Query Languages") — 42-page
  English PDF, `LANG=en` verify gate PASSES
- Ch1–Ch2 audit merged: PR #32, commit 2e011e0 — report in `docs/EN_CH1_CH2_REVIEW.md`
  (Issue #31 closed)
- Translation conventions established: preserve code fences / `@cite` keys / section numbers /
  epistemic distinctions / ⚑ draft-standard markers; translate mermaid node labels + captions
  (`Hình:`→`Figure:`); localize Vietnamese domain literals; verify-gate titles must be
  dash-free substrings (pdftotext renders em-dash as `--`)

## Audit outcome (Ch1–Ch2 English, 2026-09-01)

Verdict: Ch1 PASS (accuracy/clarity/depth). Ch2 PASS on clarity+depth, **2 MAJOR accuracy
errors found and fixed in English**:

- **A1** §2.1.7 — the claim "RDF 1.2 retains the RDF 1.1 reification vocabulary as legacy"
  cited `@w3c-rdf12-concepts`, but that spec never mentions `rdf:Statement`. Re-cited to
  RDF 1.1 Concepts + stated plainly that RDF 1.2 does not deprecate it.
- **A2** §2.7 — text said only `newtonCooling_1 requires rateOfChange_1`; the dataset has two
  `ex:requires` edges (`rate_of_change.ttl` L214–215). Corrected to name both.

Both errors are **pre-existing in the Vietnamese original** (`book/chapter02.md`), so released
v0.1.0 contains them → tracked as Issue #33.

Sources logged in `docs/source_index.json`: new **N4J-09** (Neo4j scalar functions —
`elementId()`/`id()`), corrected **SP12-01** publication_date 2026-08-20 → 2026-08-27.

## Open issues

- **#33** — fix A1 + A2 in the Vietnamese `book/chapter02.md` (EN/VI parity); needs a VI patch
  milestone + rebuilt PDF.
- **#28** — pre-existing VIETNAMESE gate failure: literal `[@key]` citation markers in the
  released v0.1.0 PDF text (Ch7–Ch10 range). Confirmed pre-existing (original script fails
  identically). Needs investigation: pdftotext artifact vs genuine latent citation bug.

## Next steps (candidates)

1. Translate Chapter 3 ("Lược đồ, Định danh và Ngữ cảnh") following the Ch1/Ch2 pattern — or
2. Fix Issue #33 (VI Ch2 parity patch, small and well-specified) — or
3. Investigate Issue #28 (locate source lines producing literal `[@key]` text)
4. Keep adding chapters → eventual English release tag (like v0.1.0 flow)

## Constraints carried forward

- GitHub workflow: Issue → Branch → Commits → PR → Validate → Merge; never invent numbers;
  verify GitHub state before claiming done
- **Each PR merge needs explicit per-PR user approval** — the auto-mode classifier blocks a
  merge otherwise (a generic "continue" does not qualify). Same for remote branch deletion.
- Use local git commit so author shows as "MinhTuan76800310"; NO Co-Authored trailer
- `uv` not on PATH → use `python -m pytest` / `python -m ruff`
- `make` not on PATH → run `LANG=en bash scripts/build_book.sh` directly
- ruff 0.16.5 formats Python blocks embedded in Markdown — keep them formatted
- Monolithic reviewer agents stall on oversized structured output (180s no-progress kill);
  split review work per-claim or do it inline with targeted WebFetch verification
