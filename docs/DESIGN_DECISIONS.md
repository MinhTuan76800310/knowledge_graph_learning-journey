# Design Decisions — Knowledge Graph Book

This document records significant architectural, pedagogical, and technical decisions made during the development of this book. Each entry includes the decision, rationale, alternatives considered, and consequences.

## DD-001: Mental Model as Engineering Framework, Not Formal Definition

**Decision:** Present "Knowledge Graph = Data Graph + Semantics + Context" as an engineering learning model, not a universally accepted formal definition.

**Rationale:** There is no single agreed-upon formal definition of "Knowledge Graph" in the academic or industrial literature. Stanford CS520, Hogan et al., and various industry practitioners use different emphases. Presenting one definition as authoritative would be misleading. The chosen decomposition serves as a practical scaffold for engineers to reason about what components are needed and what is missing at each stage.

**Alternatives considered:**
- Use Hogan et al.'s taxonomy directly (Data Graphs → Schema → Identity → Context → Deductive/Inductive Knowledge). Rejected because it is a research taxonomy optimized for comprehensive coverage, not progressive skill-building.
- Avoid any definition and let it emerge implicitly. Rejected because experienced engineers benefit from an explicit conceptual anchor they can critique and refine.

**Consequences:** Every chapter must explicitly connect back to one or more components of this model. Readers should understand that other valid decompositions exist.

---

## DD-002: Vietnamese Language with English Technical Terms

**Decision:** Write all book content in Vietnamese. Keep technical terms in English on first occurrence with Vietnamese gloss: "thực thể (entity)", "suy diễn (inference)".

**Rationale:** The target audience is Vietnamese-speaking software engineers. Writing in Vietnamese reduces cognitive load for complex conceptual material. Keeping English terms preserves precision and ensures readers can search for further resources in the dominant language of the field. Inconsistent translation of technical terms is a known source of confusion in non-English technical education.

**Alternatives considered:**
- Write entirely in English. Rejected because it excludes the intended audience.
- Translate all terms fully into Vietnamese. Rejected because many KG terms lack standardized Vietnamese equivalents, and readers need English terms for interoperability with documentation, standards, and tools.

**Consequences:** Glossary must be maintained rigorously. Code, configs, and docs/ remain in English for tooling compatibility.

---

## DD-003: RDF 1.1 as Stable Baseline, RDF 1.2 as Emerging

**Decision:** Teach RDF 1.1 (W3C Recommendation 2014) as the main curriculum baseline. Introduce RDF 1.2 features (triple terms, improved reification) only in clearly labeled "Current developments" callouts.

**Rationale:** As of 2026-08-25, RDF 1.2 is a Candidate Recommendation Snapshot (2026-04-07), not yet a full Recommendation. Tool support (RDFLib, triple stores) is still catching up. Teaching draft features as if stable would produce code that breaks when specifications change or when readers use older tooling.

**Alternatives considered:**
- Teach RDF 1.2 exclusively. Rejected because it is not yet stable and tool support is incomplete.
- Ignore RDF 1.2 entirely. Rejected because triple terms and improved reification are directly relevant to Chapter 6 (Claims, Provenance) and readers should know what is coming.

**Consequences:** Must verify RDF 1.2 status periodically. Callout boxes must be visually distinct. Experiments using RDF 1.2 features must be marked 📖 or 🚧 until tool support stabilizes.

---

## DD-004: Pure Python for Early Experiments, Libraries Introduced Progressively

**Decision:** Experiments 1-1 through 1-5 use pure Python with no external dependencies. RDFLib, pySHACL, owlrl, NetworkX, and Neo4j are introduced only when their specific capabilities become necessary.

**Rationale:** Early experiments teach concepts (graph topology, taxonomy, inference mechanics) that do not require library complexity. Introducing libraries too early obscures the underlying mechanisms. When libraries are introduced, readers already understand what problem the library solves.

