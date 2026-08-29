# Chapter 5 — ACCEPTED + TikZ Pilot Complete (2026-08-29)

Chapter 5 has been drafted, reviewed, semantically closed, and accepted.
A controlled TikZ pilot experiment added 8 formal diagrams to Chapters 4–5.

## Current state

- Chapters 1–5 are ACCEPTED
- Book PDF builds to 100 pages (was 97 before TikZ pilot; was 86 before semantic closure)
- All tests pass: 18 passed (book gate), plus optional lab tests
- Semantic contracts: docs/CHAPTER05_SEMANTIC_CONTRACTS.md (28 records)
- Checkpoint: docs/CHAPTER05_BOOK_CHECKPOINT.md
- Manuscript: 22 sections (§5.1–§5.22), ~700+ lines
- 12 misconceptions, 5 self-explanation checkpoints
- Primary sources added: RDF-MT-01 (RDF 1.1 Semantics), SP11-ENT (SPARQL 1.1 Entailment Regimes)

## TikZ pilot results

- 8 TikZ figures added: Ch4 (3), Ch5 (5)
- Baseline preserved: tag `book-preview-v0.4-baseline-pre-tikz` at commit 103432b
- Experiment branch: `exp/tikz-pilot`
- Comparison report: `docs/TIKZ_PILOT_COMPARISON.md`
- Renderer policy: `docs/BOOK_PEDAGOGY.md` §15
- TikZ sources: `book/figures/tikz/*.tex`
- Generated PDFs: `book/figures/generated/*.pdf`
- Render script: `scripts/render_tikz.sh`
- **Recommendation: ADOPT TikZ selectively for formal diagrams from Ch6 onward**
  - Use TikZ for: set/logic/inference/validation diagrams, algorithm state transitions, annotated matrices
  - Continue Mermaid for: conceptual flows without math alignment
  - Continue tables for: comparison data, regime listings
  - Do NOT retrofit Ch1–3 in this session

## Next chapter: Chapter 6 — Claims, Evidence, Provenance, Time, Contradiction

Chapter 6 covers the Context layer of Mental Model 1:
- Claim ≠ Fact
- Provenance (PROV-O)
- Temporal knowledge
- Contradiction handling
- Epistemic governance

Key sources already indexed: PROV-01 (PROV-O), WD-01/WD-02 (Wikidata statements/qualifiers).

**Figure policy for Ch6:** Use TikZ by default for formal diagrams (provenance chains, temporal models, contradiction structures). Follow the renderer taxonomy in BOOK_PEDAGOGY.md §15.

## Constraints carried forward

- Do NOT resume deferred labs
- Do NOT install Neo4j
- SHACL 1.2 Core (SH-02) = CURRENT DEVELOPMENT ONLY; stable baseline is SH-01
- Book quality > lab completeness
- All external claims must cite sources from docs/SOURCES.md
- Use GitHub MCP for commits so author shows as "MinhTuan76800310"
