# Phase 0.5 Semantic & Evidence Audit Report

**Date:** 2026-08-25  
**Auditor:** AI Assistant (Qwen3.8)  
**Scope:** Chapter 1 content, experiments, tests, research artifacts, repository metadata  
**Verdict:** ✅ **GO for Chapter 2**

---

## Errors Found

### E1: RDFS domain/range presented as validation constraints

- **Original claim:** Chapter 1 and experiment 1-5 implied that `rdfs:domain` / `rdfs:range` act as validation constraints that would detect or reject invalid subjects/objects.
- **Why problematic:** This contradicts the W3C RDF Schema 1.1 specification. RDFS domain/range are entailment rules: if `P rdfs:domain C` and `x P y`, then infer `x rdf:type C`. They do NOT reject data. Validation is SHACL's role.
- **Authoritative source:** [R11-03] W3C RDF Schema 1.1 Recommendation, Sections 3.1–3.2 (fetched 2026-08-25, HTTP 200).
- **Correction:** Rewrote all domain/range explanations in `book/chapter01.md` to describe inference behavior. Added ⚠️ callout distinguishing RDFS entailment from SHACL validation. Fixed experiment 1-5 docstring and print statements to label custom policy explicitly.
- **Impacted files:** `book/chapter01.md`, `chapter01/exp_1_5_relation_semantics.py`, `chapter01/exp_1_3_sister_city_kg.py`

### E2: KG definition presented as universal

- **Original claim:** `Knowledge Graph = Data Graph + Semantics + Context` was stated without qualification.
- **Why problematic:** This is a useful engineering mental model but not the accepted academic definition. Stanford CS520 defines KG minimally as a directed labeled graph where labels have semantically defined meanings.
- **Authoritative source:** [CS520-KG] Stanford CS520 lecture notes (fetched 2026-08-25, HTTP 200).
- **Correction:** Added "Academic/Minimal Model" section citing CS520 before introducing the book's engineering model. Explicitly labeled the book model as an engineering decomposition, not a universal definition.
- **Impacted files:** `book/chapter01.md`

### E3: Strict maturity ladder

- **Original claim:** `Plain Graph → Data Graph → Taxonomy → Ontology → Knowledge Graph` presented as exclusive stages.
- **Why problematic:** These concepts overlap; they are not mutually exclusive maturity levels. A taxonomy can be part of a KG; an ontology can exist without being called a KG.
- **Correction:** Replaced with cumulative capabilities enrichment model showing compositional layers (graph structure + semantic commitments + schema + identity + context + validation + inference).
- **Impacted files:** `book/chapter01.md`

### E4: Formal model notation inconsistency

- **Original claim:** `G = (V, E, L_V, L_E)` used `L_E` inconsistently as both edge label set and labeling function.
- **Why problematic:** Ambiguous notation confuses readers about whether edges carry labels directly or via a separate function.
- **Correction:** Changed to `G = (V, E, λ)` where `λ: E → L` is the edge labeling function. Renamed `(G, O, C)` tuple to "Book Engineering Model (KSE)" with explicit disclaimer that this notation is book-defined.
- **Impacted files:** `book/chapter01.md`

### E5: SHACL 1.2 URL error

- **Original claim:** Phase 1 research used URL `shacl-12-core` which returned 404, leading to conclusion that SHACL 1.2 did not exist.
- **Why problematic:** The correct URL is `shacl12-core` (no hyphen between shacl and 12). SHACL 1.2 Core exists as a Working Draft dated 2026-08-03.
- **Authoritative source:** [R12-SHACL12-CORE] W3C SHACL 1.2 Core Working Draft (fetched 2026-08-25, HTTP 200).
- **Correction:** Updated all references in `docs/RESEARCH_LOG.md`, `docs/PHASE1_REPORT.md`, and `docs/source_index.json` to use correct URL and mark status as WD.
- **Impacted files:** `docs/RESEARCH_LOG.md`, `docs/PHASE1_REPORT.md`, `docs/source_index.json`

### E6: License mismatch

- **Original claim:** `LICENSE` file contains GPLv3 text, but `pyproject.toml` declared MIT license.
- **Why problematic:** Legal ambiguity about project licensing.
- **Correction:** Updated `pyproject.toml` license field to `GPL-3.0-or-later` to match LICENSE file. README.md has no license reference (acceptable).
- **Impacted files:** `pyproject.toml`

### E7: Assertion vs Fact conflation

