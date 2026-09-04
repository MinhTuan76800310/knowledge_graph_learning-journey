# Chapter 7 — Knowledge Acquisition and Integration

> **Chapter orientation**
>
> **Central question:** Chapter 6 assumed statements already *sat* in the ledger with
> full provenance. But where does new knowledge come from? How does a system take content
> from many sources — textbooks, databases, APIs — turn it into structured statements,
> recognize "two sources are talking about the same thing", align schemas, remove
> duplicates, and write it into the ledger without corrupting the already-governed graph?
>
> **Why it matters:** The first six chapters built the graph (Ch1–2), identity (Ch3),
> semantics (Ch4), inference/validation (Ch5), and the epistemic layer (Ch6). But all of
> them assumed the data was already *clean, already present, already in the right place*.
> In reality, a knowledge graph is fed by **acquisition and integration pipelines**: many
> heterogeneous sources, duplicates, differing schemas, conflicting values. Without a
> disciplined process, the clean governed graph of Chapter 6 becomes contaminated by
> unverified, undeduplicated, untraceable data.
>
> **You will understand:**
>
> - The boundary between **Acquisition** (bringing information into the system) and
>   **Integration** (merging, reconciling, confirming before writing to the ledger)
> - The central pipeline: source registration → observation → extraction → normalization →
>   structuring → identity resolution → schema alignment → deduplication → SHACL gate →
>   ledger insertion
> - Entity resolution: candidate generation differs from scoring; the Fellegi–Sunter model
>   with three decision zones
> - Schema alignment and mapping: the default Direct Mapping versus custom R2RML mappings
> - Idempotent ingestion and content hashing — why re-running does not create duplicates
> - SHACL conformance differs from Accepted
> - Conflict detection, merge outcomes, ledger-first — connecting to Chapter 6 governance
> - Lineage (tracing "where did it come from?") differs from Evidence (the reason "why
>   believe it?")
> - Seven invariants I1–I7 that protect the pipeline
>
> **Prerequisites:** Chapter 3 (ownership identity, owl:sameAs, n-ary), Chapter 5
> (conformance ≠ truth, SHACL), Chapter 6 (epistemic model, Claim, governance, Claim
> Ledger, provenance).
>
> **Concept map:**
>
> Heterogeneous sources → **Acquisition** (observation → extraction → normalization →
> structuring) → **Integration** (identity resolution → schema alignment → deduplication →
> conflict control) → **Ledger insertion** (Claim Ledger) → Canonical Knowledge View

## 7.0 Introduction: Three sources, one concept

Chapter 6 led with two population figures. Chapter 7 opens with a harder situation: three
different sources, stating *almost* the same concept, but it is not self-evident that they
are talking about the same thing.

**Source A** — a calculus textbook, Chapter 3, defining the derivative:

> "The derivative of a function f at a point x — written f′(x) — is the limit of the ratio
> [f(x+h) − f(x)]/h as h approaches 0. The derivative measures the instantaneous rate of
> change of f."

**Source B** — a mechanics textbook, Chapter 2, defining velocity:

> "Instantaneous velocity is the derivative of distance with respect to time: v = ds/dt.
> In other words, velocity is the rate of change of position with respect to time."

**Source C** — an electronics textbook, Chapter 5, current through a capacitor:

> "The current through a capacitor equals the rate of change of voltage with respect to
> time: i = C·(dV/dt). When the voltage is constant, the current is zero: a capacitor
> blocks direct current."

The three statements look alike on the surface — all talk about "rate of change with
respect to time". But the system must not rush to conclude. Ask three questions:

1. **Identity:** Source A talks about `f′(x)` (the derivative of a function), source B
   about `v = ds/dt` (one-dimensional velocity), source C about `i = C·dV/dt` (current
   through a capacitor). Are they talking about *the same entity*?
2. **Schema:** If all three describe "a quantity equal to the rate of change of another
   quantity", is the "rate of change" property in the three sources *the same semantics*?
3. **Duplication and conflict:** If two sources both assert one thing, how many statements
   do we record? If the values differ, keep both or handle it how?

The naive answer — "they look alike, so merge them" — is exactly where a knowledge graph
breaks. If the system hastily links `owl:sameAs` between "the derivative of a function"
(A) and "current through a capacitor" (C) just because of the shared phrase "rate of
change", the damage propagates across the whole graph, as Chapter 3 warned (§3.2.4).

Chapter 7 builds the **acquisition and integration pipeline**: a disciplined process for
bringing these three sources into the system, turning them into structured statements,
deciding *whether or not* they are the same concept — and connecting the result to the
governance of Chapter 6.

> 🖊 **Self-check:** Before reading on, answer for yourself: in your view, should the
> "rate of change" in sources A, B, C point to the same node or not? Write down your
> reasoning. At the end of the chapter (§7.31, §7.36) you will compare it with how the
> system decides.

## 7.1 The central pipeline: from source to ledger

### Intuition

All knowledge in the system comes from some source. The central pipeline is an *ordered*
description of how source content is gradually transformed into a governed statement.
Like an oil refinery: raw material passes through many stages, each stage has controls,
and only product meeting spec enters the finished-goods store.

### Mechanism

The pipeline has two halves, corresponding to two different questions:

![The central pipeline: Acquisition (source registration → observation → extraction → normalization → structuring) then Integration (identity resolution → schema alignment → deduplication → SHACL gate → conflict → ledger insertion).](figures/generated/ch07-central-pipeline.pdf)

```
                 ACQUISITION                                    INTEGRATION
  ┌───────────┐   ┌───────────┐   ┌───────────┐   ┌───────────┐   ┌───────────┐
  │ Register  │ → │ Observe   │ → │ Extract   │ → │ Normalize │ → │ Structure │
  │ source    │   │ & fragment│   │           │   │           │   │           │
  └───────────┘   └───────────┘   └───────────┘   └───────────┘   └───────────┘
   Source          Source          Extraction      Canonical       Graph-shaped
   Artifact        Fragment        → candidate     form            candidate
                                   record                                        │
                       ┌─────────────────────────────────────────┐              │
                       ▼               INTEGRATION (cont.)        │              ▼
               ┌───────────┐   ┌───────────┐   ┌───────────┐   ┌──────────┐
               │ Resolve   │ → │ Align     │ → │ Dedup &   │ → │ SHACL    │
               │ identity  │   │ schema &  │   │ idempotent│   │ gate     │
               │           │   │ map       │   │ ingest    │   │ (valid)  │
               └───────────┘   └───────────┘   └───────────┘   └──────────┘
                                                        │              │
                                               ┌─────────┴──────────┐   │
                                               ▼                    ▼   ▼
                                     ┌──────────────┐   ┌────────────────────────┐
                                     │ Conflict &   │ → │ Claim Ledger insert &  │
                                     │ integration  │   │ projection             │
                                     │ decision     │   │ (Canonical View)       │
                                     └──────────────┘   └────────────────────────┘
```

Each stage has an accompanying output artifact:

| # | Stage | Input | Output | Purpose |
|---|-------|-------|--------|---------|
| 1 | Source registration | A real-world source | `Source Artifact` (a record with an IRI) | §7.3 |
| 2 | Observation | Source Artifact | `Source Fragment` + `Observation` | §7.4 |
| 3 | Extraction | Observation | candidate record + `Extraction Activity` | §7.5 |
| 4 | Normalization | raw record | canonical-form record | §7.7 |
| 5 | Structuring | canonical record | candidate RDF triples | §7.8 |
| 6 | Identity resolution | cluster of triples | "same entity?" decision | §7.9–7.10 |
| 7 | Schema alignment & mapping | source schema | correspondence + mapping | §7.11–7.12 |
| 8 | Deduplication & normalized ingest | the records | one deduplicated clean record | §7.13–7.14 |
| 9 | SHACL gate | candidate triples | conformance report | §7.15 |
| 10 | Conflict & decision | valid triples | decision: accept/reject/review | §7.16–7.17 |
| 11 | Ledger insertion | decision + triples | Claim Ledger entry | §7.18 |

This pipeline is not a W3C standard — it is a **book-defined architecture**
(BOOK-DEFINED), assembling real standards (R2RML, CSVW, Direct Mapping, Fellegi–Sunter,
SHACL, PROV-O) into a unified teaching framework. Each step will be tied to its
corresponding standard/concept in the sections that follow.

### Application

For the three sources A, B, C in §7.0: each source is registered as a Source Artifact;
each definition yields one Observation; the parallel knowledge lines pass through the
common stages and meet at *the integration steps*, where the system decides the
relationship between them.

> 🖊 **Self-check:** Fill in one stage of your choosing in the table above: what are its
> input and output, and if that stage were skipped, what would the consequence be?

## 7.2 Acquisition differs from Integration

### Intuition

Two people do two different jobs: one **brings goods into the warehouse**, the other
**sorts, inspects, and reconciles the goods** before closing the books. Merging the two
into one creates chaos: uninspected goods get put out for sale.

### Mechanism

**Acquisition** answers the question "how do we bring information into the system?" — read
the source, extract, normalize, structure into **candidate knowledge** with provenance.
Acquisition does *not* decide who is right, does not deduplicate, does not align schemas —
it only makes source content *structured and traceable*.

**Integration** answers the question "how do we merge many streams into one consistent
picture?" — recognize whether two pieces of knowledge talk about the same thing (identity
resolution), align differing schemas (schema alignment), remove duplicates, control
conflicts, and decide what to write into the ledger [@lenzerini-2002]
[@hogan-creation-enrichment].

Why must they be separated? Because the two questions have **different success criteria**:

- Acquisition is measured by **coverage and extraction accuracy**: did we capture all the
  content worth capturing? Does the record match the source?
- Integration is measured by **consistency and reliability of the ledger**: after merging,
  are there still duplicates? Are the identity/schema decisions evidenced and recorded?

A subtle error: treating "acquisition done = knowledge is in the system". Wrong.
Acquisition only produces **candidates**. A record extracted from source C — "current =
C·dV/dt" — is a candidate statement, not yet accepted, its relationship to sources A/B not
yet known.

### Application

The vertical axis of the §7.1 pipeline: stages 1–5 belong to Acquisition; 6–11 belong to
Integration. Source C passes through acquisition exactly like sources A/B — but at
integration, its fate is decided by evidence, not by how fluent the source text is.

> ⚠️ **Common misconception:** "The system extracted a statement from a source → the
> system *knows* it." Wrong. Extraction produces *candidate knowledge*. Becoming "known"
> requires the whole integration + governance path (Chapter 6). Extraction and accepted
> knowledge are separated by a long pipeline.

## 7.3 Source registration: Source Artifact

### Intuition

Before borrowing a book, a library records it in the system: what this book is, whose it
is, which edition. Data sources are the same. The system does not work directly with "the
actual textbook on the shelf" — it works with the **registration record** of that book.

### Mechanism

A **Source Artifact** is the system's registration record of a source — a PROV entity with
its own IRI, carrying metadata: source kind (document / database / API),
author/publisher, registration time, version, and a trust profile [@prov-o].

Example registering the chapter's three sources:

