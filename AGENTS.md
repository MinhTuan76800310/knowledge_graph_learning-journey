# Agents Guide — knowledge-graph-book

This repository is designed for AI-assisted development. Follow these rules when working on this project.

## Language policy

- **Book content** (`book/`, chapter READMEs, experiment READMEs): Write in **Vietnamese**. Keep technical terms in English on first occurrence: "thực thể (entity)", "suy diễn (inference)".
- **Code, tests, configs, docs/**: Write in **English**.
- **Commit messages**: English, conventional commits format.

## Before writing any chapter content

1. Read `docs/BOOK_PEDAGOGY.md` — the canonical authoring policy for concept introduction, forward references, and reader-friction review.
2. Read `docs/SOURCES.md` and `docs/SOURCE_MATRIX.md` to identify authoritative sources for the topic.
3. Read `docs/CURRICULUM_RATIONALE.md` to understand pedagogical sequencing.
4. Verify W3C spec status before referencing — check `docs/SOURCES.md` for current status markers.
5. Never copy text from external sources. Research, understand, write originally, cite.

## Experiment standards

Every experiment MUST have a `README.md` with all 13 required sections (see main README).

Status markers mean:
- ✅ = Actually executed successfully with captured evidence
- 📖 = Requires external service or manual reproduction
- 🚧 = Design/research exercise, not yet implemented

Never mark ✅ without running the experiment and capturing output.

## Code quality

```bash
uv run ruff check .        # Lint
uv run ruff format .       # Format
uv run pytest              # Test
uv run mypy .              # Type check (when configured)
```

All checks must pass before declaring work complete.

## Capstone domain

The recurring capstone is the **Mechanism Knowledge Graph** under `capstone/mechanism_knowledge_system/`. All chapters should contribute examples that build toward this domain. Do not use unrelated toy examples when a mechanism-related example would serve better.

## Key mental models

Always frame content through these two models:

1. **Knowledge Graph = Data Graph + Semantics + Context**
2. **Knowledge System = KG + Acquisition + Inference + Validation + Evolution**

State explicitly that Model 1 is an engineering learning model, not a universal formal definition.

## File naming

- Chapters: `chapter01/`, `chapter02/`, etc. (zero-padded)
- Experiments: `exp_01_<name>/`, `exp_02_<name>/`, etc.
- Datasets: descriptive names, no spaces
- Images: `<chapter>-<concept>.svg` or `.png`

## Testing

- Every experiment needs corresponding tests in its directory
- Tests verify both correctness AND pedagogical intent
- Use pytest with descriptive test names: `test_triple_has_subject_predicate_object`

## Docker

- Neo4j available via `docker-compose.yml`
- Early RDF experiments should NOT require Docker
- Document Docker dependencies in experiment READMEs

## Verification checklist before PR

- [ ] All experiments run and produce expected output
- [ ] Tests pass (`uv run pytest`)
- [ ] Lint passes (`uv run ruff check .`)
- [ ] Vietnamese content uses consistent terminology
- [ ] All external claims have source citations
- [ ] No copied textbook prose
- [ ] Diagrams render correctly
- [ ] Glossary updated with new terms
- [ ] EXPERIMENT_STATUS.md updated with evidence


## Standards Correctness Policy

Passing tests proves implementation conformance to the test oracle. It does NOT prove that the oracle matches RDF/RDFS/OWL/SHACL standards.

For standards-related experiments, tests must reference a semantic contract derived from an authoritative standard:

```
source (e.g., R11-03) → semantic contract → experiment behavior → test oracle
```

When adding or modifying tests for standards-sensitive behavior:
1. Identify the authoritative source ID from `docs/source_index.json`
2. Verify the semantic contract against the fetched source
3. Record the source ID in test comments
4. Never modify expected outputs to match incorrect code; fix the code to match the standard

See `docs/research_notes/R11-03.md` for the canonical RDFS domain/range semantics contract.
