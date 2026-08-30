# CLAUDE.md — Knowledge Graph Learning Journey

## Goal

Build this repo as:

1. a high-quality Knowledge Graph learning book, and
2. a traceable GitHub project.

Keep communication and workflow simple.

---

## GitHub workflow

For meaningful work, always follow:

```text
Issue → Branch → Commits → PR → Validate → Merge
```

Rules:

* Do not do planned work directly on `main`.
* Every non-trivial task needs a real GitHub Issue.
* Create a branch from updated `main`.
* One branch = one coherent task.
* Push meaningful checkpoints.
* Open a PR to `main`.
* Never invent Issue/PR/tag/release numbers.
* Verify GitHub state before saying work is pushed, merged, released, or done.
+ Don't commit Co-Authored

`next_prompt.md` is only a handoff note.
The active GitHub Issue is the real assignment.

---

## Before working

Check Git status/history and read:

```text
CLAUDE.md
AGENTS.md
docs/BOOK_STATUS.md
next_prompt.md
docs/BOOK_PEDAGOGY.md
```

For chapter work, also inspect its semantic contracts, checkpoint, sources, concept registry, and glossary.

Do not start the next chapter unless the current GitHub task/status allows it.

---

## Book rules

* Book prose: Vietnamese.
* Keep English technical terms on first occurrence.
* Write original explanations; do not copy sources.
* External claims must be traceable to registered sources.
* Stable standards are the curriculum baseline.
* Draft standards must be clearly labeled.
* Passing tests does not prove semantic correctness.

For standards-sensitive work:

```text
source → semantic contract → manuscript/code → test
```

Follow `docs/BOOK_PEDAGOGY.md`.

Keep the **Mechanism Knowledge Graph** model consistent across chapters.

---

## Validation

Before merge, run relevant checks:

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

For book changes also verify when applicable:

* semantic contracts,
* citations,
* glossary/concept registry,
* diagrams,
* PDF build and affected pages,
* editorial review.

Never report unverified results.

---

## Release

Stable book milestones must be released by Claude using GitHub CLI.

```text
accepted book milestone
→ build and validate PDF
→ tag exact commit
→ push tag
→ gh release create
→ attach versioned PDF
```

Example:

```bash
git tag v0.5.0
git push origin v0.5.0

gh release create v0.5.0 \
  dist/knowledge-graph-book-v0.5.0.pdf \
  --title "Knowledge Graph Book v0.5.0" \
  --generate-notes
```

Before new development, backfill previous stable PDF versions from Git history when their exact source commits can be verified.

Claude owns the release process. The user should not need to create releases manually.



## Done means GitHub proves it

At the end report only:

```text
Issue:
Branch:
PR:
Commit:
Validation:
Merge:
Release:
Remaining:
```

A local commit is not done.
A pushed branch is not done.
A stable book milestone without its PDF Release is not done.
