# Chapter 9 — Retrieval, Question Answering, and GraphRAG

> **Chapter orientation**
>
> **Central question:** When a user poses a question to a knowledge system — "Why is
> velocity a rate of change?", "What mechanism do velocity and electric current share?",
> "What was the definition of 'current' in 2020?", "Who ever proposed the opposite?" — how
> does the system know **what to retrieve, from where, in what order**, and then **generate
> an answer** such that every claim traces back to evidence and no claim is conjured from a
> gap?
>
> **Why it matters:** The previous eight chapters built a complete knowledge system: the
> graph (Ch1–2), identity (Ch3), semantics (Ch4), deduction (Ch5), the epistemic layer with
> the Claim Ledger (Ch6), source acquisition (Ch7), and inductive learning (Ch8). But a
> knowledge system with no **question-answering window** is like a library with no
> librarian: the knowledge is there, yet no one can find it. Chapter 9 opens the final rung
> of the journey: **retrieval** — fetching the right evidence from the right place — and
> **question answering** — turning evidence into a grounded answer. This is also where the
> system meets real users, and where every small defect in the layers below (wrong identity,
> a stale claim, a lagging index) is exposed as a wrong answer.
>
> **You will understand:**
>
> - The system's new I/O: from a natural-language question to a grounded, cited answer
> - Question interpretation and intent classification: factual, structural, comparative,
>   explanatory, provenance, temporal, contradiction, discovery, multi-hop
> - Query entity linking; intent ≠ identity; query decomposition; retrieval plan
> - Retrieval unit; **index ≠ KG**; symbolic graph retrieval (SPARQL)
> - Multi-hop traversal, depth bounds, relation-aware traversal, k-hop neighborhood
> - Lexical retrieval (BM25), dense retrieval (Dual Encoder), query vector ≠ meaning
> - Hybrid retrieval and RRF rank fusion; graph-first vs text-first
> - Epistemology-aware retrieval: Canonical View vs Claim Ledger, governance, time (many
>   clocks), provenance, contradiction, evidence diversity
> - **top_k as an epistemic bound**; precision/recall/P@K/R@K/MRR/nDCG; reranking
> - Context assembly and compression; lost in the middle; graph serialization
> - **Evidence Packet** (BOOK-DEFINED) — the interface between retrieval and generation
> - Answer generation, answer claims, grounded answer, citation, citation completeness
> - Faithfulness ≠ correctness; the 2×2 table; abstention
> - Unknown ≠ not found; retrieval error ≠ missing knowledge
> - Query planning, static vs agentic retrieval, stopping conditions, query drift
> - Confirmation bias; hypothesis-testing retrieval; local vs global questions
> - GraphRAG as **an architecture family** (not one canonical algorithm); the KGQA vs RAG
>   vs GraphRAG decision table
> - A path is an explanation but not a proof; path explosion
> - Community/hierarchical retrieval; cache and index consistency; retrieval provenance
> - **A QA answer ≠ ingested knowledge**; score semantics; multi-signal ranking
> - Seven-layer retrieval evaluation; gold evidence; QA benchmarks; adversarial tests,
>   distractors, contradiction, time
> - The 15-step full-stack work case on RATE_OF_CHANGE; the failure case; hallucination
>   taxonomy; self-check; claim–evidence alignment
> - Graph reasoning vs LLM reasoning; what GraphRAG does not guarantee; when NOT to use RAG
> - The Query Execution Router (BOOK-DEFINED); 34 misconceptions; 8 self-check checkpoints;
>   EXP-9-1..EXP-9-9 (deferred to v0.1); the depth audit; Q01–Q56; the end-of-chapter
>   competency ladder
>
> **Prerequisites:**
> - Chapters 1–2 (graphs, nodes, edges, types, paths)
> - Chapter 3 (identity — entity ≠ embedding)
> - Chapter 4 (semantics, OWA, closed-world)
> - Chapter 5 (deduction, rules, SPARQL, SHACL)
> - Chapter 6 (epistemic model, Claim, Claim Ledger, Evidence, Assessment, provenance,
>   multiple clocks)
> - Chapter 7 (source acquisition, integration, governance, canonical view)
> - Chapter 8 (inductive learning, mechanism hypotheses, hybrid pipeline, prediction ≠
>   entailment)
>
> **Concept map:**
>
> Question interpretation → Intent (9 kinds) → Entity linking → Decomposition → Retrieval
> plan → Retrieval unit → Index ≠ KG → Graph (SPARQL, multi-hop, k-hop, subgraph) → Text
> (BM25, dense, hybrid, RRF) → Epistemology (Canonical vs Ledger, governance, time,
> provenance, contradiction) → top_k bound → Measurement → Reranking → Context assembly →
> Evidence Packet → Answer generation → Grounding/citation/faithfulness → Abstention →
> Dynamic retrieval (agentic, stopping, drift, bias) → GraphRAG architecture family →
> Subgraph/community → Cache → Provenance → Seven-layer evaluation → Benchmark → Work case
> → Failure case → Boundaries → Router → Misconceptions → Competency ladder
>
> **Central chain of distinctions** (threaded through the chapter, repeated many times):
> retrieved ≠ evidence; a retrieval score ≠ confidence; grounded ≠ correct; faithful ≠
> correct; a path ≠ a proof; a summary ≠ a source; not found ≠ does not exist; a QA answer ≠
> accepted knowledge.

## 9.1 A New I/O: From Question to Answer

The previous eight chapters taught the system how to **build and maintain knowledge**:
identify entities, attach semantics, deduce consequences, govern claims in the Ledger,
acquire from sources, and learn hypotheses from the graph. But none of those rungs describes
how a user **gets knowledge out** when they need it. Chapter 9 adds two new inputs–outputs
(I/O) to the whole system:

- **New input: a natural-language question** — "Why is velocity considered a rate of change?"
- **New output: a grounded, cited, provenance-bearing answer** — not merely correct in
  content, but able to *explain why the system believes it*.

This I/O is not a simple lookup. It is a **retrieval–reasoning–synthesis pipeline** with
three distinct layers:

1. **Question-understanding layer:** a natural-language question → a structured intent + the
   mentioned entities (possibly ambiguous) → a retrieval plan.
2. **Retrieval layer:** run the plan over the knowledge sources — the structural graph, the
   Claim Ledger, source text, the vector index — then gather the results into an **Evidence
   Packet** (BOOK-DEFINED, §9.36).
3. **Answer-generation layer:** a language model (LLM) reads the Evidence Packet, synthesizes
   an answer, splits it into sub-claims, and attaches each claim to its evidence (citation).

The architectural crux: the LLM — however powerful — **reasons only over the knowledge placed
into its context window**, not over the entire knowledge system. This sounds obvious, yet it
is the root of most failures in this chapter:

> **Context window ≠ Knowledge.** The system may hold every correct claim, every correct
> structural path — but if the retrieval layer does not place the right pieces into the
> window, the answer is still wrong.

An example that illustrates the concept immediately: our knowledge system holds three
applications of the `RATE_OF_CHANGE` mechanism — `VelocityDerivativeApplication`,
`CurrentDerivativeApplication`, `PopulationDerivativeApplication`. If a user asks "What
mechanism do velocity and electric current share?", an LLM given no context may "know"
physics, but it **does not know** that our system has connected those two concepts through
the same mechanism — that is *internal* knowledge, existing only in the graph. If the
retrieval layer sends only a passage about electric current, the answer will be missing half
the structure. Conversely, only when it sends enough mechanism structure plus the source
passage does the LLM have a basis to synthesize a correct answer.

One methodological warning before we proceed, in the spirit of the whole book: **the pipeline
completing does not mean the answer is correct.** Successful retrieval, fluent synthesis,
complete citation — all of these are *procedural* properties. Correctness with respect to the
world is a *different* property, assessable only by users and external alignment processes.
This chapter teaches how to make the procedure **honest about its own certainty** — stating
what is supported, what is inferred, what is unknown — not how to make the procedure
incapable of being wrong.

## 9.2 The Big Picture: Retrieval Is Where Every Rung Meets

Before the details, place this chapter within the nine-chapter architecture (Figure 9.1).
Each earlier rung contributes a distinct capability to the retrieval layer:

- **Ch1–2** give structure: nodes, edges, types, paths — graph retrieval moves over them.
- **Ch3** gives identity: `sameAs`, fingerprints, identity — query entity linking relies on
  it to decide "who is this mention".
- **Ch4** gives semantics: classes, properties, OWA — retrieval understands what "the parent
  class of ElectricCurrent" means.
- **Ch5** gives deduction: SPARQL/entailment — symbolic retrieval executes over it.
- **Ch6** gives epistemology: Claim, Claim Ledger, Evidence, Assessment, PROV — provenance-,
  time-, and contradiction-aware retrieval live off these concepts.
- **Ch7** gives acquisition and governance: canonical view, governance state — retrieval
  distinguishes "what is currently accepted" from "what was once proposed".
- **Ch8** gives induction: mechanism hypotheses, hybrid pipeline — hypothesis-testing
  retrieval uses these concepts.

![The full nine-chapter architecture: graph → identity → semantics → deduction → epistemology → acquisition → inductive learning → retrieval and question answering. Chapter 9 is the current rung: the window that communicates with the user.](figures/generated/ch09-full-stack.pdf)

Ch9's position in the architecture also fixes its **scope of commitment**: Ch9 adds no new
rule to the ontology and no new claim to the Ledger. It *consumes* all those rungs to serve a
single purpose — answering a question honestly with the knowledge that exists. This is why
the chapter's boundaries matter so much: a system that answers wrongly "because the system
says so" is more dangerous than one that does not answer at all.

---

# Part A — Understanding the Question and the Retrieval Plan

## 9.3 Question Interpretation

The pipeline's first step: turn a natural-language question into a **structured intent** —
what the question is asking, about which entities, and what kind of evidence will be
accepted. In classical information retrieval, the standard textbook distinguishes three
concepts [@manning-ir-2008]:

- **Information need** — what the user *actually wants to know*;
- **Query** — the language expression they type;
- **Document** — the unit the system can find.

These three do not coincide. A user typing "current" may want "what is electric current" (a
concept definition), "what is the current value" (a measured value), or "what is the current
version of the definition" (a governance state). For this reason the chapter does not call the
first step "question analysis" but **interpretation**: a fallible inference that must always
be recorded and can be revised.

**Formal meaning:** question interpretation maps a natural-language question to a structure
comprising (a) a list of entity mentions (with ambiguity), (b) an intent type, (c) constraints
(time, governance state, domain), (d) the required evidence type. The interpretation result is
*an analysis*, not an assertion about the world.

**In this book:** "Question interpretation: turn a natural-language question into a structured
intent — entities, question type, evidence required. The result can be wrong and must be
recorded."

An example in our continuous-mechanism domain:

| Question | Structured intent |
|---|---|
| "What is velocity?" | FACTUAL — entity `Velocity`, requires the accepted definition |
| "How are velocity and electric current alike?" | COMPARATIVE — two entities, requires shared structure |
| "Why is velocity a rate of change?" | EXPLANATORY — entity + property, requires a structural path + evidence |
| "What is the 2020 definition of current?" | TEMPORAL — entity + time point |
| "Who ever objected to this definition?" | CONTRADICTION/PROVENANCE — requires the Ledger, not the canonical view |
| "Is there any mechanism other than RATE_OF_CHANGE governing velocity?" | DISCOVERY — requires open-ended search |

**Dangerous simplification:** treating the interpretation result as self-evident truth and
moving straight to retrieval without re-checking; or conflating "the question typed" with
"the information need".

**MUST NOT infer:**
- Do not assert that the interpreted intent is the user's real intent.
- Do not skip recording which interpretation was chosen (the interpretation is provenance
  data for everything downstream).
- Do not present the products of interpretation (intent, entity list) as accepted knowledge —
  they are an analysis, not an assertion.

## 9.4 Intent Classification: Nine Question Types

To choose the right retrieval plan, the system classifies the question by **intent type**.
Each type has its own evidence requirements and retrieval sources. Table 9.1 is the chapter's
classification (BOOK-DEFINED, built on the query taxonomy in the KGQA survey
[@chakraborty-kgqa-2019] and the GraphRAG query modes [@edge-graphrag-2024]):

| # | Intent | Typical question | Preferred retrieval source | Minimum evidence |
|---|---|---|---|---|
| 1 | FACTUAL | "What is electric current?" | Canonical View, accepted definition | Accepted claim + source passage |
| 2 | STRUCTURAL | "Which mechanism is Velocity an application of?" | Structural graph (instanceOf/mechanism) | Structural path |
| 3 | COMPARATIVE | "How are velocity and current alike?" | Graph + parallel structural paths | Shared structure (common mechanism) |
| 4 | EXPLANATORY | "Why is velocity a rate of change?" | Graph + Ledger + source text | Mechanism path + accepted claim + source passage |
| 5 | PROVENANCE | "Why does the system believe this definition?" | PROV chain: Claim→Evidence→SourceFragment→Source | Full provenance chain |
| 6 | TEMPORAL | "The 2020 definition of current?" | Ledger by valid/publication time | Time-stamped claim |
| 7 | CONTRADICTION | "Who objected?" / "Is there a conflict?" | Ledger: competing claims + scope | ≥2 opposing claims with scope |
| 8 | DISCOVERY | "Any other mechanism?" | Open search (lexical/dense + graph) | Diverse candidate set, with bounds |
| 9 | MULTI-HOP | "Why does population growth share a mechanism with current?" | Combination: structure + similarity + evidence | Chain of dependent sub-steps |

The nine rows (eight types plus one composite) are not a "single correct" taxonomy — it is
**the book's policy**, enough to illustrate the principle: *the intent type determines the
kind of evidence to retrieve, and the kind of evidence determines which data source is
allowed to answer.*

**MUST NOT infer:**
- Do not use one universal retrieval recipe for every question type.
- Do not assert that intent is fully determined by the entities present ("asking about
  velocity" does not by itself reveal whether the question is about a definition, a history,
  or a dispute).
- Do not let an intent label silently change the epistemic status of the answer (e.g.
  answering a historical question with the current definition).

## 9.5 Query Entity Linking

Questions contain mentions — "current", "velocity", "rate of change". Query entity linking
maps each mention to candidate **entities** in the graph. This is a core sub-problem of KGQA
[@chakraborty-kgqa-2019], and it inherits Ch3's semantics of identity directly: identity is a
governed decision, not a string comparison.

A mention may have several candidates for different reasons:

- **Homonym:** "current" → `ElectricCurrent` (the concept) or `CurrentValue` (the present
  value)?
- **Domain polysemy:** "growth" → `PopulationGrowth` (a population model) or `EconomicGrowth`
  (economics)?
- **Syntactic ambiguity:** is "current" an adjective ("present") or a noun ("electric
  current")?

The standard procedure has three steps, following the typical KGQA system model
[@chakraborty-kgqa-2019]:

1. **Candidate generation:** from the mention string plus its variants, find entities whose
   label/synonym matches — via a string index, via embeddings, via entities connected in the
   question's context.
2. **Contextual scoring:** score each candidate by how well it fits the context — the other
   entities in the question, class, relations, domain. "Electric current" appearing alongside
   "resistance" tilts toward `ElectricCurrent`.
3. **Decision:** pick a candidate or **declare ambiguity** — knowing you are unsure matters
   more than picking right.

**Formal meaning:** query entity linking = a mapping mention → (candidate set, score
distribution, decision/ambiguity). Selecting the highest-scoring candidate is *not* a
mandatory final step; recording ambiguity is a valid output.

**In this book:** "Query entity linking: mention → candidates → contextual scoring → pick or
report ambiguity. Never automatically take the nearest vector as the answer."

Example: "current" in the question "Why does current change when resistance changes?" — the
candidate `ElectricCurrent` wins because it shares the context `ElectricalResistance` (the
`affects`/`dependsOn` relation). But "The definition of 'current' in the 2020 book?" can still
be ambiguous between the concept entity and the version entity — the system should ask back,
or answer with both scopes, rather than pick arbitrarily.

**Dangerous simplification:** choosing the nearest-vector entity without assessing context;
assuming one mention = one entity; hiding ambiguity.

**MUST NOT infer:**
- Do not assert that the highest-scoring candidate is correct.
- Do not reuse Ch3's *entity* identity as if it were *query* linking without adapting it to
  the question's context (Ch3 merges identity across time; a question needs to distinguish
  temporary scopes).
- Do not discard ambiguity — an ambiguous mention must be recorded, not concealed.

## 9.6 Intent ≠ Identity: Two Independent Axes of Ambiguity

This is a semantic boundary the chapter stresses because it is violated often:

> **"Who is being mentioned" (entity identity) and "what is being asked" (query intent) are
> two independent axes. Both can be ambiguous, and ambiguity on one axis does not entail
> ambiguity on the other.**

Worked example: the question "How does electric current change?"

- Entity axis: `ElectricCurrent` — clear (electronics, not economics).
- Intent axis: seriously ambiguous. "How does it change" could want:
  - the mechanism: "current changes as the *derivative of charge with respect to time*"
    (STRUCTURAL);
  - the cause: "current changes *when resistance changes*" (EXPLANATORY);
  - the law: "current is inversely proportional to resistance" (FACTUAL);
  - the history: "how the definition of current changed across versions" (TEMPORAL).

Conversely: "What is velocity?" — the intent axis is clear (a definition), but the entity axis
can be ambiguous if the graph holds both `Velocity` (the concept) and `InstantaneousVelocity`
(a variant).

Design consequence: **question interpretation must produce two separate records** — an entity
list (with ambiguity) and an intent label (with ambiguity). If the system collapses these two
axes into one undifferentiated "understand the question" step, it cannot correctly report
which kind of uncertainty it holds.

**MUST NOT infer:**
- Do not merge entity identity and intent classification into one step without reason.
- Do not assert that the two axes are always ambiguous together.
- Do not let having resolved the entity imply that the intent is understood.

## 9.7 Query Decomposition

A compound question often must be split into sub-questions with explicit dependencies. The
chapter's central example — the question that motivates everything that follows:

> **Q0:** "Why are velocity and electric current regarded as the same RATE_OF_CHANGE
> mechanism, and what evidence supports that?"

One valid decomposition (among several):

- **Q1 (STRUCTURAL):** Which mechanism is `VelocityDerivativeApplication` an application of?
  → `RATE_OF_CHANGE`, via the `instanceOf` relation (or mechanism attribution).
- **Q2 (STRUCTURAL):** Which mechanism is `CurrentDerivativeApplication` an application of?
  → the same `RATE_OF_CHANGE`.
- **Q3 (STRUCTURAL/COMPARATIVE):** Do the two applications play the same role? → same
  `operation=DerivativeOperation`, `withRespectTo=Time`, `produces` a quantity.
- **Q4 (FACTUAL/PROVENANCE):** Which accepted claim asserts this correspondence, from which
  source? → Claim + Evidence + SourceFragment.
- **Q5 (CONTRADICTION):** Does any claim oppose or limit this correspondence? → query the
  Ledger.
- **Q6 (SYNTHESIS):** Combine Q1–Q5 into an explanatory answer.

**Formal meaning:** query decomposition = splitting a complex question into sub-questions + a
dependency graph (Q3 needs the results of Q1, Q2; Q6 needs all of them). A decomposition is a
*plan*, not a truth computation — a different decomposition may be no less correct.

**In this book:** "Query decomposition: complex question → sub-questions + dependencies →
retrieval plan. Not every question needs decomposition."

Two important cautions:

1. **Not every question needs decomposition.** "What is velocity?" — a single query. Reckless
   decomposition creates cost, noise, and more places for error to enter.
2. **Sub-answers do not automatically sum to a correct answer.** Each sub-question may be
   correct in isolation, but stitching them together (especially the Q6 synthesis step) is a
   separate inference that must be re-checked — this is exactly where "correct parts, wrong
   whole" arises.

**MUST NOT infer:**
- Do not assert that the decomposition result is the only correct reading.
- Do not assume the sub-questions' answers sum to a correct answer.

## 9.8 Retrieval Plan and the Query Router

From intent + entity list + decomposition, the system builds a **retrieval plan**: an ordered
sequence of concrete retrieval operations with bounds and stopping conditions. A plan for
question Q0 might be:

```
1. resolveEntity("Velocity") → Velocity
2. graphQuery(instanceOf, Velocity) → RATE_OF_CHANGE          (Q1)
3. resolveEntity("ElectricCurrent") → ElectricCurrent
4. graphQuery(instanceOf, ElectricCurrent) → RATE_OF_CHANGE   (Q2)
5. graphQuery(roleObjects, VelocityDerivativeApplication)     (Q3)
6. ledgerQuery(Accepted claims mentioning the RATE_OF_CHANGE correspondence)  (Q4)
7. ledgerQuery(Contested/Superseded claims about the correspondence)   (Q5)
8. sourcePassageRetrieval(BM25+dense for "velocity ... derivative ...") (text evidence)
9. assemble EvidencePacket; stop (stopping condition: enough evidence cells)
```

