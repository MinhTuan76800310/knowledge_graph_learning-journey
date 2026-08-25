# OWL-02: OWL 2 Web Ontology Language Primer (Second Edition)

- **Canonical URL:** https://www.w3.org/TR/owl2-primer/
- **Status:** W3C Recommendation (2012-12-11)
- **Fetched:** 2026-08-25, HTTP 200
- **Used in:** Chapter 3 (identity semantics: sameAs, differentFrom, no-UNA)

## Key Points — Section 4.7 "Equality and Inequality of Individuals"

- **No unique-name assumption (UNA).** Verbatim core: "OWL does not make the
  assumption that different names are names for different individuals." The
  primer notes this lack of a required UNA "is particularly well-suited to
  Semantic Web applications where names may be coined by different
  organizations at different times unknowingly referring to the same
  individual."
- Consequence: two IRIs give NO automatic evidence of distinctness. To exclude
  identity you must state it explicitly: `:John owl:differentFrom :Bill`.
- `owl:sameAs` states two names denote the SAME individual:
  `:James owl:sameAs :Jim`. Verbatim consequence: "This would enable a reasoner
  to infer that any information given about the individual James also holds for
  the individual Jim." — i.e., information propagates across sameAs.
- Distinctness CAN sometimes be inferred indirectly: if John ∈ Man, Mary ∈
  Woman, and Man/Woman are disjoint, John ≠ Mary follows without differentFrom.
- Cross-ontology linking: `:John owl:sameAs otherOnt:JohnBrown` connects two
  ontologies by asserting individual identity.

## Semantic Contract for Our Chapter 3

- Teach owl:sameAs as IDENTITY, not similarity. The propagation consequence
  ("any information about James also holds for Jim") is the reason a wrong
  sameAs is dangerous — use this for the thought question about incorrect
  sameAs entering a large KG.
- Teach no-UNA as: different identifiers do not prove different entities;
  sameness and distinctness are both explicit assertions requiring evidence.
- Full OWL semantics, disjointness, equivalence, restrictions belong to
  Chapter 4; Chapter 3 uses only sameAs/differentFrom/UNA conceptually.