**Alternatives considered:**
- Use RDFLib from Chapter 1. Rejected because it would conflate "what is a graph" with "how to use RDFLib."
- Use NetworkX for all graph operations. Rejected because NetworkX's API hides the distinction between plain graphs and semantic graphs.

**Consequences:** Early experiment code is intentionally minimal. Library-based experiments must explicitly map library abstractions back to the concepts taught in pure-Python experiments.

---

## DD-005: LLM Output Treated as CandidateKnowledge, Never Direct Knowledge

**Decision:** All LLM-assisted extraction (Chapter 7+) produces CandidateKnowledge that must pass through an explicit validation boundary before entering the canonical knowledge graph. No experiment writes LLM output directly into the accepted graph.

**Rationale:** LLMs generate plausible-sounding but unverified assertions. Treating LLM output as knowledge without validation violates the core principle that knowledge requires evidence and verification. This is a recurring theme in the book and must be architecturally enforced, not merely stated.

**Alternatives considered:**
- Allow direct LLM-to-graph insertion with a warning. Rejected because warnings are easily ignored and the architecture would not enforce the principle.
- Skip LLM integration entirely. Rejected because modern KG systems must handle LLM-assisted acquisition; avoiding it would make the book irrelevant.

**Consequences:** Chapter 7+ experiments have additional validation steps. The capstone system (Chapter 10) must include explicit CandidateKnowledge → AcceptedKnowledge state transitions.

---

## DD-006: Mechanism Knowledge Graph as Recurring Capstone Domain

**Decision:** Maintain one evolving graph under `capstone/mechanism_knowledge_system/` across all chapters, rather than using unrelated toy examples per chapter.

**Rationale:** Disconnected examples force readers to rebuild mental context at every chapter. A single evolving domain demonstrates how concepts compose: identity (Ch3) enables ontology (Ch4), which enables inference (Ch5), which enables provenance (Ch6), etc. The mechanism domain is chosen because it naturally requires cross-domain abstraction (rate_of_change appears in physics, biology, finance), making it suitable for exploring structural pattern recognition.

**Alternatives considered:**
- Use Wikidata as the sole running example. Rejected because Wikidata's scale and complexity would overwhelm early chapters.
- Use a different domain per chapter. Rejected because it breaks continuity and prevents cumulative understanding.

**Consequences:** Ontology design decisions must be justified incrementally. Earlier chapters may introduce simplified versions of concepts that are refined later. The mechanism recognition problem is treated as a research challenge, not a solved exercise.

---

## DD-007: Docker for Neo4j, Lightweight Local for RDF

**Decision:** Provide Neo4j Community Edition via Docker Compose. Do not require a triple store server for early RDF experiments; use RDFLib's in-memory store.

**Rationale:** Neo4j requires a server process and is impractical to run without containerization. RDFLib provides sufficient functionality for Chapters 1–5 without server overhead. Adding a triple store requirement would create unnecessary friction for readers who only need basic RDF operations.

**Alternatives considered:**
- Require Blazegraph or Apache Jena Fuseki from Chapter 2. Rejected because it adds setup complexity before readers understand why they need it.
- Run Neo4j natively. Rejected because installation varies across platforms and Docker provides reproducibility.

**Consequences:** Docker Compose file must be tested. Experiments requiring SPARQL endpoints beyond RDFLib must be marked 📖 with setup instructions.

---

## DD-008: Experiment Status Requires Execution Evidence

**Decision:** An experiment is marked ✅ only after it has been executed in the project environment and output captured. Code existence alone is insufficient.

**Rationale:** Unrunnable experiments undermine trust. Readers following the book must be able to reproduce results. Marking experiments as runnable without verification is a common failure mode in executable textbooks.

**Alternatives considered:**
- Trust that code works if it passes syntax checks. Rejected because runtime errors, dependency issues, and logic bugs are not caught by syntax alone.
- Mark all experiments ✅ and fix later. Rejected because it violates the quality gate requirement.

**Consequences:** `docs/EXPERIMENT_STATUS.md` must contain execution timestamps and output summaries. CI should eventually enforce this automatically.