```turtle
src:sourceA  a                    ex:SourceArtifact ;
             ex:sourceKind         ex:Document ;
             ex:title              "Calculus Textbook, 3rd edition" ;
             ex:publisher          ex:CalcPress ;
             ex:registeredAt      "2026-08-30T09:00:00Z"^^xsd:dateTime ;
             ex:sourceVersion      "3.1" ;
             ex:trustProfile       ex:Trust_High .

src:sourceB  a                    ex:SourceArtifact ;
             ex:sourceKind         ex:Document ;
             ex:title              "Mechanics Textbook, 2nd edition" ;
             ex:publisher          ex:MechPress ;
             ex:registeredAt      "2026-08-30T09:05:00Z"^^xsd:dateTime ;
             ex:sourceVersion      "2.4" ;
             ex:trustProfile       ex:Trust_High .

src:sourceC  a                    ex:SourceArtifact ;
             ex:sourceKind         ex:Document ;
             ex:title              "Electronics Textbook, 1st edition" ;
             ex:publisher          ex:ElecPress ;
             ex:registeredAt      "2026-08-30T09:10:00Z"^^xsd:dateTime ;
             ex:sourceVersion      "1.0" ;
             ex:trustProfile       ex:Trust_Medium .
```

Three important points:

1. **Source Artifact ≠ the real source.** `src:sourceA` is the system's *record*, not the
   book. If the system mis-records the source metadata, the error lives in the record —
   and every statement pointing to this record inherits that error.

2. **Registration ≠ trustworthy.** Having an IRI and full metadata says nothing about
   content quality. `Trust_High` is a *trust profile defined by the system*, not an
   absolute truth.

3. **The source version is recorded.** `sourceVersion "3.1"` — because the same book, in
   different printings, may differ in content. Provenance must point to the right edition.

### Application

When source C is later found to be an echo source (§7.23), its trust profile is lowered,
but the registration record **is not deleted** — its status is updated, just as a claim is
Superseded rather than deleted (Chapter 6).

> 🖊 **Self-check:** Why does the system need to register a source as a record with an
> IRI, rather than just storing the name string "Calculus Textbook"? Hint: think about two
> different books sharing a title, or two printings of the same book.

## 7.4 Observation and Source Fragment

### Intuition

When citing, we do not cite "the whole book" — we cite a sentence, a paragraph, a
definition. In a knowledge graph it is the same: provenance to *the whole source* is too
coarse. We need a level of detail fine enough to know exactly which part of the source a
statement rests on.

### Mechanism

A **Source Fragment** is an addressable sub-part of a Source Artifact: a page §, a
paragraph, a table, or an API response. It has its own IRI and points to its parent source
[@prov-dm].

An **Observation** is the raw data collected from a fragment — the definition sentence, a
number in a table — *before* it is interpreted. The Observation is the anchor of
provenance: it records "what was seen, where, when", kept separate from the later
interpretation layer.

```turtle
src:fragA_3_2  a                  ex:SourceFragment ;
               ex:partOf           src:sourceA ;
               ex:chapter          "3" ;
               ex:section          "3.2" ;
               ex:retrievedAt      "2026-08-30T10:00:00Z"^^xsd:dateTime .

ex:obsA_1      a                  ex:Observation ;
               ex:extractedFrom    src:fragA_3_2 ;
               ex:rawText          "The derivative of f at x is the limit of (f(x+h)-f(x))/h as h approaches 0." ;
               ex:observedAt       "2026-08-30T10:00:30Z"^^xsd:dateTime .
```

Two things to hold firm:

- **Observation ≠ interpretation.** `ex:obsA_1` holds the *original text string*. The
  statement "the derivative measures rate of change" is an *interpretation* — it appears at
  the extraction step (§7.5), with its own confidence (§7.6).
- **The finer the provenance, the better.** A statement from source A pointing to
  `src:fragA_3_2` is more precise than one pointing to `src:sourceA` in general. If a
  statement sits in §3.2 but the provenance only says "from the calculus textbook", that
  is imprecise provenance.

> ⚠️ **Common misconception:** "Recording provenance means recording the source name."
> Wrong. Provenance to `src:sourceA` without `src:fragA_3_2` leaves you unable to know
> which part the statement rests on — uncheckable, unlocatable when reconciliation is
> needed. Fragment-granular provenance is the minimum standard.

## 7.5 Extraction and Extraction Activity

### Intuition

Reading a sentence and writing down "who – relation – what" is a step of *interpretation*,
not copying. Extraction does exactly this: turn an Observation (raw text) into a
structured record. And because it is interpretation, it *can be wrong* — so the system must
record who (which tool) did it, and when.

### Mechanism

**Extraction** is the activity that turns each Observation into a candidate record:
recognizing entities, relations, attributes, and emitting an intermediate record according
to an **extraction schema** (§7.27).

For source A (the derivative definition):

```turtle
ex:recA_1  a              ex:ExtractedRecord ;
           ex:fromObservation ex:obsA_1 ;
           ex:subject     "derivative of f at x" ;
           ex:relation    "measures_rate_of_change_of" ;
           ex:object      "f" ;
           ex:extractionPattern  ex:Pattern_FormalDefinition .
```

An **Extraction Activity** is a PROV Activity recording the *execution* of the extraction:
the time, the agent (the extraction tool version), and the Observations used [@prov-o].
Each candidate record is `wasGeneratedBy` an Extraction Activity:

```turtle
ex:extractActA_1  a       prov:Activity ;
                    prov:startedAtTime  "2026-08-30T10:01:00Z"^^xsd:dateTime ;
                    prov:endedAtTime    "2026-08-30T10:01:02Z"^^xsd:dateTime ;
                    prov:used            ex:obsA_1 ;
                    prov:wasAssociatedWith  ex:Extractor_v2.3 ;

ex:recA_1          prov:wasGeneratedBy   ex:extractActA_1 .
```

Why need both the record and the activity? Because the record alone only says "this record
exists"; the activity says "this record came from which tool, which version, at what time".
When the extraction tool version changes (a bug fix), all old records still trace back to
the correct old version — this is the foundation of pipeline versioning (§7.24).

### Application

The three sources A, B, C yield three record streams:

| Stream | Observation | Candidate record | Recognized relation |
|--------|-------------|------------------|---------------------|
| A | `ex:obsA_1` (derivative definition) | `ex:recA_1` | derivative of f → measures rate of change of f |
| B | `ex:obsB_1` (velocity definition) | `ex:recB_1` | velocity → measures rate of change of position |
| C | `ex:obsC_1` (current-through-capacitor definition) | `ex:recC_1` | electric current → measures rate of change of voltage |

All three records have the form "X measures_rate_of_change_of Y" — but this is only the
*surface*. The integration layer will decide whether this surface overlap is real or mere
coincidence.

> 🖊 **Self-check:** How do the observation (`ex:obsA_1`) and the record (`ex:recA_1`)
> differ? What is added when moving from observation to record?

## 7.6 Extraction confidence

### Intuition

The same extraction tool extracting a math formula is different from extracting a vague
sentence. The results are not equally trustworthy. We need to note "how trustworthy was the
making of this record *in terms of extraction*".

### Mechanism

**Extraction Confidence** is an assessment attached to each record about how trustworthy
that extraction was, judged by the extraction method and the characteristics of the source
content. It is evidence *about the extraction*, not evidence about the correctness of the
extracted content.

```turtle
ex:extractAssessA_1  a          ex:ExtractionAssessment ;
                     ex:assesses ex:recA_1 ;
                     ex:pattern   ex:Pattern_FormalDefinition ;
                     ex:confidence 0.97 ;
                     ex:rationale  "Formula-type definition, low ambiguity." .
```

Note the subtle point, connecting to Chapter 6: **extraction confidence ≠ claim
confidence**. The record `ex:recC_1` may have high extraction confidence (a clear
definition sentence, a good parsing tool) — but that does not make "current through a
capacitor is the rate of change of voltage" an *accepted statement*. Good extraction only
means "the source content was captured correctly", not "that content is true".

This parallels Chapter 6: confidence must state clearly *what it is assessing* (§6.11).
Here there are three different levels:

1. **Extraction confidence** — was the source content captured correctly (this section).
2. **Claim confidence** — how trustworthy the statement is given evidence (Chapter 6).
3. **Source reliability** — is the source trustworthy (trust profile §7.3).

Three numbers measuring three different things; they must not be added or blended.

> ⚠️ **Common misconception:** "Extraction reached high confidence → the statement is
> true." Wrong. High extraction means *the source text was captured accurately*. If source
> C says something false, a perfectly extracted record is still a false statement — just
> correctly extracted.

## 7.7 Normalization

### Intuition

Two sources write "v = ds/dt" and "velocity is the derivative of position w.r.t. time".
Different surfaces, same meaning. Conversely, two sources both write "rate of change" but
one means the derivative with respect to time, the other with respect to space.
Normalization brings values to canonical form so they are *comparable* — but it must not
flatten away semantic differences.

### Mechanism

**Normalization** transforms values within a record into canonical form: unit conversion
(m/s versus km/h), date formatting, number notation, case. The goal: two values expressing
the same thing must be *equal in form* after normalization, so later steps (comparison,
deduplication, storage) are not fooled by the surface.

Example with source B: two records write "10 m/s" and "36 km/h" — after unit
normalization, both become the canonical form "10.0 m/s".

```turtle
ex:recB_1  ex:unit  "m/s" .
ex:recB_2  ex:unit  "km/h" .

# after normalization:
ex:recB_1n  ex:normValue  10.0 ; ex:normUnit  ex:meter_per_second .
ex:recB_2n  ex:normValue  10.0 ; ex:normUnit  ex:meter_per_second .   # 36 km/h = 10 m/s
```

The key point: **normalization can lose information**. The source's original unit, the
source's original notation *belong to the source* — after normalization, keep the link to
the original record for traceability. Normalization must be a recorded (derivation) step,
not an in-place repair that erases the trail.

> ⚠️ **Common misconception:** "Normalization is just a harmless technical chore." Wrong.
> Normalization decides *what counts as the same*. Choosing the wrong normalization rule
> (e.g. converting every unit to an unannotated "default") makes two different values
> collapse into one — or two identical values drift apart. Normalization is a semantic
> decision and must be versioned like the other rules (§7.24).

## 7.8 Structuring into RDF

### Intuition

A normalized record is still an intermediate data row ("subject, relation, object"). The
structuring step brings it into graph form: choose IRIs for the subject, predicate, and
value — according to a **target schema**. This is where candidate knowledge becomes RDF
triples.

### Mechanism

