# Answer-Key Findings Log

While drafting the model answers for the end-of-chapter reflection questions
(Issue #47), the drafting/verification pass flagged places where the **manuscript
itself** looks wrong or unverifiable. Per the project rule, none of these were
silently patched in the chapter text — they are logged here for a later, separate
correction pass.

The answer keys themselves are written to be correct regardless: where a chapter
example or hint is suspect, the answer states the correct position and cites the
governing standard, rather than repeating the suspect claim as true.

Severity: **high** = a load-bearing technical claim is wrong · **medium** = an
example/figure is internally inconsistent or misleading · **low** = cosmetic
(illustrative number, unverifiable real-world detail that does not carry the argument).

---

## Chapter 1 — From Graph to Knowledge

| § | Severity | Finding |
|---|----------|---------|
| §1.7 | low | "Wikidata giải quyết bằng qualifiers/references/ranks **thay vì OWL axioms**" is a deliberate simplification: the three mechanisms are correct (verified against Wikidata Help:Statements), but Wikidata does carry property constraints and some ontology-like semantics. The precise point is that it does not rely on OWL entailment for inference. Not wrong, but worth a qualifier. |
| §1.6 | low | `validFrom: 1976` for `(Hanoi) capitalOf (Vietnam)` matches the 1976 reunification date, so it is historically sensible; noted only so reviewers know it is illustrative data, not a sourced standard claim. |

## Chapter 2 — Data Models and Query Languages

| § | Severity | Finding |
|---|----------|---------|
| §2.1.5, §2.1.6 (and `datasets/mechanism_kg/rate_of_change.ttl`) | medium | The RDF namespace is written **malformed**: the chapter uses `http://www.w3.org/1999-02-22-rdf-syntax-ns#` (hyphens) instead of the W3C-correct `http://www.w3.org/1999/02/22-rdf-syntax-ns#` (slashes) — confirmed at `book/chapter02.md:222, 315, 402`. In the Turtle blocks this is harmless (only the `a` keyword is used), but in the SPARQL query at §2.1.6 (`PREFIX rdf: <…1999-02-22…>` + `?city rdf:type ex:City`) the `rdf:type` resolves to the wrong IRI and the query returns empty against the 11-triple graph built with RDFLib's correct `RDF.type` (§2.1.4) — the very example the chapter uses to illustrate a BGP. The `a rdf:Property` declarations in the dataset also point at the wrong `rdf:Property` IRI. Fix: replace `1999-02-22-rdf-syntax-ns#` with `1999/02/22-rdf-syntax-ns#` everywhere. |
| §2.1.7 | — | **Checked, NOT an error**: RDF 1.2 Concepts is indeed a W3C Candidate Recommendation Snapshot (published 2026-04-07) introducing `rdf:reifies`/triple terms (per https://www.w3.org/TR/rdf12-concepts/); the ISO/IEC 39075:2024 (GQL) reference at §2.3.4 is also correct. |

## Chapter 3 — Schema, Identity, and Context

| § | Severity | Finding |
|---|----------|---------|
| §3.2.3 | low | The illustrative "khoảng chênh 4,6%" between the two population figures (8 418 883 vs 8 053 663) does not match the arithmetic: the difference is 365 220, i.e. ≈4,53% of the smaller and ≈4,34% of the larger — no reading yields 4,6%. Illustrative only (does not carry the UNA argument); correct to "≈4,5%". |
| §3.5 (lỗi số 2) | low | The counter-example "the string *Hà Nội* is also a phường in Hà Giang province" is factually wrong: no phường named "Hà Nội" exists in Hà Giang (checked against Vietnamese Wikipedia). The argument does not depend on it; replace with a verifiable label collision, e.g. *Xa lộ Hà Nội* (a road, not a city). Answer-key Câu 1 was rewritten to attribute the example to the chapter and add the real one. |
| §3.2.1 | low | The example "a street named *Hà Nội* in Quận 1, TP.HCM" could not be verified (nearest namesake is *Xa lộ Hà Nội*, not in Quận 1). No answer key cites it; correct or replace in the manuscript. |

## Chapter 4 — Ontologies and Formal Meaning

| § | Severity | Finding |
|---|----------|---------|
| §4.12 | **high** | The chapter states that the property chain `requires ∘ requires ⊑ requires` is **not** OWL 2 EL ("EL không hỗ trợ property chain"), and the self-check (Câu 8) instructs the reader to drop that chain to reach EL. This is **wrong per the standard**: the OWL 2 EL grammar *does* allow `SubObjectPropertyOf` with `ObjectPropertyChain`; EL only excludes Symmetric / Asymmetric / Irreflexive property characteristics and `DisjointObjectProperties`. So the minimal set to drop for EL is {`Irreflexive(requires)`, `Asymmetric(hasInput)`, `Asymmetric(requires)`} — **three**, not four — and the chain need not be dropped. The "push to OWL 2 RL/Full because of the chain" conclusion is therefore incorrect. Source: OWL 2 Profiles (W3C). Answer-key Câu 8 states the corrected position. |

## Chapter 6 — Claims, Evidence, Provenance, Time, Contradiction

| § | Severity | Finding |
|---|----------|---------|
| §6.17 / §6.12 | medium | The "Ba claim cơ chế" table (§6.17) and lifecycle (§6.12) give `claim_roc_A` a valid time [1687, 1905) and mark it **Superseded** by `claim_roc_relativist`. But `claim_roc_A` carries `prop_velocity_rate_of_change` ("velocity is the rate of change of position") — a definition relativity does **not** refute. The claim that should be superseded is `claim_roc_classical` / `prop_roc_velocity_unbounded` (§6.7). Two different propositions (rate-of-change vs unbounded-velocity) are conflated. |
| §6.6 | low | Scope-disagreement example "France population 67 M nationwide vs 55 M metropolitan" uses unverifiable illustrative figures; label them as assumed numbers. |
| §6.0 / §6.7 | low | The Hanoi population pair 8 093 100 (attributed to GSO 2019) and 8 053 663 (attributed to Wikidata) — per-figure source attribution is not verifiable in-chapter and may not match reality; re-check if used as real data. |

## Chapter 9 — Retrieval, Question Answering, and GraphRAG

| § | Severity | Finding |
|---|----------|---------|
| §9.30 | medium | The second worked example is internally inconsistent: "P@5=1.0 nhưng R@5=0.25 (chỉ 2/8 liên quan) — giấu 6/8 bằng chứng." By the section's own definitions (P@K = relevant-in-top-K / K; R@K = relevant-in-top-K / total-relevant), if only 2/8 relevant are retrieved then R@5=2/8=0.25 is right but P@5=2/5=0.4, not 1.0; conversely P@5=1.0 requires 5 relevant in top-5 ⇒ R@5=5/8=0.625. The two numbers cannot both hold. (The first example, "8 relevant, top-5 contains 4 ⇒ P@5=0.8, R@5=0.5", is correct.) |
| §9.60 | low | The example "dòng điện tỉ lệ nghịch điện trở" is labelled *predicted*. In physics this is Ohm's law (normally asserted/derived); it is only *predicted* within the chapter's "if this sentence came from a learned model (Ch8)" framing. Not wrong under the book's provenance-labeling frame, but could mislead if read as a physics claim rather than a label-by-source illustration. |

## Chapter 10 — Building a Living Knowledge System

| § | Severity | Finding |
|---|----------|---------|
| §10.6 | low | The sentence "Chương 6 giới thiệu **ba** đồng hồ cho từng claim" is immediately followed by a list of **four** (valid, publication, system, assessment), and the section heading names only three (Valid/System/Assessment). Fix the count to "bốn" or drop publication time from the list to match the heading. |
| §10.33 / §10.35 | — | **Checked, NOT an error** (recorded so reviewers can stop worrying): the "giảm 11–14%" figure and the "not mainly overfitting but failure to generalise to slightly harder images" conclusion match Recht et al. 2019 (PMLR v97) exactly; the Shumailov et al. 2024 citation ("irreversible defect, original distribution tail disappears") matches Nature 2024. |

---

## Chapter 5 — Deduction, Rules, and Validation

No suspected manuscript errors. All external facts relied on by the answers
(RDF 1.1 Semantics §9.2.1 patterns, the OWL 2 RL `cax-dw` rule, SPARQL entailment-regime
IRIs, SHACL section numbers) were verified against the W3C specs and check out.

---

**Summary of open findings:** 1 high (§4.12 EL property-chain), 3 medium (§2.1.5/6 RDF
namespace typo, §6.17/12 claim-supersession conflation, §9.30 P@K/R@K arithmetic), and
several low (illustrative numbers and unverifiable real-world examples). None were patched
in the manuscript; each is a candidate for a separate correction pass.
