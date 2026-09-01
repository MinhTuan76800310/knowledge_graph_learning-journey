# English Edition — Chapters 1–2 Audit

> Issue #31 · Date: 2026-09-01 · Auditor: Claude (inline review + targeted web verification)
> Files: `book-en/chapter01.md`, `book-en/chapter02.md`
> Method note: an initial fan-out workflow (2 monolithic reviewer agents) stalled on output
> generation; the review was completed inline with per-claim web verification instead.

## Verdict

| Chapter | Accuracy | Clarity | Depth |
|---------|----------|---------|-------|
| Ch1 — From Graph to Knowledge | PASS (0 errors) | PASS (2 minor nits) | PASS (meets §16 rubric) |
| Ch2 — Data Models and Query Languages | 2 MAJOR errors found (fixed in this PR) | PASS (3 minor nits) | PASS (meets §16 rubric) |

Both chapters are faithful, readable English translations that meet the project's depth
rubric. The two MAJOR accuracy errors are **pre-existing in the Vietnamese original** (the
English reproduced them faithfully) — see Follow-ups.

## Findings

### Accuracy

**A1 — MAJOR — Ch2 §2.1.7 (RDF 1.2 box): citation does not support the claim.**
> "the older RDF 1.1 reification vocabulary is retained as legacy vocabulary for
> compatibility [@w3c-rdf12-concepts]"

Verified against the cited source: the RDF 1.2 Concepts spec (CRS 2026-04-07) does **not
mention `rdf:Statement` / `rdf:subject` / `rdf:predicate` / `rdf:object` at all** — it only
introduces `rdf:reifies` and triple terms. The "retained as legacy" statement is therefore
unsupported by the source it cites.
**Fix applied:** re-cite to RDF 1.1 Concepts (still a Recommendation) for the retained
vocabulary, and state plainly that RDF 1.2 does not deprecate it.

**A2 — MAJOR — Ch2 §2.7: dataset claim contradicts the canonical data.**
> "(in the current graph, only `newtonCooling_1 requires rateOfChange_1`)"

`datasets/mechanism_kg/rate_of_change.ttl` lines 214–215 give **two** `ex:requires` edges:
`newtonCooling_1 → rateOfChange_1` **and** `newtonCooling_1 → heatTransferRate_2`.
**Fix applied:** "…`newtonCooling_1` requires both `rateOfChange_1` and `heatTransferRate_2`".

**A3 — minor — Ch2 §2.1.6: "OPTIONAL corresponds directly to a LEFT JOIN in SQL".**
The SPARQL 1.1 algebra defines OPTIONAL as a left-join-style operation, so the analogy is
sound for teaching; "directly" slightly overstates it (non-well-designed patterns behave
differently from SQL). Left as-is; noted for a possible future softening to "closely".

**A4 — minor — Ch2 §2.1.1 table: redundant columns in English.**
The Vietnamese table had `Chủ thể | subject` (VI name | EN term). In English the Position
and Name columns now repeat the same words. Cosmetic; left as-is to keep table parity with
the VI original.

**A5 — info — Ch2 §2.1.1 "A literal is only allowed in the object position".**
Correct for the RDF 1.1 baseline the chapter teaches; RDF 1.2 triple terms in subject
position are already flagged in §2.1.7. No change.

### Clarity

- **C1 — minor — Ch2 §2.1.6 self-check hint:** "(The step-by-step expansion tables in
  section 2.1.6 illustrate this very property.)" — the hint points at tables in the *same*
  section; reads as a forward pointer. Harmless; inherited from VI.
- **C2 — minor — Ch1 §1.3 "Semantics" paragraph** is one dense block (four components +
  worked inference). Splitting would help first-time readers; deferred to keep EN/VI parity.
- **C3 — minor — Ch2 §2.3.3:** "a near character-for-character translation of the
  three-pattern BGP" — structural correspondence is exact, syntax is not; acceptable rhetoric.

No translation-artifact phrasing (Vietnamese-influenced word order, false friends) was found
in either chapter.

### Depth (per BOOK_PEDAGOGY §7/§16)

- **Ch1:** the five-step capability model reaches depth 5 — intuition → mechanism →
  worked city example → capstone repetition (RATE_OF_CHANGE steps 2′–5′) → KSE formalization
  → explicit "what it still cannot do". Self-checks present (§12) ✓.
- **Ch2:** blank nodes (intuition + existential semantics + locality + isomorphism worked
  example + capstone re-extraction case) ≥ depth 4 ✓; SPARQL BGP/solution mappings reach
  depth 5 (4-step join tables, Cartesian-product counterexample, FILTER/OPTIONAL on
  mechanism data, rdf:type-subclassing trap) ✓; LPG identity ≥ depth 3 (SUPPORTING) ✓.