The **Query Execution Router** (BOOK-DEFINED) is the component that decides the *execution
path* from the understood question:

| Condition | Execution path |
|---|---|
| Entity + property resolved, schema known | **Exact graph query** (SPARQL) |
| Consequence deduction needed | **Symbolic inference** (Ch5) |
| Ambiguous entity / open question / definition | **Text retrieval** (BM25 + dense) |
| Structure + text evidence needed | **GraphRAG/hybrid** |
| Historical/contradiction question | **Ledger query** (ledger retrieval) |

The router's principle: **the cheapest path that can answer correctly wins.** Do not use a
generative LLM for a query that SPARQL answers exactly [@chakraborty-kgqa-2019]: a structural
query already is the answer; generating text only adds a chance of fabrication.

**Formal meaning:** a retrieval plan = an ordered set (retrieval operation, parameters,
bounds, stopping condition); the router = a decision function from (intent, resolution,
schema) → execution path.

**MUST NOT infer:**
- Do not assert that the plan guarantees completeness (the plan finishing ≠ enough evidence
  gathered).
- Do not assert the plan is correct merely because it ran to the end.
- Do not let the router pick the most expensive path when an exact one suffices.

---

# Part B — Retrieval Units and Graph Retrieval

## 9.9 Retrieval Unit

When we say "retrieve", we must state what **unit** the system returns. In classical text
retrieval the unit is a document or a passage [@manning-ir-2008]. In a knowledge system there
are many unit types, each with its own strength and limitation:

| Unit | Example | Strong for | Weak for |
|---|---|---|---|
| Entity | `ElectricCurrent` | identification, anchoring the question | compound answers |
| Triple | `CurrentDerivativeApplication instanceOf RATE_OF_CHANGE` | a single fact | context |
| Claim | `#C471: "Current = RATE_OF_CHANGE(DerivativeOperation, ...)"` | epistemology (status, assessment) | raw evidence |
| Evidence | a Ch6 record linking a claim to a source passage | source tracing | self-standing content |
| Source passage | a paragraph in a physics book | real content, citable | structure |
| Path | `Velocity ->produces-> DerivativeApplication ->operation-> DerivativeOperation` | structural explanation | proof |
| Subgraph | the three applications + the shared mechanism | coherent context | size |
| Community summary | "the three applications share a role..." | compactness | compresses away evidence |
| Canonical answer object | a governed answer record | reuse | staleness |

**The crux:** an *explanatory* answer usually needs several unit types working together. An
accepted claim (an epistemic unit) is not enough without a source passage (a textual unit) to
cite; a path (a structural unit) is not enough without a claim (an epistemic unit) to know
whether that path is accepted.

**Formal meaning:** a retrieval unit = the kind of object a retrieval step returns; the choice
of unit determines recall/precision, contextual coherence, and provenance-traceability.

**MUST NOT infer:**
- Do not assert that one unit type suffices for every question type.
- Do not equate "retrieved a unit" with "have enough evidence".

## 9.10 Retrieval Index ≠ Knowledge Graph

One of the most dangerous architectural confusions in RAG systems is treating the **retrieval
index** as if it were knowledge itself. Distinguish three different entities:

1. **Knowledge Graph (KG)** — the source of structural truth: nodes, edges, claims,
   assessments, governance. This is what was built and maintained from Ch2 to Ch8.
2. **Claim Ledger** — an immutable store of provenance-bearing, status-bearing claims.
3. **Search/vector index** — a *derived* access structure: tokenized strings, embedding
   vectors, labels, precomputed neighborhoods built for fast retrieval.

In classical information retrieval, the inverted index was already clearly defined as an
*access structure* over a document collection, not the documents' content [@manning-ir-2008].
The principle extends intact: **an index is a deliberate copy made for fast lookup; it can lag
behind the KG and the Ledger.**

Why does this matter in practice? Consider a scenario: a claim is moved to `Superseded` in the
Ledger at 09:00; the vector index is only rebuilt at 10:00. During that window, a query "What
is the definition of current?" can return the old claim's passage with a high score — and the
LLM, faithful to its context, will answer with the superseded definition. **The technique runs
without error; the knowledge is still stale.** This is an *index consistency* error, not a
fault of the generative model.

**Formal meaning:** index ≠ KG: an index is a derived relation (KG or Ledger → retrieval
representation) that may be out of sync; index state does not entail KG state.

**In this book:** "A retrieval index is an access structure derived from the KG — not the KG,
not the Ledger; it can lag."

**MUST NOT infer:**
- Do not assert that index state equals graph state.
- Do not assert that a passage found in the index is accepted knowledge.
- Do not ignore index freshness when assessing an answer.

## 9.11 Symbolic Graph Retrieval

When the schema, entities, and required relations are known for certain, the strongest
retrieval path is an **exact graph query** — SPARQL [@w3c-sparql11-query]
[@w3c-sparql11-overview]. This is symbolic retrieval: results are exact in the sense of
*structural pattern match*, not in the sense of *approximate ranking*.

Example: the structural question "Which mechanism is Velocity an application of, and what are
its roles?"

```sparql
SELECT ?app ?role ?obj WHERE {
  VALUES ?app { velocity:VelocityDerivativeApplication }
  ?app velocity:instanceOf ?mech ;
       velocity:operation ?op ;
       velocity:differentiand ?diff ;
       velocity:produces ?res .
}
```

Result: `?mech = rate:RATE_OF_CHANGE`, `?op = DerivativeOperation`, `?diff = Position`,
`?res = Velocity` — a complete structural block, ready to drop into the Evidence Packet.

The strengths of symbolic retrieval [@chakraborty-kgqa-2019]:

- **High precision:** if the pattern matches, the result is *correct by graph semantics* — no
  probability involved.
- **Auditable:** anyone can re-read the query and the result.
- **Natural provenance:** every returned triple carries Ch6 provenance.

The limits:

- **Vocabulary-fragile:** it finds nothing if the data uses different words (unless a lexical
  mapping exists — Ch3).
- **No "approximate":** it cannot find "something like a derivative" if no mapping exists yet.
- **Reflects the graph, not the world:** if the KG is wrong, the SPARQL result is wrong yet
  still "exact by pattern".

**MUST NOT infer:**
- Do not assert that a symbolic graph result is semantically complete.
- Do not assert that SPARQL handles paraphrase/unmapped vocabulary.
- Do not treat a query result as automatically true of the world — it reflects what the KG
  asserts (and the KG may be wrong or stale).

## 9.12 Graph Traversal / Multi-hop Retrieval

When an answer requires *connecting entities across several steps*, the system traverses the
graph edge by edge. Consider question Q3 from §9.7: "Do the two applications play the same
role?" — multi-hop retrieval walks from `VelocityDerivativeApplication` via `operation` to
`DerivativeOperation`, then from `CurrentDerivativeApplication` via `operation` to the same
node — discovering the shared structure (Figure 9.2).

![Multi-hop retrieval: two applications both pointing to the RATE_OF_CHANGE mechanism with the same roles (operation=DerivativeOperation, withRespectTo=Time). The path expresses a structural correspondence — not a proof.](figures/generated/ch09-multihop-subgraph.pdf)

From a KGQA standpoint, this is a "multi-hop path" answer [@chakraborty-kgqa-2019]: the answer
lies at the far end of a chain of relations. But this chapter stresses an epistemic boundary:

> **A path existing ≠ the conclusion being proven.** A path shows the graph *connects* the
> concepts that way — it does not prove the relations along the path are true of the world,
> nor that no other path exists (especially a path that *refutes*).

Example: the path `Velocity ->produces-> VelocityDerivativeApplication ->instanceOf->
RATE_OF_CHANGE` is a structural fact. But if the Ledger holds a claim objecting that the
derivative is only *a model*, not the essence of velocity, then the path above is one-sided.
Honest multi-hop retrieval must record both sides — this is the bridge to contradiction-aware
retrieval in §9.27.

**Formal meaning:** multi-hop retrieval = stepping along edges over many hops, possibly with
node-type/edge-type/direction constraints, to find a set of paths or a subgraph connecting the
entities mentioned in the question.

**MUST NOT infer:**
- Do not present a traversal path as a logical entailment.
- Do not assert that a path's existence implies the correctness of the relations along it.

## 9.13 Path Bounds: Depth and Traversal Scope

Knowledge graphs are never small. From `CurrentDerivativeApplication`, one step reaches
`ElectricCurrent`, `RATE_OF_CHANGE`, `Time`, `DerivativeOperation`; two steps reach parent
classes, sources, authors, assessments, related claims, similar applications... By step three,
the node count can grow exponentially. Hence **every traversal must have explicit bounds**:

- **Max depth:** how many hops;
- **Allowed edge types:** `operation`, `instanceOf`, `produces`... or every edge;
- **Direction:** forward, backward, or both;
- **Node types:** which nodes may enter the result;
- **Branching limit:** how many outgoing edges to consider per node.

These bounds are not a harmless technical detail — they are **an implicit epistemic bound**,
of the same nature as top_k (§9.29):

> **Max depth decides which structural pieces get seen. Whatever the system does not traverse
> to, the system cannot answer about — even if it exists in the graph.**

The symmetric danger: bounds too tight hide decisive evidence; bounds too loose flood the
Evidence Packet with noise. Choosing the bounds is a design decision that must be recorded in
retrieval provenance (§9.58), not an implicit constant.

**MUST NOT infer:**
- Do not assert that "no result beyond depth d" implies "no result".
- Do not hide the depth/edge-type filters from the reader of the answer.

## 9.14 Relation-aware Traversal

Not every edge is equally useful for every intent. Relation-aware traversal = choosing which
edge types to traverse according to the question type:

- **Provenance** questions ("why does the system believe X?"): traverse `supports`,
  `derivedFrom`, `wasAttributedTo`, `wasGeneratedBy` — the evidence line.
- **Mechanism-structure** questions ("velocity is an application of what?"): traverse
  `instanceOf`, `operation`, `differentiand`, `withRespectTo`, `produces`.
- **Temporal** questions ("the 2020 definition?"): traverse by the claim's valid
  time/publication time, not by structural edges.
- **Contradiction** questions ("who objected?"): traverse claims on the same subject with
  different statuses in the Ledger.

**Formal meaning:** relation-aware traversal = a policy mapping intent → a prioritized set of
edge types (including exclusions) during traversal; the filter is a design assumption and can
drop a decisive path.

**MUST NOT infer:**
- Do not assert that an edge-type filter discards all irrelevant structure (it may discard the
  decisive path too).
- Do not assert that one relation-priority set is universal for every question.

## 9.15 k-hop Neighborhood

A common technique in GraphRAG is to expand from an anchor entity into its **k-hop
neighborhood** — every node within k edges [@edge-graphrag-2024]. The technique is powerful for
gathering context, but you must understand its real nature:

- The 2-edge neighborhood of `CurrentDerivativeApplication` holds not only the mechanism and
  roles — it also holds `ElectricCurrent`, units of measure, sources, authors, assessments,
  related claims, *other* mechanism applications...
- **Most of the neighborhood is noise from the standpoint of a specific question.** Within the
  1-hop neighborhood of `ElectricCurrent` sit both `ElectricalResistance` (possibly important)
  and the unit `Ampere` (little importance to a mechanism question).

Design consequence: **never dump the whole k-hop neighborhood into the context window.** Filter
by semantics — keep the nodes/edges matching the intent, collapse the rest into a static
reference. Figure 9.2 illustrates a filtered neighborhood: keeping only the structural roles,
discarding the noise branches.

**Formal meaning:** k-hop neighborhood = the set of nodes/edges within radius k of an anchor
node; relevance is not entailed by distance — additional semantic filtering is required.

**MUST NOT infer:**
- Do not assert "within k hops" = "relevant".
- Do not assert "beyond k hops" = "irrelevant".
- Do not dump the whole neighborhood into context and call it "rich context".

## 9.16 Subgraph Retrieval and the Minimal Sufficient Subgraph

Rather than discrete paths, the system often needs a **coherent subgraph** — a structural
block sufficient to answer the whole question. For question Q0, the target subgraph is:

```
VelocityDerivativeApplication
 ├─ operation → DerivativeOperation
 ├─ differentiand → Position
 ├─ withRespectTo → Time
 ├─ produces → Velocity
 └─ instanceOf → RATE_OF_CHANGE
CurrentDerivativeApplication
 ├─ operation → DerivativeOperation
 ├─ differentiand → ElectricCharge
 ├─ withRespectTo → Time
 ├─ produces → ElectricCurrent
 └─ instanceOf → RATE_OF_CHANGE
```

Choosing *which* subgraph is a retrieval problem in its own right: generate a candidate set,
then optimize between enough information and avoiding noise. A useful concept is the **minimal
sufficient subgraph** (BOOK-DEFINED): enough structure for the answer to be grounded, without
proliferation. For an explanatory question, the minimal structure usually comprises (a) the
applications asked about, (b) the shared mechanism, (c) the relevant roles, (d) a binding
accepted claim, (e) one source passage to cite.

**Commitment note:** "minimal" here means *minimally sufficient by design policy*, not a
mathematical minimum computable in general. No general formula can prove a subgraph is the
smallest possible — because "sufficient" depends on the question's semantics.

**Formal meaning:** subgraph retrieval = selecting a coherent subgraph that satisfies
constraints (minimal structure, entity coverage, contains evidence) from a larger candidate
set; the optimization is by policy, not in the mathematical sense.

**MUST NOT infer:**
- Do not assert that a chosen subgraph is a provably minimal one.
- Do not assert that more structure is always better.
- Do not treat any connected node set as an "evidence subgraph".

---

# Part C — Text Retrieval

Part B retrieves *structure*. But many questions cannot be answered by a structural path:
ambiguous concepts, a definition needed from a source, or a search for "something similar"
with no symbolic mapping yet. For these, the system retrieves **text** — source passages,
serialized claim records, documents ingested into the system. Part C presents the two families
of text retrieval and how to combine them.

## 9.17 Lexical Retrieval and BM25

**Lexical retrieval** matches the *words* of the question to the *words* of a document. Its
theoretical basis is the probabilistic relevance framework of IR [@robertson-bm25-2009], and
the canonical function taught in this chapter is **BM25** (Okapi BM25). The standard formula
[@robertson-bm25-2009] [@manning-ir-2008]:

$$\mathrm{score}(D,Q) = \sum_{t \in Q} \mathrm{idf}(t) \cdot \frac{f_{t,D}\,(k_1+1)}{f_{t,D} + k_1\left(1 - b + b\,\frac{|D|}{\mathrm{avgdl}}\right)}$$

where:

- $\mathrm{idf}(t) = \ln\!\left(\frac{N - n_t + 0.5}{n_t + 0.5} + 1\right)$ — **inverse
  document frequency**: a word rare across the collection carries more weight;
- $f_{t,D}$ — the frequency of word $t$ in document $D$;
- $k_1$ — the **term-frequency saturation** constant: the more repetitions, the less each
  additional one is worth;
- $b$ — the degree of **document-length normalization** (0 = none, 1 = full): long documents
  are penalized to be fair to short ones.

Reading the formula in plain language: *"a document is relevant if it contains many of the
question's rare words, repeats them without overdoing it, and is not too verbose"*
[@robertson-bm25-2009].

**BM25's strengths:**
- Needs no training data — buildable immediately over a text collection.
- Matches precise technical terms ("derivative", "electromagnetic induction") very well.
- Interpretable: anyone can see why a document ranked high.

**Inherent limits:**
- **No synonym/paraphrase understanding** without shared words: asking "rate of change" when
  the source passage says "derivative with respect to time" scores very low even though the
  content is right.
- The score is a *ranking utility*, not a probability of correctness.

**Score semantics:** a high BM25 score says "good word match", not "this document answers
correctly". The score gap between rank 1 and rank 2 is a relative ranking signal, not an
absolute confidence.

**MUST NOT infer:**
- Do not read the magnitude of a BM25 score as confidence.
- Do not assert that BM25 captures meaning beyond word co-occurrence.
- Do not use idf without explaining it (the rarer a word, the heavier — which is why a
  misspelled word, being rare, can be wrongly prioritized).

## 9.18 Dense Retrieval and the Dual Encoder

**Dense retrieval** overcomes the lexical limit by embedding the question and the documents
into a vector space and measuring proximity. The canonical architecture is the **dual encoder**
from DPR [@karpukhin-dpr-2020]:

$$\mathrm{score}(q, p) = E_Q(q) \cdot E_P(p)$$

where $E_Q$ is the question encoder, $E_P$ the passage encoder; the dot product (or cosine)
measures similarity. DPR is trained with a contrastive loss using in-batch negatives plus one
BM25 hard negative per example [@karpukhin-dpr-2020] — precisely the negative-sampling
technique Ch8 taught, now applied to the retriever problem.

**Strengths:**
- Catches paraphrase and semantic similarity that word matching misses: "rate of change" and
  "derivative with respect to time" can be near each other in embedding space.
- When well trained, dense retrieval substantially beats BM25 on open-domain QA benchmarks
  [@karpukhin-dpr-2020].

**Limits:**
- Most-similar is not correct: the nearest vector can be a passage saying the *opposite*,
  using exactly the right words.
- An embedding score is a ranking signal, not certain relevance, and certainly not truth.
- Model-version sensitive: the same passage, two encoder versions, two different rankings.

**A key boundary from Ch8, extended into this domain:** Ch8 taught **entity ≠ embedding** — an
entity is not its vector [@hogan-inductive]. The principle applies intact to questions and
text:

> **Query vector ≠ question meaning; passage vector ≠ passage content.** An embedding is a
> learned representation serving ranking, not the essence of the object.

**MUST NOT infer:**
- Do not assert that high embedding similarity guarantees relevance.
- Do not assert that dense retrieval always beats lexical retrieval.
- Do not treat a top-ranked embedding result as evidence.

## 9.19 Comparison: When Lexical, When Dense

