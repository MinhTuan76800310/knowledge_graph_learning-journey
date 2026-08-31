# Chapter 9 — ACCEPTED (2026-08-31)

Chapter 9 (Retrieval, Question Answering, and GraphRAG / Truy xuất, Hỏi đáp và GraphRAG)
has passed the full acceptance gate: semantic review 75/75 PASS (+ 13 collision rows),
depth review PASS (77/77 major concepts depth ≥4, 20 at depth 5, 1 at depth 6), reader
capability test Q01–Q56 ALL = YES, editorial review clean, PDF verified.
Status: ACCEPTED.

## Current state

- Chapters 1–9 are ACCEPTED
- Book PDF builds to 322 pages (print); Chapter 9 = physical pages 251–322
- All tests pass: 95 passed
- `ruff check .` clean; `ruff format --check .` clean
- Semantic contracts: docs/CHAPTER09_SEMANTIC_CONTRACTS.md (75 records + 13 collision rows, all PASS)
- Depth review: docs/CHAPTER09_DEPTH_REVIEW.md (depth table, 16 critical boundaries,
  capability test Q01–Q56, pipeline table)
- Manuscript: 79 sections (§9.1–§9.79), ~2470 lines
- 9 new TikZ figures (36 total in book), all compile
- 14 new sources registered (RAG-01, DPR-01, GRAPHRAG-01, BM25-01, IRBOOK-01, NDCG-01,
  RRF-01, RRANK-01, LOSTMID-01, AIS-01, CITE-01, KGQA-01, LLMKG-01, MAGRAPH-01) —
  all FETCHED_AND_VERIFIED
- Checkpoint: docs/CHAPTER09_BOOK_CHECKPOINT.md

## Key design decisions (Chapter 9)

- Retrieval is not truth-finding: retrieved ≠ evidence, score ≠ confidence, grounded ≠
  true, faithful ≠ correct, path ≠ proof, summary ≠ source, QA answer ≠ accepted knowledge
- 9 intent types (factual/structural/comparative/explanatory/provenance/temporal/
  contradiction/discovery/multi-hop); intent decides retrieval source and evidence type
- Index ≠ KG ≠ ledger: the index is a derived access structure that can lag behind
- top_k is an epistemic bound, not neutral plumbing: not-in-top_k is not a statement
  about the world (OWA)
- BOOK-DEFINED Evidence Packet: the interface between retrieval and answer synthesis;
  full fields ≠ sufficient evidence
- BOOK-DEFINED Query Execution Router: decides KGQA / symbolic / text RAG / GraphRAG /
  ledger path from the understood question
- BOOK-DEFINED Answer artifact: generatedFor, usedEvidence, generatedBy, modelVersion,
  citations, answerStatus
- 2×2 correctness × groundedness: cell C is the target; cell B (faithful to wrong source)
  cannot be turned into C by a correct process
- Unknown vs Not Found: 5-state chain (not retrieved ≠ not in index ≠ not in KG ≠ known
  false ≠ unknown); retrieval failure ≠ knowledge absence
- GraphRAG is a family of architectures (Leiden → community → summarize), not one
  standard algorithm; no hallucination guarantee
- QA answers never enter the ledger directly; the Ch7 governance pipeline remains the
  only ingestion path

## Next steps

- Chapter 10 (Building a Living Knowledge System) is the final chapter — system-level
  governance and operations: self-monitoring, staleness detection, feedback loops,
  accumulated contradictions, knowledge-quality measurement over time. It takes up the
  §9.79 bridge (the system is never "done" — it must be measured, maintained, and
  trusted under control).
- After Chapter 10: Afterword, then the v0.1 release (tag + versioned PDF).

## Constraints carried forward

- Do NOT resume deferred labs (EXP-9-1..EXP-9-9 deferred to book v0.1)
- All external claims must cite sources from docs/source_index.json / references.bib
- Use local git commit so author shows as "MinhTuan76800310"
- DO NOT start Chapter 10 until the next GitHub task authorizes it
