# Chapter 3 Book Checkpoint — 2026-08-25

Chapter 3 — *Lược đồ, Định danh và Ngữ cảnh* (Schema, Identity, and Context) is drafted,
semantically and editorially reviewed, built into both PDFs, and visually inspected.
Together with the five Chapter 2 errata (committed first, `f5ad670`) and the Chapter 3
research pass (`efec8c4`), this checkpoint closes the work slice and produces
**Book Preview v0.2**: front matter + Introduction + Chapters 1–3 + Glossary +
Bibliography. The next target is Chapter 4; it has **not** been started in this slice.

## Central mechanism

The chapter is organized around one question:

> "A graph tells us what is connected. How do we determine what those things ARE,
> whether two identifiers refer to the SAME thing, and under which CONTEXT a statement
> should be interpreted?"

The mental model is a data graph examined along three **distinct** axes — Schema
(expected structure and vocabulary), Identity (what each identifier denotes, and when
two identifiers denote the same entity), and Context (source/time/scope/perspective
under which a statement should be interpreted). The axes are deliberately *not*
collapsed into "ontology"; formal meaning is Chapter 4's territory.

A single continuous scenario — source A's `ex:Hanoi` versus source B's `wd:Q1858`,
both apparently denoting Hanoi — opens the chapter (3.0) and is carried through schema
alignment, identity resolution, and context attachment into the full worked example
(3.4). Section map: 3.1 schema (and schema ≠ ontology), 3.2 identity (the conceptual
heart: identifier ≠ entity, `owl:sameAs`, no unique-name assumption), 3.3 context
(named graphs, n-ary relation entities, relationship properties, RDF 1.2 callout),
3.4 combined worked example, 3.5 eight common modeling mistakes, 3.6 thought
questions, 3.7 know/cannot-do bridge to Chapter 4.

## Primary sources

Research notes live in `docs/research_notes/`; the registry is `docs/source_index.json`;
the reader-facing bibliography is `book/references.bib` (IEEE numeric). Sources actually
used in Chapter 3:

| Internal ID | Bibliography key | Used for |
|-------------|------------------|----------|
| H01 | `hogan-knowledge-graphs` | Conceptual backbone: schema/identity/context triad, identity links, "reified edge does not assert", named graphs as flexible higher-arity |
| S05 | `stanford-cs520-create-kg` | Schema design, IRI design, identity links, schema as evolving artifact |
| S06 | `stanford-cs520-kg-from-data` | Schema mapping, record linkage, entity identity across sources |
| R11-02 | `w3c-rdf11-concepts` | IRI, RDF dataset, named graphs (§4 note: graph name not required to denote), entailment wording (§1.7) |
| R11-03 | `w3c-rdf-schema` | RDFS vocabulary table; domain/range as entailment, not validation |
| OWL-02 | `w3c-owl2-primer` | `owl:sameAs` / `owl:differentFrom`, no unique-name assumption, identity propagation |
| NARY-01 | `w3c-nary-relations` | Pattern 1 (intermediate relation entity) for qualified/contextual relations |
| WD-01 | `wikidata-statements` | Real-world case study: statements as claim + qualifiers + references + rank |
| WD-02 | `wikidata-qualifiers` | Qualifiers as contextualizing mechanism |
| N4J-05 | `neo4j-data-modeling` | Property-graph equivalents: labels, properties, constraints, application-generated IDs |
| N4J-06 | `neo4j-cypher-manual` | `elementId()` STRING semantics; relationship properties |
| R12-01 | `w3c-rdf12-concepts` | Current-development callout only: triple terms and reifiers |

`docs/CITATION_MAP.md`, `docs/RESEARCH_LOG.md`, and `book/references.bib` were updated
for exactly these sources.

## Important semantic distinctions

Carried in the manuscript as explicit, bolded teaching points:

1. **Identifier ≠ entity.** Same string/IRI does not prove semantic agreement;
   different identifiers do not prove different entities.
2. **Database element identity ≠ domain identity.** Neo4j `elementId()` is a STRING
   implementation identifier, unique only within a single transaction, reusable after
   deletion; applications should generate their own durable IDs (Chapter 2 erratum 1,
   echoed in Chapter 3).
3. **`owl:sameAs` means identity** — not similarity, not fuzzy match. If asserted, OWL
   semantics treats the two IRIs as the same individual and information propagates;
   therefore it is an *accepted* assertion issued after evidence and review, not a
   candidate-match marker (⚑ practice-rule callout in §3.2.4).
4. **OWL has no unique-name assumption**: different names do not automatically denote
   different individuals.
5. **Candidate match → evidence/review → accepted assertion → `owl:sameAs` or canonical
   merge.** Matching algorithms themselves are deferred to Chapter 7.
6. **Schema ≠ ontology.** A schema states expected classes/relations/property
   names/types/constraints without giving formal meaning; RDFS domain/range are
   entailment rules, not validation constraints. Schema may be upfront, incremental, or
   bottom-up — a KG does not require a complete upfront schema.
7. **Named graph ≠ automatic provenance.** Per RDF 1.1 Concepts, a graph name is merely
   syntactically paired with its graph; source/provenance meaning is an application
   convention unless explicitly modeled (Chapter 6).