Table 9.2 summarizes the choice between the two text-retrieval families (BOOK-DEFINED, based
on the two families' properties [@robertson-bm25-2009] [@karpukhin-dpr-2020]):

| Criterion | Lexical (BM25) | Dense (DPR) |
|---|---|---|
| Exact terminology | very good | medium (paraphrase-sensitive) |
| Synonym / paraphrase | poor | good |
| No training needed | yes | no (needs model + data) |
| Interpretability | high | low |
| Spelling-error sensitivity | sensitive (idf boosts odd words) | more robust |
| Cost | low | medium (each passage needs embedding) |

The chapter's practical operating principle: **do not choose one — use both in a hybrid
retrieval scheme** (§9.20) — lexical preserves recall for exact terms, dense extends to
paraphrase. This is not a universal formula for a "more correct" result; it is a more robust
strategy against the diversity of phrasings.

## 9.20 Hybrid Retrieval

**Hybrid retrieval** runs several retrievers in parallel (lexical + dense + possibly a graph
query) and merges the ranked lists. The motivation: different retrievers fail in different ways
— BM25 fails when there are no shared words, dense fails when a rare phrase is decisive.
Combining them raises the chance that *at least one system* sees the important piece.

But keep expectations honest:

> **More signals ≠ a more correct answer.** Hybrid reduces the risk of *missing*, not the
> *correctness* of content. If all three systems pull in the same off-topic passage, hybrid
> merges in the error.

![Three retrieval families: text (independent chunks), graph (linked structure), and hybrid (graph-led + text) — each family is strong in a different way, none is absolutely "more correct".](figures/generated/ch09-text-vs-graph-vs-hybrid.pdf)

The technical detail of merging lists — **rank fusion** — is in the next section.

**MUST NOT infer:**
- Do not assert that hybrid guarantees relevance or correctness.
- Do not assert that hybrid is always better than each component.

## 9.21 Rank Fusion and RRF

With several ranked lists from different retrievers, we need to merge them into one. The
problem: the systems' scores are not comparable (BM25 on its scale, cosine on its scale).
**RRF** (Reciprocal Rank Fusion) solves this by using only the *rank* [@cormack-rrf-2009]:

$$\mathrm{RRF}(d) = \sum_{s \in \mathrm{systems}} \frac{1}{k + \mathrm{rank}_s(d)}$$

with $k$ typically 60. Read it as: *"each system contributes according to the document's
position in that system's list; the lower the rank, the smaller the contribution."*

Strengths: no score normalization needed, robust to incompatible scales, and combines
rank-only lists well [@cormack-rrf-2009]. It is the natural choice for hybrid (lexical + dense
+ graph signal).

**Merged-score semantics:** an RRF score is an *aggregate retrieval utility* — it states a
document's good relative position in the systems' eyes. It is **not** confidence, not a
probability, not an evidence strength.

**MUST NOT infer:**
- Do not read a merged RRF score as confidence.
- Do not assert that RRF selects evidence (it only ranks candidates).
- Do not use an RRF score as a Ch6 assessment value.

## 9.22 Graph-first vs Text-first

An important architectural question: when starting retrieval, should we **go from graph to
text** (graph-first) or **from text into graph** (text-first)?

- **Graph-first:** question → entity linking → fetch structure/subgraph → expand to the text
  passages attached to those nodes. Fits when the schema is known, entities resolve, and the
  question is structural (mechanism, roles).
- **Text-first:** question → passages (BM25/dense) → from passages discover entities/claims →
  expand into the graph. Fits when the question is open, entities are ambiguous, or a
  definition from a source is needed before structure.

In GraphRAG, the two main query modes mirror exactly these two directions: **Local Search**
starts from an entity (graph-first) for entity questions; **Global Search** starts from
community summaries for global questions [@edge-graphrag-2024] [@microsoft-graphrag-docs].

**Honesty principle:** neither side always wins. Mechanism questions in our knowledge system
usually lean *graph-first* (schema known); open definition questions from a source lean
*text-first*. The router (§9.8) picks the direction by intent.

**MUST NOT infer:**
- Do not assert that access order determines correctness.
- Do not declare one side always wins between graph-first and text-first.

---

# Part D — Epistemology-aware Retrieval

## 9.23 Canonical View vs Claim Ledger

This is the most important epistemological distinction of the chapter. Since Ch6–Ch7, the
system stores a **Claim Ledger** (every claim has provenance, a status, and a history) and
maintains a **canonical view** (the state of "what is currently accepted").

Retrieval must *choose the right source according to intent*:

- **FACTUAL/STRUCTURAL** questions ("what is velocity?") → retrieve from the canonical
  view: the currently accepted definition.
- **PROVENANCE/TEMPORAL/CONTRADICTION** questions ("who once objected?", "the 2020
  definition?") → retrieve from the Ledger: claim history, competing claims, superseded
  versions.

The classic violation: answering a *historical/contested* question from the current
canonical view. Figure 9.3 illustrates the two distinct retrieval domains.

![Epistemology-aware retrieval: the Canonical View answers "what is currently accepted"; the Claim Ledger answers "what has been proposed/contested". Historical or contradictory questions must go to the Ledger, not the canonical view.](figures/generated/ch09-ledger-vs-canonical.pdf)

**Formal meaning:** two retrieval domains — the canonical view (state: Accepted, current)
and the Ledger (immutable, with status + history); choosing the domain is an
epistemological decision driven by intent, not a query detail.

**In this book:** "The canonical view answers 'what is currently accepted'; the Ledger
answers 'what has been proposed/contested'. Historical/contradictory questions must go to
the Ledger."

**MUST NOT infer:**
- Do not infer "empty canonical view" ⇒ "empty Ledger" (the canonical view can be empty
  because no claim is Accepted yet, while the Ledger is full of candidates).
- Do not assert that the currently accepted definition is the only definition ever
  proposed.

## 9.24 Governance-aware Retrieval

Since Ch6, each claim carries a governance status: `Accepted`, `Candidate`, `Contested`,
`Rejected`, `Superseded`. Retrieval can filter or prioritize by this status — and
*the filtering must follow intent*:

| Intent | Default status policy |
|---|---|
| Production / FAQ | only `Accepted` (and a note if there is a dispute) |
| Research / comparison | `Accepted` + `Contested` + `Superseded` (with status) |
| History of knowledge | every status, at the correct point in time |
| Audit | every status, including `Rejected` (to understand why it was rejected) |

The epistemological principle: **no status is, by itself, truth.** `Accepted` means
"governance has accepted it", not "true of the world"; `Rejected` means "did not pass
governance", not "false of the world". Retrieval presents status as a provenance fact of
the evidence, not as a conclusion.

**MUST NOT infer:**
- Do not assert `Rejected` ⇒ false of the world.
- Do not assert `Accepted` ⇒ true (governance-accepted ≠ proven).
- Do not filter out every non-Accepted claim for every kind of question (this destroys
  contradiction/history questions).

## 9.25 Temporal Retrieval: Multiple Clocks

The question "What was the definition of current in 2020?" sounds simple but hides a trap:
*2020 is which kind of time?* Since Ch6, the system has several independent clocks:

- **valid time**: when the assertion `ElectricCurrent` was defined to apply from / changed;
- **publication time / assertion time**: which source the claim entered the system from,
  and when;
- **transaction/system time**: from when the system *believed* it, and until when it
  believed it before being superseded.

These three clocks do not coincide. "The definition of current applies from 2019 (valid),
was published in 2021 (publication), and the system believed it from 2022 (system)" is
entirely legitimate. Therefore:

- "What did the system believe in 2020?" → retrieve by **system time**.
- "What definition applied in 2020?" → retrieve by **valid time**.
- "What was published in 2020?" → retrieve by **publication time**.

**Formal meaning:** temporal retrieval = choosing the clock + time point according to
intent; the clocks are independent and must not be conflated.

**Dangerous simplification:** answering every "year X" question with the current state, or
merging the three clocks into one.

**MUST NOT infer:**
- Do not assert that a present truth was believed in the past.
- Do not mix valid time with publication time.
- Do not answer a validity question with a publication record (and vice versa).

## 9.26 Provenance-aware Retrieval

The most common and hardest epistemological question: **"Why does the system believe
this?"** Answering it needs a special kind of retrieval — provenance retrieval — that walks
the provenance chain built since Ch6 (PROV lineage):

```
Claim #C471
  ← supports:  Evidence #E88
  ← derivedFrom: SourceFragment "derivative with respect to time..."
  ← wasAttributedTo: SourceArtifact (book, page, publication)
  ← wasGeneratedBy: ExtractionActivity (model, version, parameters)
  + assessments: reliability, consistency, degree of support
  + governance: status, who/activity that decided, when
```

This chain assembles into an **explanation subgraph**. The key concept parallels
attribution research in NLP: a statement about the world is **attributable to identified
sources** if the identified source(s) support it [@rashkin-ais-2021]. Provenance retrieval
is precisely the mechanism that lets the system demonstrate "attribution" in that sense.

**Formal meaning:** provenance retrieval = fetching the
Claim→Evidence→SourceFragment→SourceArtifact→(activity, assessment, governance) chain and
assembling it into an explanation subgraph; the existence of the chain is a fact, not
evidence of correctness.

**MUST NOT infer:**
- Do not assert that the existence of a provenance chain proves correctness.
- Do not treat a source passage as independent of the extraction chain that produced it
  (the passage may be the result of a mistaken extraction).

## 9.27 Contradiction-aware Retrieval

When a question touches a contested concept — that is, the Ledger holds several claims on
the same topic with differing statuses/assessments — ordinary retrieval (taking the top
evidence on one side) will *hide* the dispute. **Contradiction-aware retrieval** must:

1. Recognize the contested topic (several claims on the same topic, opposing statuses);
2. Retrieve the **competing claims** and the **scope** of each (an opposing claim may be
   limited to a sub-domain);
3. Put them all into the Evidence Packet — *not* forcing the LLM to pick a winning side
   without a policy/evidence.

Example: claim `C471: "RATE_OF_CHANGE describes the essence of velocity"` and claim
`C210: "the derivative is only a model; velocity has its own definitional essence"` share a
topic but differ in scope. Contradiction-aware retrieval returns both with their scopes; the
LLM presents "according to some sources ..., according to other views ...", rather than
picking arbitrarily.

**Formal meaning:** contradiction-aware retrieval = when a claim node/cluster has several
opposing candidates, return the set of competing claims with their scopes and statuses, and
maintain the constraint "do not merge contradictory claims while losing their scope".

**MUST NOT infer:**
- Do not assert that the higher-scoring source is correct.
- Do not merge contradictory claims without preserving their scope.
- Do not answer a contradiction question from the canonical view (it has only one side).

## 9.28 Evidence Diversity

A good explanatory answer needs **diverse** evidence, not merely *a lot*: many copies of the
same source do not increase persuasiveness. The diversity dimensions (BOOK-DEFINED):

- **Multi-source:** source passages from independent documents, not one document quoted
  many times;
- **Multi-type:** structure (mechanism path) + claim (governed) + text (source passage) —
  three mutually complementary types as in §9.9;
- **Multi-perspective:** if the topic is contested, include the opposing claims (§9.27);
- **Multi-time:** if the question is about evolution, include older versions (§9.25).

The retrieval paradox: an LLM tends to become "more confident" when it sees many similar
passages — but the number of *same-viewpoint passages from the same provenance* is a form of
pseudo-replication, not independent evidence. The diversity policy guards against this.

**MUST NOT infer:**
- Do not assert many same-source passages = much evidence.
- Do not assume every unit type is needed in every answer (policy follows intent).

## 9.29 top_k as an Epistemic Bound

The central concept of the whole chapter, echoed in the standard RAG pipelines
[@lewis-rag-2020] [@karpukhin-dpr-2020]: every ranked retrieval *cuts* at a top_k threshold.
Since Ch7 the book has taught top_k as an implicit boundary. Here it is elevated to a
principle:

> **top_k is an epistemic boundary: the model cannot reason over evidence it does not see.**
> For an explanatory question, the answer changes entirely if the decisive evidence sits at
> rank 6 while top_k=5.

At the same time, the opposite trap is real:

- **top_k too small** → the decisive evidence is lost → a "plausible" answer missing half
  the truth (Figure 9.4).
- **top_k too large** → flooded with noise and distractors → the LLM "gets lost" in a pile
  of context; accuracy falls rather than rises.

![top_k as an epistemic boundary: if the decisive evidence lies outside the top_k window, the system does not know it exists — "not in top_k" ≠ "not relevant".](figures/generated/ch09-topk-bound.pdf)

**The chapter's policy:** top_k is not a constant. It is tuned to the question type
(contradiction questions need higher recall) and is *recorded in the retrieval provenance*
so the reader of the answer knows the boundary they are looking through.

**MUST NOT infer:**
- Do not infer "not in top_k" ⇒ "not relevant" or "does not exist".
- Do not assert that raising top_k monotonically improves the answer.
- Do not treat top_k as a neutral plumbing detail (it is an epistemic boundary).

## 9.30 Measuring Retrieval: Precision, Recall, P@K, R@K, MRR, nDCG

To evaluate the retrieval tier (separately from the generation tier), we need the IR metrics
[@manning-ir-2008] [@jarvelin-ndcg-2002]. Defined over a gold-relevant set $R$ and a
retrieved set $A$:

- **Precision** = $|R \cap A|\,/\,|A|$ — of what was retrieved, how much is relevant.
- **Recall** = $|R \cap A|\,/\,|R|$ — of what should have been retrieved, how much was.

The two trade off against each other: raising recall (retrieving more) usually lowers
precision (adding junk). For explanatory questions, low recall is a hidden catastrophe
(§9.29); for questions with many distractors, low precision wrecks synthesis.

**When retrieval ranks rather than returning a flat set**, use cutoff metrics:

- **P@K**: of the top-K, how many are relevant.
- **R@K**: of the top-K, how much *of the entire relevant set* was cut off.

Worked example: the corpus has 8 relevant passages for question Q0; the top-5 retrieval
contains 4 of them. Then P@5 = 4/5 = 0.8, R@5 = 4/8 = 0.5. A "high-quality" system with
P@5=1.0 but R@5=0.25 (only 2/8 relevant) looks perfect on the surface while hiding 6/8 of
the evidence.

- **MRR** (Mean Reciprocal Rank): the mean of 1/rank of the *first relevant result*
  [@manning-ir-2008]. Fitting when the user needs only the first correct answer.
- **nDCG** (normalized Discounted Cumulative Gain): scores *graded relevance* (e.g.
  0/1/2/3) rather than binary, discounts by log position, and normalizes by the ideal
  ordering [@jarvelin-ndcg-2002]:

$$\mathrm{DCG}@k = \sum_{i=1}^{k} \frac{\mathrm{rel}_i}{\log_2(i+1)}, \qquad
\mathrm{nDCG}@k = \frac{\mathrm{DCG}@k}{\mathrm{IDCG}@k}$$

**The unified semantics of ALL these metrics:** they measure *ranking quality against a set
of relevance judgments* — not the correctness of the answer, not truth, not epistemic
confidence.

**An important note on inheritance:** MRR appears in Ch8 for link prediction. The metric
formula is shared, but the *object* differs: Ch8 evaluates link prediction (candidate
triples), this chapter evaluates retrieval (evidence units). Do not borrow the semantics of
Ch8-MRR as "retrieval truth".

**MUST NOT infer:**
- Do not assert that P@K/R@K/MRR/nDCG measure the correctness of the answer.
- Do not compare nDCG across different relevance scales.
- Do not compute these metrics without a clearly defined gold-relevance set.

## 9.31 Reranking

A two-stage architecture: **a broad, cheap first stage** — lexical/dense pulls a large
candidate bag (e.g. 100–1000) — then **a sharp second stage** with a stronger but slower
reranker that scores *each (question, candidate) pair* jointly [@nogueira-rerank-2019]. The
original BERT re-ranking work demonstrated MRR@10 gains on MS MARCO when the cross-encoder
sees the question and passage together [@nogueira-rerank-2019].

A reranker can be:

- **Cross-encoder** (BERT) — scores the (q, p) pair jointly [@nogueira-rerank-2019];
- **LLM reranker** — asks the LLM "which passage is more relevant" (expensive, needs
  supervision);
- **Graph-feature reranker** (BOOK-DEFINED) — adds graph distance, relation type, shared
  mechanism, governance status, provenance availability, temporal match, and source
  diversity into the relevance decision. **Special note:** there is no universal weighting
  formula the book endorses — combining these signals is a *per-problem policy* and must be
  stated explicitly.

The essential boundary:

> **Reranking cannot rescue recall.** If the first stage missed the decisive passage, no
> matter how excellent the reranker, it cannot see it to promote it. A first-stage miss is a
> fatal error.

**MUST NOT infer:**
- Do not assert that a reranker score is confidence.
- Do not expect the reranker to fix the first stage's recall errors.
- Do not assert that LLM re-ranking guarantees correctness.
- Do not publish a signal-weighting formula as "standard" when it is only one problem's
  policy.

---

# Part E — Context Assembly and Answer Generation

## 9.32 Context Assembly

After retrieval, the evidence units (structural paths, claims, source passages,
contradictions, provenance, temporal facts) must be **assembled** into the LLM's input.
Assembly is a semantic design decision, not string concatenation:

- **Select:** which units enter the window (per §9.28 diversity and §9.29 boundary);
- **Group:** cluster by topic/aspect (shared structure, evidence, contradiction, provenance);
- **Order:** place the decisive evidence in the most reliably-read position (§9.34);
- **Label:** each block carries its type, status, and provenance.

Standardized from research: original RAG concatenates the question with the retrieved
passages to form the generator's input [@lewis-rag-2020]. This chapter extends it: the input
is not just "question + passages" but "question + a structured Evidence Packet".

**MUST NOT infer:**
- Do not assert that assembly order does not affect the result (it does, §9.34).
- Do not assert that more context means more knowledge (noise grows too).

## 9.33 Context Compression

When the evidence set exceeds the window, **compression** is needed: drop duplicates,
summarize neighborhoods, keep the decisive path, select representatives. Three techniques:

1. **Dedupe:** drop same-source / same-content passages (§9.28).
2. **Representative selection:** keep the most fully-supporting passage for each important
   claim.
3. **Summarization:** condense a neighborhood/subgraph into compact prose.

Technique 3 is the most dangerous:

> **A summary is a derived artifact — not a source.** A summary can discard the decisive
> evidence, flatten the nuance of a contradiction, and go stale when the source changes. A
> summary must keep a provenance link back to its origin [@rashkin-ais-2021].

This is also the operating principle of community summaries in GraphRAG (§9.56): they are
provenance-bearing LLM products, candidate inputs — not canonical knowledge
[@edge-graphrag-2024] [@microsoft-graphrag-docs].

**MUST NOT infer:**
- Do not assert that a summary is equivalent to its source.
- Do not assert that compression preserves all evidence.
- Do not inject a summary into the canonical KG without going through governance
  (Ch6/Ch7).

## 9.34 Lost in the Middle: Context Order Affects Reliability

Empirical research on long-context language models has shown: **information at the beginning
and end of the context window is used more reliably by the model than information in the
middle** — the "lost in the middle" effect [@liu-lostmid-2023]. When the decisive passage
sits in the middle of a long context, answer quality drops markedly compared to when it is
at the start or end.

Engineering consequences for the assembly tier:

- Place the decisive evidence (mechanism path, accepted claim, primary source passage) at
  the start or end of the window;
- Do not bury important contradictions in the middle of a pile of secondary evidence;
- When the window is long, lower the expectation that the model "sees" every detail in the
  middle of the window.

**Commitment note:** the result is empirical on specific models/tasks — do not elevate it to
a universal law, but the engineering consequence (order affects quality) is real and must be
designed for [@liu-lostmid-2023].

**MUST NOT infer:**
- Do not assert that every model is affected equally.
- Do not use this research to justify reordering context arbitrarily.
- Do not treat context position as a *right/wrong* mechanism, only a *reliability* factor.

## 9.35 Graph Serialization for the LLM

The LLM reads text, not RDF directly. So the graph structure must be **serialized** into a
textual form. The options and trade-offs:

| Form | Example | Pro | Con |
|---|---|---|---|
| Triple | `C_app operation DerivativeOperation` | precise, no added inference | long, context-poor |
| Table | role × application table | intuitive comparison | bulky with many nodes |
| JSON | nested structure | machine-readable | less natural for humans |
| Compact prose | "both applications use the derivative with respect to time" | concise, natural | loses structure, easily confused with the model's own inference |
| Evidence Card | fixed-field Evidence Card | traceable (BOOK-DEFINED) | rigid frame |

The principle: **no serialization preserves all semantics.** Raw RDF is precise but
token-hungry; prose is compact but easily "translates" meaning away — especially dangerous
if the model re-presents it as though it were its own inference. The chapter's policy: for
structural questions, prefer triples/tables with a "this is graph data" label; for
explanatory questions, use both structure and prose and label each kind.

**MUST NOT infer:**
- Do not assert that one serialization preserves all semantics.
- Do not treat writing structure as prose as a zero-cost loss.

## 9.36 Evidence Packet — BOOK ENGINEERING MODEL

The **Evidence Packet** is an architectural concept defined by this book (BOOK-DEFINED): a
structured container that is the **single interface between the retrieval tier and the answer
generation tier**. Instead of throwing loose chunks at the LLM, the retrieval tier packages
everything the generation tier needs to answer faithfully.

The canonical structure of an Evidence Packet (Figure 9.5):

```
EvidencePacket
├─ question (original) + interpreted_intent (with ambiguity)
├─ resolved_entities (each entity: id, confidence, ambiguity note)
├─ canonical_claims    (relevant Accepted claims + status)
├─ competing_claims    (Contested/Superseded + scope + status)
├─ structural_paths    (traversed structural paths + depth bound)
├─ source_passages     (source passages for citation + provenance)
├─ provenance_chain    (Claim→Evidence→SourceFragment→SourceArtifact)
├─ temporal_scope      (which clock + which time point was used)
├─ assessments         (relevant Ch6 assessments)
├─ retrieval_metadata  (retriever, version, index snapshot, top_k, scores, reranker)
└─ statuses            (each item labeled: asserted / derived / predicted)
```

![Evidence Packet (BOOK-DEFINED): a structured container — question, intent, entities, claims, paths, source passages, provenance, time, assessments, retrieval metadata, and epistemic status labels.](figures/generated/ch09-evidence-packet.pdf)

### 9.36.1 The Evidence Packet as a 3-Compartment Dossier

To make the structure above *auditable*, this chapter frames the Evidence Packet as a
**physical three-compartment dossier** (BOOK-DEFINED) — each compartment bears a distinct
epistemic responsibility, and each is read by a different layer of the pipeline:

**Compartment 1 — Raw Evidence & Citations.** Every *verbatim* source fragment the answer is
allowed to lean on: source passages verbatim, a **document hash** for tamper-evidence, a
**URI span** and **line numbers** to point precisely to a location in the source. This
compartment answers: *"which words, where, does the answer rest on?"* — this is where
citations (§9.40) must point, not to "the whole document".

**Compartment 2 — Epistemic Statuses.** Every relevant claim with its **Claim Ledger ID**
(C471 vs C210), its **governance status** (`Accepted`, `Contested`, `Candidate`,
`Superseded`), and its **time window** (valid time / transaction time, §9.25). This
compartment answers: *"to what degree does the system believe this, since when, and who
objects?"* — this is what the generation tier reads to know which sentences to write as
fact, which to present on both sides, and which to abstain on (§9.43).

**Compartment 3 — Verification & Lineage Trail.** The **PROV-O** activity chain
[@prov-o] recording *who produced each item in the packet*: which extractor (with **model
version**), which evaluator (with **signature**), and each item's **aggregated confidence**.
This compartment answers: *"by what process was this item produced, and how reliable is that
process?"* — this is what an auditor reads back to reproduce the whole process.

Mapping the fields of the canonical structure tree onto the three compartments:

| Compartment | Fields in the structure tree (§9.36) | Epistemic responsibility |
|---|---|---|
| 1 — Raw Evidence & Citations | `source_passages`, `structural_paths`, `provenance_chain` (SourceFragment→SourceArtifact branch) | which words, where, the answer rests on |
| 2 — Epistemic Statuses | `canonical_claims`, `competing_claims`, `temporal_scope`, `statuses` | to what degree, since when the system believes it |
| 3 — Verification & Lineage | `provenance_chain` (PROV-O activity branch), `assessments`, `retrieval_metadata` | by what process the item was produced, how reliable |

**Why three compartments, not one flat list?** Because the three audit questions — *"based on
which words"*, *"believed to what degree"*, *"produced by whom"* — are answered by three
different layers: the generation tier reads Compartments 1–2, the self-check tier (§9.67)
cross-checks against Compartments 1–2, and the auditor reads Compartment 3. Merging them into
one flat list makes an error in Compartment 2 (a Contested claim written as Accepted)
undetectable independently of an error in Compartment 1 (a wrong source passage). Separating
compartments turns "a complete packet" into a property *checkable compartment by compartment*.

**Honesty note:** a three-compartment dossier with *all fields present* still does not
guarantee *enough evidence* — it can be full yet missing the decisive piece (a recall error,
§9.30), or full of noise. The three compartments are an audit structure, not a quality
guarantee.

Why is such a structure needed instead of "just retrieve and dump into the prompt"?

1. **Separation of responsibility:** the retrieval tier owns *getting the right things*; the
   generation tier owns *synthesizing faithfully*. The Evidence Packet makes this boundary
   checkable.
2. **Epistemic labeling:** each item in the packet carries a label `asserted` (stated by a
   source), `derived` (sound entailment, Ch5), or `predicted` (a model's prediction, Ch8).
   The three levels must not be conflated (see §9.60).
3. **Full provenance:** the later answer to "why say this" is simply reading back the issued
   Evidence Packet.

**Honesty note:** a "fully-fielded" Evidence Packet does not guarantee *enough evidence* — it
can be full yet missing the decisive piece (a recall error, §9.30), or full of noise. The
Evidence Packet is a necessary condition for a good answer, not a sufficient one.

**MUST NOT infer:**
- Do not assert packet-full ⇒ evidence-sufficient.
- Do not assert the packet's content is true of the world.
- Do not call dumping raw chunks into a prompt an "Evidence Packet".

## 9.37 Answer Generation

The generation tier receives the Evidence Packet and produces an answer draft. In original
RAG the generator is a seq2seq model reading question + retrieved passages
[@lewis-rag-2020]; in this chapter's architecture the generator reads question + packet and
must obey four disciplines:

1. **Add no relation outside the packet:** every new assertion about a relation between
   entities not present in the packet is a prohibited act (this is the main source of
   hallucination, §9.66).
2. **Distinguish speech acts:** an answer comprises different kinds — structural summary,
   comparison, path explanation, hedged statement, unknown declaration — and each kind is
   written differently.
3. **Present contradictions rather than pick a side** (when the packet holds competing
   claims).
4. **Self-check before emitting:** match each sentence against an item in the packet
   (self-check §9.67).

**Formal meaning:** answer generation = a mapping (question, Evidence Packet) → draft, under
the constraint of not inventing relations; the draft distinguishes supported, inferred,
uncertain, and unknown sentences.

**MUST NOT infer:**
- Do not assert that generated text has been verified against the world.
- Do not assert that a fluent answer is a grounded answer.

## 9.38 Answer Claims

An answer is not a single undifferentiated block — it decomposes into **answer claims**
(AnswerClaims). For example, the answer to Q0 can split into:

- **A1:** "VelocityDerivativeApplication and CurrentDerivativeApplication are both
  applications of the RATE_OF_CHANGE mechanism." — supported by the structural path + an
  Accepted claim.
- **A2:** "Both take the derivative with respect to time (withRespectTo=Time)." — supported
  by the role table.
- **A3:** "This means velocity 'is in essence' a rate of change." — an **inference**, needs a
  different label; may be opposed by claim C210.
- **A4:** "No other mechanism governs velocity." — **unknown** (not exhaustively searched),
  must not be written as fact.

Decomposing into answer claims allows evaluation *per sentence*: citation, support,
faithfulness — rather than scoring the whole paragraph as one block [@gao-cite-2023]
[@rashkin-ais-2021].

**MUST NOT infer:**
- Do not assert that every answer claim is verifiable against the world.
- Do not assert that an answer with one cited sentence is fully cited.

## 9.39 Grounded Answer

A **grounded** answer means it is supported by sources the system has identified — the
"attributable to identified sources" (AIS) property [@rashkin-ais-2021]. This is the central
concept of attribution evaluation: *generated text about the outside world is attributable if
identified sources support it*.

The decisive epistemic boundary:

> **Grounded ≠ correct.** An answer can be fully grounded — every claim supported by an
> identified source — and still be false of the world, if that source is wrong, stale, or
> misinterpreted. Groundedness is a property of the *answer–source* relation, not the
> *answer–world* relation [@rashkin-ais-2021].

Conversely, an answer correct of the world but with no supporting source in the system is
"lucky-correct" — indefensible under audit.

### 9.39.1 Closed-World Prompting: Guarding Against Hallucination by Structure

The "grounded" state is not a natural result of handing the packet to the model — it is the
result of a **prompt that treats the Evidence Packet as a closed world** (a closed-world
constraint). The generation tier (§9.37) receives the packet with a structured command:

> *"Every assertion about a relation must point to an identifier in the packet — a Claim
> Ledger ID in Compartment 2 (C471, C210) or a source passage in Compartment 1 (URI + line
> number). If the question cannot be derived from the items in the packet, answer 'Unknown'
> or 'Evidence missing'; do not fill the gap with your latent knowledge."*

Three design consequences of this command:

1. **Every utterance has an identifier anchor.** Because each answer claim is forced to point
   to Compartment 1/2, a sentence *without* an anchor is an immediate warning flag at the
   self-check tier (§9.67) — relational hallucination (§9.66, type 1) is forced to be
   "invisible" to slip through.
2. **Abstention is a valid, named output.** "Unknown" and "Evidence missing" are two of the
   states in §9.44; the prompt permits them as the *correct choice*, not a failure. This turns
   abstention (§9.43) from a desired behavior into an activatable one.
3. **The closed world cuts off the "lucky-correct" loop (cell A, §9.42).** The model is
   forbidden from using latent knowledge to answer, so a correct answer can only be correct
   *and* inside the packet — that is, cell C, not cell A.

**Commitment note:** the closed world reduces hallucination but does **not eliminate** it —
the model can still fabricate a "identifier" that looks like a Claim ID, or misinterpret a
genuine source passage. So the packet constraint is *layer one* (risk reduction), while
claim–evidence alignment (§9.67) is *layer two* (catching what slips through). The two layers
work together; neither is sufficient alone.

**MUST NOT infer:**
- Do not infer "grounded" ⇒ "correct".
- Do not infer "not grounded" ⇒ "false" (it may be true but untraceable).
- Do not treat the closed-world prompt as sufficient to eliminate hallucination (it only
  reduces risk; the alignment layer §9.67 is still needed).

## 9.40 Citation & Citation Completeness

A **citation** attaches an answer claim to the *evidence that actually supports it* and that
evidence's provenance. The ALCE benchmark defines two complementary metrics
[@gao-cite-2023]:

- **Citation recall** — how much of *the sentences/claims needing support* carry a citation;
- **Citation precision** — of the citations, how many *actually support* the sentence they
  are attached to.

The two metrics separate two different errors: missing citations (a recall error) and wrong
citations (a precision error). The ALCE study also shows that even strong models struggle to
cite every claim fully [@gao-cite-2023] — so this chapter teaches citation as an *output that
must be checked*, not a cosmetic option.

The chapter's citation rules (BOOK-DEFINED):

1. Each important, verifiable answer claim → at least one citation.
2. A citation must point to the *source passage that actually contains the supporting
   information* — not to a document merely because it is in the packet.
3. An inferred citation (A3 in §9.38) must point to the *structural path/claim* serving as
   premise, and be labeled "inferred from ...".
4. When the answer presents a contradiction, each side must have its own citation.

**MUST NOT infer:**
- Do not assert that having a citation ⇒ being supported.
- Do not assert that every document in the packet is citable (only genuinely supporting
  passages are worth citing).
- Do not count citations in place of checking each claim (coverage).

## 9.41 Faithfulness ≠ Correctness

**Faithfulness** measures the relation between the answer and the *provided context*: the
answer does not fabricate and does not contradict that context. In the book's terms:

> **Faithfulness = the answer lies within the support scope of the Evidence Packet.**

The key boundary: faithfulness is an **answer–context** property, entirely distinct from
correctness being an **answer–world** property:

- An answer can be **faithful but wrong**: if the packet contains a wrong/stale source and
  the model faithfully summarizes that source, the "faithful to a wrong source" result is
  still wrong.
- An answer can be **correct but unfaithful to the packet**: the model ignores the packet and
  uses its latent knowledge to answer correctly — this is "lucky-correct", uncontrollable.

**MUST NOT infer:**
- Do not infer "faithful" ⇒ "correct".
- Do not infer "unfaithful to the context" ⇒ "false of the world".

## 9.42 The 2×2 Table: Correctness × Groundedness

Combining the two axes — *correct of the world* (correctness) and *grounded in the packet*
(groundedness) — yields the decisive 2×2 table (Figure 9.6):

| | Grounded | Not grounded |
|---|---|---|
| **Correct** | **C** — the goal: correct and supported | **A** — "lucky-correct": untraceable |
| **Wrong** | **B** — faithful to a wrong source | **D** — wrong and fabricated |

- Cell **C** is the goal of every design: correct of the world *and* every claim supported by
  an identified source.
- Cell **B** is the most dangerous trap for audit: the system "follows the process" —
  retrieval, assembly, full citation — yet is wrong because the source is wrong. **A good
  process does not turn cell B into cell C**; only external evaluation (users, cross-checking)
  can.
- Cell **A** is "lucky-correct": the LLM uses latent knowledge, bypassing the packet;
  indefensible and non-reproducible.
- Cell **D** is wholesale hallucination.

![The 2×2 correctness/groundedness table: the goal is cell C (correct and supported); cell B (faithful to a wrong source) is the audit trap — a good process does not turn cell B into cell C.](figures/generated/ch09-correctness-grounding.pdf)

Design consequence: answer evaluation must measure *both axes*, never collapsing them into one
score. This chapter and §9.61 build the evaluation procedure along exactly these two axes.

**MUST NOT infer:**
- Do not assert that a grounded answer is automatically in cell C.
- Do not score a single axis and then declare quality.
- Do not use "the process was correct" to conclude "the answer is correct" (cell B is the
  counterexample).

## 9.43 Abstention

When evidence is insufficient, the system's correct behavior is **abstention**: stating
clearly "insufficient evidence" rather than fabricating a fluent answer. The abstention
conditions (BOOK-DEFINED):

1. **No relevant claim** — nothing found in the Ledger/canonical view;
2. **Unresolved entity** — an ambiguous mention not yet decided (§9.5);
3. **Undecidable contradiction** — opposing claims all carry weight, no policy/metric to
   choose;
4. **Weak support** — a claim exists but the assessment is low/inconsistent;
5. **Out of scope** — the question exceeds the system's knowledge domain;
6. **High retrieval uncertainty** — large interpretation ambiguity (§9.3).

Abstention is *not* a failure — it is the correct epistemic behavior. An abstaining answer
must name *which kind of lack* is occurring (see §9.44), so the user knows how to proceed.

**Abstention is unlocked by the closed-world prompt (§9.39.1).** The six conditions above only
become *realizable* behavior once the prompt permits the model to say "Unknown"/"Evidence
missing" as a valid output instead of forcing text generation. Without that license, the model
is forced to "answer at all costs" and abstention becomes impossible — this is why §9.39.1
(prompt design) and §9.43 (abstention policy) are two faces of one mechanism: the closed-world
constraint *unlocks* abstention, and abstention *consumes* that unlock.

**MUST NOT infer:**
- Do not assert abstention ⇒ the fact is false (missing evidence ≠ false).
- Do not treat abstention as a system failure when it is the correct behavior per policy.
- Do not abstain too early when the real error is in the retrieval tier (§9.44).

## 9.44 Unknown vs Not Found; Retrieval Error vs Missing Knowledge

The final chain of distinctions in this part — and one of the most important in the chapter:

> **NOT RETRIEVABLE ≠ NOT IN INDEX ≠ NOT IN KG ≠ KNOWN FALSE ≠ UNKNOWN.**

Five distinct epistemic states, and the system must state clearly which one it is in:

1. **Not found by this retrieval** — the retrieval plan found nothing (possibly due to top_k,
   depth, or a weak retriever);
2. **Not in index** — the index does not contain it (index lag, §9.10);
3. **Not in KG** — the graph/Ledger has no claim (but OWA from Ch4: absent ≠ false);
4. **Known false** — there is a rejecting assessment (only when the Ledger holds refuting
   evidence);
5. **Unknown** — insufficient information at every level.

Alongside it, a diagnosis that separates two kinds of error:

> **Retrieval error ≠ missing knowledge.** If the correct claim *is in the Ledger* but the
> retriever missed it, the fault is in the retrieval tier (top_k, index, embedding, depth),
> not "the system doesn't know". A wrong diagnosis leads to fixing the wrong place: dumping
> in more data when the problem is retriever configuration.

**MUST NOT infer:**
- Do not infer "no retrieval result" ⇒ "no knowledge".
- Do not infer "not found" ⇒ "false".
- Do not blame the KG/model when the real error is in retrieval configuration.

---

# Part F — Dynamic and Agentic Retrieval

## 9.45 Query Planning & Execution

In §9.8, the retrieval plan was introduced as a sequence of retrieval operations. Here we go
deeper into *who plans*. There are three options, and an LLM is not mandatory:

1. **Rule-based:** intent FACTUAL/STRUCTURAL → a fixed sequence; cheap, deterministic,
   checkable.
2. **LLM planner:** given the intent + a retrieval-operation library, the LLM proposes a
   sequence; flexible for unusual questions, but needs supervision and bounds (the LLM can
   "invent" a nonsensical retrieval sequence).
3. **Hybrid:** rules for common patterns, LLM for exceptions: planning changes the router's
   route (§9.71).

**MUST NOT infer:**
- Do not assert that an LLM is *required* to plan.
- Do not assert that a plan is deterministic truth (the planner can be wrong).
- Do not assert that any planner is infallible.

## 9.46 Static vs Agentic Retrieval

- **Static:** run the plan once, assemble, generate the answer. Enough for simple/single-hop
  questions. Original RAG is a one-pass static style [@lewis-rag-2020].
- **Agentic / iterative:** after each retrieval round, check the gaps and issue the next query
  round. Useful for multi-step questions ("find the mechanism, then find other applications of
  that mechanism, then find evidence for each application").

Agentic is not automatically better:

| Agentic risk | Why |
|---|---|
| Query drift | each round strays further from the intent (§9.48) |
| Noise/cost escalation | each round adds tokens, adds latency |
| Confirmation bias | later rounds usually only reinforce earlier ones (§9.49) |
| Non-convergence | no stopping condition → infinite loop (§9.47) |

**MUST NOT infer:**
- Do not assert that iterative retrieval guarantees a better answer.
- Do not assert that many retrieval rounds are always worth the cost.

## 9.47 Stopping Conditions

Agentic retrieval must have an **explicit stopping condition** (BOOK-DEFINED), because "keep
searching to be sure" is a circular fallacy — more evidence can add noise and cost. Valid
stopping conditions:

1. **Evidence cells filled:** every important answer claim of the question has an item in the
   packet (per each intent's policy, §9.4);
2. **No new information:** a new retrieval round adds no significant relevant unit;
3. **Relevance threshold:** the new score/ratio drops below a threshold;
4. **Budget exhausted:** the allowed rounds/tokens are used up → *report the lack state*, do
   not continue blindly;
5. **Human-needed contradiction:** opposing claims all carry weight → stop and escalate to a
   human/policy decision.

**Honesty note:** most stopping conditions only guarantee *the process stops*, not *the
evidence is sufficient*. The final report must record which stopping condition fired — budget
exhausted means the result is "lacking due to budget", not "complete".

**MUST NOT infer:**
- Do not infer stopped-searching ⇒ complete.
- Do not infer a budget-limited result is complete.

## 9.48 Query Drift

**Query drift** is the cumulative error of iterative retrieval: each subquery round deviates
further from the original intent. A real example in the continuous domain:

```
Round 1: "the mechanism of RATE_OF_CHANGE"     → original intent: mechanism structure
Round 2: "the derivative"                       → narrows to mathematics
Round 3: "derivatives in finance"               → drifts to another domain
```

By round 4, the system "successfully" retrieves passages about financial derivatives —
entirely far from the original intent, yet every step was locally valid. This is why one must
**keep a record of the original intent** and compare each round against it, together with
recording provenance for each subquery (which spawned from which).

**MUST NOT infer:**
- Do not assert that later retrieval rounds are evaluating the same original question.
- Do not omit recording subquery provenance (it loses the ability to detect drift).

## 9.49 Confirmation Bias in Retrieval

When the system (or the user) starts from a hypothesis — "velocity and current are in essence
the same mechanism" — one-sided retrieval will fetch only supporting evidence. The chapter's
chain of distinctions:

> **Supporting evidence ≠ truth.** A system that retrieves only the supporting side is a
> system that *confirms* rather than *tests*.

Example: question Q5 (is there any claim opposing/limiting the correspondence?) must go to the
Ledger to find opposing claims — not merely to "present objectively" but because **counter-
examples are the primary data** of an honest explanatory answer. Omitting the opposing side is
an epistemic error, not just an omission.

**MUST NOT infer:**
- Do not infer a supporting-only evidence set ⇒ the hypothesis is true.
- Do not assert a retrieval was "thorough" when it fetched only one side.

## 9.50 Hypothesis-testing Retrieval

This is a direct bridge to Ch8. Suppose Ch8 generated a candidate mechanism hypothesis
(CandidateMechanismHypothesis): "velocity, current, and population growth share the
RATE_OF_CHANGE mechanism". Retrieval here plays the role of a *testing interface*
[@edge-graphrag-2024]:

- Retrieve **support**: existing applications, Accepted claims asserting the correspondence;
- Retrieve **challenge**: the hard negatives — finite difference (average rate differs from
  instantaneous derivative), ratio (% growth differs from absolute derivative), gradient,
  accumulation — all *competing candidates* with the derivative mechanism;
- Retrieve **boundary**: the precise definition of each concept to detect scope mismatch.

Result: an honest answer does not absolutely assert "the three phenomena are the same
mechanism", but presents the correspondence as *bounded and contested*: "structurally, as
derivatives, they are alike; numerically, there are differences ...".

**MUST NOT infer:**
- Do not infer no-challenge ⇒ the hypothesis is accepted.
- Do not assert a hypothesis tested by retrieval is accepted knowledge (still a candidate
  until it passes Ch6/Ch7).

## 9.51 Local vs Global Questions

GraphRAG distinguishes two question types with two different retrieval strategies
[@edge-graphrag-2024]:

- **LOCAL** — about a specific entity/subgraph: "What is the definition of current?" — needs
  entity-anchored retrieval: resolve the entity → its subgraph/neighborhood → attached
  evidence.
- **GLOBAL** — about an overall pattern across the whole graph: "Which mechanisms are used
  most in this knowledge system?" — the answer is not in one entity but *globally*; needs a
  hierarchical synthesis strategy or a synthesis query (§9.56).

**Principle:** there is no single strategy for both. The domain modeled by each question per
§9.4 — intents 8/9 (discovery/multi-hop) usually lean global.

**MUST NOT infer:**
- Do not assert that a global answer exists within each individual entity.
- Do not assert that local retrieval suffices for a global question.

---

# Part G — GraphRAG and the Complete Retrieval System

## 9.52 GraphRAG Is an Architecture Family, Not a Standard Algorithm

The term **GraphRAG** sounds like a single technique, but in practice it is a *family* of
architectures: retrieval-augmented generation methods that use explicit graph structure in the
retrieval/context-assembly process — as opposed to pure RAG that relies only on independent
text passages [@edge-graphrag-2024].

The original "From Local to Global" research describes one concrete pipeline
[@edge-graphrag-2024]:

```
TextUnits → LLM extracts entities/relations/claims
  → entity/relation/claim graph
  → Leiden community detection
  → bottom-up community summarization
  → question-driven retrieval:
      Local Search  (fan-out around an entity)
      Global Search (map-reduce over community summaries)
```

Microsoft's official documentation describes a public implementation (MIT license) with search
modes: Global, Local, DRIFT, Basic [@microsoft-graphrag-docs]. What matters for the book's
semantics:

> **Microsoft GraphRAG is ONE implementation of the GraphRAG family — not the definition of
> GraphRAG.** Community summarization is *one design choice*; graph structure in retrieval is
> the family's central feature, not one product's.

**Marketing warning:** any system that "adds a bit of graph" to RAG can call itself GraphRAG;
from that one says very little about quality. In this book, the phrase "GraphRAG" always comes
with a description of *which specific structure* is being used.

**MUST NOT infer:**
- Do not assert GraphRAG is a single standardized algorithm.
- Do not assert Microsoft GraphRAG is the standard of GraphRAG.
- Do not assert GraphRAG guarantees better answers, or eliminates hallucination.

## 9.53 RAG vs KGQA vs GraphRAG: a Decision Table

Three question-answering mechanisms are often confused. Distinguish them by *answer mechanism*
[@chakraborty-kgqa-2019] [@lewis-rag-2020] [@edge-graphrag-2024]:

| Criterion | KGQA | Text RAG | GraphRAG |
|---|---|---|---|
| Answer mechanism | structural query/reasoning over the graph | passage retrieval + generation | graph-guided context retrieval + generation |
| Output | result set / set | generated text | generated text (structured context) |
| Precise facts | very strong | medium (needs grounding) | medium-high |
| Open/definition questions | weak (needs mapping) | strong | strong |
| Path-style explanation | direct | indirect | intermediate |

The router's decision table (§9.8, §9.71):

| Question | Best route | Why |
|---|---|---|
| "Velocity is an application of which mechanism?" (clear entity, known schema) | **KGQA** — precise graph query | absolute precision, low cost [@chakraborty-kgqa-2019] |
| "The 2020 definition of 'current'?" | **KGQA temporal / ledger** | needs temporal + status precision |
| "What is analogous to 'rate of change' in the documents?" (open) | **Text RAG** | no schema to query precisely |
| "Why are velocity and current the same mechanism?" (structure + evidence) | **GraphRAG/hybrid** | needs structure + source passages combined |
| "The most common mechanisms?" (global) | **GraphRAG Global** | needs cross-community synthesis [@edge-graphrag-2024] |

**The key point:** no mechanism is absolutely "better" — each is strong in a region of
questions. A precise structural question routed through RAG/LLM is *wasteful and adds
fabrication risk*; an open question forced into SPARQL is *useless*.

![Comparison of three QA mechanisms: KGQA (precise querying over the graph), Text RAG (passages + generation), GraphRAG (graph-guided retrieval + generation). Complementary, not substitutes.](figures/generated/ch09-kgqa-rag-graphrag.pdf)

**MUST NOT infer:**
- Do not call every "graph-having" RAG a KGQA.
- Do not assert that a determinately queryable question needs RAG.
- Do not assert GraphRAG replaces KGQA for precise questions.

## 9.54 The Path Is an Explanation, Not a Proof

One of the strengths of question answering over graphs is **path-based explanation**:
presenting the answer with a "why" chain of relations. For example:

> "Velocity is produced by VelocityDerivativeApplication — an application of the
> RATE_OF_CHANGE mechanism, in which operation = DerivativeOperation, withRespectTo = Time.
> Therefore velocity is classified as a rate of change."

This path is a *structural explanation*: it shows which graph structure the answer adheres to.
But the epistemic boundary must be held (this distinction runs throughout the chapter, see
§9.12):

> **Path ≠ logical entailment.** A path shows the graph connects concepts in a certain way,
> within the traversed depth and with the chosen relations. It does not prove the relations are
> true of the world, nor that no opposing path exists.

One more distinction: a *structural path* differs from *entailment* (Ch5). Entailment is
deriving a consequence according to semantics; a path is a connectivity fact. Presenting a path
as "therefore" is valid; presenting it as "proven" overreaches.

**MUST NOT infer:**
- Do not present a path as an entailment.
- Do not assert the existence of a path ⇒ true.

## 9.55 Path Explosion

When a graph is large and densely connected, the number of paths between two nodes grows
exponentially. For example, within three hops of `VelocityDerivativeApplication`, paths run
through `DerivativeOperation`, `RATE_OF_CHANGE`, `Time`, `Position`, the superclass nodes, the
sources, the related claims — and each branching node opens further branches. This is **path
explosion**: enumerate every path and the context collapses.

This section lifts that phenomenon from an intuitive observation to a **quantitative
combinatorics** result you can actually compute, then presents two families of bounding
algorithms — *prioritization* (Personalized PageRank) and *minimal connection* (the Steiner
Tree approximation) — together with a law of **probabilistic error decay** that explains why
unconstrained traversal fails in production. The reader needs only basic linear algebra
(adjacency matrix, matrix powers) and elementary calculus (exponentiation, geometric series) —
both already used since Ch5.

### 9.55.1 The combinatorial mechanism: counting paths $O(\bar{d}^k)$

Let $\bar{d}$ be the graph's **average degree** — the average number of edges per node. A
uniform breadth-first expansion from an anchor node: each hop multiplies the current number of
paths by $\bar{d}$ choices for the next edge. The number of paths of length $k$ therefore grows as

$$N(k) \;=\; O\!\left(\bar{d}^{\,k}\right).$$

Read the formula in words: *"each hop multiplies the workload by $\bar{d}$; $k$ hops is
$\bar{d}$ multiplied by itself $k$ times."* This is **exponential growth in depth** — the same
nature as the $b^l$ of a hierarchical tree that Ch8 used to justify hyperbolic embeddings, the
only difference being that here it counts *paths* rather than *nodes*.

Table 9.3 shows how fast the explosion runs at three average-degree levels:

| $\bar{d}$ | $k=1$ | $k=2$ | $k=3$ | $k=4$ |
|---|---|---|---|---|
| 4 (sparse tree, mechanism subgraph) | 4 | 16 | 64 | 256 |
| 10 (medium-sized knowledge graph) | 10 | 100 | 1.000 | 10.000 |
| 50 (hub nodes like `Time`, `rdf:Resource`) | 50 | 2.500 | 125.000 | 6.250.000 |

In our running domain, `VelocityDerivativeApplication` has a local degree of ~5 (`operation`,
`differentiand`, `withRespectTo`, `produces`, `instanceOf`), so $k=3$ gives $\approx 5^3 = 125$
paths — still manageable. But it connects to `Time` and `RATE_OF_CHANGE`, which are **hub
nodes** with degrees in the thousands (every mechanism is `withRespectTo Time`). A single branch
that reaches a hub at hop 2 is enough to turn $k=4$ into millions of paths.

**Linear-algebra bridge.** The number of paths of length exactly $k$ from node $i$ to node $j$
equals the $(i,j)$ entry of the **adjacency-matrix power** $A^k$ (with $A_{ij}=1$ if there is an
edge $i\to j$). The total number of walks of length $\le k$ is

$$A + A^2 + \dots + A^k,$$

which is exactly the **transitive closure** that Ch5 taught when computing the fixpoint of the
operator $T_P$. Path explosion, seen through the lens of linear algebra, is simply the remark:
*the entries of $A^k$ grow exponentially with $k$ when $\bar{d}>1$.* This is not a metaphor — it
is the very same matrix multiplication.

![Path explosion $O(\bar{d}^k)$: from an anchor node, each hop multiplies the number of paths by the average degree; a branch that reaches a hub node (Time) at hop 2 makes the count explode at hops 3–4. It must be bounded by structural constraints and prioritization — it cannot be enumerated.](figures/generated/ch09-path-explosion.pdf)

### 9.55.2 Multi-hop probabilistic error cascading: $p^k$

Even if you *could* enumerate, each hop of a multi-hop path is a step that **can be wrong**:
entity linking at that hop, picking the right edge type, mapping the relation correctly. Let
$p_i\in(0,1]$ be the **precision** of hop $i$ — the probability that the hop is correct. If the
hops are independent, the probability that the *entire* $k$-hop path is correct is the product

$$P(\text{valid path}) \;=\; \prod_{i=1}^{k} p_i \;=\; p^{\,k}\quad(\text{if } p_i=p).$$

This is **exponential error decay** (probabilistic error cascading): each hop multiplies in
another factor $<1$, so the reliability of the path *falls very fast* with depth.

A numeric example on the chapter's Q0 path — `Velocity` $\to$ `VelocityDerivativeApplication`
$\to$ `RATE_OF_CHANGE` $\to$ `CurrentDerivativeApplication` $\to$ `ElectricCurrent` — with a
per-hop precision of $p=0.8$ (a fairly good retriever/entity-linker, *not* a perfect one):

| number of hops $k$ | $P=0.8^{\,k}$ | interpretation |
|---|---|---|
| 1 | 0.800 | one edge — acceptable |
| 2 | 0.640 | two edges — already lost more than a third of the reliability |
| 3 | 0.512 | **coin-flip territory** — a 3-hop path is right only ~50% of the time |
| 4 | 0.410 | a 4-hop path is *more likely wrong than right* |
| 5 | 0.328 | most 5-hop paths are wrong |

The crux: $0.8^3 = 0.512$ — a path whose *every hop is "fairly good"* is still only about half
right after three hops. This is why honest multi-hop retrieval **never presents a long path as a
proof** (§9.54): the accumulated probability has already destroyed the reliability before you
finish reading the path.

**MUST NOT infer from $p^k$:**
- Do not treat $p$ as a precisely measurable constant — it is a design estimate; the formula
  gives the *shape* of the decay (exponential), not a single number of truth.
- Do not assume the hops are independent when they are not (a wrong entity link at hop 1 usually
  drags hop 2 into error too — in which case the decay is *faster* than $p^k$).

### 9.55.3 Why unconstrained traversal fails — and bounding via symbolic constraints

The two laws above ($\bar{d}^k$ and $p^k$) combine to explain a classic production failure: a
vector/heuristic pipeline that "just keeps expanding the neighborhood and lets the model pick"
will (a) explode combinatorially at $\bar{d}^k$, and (b) even the surviving paths decay in
reliability at $p^k$. *Unconstrained* traversal — walking every edge type, every direction, every
node type — maximizes $\bar{d}$ at each hop.

The countermeasure is not "traverse more slowly" but **shrink $\bar{d}$ before traversing**, using
precisely the symbolic tools the book has built:

- **Ontology constraints (Ch4):** a `withRespectTo` edge is valid only between a
  `RateOfChangeMechanism` and a `Quantity`. The schema discards wrongly-typed edges outright,
  cutting the effective degree $\bar{d}\to\bar{d}'$ with $\bar{d}'\ll\bar{d}$.
- **SHACL shape checks (Ch5):** `sh:maxCount`, `sh:class`, `sh:nodeKind` prune branches that
  violate structural constraints *before* they are ever expanded — a semantically grounded
  pruning, not a scored heuristic.
- **Relation-aware traversal (§9.14):** traverse only the edge types that match the intent — this
  is exactly the $\bar{d}'$ chosen by policy.

> **Bounding path explosion is a semantics problem, not a speed problem.** The cheapest way not to
> traverse a million meaningless paths is to *know in advance* (from ontology + SHACL) that nine
> hundred ninety-nine thousand of them are wrongly typed — and never generate them. Vector
> similarity cannot do this: it ranks, it does not exclude by logical constraint.

### 9.55.4 Personalized PageRank: prioritizing instead of enumerating

When you cannot (and should not) enumerate every path, the second strategy is **prioritization**:
score each node's topological relevance to the question, then keep only the head of the list. The
standard tool is **Personalized PageRank (PPR)** — PageRank biased toward a seed set, rooted in
PageRank [@page-pagerank-1999] and Haveliwala's topic-sensitive PageRank [@haveliwala-ppr-2002].

**Intuition (random walk with restart):** imagine a "random walker" on the graph: at each step it
jumps to a random neighbor with probability $1-\alpha$, or **restarts** (teleports) back to the
seed set with probability $\alpha$. PPR is this walker's stationary distribution — the more
frequently a node is visited, the *closer* it is to the seeds topologically.

**Mechanism (matrix form):** let

$$\mathbf{p} \;=\; (1-\alpha)\,\tilde{A}\,\mathbf{p} \;+\; \alpha\,\mathbf{s},$$

with each symbol mapped onto the Q0 example:

- $\mathbf{s}\in\mathbb{R}^{n}$ — the **restart distribution** (restart/seed): mass 1 placed on
  the question's anchor entities. For Q0, $\mathbf{s}$ concentrates mass on
  `VelocityDerivativeApplication` (and `ElectricCurrent` if the question is comparative); the
  other coordinates are 0.
- $\tilde{A}$ — the **degree-normalized, column-stochastic transition matrix**:
  $\tilde{A}_{ij} = A_{ij}/\deg(j)$, the probability the walker steps from $j$ to neighbor $i$.
- $\alpha\in(0,1)$ — the **restart probability** (typically $0.1$–$0.2$): anchors the walker to
  the seeds, preventing it from drifting off to infinity.
- $\mathbf{p}$ — the **stationary distribution**: each node's topological relevance to the seeds.

**Computed by power iteration** (the very technique Ch8 used for embeddings):

$$\mathbf{p}^{(t+1)} = (1-\alpha)\,\tilde{A}\,\mathbf{p}^{(t)} + \alpha\,\mathbf{s},
\qquad \mathbf{p}^{(0)}=\mathbf{s},$$

iterating until $\|\mathbf{p}^{(t+1)}-\mathbf{p}^{(t)}\|$ falls below a threshold. Each round is a
sparse matrix–vector product, $O(|E|)$ — far cheaper than enumerating $O(\bar{d}^k)$.

**Linear-algebra bridge (why it converges):** unrolling the recursion gives the geometric series

$$\mathbf{p} \;=\; \alpha\left(I-(1-\alpha)\tilde{A}\right)^{-1}\mathbf{s}.$$

Because $\tilde{A}$ is column-stochastic (spectral radius $=1$), $(1-\alpha)\tilde{A}$ has
spectral radius $1-\alpha<1$; the map $\mathbf{p}\mapsto(1-\alpha)\tilde{A}\mathbf{p}+\alpha\mathbf{s}$
is a **contraction**, so a fixed point exists, is unique, and power iteration converges to it —
the same fixed-point theorem that guaranteed Ch5 halts at the closure.

**PPR penalizes hub nodes naturally.** This is the decisive property for path explosion: because
$\tilde{A}_{ij}=1/\deg(j)$, a high-degree node (like `Time`, connected to *every* mechanism)
**spreads** its mass evenly across thousands of neighbors, so each neighbor receives only a tiny
fraction. Topologically near seeds (the `RATE_OF_CHANGE` mechanism, the sibling application
`CurrentDerivativeApplication`) receive concentrated mass. The result: PPR *automatically* pushes
hubs to the bottom of the list and lifts the relevant local subgraph to the top — exactly what we
need to cut $\bar{d}^k$ without a hard degree threshold.

**Worked example (Q0):** $\mathbf{s}$ concentrated on `VelocityDerivativeApplication`,
$\alpha=0.15$. After convergence, the head of the list contains `RATE_OF_CHANGE` (1 hop),
`CurrentDerivativeApplication` (2 hops, sharing the mechanism), `DerivativeOperation`, `Position`,
`Velocity`. `Time` — despite being only 1 hop away — is pushed deep down because
$\deg(\text{Time})$ is very large. PPR both *prioritizes* the correct mechanism subgraph and
*cuts* the hub branch that causes the explosion.

### 9.55.5 Steiner Tree: the minimum connecting subgraph (2-approximation)

PPR prioritizes *nodes*. But many questions need a **connected subgraph** that minimally joins a
*set* of query entities — for instance Q0 needs to connect `Velocity`, `ElectricCurrent`, and
`RATE_OF_CHANGE` with the fewest edges / least weight. This is precisely the **Steiner Tree in
Graphs** problem: given a weighted graph $G=(V,E)$ with weights $w$ and a **terminal** set
$T\subseteq V$, find the minimum-weight subtree containing all of $T$ (allowed to use intermediate
nodes not in $T$ — the Steiner nodes).

**Hardness (Karp 1972):** Steiner Tree in Graphs is one of the 21 **NP-complete** problems in
Karp's classic list [@karp-reducibility-1972]. Consequence: no polynomial-time algorithm yields
the exactly optimal solution unless $\mathrm{P}=\mathrm{NP}$. This is a *theoretical* boundary,
not an implementation limit — it applies to every GraphRAG system.

**The 2-approximation algorithm** (metric closure + minimum spanning tree, MST):

1. **Metric closure:** compute the shortest path between *every pair* of terminals (all-pairs
   shortest path, Floyd–Warshall or Dijkstra from each terminal). Build the complete graph $G_T$
   on $T$, each edge $(u,v)$ carrying weight $d(u,v)$ = the shortest distance in $G$. $G_T$
   satisfies the **triangle inequality** (hence *metric*).
2. **Minimum spanning tree:** compute the MST of $G_T$ (Prim or Kruskal), $O(|T|^2\log|T|)$.
3. **Expansion:** replace each MST edge $(u,v)$ with its corresponding original shortest path in
   $G$; take the union of these paths → a connected subgraph spanning all of $T$.

**Approximation guarantee:** the resulting weight $\le 2\times$ the optimal Steiner weight. (Short
proof: the MST of the metric closure $\le$ the weight of the optimal Steiner tree "walked around"
the terminals; expanding each shortest edge at most doubles the length in the worst case.) This is
a *proven upper bound*, not a lucky heuristic.

**Worked example (Q0):** $T=\{\text{Velocity},\ \text{ElectricCurrent},\ \text{RATE\_OF\_CHANGE}\}$.

- Metric closure (counting hops, each edge weight 1):
  $d(\text{Velocity},\text{RATE\_OF\_CHANGE})=2$ (via `VelocityDerivativeApplication`);
  $d(\text{ElectricCurrent},\text{RATE\_OF\_CHANGE})=2$ (via `CurrentDerivativeApplication`);
  $d(\text{Velocity},\text{ElectricCurrent})=4$ (via both applications + the mechanism).
- The MST of $G_T$ picks the two shortest edges:
  $\{\text{Velocity}\!-\!\text{RATE\_OF\_CHANGE}\ (2),\ \text{ElectricCurrent}\!-\!\text{RATE\_OF\_CHANGE}\ (2)\}$,
  total $4$ (dropping the weight-$4$ edge, which would form a cycle).
- Expansion → a subgraph of `RATE_OF_CHANGE`, the two intermediate applications (Steiner nodes),
  and the four `produces`/`instanceOf` edges. This is exactly the *minimally sufficient subgraph*
  of §9.16, now chosen by an algorithm with a guaranteed approximation factor rather than by eye.

**Honest caveat:** Steiner minimizes **connection weight**, not **meaning**. A "short" edge by hop
count is not necessarily the decision-bearing route by intent (§9.14) — a 2-hop path through a
wrongly-typed relation is still "short." So in the chapter's pipeline, Steiner runs *after* the
ontology/SHACL constraints have removed wrongly-typed edges (§9.55.3), so that the weights reflect
length over the *valid* edge set.

### 9.55.6 The chapter's countermeasures (synthesis)

Five countermeasures, ordered by the sequence in which they should be applied (BOOK-DEFINED):

1. **Bound via symbolic constraints (§9.55.3):** ontology (Ch4) + SHACL (Ch5) shrink the effective
   degree $\bar{d}\to\bar{d}'$ *before* traversal — the cheapest and strongest countermeasure;
2. **Structural bounds (§9.13):** maximum depth $k$, relation types, node types, max branching —
   cutting $\bar{d}'^k$ from the start;
3. **Prioritize with PPR (§9.55.4):** when nodes must be ranked by topological relevance, use
   $\mathbf{p}=(1-\alpha)\tilde{A}\mathbf{p}+\alpha\mathbf{s}$ — self-penalizes hubs, lifts the
   local subgraph;
4. **Connect with the Steiner approximation (§9.55.5):** when a subgraph joining many terminals is
   needed, use metric closure + MST (factor 2), run over the filtered edge set;
5. **Prioritize decision paths + structural de-duplication:** *one* decision path (one that answers
   the intent) is worth *a thousand* incidental paths; keep the decision path, merge the rest
   (counter-paths are handled in §9.27); drop repeated-role or cyclic paths that add no information.

**MUST NOT infer:**
- Do not claim to have enumerated "every path" (the $O(\bar{d}^k)$ explosion is a real property of
  the graph, not an implementation bug).
- Do not claim the chosen path is the "uniquely correct" one — it is only the decision path under
  the retrieval policy.
- Do not read a PPR score as a probability of correctness or an epistemic confidence (it is a
  topological ranking signal, §9.60).
- Do not claim the Steiner approximation yields the *optimal* subgraph (it gives a $\le 2\times$
  bound; the underlying problem is NP-complete [@karp-reducibility-1972]).
- Do not ignore the $p^k$ decay when presenting a long multi-hop path as a firm conclusion (§9.54).

## 9.56 Community / Hierarchical Retrieval

On a large graph, one strategy for global questions is to **cluster and then summarize by level**:
detect communities (the original GraphRAG uses Leiden) and generate bottom-up summaries for each
community [@edge-graphrag-2024] [@microsoft-graphrag-docs]. Global retrieval then map-reduces over
these summaries to answer questions about the whole.

Four risks must be managed:

1. **Information loss in summaries:** a summary compresses away detailed evidence;
2. **Unstable communities:** when the graph changes by a few claims, the clustering can jump
   wholesale — the global answer changes even though the content barely did;
3. **Stale summaries:** an old summary no longer reflects the current graph;
4. **Lost provenance:** the reader can hardly trace "where did this summary come from."

The policy (continuing §9.33): a community summary is a **derived artifact with
provenance** — model/version/source — it is a *candidate input*, not canonical knowledge. A summary
must never be silently promoted to truth.

**MUST NOT infer:**
- Do not claim community summaries are a mandatory component of every GraphRAG.
- Do not claim a summary is complete.
- Do not inject a summary into the canonical KG without going through governance.

## 9.57 Cache and index consistency

A system can **cache** many things: entity-resolution results, retrieval results, chosen
subgraphs, summaries, and even answers. Caching cuts cost but introduces **staleness**, because the
knowledge system keeps evolving (§9.10). Policy (BOOK-DEFINED):

- A cache key where accuracy matters must bind the **version** of: the KG/Ledger snapshot, the
  index version, the ontology version, the retriever version;
- A cached answer must carry a label for the point in time of the system state it reflects;
- When the Ledger changes (a new claim / Superseded), the related cache must be invalidated or
  flagged.

**MUST NOT infer:**
- Do not claim a cached answer reflects current knowledge.
- Do not serve a stale cache as though it were fresh state.

## 9.58 Retrieval & Answer Provenance

**Retrieval provenance** records *why this fragment was handed to the model*: the original
question, the interpretation, the retrievers and their versions, the index snapshot, the filters,
top_k, the scores, the re-ranker, the expansion rules, the time. Enough to reproduce and debug.

The **Answer artifact** (BOOK ENGINEERING MODEL — PROV-O [@prov-o]) records:

```
Answer
  └─ generatedFor → Question
  └─ usedEvidence → EvidencePacket
  └─ generatedBy → AnswerGenerationActivity
  └─ generatedAt → time
  └─ modelVersion / promptConfigVersion
  └─ citations → (answer claim ↔ source passage)
  └─ answerStatus → SUPPORTED | PARTIAL | CONTESTED | ABSTAINED | UNKNOWN
```

These two kinds of provenance are *reproducible* facts, not evidence of correctness: a perfect
record can still be the record of a wrong answer (cell B, §9.42).

**MUST NOT infer:**
- Do not claim retrieval provenance proves correctness.
- Do not claim a logged score is the answer's confidence.
- Do not declare an answer audit-able when there is no retrieval record.

## 9.59 QA Answer ≠ Knowledge Ingestion

This is one of the most important governance boundaries in the entire book:

> **An answer from a QA system does not automatically become newly accepted knowledge.**

The correct process takes the form of a loop:

```
KG/policy → retrieval → answer → (if a new candidate knowledge is discovered)
  → CandidateClaim → Ch7 integration pipeline (assessment, evidence, governance)
  → (if Accepted) → only then into the Ledger
```

A shortcut loop `answer -> insert into KG` that bypasses governance is forbidden. The reason: an
answer is the product of an error-prone pipeline (retrieval miss, wrong source, LLM fabrication);
feeding it straight into the KG *freezes error as knowledge* and opens a self-reinforcing loop
(recall model collapse — Ch8 §8.34 makes the same point at the system level).

**MUST NOT infer:**
- Do not infer "the system can answer" ⇒ "the system knows it."
- Do not insert an answer into the KG while skipping governance.
- Do not claim an Answer is an Accepted Claim (they are two different record types).

## 9.60 Score semantics, multi-signal ranking, and the three epistemic states

**Score semantics.** In a retrieval process there are many kinds of score: BM25 (a lexical ranking
utility), cosine/dot-product (an embedding signal), a re-ranker score (a learned ranking utility),
graph distance (structural), rule priority. The one boundary that must hold:

> **Every score in the retrieval pipeline is a ranking signal — none of them is the probability
> that the answer is correct.**

**Multi-signal ranking (BOOK-DEFINED).** When several signals are combined to judge relevance, the
combination is a *policy tailored to the problem*: text match, embedding similarity, graph
distance, relation type, governance status, validity time, source quality, and evidence diversity
may all be combined — but there is no universal weighting formula. The chapter's rule: state the
combination policy openly, do not pretend at a magic constant.

**Three epistemic states (mandatory).** Each item in the Evidence Packet carries a label:

- **ASSERTED** — asserted from a source / the Ledger (with an identified source);
- **DERIVED** — derived by sound inference under the semantics (Ch5), from asserted premises;
- **PREDICTED** — predicted by a learned model (Ch8), a candidate, carrying a score.

These three levels must not be blended: an answer that writes "current is inversely proportional
to resistance" (predicted) must read differently from one that writes "current is modeled as a
derivative with respect to time" (asserted+derived). The state is recorded in the answer artifact
(§9.58) so the reader can tell the levels of trust apart.

**MUST NOT infer:**
- Do not claim predicted = asserted.
- Do not claim derived = asserted with respect to the world.
- Do not present a prediction as an accepted fact.
- Do not store a retrieval score as the answer's "confidence."

---

# Part H — Evaluation, worked cases, and boundaries

## 9.61 Evaluating retrieval in seven tiers

Evaluating a question-answering system with a single end-to-end number is the most common mistake:
it does not tell you which tier the error lives in. This chapter teaches evaluation **by tier**
(BOOK-DEFINED):

| Tier | What it measures | Metric / check |
|---|---|---|
| 1. Entity linking | mention → correct entity? | accuracy on an ambiguous/hard set |
| 2. Retrieval | is the relevant unit in top_k? | P@K, R@K, MRR, nDCG (§9.30) |
| 3. Evidence sufficiency | does the packet contain every important answer claim? | gold-evidence check (§9.62) |
| 4. Grounding | is each answer supported by the packet? | AIS-style assessment [@rashkin-ais-2021] |
| 5. Correctness | correct with respect to the world? | external assessment (human/expert) |
| 6. Citation | citation recall/precision? | ALCE metrics [@gao-cite-2023] |
| 7. Boundary behavior | how it handles contradiction/unknown? | tests in §9.63 |

Each tier has its own instrument; a system can score 100% on tier 2 and fail badly on tier 4 (right
evidence, wrong synthesis). Conversely, a system that fails on tier 2 drags down every later tier —
tier-by-tier diagnosis is the only way to know what to fix.

**MUST NOT infer:**
- Do not infer good retrieval metrics ⇒ good answers.
- Do not claim a single number can identify the failing tier.

## 9.62 Gold Evidence and the QA benchmark

**Gold evidence** is the annotated set of "which units should be retrieved for this question" —
the equivalent of a relevance judgment in IR [@manning-ir-2008]. For question Q0:

```
gold_evidence(Q0) = {
  structural: VelocityDerivativeApplication, CurrentDerivativeApplication,
              RATE_OF_CHANGE, the operation/differentiand/withRespectTo/produces roles,
  claims:     claim Accepted "Velocity = derivative application of RATE_OF_CHANGE",
              the counter-claim (if any),
  passages:   the source passage defining velocity + derivative with respect to time
}
```

It is used to measure tiers 2–3 (§9.61): how much of the gold did the system retrieve?

The chapter's **QA benchmark** is a set of questions tied to the system's knowledge, each with: an
intent, gold evidence, a gold answer (following cell C of the 2×2 table — *correct and grounded*),
and adversarial variants (§9.63).

**Commitment caveat:** gold evidence is the *dataset's annotation*, not a transcendent truth. It can
be wrong, incomplete, or stale — like any human assessment. Scoring against gold measures *agreement
with the annotation*, not *truth*.

**MUST NOT infer:**
- Do not treat gold annotation as infallible.
- Do not infer a score against gold ⇒ correctness with respect to the world.

## 9.63 Adversarial tests: distractors, contradiction, time

Beyond the standard benchmark, a system needs **adversarial tests** — deliberately planted traps to
probe the epistemic boundaries (BOOK-DEFINED, continuing Ch8's hard-negative concept
[@karpukhin-dpr-2020]):

1. **Distractor test:** insert surface-similar but irrelevant/wrong-direction passages into the
   store — does the system get fooled into selecting them? (measures precision / synthesis
   robustness);
2. **Contradiction test:** ask about a topic with competing claims — does the system retrieve both
   sides and present the contradiction, or just pick one? (§9.27);
3. **Temporal test:** ask about a past state — does the system use the right clock, or answer with
   the present? (§9.25);
4. **Absence test:** ask about something that does not exist — does the system abstain or
   fabricate? (§9.43);
5. **Top_k test:** place the decisive evidence just outside top_k — does the system stay
   "suspiciously stable," or does it correctly report missing evidence? (§9.29).

A system that passes the benchmark but fails these tests looks brilliant in the lab and breaks in
the real world.

**MUST NOT infer:**
- Do not infer passing the benchmark ⇒ robustness (adversarial tests are mandatory).
- Do not claim a single test covers every boundary.

## 9.64 The full worked case: 15 steps over RATE_OF_CHANGE

Now we run the whole system through the chapter's central question:

> **Q0:** "Why are velocity and electric current regarded as the same RATE_OF_CHANGE mechanism, and
> what evidence supports that?"

**Step 1 — Interpretation (question interpretation, §9.3).** Intent: EXPLANATORY + COMPARATIVE
(requests the shared structure + evidence). Mentions: "velocity", "electric current",
"RATE_OF_CHANGE".

**Step 2 — Entity linking (§9.5).** "velocity" → `Velocity` (score 0.93, unambiguous); "electric
current" → `ElectricCurrent` (0.91, unambiguous in the electronics context); "RATE_OF_CHANGE" →
`rate:RATE_OF_CHANGE` (0.98). Noted: no significant ambiguity.

**Step 3 — Decomposition (§9.7).** Q1/Q2 (each side's structure), Q3 (the comparison roles), Q4
(Accepted claim), Q5 (contradiction), Q6 (synthesis).

**Step 4 — Planning (§9.8).** The router chooses: Graph-first hybrid — structural query + ledger +
text; the plan table as in §9.8.

**Step 5 — Structural query (KGQA, §9.11).** SPARQL fetches the 2 applications + roles:
`VelocityDerivativeApplication instanceOf RATE_OF_CHANGE; operation DerivativeOperation;
differentiand Position; withRespectTo Time; produces Velocity` — and likewise for
`CurrentDerivativeApplication` (differentiand = ElectricCharge, produces = ElectricCurrent).
Result: 2 structural paths that match exactly on operation/withRespectTo.

**Step 6 — Ledger lookup for Q4 (§9.23).** Ledger query: Accepted claims about the mechanism
correspondence between the two concepts → claim `C471` with Evidence `E88` (source passage) and an
assessment.

**Step 7 — Ledger lookup for Q5 (§9.27).** Ledger query for Contested/Superseded claims on the same
topic → `C210` ("the derivative is only a model; velocity has its own definitional essence", status
Contested, scope: philosophy of physics).

**Step 8 — Text retrieval (§9.17–9.18).** BM25 + dense on the query "velocity derivative with
respect to time electric current" → top-10 passages; RRF rank fusion; keep top-5 after re-ranking.

**Step 9 — Evidence assessment (§9.28).** Filter: keep 3 independent source passages, 1
counter-passage, drop 2 same-source duplicates. Check gold coverage: 5/5 gold groups present —
sufficient.

**Step 10 — Assemble the packet (§9.32–9.36).** Close the **Evidence Packet**: the question, intent,
entities, 2 structural paths, C471 (asserted), C210 (contested, scoped), 3 source passages
(asserted source), the provenance chain E88→fragment→book, temporal scope "current", retrieval
metadata (top_k=5, depth=2, retriever version 2.1). Order: structural paths at the head of the
window, the contradiction at the tail (§9.34).

**Step 11 — Generate the answer (§9.37–9.38).** The LLM drafts 4 answer claims A1–A4 (§9.38),
clearly separating what is supported, what is inferred, and what is unknown.

**Step 12 — Citation (§9.40).** A1→C471+E88; A2→the roles table (derived from structure); A3→labeled
"inferred from C471 + structure" + a note that C210 objects; A4→abstention.

**Step 13 — Self-check (§9.67).** Reconcile each sentence against the packet: no answer claim lies
outside the packet; A3 is indeed an inference and is labeled so; the contradiction is presented on
both sides.

**Step 14 — Answer artifact (§9.58).** Answer artifact: generatedFor Q0, usedEvidence = the packet,
answerStatus = SUPPORTED_WITH_CONTESTATION (because of C210), full citations.

**Step 15 — Answer and record.** The user receives an answer with: (1) the shared structure;
(2) the evidence; (3) the opposing view and its scope; (4) what is unknown. The QA answer is NOT
inserted into the KG (§9.59); if the answer surfaces a new claim → CandidateClaim → Ch7.

**The lesson of the worked case:** every step can be wrong in its own way; a good answer is not the
"most natural" answer but the answer *whose every step can be re-checked*.

## 9.65 Failure cases: when the system is wrong

Three classic failure cases, each illustrating one of the chapter's boundaries.

**Case A — "Faithful to a wrong source" (cell B, §9.42).**

- Scenario: a stale index (§9.10). The Ledger Superseded the old definition at 09:00; the index was
  rebuilt at 10:00. The user asks at 09:30 "what is current?".
- What happens: the retriever (following the process correctly) returns the old-definition passage;
  the LLM (faithful to the packet) answers correctly according to the old passage; citations are
  complete. Every step is "right," the answer is wrong.
- Diagnosis: an index-consistency error — not an LLM error, not a query error.
- Lesson: the system must report the index snapshot in provenance (§9.58) and have a staleness
  detector before answering time-sensitive questions.

**Case B — "The user did not say what they meant" (misinterpretation, §9.3).**

- Scenario: the user asks "How do velocity and speed differ?" A simple FACTUAL intent, but in fact
  they are arguing about a contradictory claim in the Ledger.
- What happens: the system answers with the standard definitional comparison; the user finds it
  meaningless.
- Diagnosis: the interpretation missed the information need; it may also be an ambiguous intent that
  was never re-asked.
- Lesson: interpretation must record ambiguity (§9.3) and the system is allowed to re-ask rather than
  guess (§9.43).

**Case C — "Proof by path" (path abuse, §9.54).**

- Scenario: the system answers "velocity is a rate of change because the path
  Velocity→produces→VelocityDerivativeApplication→instanceOf→RATE_OF_CHANGE" while saying nothing
  about C210 (the Contested counter-claim).
- What happens: the path is graph-correct; the answer is presented as a proof.
- Diagnosis: one-sided retrieval (confirmation bias §9.49), a missing Q5 step; presenting a path as
  an entailment (§9.54).
- Lesson: a path is a structural fact; the answer must include the opposing side, and the word
  "therefore" is valid only when a claim + supporting assessment exist, not merely because an edge
  exists.

## 9.66 A taxonomy of hallucination and the self-check

**Hallucination** is defined narrowly in this chapter's context: *an assertion about the world not
supported by the issued Evidence Packet* (not "wrong" in general — a true statement that lies
outside the packet is still uncontrolled behavior, cell A §9.42). Four types (BOOK-DEFINED):

1. **Relation fabrication:** asserting a relation not in the packet — e.g. "velocity and electric
   current share a `differentiand`" (false: the differentiands differ);
2. **Entity/number fabrication:** introducing a number/unit not in the packet;
3. **Misattribution:** citing a passage that does not actually support the sentence (a citation
   precision error [@gao-cite-2023]);
4. **False certainty:** writing the unknown as the known — "there is no other mechanism" when the
   search was not exhaustive (the unknown cell §9.44).

**The self-check** is step 13 of the worked case: before release, the system reconciles each answer
claim against the packet and labels the result: `SUPPORTED` / `PARTIALLY_SUPPORTED` / `UNSUPPORTED`
/ `CONTESTED`. This is a **valuable automated check layer**, but it must be honest about its limits:
*the reconciliation is itself performed by a model and can also be wrong*. It reduces risk, it does
not eliminate it.

**MUST NOT infer:**
- Do not infer a passing self-check ⇒ a correct answer (it can still be cell B).
- Do not infer that every ungrounded sentence is false with respect to the world.

## 9.67 Claim–Evidence Alignment

A more detailed checking technique: for each answer claim, find the *item in the packet* that
supports it and classify it:

| Alignment result | Meaning | Action |
|---|---|---|
| SUPPORTED | a packet item supports it directly | keep as-is, cite it |
| PARTIALLY_SUPPORTED | only part of the claim is supported | narrow the claim or add evidence |
| UNSUPPORTED | no item supports it | drop the claim or mark it as inference |
| CONTESTED | the packet holds a weighty opposing claim | present both sides + status |

Alignment is a *process check*: it does not prove a claim correct with respect to the world, but it
forces the system to *state plainly* the relation between its words and its evidence
[@rashkin-ais-2021] [@gao-cite-2023].

**MUST NOT infer:**
- Do not claim a passing alignment ⇒ a correct answer.
- Do not skip the alignment layer because "it's only a model too."

## 9.68 Graph reasoning vs LLM reasoning

A comparison of the two "reasoning engines" in the system (BOOK-DEFINED, synthesized from the
chapters):

| Aspect | Graph reasoning (symbolic) | LLM reasoning |
|---|---|---|
| Premises | triples in the KG, semantic rules (Ch4–5) | text in the context window |
| Inference step | determined by semantics (entailment) | probabilistic per the model |
| Reproducibility | anyone can re-derive it | not fully reproducible |
| Characteristic errors | wrong/incomplete KG, wrong rules | hallucination, focus drift, lost-in-middle |
| Provenance trail | natural (every triple has provenance) | needs a separate citation layer |
| Strength | precise, premises explainable | flexible, natural phrasing |

The architectural conclusion: **not replacement, but assignment.** Structural questions → graph
reasoning (KGQA); open/synthetic questions → the LLM over the evidence packet. Where the boundary is
blurred — for instance "which mechanism" between two concepts — let the graph do the *structural
decision* part and the LLM do the *phrasing* part, with the structural path as a re-checkable
premise.

**MUST NOT infer:**
- Do not claim the LLM "reasons" identically to graph reasoning.
- Do not claim the graph can replace the LLM for open questions.

## 9.69 What GraphRAG does not guarantee

We gather the limits built up throughout the chapter into one focused statement:

**GraphRAG (or any RAG pipeline) does not guarantee:**

1. **Correctness** — a wrong/stale source ⇒ a "by-the-process" but wrong answer (cell B);
2. **Completeness** — index lag, top_k, depth: things outside the retrieval boundary are not
   "known";
3. **Freedom from hallucination** — the citation/self-check layers reduce risk, they do not remove
   it;
4. **New knowledge** — an answer does not become accepted knowledge on its own;
5. **Semantics** — the graph *organizes* retrieval, it does not *supply* correct meaning: a wrong
   entity link, a wrong claim, a noisy community all pass straight through into the answer;
6. **Fairness / certainty level** — a score is not a probability of correctness.

A good GraphRAG system is one that *knows what it does not guarantee*: it reports status, abstains
when evidence is missing, and makes every step re-checkable.

## 9.70 When NOT to Use RAG

Symmetric to §8.37 of the previous chapter: there are questions that should never pass through RAG or a generative LLM.

**Do not use RAG when:**

1. **A precise query is enough** — entities + attributes + schema are known in advance: SPARQL answers exactly, cheaply, and verifiably (KGQA);
2. **You need authoritative, exact facts** — figures, regulations, governed definitions: answer straight from the Canonical View, without going through text generation;
3. **Hallucination risk is unacceptable** — audits, legal: a generative answer must come with strong abstention, or you do not use a generative LLM at all;
4. **The question is outside the system's knowledge** — a domain with no sources: answering "out of scope" beats RAG "finding something roughly related";
5. **Cost/latency outweighs the benefit** — a FAQ that is already indexed does not need an LLM on every query;
6. **Absolute reproducibility is mandatory** — an LLM cannot reproduce exactly the same output: use a symbolic path.

**Reverse diagnosis:** if a question *should* have had a symbolic path but the system still went through RAG, that is a router error (§9.71), not "RAG being more powerful".

### 9.70.1 GraphRAG versus 1M–2M-token long context windows: the Pareto frontier

All of the items above assume we have *already* chosen between RAG and a symbolic query. But there is a third question — hotter this year for practitioners — and it must be answered head-on:

> **"Why should I go to the trouble of building GraphRAG — entity linking, ontology, graph retrieval — when Gemini 1.5 Pro or Claude 3.5 Sonnet already support a 1–2 million token context window, enough for me to *dump the entire raw corpus* straight in and ask?"**

This is not the "RAG vs KGQA" question (§9.53) but **"raw long context vs structured retrieval"**. Answering it on instinct — "long context solves everything" or "the graph is always right" — is wrong either way. The honest answer is a **Pareto frontier**: each option wins on some axes and loses on others, and the optimal operating point *shifts* with corpus size, question type, and audit requirements.

**Four trade-off axes.** Table 9.4 puts the two architectures head to head (BOOK-DEFINED, synthesized from the limits built up across the chapter):

| Axis | Dump everything into long context (Long-Context) | GraphRAG (subgraph retrieval) |
|---|---|---|
| **Per-query complexity & cost** | Self-attention is $O(N^2)$ in the length $N$; KV-cache memory and latency grow linearly–quadratically in $N$. Dumping $N$ million tokens *every time you ask* = paying for $N$ *every time*. | Extracts a compact subgraph, $O(1)$–$O(\lvert E\rvert)$ in the *question*, not in corpus size. The tokens fed to the model are small and nearly constant even as the corpus balloons. |
| **Reliability under long context** | **"Lost in the middle"** (§9.34): the model uses the start/end more reliably than the middle; burying the decisive fact among hundreds of thousands of tokens degrades quality markedly [@liu-lostmid-2023]. | The linking path is **explicitly handed up** into the packet, ordered for the decision (§9.32); there is no giant "middle" for facts to be buried in. |
| **Relational & epistemic precision** | The model *generates* a probabilistic answer and can fabricate links absent from the documents (cell D, §9.42); no record says "this was accepted". | Answers are **anchored to Claim Ledger IDs** (C471 vs C210) with explicit governance status (`Accepted`/`Contested`) and temporal validity (§9.23–9.25); relational hallucination is blocked by the packet's constraints (§9.37). |
| **Global sensemaking across the whole corpus** | A flat prompt cannot reliably answer *holistic* questions: "what mechanism pattern recurs across 10,000 articles?" — there is no place in one window to "read it all then summarize". | GraphRAG's **Global Search** uses hierarchical community detection (Leiden/Louvain) + precomputed community summaries, then map-reduce over them to synthesize global themes [@edge-graphrag-2024] (§9.51, §9.56). |

**Calculus / linear-algebra bridge for the cost axis.** The cost of self-attention over $N$ tokens is $O(N^2)$ because every token is matched against every other token — $N\times N$ dot products $\mathbf{q}_i\cdot\mathbf{k}_j$ (exactly the vector multiplication Ch8 taught). Multiplying $N$ by 10 raises the per-query cost ~100-fold. GraphRAG replaces $N$ (the size of the *corpus*) with $\lvert E_{\text{sub}}\rvert$ (the size of the *subgraph relevant to the question*), which does not grow with the corpus. This is the difference between a function of the **data** and a function of the **question** — the same kind of trade-off that made the index valuable in §9.10.

**When Long-Context wins (positive ROI for dumping straight in):**

- The corpus is **small-to-medium** and fits entirely in the window within the allowed token budget;
- Questions are **exploratory, open-ended**, and you do not yet know what structure you need;
- **Rapid prototyping**: you do not yet want to invest in an ontology + entity linking;
- The documents are **pure text, low-relation** — there is no multi-hop structure to exploit;
- The requirement is **whole-document reading** (summarize a 200-page contract) — which is *real* long context, not retrieval.

**When GraphRAG is mandatory (Long-Context gives negative ROI):**

- **Multi-hop cause–effect reasoning** — long relation chains where $p^k$ (§9.55.2) and $\bar{d}^k$ (§9.55.1) make "read it all then guess" both inaccurate and uneconomical;
- **Regulatory compliance / audit** — every assertion must trace to a Claim ID + governance status + provenance (Compartments 2–3 of the Evidence Packet, §9.36); long context cannot hold that invariant;
- **Contradictory / time-scoped claims** — you need to retrieve *both sides* with their scope (§9.27) and on the correct clock (§9.25); flat dumping blends them uncontrollably;
- **High throughput, production** — $O(N^2)$ per query on a large corpus is unaffordable in cost and latency;
- **Global sensemaking** — "across the whole corpus" questions that only community structure + precomputed summaries can answer [@edge-graphrag-2024].

**The Pareto principle (BOOK-DEFINED):** there is no "absolute winner". There is an **ROI boundary** that depends on three variables — corpus size, the relational depth of the question, and the audit requirement. When all three are low, long context wins because its build cost is zero. When any one is high, GraphRAG starts to pay back its build cost. A mature system often uses **both**: GraphRAG retrieves the *structured* subgraph, then feeds the serialized subgraph (§9.35) into the LLM's long window to synthesize — long context is the *generation layer*, not the *retrieval layer*.

![The Pareto frontier of GraphRAG vs Long-Context: the two axes of per-query cost and epistemic precision; the Pareto curve joins the optimal operating points. Long-context wins in the small-corpus/open-question region; GraphRAG wins in the multi-hop/audit/global region.](figures/generated/ch09-pareto-graphrag.pdf)

**MUST NOT infer:**
- Do not claim the long window "solves everything" about retrieval — it moves the cost into $O(N^2)$ and into mid-window reliability (§9.34); it does not eliminate them.
- Do not claim GraphRAG is always better than long context — for a small corpus and open questions, the graph-build cost is negative ROI.
- Do not treat window length (1M, 2M tokens) as evidence for the *quality* of context use — "can be stuffed in" ≠ "is used reliably" (§9.34).
- Do not present Table 9.4 as a permanent verdict — it is a Pareto frontier, and the optimum shifts with hardware and models.

## 9.71 The Query Execution Router (BOOK-DEFINED)

This gathers the whole chapter into a single decision. The **router** (introduced in §9.8) is the central component of the question-answering system — BOOK ENGINEERING MODEL — whose input is the interpreted question and whose output is the execution path plus the Evidence Packet:

```
                  ┌─────────── intent/entities/decomposition ───────────┐
                  ▼                                                      │
        ┌─ clear entities + known schema + structural intent ──► KGQA (SPARQL/graph) ──┐
        │                                                                              │
        ├─ needs consequence inference ────────────────────────► Symbolic reasoning ───┤
        │                                                                              │
Router ─┼─ ambiguous entities / open question / definition ────► Text RAG (BM25+dense) ┤
        │                                                                              │
        ├─ structure + textual evidence ───────────────────────► GraphRAG / hybrid ────┤
        │                                                                              │
        └─ history / contradiction / provenance ───────────────► Ledger retrieval ─────┘
                                  │
                                  ▼
                        Evidence Packet (BOOK-DEFINED)
                                  ▼
                        Answer Generation + citation + self-check
                                  ▼
                        Answer artifact (full provenance)
```

Figure 9.7 draws this router. Operating principle: **the most precise path that suffices to answer wins**; ambiguity falls down to a more flexible tier; every path ends at the Evidence Packet so the generation and check layers work over a single interface.

![The Query Execution Router (BOOK-DEFINED): from the intent it selects the KGQA/reasoning/text-RAG/GraphRAG/ledger path; every path closes into an Evidence Packet before an answer with citations and a provenance record is generated.](figures/generated/ch09-query-router.pdf)

**MUST NOT infer:**
- Do not claim the router's choice is the truth.
- Do not claim generative text beats a precise query when the precise query suffices.

## 9.72 Common Misconceptions

Thirty-four misconceptions this chapter directly refutes — each points back to the section that explained it:

1. "If it was retrieved then it can be answered" — retrieved ≠ evidence (§9.28, §9.37).
2. "A high retrieval score means it is surely correct" — score semantics (§9.60).
3. "BM25 understands semantics" — it is only term matching (§9.17).
4. "Identical embeddings mean identical meaning" — vector ≠ meaning (§9.18).
5. "Dense retrieval always beats lexical" — the two families are strong in different ways (§9.19).
6. "More signals means more correct" — hybrid reduces misses, it does not increase truth (§9.20).
7. "top_k is just an implementation detail" — it is an epistemic boundary (§9.29).
8. "Not in the top_k means it does not exist" — OWA (§9.29, §9.44).
9. "The index is the knowledge" — index ≠ KG (§9.10).
10. "Answering from the Ledger is the same as answering from the projection" — two different epistemic domains (§9.23).
11. "For a history question, use the current state" — multiple clocks (§9.25).
12. "A path exists, therefore it is proven" — path ≠ proof (§9.12, §9.54).
13. "The deeper the traversal the better" — the depth limit is also a boundary (§9.13).
14. "Within k hops means relevant" — k-hop ≠ relevance (§9.15).
15. "A summary can replace the source" — summary ≠ source (§9.33, §9.56).
16. "Context compression loses nothing" — compression can discard the decisive evidence (§9.33).
17. "Context order does not matter" — lost in the middle (§9.34).

18. "A full evidence packet means sufficient evidence" — packet ≠ sufficiency (§9.36).
19. "Grounded means correct" — grounded ≠ true (cell B) (§9.39, §9.42).
20. "A fluent answer is a correct answer" — fluency ≠ correctness (§9.37).
21. "It has a citation, therefore it is supported" — citation precision (§9.40).
22. "Many citations means good citations" — citation recall/completeness (§9.40).
23. "Faithful means correct" — faithfulness ≠ correctness (§9.41).
24. "Not found → does not exist" — unknown vs not found (§9.44).
25. "An answer error → a knowledge error" — retrieval failure ≠ knowledge absence (§9.44).
26. "Abstention is a failure" — abstention can be correct behavior (§9.43).
27. "A GraphRAG system is one standard algorithm" — a family, not a standard (§9.52).
28. "KGQA = GraphRAG" — different mechanisms (§9.53).
29. "GraphRAG can replace KGQA for precise questions" — decision table (§9.53).
30. "GraphRAG eliminates hallucination" — not guaranteed (§9.69).
31. "A QA answer automatically becomes new knowledge" — not without governance (§9.59).
32. "An LLM can replace graph reasoning" — two different machines (§9.68).
33. "A path is a proven bridge" — path explosion hides the alternatives (§9.55).
34. "Every question needs RAG" — when NOT to use RAG (§9.70).

## 9.73 Self-explanation Checkpoints

Eight questions for the reader to check that they have grasped the chapter's boundaries. There is no single answer — there is a reasoned answer.

1. The question "What is the definition of current in 2020?" needs to retrieve from which domain: the projection or the Ledger? Why?
2. Suppose BM25 ranks passage A first with score 12.3 and passage B second with score 12.1. Can you conclude "the system is 0.2 units more confident A is correct than B"? Why not?
3. top_k=5, and the decisive evidence for your question sits at rank 6. What will the answer look like, and at which layer is the system "wrong" (per the 7 layers of §9.61)?
4. A GraphRAG community summary says "all three phenomena are one mechanism". Is it evidence? What is it missing to become evidence?
5. Distinguish asserted/derived/predicted for the statement "velocity is the rate of change": which group does it belong to if it comes (a) from a rule? (b) from the Ledger? (c) from a learned model?
6. Cell B of the 2×2 table (faithful to a wrong source) — why does "the process ran correctly" not turn cell B into cell C?
7. Agentic retrieval adds a 4th and 5th retrieval round, each "successful". Why might the answer still be poor — name three failure mechanisms (§9.46–9.50)?
8. If Q0 answers "no mechanism other than RATE_OF_CHANGE governs velocity" — what epistemic label should this statement get (§9.60)? Why?

### 9.73.1 Suggested answers

**Checkpoint 1.** The question "What is the definition of current in 2020?" needs to retrieve from which domain: the projection or the Ledger? Why?

It must retrieve from the **Ledger (Claim Ledger)**, not the projection (Canonical View). "What is the definition of current in 2020?" is a TEMPORAL question — it asks about a past state, not the current state.

Reason: the projection keeps only one answer — "what is *currently* accepted" — so querying it would return the *current* definition of `ElectricCurrent`, answering in the wrong temporal category. §9.23 calls this precisely "the classic violation: answering a *history/dispute* question from the current projection." The intent table in §9.4 (row 6, TEMPORAL) prescribes the priority source as "the Ledger by valid/publication time", and §9.23 repeats: "history/dispute questions must go to the Ledger." One more subtle layer: even within the Ledger you must pick the right clock (§9.25) — "the definition *in effect* in 2020" is valid time, "*published* in 2020" is publication time, "the system *believed* in 2020" is system time; these three clocks are independent and must not be blended.

Evidence: §9.4 (the 9-intent table, TEMPORAL row), §9.23 (the two retrieval domains and the MUST NOT "empty projection ⇒ empty Ledger"), §9.25 (multiple time clocks).

**Checkpoint 2.** Suppose BM25 ranks passage A first with score 12.3 and passage B second with score 12.1. Can you conclude "the system is 0.2 units more confident A is correct than B"? Why not?

No. The 0.2 score gap must not be interpreted as a difference in confidence or correctness.

Reason: the BM25 score is a *ranking utility*, not a probability of being correct, not an absolute confidence. §9.17 says it plainly: "Scores are a *ranking utility*, not a probability of correctness. The score gap between rank 1 and rank 2 is a relative ranking signal, not an absolute confidence." So "A beats B by 0.2 units" is meaningless: the BM25 scale has no content units, and 0.2 on that scale maps to no "correctness" difference. This principle is generalized in §9.60: "Every score in the retrieval pipeline is a ranking signal — no score is the probability that the answer is correct." The same logic applies to the RRF score (§9.21) and the re-ranker score (§9.31). A practical consequence: BM25 can also rank A higher merely because A repeats many rare query terms, even when B is the passage that actually answers correctly — a high score cannot rule out a "right words, wrong reasoning" passage.

Evidence: §9.17 (BM25 score semantics), §9.60 (score semantics), §9.21 (RRF is not confidence), §9.30 (metrics do not measure correctness).

**Checkpoint 3.** top_k=5, and the decisive evidence for your question sits at rank 6. What will the answer look like, and at which layer is the system "wrong" (per the 7 layers of §9.61)?

The answer will be *fluent and "plausible" but missing half the truth* — the model synthesizes over exactly what it sees (the top-5) and has no idea the rank-6 piece exists.

Reason: §9.29 raises exactly this scenario: "For an explanatory question, the outcome changes entirely if the decisive evidence sits at rank 6 while top_k=5," and "top_k too small → decisive evidence lost → a 'plausible' answer missing half the truth." This is a consequence of the "context window ≠ knowledge" principle (§9.1): the correct claim *is* in the Ledger/KG but was not put into the packet. Per the 7-layer table of §9.61, the error lies at **layer 2 (Retrieval)** — "is the relevant unit in the top_k?" — and immediately propagates down to **layer 3 (Sufficient evidence)** because the packet is missing the decisive sub-claim; §9.61 notes "a system that fails at layer 2 drags down every subsequent layer." Importantly: this is **not** a layer-5 (correctness) error or a knowledge error — §9.44 distinguishes sharply "retrieval failure ≠ knowledge absence"; misdiagnosing it leads to pouring in more data when the problem is the top_k configuration. Reranking (§9.31) cannot save it either, because "reranking cannot save recall."

Evidence: §9.29 (top_k is an epistemic bound), §9.61 (7 layers, layer 2→3), §9.44 (retrieval failure ≠ knowledge absence), §9.31 (rerank does not save recall).

**Checkpoint 4.** A GraphRAG community summary says "all three phenomena are one mechanism". Is it evidence? What is it missing to become evidence?

No, on its own it is **not evidence**. It is a *derived artifact* — a candidate input, not yet standard knowledge.

Reason: §9.33 sets the principle "A summary is a derived artifact — not a source," and §9.56 applies it to GraphRAG specifically: "a community summary is a **derived artifact carrying provenance** of model/version/source — it is a *candidate input*, not standard knowledge." §9.9 also classifies the "community summary" unit as "compact" but "weak because: compression loses evidence." To become evidence, it lacks: (1) a **provenance chain** back to the real source passages (§9.26: Claim→Evidence→SourceFragment→SourceArtifact) — which model/version generated this summary, from which fragments; (2) the **underlying evidence units** it compresses (structural path + claim + source passage, §9.9, §9.28); (3) an **epistemic status label** asserted/derived/predicted (§9.60, the `statuses` field of the Evidence Packet §9.36) — a sentence "three phenomena are one mechanism", if produced only by an LLM summary, is at most *predicted* and must not be presented as asserted; (4) **governance**: it has not passed through Ch6/Ch7 to become an Accepted claim (§9.59), and it carries no competing claims/counterexamples (§9.27, §9.50).

Evidence: §9.33 (summary ≠ source), §9.56 (community summary is a candidate), §9.9 (the summary unit compresses away evidence), §9.26 (the provenance chain), §9.60/§9.36 (status labels), §9.59 (QA ≠ knowledge).

**Checkpoint 5.** Distinguish asserted/derived/predicted for the statement "velocity is the rate of change": which group does it belong to if it comes (a) from a rule? (b) from the Ledger? (c) from a learned model?

Three sources give three different statuses, and they must not be blended (§9.60).

Reason: §9.60 defines the three labels. (a) **From a rule** (sound inference under the semantics, Ch5): the statement is **DERIVED** — "entailed by sound inference under the semantics (Ch5), premises are asserted"; it is true *within the graph* because validly derived from the premises, but "derived ≠ asserted about the world" (§9.60 MUST NOT). (b) **From the Ledger** (a claim with a definite source, status Accepted): the statement is **ASSERTED** — "asserted from a source/Ledger (with a definite source)"; this is what the governed system holds to be true, with provenance (§9.23, §9.26). (c) **From a learned model** (Ch8): the statement is **PREDICTED** — "predicted by a learned model (Ch8), is a candidate, carries a score"; it is only an unvalidated hypothesis and must not be written as a fact. The key point: the same wording, from three different sources, demands three presentations and three levels of confidence; the `statuses` field of the Evidence Packet (§9.36) is exactly where this label is recorded so the generation layer does not blend them.

Evidence: §9.60 (the three statuses asserted/derived/predicted and the MUST NOT), §9.36 (the packet's `statuses` field), §9.23/§9.26 (the Ledger = asserted source).

**Checkpoint 6.** Cell B of the 2×2 table (faithful to a wrong source) — why does "the process ran correctly" not turn cell B into cell C?

Because "the process ran correctly" only guarantees the **grounded/faithful** axis, whereas cell B is determined by the **true-to-the-world** axis — two independent axes, so doing one well does not move the cell across to the other.

Reason: §9.42 defines cell B as "faithful to a wrong source" and states clearly: "the system 'followed the process correctly' — retrieved, assembled, cited fully — yet is still wrong because the source is wrong. **A good process does not turn cell B into cell C**; only external evaluation (users, cross-checking) can." Cell C requires *true to the world* **and** *grounded*; a correct process delivers only the "grounded" part. This connects to two foundational distinctions: faithfulness is a property of the *answer–context* pair (§9.41), groundedness is a property of the *answer–source* pair, not the *answer–world* pair (§9.39). Failure case A in §9.65 illustrates it numerically: a stale index returns a Superseded definition, the LLM faithfully summarizes it, cites it fully — "every step 'correct', the answer wrong." This is exactly the methodological warning that opens the chapter: "the process having run does not mean the answer is correct" (§9.1).

Evidence: §9.42 (the 2×2 table, cell B, the MUST NOT "use a correct process to conclude correctness"), §9.41 (faithfulness ≠ correctness), §9.39 (grounded ≠ true), §9.65 Case A, §9.1.

**Checkpoint 7.** Agentic retrieval adds a 4th and 5th retrieval round, each "successful". Why might the answer still be poor — name three failure mechanisms (§9.46–9.50)?

Because "successful" is only the success *of each round locally*, not *global progress toward the correct answer*. Three mechanisms:

Reason: (1) **Query drift (§9.48)** — each round's subquery veers further from the original intent; the chapter's example: round 1 "the RATE_OF_CHANGE mechanism" → round 3 "derivatives in finance" → round 4 "successfully" retrieves a passage on financial derivatives, "entirely far from the original intent, yet every step is locally valid." (2) **Confirmation bias (§9.49)** — later rounds only reinforce the previous round's hypothesis; §9.46 notes "later rounds usually only reinforce earlier ones," so adding rounds = adding one-sided confidence, not = adding truth ("Supporting evidence ≠ truth"). (3) **Non-convergence / stopping because the budget ran out, not because evidence was sufficient (§9.47)** — "most stopping conditions only guarantee the *process stops*, not that *evidence is sufficient*"; if rounds 4–5 run until tokens are exhausted, the result is "insufficient due to budget," not "sufficient." Accompanying this is escalating noise and cost (§9.46).

Evidence: §9.46 (the agentic risk table), §9.47 (stopping conditions), §9.48 (query drift), §9.49 (confirmation bias).

**Checkpoint 8.** If Q0 answers "no mechanism other than RATE_OF_CHANGE governs velocity" — what epistemic label should this statement get (§9.60)? Why?

It must **not** be labeled asserted (nor derived, nor predicted as a positive assertion). The honest label is **UNKNOWN / abstention** — an unverified negation, not a truth.

Reason: §9.60 gives only three *positive* statuses (asserted/derived/predicted); this statement is an **existential negation** ("no other mechanism exists") that no source asserted, no rule derived, and no learned model predicted. It matches exactly claim A4 in §9.38: "No other mechanism governs velocity. — **unknown** (not exhaustively searched), must not be written as a fact." The basis: the system only searches within the depth bound and top_k, and "no results beyond depth d" ⇏ "no results" (§9.13) and "not in the top_k" ⇏ "does not exist" (§9.29); per the OWA of Ch4, "absent from the KG" ≠ "false" (§9.44, status 3). The chain in §9.44 ("NOT RETRIEVABLE ≠ ... ≠ UNKNOWN") forces the system to say it is in the "not found/unknown" state, not the "known false" state. Writing this statement as a fact is exactly the "false certainty" hallucination type (§9.66, type 4); the correct behavior is abstention (§9.43).

Evidence: §9.60 (the three positive statuses), §9.38 (A4 = unknown), §9.44 (five statuses, OWA), §9.13/§9.29 (depth/top_k bounds), §9.66 (false certainty), §9.43 (abstention).

## 9.74 Experiment Backlog

Nine proposed experiments but **DEFERRED TO BOOK V0.1** — outside the chapter's theoretical scope, requiring real data, a real system, and evaluation datasets:

- **EXP-9-1:** (DEFERRED) Build a RATE_OF_CHANGE benchmark of ≥40 questions (≥4 per intent), with gold evidence + gold answer for each; measure the 7 layers (§9.61).
- **EXP-9-2:** (DEFERRED) Compare BM25 vs dense vs hybrid on the system's own text corpus — P@K/R@K/MRR/nDCG against the gold of EXP-9-1.
- **EXP-9-3:** (DEFERRED) Measure the top_k impact: fix one question, move the decisive evidence to rank 1..10, observe answer quality (verifying §9.29).
- **EXP-9-4:** (DEFERRED) Verify lost-in-the-middle on the model in use: same packet, change the order, measure stability (§9.34).
- **EXP-9-5:** (DEFERRED) Build the adversarial test suite (§9.63): distractor, contradiction, temporal, absence, top_k; run it periodically on the real pipeline.
- **EXP-9-6:** (DEFERRED) Measure agentic vs static effectiveness on multi-step questions: quality, number of rounds, cost; check stopping conditions (§9.46–9.47).
- **EXP-9-7:** (DEFERRED) Install a GraphRAG implementation (e.g. Microsoft GraphRAG) on the system's corpus; measure Local/Global on the EXP-9-1 benchmark; record community instability (§9.56).
- **EXP-9-8:** (DEFERRED) Measure staleness: after Superseding a claim, track the probability the system still answers from the old claim under different cache/index configurations (§9.10, §9.57).
- **EXP-9-9:** (DEFERRED) Test the router (§9.71): compare the rate of "precise questions taking the wrong RAG path" when using a rule-based vs an LLM planner, recording cost.

## 9.75 Chapter Depth Audit

The chapter's main concepts and the minimum committed depth (rubric 1–6, from "mentioned" to "analyzed and synthesized in multiple contexts"):

| Main concept | Section | Depth | Main concept | Section | Depth |
|---|---|---|---|---|---|
| Question Interpretation | §9.3 | 4 | Symbolic Graph Retrieval | §9.11 | 5 |
| Query Intent (9 types) | §9.4 | 4 | Multi-hop Retrieval | §9.12 | 4 |
| Query Entity Linking | §9.5 | 4 | Path Bounds | §9.13 | 4 |
| Intent ≠ Identity | §9.6 | 4 | Relation-aware Traversal | §9.14 | 4 |
| Query Decomposition | §9.7 | 4 | k-hop Neighborhood | §9.15 | 4 |
| Retrieval Plan | §9.8 | 4 | Subgraph Retrieval | §9.16 | 4 |
| Retrieval Unit | §9.9 | 4 | BM25 | §9.17 | 5 |
| Index ≠ KG | §9.10 | 4 | Dense Retrieval (DPR) | §9.18 | 4 |
| Query Embedding ≠ Meaning | §9.18–9.19 | 4 | Hybrid Retrieval | §9.20 | 4 |
| Rank Fusion (RRF) | §9.21 | 5 | Graph-first vs Text-first | §9.22 | 4 |
| Canonical View vs Claim Ledger | §9.23 | 5 | Governance-aware Retrieval | §9.24 | 4 |
| Temporal Retrieval (clocks) | §9.25 | 4 | Provenance-aware Retrieval | §9.26 | 4 |
| Contradiction-aware Retrieval | §9.27 | 4 | Evidence Diversity | §9.28 | 4 |
| top_k as Epistemic Bound | §9.29 | 5 | Precision/Recall | §9.30 | 4 |
| P@K / R@K | §9.30 | 4 | MRR / nDCG | §9.30 | 4 |
| Reranking | §9.31 | 4 | Context Assembly | §9.32 | 4 |
| Context Compression | §9.33 | 4 | Lost in the Middle | §9.34 | 4 |
| Graph Serialization | §9.35 | 4 | Evidence Packet | §9.36 | 5 |
| Answer Generation | §9.37 | 4 | Answer Claims | §9.38 | 4 |
| Grounded Answer | §9.39 | 5 | Citation (completeness) | §9.40 | 4 |
| Faithfulness | §9.41 | 4 | Correctness × Groundedness 2×2 | §9.42 | 5 |
| Abstention | §9.43 | 4 | Unknown vs Not Found | §9.44 | 5 |
| Query Planning | §9.45 | 4 | Static vs Agentic | §9.46 | 4 |
| Stopping Conditions | §9.47 | 4 | Query Drift | §9.48 | 4 |
| Confirmation Bias | §9.49 | 4 | Hypothesis-testing Retrieval | §9.50 | 4 |
| Local vs Global | §9.51 | 4 | GraphRAG (family) | §9.52 | 5 |
| RAG vs KGQA vs GraphRAG | §9.53 | 5 | Path as Explanation | §9.54 | 4 |
| Path Explosion | §9.55 | 4 | Community Retrieval | §9.56 | 4 |
| Caching / Index Consistency | §9.57 | 4 | Retrieval & Answer Provenance | §9.58 | 4 |
| QA Answer ≠ Ingestion | §9.59 | 5 | Score Semantics / 3 statuses | §9.60 | 5 |
| 7-layer Retrieval Evaluation | §9.61 | 5 | Gold Evidence / Benchmark | §9.62 | 4 |
| Adversarial Tests | §9.63 | 4 | End-to-end 15-step Case | §9.64 | 6 |
| Failure Walkthroughs | §9.65 | 5 | Hallucination Taxonomy | §9.66 | 4 |
| Claim–Evidence Alignment | §9.67 | 4 | Graph vs LLM Reasoning | §9.68 | 4 |
| GraphRAG Limits | §9.69 | 4 | When NOT to use RAG | §9.70 | 4 |
| Query Execution Router | §9.71 | 5 | | | |

## 9.76 Reader Capability Test (Q01–Q56)

Requirement: **Q01–Q56 all = YES**. If any answer is NO, re-read the section it points to before continuing.

| # | I can... | Section |
|---|---|---|
| Q01 | ...distinguish information need, query, document | §9.3 |
| Q02 | ...list the 9 intent types and the priority retrieval source for each | §9.4 |
| Q03 | ...perform generation/scoring/decision for an ambiguous mention | §9.5 |
| Q04 | ...explain why intent and identity are two independent ambiguity axes | §9.6 |
| Q05 | ...decompose a complex question and draw the dependency graph of its sub-questions | §9.7 |
| Q06 | ...write a retrieval plan with order, bounds, and stopping condition | §9.8 |
| Q07 | ...choose the retrieval unit by question type | §9.9 |
| Q08 | ...explain index ≠ KG and the consequence of a lagging index | §9.10 |
| Q09 | ...write a simple SPARQL query and state its limits correctly | §9.11 |
| Q10 | ...tell why a multi-hop path is not a proof | §9.12 |
| Q11 | ...design a depth limit and explain why it is an epistemic boundary | §9.13 |
| Q12 | ...choose the traversal edge type by intent | §9.14 |
| Q13 | ...explain why k-hop ≠ relevance | §9.15 |
| Q14 | ...justify the policy-based minimally-sufficient subgraph (not a mathematical optimum) | §9.16 |
| Q15 | ...write the BM25 formula and explain idf, k1, b | §9.17 |
| Q16 | ...explain the dual encoder and the meaning of the dot product | §9.18 |
| Q17 | ...explain query vector ≠ query meaning | §9.18 |
| Q18 | ...discuss when lexical beats dense and vice versa | §9.19 |
| Q19 | ...explain that hybrid reduces misses but does not increase truth | §9.20 |
| Q20 | ...compute the RRF of a document from 2 systems | §9.21 |
| Q21 | ...choose graph-first or text-first by intent | §9.22 |
| Q22 | ...explain projection vs Ledger and choose the right domain by intent | §9.23 |
| Q23 | ...design a filtering policy by governance status | §9.24 |
| Q24 | ...distinguish the three time clocks and choose the right one | §9.25 |
| Q25 | ...draw the provenance chain Claim→Evidence→Source and explain that it does not prove correctness | §9.26 |
| Q26 | ...retrieve competing claims with their scope when asking about a disputed topic | §9.27 |
| Q27 | ...explain why many passages from the same source are not many pieces of evidence | §9.28 |
| Q28 | ...explain that top_k is an epistemic boundary and its consequences | §9.29 |
| Q29 | ...compute P@K, R@K, MRR, nDCG for a concrete example | §9.30 |
| Q30 | ...explain why retrieval metrics do not measure correctness | §9.30 |
| Q31 | ...explain that re-ranking cannot save recall | §9.31 |
| Q32 | ...design context assembly (select, group, order, label) | §9.32 |
| Q33 | ...explain that a summary is a derived artifact, not a source | §9.33 |
| Q34 | ...explain lost-in-the-middle and apply it when ordering the packet | §9.34 |
| Q35 | ...trade off between the graph serialization forms | §9.35 |
| Q36 | ...list the fields of the Evidence Packet and why it is an interface | §9.36 |
| Q37 | ...explain the 4 disciplines of the answer generation layer | §9.37 |
| Q38 | ...decompose an answer into sub-claims and label each | §9.38 |
| Q39 | ...explain grounded ≠ correct | §9.39 |
| Q40 | ...explain citation recall vs precision | §9.40 |
| Q41 | ...explain faithfulness ≠ correctness | §9.41 |
| Q42 | ...place an answer into one of the 4 cells of the 2×2 table | §9.42 |
| Q43 | ...list the 6 abstention conditions and state the type of deficiency | §9.43 |
| Q44 | ...distinguish the 5 "not found" statuses and retrieval failure vs knowledge absence | §9.44 |
| Q45 | ...design agentic retrieval with a stopping condition and query-drift detection | §9.46–9.48 |
| Q46 | ...explain confirmation bias and hypothesis-testing retrieval | §9.49–9.50 |
| Q47 | ...distinguish local vs global questions and choose a strategy | §9.51 |
| Q48 | ...explain that GraphRAG is a family of architectures, not a standard | §9.52 |
| Q49 | ...use the KGQA/RAG/GraphRAG decision table for a concrete question | §9.53 |
| Q50 | ...explain that a path is an explanation, path explosion, and the limits of GraphRAG | §9.54–9.55, §9.69 |
| Q51 | ...list the fields of the Answer artifact (answer provenance) and the meaning of each | §9.58 |
| Q52 | ...explain why a QA answer does not automatically become KG knowledge | §9.59 |
| Q53 | ...distinguish the epistemic statuses asserted / derived / predicted | §9.60 |
| Q54 | ...explain the role of precise symbolic reasoning in QA | §9.68 |
| Q55 | ...present the entire RATE_OF_CHANGE QA flow from question to answer | §9.64 |
| Q56 | ...name the open problems Chapter 10 must solve | §9.79 |

## 9.77 End-of-Chapter Competence Ladder

At the end of this chapter, the reader (and the system) reach the following competence rungs:

1. **Recognize** — know the concepts: intent, entity linking, decomposition, BM25, DPR, RRF, nDCG, Evidence Packet, faithfulness, abstention, agentic, GraphRAG, KGQA, router.
2. **Distinguish** — do not confuse retrieved ≠ evidence, index ≠ KG, grounded ≠ correct, faithful ≠ correct, path ≠ proof, not found ≠ does not exist.
3. **Analyze** — from a question, decompose into the 9 intent types, choose a retrieval strategy, design an Evidence Packet, point out the risks (depth, top_k, query drift, confirmation bias, lost-in-the-middle).
4. **Synthesize** — run the 15-step working case, design a router, build the KGQA/RAG/GraphRAG decision table, construct an adversarial test suite, evaluate across 7 layers.
5. **Critique** — detect one-sided evidence, confirmation bias, query drift, lost provenance, and distinguish cell B from cell C of the 2×2 table.

## 9.78 Chapter Summary

Chapter 9 opened the **retrieval and question-answering rung** — the knowledge system's new IO comprises three layers: understanding the question, retrieval (structure + text + epistemology), and generating the answer. The through-line principles:

- **Nine intent types** — each determines the retrieval source and the type of evidence.
- **Index ≠ KG** — a lagging index, wrong retrieval, wrong answer even when the process is "correct".
- **top_k is an epistemic boundary** — the model only reasons over the evidence it sees.
- **Evidence Packet (BOOK-DEFINED)** — the single interface between retrieval and the generation layer.
- **The 2×2 table (correct × grounded)** — grounded ≠ true; faithfulness ≠ correctness.
- **GraphRAG is a family of architectures** — not one standard algorithm; KGQA, RAG, and GraphRAG complement each other, they do not replace each other.
- **A QA answer ≠ ingested knowledge** — no shortcut that bypasses governance.
- **Three statuses** — asserted, derived, predicted — never blended.
- **The 15-step end-to-end flow** — every step can be wrong; a verifiable answer is the goal.

## 9.79 Bridge to Chapter 10

Chapter 9 closes the question-answering part over existing knowledge. Chapter 10 — **System Governance and Operation** — expands into operational questions: how does the system monitor its own growth? How does it detect staleness, feedback loops, accumulating contradiction? How does it measure knowledge quality over time? Governing the lifecycle not only for each claim (Ch6) but for the whole system. Chapter 10 begins there — and leaves open questions for the reader who wants to build a real system, the most important of which is: **a knowledge system is never "done" — it must be measured, maintained, and trusted in a controlled way.**

## Terms encountered in this chapter

| Term | Short meaning | More in |
|---|---|---|
| Question interpretation | Mapping a natural question to a structured form | §9.3 |
| Query intent | The intent class (9 types) | §9.4 |
| Entity linking | Linking query mentions to entities | §9.5 |
| Query decomposition | Splitting a complex question | §9.7 |
| Retrieval plan | The ordered retrieval plan | §9.8 |
| Retrieval unit | The unit a retrieval step returns | §9.9 |
| Search index | The retrieval index | §9.10 |
| Symbolic retrieval | Exact-pattern retrieval (SPARQL) | §9.11 |
| Multi-hop retrieval | Retrieval across multiple hops | §9.12 |
| Path bound / depth limit | The traversal depth limit | §9.13 |
| k-hop neighborhood | The neighborhood within k hops | §9.15 |
| Subgraph retrieval | Retrieving a coherent subgraph | §9.16 |
| BM25 | The lexical ranking function | §9.17 |
| Dense retrieval / Dual encoder | Vector retrieval / the dual encoder | §9.18 |
| Hybrid retrieval | Combining lexical and dense | §9.20 |
| Reciprocal Rank Fusion (RRF) | Rank-based fusion | §9.21 |
| Graph-first / Text-first | Graph-first vs text-first ordering | §9.22 |
| Canonical View | The projection (currently accepted state) | §9.23 |
| Claim Ledger | The Ledger of claims (history, complete) | §9.23 |
| Governance-aware retrieval | Retrieval filtered by governance | §9.24 |
| Temporal retrieval | Retrieval over time (multiple clocks) | §9.25 |
| Provenance-aware retrieval | Retrieval that carries provenance | §9.26 |
| Contradiction-aware retrieval | Retrieval sensitive to contradiction | §9.27 |
| Evidence diversity | Diversity of evidence | §9.28 |
| Epistemic bound | An epistemic boundary | §9.29 |
| P@K, R@K, MRR, nDCG | The retrieval metrics | §9.30 |
| Reranking | Re-ranking retrieved units | §9.31 |
| Context assembly | Assembling the context | §9.32 |
| Context compression | Compressing the context | §9.33 |
| Lost in the middle | The mid-window information-loss effect | §9.34 |
| Graph serialization | Serializing the graph for an LLM | §9.35 |
| **Evidence Packet** | **The evidence packet (BOOK-DEFINED)** | §9.36 |
| Answer generation | Generating the answer | §9.37 |
| Answer claim | A sub-claim within the answer | §9.38 |
| Grounded answer | An answer grounded in sources | §9.39 |
| Citation | A citation | §9.40 |
| Citation completeness | Completeness of citations | §9.40 |
| Faithfulness | Faithful (to the context) | §9.41 |
| Correctness | Correct (about the world) | §9.42 |
| Abstention | Declining to answer | §9.43 |
| Query planning | Planning the query | §9.45 |
| Agentic retrieval | Iterative / agent-driven retrieval | §9.46 |
| Stopping condition | The condition to stop | §9.47 |
| Query drift | Drift of the question | §9.48 |
| Confirmation bias | Confirmation bias | §9.49 |
| Hypothesis-testing retrieval | Retrieval that tests a hypothesis | §9.50 |
| Local vs Global question | Local vs global questions | §9.51 |
| GraphRAG | The family of graph-based RAG architectures | §9.52 |
| KGQA | Knowledge-graph question answering | §9.53 |
| Path explanation | Explanation along a path | §9.54 |
| Path explosion | The combinatorial path explosion | §9.55 |
| Community retrieval | Retrieval over communities | §9.56 |
| Answer provenance | The answer's provenance record (BOOK-DEFINED) | §9.58 |
| Score semantics | The semantics of scores | §9.60 |
| Asserted / Derived / Predicted | The three epistemic statuses | §9.60 |
| Gold evidence | The reference (gold) evidence | §9.62 |
| **Query Execution Router** | **The query router (BOOK-DEFINED)** | §9.71 |

## Further reading

- Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (Lewis et al., NeurIPS
  2020) [@lewis-rag-2020]
- Dense Passage Retrieval for Open-Domain Question Answering (Karpukhin et al., EMNLP
  2020) [@karpukhin-dpr-2020]
- From Local to Global: A Graph RAG Approach (Edge et al., 2024) [@edge-graphrag-2024]
- Microsoft GraphRAG Documentation [@microsoft-graphrag-docs]
- The Probabilistic Relevance Framework: BM25 and Beyond (Robertson & Zaragoza, 2009)
  [@robertson-bm25-2009]
- Introduction to Information Retrieval (Manning, Raghavan & Schutze, 2008)
  [@manning-ir-2008]
- Cumulated gain-based evaluation of IR techniques (Jarvelin & Kekalainen, 2002)
  [@jarvelin-ndcg-2002]
- Reciprocal rank fusion (Cormack, Clarke & Buettcher, 2009) [@cormack-rrf-2009]
- Passage Re-ranking with BERT (Nogueira & Cho, 2019) [@nogueira-rerank-2019]
- Lost in the Middle (Liu et al., 2024) [@liu-lostmid-2023]
- Measuring Attribution in Natural Language Generation Models (Rashkin et al., 2021)
  [@rashkin-ais-2021]
- Enabling Large Language Models to Generate Text with Citations (Gao et al., 2023)
  [@gao-cite-2023]
- Introduction to Neural Network based Approaches for KGQA (Chakraborty et al., 2019)
  [@chakraborty-kgqa-2019]
- Unifying Large Language Models and Knowledge Graphs (Zhu et al., 2023)
  [@zhu-llmkg-2023]

