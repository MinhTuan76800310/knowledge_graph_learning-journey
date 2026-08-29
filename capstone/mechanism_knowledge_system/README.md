# capstone/mechanism_knowledge_system/ — Evolving Capstone Domain

The home of the book's capstone domain: a **Mechanism Knowledge System** — a knowledge
graph about mechanisms (physics, control theory, engineering, and beyond) built with a
living epistemic layer. This directory is where the running capstone lives and evolves
across chapters.

## Relation to datasets/mechanism_kg/

- `datasets/mechanism_kg/` holds the **canonical RDF data** (the graph itself) that all
  chapters share, seeded by `RATE_OF_CHANGE`.
- This directory holds the **system-level model**: what the system is, how knowledge
  flows through it, and the design decisions that evolve chapter by chapter.

## Status

- **2026-08-29 (remediation §5):** Directory created. The system is in its seed state —
  the canonical object model is frozen (`docs/MECHANISM_KG_CANONICAL_MODEL.md`), the
  dataset exists (`datasets/mechanism_kg/rate_of_change.ttl`), and `MODEL.md` documents
  the evolving design. Chapters 1–6 build the enabling machinery; the full system is
  completed in Chapter 10.

## Documents

| File | Purpose |
|------|---------|
| `MODEL.md` | The evolving capstone domain model: system definition, knowledge-flow pipeline, current model snapshot, deferred classes |
