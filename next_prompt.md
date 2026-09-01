# English edition — Ch1+Ch2 merged (2026-09-01); next: Ch3 or Issue #28

## Current state

**Vietnamese book: complete.** Chapters 1–10 + Afterword + Glossary ACCEPTED; v0.1.0
released (PDF Release, 358 print pages, 226 glossary terms, 91 sources, 106 tests).

**English edition: active.** Parallel `book-en/` tree, incremental per-chapter translation.
Infrastructure (build scripts + Makefile LANG switch, metadata, verify gate) was built with
Chapter 1.

- Chapter 1 merged: PR #27, commit 887fb9d ("From Graph to Knowledge")
- Chapter 2 merged: PR #30, commit ed95d6c ("Data Models and Query Languages") — 42-page
  English PDF, `LANG=en` verify gate PASSES
- Issue #29 (Ch2) closed by PR #30
- Translation conventions established: preserve code fences / `@cite` keys / section numbers /
  epistemic distinctions / ⚑ draft-standard markers; translate mermaid node labels + captions
  (`Hình:`→`Figure:`); localize Vietnamese domain literals; verify-gate titles must be
  dash-free substrings (pdftotext renders em-dash as `--`)

## Open issue

- **#28** — pre-existing VIETNAMESE gate failure: literal `[@key]` citation markers in the
  released v0.1.0 PDF text (Ch7–Ch10 range). Confirmed pre-existing (original script fails
  identically). Needs investigation: pdftotext artifact vs genuine latent citation bug.

## Next steps (candidates)

1. Investigate Issue #28 (locate source lines producing literal `[@key]` text) — or
2. Translate Chapter 3 ("Lược đồ, Định danh và Ngữ cảnh") following the Ch1/Ch2 pattern
3. Keep adding chapters → eventual English release tag (like v0.1.0 flow)

## Constraints carried forward

- GitHub workflow: Issue → Branch → Commits → PR → Validate → Merge; never invent numbers;
  verify GitHub state before claiming done
- Use local git commit so author shows as "MinhTuan76800310"; NO Co-Authored trailer
- `uv` not on PATH → use `python -m pytest` / `python -m ruff`
- `make` not on PATH → run `LANG=en bash scripts/build_book.sh` directly
- ruff 0.16.5 formats Python blocks embedded in Markdown — keep them formatted