**Structuring** produces RDF triples from normalized records. For the chapter's three
sources, the target schema is the mechanism schema familiar from earlier chapters:
`ex:rateOfChange_1` (RateOfChange), `ex:derivativeOperation_1` (DerivativeOperation),
`ex:velocity_1` (Velocity), `ex:position_1` (Position) [the book's mechanism frame].

Source A → structured:

```turtle
ex:mechA_1  a             ex:Mechanism ;
            ex:hasOperation  ex:derivativeOperation_1 ;
            ex:hasOutput     ex:rateOfChange_1 .
```

Source B → structured:

```turtle
ex:mechB_1  a             ex:Mechanism ;
            ex:hasOperation  ex:derivativeOperation_1 ;
            ex:hasOutput     ex:velocity_1 ;
            ex:hasInput      ex:position_1 ;
            ex:hasInput      ex:time_1 .
```

Source C → structured (not yet attached to an existing mechanism!):

```turtle
ex:mechC_1  a             ex:Mechanism ;
            ex:hasOperation  ex:derivativeOperation_1 ;
            ex:hasOutput     ex:current_1 ;
            ex:hasInput      ex:voltage_1 ;
            ex:hasInput      ex:time_1 .
```

Note: the structuring step **has not decided** whether `ex:velocity_1` equals
`ex:current_1`. It only brings the three streams into *the same representational shape* so
the later integration steps can compare them. Rendering `ex:current_1` in the same RDF form
as `ex:velocity_1` does not mean they are identical — identity is a *decision* at §7.9–7.10.

Note: `ex:mechC_1` above is the **target shape** under full extraction. In the chapter's
actual case, the source-C extraction did not yet capture the reference variable, so the
record entering the SHACL gate is `ex:appC_1` missing `withRespectTo` (§7.15) — not the
complete `ex:mechC_1`.

### Application

Structuring is where the **target schema** comes into its own: it is the ontology every
source must be mapped to (mapping, §7.12). If the target schema has no "current" (electric
current) concept, source C's record must either create a new concept — or report "not yet
mappable" (unresolved, §7.28); it must not be force-fit onto a near-miss concept.

> 🖊 **Self-check:** Which step in the pipeline (a) decides the RDF shape, (b) decides
> "two things are one", (c) decides "which value is valid"? Mark each step on the §7.1
> diagram.

## 7.9 Identity resolution: candidate generation vs scoring

### Intuition

Two pieces of knowledge "might" talk about the same entity. Comparing every pair is
infeasible when the record count is large (n records → n²/2 pairs). The system must
separate two jobs: *propose the pairs worth looking at* (cheap, biased against missing
any) and *score each proposed pair* (more careful, making the decision).

### Mechanism

**Entity Resolution** is the whole process: deciding whether records from the same or
different sources point to the same real-world entity [@hogan-creation-enrichment]
[@rahm-bernstein-2001]. It comprises two stages with different goals:

1. **Candidate Generation:** produce pairs *likely* to match, using coarse keys (same
   normalized name, same time window). The goal is **recall** — do not miss a truly
   matching pair, accept many non-matching pairs. At this stage, "likely" ≠ "is one".

2. **Scoring:** for each candidate pair, compare in detail across each attribute and make
   a decision: match / non-match / needs review. This is the core of the Fellegi–Sunter
   model (§7.10).

**Blocking** is the technique that implements candidate generation: partition records into
blocks by a blocking key, compare only within each block. Example: a block by the first
letter of the normalized name, or by `ex:hasInput`. If the blocking key is too fine, truly
matching pairs land in different blocks → never compared → **lost recall**. Choosing the
blocking key is a trade-off between speed and coverage.

For this chapter: candidate generation groups `ex:mechB_1` and `ex:mechC_1` into the same
block (both have `ex:hasInput ex:time_1` — both have a time input); `ex:mechA_1` has no
explicit time input so it sits in a different block. The system will compare the pair (B,
C) but not (A, C) — because the blocking key judges A and C to be entirely different. This
is where recall can be lost.

> ⚠️ **Common misconception:** "Candidate generation finds the matching entities." Wrong.
> Candidate generation finds *the pairs to examine*. The match/non-match conclusion comes
> only from the scoring stage. Blending the two stages is the origin of both identity false
> positives and false negatives.

## 7.10 Record linkage: the Fellegi–Sunter model

### Intuition

When a station clerk compares two passengers with the same name, they do not only ask "is
the name the same" — they compare many features (age, hometown, ticket number) and then
estimate the likelihood of being the same person. The Fellegi–Sunter model (1969) does
exactly this, probabilistically [@fellegi-sunter-1969].

### Mechanism

For each candidate record pair, we compare across k attributes and obtain a **comparison
vector** γ — each component records agreement/disagreement on one attribute. Example, the
pair (B, C):

![Identity resolution: candidate generation by blocking → compare the γ vector → three-zone decision by the two Fellegi–Sunter thresholds (non-match / possible match / match).](figures/generated/ch07-entity-resolution.pdf)

| Compared attribute | B (velocity) | C (current) | Agree? |
|--------------------|--------------|-------------|--------|
| operation (derivative) | derivativeOperation_1 | derivativeOperation_1 | ✓ |
| input 1 | position_1 | voltage_1 | ✗ |
| input 2 | time_1 | time_1 | ✓ |
| output | velocity_1 | current_1 | ✗ |

The vector γ = (agree, disagree, agree, disagree).

Fellegi–Sunter defines two probabilities:

- **m(γ):** the probability of observing γ among pairs that *truly match* (same entity).
- **u(γ):** the probability of observing γ among pairs that *truly do not match*.

The likelihood ratio m(γ)/u(γ) is the weight of the comparison vector. Two thresholds
(chosen by the acceptable error rates) divide the result into three zones:

```
γ below the low threshold   →  non-match
γ between the two thresholds →  possible match → manual review
γ above the high threshold  →  match
```

The model is optimal when the compared attributes are conditionally independent — an ideal
assumption, not always true in practice. Importantly: m(γ) and u(γ) must be **estimated
from data** (labels or an unsupervised algorithm), not guessed.

For the pair (B, C): γ = (agree, disagree, agree, disagree). If the system estimates a low
m(γ)/u(γ) (differing inputs/outputs strongly suggest different entities), the pair falls
into the "non-match" zone — the system concludes `ex:velocity_1` ≠ `ex:current_1`, as
physics expects.

For the pair (A, B) — if the blocking key permits comparison: both share the operation
(derivative) and the same "measures rate of change" relation frame, but the outputs differ
(`rateOfChange_1` versus `velocity_1`) and the inputs differ (A does not bind inputs, B has
position + time). The vector γ = (agree operation, disagree output, disagree input) is a
*mixed* vector — it falls into the "possible match" zone, sent to a human. Here caution is
needed: §7.11 schema alignment will check whether "A's output" and "B's output" are the
same *property* — not yet saying they are the same *value*.

### Application

The Fellegi–Sunter result is an **identity decision**, recorded as an integration event:

```turtle
ex:idDecision_BC  a            ex:IdentityDecision ;
                  ex:compares   ex:mechB_1 , ex:mechC_1 ;
                  ex:comparisonVector  "agree,disagree,agree,disagree" ;
                  ex:decision   ex:NonMatch ;
                  ex:rationale  "Different input and output quantities; low likelihood ratio." ;
                  ex:madeAt     "2026-08-30T11:00:00Z"^^xsd:dateTime .
```

A "non-match" decision is a decision **with an error probability**, not an immutable truth.
If new evidence later appears (a source D says "current is exactly the rate of change of
voltage with respect to time, the same derivative mechanism"), the decision can be
overturned — and the trace of the old decision is kept, just like Chapter 6's governance
states.

> 🖊 **Self-check:** A record pair has an all-agreeing γ (every attribute identical). May
> the system immediately conclude "same entity"? If not, what else is needed? Hint: what
> does m(γ)/u(γ) depend on, and how is "possible match" handled?

## 7.11 Schema alignment

### Intuition

Source B calls it "velocity", source D (not yet seen) calls it "vận tốc" (velocity). Before
comparing values, you must know whether the two *columns/properties* share semantics.
Schema alignment answers "which property of this schema corresponds to which property of
that schema".

### Mechanism

**Schema Matching / Schema Alignment** is the process of finding semantic correspondences
between schema elements [@rahm-bernstein-2001]:

- **Element-level:** match individual properties one by one — similar names, similar data
  types ("velocity" ↔ "vận tốc").
- **Structure-level:** match combinations of elements that co-occur within a structure
  ("input pair (position, time) → output velocity" is a structural pattern).

Schema matchers are classified by the information they use:

- **Schema-level:** use only the schema — names, types, constraints, relations.
- **Instance-level:** use the data values to infer meaning ("this column is all large
  positive numbers → possibly a physical measurement").
- **Hybrid:** combine both.

Importantly: **schema alignment does not prove** two properties are one. It proposes a
correspondence + evidence (name similarity, structure similarity) — and the correspondence
must be *confirmed* before use, like Chapter 3's candidate → evidence → acceptance process
(§3.2.5).

### Application

The three sources A, B, C use different names for the same concept. Schema alignment
proposes:

![Schema alignment: `velocity`/`position` (B) have correspondences confirmed against the target ontology; `current`/`voltage` (C) have proposals rejected — correspondence is an evidenced decision, not a name match.](figures/generated/ch07-schema-alignment.pdf)

| Source schema | Element | Proposed correspondence | Evidence |
|---------------|---------|-------------------------|----------|
| A | "derivative of f" | `ex:derivativeOperation_1` | name + definition structure |
| B | "velocity" | `ex:velocity_1` | name + definition |
| B | "position" | `ex:position_1` | name + definition |
| C | "current" | (none yet) — suggests creating a new one | no match in the existing ontology |

Note: source C uses "rate of change of voltage" — schema alignment *may* propose it as
"rate of change" (the same mechanism concept). But this proposal must pass confirmation:
does "electric current" occupy the same structural position as "velocity"? The structure
says no — the inputs differ (position vs voltage), the outputs differ (velocity vs
current). The correspondence is rejected at the confirmation step.

> ⚠️ **Common misconception:** "Two columns with the same name → the same semantics."
> Wrong. "velocity" in schema A might mean "angular velocity" — same name, different
> meaning. Schema alignment is only an *evidenced proposal*; confirmation is the decision.

## 7.12 Mapping: Direct Mapping, R2RML, and CSVW

### Intuition

Having learned "this column ↔ that property", the next step is to *transform the data* from
the source schema to the target schema. There are two extremes: let the system do it
automatically (default mapping) or hand-write a mapping specification (custom mapping).
Both are W3C standards for RDB → RDF.

### Mechanism

**Direct Mapping** (W3C Recommendation 2012-09-27) is the automatic default mapping from a
relational database to RDF [@w3c-direct-mapping]: each table → a class; each row → a
resource (an IRI built from the table name + primary key); each column → a predicate; a
cell value → the object. Because it is fully automatic, the output RDF shape *follows the
database schema*, not the target ontology.

**R2RML** (W3C Recommendation 2012-09-27) is a declarative language for custom mappings
[@w3c-r2rml]. Its central unit is the **Triples Map**: a rule translating each row of a
logical table (a base table, a view, or an SQL query) into zero or more RDF triples, via:

- **Subject Map:** generate the subject IRI (a string template or a constant).
- **Predicate-Object Map:** pair each predicate + object (the object may be a constant, a
  column, or an IRI from another column).

Example R2RML mapping for source B's `velocity_defs` table:

```turtle
@prefix rr: <http://www.w3.org/ns/r2rml#> .
@prefix ex: <http://example.org/mechkg/> .

<#TriplesMap_Velocity>
    rr:logicalTable [ rr:tableName "velocity_defs" ] ;
    rr:subjectMap [
        rr:template "http://example.org/mechkg/velocity/{def_id}"
    ] ;
    rr:predicateObjectMap [
        rr:predicate ex:hasOutput ;
        rr:objectMap [ rr:column "output_iri" ]
    ] ;
    rr:predicateObjectMap [
        rr:predicate ex:hasInput ;
        rr:objectMap [ rr:column "input1_iri" ]
    ] .
```

Why distinguish the two kinds? Because **Direct Mapping does not know the target
ontology**: it yields "table velocity_defs becomes class velocity_defs" — faithful to the
source, but not the desired shape (`ex:velocity_1 a ex:Velocity`). R2RML lets you write the
intent exactly. The decision "use the default mapping or hand-write one" is precisely the
decision about *the shape of knowledge in the system* — a semantic decision, not a
technical one.

(For spreadsheet-style CSV sources, the corresponding standard is CSVW — the Model for
Tabular Data, W3C Recommendation 2015-12-17 — with a table model: table/row/column/cell +
annotations to declare the primary key, data types, and to generate RDF via csv2rdf
[@w3c-tabular-data-model].)

### Application

In the book's pipeline, mapping sits at the structuring boundary (§7.8): the system's
target schema is the mechanism ontology; each new source has a **mapping specification** —
a versioned artifact (something reviewable, editable, reprocessable), not hidden code
inside the pipeline.

> 🖊 **Self-check:** For source C's table `definitions(name, meaning, unit)`. Write an R2RML
> subject map and one predicate-object map that turns the `meaning` column into
> `ex:hasOutput`. If you used Direct Mapping, what would the output look like — and why
> might it be unusable?

## 7.13 Deduplication

### Intuition

Two sources both say "velocity is the rate of change of position with respect to time" —
same content, different sources. These are not two independent statements worth keeping
whole: they are **content duplicates**. But you must not delete one either: each carries
its own provenance. Deduplication is *reconciliation*, not deletion.

### Mechanism

**Deduplication** is recognizing duplicate records/statements — exact duplicates
(identical) or near-duplicates (same proposition, differing value/unit) — and deciding how
to handle them. Connecting to Chapter 6: two claims with the same content are still two
separate objects (claim identity ≠ content identity, §6.2). So deduplication at the
integration layer does not merge claim IRIs; it merges *how they enter the ledger*.

**Claim Deduplication** is the book's own rule: two candidate claims with the same content
but different provenance are *content-duplicate candidates*; they may be merged into one
ledger entry only through a merge decision that records **both** provenances — never
silently discarding one side.

Compare two records B (from source B) and B′ (from source D, same content):

| Record | Content | Source |
|--------|---------|--------|
| `ex:recB_1` | velocity = rate of change of position | `src:sourceB` |
| `ex:recD_1` | velocity = rate of change of position | `src:sourceD` |

The content hashes (§7.14) of the two records are equal → a content duplicate is detected.
The system does not create two ledger entries; it creates *one* integrated claim carrying
two provenances. If the two sources are *both independent* (not an echo source, §7.23), the
integrated claim has two independent supporting sources — stronger evidence than a
single-source claim.

> ⚠️ **Common misconception:** "Deduplication = delete the duplicate record." Wrong.
> Deletion loses evidence and provenance. Correct deduplication is *loss-preserving
> merging*: both sources remain stored in the integrated claim, they simply no longer stand
> as two independent claims in the ledger.

## 7.14 Idempotent ingestion and content hashing

### Intuition

Re-running the pipeline on the same data — to fix a bug, to experiment — must yield the
same result. If the second run creates a second copy of every claim, the ledger quickly
becomes contaminated with duplicates. The system needs a mechanism that makes re-running
"harmless": **idempotent ingestion**.

### Mechanism

**Idempotent Ingestion** means: running the same acquisition/integration process many
times yields the same ledger state — no duplicate claims, no duplicate provenance. The
condition: the steps must be *deterministic* and use a **content hash** as a stable key.

A **Content Hash** is a deterministic fingerprint (digest) of a record/normalized content —
hashed over the canonical form (subject IRI, predicate, typed object, source fragment).
Change the content → change the hash. Example:

```turtle
ex:recB_1  ex:contentHash  "f3a9…c2"^^xsd:string .
```

Two runs over the same source B both yield `ex:recB_1` with the same hash. The second run
finds the hash already exists → skips it, creating no copy. If source B is updated (a new
edition), the hash changes → a new record is created, the old one kept with its old
provenance (no overwrite, per Chapter 6's immutability principle).

Four cautions:

1. **Hash ≠ claim identity.** A content hash is only a duplicate-detection key. The claim's
   IRI in the ledger is a separate governed object (Chapter 6). Using the hash as the
   claim's IRI is a mistake: two same-content claims from different sources would be wrongly
   merged.

2. **Hash ≠ provenance.** Knowing "this record has hash X" does not tell you "where this
   record came from". The hash only serves deduplication and idempotency.

3. **Different hashes ≠ different meaning.** Two different phrasings of the same proposition
   ("velocity is the derivative of position" and "vận tốc là đạo hàm của vị trí") produce
   two different hashes over the raw form — but may be the same semantic content after
   normalization and schema alignment (§7.11). Conversely, *equal* hashes only mean
   normalized-content duplication, not that the two claims are one (point 1). The hash
   reports *form duplication*; every conclusion about *meaning* must pass through the
   integration steps.

4. **Idempotent ≠ correct.** Re-running to the same result does not mean the result is
   correct — only that it is *stable*. An idempotent pipeline can still consistently produce
   false statements, if its rules are wrong.

> 🖊 **Self-check:** Why must the hash be computed over the *normalized form* rather than
> the source's raw text? Hint: two sources write "10 m/s" and "36 km/h" — the raw-form
> hashes differ, the normalized-form hashes match. If you skipped normalization, what would
> happen to deduplication?

## 7.15 The SHACL gate: valid differs from accepted

### Intuition

Before entering the ledger, a candidate statement must pass a *shape* check: does it have
all required properties, are the data types correct, is the cardinality valid? This is
where SHACL (Chapter 5) enters the pipeline.

### Mechanism

The **SHACL gate** checks candidate triples against declared shapes — requirements on
class, property, type, cardinality — and produces a conformance report [@w3c-shacl].

Two shape levels in the pipeline:

```turtle
ex:MechanismShape  a            sh:NodeShape ;
                   sh:targetClass ex:Mechanism ;
                   sh:property [
                       sh:path ex:hasOperation ;
                       sh:minCount 1 ;
                       sh:nodeKind sh:IRI
                   ] ;
                   sh:property [
                       sh:path ex:hasOutput ;
                       sh:minCount 1 ;
                       sh:nodeKind sh:IRI
                   ] .

ex:DerivativeApplicationShape  a          sh:NodeShape ;
                   sh:targetClass ex:DerivativeApplication ;
                   sh:property [
                       sh:path ex:hasOperation ;
                       sh:minCount 1 ;
                       sh:nodeKind sh:IRI
                   ] ;
                   sh:property [
                       sh:path ex:differentiand ;
                       sh:minCount 1 ;
                       sh:nodeKind sh:IRI
                   ] ;
                   sh:property [
                       sh:path ex:withRespectTo ;
                       sh:minCount 1 ;
                       sh:nodeKind sh:IRI
                   ] ;
                   sh:property [
                       sh:path ex:hasOutput ;
                       sh:minCount 1 ;
                       sh:nodeKind sh:IRI
                   ] .
```

`ex:DerivativeApplicationShape` is the shape for candidates in **n-ary** form (Chapter 3):
a `DerivativeApplication` must bind operation, differentiand (the differentiated quantity),
`withRespectTo` (the reference variable), and output. Suppose the source-C extraction yields
the following candidate — missing `withRespectTo` (the extraction tool did not capture "with
respect to time"):

```turtle
ex:appC_1  a                ex:DerivativeApplication ;
           ex:hasOperation  ex:derivativeOperation_1 ;
           ex:differentiand ex:voltage_1 ;
           ex:hasOutput     ex:current_1 .
           # missing ex:withRespectTo
```

The SHACL gate runs the shape over `ex:appC_1` and produces a violation report:

```turtle
[]  a                sh:ValidationReport ;
    sh:conforms       false ;
    sh:result  [ a    sh:ValidationResult ;
                 sh:focusNode ex:appC_1 ;
                 sh:resultPath ex:withRespectTo ;
                 sh:sourceConstraintComponent sh:MinCountConstraintComponent ;
                 sh:resultSeverity sh:Violation ;
                 sh:resultMessage "ex:withRespectTo is required but missing." ] .
```

The report pinpoints: the focus node (`focusNode` = `ex:appC_1`), the path (`resultPath` =
`ex:withRespectTo`), the constraint (`MinCountConstraintComponent`), the severity
(`Violation`). Given this report, the possible policy responses are:

- **Retry extraction:** re-run the tool with a fixed pattern to capture "with respect to
  time".
- **Review:** send the candidate to the queue (§7.20) for a human to resolve.
- **Defer:** keep the candidate, do not enter the ledger.
- **Reject:** drop the candidate, record the reason.
- **Evidence-supported repair:** add `withRespectTo ex:time_1` *only if* another source
  fragment within the same fragment proves the reference variable.

You must **never fabricate `ex:time_1`** just to make the report `conforms true` — that
policy turns the SHACL gate into an error-rationalizing machine, the opposite of its
purpose (see §7.27 on unresolved values).

The crux — **valid ≠ accepted**:

- A triple *valid* in shape may still be *rejected* at the governance step (conflicting
  with stronger evidence, §7.16).
- A triple *not valid* is not auto-deleted — it goes to the review queue (§7.20) or back to
  extraction.

The SHACL gate is a **structural filter**, not a truth filter. It ensures "correct shape",
not "correct fact". This is exactly Chapter 5's conformance ≠ truth lesson, placed in the
middle of the pipeline.

### Application

In the pipeline: all structured triples (A, B, C) must pass the gate. A's and B's triples
are valid; C's candidate `ex:appC_1` is missing `withRespectTo` → not valid → falls into
the review queue, and must *not* go straight into the ledger.

> ⚠️ **Common misconception:** "The SHACL report says conforms → the statement is true."
> Wrong. `conforms true` only means *the shape matches*. A shape-valid triple can be
> semantically meaningless (e.g. `ex:velocity_1 ex:hasInput ex:voltage_1` — right shape,
> wrong meaning). Validity is a necessary, not sufficient, condition for acceptance.

## 7.16 Conflict detection

### Intuition

When two candidates say different things about the same thing, the system must not ignore
it. It must *recognize* the conflict, classify it, and decide. This is where Chapter 6's
five-kind contradiction taxonomy is exercised inside the pipeline.

### Mechanism

**Conflict Detection** finds pairs of statements (candidate-vs-candidate, or candidate-vs-a
claim already in the ledger) whose contents cannot both be true in the same context. It
uses the five-kind taxonomy of §6.6:

| Kind | Example in the mechanism domain |
|------|---------------------------------|
| Logical | `ex:current_1` being both `ex:Velocity` and `ex:Current` if the two classes are disjoint |
| Value | two claims both stating `ex:velocity_1 ex:value` but with different numbers |
| Temporal | "velocity = ds/dt" valid from 1687, "velocity is additive" valid from 1905 — different valid time, not a conflict |
| Scope | instantaneous derivative versus finite difference Δx/Δt over an interval — different scope, *not* automatically a contradiction; source A says "derivative with respect to space", source B "with respect to time" — different scope |
| Source | two sources say different things but both assert one event — a source conflict |

Note: **not every textual difference is a conflict.** Source A says "the derivative
measures the rate of change of f", source B says "velocity is the rate of change of
position" — differing wording but possibly the same proposition under a schema mapping.
Before declaring a conflict, the system must *try to reconcile context* (§6.6): is it a
valid-time difference? a scope difference? If reconcilable, there is no conflict — only two
statements with different contexts.

### Application

The pair (A, B) after schema alignment: "derivative of f" ↔ `ex:derivativeOperation_1`,
"velocity" ↔ `ex:velocity_1` — two different statements that both reduce to the mechanism
`rateOfChange_1`. They **do not conflict**, and are also **not content duplicates** (the
outputs differ: `rateOfChange_1` versus `velocity_1`) — they are two complementary distinct
statements (§7.31, stage 8). The pair (B, C): `ex:velocity_1` versus `ex:current_1` — schema
alignment already rejected the correspondence (differing input/output) → not a conflict, but
two different concepts. A real conflict appears only when, *in the same context*, the values
differ — for example two sources both asserting the velocity value of the same object at
the same moment but with different numbers.

> ⚠️ **Common misconception:** "Two sources say different things → the system is
> inconsistent → must fix it." Wrong. A difference may be a contextual difference (time,
> scope) — not a conflict. Declaring conflicts too hastily leads to "fixing" what did not
> need fixing and losing information.

## 7.17 Integration decisions and merge outcomes

### Intuition

A group of candidates has passed identity, schema alignment, deduplication, SHACL, and
conflict detection. Now the system must *decide*: what to write into the ledger, what to
reject, what to send to a human for review.

### Mechanism

An **Integration Decision** is a decision over each candidate group: **accept**, **reject**,
or **defer to review**. Every decision must carry a recorded reason — nothing may be
accepted silently.

![The integration decision diagram: SHACL gate → conflict detection → three branches (accept / review / reject) → ledger insertion. Every branch records its reason; no claim is deleted.](figures/generated/ch07-integration-decision.pdf)

A **Merge Outcome** is the effect on the ledger of an accepted candidate group, per
Chapter 6's possibilities:

- **Insert:** a new integrated claim is created in the ledger.
- **Strengthen:** an existing claim gains additional evidence from the new candidate (same
  content, independent source).
- **Supersede:** a better candidate replaces the old claim — the old claim moves to the
  Superseded state, not deleted (§6.13).
- **Merge:** two same-content candidates from different sources combine into one entry,
  keeping both provenances (§7.13).

```turtle
ex:mergeOutcome_1  a            ex:MergeOutcome ;
                   ex:kind       ex:Strengthen ;
                   ex:target     ex:claim_velocity_rate_of_change ;
                   ex:addsEvidence  ex:recD_1 ;
                   ex:fromDecision  ex:integrationDecision_1 .

ex:integrationDecision_1  a         ex:IntegrationDecision ;
                          ex:verdict  ex:Accept ;
                          ex:rationale "Content identical to accepted claim; independent source adds evidence." ;
                          ex:madeAt   "2026-08-30T12:00:00Z"^^xsd:dateTime .
```

The preservation principle throughout: **a losing claim is never deleted** — it is either
Superseded or stored with a Rejected state and a full reason, as Chapter 6 stipulated
(§6.12, §6.14).

> 🖊 **Self-check:** Consider this: a new candidate has the same content as an existing
> Accepted claim, but the new candidate's source is an echo source (copied from the old
> claim's source). What should the integration decision be? Should the old claim be
> strengthened by this "new" evidence?

## 7.18 Claim Ledger first

### Intuition

The Claim Ledger (Chapter 6) is the *single place* recording the system's governed truth.
Every query should read from the ledger (via the projection), not from the pipeline's
intermediate buffers. The principle: **ledger first, everything else after**.

### Mechanism

**Claim Ledger Insertion** is a committed write of an Accepted claim into the ledger,
carrying the full "epistemic envelope": content, provenance, evidence, temporal scope,
governance state, confidence.

The **Canonical Projection** is a materialized view rebuilt *from* the ledger after
governance — a query reading this view sees the Accepted (and reconciled) claims. It is
reconstructed from the ledger; it is not an independent store of truth.

Why "ledger first"? Because if the intermediate steps (extraction buffer, integration
buffer) are treated as sources of truth, the system ends up with several competing truth
sources. One query might read an "Accepted" claim from the ledger, another read the same
content from an intermediate buffer that has not passed governance — contradictory results,
unexplainable. The "ledger first" principle guarantees *a single source of truth*.

### Application

In the pipeline: the final stage writes to the ledger only after every gate has been
passed. There is no "draft-write first, govern later" — everything entering the ledger is
the result of a recorded integration decision.

> ⚠️ **Common misconception:** "Querying the extraction buffer is also querying the
> knowledge graph." Wrong. The intermediate buffer holds *candidate knowledge* — not yet
> deduplicated, not yet governed. Only the projection from the ledger is "what the system
> believes". Mixing the two is the origin of inconsistent answers.

## 7.19 Lineage: where did it come from? — and why lineage differs from evidence

### Intuition

When an Accepted claim appears in the projection, a user has the right to ask: "where did
this come from?" and "why should I believe it?". Two different questions, two different
kinds of data.

### Mechanism

**Lineage** is the full provenance chain from a claim in the ledger, traced backward
through the integration decisions, the extractions, the observations, to the source
fragments [@prov-dm]. Lineage answers "where did it come from?" — an auditable path:

```
ex:claim_velocity_rate_of_change
   ← ex:integrationDecision_1          (integration decision)
   ← ex:mergeOutcome_1                 (merge)
   ← ex:recB_1                         (extracted record)
   ← ex:extractActB_1                  (extraction activity, version 2.3)
   ← ex:obsB_1                         (observation)
   ← src:fragB_2_1                     (source fragment)
   ← src:sourceB                       (source)
```

**Evidence** answers "why believe it?" — information supporting/refuting the claim
(Chapter 6, §6.3, §6.5). A claim can have very complete lineage but weak evidence, or
strong evidence but thin lineage.

This is the chapter's subtlest point: **complete lineage is not evidence**. A perfect
pipeline (long, complete, clean lineage) can produce a false claim if the source is wrong
or the rule is wrong. Long lineage only tells you "every step was recorded" — not that
"those steps are correct".

### Application

Every claim in the ledger must have minimum lineage (this is invariant I1, §7.30). During
an audit, the reviewer walks backward along the lineage to reconstruct *how* the claim
formed — then *separately* assesses the evidence supporting that claim.

> ⚠️ **Common misconception:** "The longer the lineage, the more trustworthy the claim."
> Wrong. Lineage says "where it came from"; Evidence says "why believe it". A claim with a
> 10-step lineage and zero evidence is still weaker than a claim with a 2-step lineage and
> strong independent evidence. Using lineage as a trustworthiness measure is a serious
> semantic error.

## 7.20 Human in the loop: the review queue

### Intuition

The Fellegi–Sunter model has a "possible match" zone between the two thresholds — not
confident enough to conclude, not confident enough to discard. This zone, together with
SHACL-failure cases and unreconcilable conflicts, enters the **review queue** — where
humans decide.

### Mechanism

The **Review Queue** is the lane for cases the automated pipeline cannot decide with the
policy-required confidence. A human reviews with the *full evidence set* — not a one-line
summary — and decides, the decision recorded in the ledger like every other decision.

Three kinds of cases enter the queue:

| Case type | Example |
|-----------|---------|
| Possible match (Fellegi–Sunter) | pair (A, B): 3/4 attributes agree, needs a human eye to confirm "same proposition?" |
| SHACL fail | `ex:appC_1` missing `withRespectTo` — needs a re-look at extraction |
| Unreconcilable conflict | two claims, same context, differing values, not reconcilable |

The balancing principle: send *every* case to a human → there is no pipeline (everything
stops at a person); send *no* case → uncontrolled error risk. The review policy is part of
the integration policy (§7.29), and is versioned.

> ⚠️ **Common misconception:** "A human reviewer is more correct than the machine." Not
> automatically true. Human reviewers also make mistakes — but they are a *different
> decision channel*, one that may carry knowledge beyond the data. The queue's value lies
> in the decision being *recorded and traceable*, not in "humans are always right".

## 7.21 Dimensions of data quality

### Intuition

"Good data quality" is a vague phrase. Data can be accurate but incomplete, complete but
outdated, consistent but untraceable. Quality is **multi-dimensional** — and each
dimension measures a different thing, like Chapter 6's multi-dimensional confidence (§6.11).

### Mechanism

The book uses six quality dimensions for the pipeline:

| Dimension | Question | Measured by |
|-----------|----------|-------------|
| **Accuracy** | Does the record match the source / reference standard? | sample reconciliation |
| **Completeness** | Has all the content worth capturing been captured? | fraction of fragments processed |
| **Consistency** | Are there unreconciled contradictions in the ledger? | count of outstanding found/contradictions |
| **Timeliness** | Is the data still current relative to its valid time? | compare system time with valid time |
| **Provenance completeness** | Does every claim have sufficient lineage? | invariants I1–I2 (§7.31) |
| **Conformance** | Does the SHACL shape match? | validation report (§7.15) |

Three important lessons:

1. **A single "95% quality" number is meaningless.** 95% of which dimension? Accuracy 95%
   + completeness 40% is a very different picture.
2. **Completeness does not imply accuracy.** Capturing everything (good completeness) but
   extracting wrongly (poor accuracy) still yields a ledger full of false statements.
3. **Quality is policy-relative.** The "reference standard" used to measure accuracy is a
   choice — measuring against an internal ontology differs from measuring against an
   external reference source.

> 🖊 **Self-check:** A pipeline reports "completeness 100%, accuracy 92%". Write two
> scenarios (one harmless, one dangerous) for that 8% inaccuracy. Why do you need both
> numbers, not just one?

## 7.22 Pipeline failure modes

### Intuition

An 11-stage pipeline has 11 places to break. A good system is not one that never breaks —
it is one that knows each *failure mode* clearly, has a detection signal, and has a
recovery path.

### Mechanism

The book catalogs 13 failure modes of the acquisition/integration pipeline. For each mode:
a detection signal and a recovery action.

| # | Failure mode | Detection signal | Recovery |
|---|--------------|------------------|----------|
| FM1 | Wrong extraction (captured the wrong content) | sample reconciliation; low extraction confidence | fix the pattern, reprocess |
| FM2 | Wrong normalization (wrongly merged / failed to merge) | two "similar" values yield different hashes; or the reverse | review the normalization rules, new version |
| FM3 | Blocking loses recall (matching pairs never meet) | compare results against a known sample | change the blocking key, re-run |
| FM4 | Identity error (false positive/negative) | sample check; a decision overturned when new evidence appears | record it, overturn the decision with a reason |
| FM5 | Wrong schema alignment (mis-mapped property) | weak alignment evidence, rejected at confirmation | keep the rejected proposal as a trace |
| FM6 | Mapping bug (R2RML runs wrong) | validation report; output data not as expected | fix the mapping spec, new version |
| FM7 | Lost idempotency (re-run creates duplicates) | claim counts before/after a re-run differ | fix determinism, delete the duplicate with a reason |
| FM8 | Confusing validation ≠ acceptance | a "valid" claim enters the ledger without governance | keep the SHACL gate and the governance gate separate |
| FM9 | Partial acquisition (missed a fragment) | completeness < 100%, missing fragments flagged | re-run with the full fragment list |
| FM10 | An echo source counted as independent evidence | two "independent" sources share a lineage | flag the echo source (§7.23) |
| FM11 | Chunking breaks meaning (cut mid-definition) | incomplete fragment; repeated extraction failure | change the chunk boundary, re-run |
| FM12 | Retrieval-bound violation (over-reading) | a statement exceeds the fragment's content | check the retrieval bound (§7.26) |
| FM13 | Policy drift | integration decisions deviate from the historical norm | version the policy, alert |

An important observation: **no failure mode is detected by "the run finished smoothly"** —
every signal requires *active measurement* (observability, §7.34). A pipeline that reports
no errors does not mean the pipeline is error-free; it may be failing quietly.

> ⚠️ **Common misconception:** "The pipeline finished without errors → the data is good."
> Wrong. Three failure modes (FM3, FM4, FM9) can complete "successfully" yet yield wrong
> results — wrong identity, missing data. "No errors reported" and "no errors" are two
> different things.

## 7.23 Echo sources

### Intuition

A website aggregating "10 essential physics definitions" copies the velocity definition
from textbook B. If the system records both as two independent sources, it will believe
`ex:recB_1` has two supporting sources — when in reality there is only one. An **echo
source** inflates the apparent evidence count.

### Mechanism

An **Echo Source** is a source whose content is ultimately derived from another source
already in the system — a summary, a copy, an aggregator feed. Recognizing an echo source
usually rests on: very high content overlap, lineage/publication history, or an explicit
"after [the original source]" attribution.

Echo sources are not banned — they have traceability value (knowing "who copied from whom"
is also knowledge). What is banned is **counting an echo claim as independent evidence**:

```turtle
ex:claim_vroc  ex:hasEvidence  ex:recB_1 ;        # independent source (textbook B)
               ex:hasEvidence  ex:recD_1 .        # echo source (aggregator copied B)
```

The claim has "two pieces of evidence" — but these two pieces are **not independent**.
Under the trust policy (Chapter 6 §6.5), dependent evidence must be scored lower: two
same-origin sources are worth only slightly more than one source, not twice as much.

### Application

For the chapter's three sources: if source D (the aggregator) registers later with content
matching source B, the system flags `src:sourceD` as an echo of `src:sourceB`. When source
D submits a same-content candidate, that candidate is kept (provenance) but is **not**
counted as independent evidence for the claim.

> ⚠️ **Common misconception:** "Many sources say the same thing → it must be true." Wrong
> — if those sources are echoes of one another, the "many" is an illusion. Counting
> evidence must count *independent sources*, not *instances*.

## 7.24 Pipeline versioning and reprocessing

### Intuition

The pipeline is not a static machine — it is improved: normalization rules get bug fixes,
R2RML mappings gain a column, the blocking key changes. Each change can alter the results
of everything *downstream* of the change. Without versioning, no one knows which "pipeline"
produced a given claim.

### Mechanism

**Pipeline Versioning:** every output-shaping component — mapping, extraction pattern,
normalization rules, blocking key, target schema, SHACL gate, integration policy — is
versioned; and the *version stamp* is written into the provenance of each acquired claim.

```turtle
ex:recB_1  ex:pipelineVersion  "acq-int-v7.3"^^xsd:string ;
           ex:extractorVersion  "extractor-2.3"^^xsd:string .
```

**Reprocessing** is re-running all or part of the pipeline over the same source data after
the pipeline changes version. Reprocessing is safe **only if** ingestion is idempotent
(§7.14): re-running creates no duplicates. Reprocessing results pass through *the same
gates* as the first time — they must not be "grandfathered" because the data is thought to
be already known.

Importantly: reprocessing **does not automatically overturn the old decision**. The old
claim remains the ledger; the new candidate (from the new pipeline) goes through
governance: it may strengthen, supersede, or be rejected. The ledger is never "overwritten
by a re-run".

### Application

When fixing source C's extraction pattern (FM9: previously the extraction missed the
reference variable `withRespectTo` — see §7.15), the system re-runs the new-version
pipeline over source C. The new records carry the new `pipelineVersion`; the old claim
missing `withRespectTo` is not deleted — it is superseded by the new complete claim, with a
transition trace.

> 🖊 **Self-check:** Why do "re-running the pipeline" and "idempotency" go hand in hand? If
> the pipeline were not idempotent, what would a re-run create — and why would that corrupt
> the ledger?

## 7.25 Batch vs stream processing

### Intuition

Some sources arrive in large periodic volumes (a weekend database dump), others trickle in
continuously (an API updating every minute). The same conceptual pipeline, two different
deployment rhythms.

### Mechanism

**Batch:** all source data is processed in one periodic pass, results written to the ledger
after the pass completes. Pros: good control, easy reproducibility, easy per-pass audit.
Cons: the ledger ages between passes.

**Streaming:** each part of the data is processed as it arrives. Pros: timely (high
timeliness). Cons: must handle *order*, and the integration state may be incomplete (a
candidate arrives first, the source to reconcile against arrives later).

Regardless of rhythm, **the batch and stream segments must share logic and version** — the
same normalization rules, the same blocking key, the same SHACL gate. If batch and stream
use two different logic versions, the same data taking two paths yields two different
results — and the ledger can no longer explain why. This is a variant of FM13 (policy
drift).

For the ledger: both rhythms end in a committed ledger write (§7.18) — the ledger does not
distinguish "arrived by batch or by stream"; it only knows claim + provenance.

> ⚠️ **Common misconception:** "Streaming is the more modern version of batch, so it is
> better." Wrong. Streaming pays with harder order and state control. Choosing batch or
> stream is a choice driven by *source characteristics and timeliness requirements*, not by
> fashion.

## 7.26 Source types: structured, semi-structured, unstructured text

### Intuition

The chapter's three sources are all textbook prose. But sources can be relational
databases, CSV tables, long PDF documents. Each type has its own extraction path — but all
paths converge on the same integration stages.

### Mechanism

| Source type | Example | Path into the pipeline | Related standard |
|-------------|---------|------------------------|------------------|
| **Structured** | relational database | table → triple mapping | Direct Mapping, R2RML [@w3c-direct-mapping] [@w3c-r2rml] |
| **Semi-structured** | CSV, JSON, HTML | declare annotations + column mapping | CSVW + csv2rdf [@w3c-tabular-data-model] |
| **Unstructured** | text, PDF | chunking → extraction (§7.5) | no dedicated extraction standard; the result is a candidate record |

**Chunking** applies to long documents: a document is split into fragments with boundaries
and addresses (by heading, paragraph, or fixed size) so extraction works on coherent units
and provenance is fine-grained. The chunk boundary is **an epistemic decision**, not a
neutral plumbing detail: it decides *which information is available to the extraction step*.
A mechanism example:

> Sentence 1: "The derivative measures instantaneous change."
> Sentence 2: "For position with respect to time, this quantity is velocity."

A bad chunk boundary cuts between these two sentences: sentence 1 goes into the first
chunk, sentence 2 into the second. Extraction over chunk 1 sees only "the derivative
measures instantaneous change" — it *cannot* know that "this quantity" in sentence 2 is
velocity, because the connective material (the pronoun "this quantity") was pulled into a
different chunk. The same document, two chunkings, two different extraction capabilities —
cutting mid-definition (FM11) breaks both the fragment and the extraction. Chunking
therefore changes *the information extraction is allowed to see*, and is a design with
semantic consequences.

**Retrieval Bound:** extraction from a fragment may assert only what *that fragment itself*
contains, in its context — not using knowledge from later chapters, an adjacent table, or
"world knowledge" to fill gaps. Source A defines the derivative in §3.2; the system must not
attribute to fragment A the sentence "velocity is the derivative of position" just because
source B says so.

This also applies when the pipeline has a **retrieval** step that selects documents to feed
extraction: the `top_k`/context-limit parameter decides which fragments are *seen* in this
extraction pass. If the RATE_OF_CHANGE definition falls outside the retrieved context, the
extraction tool cannot use it — and a statement may be misclassified merely because the
deciding evidence was not in the window. The lesson: *evidence that is not seen cannot
affect this extraction pass* — not because the evidence does not exist, but because the
retrieval bound blocked it. Retrieval and chunking are epistemic decisions, not harmless
implementation details.

Note: a silent fragment ≠ a negation. Fragment A not mentioning "electric current" does not
mean fragment A denies the concept of electric current (still the Open World Assumption,
§5–6). The retrieval bound forbids *adding*, not *lacking*.

### Application

Sources A, B, C (textbook prose) → chunk by heading: each definition is one chunk. If
source A is also supplied in tabular form (a table of derivatives of basic functions), that
table takes the CSVW path with annotations, while the prose definitions take the chunk path.
The two streams meet at the candidate record — and from there, regardless of origin, they
share one path.

> 🖊 **Self-check:** A source-A fragment contains the derivative definition, not mentioning
> velocity. The system may assert "the derivative is a mathematical concept" from this
> fragment — but may not assert "velocity is the derivative of position" from *this same*
> fragment. Why? Where does the difference between the two assertions lie?

## 7.27 Extraction schemas and unresolved values

### Intuition

Extraction must know in advance *what shape of record it will produce*: which fields, what
types, required or optional. Without this declaration, each source emits an arbitrary
record shape — and the later stages do not know how to cope. At the same time, extraction
may *fail to find* a value: the system must have an honest way to say "not yet known".

### Mechanism

An **Extraction Schema** declares the structure of the intermediate record: the field
list, expected data types, cardinality (1..1, 0..n), and the allowed value domain. It makes
the extraction output *predictable and checkable* — like a contract between the extraction
step and the later steps.

```turtle
ex:ExtractionSchema_Velocity  a        ex:ExtractionSchema ;
                              ex:field  ex:subject     ; ex:fieldKind ex:Required ;
                              ex:field  ex:relation    ; ex:fieldKind ex:Required ;
                              ex:field  ex:object      ; ex:fieldKind ex:Required ;
                              ex:field  ex:unit        ; ex:fieldKind ex:Optional ;
                              ex:field  ex:contextNote ; ex:fieldKind ex:Optional .
```

When extraction cannot determine a value (the unit is not written in the sentence, the
reference is ambiguous), there are two wrong ways and one right way:

- **Wrong — Guess** — fill the value by inference beyond the fragment (violates the
  retrieval bound).
- **Wrong — Stay silent** — drop the field, losing the trace "we once did not know".
- **Right — Unresolved Value** — model it explicitly:

```turtle
ex:recC_1  ex:unit  ex:unknownUnit .
```

Note the OWA semantics: `ex:unknownUnit` means *"the system has not yet determined the
unit"*, not *"there is no unit"*, and certainly not "a default value". Not-yet-known ≠
does-not-exist (§6.20 — negation differs from absence).

> ⚠️ **Common misconception:** "If extraction fails, leaving it blank is harmless." Wrong.
> A blank value is handled by later steps as "no value" — different from "not determined".
> Leaving it blank distorts things: deduplication may treat two "missing-unit" records as
> duplicates even though their units actually differ. You must record "unknown" explicitly.

## 7.28 Integration policy: rules governing decisions

### Intuition

The decisions in §7.17 are not arbitrary — they follow a declared rule set, treated as an
artifact. That rule set is the **integration policy**.

### Mechanism

An **Integration Policy** is a versioned rule set deciding how integration behaves: which
threshold to accept at, which conflicts must go to a human, how echo sources are handled,
what independent evidence requires, when to supersede. It *operationalizes* Chapter 6's
governance over Chapter 7's pipeline.

The theoretical grounding comes from data-integration theory: an integration system is
formalized into three components (a global schema G, source schemas S, and mappings M)
[@lenzerini-2002]. Two important concepts:

- **GAV (global-as-view):** the global schema is expressed *through* the sources — easy to
  query, hard to add new sources.
- **LAV (local-as-view):** the sources are expressed *in terms of* the global schema — easy
  to add sources, hard to query.
- A mapping can be **sound** (the data is a subset of the assertion), **complete** (a
  superset), or **exact** (both).

The book does not require implementing a specific GAV/LAV — it uses this frame to teach the
core lesson: **integration is a mapping decision with a chosen semantics**, not a
mechanical blend. The book's policy specifies that the integration side behaves *according
to which semantics* (default: sound — never assert more than the source allows).

Example policy rules:

```turtle
ex:policy_v1  a          ex:IntegrationPolicy ;
              ex:rule    ex:rule_review_on_value_conflict ;   # value conflict → human review
              ex:rule    ex:rule_echo_not_independent ;       # echo not counted as independent evidence
              ex:rule    ex:rule_sound_mapping_default .      # mapping under sound semantics
```

The policy is a versioned artifact (§7.24) — editing the policy does not edit the decision
history, but subsequent decisions follow the new version.

## 7.29 Transaction boundaries

### Intuition

Writing many claims to the ledger at once — half succeed, half error — leaves the ledger in
a "half-done" state. We must define the unit of commitment: **what commits, commits fully,
or nothing commits**.

### Mechanism

A **Transaction Boundary** defines a group of operations committed as one atomic unit. In
the book's pipeline, the default boundary is *one integration decision together with its
consequences*: insert/strengthen/supersede/merge + record the reason + record the
provenance + update the projection — all commit together, or all roll back.

Why needed? Because the ledger must never be in a state "the new claim is written but the
reason is lost" (violates invariant I7, §7.30). The transaction guarantees *all or nothing*
— the ledger is always a valid state.

> 🖊 **Self-check:** A transaction writes claim + evidence + decision rationale. If the
> rationale-write step fails but the claim is still kept, what is the consequence? Which
> invariant is violated?

## 7.30 Seven invariants of the pipeline: I1–I7

### Intuition

The discipline of the whole chapter can be packed into seven rules that must never be
violated. Each invariant protects one dimension: traceability, transparency,
non-destruction.

### Mechanism

**Invariants** are constraints the pipeline must *never* violate — enforced automatically
and by audit. The book's seven invariants:

| # | Invariant | Meaning | Guards against |
|---|-----------|---------|----------------|
| **I1** | Every claim in the ledger has provenance to at least one source fragment | No claim "springs from nothing" | FM6, FM8, lost origin |
| **I2** | Every provenance edge carries a pipeline version stamp | Know which pipeline produced the claim | FM13, policy drift |
| **I3** | Content hash uniquely identifies normalized content within a source | Deduplication and idempotency work correctly | FM7, FM2 |
| **I4** | A validation report accompanies every candidate through integration | Decisions can see conformance | FM8, confusing validation/acceptance |
| **I5** | No claim is ever overwritten — only state transitions | Immutable ledger, contradiction preserved (Ch6) | overwrite FM, lost history |
| **I6** | Re-ingestion yields the same ledger state (idempotent) | Re-running is harmless | FM7, duplicates |
| **I7** | Every decision has a recorded reason | Decisions are not arbitrary | FM4, FM5, lost accountability |

Invariants I1–I7 do not guarantee *correctness* — they guarantee *not failing on
discipline*. A system satisfying all seven invariants can still contain false claims (wrong
source, wrong rule); but every false claim is *traceable, explainable, and fixable* without
destroying the trail.

> ⚠️ **Common misconception:** "A system that satisfies the invariants → the data is
> correct." Wrong. The invariants are a condition of *process discipline*, not of *content
> truth*. This distinction parallels conformance ≠ truth (Ch5) and acceptance ≠ truth (Ch6).

## 7.31 Mechanism KG example: full acquisition–integration cycle for RATE_OF_CHANGE

### Intuition

Assemble the whole pipeline into one concrete working case: three sources A, B, C brought
into the system, through eleven stages, ending in a queryable ledger state.

### Mechanism: the journey of the three streams

![RATE_OF_CHANGE full cycle: three sources through acquisition, meeting at integration, past the SHACL gate, into the ledger — ending with claim_vroc strengthened and current_1 in the queue.](figures/generated/ch07-acquisition-full.pdf)

**Stage 1 — Registration (§7.3):** `src:sourceA`, `src:sourceB`, `src:sourceC` are
registered with trust profiles.

**Stage 2 — Observation (§7.4):** three definitions become three fragments + three
observations: `ex:obsA_1` (derivative), `ex:obsB_1` (velocity), `ex:obsC_1`
(current-through-capacitor).

**Stage 3 — Extraction (§7.5):** `ex:recA_1`, `ex:recB_1`, `ex:recC_1` with three
Extraction Activities, extraction confidence recorded per record (§7.6).

**Stage 4 — Normalization (§7.7):** units and notation to canonical form.

**Stage 5 — Structuring (§7.8):** `ex:mechA_1`, `ex:mechB_1` under the mechanism schema.
For C, the normalized record still lacks the reference variable (extraction did not yet
capture "with respect to time"), so structuring yields `ex:appC_1` — a `DerivativeApplication`
missing `withRespectTo` (§7.15).

**Stage 6 — Identity (§7.9–7.10):** the blocking key groups the comparison pairs;
Fellegi–Sunter yields: (A, B) → "possible match" (same operation, different output), sent
to a human; (B, C) → "non-match" (differing input/output); (A, C) not in the same block.

**Stage 7 — Schema alignment (§7.11):** A: "derivative of f" ↔ `ex:derivativeOperation_1`;
B: "velocity"/"position" ↔ `ex:velocity_1`/`ex:position_1`; C: "current"/"voltage" → no
correspondence, suggests creating a new concept.

**Stage 8 — Deduplication (§7.13):** A and B are **not content duplicates** — the outputs
differ (`rateOfChange_1` versus `velocity_1`), the content hashes differ → keep two separate
records, each with its own provenance. Deduplication finds no duplicate pair among the three
streams; the real content-duplicate case (B with source D) is handled as in the §7.13
example.

**Stage 9 — SHACL gate (§7.15):** `ex:appC_1` missing `withRespectTo` → violation report
(`resultPath ex:withRespectTo`) → not valid → review queue. A, B valid.

**Stage 10 — Conflict + decision (§7.16–7.17):** (A, B) do not conflict — two different
statements both reducing to the mechanism `rateOfChange_1`: A establishes the operation
semantics (the derivative measures rate of change), B establishes a concrete application
(velocity = rate of change of position). Decision: accept both → **strengthen** the
existing claim `ex:claim_vroc` in the ledger (already Accepted from Chapter 6) with **two
independent evidence fragments** — `recB_1` directly, `recA_1` supporting via the operation
semantics. The two records are not merged into one claim (§7.13). C's decision is *defer*
(await review).

**Stage 11 — Ledger insertion (§7.18):** the claim `ex:claim_vroc` is strengthened, the
decision + rationale + pipelineVersion recorded in one transaction (§7.29). The projection
updates.

### Result in the ledger

```turtle
ex:claim_vroc  a               ex:Claim ;
               ex:content      ex:prop_velocity_rate_of_change ;
               ex:hasEvidence  ex:recB_1 , ex:recA_1 ;      # two independent sources
               ex:status       ex:Accepted ;
               ex:pipelineVersion  "acq-int-v7.3"^^xsd:string .
```

Projection query:

```sparql
SELECT ?claim ?status WHERE {
  ?claim ex:content ex:prop_velocity_rate_of_change ;
         ex:status ?status .
}
```

Returns: `ex:claim_vroc | Accepted` (strengthened). As for `ex:current_1` — the new concept
from C — *it is still a candidate*: not Accepted, not in the projection, awaiting a human
to confirm the mapping and the `withRespectTo`.

## 7.32 Failure drill: when everything goes wrong

### Intuition

The most beautiful theory must still face the broken case. This section walks a case in
which *many* failure modes happen at once — and shows how the invariants catch the errors
step by step.

### The drill

**Case:** the system acquires source E — a popular science article summarizing "derivatives,
velocity, and current in a capacitor".

**FM11 (chunking breaks meaning):** the chunk step cuts the current-through-capacitor
definition sentence in half → the fragment is missing its second half → extraction
`ex:recE_1` yields "current = C × (dV" — meaningless, missing "/dt)".

**FM9 (partial acquisition):** the pipeline reports completeness below threshold — the
article's second fragment (the velocity definition, copied from source B) was not scheduled
for processing.

**FM3 (lost recall):** the blocking key places `ex:recE_1` (current) in the same block as
`ex:mechC_1` — good — but *not* in the same block as `ex:mechB_1`, because "current" and
"velocity" differ in first letter. The pair (E, B) is never compared → the system does not
detect that E copied B.

**FM7 (lost idempotency):** because record E was created with a varying timestamp inside its
content hash (the hash was computed over a time field — wrong per the §7.14 rule), a re-run
creates record E′ "different" from E → two duplicate records in the buffer.

**FM8 (confusing validation/acceptance):** `ex:recE_1` is hand-edited to be "valid" and then
fed into integration without an accompanying validation report — violating I4.

**The invariants catch the errors:**

| Invariant | Detection | Response |
|-----------|-----------|----------|
| I3 (unique hash) | records E and E′ have the same content but different hashes → suspect FM2/FM7 | review the hash rule, find the time field being hashed |
| I4 (validation accompanies) | `ex:recE_1` has no report → blocked at the integration gate | send to the queue, not into the ledger |
| I1 (sufficient provenance) | the fragment was cut in half → ambiguous provenance → the claim is ineligible | fix the chunk, re-run |
| I6 (idempotent) | re-run after fixing the hash → creates no new copy | confirm idempotency recovered |
| I2 (version) | every new record carries the new version; old records unchanged | the whole sequence is auditable |

**Result:** the ledger is *not contaminated* — no claim from E enters the projection. The
buffer holds the erroneous records but all of them carry traces, versions, and reasons; the
system fixes each failure mode (chunk, blocking key, hash, gate), re-runs, and the re-run
follows the correct process. The lesson: **failure is normal; disciplined response is what
distinguishes a good system.**

### A secondary case: shape-valid, semantically wrong

There is a more dangerous failure — **fully valid structure but a wrong interpretation**.
Source F — an experimental document — records: "the average speed over the time interval Δt
is Δx/Δt = 5 m/s". This is a **finite difference** (average/finite rate), not an
instantaneous derivative. Extraction builds the candidate:

```turtle
ex:appF_1  a                ex:DerivativeApplication ;
           ex:hasOperation  ex:derivativeOperation_1 ;
           ex:differentiand ex:position_1 ;
           ex:withRespectTo ex:time_1 ;
           ex:hasOutput     ex:velocity_1 ;
           ex:value         5.0 .
```

This candidate **passes the SHACL gate**: right class, complete
operation/differentiand/withRespectTo/output, right types. The report says `conforms true`.
But the interpretation is wrong: Δx/Δt is a speed *over an interval*, whereas
`ex:derivativeOperation_1` is the *instantaneous* derivative — the scopes are misaligned
(§7.16). Three layers must be kept distinct:

1. **Structurally valid** — the SHACL shape matches (this layer passes).
2. **Semantically correct** — the statement matches the source's true meaning in the right
   scope (this layer fails: "instantaneous" ≠ "average").
3. **Epistemically accepted** — passed governance, with evidence and a reasoned decision
   (not reached until layer 2 is established).

The system must respond: keep `ex:appF_1` as a candidate, send it to the queue because of a
**scope conflict between the source claim (average over an interval) and the candidate
structure (instantaneous operation)**; not automatically Accepted despite `conforms true`. A
human reviewer may: (a) remap the operation to "finite difference" (a different operation),
(b) reject the candidate, or (c) record the scope explicitly as the interval Δt. This is
exactly why the SHACL gate is **never a truth gate** — it only filters shape-breakers, not
meaning-errors.

> ⚠️ **Common misconception:** "SHACL conforms true → the claim is accepted." Wrong. This
> secondary case is a counter-example: a candidate passes every shape yet is semantically
> wrong. `conforms true` says only *the shape is right*, not *the meaning is right*, and
> certainly not *it is accepted*.

> 🖊 **Self-check:** In the drill, if the system did *not* have I3, which failure mode
> would pass silently? What does I6 guard against after the hash is fixed?

## 7.33 Ingestion status queries and observability

### Intuition

Operators need to look *inside* the pipeline: which sources are registered, which fragments
are pending, which candidates are in the queue, how the last run went. Without this
capability, the pipeline is a black box — and every failure mode becomes "cause unknown".

### Mechanism

**Ingestion status queries:** the pipeline's artifacts are RDF data — so they can be queried
with SPARQL. Example: count candidates awaiting review:

```sparql
SELECT ?fragment (COUNT(?rec) AS ?pending) WHERE {
  ?rec a ex:ExtractedRecord ;
       ex:fromObservation/ ex:extractedFrom ?fragment .
  FILTER NOT EXISTS { ?rec ex:decision ?d . }
} GROUP BY ?fragment
```

**Observability:** each stage emits metrics — fragments processed, records extracted, mean
confidence, cases passing the SHACL gate, accept/reject/defer decision counts, queue
backlog. These metrics *are themselves pipeline data* and must be stored with version +
time — so "how did week 34's run go" can be answered.

The core lesson: observability is not "add a dashboard" — it is *the condition for the
§7.22 detection signals to exist at all*. A failure mode with no metric tracking it is a
failure mode that is never detected in time.

## 7.34 Scope and limitations: not solving inductive learning

### Intuition

This chapter teaches *bringing knowledge in* and *merging knowledge*. There is a larger
problem this chapter **deliberately does not solve**: how to infer new knowledge that is in
none of the sources.

### Mechanism

The first six chapters handled *deductive* inference: conclusions that follow logically
from premises (Ch4–5). Chapter 7 handles *acquisition and integration*: source knowledge is
brought into the system intact in the sense of "present in the source". **Inductive
learning** — deriving new laws/concepts from data, e.g. "from 1000 velocity records, infer
the general formula" — **is not solved in this chapter**.

Why deliberately excluded?

1. **Different epistemic nature.** Inductive knowledge is a *hypothesis* — different in
   nature from source knowledge. Blending the two breaks Chapter 6's governance semantics
   (a machine-learned hypothesis is not a sourced claim).
2. **Different norms.** Acquisition/integration have stable standards (R2RML, CSVW, Direct
   Mapping, Fellegi–Sunter). Inductive learning is a developing research area with no
   equivalent "baseline standard".
3. **Big enough for its own chapter.** If present, it deserves a standalone chapter — with
   its own semantics for "hypothesis", "confirmation", "refutation".

If machine learning appears in the book's system, its output is **CandidateKnowledge**
(Chapter 6 §6.16): a kind of candidate needing independent evidence, passing through the
gates like every other candidate — never automatically Accepted.

> ⚠️ **Common misconception:** "The acquisition pipeline has ML-based extraction → this
> chapter teaches machine learning." Wrong. Extraction may use ML tools, but the *product*
> is still a candidate record from a source — not a new inductive hypothesis. Conflating
> "ML tools in the pipeline" with "inductive learning" is a conceptual error.

## 7.35 Chapter summary

**Acquisition** brings source content into the system via: registration (Source Artifact,
§7.3) → observation by fragment (Source Fragment, §7.4) → extraction recording activity and
confidence (§7.5–7.6) → normalization (§7.7) → structuring per the target schema (§7.8).
The result: **candidate knowledge** — structured, traceable, not yet governed.

**Integration** merges the candidate streams via: identity resolution with candidate
generation / Fellegi–Sunter scoring (§7.9–7.10) → schema alignment and mapping (Direct
Mapping/R2RML, §7.11–7.12) → loss-preserving deduplication (§7.13) → idempotent ingestion
via content hash (§7.14) → the SHACL gate with conformance ≠ acceptance (§7.15) → conflict
detection per the Chapter 6 taxonomy (§7.16) → decision/merge outcome (§7.17) → ledger
first, projection from the ledger (§7.18) → lineage differs from evidence (§7.19) → human
in the loop via the queue (§7.20).

**Operational discipline:** multi-dimensional quality (§7.21); 13 failure modes — each with
a signal and a recovery (§7.22); echo sources not counted as independent evidence (§7.23);
pipeline versioning and safe reprocessing via idempotency (§7.24); batch or stream is a
source-characteristic choice with shared logic (§7.25); structured/semi-structured/text
sources — all paths converge on the same integration stages (§7.26); extraction schemas and
explicitly modeled unresolved values (§7.27); a versioned integration policy — integration
is a mapping decision with a semantics (§7.28); atomic transaction boundaries for ledger
writes (§7.29); seven invariants I1–I7 (§7.30). Inductive learning is not part of this
chapter (§7.34).

**Continuing Chapter 6:** the Chapter 6 claim ledger now has an *entry path*: this pipeline
is where new claims are born, assessed, and written to the ledger — with full provenance,
evidence, and governance. RATE_OF_CHANGE remains the through-line: `ex:claim_vroc` Accepted
in the ledger (Ch6) is strengthened by evidence from two independent sources A and B via
the pipeline (§7.31) — while source C's `ex:current_1` stays in the queue, awaiting
confirmation, not hastily identified with velocity.

## 7.36 Mechanism Knowledge System — Acquired capabilities

**BEFORE THIS CHAPTER** — the system had the epistemic layer (Ch6): claims with sources,
evidence, time, governance state. But every claim was *written into the ledger by hand*:
`claim_vroc` was composed in advance, treated as having provenance. There was no question
of "where does new knowledge come from?", "how do we handle two sources saying the same
thing under different schemas?", "does re-running the pipeline create duplicates?".

**AFTER THIS CHAPTER** — the system has an acquisition and integration pipeline standing
*in front of* the ledger:
- **Acquisition:** sources are registered (`Source Artifact`), content is observed by
  fragment (`Source Fragment`), extracted into candidate records with an `Extraction
  Activity` + extraction confidence (§7.3–7.6), normalized and structured per the target
  schema (§7.7–7.8).
- **Integration:** identity resolution by candidate generation + Fellegi–Sunter (§7.9–7.10);
  schema alignment and Direct Mapping/R2RML/CSVW mapping (§7.11–7.12); loss-preserving
  deduplication and idempotent ingestion via content hash (§7.13–7.14); the SHACL gate with
  conformance ≠ acceptance (§7.15); conflicts per the Ch6 taxonomy and reasoned integration
  decisions (§7.16–7.17).
- **Ledger first:** everything enters the ledger through a recorded decision; the projection
  is built from the ledger; lineage traces back to the fragment, distinct from evidence
  (§7.18–7.19); humans review via the queue (§7.20).
- **Discipline:** multi-dimensional quality; 13 failure modes with signals; echo sources not
  counted as independent evidence; pipeline versioning; transaction boundaries; seven
  invariants I1–I7 (§7.21–7.30).

**CONCRETE RATE_OF_CHANGE EXAMPLE** — three sources (Calculus A, Mechanics B, Electronics C)
all say "rate of change with respect to time". After the pipeline: source A (the derivative
measures rate of change) and source B (velocity = rate of change of position) are **two
different statements** — different content, different hash, different provenance — but both
reduce to the mechanism `rateOfChange_1` after schema alignment. Both are kept separate and
together strengthen `ex:claim_vroc` in the ledger (§7.31) — not merged into one claim
(§7.13). Source C (`current = C·dV/dt`) is **not** identified with velocity: identity says
"non-match", schema alignment finds no correspondence, the SHACL gate catches the missing
`withRespectTo` → `ex:current_1` sits in the review queue. The answer to §7.0: "do the three
sources say the same concept?" — turns out to be *not quite*: A and B share one mechanism yet
remain two separate statements; C does not belong to that mechanism at all. The structural
similarity between the two applications (velocity and current-through-a-capacitor) is a
**hint** — it may lead to a candidate hypothesis (CandidateMechanismHypothesis) about a
shared abstract mechanism, but establishing that abstract identity belongs to inductive
learning (Chapter 8), not to this chapter's conclusions. Without the pipeline, the system
would have hastily merged all three and corrupted the mechanism ontology.

**WHAT REMAINS UNSOLVED** — the pipeline assumes *sources already exist, content already
complete*. Three problems remain open: (1) **inductive learning** — inferring new knowledge
not present in a source (not part of this chapter, §7.34); (2) **automatic source
selection** — when there are thousands of sources, choosing which are worth acquiring is
its own problem; (3) **deep semantic extraction** — capturing the precise meaning of natural
text is still a developing area, not a stage with a baseline standard. Chapter 8 (if
present) opens the next rung: using the integrated graph to *deduce and query knowledge at
scale* — where the claims already written to the ledger become premises.

## Terms encountered in this chapter

| Term | Short meaning | More in |
|------|---------------|---------|
| Acquisition | Bring source content into the system as candidate knowledge | §7.2 |
| Integration | Merge, reconcile, confirm before writing to the ledger | §7.2 |
| Source Artifact | The registration record of a source, with IRI and metadata | §7.3 |
| Source Fragment | An addressable sub-part of a source | §7.4 |
| Observation | Raw data collected from a fragment, before interpretation | §7.4 |
| Extraction / Extraction Activity | Extract a candidate record + a PROV Activity recording the execution | §7.5 |
| Extraction Confidence | Confidence *of the extraction*, not of the content | §7.6 |
| Normalization | Bring values to canonical form for comparison; may lose information | §7.7 |
| Structuring | Normalized record → RDF triples per the target schema | §7.8 |
| Entity Resolution | The process of deciding "are two records one entity?" | §7.9 |
| Candidate Generation / Blocking | Generate pairs worth examining via a blocking key (recall-biased) | §7.9 |
| Record Linkage (Fellegi–Sunter) | Compare the γ vector, m/u, two thresholds: match / review / non-match | §7.10 |
| Schema Alignment | Find semantic correspondences between schema elements | §7.11 |
| Direct Mapping / R2RML / CSVW | Default mapping / custom mapping / tabular→RDF (W3C standards) | §7.12 |
| Deduplication | Recognize content duplicates and reconcile, without deleting | §7.13 |
| Idempotent Ingestion | Re-running yields the same ledger state | §7.14 |
| Content Hash | Fingerprint of normalized content; dedup/idempotency key | §7.14 |
| SHACL gate | Shape-check gate; conformance ≠ acceptance | §7.15 |
| Conflict Detection | Find pairs that cannot both be true in the same context | §7.16 |
| Merge Outcome | Insert / strengthen / supersede / merge — preserving both sides | §7.17 |
| Claim Ledger First | The ledger is the single source of truth; the projection is built from it | §7.18 |
| Lineage vs Evidence | "Where did it come from?" differs from "why believe it?" | §7.19 |
| Review Queue | The review lane: possible match, SHACL fail, conflict | §7.20 |
| Data Quality Dimensions | 6 dimensions; there is no single "quality" number | §7.21 |
| Failure Modes | 13 failure modes, each with a signal + recovery | §7.22 |
| Echo Source | A derived source; not counted as independent evidence | §7.23 |
| Pipeline Versioning | Every output-shaping component is versioned | §7.24 |
| Batch vs Streaming | Two processing rhythms; shared logic, different rhythm | §7.25 |
| Chunking / Retrieval Bound | Split a document into fragments; assert only what a fragment entails | §7.26 |
| Extraction Schema / Unresolved Value | Declare the record structure; model "not yet known" explicitly | §7.27 |
| Integration Policy | A versioned rule set governing integration decisions | §7.28 |
| Transaction Boundary | Atomic ledger write: all or nothing | §7.29 |
| Invariants I1–I7 | Seven invariants protecting traceability, no-overwrite, idempotency | §7.30 |

## Further reading

- R2RML: RDB to RDF Mapping Language [@w3c-r2rml]
- A Direct Mapping of Relational Data to RDF [@w3c-direct-mapping]
- Model for Tabular Data and Metadata on the Web (CSVW) [@w3c-tabular-data-model]
- A Theory for Record Linkage (Fellegi & Sunter) [@fellegi-sunter-1969]
- A Survey of Approaches to Automatic Schema Matching (Rahm & Bernstein) [@rahm-bernstein-2001]
- Data Integration: A Theoretical Perspective (Lenzerini) [@lenzerini-2002]
- Shapes Constraint Language (SHACL) [@w3c-shacl]
- PROV-O: The PROV Ontology [@prov-o]
- PROV Data Model (PROV-DM) [@prov-dm]
- Knowledge Graphs (Hogan et al.), Creation and Enrichment [@hogan-creation-enrichment]
