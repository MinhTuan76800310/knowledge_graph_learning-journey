# Research Log — Knowledge Graph Book

Chronological record of research activities, findings, and decisions made during Phase 0.

## 2026-08-25: Environment Verification

- **Python**: 3.12.3 available at `/home/minhtuan958/.platformio/penv/bin/python3.12`
- **uv**: 0.12.3 (2026-08-07 build)
- **Docker**: 29.5.2
- **Git**: 2.43.0
- **Workspace**: Empty directory at `/home/minhtuan958/Desktop/tuan_dz/knowledge_graph_leanring-journey/`
- **Decision**: All required tooling is present. No environment setup needed before implementation.

## 2026-08-25: W3C Standards Status Audit

Verified current status of all W3C specifications by fetching live pages from `w3.org/TR/`.

### Stable Recommendations (Main Curriculum Baseline)

| Specification | Status | Date Verified |
|---|---|---|
| RDF 1.1 Primer | Recommendation | 2026-08-25 |
| RDF 1.1 Concepts and Abstract Syntax | Recommendation | 2026-08-25 |
| SPARQL 1.1 Overview | Recommendation (2013-03-21) | 2026-08-25 |
| SPARQL 1.1 Query Language | Recommendation (2013-03-21) | 2026-08-25 |
| OWL 2 Web Ontology Language Document Overview (Second Edition) | Recommendation (2012-12-11) | 2026-08-25 |
| PROV-O: The PROV Ontology | Recommendation (2013-04-30) | 2026-08-25 |
| Shapes Constraint Language (SHACL) | Recommendation (`specStatus: "REC"`) | 2026-08-25 |

### Emerging / Current Development

| Specification | Status | Date | Notes |
|---|---|---|---|
| RDF 1.2 Concepts and Abstract Data Model | Candidate Recommendation Snapshot | 2026-04-07 | Triple terms, improved reification. Teach as emerging feature with callout. |
| RDF 1.2 Primer | Working Draft | 2026 | Companion to RDF 1.2 Concepts. Not yet stable. |
| SPARQL 1.2 Query Language | Working Draft | 2026-08-20 | Very recent draft. Do NOT teach as baseline. Reference only in "Current developments" sections. |

### SHACL 1.2 Status

- URL `https://www.w3.org/TR/shacl-12-core/` returns **404 Page Not Found**.
- URL `https://www.w3.org/TR/shacl-12/` also returns 404.
- The Data Shapes Working Group exists (`w3c.github.io/shacl/`) but no SHACL 1.2 draft is currently published at a stable TR URL.
- **Decision**: Use SHACL 1.0 (Recommendation) as the sole SHACL baseline. If SHACL 1.2 emerges during writing, add it as an explicitly labeled "Current development" note. Do not reference SHACL 1.2 until a W3C TR URL exists.

### Key Teaching Implications

1. **RDF baseline = RDF 1.1**. All introductory experiments use RDF 1.1 semantics.
2. **RDF 1.2 triple terms** are introduced in Chapter 3 and Chapter 6 as an *emerging* alternative to RDF 1.1 reification, with explicit callout boxes marking them as Candidate Recommendation material.
3. **SPARQL baseline = SPARQL 1.1**. SPARQL 1.2 is too recent (Working Draft dated 5 days ago) to serve as curriculum foundation. Mention in Chapter 2 "Current developments" section only.
4. **OWL baseline = OWL 2 Second Edition** (2012). This remains the current stable OWL standard.
5. **PROV-O baseline = PROV-O** (2013 Recommendation). Stable and sufficient for provenance modeling in Chapter 6.
6. **SHACL baseline = SHACL 1.0** (Recommendation). No 1.2 draft exists yet.

## 2026-08-25: Python Library Maintenance Audit

| Library | Latest Version | Last Release Date | Status | Decision |
|---|---|---|---|---|
| RDFLib | 7.6.0 | 2026-02-13 | ✅ Actively maintained | Selected for all RDF experiments |
| pySHACL | 0.40.1 | 2026-07-28 | ✅ Actively maintained | Selected for SHACL validation experiments |
| owlrl | 7.6.2 | 2026-07-08 | ✅ Actively maintained | Selected for RDFS/OWL reasoning experiments |
| NetworkX | 3.6.1 | 2025+ | ✅ Actively maintained | Selected for graph analytics (Ch8) |
| PyKEEN | 1.11.1 | 2025-04-24 | ⚠️ Moderate maintenance | Selected for KG embeddings (Ch8); re-verify before Chapter 8 implementation |

### Library Notes

- **PyKEEN**: Latest release (1.11.1) is from April 2025 — over a year ago. Still functional and the most maintained Python KG embedding library. Re-evaluate alternatives (e.g., LibKGE, DGL-KE) before Chapter 8 implementation. If PyKEEN is incompatible with Python 3.12+ at that time, switch to a maintained alternative and document the change.
- **RDFLib, pySHACL, owlrl**: All released within the last 7 months. Healthy ecosystem for RDF work.
- **NetworkX**: De facto standard for Python graph analytics. No concerns.

## 2026-08-25: Academic Source Scope Confirmation

Confirmed scope boundaries for academic sources:

- **Stanford CS520**: Conceptual framework for "What is a KG?", graph data models, schema design, KG creation, inference, evolution, applications. Used as structural backbone for Chapters 1–6.
- **Hogan et al., Knowledge Graphs (kgbook.org)**: Taxonomy of Data Graphs → Schema → Identity → Context → Deductive/Inductive Knowledge → Creation → Quality → Refinement → Publication → Applications. Maps directly to chapter progression. Used as conceptual reference only; all text is original.
- **Stanford CS224W**: Limited to KG embeddings, reasoning over KGs, and graph-learning foundations. Used only in Chapter 8.
- **Stanford Ontology Development 101**: Methodology for ontology engineering. Used in Chapter 4.
- **Wikidata**: Recurring case study for contextualized claims (qualifiers, references, ranks, temporal qualifiers). Primary real-world laboratory for Chapter 6.
- **Neo4j / GraphAcademy**: Property graph teaching laboratory. Used in Chapters 2, 3, 9. Never presented as synonymous with Knowledge Graphs.
- **Microsoft GraphRAG + "Unifying LLMs and KGs" Roadmap**: Introduced only in Chapter 9 after foundations are established.

## Open Questions

1. SHACL 1.2 may emerge during the writing period. Set up a periodic check mechanism.
2. PyKEEN compatibility with Python 3.12+ should be verified empirically before Chapter 8.
3. RDF 1.2 is advancing rapidly (CR as of April 2026). Monitor for promotion to Proposed Recommendation or full Recommendation.
4. Need to verify Neo4j Community Edition Docker image compatibility with current Docker version (29.5.2) during skeleton phase.

</parameter>