8. **A reified/n-ary edge does not assert** the relation it describes (Hogan):
   representation and assertion are separate acts.
9. **Context enables evaluation; context does not create truth.** — the mandatory
   sentence, printed in Vietnamese and English in §3.3.7.
10. **Entailment ≠ factual truth** (Chapter 2 erratum 5): RDFS/OWL define formal
    entailment semantics; validity of consequences does not establish the factual
    truth of the input assertions.
11. **GQL is an ISO query-language standard**, not a graph data-exchange format
    (Chapter 2 erratum 2); and **no inherent traversal-performance superiority** is
    claimed for either data model (Chapter 2 erratum 3).
12. **RDF 1.1 baseline vs RDF 1.2 development** for relationship metadata: reification /
    intermediate entity / n-ary pattern today; triple terms and reifiers as an
    emerging, clearly-marked mechanism (Chapter 2 erratum 4; ⚑ callout in §3.3.5).

## Diagrams

Four original figures, Mermaid `neutral` theme, pre-rendered at 3× to PNG
(`build/figures/chapter03-fig1..4.png`), grayscale-safe and readable at A4:

| Printed no. | File | Content |
|-------------|------|---------|
| Hình 4 | `chapter03-fig1.png` | Three-axis mental model: Data Graph + Schema / Identity / Context |
| Hình 5 | `chapter03-fig2.png` | Two-source identity resolution: candidates → evidence/review → accepted assertion |
| Hình 6 | `chapter03-fig3.png` | Contextualized binary relation → qualified n-ary relation (`CapitalStatus`) |
| Hình 7 | `chapter03-fig4.png` | Full integration pipeline: sources → schema alignment → identity → context → integrated representation |

## Editorial decisions

- Prose-first Vietnamese book prose; Turtle/Cypher/SPARQL appear only as compact
  illustrations; the chapter is readable with the laptop closed. Every major concept is
  treated with the five-question discipline (problem solved / information represented /
  what it does NOT imply / easy mistake / downstream mechanism).
- The named-graph example is fenced as `trig` with a sentence explaining the format,
  keeping Turtle vs TriG precise.
- A CJK alias example ("河内") was removed after the build gate caught missing glyphs
  (U+FFFD); the alias discussion now uses Latin-script variants only.
- ⚑ callouts mark practice rules (`owl:sameAs` assertion discipline) and current
  developments (RDF 1.2), per the book's print-safe marker convention.
- Glossary gained 12 entries (Alias, Canonical identifier, Denotation, Identifier,
  Identity resolution, Named graph, N-ary relation, owl:sameAs, Qualifier, Record
  linkage, Schema, Unique name assumption); `book-manifest.yaml` and the verification
  script's expected-title list were updated.
- BOOK-FIRST: labs 3-1…3-6 are recorded as `EXP-3-1`…`EXP-3-6` in `docs/LAB_BACKLOG.md`
  with status `DEFERRED_UNTIL_BOOK_V0.1` (GitHub issues #4–#9, label `chapter-03`).
  No Neo4j labs resumed, no Docker work.

## Build, verification, and visual inspection

- `scripts/verify_book_pdf.sh` (via `make book-check`): **GATE PASSED**, 53 pages in
  both the print and screen PDFs; checks green for chapter titles (including
  "Chương 3 — Lược đồ, Định danh và Ngữ cảnh"), TOC, numeric bibliography, no leftover
  `[@key]`, no leftover Mermaid fences, no U+FFFD, no wrapper artifacts.
- Chapter 3 occupies PDF pages 33–48; the Glossary begins on page 49.
- Representative pages rendered to `dist/preview/ch3-page-{33,36,39,42,45,47}.png` and
  visually inspected:
  - p.33 — chapter opening and orientation block render cleanly;
  - p.36 — RDFS vocabulary table with numeric citations renders cleanly;
  - p.39 — §3.2.4–3.2.5 identity prose, monospaced `owl:sameAs`, ⚑ callout clean;
  - p.42 — named-graph caution, n-ary Pattern 1 Turtle, PG relationship-property
    snippet clean;
  - p.45 — worked-example steps 1–3 and the Hình 7 pipeline diagram clean and
    grayscale-readable;
  - p.47 — thought questions, §3.7 know/cannot-do lists, Chapter 4 bridge, and
    "Đọc thêm" clean.

## Unresolved questions

- RDF 1.2 triple terms/reifiers are cited only as current development; wording must be
  revisited when RDF 1.2 reaches formal recommendation status.
- Validating-schema vocabularies (SHACL/ShEx) are intentionally not treated here; their
  placement belongs to the ontology/rules chapters.
- Canonical-identifier policy on merge (which IRI survives) is application-specific; the
  chapter teaches the process, not a universal rule.
- Formal identity-propagation semantics and full provenance models (PROV, claims) are
  deferred to Chapters 4–6 by design.

## Chapter 4 bridge

§3.7 ends by listing what the three axes still cannot express — two classes being
disjoint, class equivalence, logical restrictions on properties, and definitions by
necessary/sufficient conditions — which opens **Chapter 4 — Bản thể học và Ngữ nghĩa
Hình thức** (Ontologies and Formal Meaning). Chapter 4 remains NOT_STARTED.
