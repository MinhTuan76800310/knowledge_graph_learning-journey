# Documentation Index — Knowledge Graph Book

This directory contains the foundational specifications, pedagogical standards, source verification archives, semantic contracts, and acceptance review records for the **Knowledge Graph Book** project.

---

## 🗺️ Documentation Map

### 1. Milestones, Status & Roadmaps
- [`BOOK_STATUS.md`](BOOK_STATUS.md) — Real-time publication status of each manuscript section across both Vietnamese and English editions.
- [`BOOK_V0_3_MILESTONE.md`](BOOK_V0_3_MILESTONE.md) — Comprehensive specification for the **Theoretical Rigor & Frontier AI Upgrade** (Pillars 1–6) across all 10 chapters.
- [`BOOK_V0_4_ROADMAP.md`](BOOK_V0_4_ROADMAP.md) — Strategic roadmap for Version 0.4: Neuro-Symbolic Information Extraction, Structural Causal Models (SCMs), Vector-Graph Entity Resolution, and Conformal Prediction.
- [`BOOK_V0_1_MILESTONE.md`](BOOK_V0_1_MILESTONE.md) — Baseline specification for the initial complete Vietnamese manuscript release.

---

### 2. Pedagogical Standards & Curriculum Design
- [`BOOK_PEDAGOGY.md`](BOOK_PEDAGOGY.md) — **The canonical authoring policy**: Concept introduction guidelines, mechanism-first prose patterns, forward-reference prevention, and epistemic honesty rules.
- [`CURRICULUM_RATIONALE.md`](CURRICULUM_RATIONALE.md) — Pedagogical sequencing rationale: Why foundations precede tools, why deduction precedes induction, and why retrieval is placed last.
- [`LEARNING_PATH.md`](LEARNING_PATH.md) — Reader guide: Recommended progression paths, prerequisites, and experiment difficulty ratings.

---

### 3. Sources, Citations & Research Notes
- [`source_index.json`](source_index.json) — Canonical machine-readable registry of all 92+ foundational sources with W3C status, DOIs, and URLs.
- [`SOURCES.md`](SOURCES.md) & [`SOURCE_MATRIX.md`](SOURCE_MATRIX.md) — Exhaustive source index categorizing W3C Recommendations, seminal papers, textbooks, and tool specifications.
- [`CITATION_MAP.md`](CITATION_MAP.md) — Chapter-by-chapter mapping of concepts to authoritative citations.
- [`research_notes/`](research_notes/) — Individual per-source analysis files verifying claims and formal semantics (e.g., `R11-03.md` for RDFS domain/range entailment contracts).

---

### 4. Capstone Architecture: Mechanism Knowledge Graph
- [`MECHANISM_KG_CANONICAL_MODEL.md`](MECHANISM_KG_CANONICAL_MODEL.md) — Formal schema and architectural definitions for the recurring physical/computational mechanism domain.
- [`MECHANISM_KG_TEACHING_COVERAGE.md`](MECHANISM_KG_TEACHING_COVERAGE.md) — Audit of how each chapter advances the Mechanism KG capstone domain from basic graphs to autonomous cybernetic feedback loops.
- [`TERMINOLOGY_GLOSS_MECHANISM.md`](TERMINOLOGY_GLOSS_MECHANISM.md) — Bilingual technical glossary and translation mappings.

---

### 5. Semantic Contracts & Chapter Acceptance Checkpoints
Every chapter in the manuscript must fulfill formal semantic contracts and pass an independent acceptance audit before release:

