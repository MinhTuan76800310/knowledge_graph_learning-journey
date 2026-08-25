# Curriculum Rationale — Knowledge Graph Book

This document explains the pedagogical and structural decisions behind the book's curriculum.
It justifies why topics appear in this order, what mental models drive the progression, and how each chapter connects to the next.

## Pedagogical Philosophy

This book is designed for experienced software engineers who want to understand Knowledge Graphs at a mechanism level — not merely learn a specific tool or framework. The reader should finish the book able to design a custom knowledge system for AI agents, not just query Neo4j or call a GraphRAG API.

The pedagogy is inspired by the structure of `bojieli/ai-agent-book`:
- One unifying abstraction that evolves across chapters
- Progressive difficulty with explicit scaffolding
- Theory paired with runnable experiments at every stage
- Difficulty-rated experiments (★ / ★★ / ★★★)
- Thought questions that require reasoning, not recall
- Reproducible environments via Docker and pinned dependencies
- Chapter-level README files with experiment status
- Source-backed technical writing with traceable citations

**This book does NOT copy any text, diagrams, code, or chapter content from that repository.** Only the pedagogical structure is borrowed.

## Two Mental Models

### Mental Model 1: Knowledge Graph = Data Graph + Semantics + Context

This is an **engineering learning model**, not a universally accepted formal definition. It serves as the conceptual scaffold for the first half of the book.

- **Data Graph**: entities, relations, properties — the structural substrate
- **Semantics**: schema, meaning, ontology, identity, constraints — what makes the graph interpretable
- **Context**: source, provenance, time, scope, confidence — what makes the graph trustworthy and updatable

Chapters 1–5 progressively build each layer. By Chapter 5, the reader has assembled all three components into a working mental model.

### Mental Model 2: Knowledge System = KG + Acquisition + Inference + Validation + Evolution

This model emerges gradually and becomes the architecture of the capstone project (Chapter 10). It reframes the Knowledge Graph not as a static data structure but as a living system with operational concerns.

- **Acquisition**: How knowledge enters the system (Ch7)
- **Inference**: How new knowledge is derived (Ch5, Ch8)
- **Validation**: How knowledge quality is enforced (Ch5, Ch6)
- **Evolution**: How knowledge changes over time (Ch6, Ch10)

## Chapter Progression Logic

Each chapter answers a specific question that naturally arises from the previous chapter's "What We Still Cannot Do" section.

| Chapter | Question Answered | Builds On | Bridges To |
|---------|------------------|-----------|------------|
| 1 | What turns a graph into a *knowledge* graph? | Nothing (starting point) | Need for concrete data models (Ch2) |
| 2 | How do we represent and query knowledge mechanically? | Ch1 concepts | Need for identity and context (Ch3) |
| 3 | How do we handle identity, ambiguity, and context? | Ch2 data models | Need for formal meaning (Ch4) |
| 4 | How do we give machine-readable meaning to the graph? | Ch3 identity/context | Need for inference and validation (Ch5) |
| 5 | How do we infer new knowledge and validate existing knowledge? | Ch4 ontologies | Need for claims, evidence, and time (Ch6) |
| 6 | How do we represent competing claims, provenance, and temporal validity? | Ch5 inference/validation | Need for acquisition pipelines (Ch7) |
| 7 | How do we acquire knowledge without blindly trusting extraction? | Ch6 claims/provenance | Need for inductive learning (Ch8) |
| 8 | How do graphs learn patterns and make uncertain predictions? | Ch7 acquisition | Need for retrieval and QA (Ch9) |
| 9 | How do we retrieve knowledge for humans and LLMs? | Ch8 induction | Need for a living system (Ch10) |
| 10 | How do we design a living knowledge system? | All previous chapters | Capstone integration |

## Why This Order Matters

### Foundations Before Tools
Chapters 1–4 establish conceptual foundations before introducing any specific technology. The reader must understand *what* a Knowledge Graph is before learning *how* to build one with RDF or Neo4j. This prevents tool-centric thinking where the reader conflates Neo4j with Knowledge Graphs.

### Semantics Before Inference
Chapter 4 (Ontologies) must precede Chapter 5 (Deduction/Validation). You cannot reason over a graph whose semantics are undefined. Many tutorials jump to SPARQL queries before establishing what entailment means; this book avoids that trap.

