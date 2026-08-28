# ⛔ SUPERSEDED — DO NOT EXECUTE

**This file is superseded as of 2026-08-28.**

The Deep Readability Closure (Chapters 1–3) must be completed and accepted BEFORE
Chapter 4 begins. See the active work specification in the conversation context or
in `docs/BOOK_DEEP_READABILITY_CHECKPOINT.md` once created.

Do NOT start Chapter 4 until the Go/No-Go for Chapter 4 is explicitly reported.

---

# Original content below (retained for historical reference only)

You are continuing an existing repository from a NEW Claude Code session on a NEW machine.

Do not rely on any memory from previous sessions.

The Git repository is the source of truth.

Repository:

https://github.com/MinhTuan76800310/knowledge_graph_learning-journey

The last known accepted checkpoint is commit:

`645f429`

At that checkpoint:

* Book Preview v0.2 is complete
* Front matter is ACCEPTED
* Chapter 1 is ACCEPTED
* Chapter 2 is ACCEPTED
* Chapter 3 is ACCEPTED
* Glossary is ACCEPTED
* Bibliography is ACCEPTED
* print + screen PDFs contain 53 pages
* Chapter 4 is NOT_STARTED
* labs are secondary and deferred until Book v0.1

The PRIMARY project goal remains:

> Produce a high-quality, complete, printable Knowledge Graph book before completing the hands-on labs.

BOOK QUALITY > LAB COMPLETENESS.

Semantic correctness remains non-negotiable.

---

# 0. NEW-MACHINE ONBOARDING

First establish the actual repository state.

If the repository is not present:

```bash
git clone https://github.com/MinhTuan76800310/knowledge_graph_learning-journey.git
cd knowledge_graph_learning-journey
```

If it already exists:

```bash
git remote -v
git fetch origin
git switch main
git pull --ff-only origin main
```

Then run:

```bash
git rev-parse --short HEAD
git status
```

The current remote should contain commit `645f429` or a descendant of it.

Do NOT reset or discard newer work if HEAD is ahead of that commit.

Do NOT begin writing yet.

Read these repository documents first:

```text
CLAUDE.md
AGENTS.md

docs/BOOK_V0_1_MILESTONE.md
docs/BOOK_STATUS.md
docs/CHAPTER03_BOOK_CHECKPOINT.md
docs/LAB_BACKLOG.md

docs/source_index.json
docs/SOURCE_MATRIX.md
docs/CITATION_MAP.md
docs/RESEARCH_LOG.md

book/introduction.md
book/chapter01.md
book/chapter02.md
book/chapter03.md
book/references.bib
book/book-manifest.yaml
book/metadata.yaml

scripts/build_book.sh
scripts/verify_book_pdf.sh
Makefile
```

Understand the existing writing style, citation conventions, PDF pipeline, diagram numbering, callout conventions, glossary style, and source-ID discipline.

Do not redesign these systems without a real defect.

Run the current baseline before modifying anything:

```bash
uv sync
uv run pytest
uv run ruff check .
uv run ruff format --check .
make book-check
```

Record the baseline results privately for comparison.

If the PDF toolchain has new-machine dependencies that are missing, install/document only the minimum required system dependencies needed by the existing repository.

Do not change publishing technology merely because this machine is new.

---

# 1. CURRENT WORK SLICE

This work slice has exactly one manuscript target:

# Chapter 4 — Ontologies and Formal Meaning

Vietnamese title:

# Chương 4 — Bản thể học và Ngữ nghĩa Hình thức

Complete Chapter 4 as publication-quality book prose.

Then produce:

**Book Preview v0.3**

containing:

* front matter
* Introduction
* Chapters 1–4
* Glossary
* Bibliography

Then STOP.

Do NOT begin Chapter 5.

Do NOT resume deferred labs.

Do NOT perform Neo4j/Docker work.

---

# 2. CENTRAL QUESTION

Chapter 3 ended with:

Schema tells us expected structure.

But schema alone cannot formally express things such as:

* two classes are disjoint
* two classes have the same extension
* a class is defined by necessary and sufficient conditions
* a property is transitive or symmetric
* membership in a class follows logically from other assertions

Chapter 4 must answer:

> What does it mean to give concepts and relationships FORMAL MEANING, such that a machine can determine what must logically follow?

The chapter must NOT be organized around memorizing OWL vocabulary.

Its central mechanism is:

```text
Vocabulary + Axioms
        |
        v
Formal Semantics
        |
        v
Possible Interpretations
        |
        v
Models that satisfy the ontology
        |
        v
Entailment:
what is true in EVERY model?
```

This is the conceptual heart of Chapter 4.

A reader who finishes the chapter should finally understand what phrases such as:

* "formal semantics"
* "model"
* "interpretation"
* "entailment"
* "necessary condition"
* "sufficient condition"

actually mean.

---

# 3. SOURCE-FIRST RESEARCH

Before drafting Chapter 4, audit/fetch authoritative sources.

Prefer existing source IDs if already registered.

Do NOT create duplicate IDs for the same source.

Required primary sources:

## OWL 2 official W3C family

Research:

1. OWL 2 Document Overview
2. OWL 2 Primer
3. OWL 2 Structural Specification and Functional-Style Syntax
4. OWL 2 Direct Semantics
5. OWL 2 Profiles

OWL 2 Direct Semantics is CRITICAL for this chapter.

If it is not currently registered in `source_index.json`, add it using one new canonical source ID.

Do not silently alias it to the RDF-Based Semantics source.

Also understand that OWL 2 has:

* Direct Semantics
* RDF-Based Semantics

Do NOT imply there is only one OWL semantics.

For the pedagogical formal model in this chapter, use the Direct Semantics / OWL 2 DL viewpoint because it provides a clean model-theoretic explanation.

Clearly state that this is a deliberate pedagogical focus, not the whole OWL universe.

## Academic backbone

Use:

* Hogan et al., *Knowledge Graphs*

  * Deductive Knowledge
  * Ontologies
  * Interpretations and models
  * ontology features
  * entailment
  * if-then vs if-and-only-if semantics
  * Description Logics

Use:

* Stanford CS520 inference material

  * ontology-based inference
  * taxonomic reasoning

Use:

* Stanford Ontology Development 101

  * classes
  * properties
  * individuals
  * ontology-engineering intuition

Do not copy prose or figures.

Research, understand, paraphrase, cite.

---

# 4. CHAPTER BOUNDARIES

This is extremely important.

## Chapter 4 owns:

* ontology as formal domain model
* classes
* individuals
* object properties
* data properties
* axioms
* class expressions
* formal interpretation
* model
* satisfaction intuition
* entailment intuition
* subclass
* equivalence
* disjointness
* property characteristics
* restrictions
* necessary vs sufficient conditions
* open-world assumption
* Description Logic intuition
* TBox / ABox / RBox mental model
* OWL 2 profiles at conceptual level
* expressivity vs reasoning cost

## Chapter 5 owns:

* reasoning algorithms
* forward chaining
* materialization
* rule systems
* RDFS/OWL reasoner behavior in depth
* consistency checking workflows
* SHACL
* validation
* graph repair
* inference vs validation

Chapter 4 MAY show tiny logical consequences in order to explain semantics.

It must NOT become a reasoner tutorial.

## Chapter 6 owns:

* claim
* evidence
* provenance
* time
* contradiction
* epistemic governance

Do not solve those in Chapter 4.

---

# 5. RUNNING EXAMPLE

Continue the city/country domain from Chapters 2–3.

Avoid switching to unrelated wine/pizza/family examples merely because OWL tutorials use them.

Use:

```text
City
Country
Place
CapitalCity

Hanoi
Vietnam

capitalOf
locatedIn
```

Start with explicit data:

```text
Hanoi rdf:type City
Vietnam rdf:type Country
Hanoi capitalOf Vietnam
```

Then progressively introduce ontology axioms.

A useful target definition is conceptually:

```text
CapitalCity ≡
    City
    AND
    capitalOf SOME Country
```

Description Logic intuition:

```text
CapitalCity ≡ City ⊓ ∃ capitalOf.Country
```

This definition is powerful because it allows Chapter 4 to teach:

* class expressions
* intersection
* existential restriction
* equivalence
* necessary + sufficient conditions
* classification

without abandoning the existing book example.

Use this example throughout the chapter.

Do not claim this ontology is a universal geopolitical model.

It is a teaching ontology.

---

# 6. REQUIRED CHAPTER PROGRESSION

Use natural Vietnamese book prose.

Do not mechanically copy documentation headings.

A good progression is:

---

## 4.0 Opening — From labels to meaning

Begin from Chapter 3.

We already have:

```text
City
Country
capitalOf
```

But what do these symbols MEAN to a machine?

A label named `City` does not inherently mean a set of cities.

A relation called `capitalOf` does not inherently behave according to human expectations.

Introduce the problem:

```text
syntax
!=
meaning
```

Then state the chapter goal:

Formal semantics connects symbols to mathematical interpretations.

---

## 4.1 What is an ontology?

Give multiple layers of intuition.

Distinguish:

```text
Vocabulary
    terms we use

Schema
    expected structure

Ontology
    formally stated conceptual commitments
    about the domain
```

Do NOT make `schema != ontology` an absolute universal taxonomy.

Use careful language:

For this book:

* schema emphasizes expected structure/vocabulary
* ontology emphasizes formal semantic commitments and axioms

Different communities use these words with overlap.

An OWL ontology should be introduced through:

```text
Entities
Expressions
Axioms
```

where entities include:

* classes
* object properties
* data properties
* individuals

Explain the difference between:

```text
declaration
```

and:

```text
semantic axiom
```

A human-readable label or annotation is not automatically part of logical semantics.

---

## 4.2 The mechanism of formal meaning

THIS SECTION IS THE MOST IMPORTANT SECTION OF THE CHAPTER.

Do not rush it.

Introduce a simplified model-theoretic interpretation.

Use intuitive mathematics.

An interpretation I provides at least the intuition:

```text
Δ^I
```

= a non-empty domain of things under consideration.

Then:

Class:

```text
City^I ⊆ Δ^I
```

A class denotes a SET of individuals.

Object property:

```text
capitalOf^I ⊆ Δ^I × Δ^I
```

An object property denotes a BINARY RELATION.

Individual:

```text
Hanoi^I ∈ Δ^I
```

An individual name denotes an element of the domain.

Do not drown the reader in the complete W3C 10-tuple interpretation immediately.

Mention that the normative Direct Semantics is more detailed.

The book's simplified version exists to expose the mechanism.

Then explain:

### Interpretation

A possible assignment of meaning to the vocabulary.

### Satisfaction

An interpretation satisfies an axiom when the axiom's semantic condition holds.

### Model

An interpretation that satisfies all required axioms of the ontology.

### Entailment

Ontology O entails statement α when:

```text
EVERY model of O
also satisfies α
```

Use notation:

```text
O ⊨ α
```

This is the central formal equation of the chapter.

Give one intuitive diagram:

```text
All possible interpretations
        |
        | ontology axioms eliminate
        | incompatible interpretations
        v
Models(O)
        |
        | if α holds in all of them
        v
O ⊨ α
```

Explain:

Ontology reasoning is not a machine "thinking like a human."

It is elimination/restriction of possible interpretations according to formal semantics.

This sentence or an equivalent should appear prominently.

---

## 4.3 Classes as sets: subclass, equivalence, disjointness

Teach these using model semantics.

### Subclass

```text
City ⊑ Place
```

means:

```text
City^I ⊆ Place^I
```

This is one direction.

### Equivalent classes

```text
A ≡ B
```

means:

```text
A^I = B^I
```

Do NOT confuse:

```text
owl:equivalentClass
```

with:

```text
owl:sameAs
```

The former concerns class extensions.

The latter concerns individual identity.

This distinction deserves a Common Misconception callout.

### Disjoint classes

```text
City ⊓ Country ≡ ⊥
```

intuition:

```text
City^I ∩ Country^I = ∅
```

Explain:

disjointness must be explicitly modeled.

Different class names are not automatically disjoint.

Tie this to Chapter 3's lack of unique-name assumption, but do not re-teach that chapter.

---

## 4.4 Necessary vs sufficient conditions

THIS SHOULD BE ANOTHER DEEP SECTION.

Use the CapitalCity example.

First:

```text
CapitalCity ⊑ City
```

means:

Being a CapitalCity is sufficient to conclude City membership.

But being a City is NOT sufficient to conclude CapitalCity.

Then:

```text
CapitalCity
⊑
City ⊓ ∃ capitalOf.Country
```

These are NECESSARY conditions for a CapitalCity.

If something is known to be a CapitalCity, those consequences follow.

But the reverse does not follow.

Then use equivalence:

```text
CapitalCity
≡
City ⊓ ∃ capitalOf.Country
```

Now the conditions are necessary AND sufficient.

Given:

```text
Hanoi : City
Hanoi capitalOf Vietnam
Vietnam : Country
```

the ontology can entail:

```text
Hanoi : CapitalCity
```

Explain precisely WHY:

the right-hand class expression contains Hanoi,
and equivalence makes the two class extensions equal.

This is much deeper than saying:

"`owl:equivalentClass` allows inference."

The reader must understand the mechanism.

---

## 4.5 Class expressions

Introduce only the constructs necessary to build intuition.

### Intersection

```text
C ⊓ D
```

set intersection.

### Union

```text
C ⊔ D
```

set union.

### Complement

```text
¬C
```

relative complement in the interpretation domain.

### Existential restriction

```text
∃ R.C
```

means:

things having at least one R-successor belonging to C.

Formally/intuitively:

```text
{x | exists y:
     (x,y) ∈ R^I
     and
     y ∈ C^I}
```

Important Open World consequence:

An existential restriction may require the existence of some filler even when that
filler has no explicit named individual in the RDF data.

Do not imply that all logical objects must already have names in the graph.

### Universal restriction

```text
∀ R.C
```

means:

all known-in-the-model R-successors of the individual belong to C.

Explain the important logical nuance:

A universal restriction does NOT by itself state that an R-successor exists.

This is a useful example of why formal meaning matters.

### Cardinality

Introduce conceptually:

```text
≥ n R.C
≤ n R.C
= n R.C
```

but do not spend pages on syntax.

Strong warning:

OWL cardinality restrictions are NOT form/database validation rules.

Open-world semantics and lack of unique-name assumption create behavior that surprises
database engineers.

Full validation comparison belongs to Chapter 5.

---

## 4.6 Properties have semantics too

Teach selected object-property axioms:

* subproperty
* inverse
* symmetric
* asymmetric
* transitive
* reflexive
* irreflexive
* functional
* inverse-functional

Do not just provide a vocabulary table.

For each selected important property characteristic, give:

```text
semantic condition
→ consequence
→ common misuse
```

Example:

Symmetry:

```text
R(x,y) => R(y,x)
```

Transitivity:

```text
R(x,y) AND R(y,z)
=> R(x,z)
```

Functionality:

for each subject, property values denote at most one individual in the model.

CRITICAL:

Under OWL semantics + no unique-name assumption, two syntactically different object
names used as values of a functional property may be inferred to denote the SAME
individual rather than automatically causing a validation failure.

This is a high-value database-engineer surprise.

Explain it carefully.

Do not let this section become a complete OWL reference manual.

---

## 4.7 Open World Assumption

Give this its own major section.

W3C OWL Primer explicitly contrasts OWL with typical database assumptions.

Teach:

```text
not known true
!=
known false
```

Example:

Graph does not state:

```text
Hanoi hasAirport X
```

This does NOT entail:

```text
Hanoi has no airport
```

Distinguish three states:

```text
entailed true
entailed false / explicit logical negation where expressible
unknown
```

Do not describe OWL as simply "everything might be true."

Axioms still constrain the set of models.

Use a diagram:

```text
Database intuition:
missing -> false

OWL open world:
missing -> unknown
          unless falsity follows logically
```

Then connect to validation:

This is why OWL restrictions are not equivalent to:

```text
required field
NOT NULL
schema validation
```

Chapter 5 will introduce SHACL for that different problem.

---

## 4.8 Description Logic intuition

Do not teach a full DL course.

Explain why Description Logics exist:

They occupy a useful region between:

```text
expressive logical language
```

and:

```text
reasoning that remains computationally manageable/decidable
```

Introduce the common conceptual partition:

```text
TBox
ABox
RBox
```

with a VERY IMPORTANT qualification:

These are useful Description Logic mental categories.

They are not mandatory physical sections that every OWL file must contain.

Example:

TBox-like:

```text
City ⊑ Place
CapitalCity ≡ City ⊓ ∃capitalOf.Country
City ⊓ Country ⊑ ⊥
```

ABox-like:

```text
Hanoi : City
Vietnam : Country
capitalOf(Hanoi, Vietnam)
```

RBox-like:

```text
locatedIn is transitive
hasCapital inverseOf capitalOf
```

Tie this back to:

```text
general domain knowledge
vs
individual assertions
vs
relation/property semantics
```

---

## 4.9 Consistency, satisfiability, entailment: not the same question

Introduce three different semantic questions conceptually.

