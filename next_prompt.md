# English edition — Ch1+Ch2 merged and audited (2026-09-01); next: Ch3 or #28

## Current state

**Vietnamese book: complete.** Chapters 1–10 + Afterword + Glossary ACCEPTED; v0.1.0
released (PDF Release, 358 print pages, 226 glossary terms, 91 sources, 106 tests).
**Re-audit follow-up:** Ch2 §2.1.7 RDF 1.1 Schema citation + §2.7 requires edge fixed in
`book/chapter02.md` and merged (PR #36 / Issue #33).

**English edition: active.** Parallel `book-en/` tree, incremental per-chapter translation.
Infrastructure (build scripts + Makefile LANG switch, metadata, verify gate) was built with
Chapter 1.

- Chapter 1 merged: PR #27, commit 887fb9d ("From Graph to Knowledge")
- Chapter 2 merged: PR #30, commit ed95d6c ("Data Models and Query Languages") — 42-page
  English PDF, `LANG=en` verify gate PASSES
- Ch1–Ch2 audit merged: PR #32, commit 2e011e0 — report in `docs/EN_CH1_CH2_REVIEW.md`
  (Issue #31 closed)
- Re-audit fixes merged: PR #36 (VI Ch2 follow-up, Issue #33) and PR #37 (EN Ch2 citation
  fix, Issue #35)
- Translation conventions established: preserve code fences / `@cite` keys / section numbers /
  epistemic distinctions / ⚑ draft-standard markers; translate mermaid node labels + captions
  (`Hình:`→`Figure:`); localize Vietnamese domain literals; verify-gate titles must be
  dash-free substrings (pdftotext renders em-dash as `--`); re-audit before claiming audit done

## Audit outcome (Ch1–Ch2 English + re-audit, 2026-09-01)

Verdict: Ch1 PASS (accuracy/clarity/depth). Ch2 PASS on clarity+depth, **MAJOR accuracy
errors found and fixed**:

- **A1** §2.1.7 — claim "RDF 1.2 retains the RDF 1.1 reification vocabulary as legacy"
  cited `@w3c-rdf12-concepts`, but that spec never mentions `rdf:Statement`. Re-cited to
  RDF 1.1 Schema (`@w3c-rdf-schema`) and stated plainly that RDF 1.2 does not mention or
  deprecate it.
- **A1′** §2.1.7 — the first English "fix" in PR #32 cited `@w3c-rdf11-concepts` for the
  same vocabulary; re-audit found the correct source is **RDF 1.1 Schema** (§5.3). Corrected
  in PR #37.
- **A2** §2.7 — text said only `newtonCooling_1 requires rateOfChange_1`; the dataset has
  two `ex:requires` edges (`rate_of_change.ttl` L214–215). Corrected to name both.

Sources logged in `docs/EN_CH1_CH2_REVIEW.md`; `@w3c-rdf-schema` (R11-03) confirmed as the
source for `rdf:Statement`, `rdf:subject`, `rdf:predicate`, `rdf:object`.

## Open issues

- **#28** — pre-existing VIETNAMESE gate failure: literal `[@key]` citation markers in the
  released v0.1.0 PDF text (Ch7–Ch10 range). Confirmed pre-existing (original script fails
  identically). Needs investigation: pdftotext artifact vs genuine latent citation bug.

## Next steps (candidates)

1. Translate Chapter 3 ("Lược đồ, Định danh và Ngữ cảnh") following the Ch1/Ch2 pattern — or
2. Investigate Issue #28 (locate source lines producing literal `[@key]` text)
3. Keep adding chapters → eventual English release tag (like v0.1.0 flow)

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