### Claims Before Acquisition
Chapter 6 (Claims/Evidence/Provenance) must precede Chapter 7 (Acquisition). Without understanding that extracted statements are *candidate claims* rather than facts, the reader will build naive ETL pipelines that corrupt canonical knowledge. The mandatory principle "LLM output ≠ Knowledge" requires the claim/evidence vocabulary established in Ch6.

### Deduction Before Induction
Chapter 5 (Deduction) must precede Chapter 8 (Induction). The reader must understand the difference between guaranteed entailment and probabilistic prediction before encountering KG embeddings. Otherwise, ML predictions will be silently treated as asserted facts.

### Retrieval Last
Chapter 9 (Retrieval/GraphRAG) appears only after all foundational layers are in place. GraphRAG is a *consumer* of well-structured knowledge, not a substitute for it. Introducing it earlier would encourage shortcutting the hard work of modeling, validation, and provenance.

## Recurring Capstone: Mechanism Knowledge Graph

Instead of disconnected toy examples, the book maintains one evolving domain throughout: a **Mechanism Knowledge Graph** under `capstone/mechanism_knowledge_system/`.

Core concepts evolve gradually:
- Ch1–3: Basic entities (Book, Chapter, Concept, Definition)
- Ch4: Mechanism, MechanismInput, MechanismOperation, Condition
- Ch5–6: Claim, Evidence, Observation, Hypothesis
- Ch7–8: Experiment, Experience, candidate vs accepted knowledge
- Ch9–10: Full living system with agent interactions

The mechanism concept is chosen because it forces cross-domain abstraction: population growth, temperature change, velocity, and financial growth rate may all instantiate RATE_OF_CHANGE. Recognizing this requires structural signatures, typed inputs, mathematical operators, preconditions, and causal roles — not string similarity. This makes mechanism recognition a genuine research problem suitable for ★★★ experiments.

## Experiment Design Principles

Every experiment follows a fixed template (Question → Hypothesis → Architecture → Run → Observe → Explain → Fail → Extend). This consistency reduces cognitive load and lets the reader focus on content.

Difficulty ratings serve distinct purposes:
- **★**: Verify understanding of a single concept. Should take <15 minutes.
- **★★**: Combine multiple concepts or compare approaches. May take 30–60 minutes.
- **★★★**: Open-ended design/research challenge. No single correct answer. May take hours.

Status markers are honest:
- **✅**: Independently runnable and verified by executing the code
- **📖**: Requires external dependency or manual reproduction step
- **🚧**: Design/research exercise without automated verification

An experiment is NEVER marked ✅ merely because source code exists. It must be executed and evidence captured.

## Language and Terminology Policy

The main book is written in Vietnamese because the target audience is Vietnamese-speaking engineers. However, technical terminology is kept in English on first occurrence with Vietnamese glosses: "thực thể (entity)", "suy diễn (inference)", "nguồn gốc dữ liệu (provenance)".

This policy balances accessibility with precision. Translating technical terms inconsistently causes more confusion than keeping them in English. The glossary (`docs/GLOSSARY.md`) provides consistent mappings.

## Standards Version Awareness

W3C standards evolve. The book explicitly distinguishes:
- **Stable baseline**: W3C Recommendations (RDF 1.1, SPARQL 1.1, OWL 2, SHACL, PROV-O)
- **Current development**: Candidate Recommendations or Working Drafts (RDF 1.2, SPARQL 1.2)
- **Experimental**: Pre-standard proposals

As of 2026-08-25:
- RDF 1.2 Concepts is a Candidate Recommendation Snapshot (2026-04-07)
- SPARQL 1.2 Query is a Working Draft (2026-08-20)
- SHACL 1.2 does not yet exist as a published document; SHACL 1.0 remains stable
- All other referenced specs are stable Recommendations

Callout boxes mark emerging material. The main curriculum never teaches a draft as if it were stable.

## Copyright and Originality

This repository contains ORIGINAL writing. No substantial passages are copied from any source. All external claims are paraphrased and cited. Diagrams are created from scratch using Mermaid or generated SVG. Third-party code is only included after license verification and attribution.

The Hogan et al. textbook (kgbook.org) is used strictly as a research reference. Its conceptual taxonomy informs the book's structure, but no paragraphs, figures, examples, or substantial wording are reproduced.

</parameter>