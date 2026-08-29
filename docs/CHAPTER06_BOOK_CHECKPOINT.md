# Chapter 6 Book Checkpoint

**Chapter:** 6 — Claims, Evidence, Provenance, Time, and Contradiction
**Status:** ACCEPTED
**Date:** 2026-08-29

## Acceptance criteria met

| Criterion | Status | Evidence |
|-----------|--------|----------|
| Research complete | ✅ | PROV-O, PROV-DM, OWL-Time, Wikidata statements/qualifiers/references/ranks fetched and verified |
| Manuscript drafted | ✅ | 22 sections (§6.0–§6.22), ~1150 lines |
| Semantic contracts defined | ✅ | 28 records in docs/CHAPTER06_SEMANTIC_CONTRACTS.md |
| Semantic review passed | ✅ | 28/28 PASS, 0 FAIL, 0 PARTIAL |
| Editorial review passed | ✅ | No blocking issues; 2 low-priority gloss fixes applied |
| TikZ figures created | ✅ | 5 figures: epistemic-model, prov-chain, contradiction-taxonomy, temporal-clocks, epistemic-layers |
| TikZ compilation | ✅ | All 13 figures (8 Ch4-5 + 5 Ch6) compile without errors |
| PDF build | ✅ | 124 pages, no LaTeX errors, no undefined citations |
| Tests pass | ✅ | 43 passed, 1 skipped |
| Concept registry updated | ✅ | 29 Ch6 entries in book/concept_registry.yaml |
| Source index updated | ✅ | PROV-DM-01, OWL-TIME-01 registered; PROV-01 pre-existing |
| Bibliography updated | ✅ | prov-o, prov-dm, owl-time entries added to references.bib |
| Research notes | ✅ | docs/research_notes/PROV-DM-01.md, OWL-TIME-01.md |

## Key design decisions

1. **Epistemic model is BOOK-DEFINED** — Observation → Assertion → Claim → Evidence → Accepted Knowledge is not a W3C standard. Clearly labeled throughout.
2. **Claim as first-class object** via n-ary pattern (stable RDF baseline, not RDF 1.2 Triple Terms).
3. **RDF 1.2 Triple Terms** mentioned as emerging development, not baseline.
4. **Five contradiction types** with context dissolution procedure (identity, predicate semantics, temporal scope, spatial/jurisdictional scope).
5. **Four temporal clocks** explicitly distinguished: valid time, assertion time, observation time, system time.
6. **LLM output = CandidateKnowledge** requiring independent evidence; LLM cannot be its own verification evidence.
7. **Governance states**: Candidate, Accepted, Rejected, Contested, Superseded — accepted ≠ eternal truth.
8. **Source ≠ Evidence** distinction maintained throughout.
9. **Contradiction preservation** — never delete losing claims; preserve provenance, contexts, support, assessment.
10. **Claim identity ≠ content identity** — C₁ ≠ C₂ even when content(C₁) = content(C₂).

## Misconceptions addressed (10 callouts)

1. Epistemic model is W3C standard → No, book-defined framework
2. Source uy tín → phát biểu đúng → No, source reliability ≠ claim truth
3. Nhiều bằng chứng hỗ trợ → phát biểu đúng → No, quantity ≠ quality
4. Thời gian trong RDF là valid time → No, RDF has no built-in temporal semantics
5. Confidence = xác suất phát biểu đúng → No, confidence is multi-dimensional
6. Phát biểu mới luôn đúng hơn phát biểu cũ → No, newer ≠ truer
7. Hệ thống tri thức phải nhất quán → No, contradiction preservation is a feature
8. LLM nói đúng → phát biểu đúng → No, LLM output = CandidateKnowledge
9. Không có claim về P → P sai → No, absence ≠ negation (OWA)
10. Hai nguồn nói khác nhau → hệ thống bất nhất → No, contextualized claims maintain consistency

## Self-explanation checkpoints (7)

1. Assertion vs Claim distinction (§6.2)
2. Proposition → Assertion → Claim exercise (§6.2)
3. PROV chain drawing exercise (§6.4)
4. Contradiction classification exercise (§6.6)
5. Wikidata rank design explanation (§6.9)
6. Accepted ≠ True explanation (§6.12)
7. Three end-of-chapter synthesis checkpoints (§6.22)

## Renderer usage

| Type | Count | Details |
|------|-------|--------|
| TikZ figures | 5 | epistemic-model, prov-chain, contradiction-taxonomy, temporal-clocks, epistemic-layers |
| Tables | 12+ | Contradiction types, temporal clocks, governance states, confidence types, etc. |
| Code blocks | 8+ | Turtle examples for claims, PROV chains, Wikidata mappings |
| Mermaid | 0 | All formal diagrams use TikZ per renderer policy |

## Constraints carried forward

- Do NOT resume deferred labs
- Do NOT install Neo4j
- SHACL 1.2 Core (SH-02) = CURRENT DEVELOPMENT ONLY; stable baseline is SH-01
- OWL-Time is stable REC (2020), not CR Draft — correctly labeled in manuscript
- Book quality > lab completeness
- All external claims cite sources from docs/SOURCES.md / references.bib
- Use GitHub MCP for commits so author shows as "MinhTuan76800310"
- DO NOT start Chapter 7 until explicitly requested
