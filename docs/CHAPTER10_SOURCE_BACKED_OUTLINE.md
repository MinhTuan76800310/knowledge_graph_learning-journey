# Chapter 10 Source-Backed Outline

**Chapter:** 10 — Building a Living Knowledge System / Xây dựng Hệ thống Tri thức Sống
**Status:** OUTLINE (P4) — sources registered 2026-08-31
**Spec:** user_prompt/create_chapter10.md

## Central mechanism (confirmed)

The **Monitoring Loop**:

    COLLECT observations → AGGREGATE into metrics → COMPARE against thresholds (policy)
    → ALERT → ASSESS (epistemic, governed) → ACT (re-validate / re-assess / retire /
    supersede / ingest) → RE-MEASURE

It is the chapter's central mechanism because every other Ch10 concept (staleness
detection, feedback loops, contradiction debt, quality dimensions, maintenance
operations, audit, trust) plugs into it as a stage, a trigger, or a governed action.
Target depth 5.

## Concept → source mapping

| # | Concept section | Depth | Primary source(s) | Reuse |
|---|-----------------|-------|-------------------|-------|
| 1 | From static artifact to living system | 4 | NELL-01, HIDDENTECH-01 | — |
| 2 | Six flows of change | 4 | ONTEVOL-01, ONTVR-01 | Ch3/Ch4, Ch6, Ch7, Ch8, Ch9 |
| 3 | Staleness detection | 5 | DRIFT-01, TKG-01 | Ch6 clocks, Ch9 index lag |
| 4 | Freshness as a first-class metric | 4 | KGQ-01, DQSTD-01 | Ch9 §9.57 |
| 5 | Freshness ≠ correctness | 4 (boundary) | KGQ-01, BENCH-01 | Ch9 correctness–groundedness 2×2 |
| 6 | Valid/system/assessment clocks at system scale | 4 | TKG-01 | Ch6 clocks |
| 7 | Self-observation / observability | 4 | NELL-01, HIDDENTECH-01 | Ch9 logs |
| 8 | What to log / what to measure | 4 | KGQ-01, DQSTD-01 | — |
| 9 | **Monitoring loop (CENTRAL)** | 5 | HIDDENTECH-01, CASCADE-01 | Ch6 governance, Ch7 pipeline |
| 10 | Aggregation windows | 4 | Gama DRIFT-01 | — |
| 11 | Thresholds as policy | 4 | DQSTD-01, GOVDATA-01 | Ch6 governance states |
| 12 | Threshold ≠ truth | 4 (boundary) | BENCH-01 | Ch9 score ≠ confidence |
| 13 | Alerting | 4 | CASCADE-01 | — |
| 14 | Assessment step | 4 | REFINE-01 | Ch6 assessment |
| 15 | Monitored ≠ governed | 4 (boundary) | GOVDATA-01 | Ch6/Ch7 |
| 16 | Feedback loops | 4 | HIDDENTECH-01, Sculley, DRIFT-01 | Ch8 hypotheses |
| 17 | QA answers → candidate claims | 4 | — (book rule from Ch9 §9.59) | Ch7 pipeline, Ch9 |
| 18 | User corrections | 4 | NELL-01 | Ch7 CandidateKnowledge |
| 19 | Feedback ≠ evidence | 4 (boundary) | — | Ch6 evidence chain |
| 20 | Feedback loop safety | 5 | HIDDENTECH-01, COLLAPSE-01 | Ch7 governance gate |
| 21 | Contradiction accumulation | 4 | REFINE-01, CASCADE-01 | Ch6 C471/C210 |
| 22 | Contradiction debt | 4 | HIDDENTECH-01, CASCADE-01 | Ch6 |
| 23 | Escalation policy | 4 | GOVDATA-01 | Ch6 |
| 24 | Knowledge quality dimensions | 5 | KGQ-01, DQSTD-01 | — |
| 25 | Correctness over time | 4 | REFINE-01 | Ch6 evidence |
| 26 | Completeness over time | 4 | REFINE-01, KVLT-01 | — |
| 27 | Freshness over time | 4 | KGQ-01, TKG-01 | — |
| 28 | Consistency over time | 4 | KGQ-01 | Ch6 |
| 29 | Trustworthiness | 4 | KGQ-01, GOVDATA-01 | Ch6 provenance, Ch7 |
| 30 | Levels vs trends | 4 | DRIFT-01 | — |
| 31 | Quality ≠ truth | 4 (boundary) | BENCH-01 | Ch9 |
| 32 | Degradation | 4 | DRIFT-01, CASCADE-01 | — |
| 33 | Benchmark decay | 4 | BENCH-01 | Ch9 |
| 34 | Feedback collapse | 5 | COLLAPSE-01, HIDDENTECH-01 | Ch9 §9.46–9.50 |
| 35 | Model collapse | 4 | COLLAPSE-01 (Ch8 reuse) | Ch8 |
| 36 | Collapse ≠ staleness | 4 (boundary) | COLLAPSE-01, DRIFT-01 | — |
| 37 | Maintenance operations | 5 | REFINE-01, ONTEVOL-01 | Ch6/Ch7 |
| 38 | Re-validation at scale | 4 | REFINE-01, KVLT-01 | — |
| 39 | Re-assessment | 4 | ONTEVOL-01 | Ch6 |
| 40 | Retirement | 4 | ONTEVOL-01, ONTVR-01 | Ch6 |
| 41 | Supersession at scale | 4 | ONTVR-01 | Ch6 |
| 42 | Batch governance operations | 4 | ONTEVOL-01, GOVDATA-01 | — |
| 43 | System-level audit trails | 5 | GOVDATA-01 | Ch6 provenance, Ch9 provenance |
| 44 | Controlled trust | 4 | GOVDATA-01 | Ch7 registered sources |
| 45 | Trust ≠ blind trust | 4 (boundary) | BENCH-01 | — |
| 46 | The living architecture | 5 | NELL-01, HIDDENTECH-01 | all chapters |
| 47 | Orchestration of the loops | 4 | HIDDENTECH-01 | — |
| 48 | Automation gradient | 4 | GOVDATA-01 | Ch6 |
| 49 | Auto-repair ≠ auto-truth | 4 (boundary) | COLLAPSE-01 | Ch6/Ch7 |
| 50 | The system is never "done" | 4 | NELL-01 | Ch9 §9.79 bridge |
| 51 | Open problems → Afterword | 4 | — (book-defined) | — |
| 52 | Worked case: system health report | 5 | all metrics sources | C471/C210 |
| 53 | Worked case: stale accepted claim | 5 | DRIFT-01, TKG-01 | C471/E88 |
| 54 | Worked case: feedback loop gone wrong | 5 | COLLAPSE-01, HIDDENTECH-01 | Ch7 gate |