### Ontology consistency

Does at least one model satisfy the ontology?

### Class satisfiability

Can this class have at least one member in some model of the ontology?

Important subtle example:

An ontology may be CONSISTENT while a particular class is UNSATISFIABLE.

Example:

```text
City disjointWith Country

ImpossiblePlace
≡
City ⊓ Country
```

The ontology may still have valid models.

`ImpossiblePlace` is simply forced to have an empty extension.

This distinction is very valuable.

### Entailment / instance checking

Does a statement hold in every model?

Do not implement reasoner algorithms here.

Chapter 5 will explain how systems compute/use these tasks.

---

## 4.10 OWL syntax is not OWL meaning

Make this explicit.

The same logical OWL ontology can be represented through multiple syntactic forms.

Teach the distinction:

```text
OWL Structural Model
        |
        +-- Functional-Style Syntax
        +-- RDF serialization
        +-- Manchester Syntax
        +-- other supported forms
```

Do NOT make the reader think:

```text
OWL == Turtle vocabulary
```

Turtle is serialization syntax.

OWL constructs have formal semantics independent of one concrete serialization.

Use only small Turtle and optionally Manchester/functional-style examples.

Book-first means concept before syntax.

---

## 4.11 Expressivity has computational cost

Introduce OWL 2 profiles briefly.

This section should be practical and compact.

The mechanism:

```text
more expressive language
        |
        v
potentially harder reasoning
```

OWL 2 defines profiles trading expressivity for computational/implementation benefits.

Teach only the high-level purpose:

### OWL 2 EL

Useful for ontologies with very large numbers of classes/properties and supports
scalable polynomial-time standard reasoning tasks.

### OWL 2 QL

Designed around large amounts of instance data and query answering, with query
rewriting / relational-database-oriented implementation possibilities.

### OWL 2 RL

Designed for scalable rule-oriented reasoning over RDF-style data.

Do NOT make simplistic claims like:

"EL is fastest"
or
"RL is best for production."

Choice depends on ontology structure and reasoning task.

Do not drown the chapter in complexity-class tables.

A small comparison table is sufficient.

---

# 7. ONE CRITICAL DIAGRAM: HOW SEMANTICS WORKS

Create an original, publication-quality diagram around:

```text
Vocabulary + Axioms
        |
        v
Interpretations
        |
        | satisfy all axioms?
        v
Models(O)
        |
        | proposition true in every model?
        v
Entailment
```

This should be the visual anchor of Chapter 4.

A reader should be able to look at this diagram months later and reconstruct the
mechanism.

---

# 8. OTHER REQUIRED DIAGRAMS

Create 3–5 original diagrams total.

Recommended:

1. Syntax → Interpretation → Models → Entailment
2. Classes as sets:
   subclass / equivalent / disjoint
3. Necessary vs sufficient:
   SubClassOf vs EquivalentClasses
4. Open-world vs closed-world mental model
5. TBox / ABox / RBox conceptual split

All diagrams:

* grayscale-safe
* A4 readable
* consistent with existing Hình numbering
* print-safe
* original
* non-decorative

Continue figure numbering from Chapter 3.

Do not restart from Hình 1.

---

# 9. MECHANISM KNOWLEDGE GRAPH BRIDGE

Add one compact section/callout near the end showing why Chapter 4 matters for the
book's future Mechanism Knowledge Graph.

Use the recurring research idea:

```text
Mechanism: RATE_OF_CHANGE
```

Do NOT attempt to solve cross-domain mechanism recognition yet.

Show only what ontology contributes.

For example, conceptually:

```text
Mechanism
DerivativeOperation
Quantity
ReferenceVariable

RateOfChangeMechanism
≡
Mechanism
AND hasOperation SOME DerivativeOperation
AND hasInput SOME Quantity
AND hasReferenceVariable SOME ReferenceVariable
```

Then explain:

An ontology can formally characterize the conditions under which something belongs to
a mechanism class.

But this STILL does not solve:

* how knowledge is extracted from books
* how two noisy descriptions are aligned
* how evidence is evaluated
* how uncertain mechanism matches are scored
* how a new candidate becomes accepted knowledge

Those later problems belong to Chapters 6–10.

This callout should make the reader see why ontology matters to the final system.

---

# 10. COMMON MISCONCEPTIONS

Chapter 4 should explicitly correct at least these:

1. "Ontology = taxonomy"
2. "Ontology = schema"
3. "OWL gives words human meaning automatically"
4. "`owl:equivalentClass` means the same thing as `owl:sameAs`"
5. "Different class names are automatically disjoint"
6. "Missing information is false"
7. "An OWL restriction is a database validation rule"
8. "`minCardinality 1` means the RDF document must contain a visible value"
9. "Formal entailment proves the real-world truth of premises"
10. "A reasoner invents knowledge using AI"
11. "TBox/ABox/RBox are mandatory physical OWL files"
12. "More expressive ontology language is always better"

Use concise but deep corrections.

---

# 11. THOUGHT QUESTIONS

Use reasoning questions, not vocabulary recall.

Examples:

### ★

If:

```text
CapitalCity ⊑ City
```

and Hanoi is a City, can we conclude Hanoi is a CapitalCity?

Why not?

### ★★

If:

```text
CapitalCity ≡ City ⊓ ∃capitalOf.Country
```

and:

```text
Hanoi : City
Hanoi capitalOf Vietnam
Vietnam : Country
```

why can Hanoi be classified as CapitalCity?

Explain using set/model semantics rather than OWL keywords.

### ★★

If the graph contains no `hasChild` triple for Alice, can OWL conclude that Alice has
no children?

What additional statement would be required to establish something stronger?

### ★★★

Suppose `hasNationalCapital` is declared functional and we assert:

```text
Vietnam hasNationalCapital Hanoi
Vietnam hasNationalCapital HaNoiCity
```

with no assertion that Hanoi and HaNoiCity are different.

Why might OWL semantics NOT treat this as inconsistency?

Connect the answer to Chapter 3.

### ★★★

Can an ontology be consistent while containing an unsatisfiable class?

Construct an example.

---

# 12. BOOK QUALITY BAR

This chapter contains more formal material than Chapters 1–3.

Do not respond by making it denser and uglier.

For every formal expression:

1. explain the intuition first,
2. show the mathematical expression,
3. apply it to the Hanoi example,
4. explain what follows,
5. explain what does NOT follow.

For example:

```text
CapitalCity ≡ City ⊓ ∃capitalOf.Country
```

must never appear as unexplained notation.

The reader should be able to close the laptop and understand it from the printed page.

Avoid encyclopedia-style lists of OWL constructs.

Depth > coverage.

---

# 13. FORMAL PRECISION RULES

Be especially careful with these:

## `SubClassOf`

One-directional inclusion.

Do not accidentally teach equivalence.

## `EquivalentClasses`

Equality of class extensions under an interpretation.

Do not confuse with identity of ontology terms.

## `DisjointClasses`

Empty intersection.

Not automatically implied by different class names.

## Existential restriction

Requires existence in the model.

Does not require a named RDF node to have been explicitly written.

## Universal restriction

Does not imply existence of a property value.

Avoid the classic vacuous-truth mistake.

## Cardinality

Open-world + no unique-name assumption matter.

Do not present cardinality as SHACL-like validation.

## Open World

Unknown is not false.

But OWL is not "anything goes"; axioms constrain possible models.

## Entailment

Logical consequence of ontology.

Not empirical/factual verification.

## Consistency

Existence of a model.

Not the same as "the data is correct."

## Class satisfiability

Nonempty class extension in at least one model.

Not the same as ontology consistency.

---

# 14. SOURCE / CITATION DISCIPLINE

For every standards-sensitive claim:

```text
source
→ semantic contract
→ manuscript explanation
```

Update as necessary:

```text
docs/source_index.json
docs/SOURCE_MATRIX.md
docs/CITATION_MAP.md
docs/RESEARCH_LOG.md
docs/research_notes/

book/references.bib
```

Reader-facing manuscript uses bibliography citations.

Internal source IDs remain engineering metadata.

Do not expose internal source IDs throughout the printed prose.

Do not cite random blogs when W3C/academic primary sources exist.

---

# 15. CHAPTER 4 SEMANTIC CONTRACT

Before or while drafting, create:

```text
docs/CHAPTER04_SEMANTIC_CONTRACTS.md
```

This document should contain the precise teaching contracts for:

* ontology
* entity / expression / axiom
* interpretation
* class interpretation
* property interpretation
* individual interpretation
* satisfaction
* model
* entailment
* subclass
* equivalent classes
* disjoint classes
* existential restriction
* universal restriction
* cardinality
* open-world assumption
* no-UNA interaction
* ontology consistency
* class satisfiability
* OWL Direct vs RDF-Based Semantics
* OWL 2 profiles