| Chapter | Semantic Contracts | Acceptance Checkpoint | Depth Review / Audit |
|---|---|---|---|
| **Ch 1** | [`CHAPTER01_SEMANTIC_CONTRACTS.md`](CHAPTER01_SEMANTIC_CONTRACTS.md) | Included in Preview | [`BOOK_CH1_CH3_DEEP_READABILITY_AUDIT.md`](BOOK_CH1_CH3_DEEP_READABILITY_AUDIT.md) |
| **Ch 2** | [`CHAPTER02_SEMANTIC_CONTRACTS.md`](CHAPTER02_SEMANTIC_CONTRACTS.md) | [`CHAPTER02_RDF_CHECKPOINT.md`](CHAPTER02_RDF_CHECKPOINT.md) | [`BOOK_CH1_CH2_CONTENT_AUDIT.md`](BOOK_CH1_CH2_CONTENT_AUDIT.md) |
| **Ch 3** | [`CHAPTER03_SEMANTIC_CONTRACTS.md`](CHAPTER03_SEMANTIC_CONTRACTS.md) | [`CHAPTER03_BOOK_CHECKPOINT.md`](CHAPTER03_BOOK_CHECKPOINT.md) | [`BOOK_CONCEPT_DEPTH_AUDIT.md`](BOOK_CONCEPT_DEPTH_AUDIT.md) |
| **Ch 4** | [`CHAPTER04_SEMANTIC_CONTRACTS.md`](CHAPTER04_SEMANTIC_CONTRACTS.md) | [`CHAPTER04_BOOK_CHECKPOINT.md`](CHAPTER04_BOOK_CHECKPOINT.md) | [`BOOK_DEPTH_REMEDIATION_PLAN.md`](BOOK_DEPTH_REMEDIATION_PLAN.md) |
| **Ch 5** | [`CHAPTER05_SEMANTIC_CONTRACTS.md`](CHAPTER05_SEMANTIC_CONTRACTS.md) | [`CHAPTER05_BOOK_CHECKPOINT.md`](CHAPTER05_BOOK_CHECKPOINT.md) | [`PHASE0_6_CLOSURE_REPORT.md`](PHASE0_6_CLOSURE_REPORT.md) |
| **Ch 6** | [`CHAPTER06_SEMANTIC_CONTRACTS.md`](CHAPTER06_SEMANTIC_CONTRACTS.md) | [`CHAPTER06_BOOK_CHECKPOINT.md`](CHAPTER06_BOOK_CHECKPOINT.md) | [`POST_REMEDIATION_AUDIT.md`](POST_REMEDIATION_AUDIT.md) |
| **Ch 7** | [`CHAPTER07_SEMANTIC_CONTRACTS.md`](CHAPTER07_SEMANTIC_CONTRACTS.md) | [`CHAPTER07_BOOK_CHECKPOINT.md`](CHAPTER07_BOOK_CHECKPOINT.md) | [`CHAPTER07_DEPTH_REVIEW.md`](CHAPTER07_DEPTH_REVIEW.md) |
| **Ch 8** | [`CHAPTER08_SEMANTIC_CONTRACTS.md`](CHAPTER08_SEMANTIC_CONTRACTS.md) | [`CHAPTER08_BOOK_CHECKPOINT.md`](CHAPTER08_BOOK_CHECKPOINT.md) | [`CHAPTER08_DEPTH_REVIEW.md`](CHAPTER08_DEPTH_REVIEW.md) |
| **Ch 9** | [`CHAPTER09_SEMANTIC_CONTRACTS.md`](CHAPTER09_SEMANTIC_CONTRACTS.md) | [`CHAPTER09_BOOK_CHECKPOINT.md`](CHAPTER09_BOOK_CHECKPOINT.md) | [`CHAPTER09_DEPTH_REVIEW.md`](CHAPTER09_DEPTH_REVIEW.md) |
| **Ch 10** | [`CHAPTER10_SEMANTIC_CONTRACTS.md`](CHAPTER10_SEMANTIC_CONTRACTS.md) | [`CHAPTER10_BOOK_CHECKPOINT.md`](CHAPTER10_BOOK_CHECKPOINT.md) | [`EN_VI_CH10_PILLAR6_REVIEW.md`](EN_VI_CH10_PILLAR6_REVIEW.md) |
| **Ch 11** | [`CHAPTER11_SEMANTIC_CONTRACTS.md`](CHAPTER11_SEMANTIC_CONTRACTS.md) | Scheduled (v0.4.0) | Scheduled (v0.4.0) |
| **Ch 12** | [`CHAPTER12_SEMANTIC_CONTRACTS.md`](CHAPTER12_SEMANTIC_CONTRACTS.md) | Scheduled (v0.4.0) | Scheduled (v0.4.0) |
| **Ch 13** | [`CHAPTER13_SEMANTIC_CONTRACTS.md`](CHAPTER13_SEMANTIC_CONTRACTS.md) | Scheduled (v0.4.0) | Scheduled (v0.4.0) |
| **Ch 14** | [`CHAPTER14_SEMANTIC_CONTRACTS.md`](CHAPTER14_SEMANTIC_CONTRACTS.md) | Scheduled (v0.4.0) | Scheduled (v0.4.0) |

---

### 6. Experiments & Validation Suites
- [`EXPERIMENT_STATUS.md`](EXPERIMENT_STATUS.md) — Live tracking of all 106 automated tests, experiment execution status, and PDF verification gates.
- [`LAB_BACKLOG.md`](LAB_BACKLOG.md) — Design documents and backlog for standalone Docker-based interactive lab exercises.
