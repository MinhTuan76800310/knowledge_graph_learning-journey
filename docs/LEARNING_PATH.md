# Learning Path — Knowledge Graph Book

This document describes the recommended reading order and how concepts build across chapters.

## Prerequisites

- Proficiency in Python (type hints, data structures, file I/O)
- Basic understanding of graphs (nodes, edges, paths)
- Familiarity with command-line tools and virtual environments
- No prior knowledge of RDF, SPARQL, or Neo4j required

## Chapter Progression

| Chapter | Core Question | Key Outcome | Dependencies |
|---------|--------------|-------------|--------------|
| 1 | What turns a graph into knowledge? | Distinguish data graph, taxonomy, ontology, KG | None |
| 2 | How do we represent and query graphs? | RDF vs Property Graph trade-offs | Ch1 |
| 3 | How do we model identity and context? | Entity resolution, reification, named graphs | Ch1-2 |
| 4 | How do we give machine-readable meaning? | RDFS/OWL ontologies, TBox/ABox | Ch1-3 |
| 5 | How do we infer and validate? | Entailment vs SHACL constraints | Ch1-4 |
| 6 | How do we handle claims, time, contradiction? | Provenance-aware knowledge modeling | Ch1-5 |
| 7 | How do we acquire knowledge safely? | Extraction → Candidate → Validated pipeline | Ch1-6 |
| 8 | How do graphs learn patterns? | Embeddings, link prediction, uncertainty | Ch1-7 |
| 9 | How do we retrieve knowledge for agents? | Hybrid retrieval, GraphRAG, evidence trails | Ch1-8 |
| 10 | How do we build a living knowledge system? | Capstone: Mechanism Knowledge System | Ch1-9 |

## Experiment Difficulty Guide

- **★ Beginner**: Run the script, observe output, read explanation. No modifications needed.
- **★★ Intermediate**: Modify parameters, extend queries, compare behaviors. Some coding expected.
- **★★★ Research/Design**: Open-ended exploration. Multiple valid approaches. Requires synthesis.

## Skipping Chapters

Chapters are designed to be sequential. However:
- If you already know RDF/SPARQL, skim Chapter 2 but do Experiment 2-6 (RDF vs Property Graph comparison).
- If you have ontology experience, review Chapter 4's "Mechanism" section as it introduces the capstone domain.
- Chapter 6 (Claims/Provenance) is foundational for Chapters 7-10. Do not skip it.

## Capstone Thread

The Mechanism Knowledge Graph evolves across all chapters. Each chapter adds capabilities to the same evolving system under `capstone/mechanism_knowledge_system/`. By Chapter 10, this becomes a complete living knowledge system.

</content>