- **Original claim:** "A triple becomes a fact only after verification, provenance, and suitable context."
- **Why problematic:** This conflates RDF representation semantics (what it means to assert a triple) with epistemic governance policy (when our system promotes an assertion to accepted knowledge). RDF itself does not require provenance for a triple to be "asserted."
- **Correction:** Clarified distinction between representation semantics (triple assertion per RDF 1.1) and epistemic governance policy (our system's criteria for accepting knowledge). Added forward reference to Chapter 6's observation/assertion/claim/evidence/knowledge hierarchy.
- **Impacted files:** `book/chapter01.md`

---

## Source Audit Results

| Category | Count |
|----------|-------|
| Fetched and verified | 12 |
| Fetch failed | 0 |
| Not yet fetched | 0 |
| Stable Recommendations | 7 |
| Emerging drafts | 3 |
| Academic sources | 2 |

**Stable standards verified:**
- RDF 1.1 (REC 2014-02-25)
- RDF Schema 1.1 (REC 2014-02-25)
- SPARQL 1.1 Query Language (REC 2013-03-21)
- OWL 2 Web Ontology Language (REC 2012-12-11)
- SHACL 1.0 (REC 2017-07-20)
- PROV-O (REC 2013-04-30)
- Turtle 1.1 (REC 2014-02-25)

**Emerging drafts verified:**
- RDF 1.2 (CR 2026-04-07)
- SPARQL 1.2 (WD 2026-08-20)
- SHACL 1.2 Core (WD 2026-08-03)

All fetches recorded in `docs/source_index.json` with canonical URLs, HTTP status codes, final URLs after redirects, titles, publication dates, and document statuses. Research notes created under `.research/cache/` for key sources.

---

## Semantic Corrections

### RDFS Inference vs Validation

**Before:** Domain/range described as constraints that detect violations.  
**After:** Domain/range described as entailment rules per W3C RDF Schema 1.1 §3.1–3.2. Added explicit ⚠️ callout:

> ⚠️ **RDFS ≠ Validation**  
> RDFS domain/range enable *inference* (inferring new type assertions), not *validation*. If you need constraint checking that rejects non-conforming data, use SHACL (covered in Chapter 5).

### KG Definition vs Book Mental Model

**Before:** Single definition presented as universal.  
**After:** Two-layer presentation:
1. **Academic/Minimal Model:** Directed labeled graph where labels have semantically defined meanings (Stanford CS520). Formal: subset of N × L × N.
2. **Book Engineering Model (KSE):** Data Graph + Semantics + Context. Explicitly labeled as this book's engineering decomposition for building production knowledge systems, not a universal definition.

### Assertion vs Accepted Knowledge

**Before:** Conflated RDF assertion with epistemic acceptance.  
**After:** Clear separation:
- **Representation semantics:** Per RDF 1.1, asserting a triple means including it in the graph. No provenance required for assertion.
- **Epistemic governance policy:** Our system's criteria for promoting assertions to accepted knowledge (verification, provenance, context). This is a design choice, not RDF semantics. Forward-references Chapter 6 hierarchy.

---

## Changed Files

| File | Change Summary |
|------|----------------|
| `book/chapter01.md` | Fixed RDFS semantics, added academic KG definition, replaced ladder with enrichment model, fixed formal notation, clarified assertion vs fact |
| `chapter01/exp_1_5_relation_semantics.py` | Fixed docstring ("constraint checking" → "inference"), clarified RDFS vs custom policy in output |
| `chapter01/exp_1_3_sister_city_kg.py` | Fixed docstring ("constraints" → "inference") |
| `docs/RESEARCH_LOG.md` | Corrected SHACL 1.2 URL and status |
| `docs/PHASE1_REPORT.md` | Corrected SHACL 1.2 row from previous incorrect status to "🔄 Working Draft \| 2026-08-03" |
| `docs/source_index.json` | Created with fetch evidence for 12 P0 sources |
| `pyproject.toml` | Fixed license from MIT to GPL-3.0-or-later |
| `AGENTS.md` | Added Standards Correctness Policy section (P1-4) |
| `.research/cache/` | Created; contains fetched HTML for rdf-schema.html, shacl.html, shacl12-core.html, cs520-what-is-kg.html |

---

## Tests Added/Changed

No new tests were added. All 20 existing Chapter 1 tests continue to pass after semantic corrections. The tests verify implementation behavior consistent with RDFS entailment semantics (not validation). Key test coverage:

- `test_symmetric_inference_present` — verifies symmetric property inference (exp 1-3)
- `test_subclass_inference_present` — verifies rdfs:subClassOf transitive inference (exp 1-3)
- `test_inference_produces_new_triples` — verifies domain/range entailment produces new type assertions (exp 1-4)
- `test_inverse_inference` — verifies owl:inverseOf inference (exp 1-5)
- `test_transitive_inference` — verifies transitive property inference (exp 1-5)

Standards-correctness policy added to `AGENTS.md` requires future tests to reference source IDs from `docs/source_index.json` and record semantic contracts.

---

## Clean-run Evidence

```
$ PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 .venv/bin/python -m pytest chapter01/ -v --tb=short
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0
collected 20 items

chapter01/test_experiments.py::TestExp11::test_plain_graph_nodes_and_edges PASSED
chapter01/test_experiments.py::TestExp11::test_plain_graph_neighbors PASSED
chapter01/test_experiments.py::TestExp11::test_plain_graph_bfs_path PASSED
chapter01/test_experiments.py::TestExp11::test_plain_graph_no_path PASSED
chapter01/test_experiments.py::TestExp11::test_city_and_social_same_topology PASSED
chapter01/test_experiments.py::TestExp11::test_experiment_runs PASSED
chapter01/test_experiments.py::TestExp12::test_data_graph_query PASSED
chapter01/test_experiments.py::TestExp12::test_taxonomy_ancestors PASSED
chapter01/test_experiments.py::TestExp12::test_taxonomy_all_instances_includes_subclasses PASSED
chapter01/test_experiments.py::TestExp12::test_taxonomy_transitive_instances PASSED
chapter01/test_experiments.py::TestExp12::test_experiment_runs PASSED
chapter01/test_experiments.py::TestExp13::test_experiment_runs PASSED
chapter01/test_experiments.py::TestExp13::test_symmetric_inference_present PASSED
chapter01/test_experiments.py::TestExp13::test_subclass_inference_present PASSED
chapter01/test_experiments.py::TestExp14::test_experiment_runs PASSED
chapter01/test_experiments.py::TestExp14::test_inference_produces_new_triples PASSED
chapter01/test_experiments.py::TestExp14::test_region_query_works_after_semantics PASSED
chapter01/test_experiments.py::TestExp15::test_experiment_runs PASSED
chapter01/test_experiments.py::TestExp15::test_inverse_inference PASSED
chapter01/test_experiments.py::TestExp15::test_transitive_inference PASSED

============================== 20 passed in 0.16s ==============================
```

Note: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` is required due to ROS `launch_testing` plugin conflict in the development environment. This workaround does not affect test correctness.

---

## Remaining Uncertainties

1. **RDF 1.2 and SPARQL 1.2 are Candidate Recommendation / Working Draft.** Content may change before final Recommendation. Book should reference these as emerging standards, not stable baselines.
2. **SHACL 1.2 Core is Working Draft (2026-08-03).** Chapter 5 should teach SHACL 1.0 as stable baseline and mention 1.2 as upcoming. Do not teach 1.2 features as established.
3. **ROS plugin conflict workaround.** The `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` requirement should be documented in contributor setup instructions. Consider investigating root cause or isolating test environment.
4. **Content hash not recorded.** Source index entries omit content hashes for legal/practical reasons. If reproducibility auditing becomes critical, add SHA-256 hashes of fetched HTML.
5. **Chapter 6 epistemic hierarchy not yet implemented.** Forward reference added but full observation/assertion/claim/evidence/knowledge model deferred to Chapter 6.

---

## Go / No-Go for Chapter 2

### ✅ GO

All P0 issues resolved:
- [x] P0-1: RDFS domain/range semantics corrected (inference, not validation)
- [x] P0-2: Canonical KG definition separated from book engineering model
- [x] P0-3: Strict ladder replaced with enrichment model
- [x] P0-4: Formal model notation fixed
- [x] P0-5: W3C sources re-fetched using exact canonical URLs
- [x] P0-6: Machine-readable `source_index.json` created with fetch evidence
- [x] P0-7: Research document contradictions resolved
- [x] P0-8: Assertion vs accepted knowledge clarified

All P1 issues resolved:
- [x] P1-1: Experiment status synchronized
- [x] P1-2: License consistency fixed (GPL-3.0-or-later)
- [x] P1-3: Dependency hygiene audited (no changes needed)
- [x] P1-4: Standards-correctness policy added to contributor docs

**Evidence (Phase 0.5):** 20/20 tests passing at time of audit. *Superseded by Phase 0.6: test suite expanded to 25 tests. See docs/PHASE0_7_FINAL_INTEGRITY_REPORT.md for current status.* All semantic corrections backed by fetched primary sources. No cosmetic changes made before substantive fixes. Repository metadata internally consistent.

**Chapter 2 may proceed.**