- No "explanation theater" found: every Mechanism-KG integration is a worked instantiation.

## Verified claims (web/local, 2026-09-01)

| # | Claim | Verdict | Source |
|---|-------|---------|--------|
| 1 | Triple positions: subject IRI/blank, predicate IRI only, object IRI/literal/blank | CONFIRMED | https://www.w3.org/TR/rdf11-concepts/ §3.1 |
| 2 | Blank node identifiers are local, not persistent/portable | CONFIRMED | rdf11-concepts §3.4 |
| 3 | Graph isomorphism = bijection preserving triples (predicates fixed) | CONFIRMED | rdf11-concepts §3.6 |
| 4 | Turtle `a` = rdf:type; `;` repeats subject; `,` repeats subject+predicate; prefixes are notation | CONFIRMED | https://www.w3.org/TR/turtle/ |
| 5 | BGP = set of triple patterns; solutions = partial functions var→term; DISTINCT de-dupes | CONFIRMED | https://www.w3.org/TR/sparql11-query/ |
| 6 | OPTIONAL adds bindings when matched, preserves solution otherwise (left-join-like) | CONFIRMED | sparql11-query |
| 7 | Neo4j elementId() → STRING, transaction-scoped uniqueness; id() deprecated INTEGER; internal IDs reused → use application-generated IDs | CONFIRMED | https://neo4j.com/docs/cypher-manual/current/functions/scalar/ |
| 8 | GQL = ISO/IEC 39075:2024; Cypher covers most mandatory features, not identical | CONFIRMED | https://neo4j.com/docs/cypher-manual/current/appendix/gql-conformance/ (iso.org 403s bots; GQL-01 registered) |
| 9 | RDF 1.2 Concepts = W3C CRS 2026-04-07; triple term denotes a proposition; rdf:reifies reifier | CONFIRMED | https://www.w3.org/TR/rdf12-concepts/ |
| 10 | RDF 1.2 retains RDF 1.1 reification vocabulary as legacy | **REFUTED** (see A1) | rdf12-concepts — no mention of rdf:Statement |
| 11 | SPARQL 1.2 Query = W3C Working Draft (now dated 2026-08-27) | CONFIRMED (date updated) | https://www.w3.org/TR/sparql12-query/ |
| 12 | CS520 minimal def: directed labeled graph, subset of N × L × N | CONFIRMED | https://web.stanford.edu/class/cs520/2020/notes/What_is_a_Knowledge_Graph.html |
| 13 | Dataset: newtonCooling_1 requires rateOfChange_1 AND heatTransferRate_2 | CONFIRMED (text was wrong, see A2) | datasets/mechanism_kg/rate_of_change.ttl L214–215 |
| 14 | Dataset: position_1 hasValue 12.5; thermalEnergy_1 hasValue 300.0; heatTransferRate_2 → heatRate_2 | CONFIRMED | rate_of_change.ttl L147, L189, L194 |

## Sources consulted this review (log)

Already registered (re-verified, no new entries): R11-02, R11-05, R12-01, SP11-02, SP12-01,
N4J-06, GQL-02, S03.

New / updated in `docs/source_index.json`:
- **N4J-09** — Neo4j Cypher manual, scalar functions (elementId/id) — the decisive page for
  the §2.2.2 identity discussion.
- **SP12-01** — publication_date corrected 2026-08-20 → 2026-08-27 (re-fetched).

## Re-audit addendum (2026-09-01)

A second targeted review was requested to check whether any logic errors remained in
Chapters 1–2 of both editions. It confirmed A1/A2 in the Vietnamese original and found
one additional citation issue in the English fix from PR #32.

- **A1′ — MAJOR — EN §2.1.7:** PR #32 re-cited the RDF 1.1 reification vocabulary to
  `@w3c-rdf11-concepts`, but the vocabulary (`rdf:Statement`, `rdf:subject`,
  `rdf:predicate`, `rdf:object`) is actually defined in **RDF 1.1 Schema** (§5.3),
  not in RDF 1.1 Concepts. Fixed by citing `@w3c-rdf-schema` (Issue #35 / PR #37).
- **A1 + A2 in VI:** the Vietnamese original still carries both errors. They are
  corrected in PR #36 (Issue #33).
- **No new logic errors** were found in Chapter 1 (either language) or in the core
  SPARQL/LPG/model explanations of Chapter 2.

## Follow-ups

- **VI original carries A1 + A2** (`book/chapter02.md` §2.1.7 and §2.7) — the released
  v0.1.0 PDF contains both errors. Opened as a follow-up Issue for the next Vietnamese
  patch; EN/VI parity will be restored there.
- A3/A4/C1–C3: cosmetic, intentionally not changed to avoid EN/VI divergence.