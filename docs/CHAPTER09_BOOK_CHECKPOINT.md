# Chapter 9 Book Checkpoint

**Chapter:** 9 — Retrieval, Question Answering, and GraphRAG / Truy xuất, Hỏi đáp và GraphRAG
**Status:** DRAFT COMPLETE — pending PR review (branch `chapter09-retrieval-qa-graphrag`)
**Date:** 2026-08-31

## Acceptance criteria met

| Criterion | Status | Evidence |
|-----------|--------|----------|
| Research complete | ✅ | 14 Ch9 sources registered and verified in docs/source_index.json |
| Manuscript drafted | ✅ | 79 sections (§9.1–§9.79), ~2470 lines |
| Semantic contracts defined | ✅ | 75 concept records + 13 collision rows in docs/CHAPTER09_SEMANTIC_CONTRACTS.md |
| Semantic review passed | ✅ | 75/75 PASS, 0 FAIL, 0 PARTIAL |
| Depth review passed | ✅ | docs/CHAPTER09_DEPTH_REVIEW.md: 77/77 major concepts depth ≥4 (20 at depth 5), 16/16 critical boundaries PASS, 50/50 reader capabilities = YES |
| Reader capability test | ✅ | Q01–Q50 ALL = YES (see docs/CHAPTER09_DEPTH_REVIEW.md) |
| Editorial review passed | ✅ | No blocking issues |
| Source index updated | ✅ | 14 new Ch9 source records (RAG-01, DPR-01, GRAPHRAG-01, BM25-01, IRBOOK-01, NDCG-01, RRF-01, RRANK-01, LOSTMID-01, AIS-01, CITE-01, KGQA-01, LLMKG-01, MAGRAPH-01) |
| Bibliography updated | ✅ | 18 Ch9 bib keys cited and resolved in references.bib |
| Citation map updated | ✅ | 14 new rows in docs/CITATION_MAP.md |
| Research notes | ✅ | 14 new research notes in docs/research_notes/ |
| TikZ figures created | ✅ | 9 figures: full-stack, multihop-subgraph, ledger-vs-canonical, topk-bound, evidence-packet, correctness-grounding, query-router, text-vs-graph-vs-hybrid, kgqa-rag-graphrag |
| TikZ compilation | ✅ | All 9 Ch9 figures compiled with lualatex |
| Concept registry updated | ✅ | 77 Ch9 concepts in book/concept_registry.yaml |
| Glossary updated | ✅ | 59 Ch9 terms added; book/glossary.md now 172 entries |
| Book manifest updated | ✅ | chapter09.md added before glossary.md |
| Tests pass | ✅ | 95 passed (11 new Ch9 integrity tests) |
| ruff check | ✅ | 0 errors |
| ruff format --check | ✅ | clean |
| PDF build | ✅ | 322 print pages (A4); Ch9 = pp. 251–322 incl. glossary+references; 0 LaTeX errors; 0 undefined citations |
| PR / merge | ⏳ | PR pending (Issue #17) |

## Key design decisions

1. **Retrieval is not truth-finding** — the whole chapter is built on the boundary chain retrieved ≠ evidence, score ≠ confidence, grounded ≠ true, faithful ≠ correct, path ≠ proof.
2. **9 intent types** — factual/structural/comparative/explanatory/provenance/temporal/contradiction/discovery/multi-hop; intent determines retrieval source and evidence type.
3. **Index ≠ KG** — a derived access structure that can lag the ledger; three entities (KG, ledger, index) kept distinct.
4. **top_k as epistemic bound** — the model cannot reason over evidence it does not see; not-in-top_k is not a statement about the world.
5. **BOOK-DEFINED Evidence Packet** — the single structured interface between retrieval and answer synthesis; full fields ≠ sufficient evidence.
6. **BOOK-DEFINED Query Execution Router** — decides the execution path (KGQA / symbolic / text RAG / GraphRAG / ledger) from the understood question.
7. **BOOK-DEFINED Answer artifact** — answer provenance: generatedFor, usedEvidence, generatedBy, modelVersion, citations, answerStatus.
8. **2×2 correctness × groundedness** — cell C is the target; faithful-to-wrong-source (cell B) cannot be turned into C by a correct process.
9. **Unknown vs Not Found** — 5-state chain: not retrieved ≠ not in index ≠ not in KG ≠ known false ≠ unknown; retrieval failure ≠ knowledge absence.
10. **GraphRAG as a family** — not one standard algorithm; Microsoft GraphRAG is one implementation; no hallucination guarantee.
11. **QA answer ≠ knowledge ingestion** — answers never enter the ledger directly; the Ch7 governance pipeline remains the only ingestion path.
12. **Capability ladder ending at Ch9** — Ch10 is bridged but not started.

## Misconceptions addressed (34 ⚠️ callouts)

A representative sample (all callouts use ⚠️ in the manuscript):

1. Retrieved then answered — No (retrieved ≠ evidence)
2. High retrieval score = confident — No (score semantics)
3. BM25 understands semantics — No (lexical only)
4. Similar embeddings = same meaning — No (vector ≠ meaning)
5. Dense always beats lexical — No (complementary)
6. More signals = more truth — No (hybrid reduces misses)
7. top_k is implementation detail — No (epistemic bound)
8. Not in top_k = does not exist — No (OWA)
9. Index is the knowledge — No (index ≠ KG)
10. Ledger answers = canonical answers — No (two epistemic domains)
11. Ask history with current state — No (multiple clocks)
12. A path proves the conclusion — No (path ≠ proof)
13. Deeper traversal always better — No (depth bounds)
14. Within k-hop = relevant — No (k-hop ≠ relevance)
15. Summary replaces source — No (summary ≠ source)
16. Compression loses nothing — No (may drop decisive evidence)
17. Context order does not matter — No (lost in the middle)
18. Full evidence packet = sufficient — No (packet ≠ sufficiency)
19. Grounded = correct — No (cell B)
20. Fluent answer = correct answer — No (fluency ≠ correctness)
21. Has citation = supported — No (citation precision)
22. More citations = better citations — No (citation recall)
23. Faithful = correct — No (faithfulness ≠ correctness)
24. Not found → does not exist — No (unknown vs not found)
25. Answer error → knowledge error — No (retrieval failure ≠ knowledge absence)
26. Abstention is a failure — No (can be correct behavior)
27. GraphRAG is a standard algorithm — No (family of architectures)
28. KGQA = GraphRAG — No (different mechanisms)
29. GraphRAG replaces KGQA for exact queries — No (decision table)
30. GraphRAG removes hallucination — No (no guarantee)
31. QA answer becomes new knowledge — No (governance required)
32. LLM replaces graph reasoning — No (two machines)
33. Chosen path was proven — No (path explosion hides alternatives)
34. All questions need RAG — No (when NOT to use RAG)

## Self-explanation checkpoints (8)

1. Canonical View vs Ledger: which domain for "Định nghĩa current 2020?" (§9.73)
2. BM25 score gap semantics: can we conclude "0.2 units more confident"? (§9.73)
3. top_k=5 with decisive evidence at rank 6 — which layer failed (§9.61, §9.73)
4. Community summary as evidence: what is missing to make it evidence (§9.73)
5. asserted/derived/predicted for "vận tốc là tốc độ biến thiên" (§9.73)
6. Cell B: why correct process cannot move B to C (§9.42, §9.73)
7. Agentic retrieval: three failure mechanisms after 4th/5th successful turn (§9.46–9.50)
8. "No mechanism other than RATE_OF_CHANGE" — which epistemic label (§9.60)

## Renderer usage

| Type | Count | Details |
|------|-------|--------|
| TikZ figures | 9 | full-stack, multihop-subgraph, ledger-vs-canonical, topk-bound, evidence-packet, correctness-grounding, query-router, text-vs-graph-vs-hybrid, kgqa-rag-graphrag |
| Tables | 25+ | 9-intent, retrieval unit, lexical vs dense, governance state, decision table, 7-layer, hallucination, 34 misconceptions, depth audit, capability test, glossary |
| Code blocks | 30+ | SPARQL, retrieval plan, JSON Evidence Packet, Turtle, formulas |
| Mermaid | 0 | All formal diagrams use TikZ per renderer policy |

## Constraints carried forward

- Do NOT resume deferred labs (EXP-9-1..EXP-9-9 deferred to book v0.1)
- Do NOT start Chapter 10 (only a bridge in §9.79)
- All external claims traceable to docs/source_index.json / references.bib
- BOOK-DEFINED terms labeled explicitly (Evidence Packet, Query Execution Router, Answer artifact)
- Mechanism-KG consistency: RATE_OF_CHANGE domain with VelocityDerivativeApplication/CurrentDerivativeApplication/PopulationDerivativeApplication
- Use local git commit so author shows as "MinhTuan76800310"

## Remaining work

PR review and merge for Chapter 9. Chapter 10 only when a new GitHub task authorizes it.