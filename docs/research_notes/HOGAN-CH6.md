# HOGAN-CH6: Knowledge Graphs — Deductive Knowledge

- **URL:** https://kgbook.org/ (Chapter 4 in the HTML edition, titled "Deductive Knowledge")
- **Status:** FETCHED_AND_VERIFIED
- **Used in:** Chapter 4
- **Document status:** Academic textbook (Springer 2021), open full text

## Note on chapter numbering
The source_index.json entry says "Chapter 6" but the relevant content is actually **Chapter 4** ("Deductive Knowledge") in the Hogan et al. HTML edition. The PDF/print edition may use different numbering. Content was verified via the GitHub source at https://github.com/Knowledge-Graphs-Book/HTML-Book/blob/main/chapters/04-deductive.php.

## Key findings for Chapter 4

### Interpretation and Model
Hogan defines interpretation as I = (Γ, ·^I) with domain graph Γ. Model = interpretation satisfying the graph. Entailment G₁ ⊨_Φ G₂ = every model of G₁ under Φ is also model of G₂.

### TBox/ABox/RBox
Presented as formal tuple components (A,T,R) of an ontology, not explicitly labeled "mental categories." Our book's characterization as "phân loại tinh thần" is a pedagogical choice that is defensible but should note that some formalisms treat them as structural components.

### OWL 2 DL and SROIQ
Hogan says OWL 2 DL "(roughly) corresponds to" SROIQ — note the qualifier "roughly." This supports our corrected wording "tương thích chặt chẽ với SROIQ, mở rộng với các tính năng đặc thù OWL."

### Decidability vs Tractability
Explicitly distinguished. Undecidability of full entailment vs computational complexity tradeoffs in DLs. Supports our correction separating decidability from tractability.

### OWA vs CWA
Explicitly discussed and contrasted. Supports our three-way distinction.

### Materialization caveat
Materialization can be unfeasibly large; rules incomplete for negation; not all OWL features capturable by rules.

## What this source establishes for Ch4
- General framework for deductive knowledge on KGs
- TBox/ABox/RBox as formal components
- SROIQ relationship (with "roughly" qualifier)
- Decidability vs tractability distinction
- OWA/CWA contrast

## Safe simplifications
- Treating TBox/ABox/RBox as mental categories is pedagogically defensible.
- Omitting rule-system details is safe for Ch4 scope.

## Dangerous simplifications
- Saying "OWL 2 DL = SROIQ" without qualification.
- Implying materialization is always feasible.

## What this source does NOT justify
- Specific OWL 2 syntax or satisfaction conditions (use W3C specs).
- Profile-specific complexity claims (use Profiles spec).