Each contract should include:

```text
Concept
Authoritative source
Precise meaning
Simplified book wording
What the wording must NOT imply
```

This document is part of the authoring process, not necessarily reader-facing.

---

# 16. LABS REMAIN DEFERRED

Do not implement Chapter 4 experiments.

Add backlog entries such as:

```text
EXP-4-1 Taxonomy vs ontology
EXP-4-2 RDFS/OWL class inference
EXP-4-3 Equivalent/disjoint classes
EXP-4-4 Restrictions and OWA
EXP-4-5 Consistency / satisfiability
EXP-4-6 Mechanism ontology
```

Use:

```text
DEFERRED_UNTIL_BOOK_V0.1
```

If GitHub issue creation is already part of the established workflow and authenticated,
create issues.

Otherwise only update `docs/LAB_BACKLOG.md`.

No experiment implementation.

No reasoner installation unless absolutely required to verify a disputed semantic claim.

---

# 17. PDF / PUBLICATION CHECKPOINT

When Chapter 4 manuscript is complete:

Update:

```text
docs/BOOK_STATUS.md
book/book-manifest.yaml
book/references.bib
docs/GLOSSARY.md
```

Add important glossary terms such as:

* ABox
* axiom
* class expression
* consistency
* Description Logic
* entailment
* existential restriction
* interpretation
* model
* ontology
* open-world assumption
* RBox
* satisfiability
* sufficient condition
* necessary condition
* TBox
* universal restriction

Avoid duplicate glossary definitions if some already exist.

Build:

```bash
make book
make book-check
```

Create:

```text
docs/CHAPTER04_BOOK_CHECKPOINT.md
```

The checkpoint must record:

* central question
* central semantic mechanism
* primary sources
* formal distinctions
* figures
* editorial decisions
* glossary additions
* deferred labs
* PDF page count
* Chapter 4 page range
* PDF verification results
* representative pages visually inspected
* unresolved questions
* Chapter 5 bridge

Visually inspect representative pages containing:

1. chapter opening map
2. interpretation/model diagram
3. necessary vs sufficient explanation
4. existential/universal restriction section
5. OWA section
6. TBox/ABox/RBox or profiles section
7. final bridge

Check:

* equations do not overflow
* DL notation renders correctly
* Vietnamese glyphs are intact
* code blocks do not clip
* diagrams are readable in grayscale
* citations resolve
* no raw Mermaid
* no raw citation keys
* no wrapper artifacts

---

# 18. CHAPTER 5 BRIDGE

Chapter 4 must end naturally with something like:

We now know WHAT the formal meaning is and WHAT consequences are logically defined.

But we have not yet answered:

* How does a reasoner compute those consequences?
* Should consequences be precomputed or derived at query time?
* How do rule systems relate to OWL/RDFS?
* How do we distinguish inference from validation?
* How do we reject structurally invalid data under an open-world semantic model?

Those questions open:

# Chapter 5 — Deduction, Rules, and Validation

Do not answer them fully in Chapter 4.

---

# 19. DEFINITION OF DONE

Chapter 4 is DONE only when:

* source research is recorded
* semantic contracts are complete
* manuscript is complete
* central mechanism is understandable without code
* necessary vs sufficient conditions are explained correctly
* OWA is explained correctly
* OWL is not presented as validation
* formal meaning is explained through interpretation/models
* all important formal claims are cited
* diagrams are original and print-readable
* glossary is updated
* deferred labs are logged
* PDF build succeeds
* PDF verification gate passes
* representative pages are visually inspected
* `BOOK_STATUS.md` marks Chapter 4 ACCEPTED
* everything is committed
* everything is pushed to `origin/main`
* working tree is clean

The resulting milestone is:

# Book Preview v0.3

Front matter

* Introduction
* Chapters 1–4
* Glossary
* Bibliography

Then STOP.

Do not begin Chapter 5 in this session.

At the end report:

```text
HEAD commit:
Files created:
Files updated:
Primary sources:
Central mechanism:
Major semantic distinctions:
Figures:
Glossary additions:
Deferred labs:
PDF page count:
Chapter 4 PDF page range:
Verification:
Visual inspection:
Known limitations:
Go/No-Go for Chapter 5:
```