## Boundary table (protected distinctions)

| Distinction | Supported by |
|-------------|--------------|
| fresh ≠ correct | KGQ-01 (timeliness vs accuracy), BENCH-01 |
| monitored ≠ governed | GOVDATA-01, DQSTD-01 |
| measured ≠ understood | KGQ-01 (dimensions ≠ truth) |
| feedback ≠ evidence | Ch6 evidence chain (book rule) |
| versioned ≠ verified | ONTVR-01 |
| auto-repair ≠ auto-truth | COLLAPSE-01 |
| knowledge debt ≠ code debt | HIDDENTECH-01 (adapted) |
| collapse ≠ staleness | COLLAPSE-01 vs DRIFT-01 |
| trust ≠ blind trust | GOVDATA-01 |
| maintenance ≠ unreviewed change | ONTEVOL-01 |
| quality score ≠ truth | BENCH-01 |

## Source registration summary (P3)

| ID | Source | Bib key | Status |
|----|--------|---------|--------|
| KGQ-01 | Zaveri et al., Semantic Web 2016 | `zaveri-kgquality-2016` | FETCHED_AND_VERIFIED |
| REFINE-01 | Paulheim, Semantic Web 2017 | `paulheim-refinement-2017` | FETCHED_AND_VERIFIED |
| ONTEVOL-01 | Noy & Klein, KAIS 2004 | `noy-ontology-evolution-2004` | FETCHED_AND_VERIFIED |
| ONTVR-01 | Klein & Fensel, SWWS 2001 | `klein-ontology-versioning-2001` | FETCHED_AND_VERIFIED |
| KVLT-01 | Dong et al., KDD 2014 | `dong-knowledge-vault-2014` | FETCHED_AND_VERIFIED |
| NELL-01 | Mitchell et al., CACM 2018 | `mitchell-neverending-2018` | FETCHED_AND_VERIFIED |
| DRIFT-01 | Gama et al., ACM CSUR 2014 | `gama-drift-2014` | FETCHED_AND_VERIFIED |
| DRIFT-02 | Widmer & Kubat, ML 1996 | `widmer-drift-1996` | FETCHED_AND_VERIFIED |
| HIDDENTECH-01 | Sculley et al., NIPS 2015 | `sculley-debt-2015` | FETCHED_AND_VERIFIED |
| BENCH-01 | Recht et al., ICML 2019 | `recht-imagenet-2019` | FETCHED_AND_VERIFIED |
| CASCADE-01 | Sambasivan et al., CHI 2021 | `sambasivan-cascades-2021` | FETCHED_AND_VERIFIED |
| DQSTD-01 | ISO/IEC 25012:2008 | `iso-25012-2008` | FETCHED_METADATA_ONLY |
| GOVDATA-01 | ISO 8000-1:2022 | `iso-8000-2022` | FETCHED_METADATA_ONLY |
| TKG-01 | Cai et al., IJCAI 2023 | `cai-tkgc-2023` | FETCHED_AND_VERIFIED |
| COLLAPSE-01 | Shumailov et al., Nature 2024 | `shumailov-collapse-2024` | reused from Ch8 (tagged ["8","10"]) |

## Registering (done)

- `docs/source_index.json` — 14 new records (91 total), COLLAPSE-01 tagged ["8","10"]
- `book/references.bib` — 14 new keys (88 total), 0 duplicates
- `docs/CITATION_MAP.md` — 14 new rows + Ch10 note
- `docs/research_notes/` — 14 new notes

## Validation (P3 exit)

- `python -m pytest` → 95 passed
- `python -m ruff check .` → clean
- `python -m ruff format --check .` → clean

Next: P5 — `docs/CHAPTER10_SEMANTIC_CONTRACTS.md`.
