# NARY-01: W3C — Defining N-ary Relations on the Semantic Web

- **Canonical URL:** https://www.w3.org/TR/swbp-n-aryRelations/
- **Status:** W3C Working Group Note (2006-04-12), informative
- **Editors:** Natasha Noy (Stanford), Alan Rector (U. Manchester)
- **Fetched:** 2026-08-25, HTTP 200
- **Used in:** Chapter 3 (qualified/n-ary relation pattern)

## Key Points

- In RDF/OWL a property is a BINARY relation (links two individuals, or an
  individual and a value). But many natural concepts need more participants.
- Two motivating families:
  1. **Properties of a relation**: certainty, severity, strength, relevance of
     a relation instance (e.g., "Christine has breast tumor with high
     probability").
  2. **Relations among multiple individuals**: buyer, seller, and object bought
     in a purchase.
- **Pattern 1 — introduce a new class for the relation**: create a class + n
  properties; an instance of the relation linking the n individuals is an
  instance of this class. Ontologically these are "reified relations". The note
  deliberately avoids the word "reification" because RDF and Topic Maps use it
  differently (terminology caution).
  - Use cases: additional attributes of a relation instance; different aspects
    of the same relation; n-ary relation with no distinguished participant.
- **Pattern 2 — use lists for arguments** (ordered argument list; less common
  for open querying).
- Trade-offs when introducing a new class: query complexity increases; the
  intermediate instance needs a name/identity; reasoning over the original
  binary form requires extra machinery.

## Semantic Contract for Our Chapter 3

- This is the authoritative pattern behind our CapitalStatus example
  (city/country/validFrom). Teach Pattern 1 conceptually; mention trade-offs.
- Use the note's own caution: "reification" is overloaded across communities —
  our chapter distinguishes RDF reification (subject/predicate/object quadruple)
  from the n-ary/qualified-relation entity pattern.
- RDF 1.1 Concepts itself cites this note: relations with >2 participants "can
  only be indirectly expressed in RDF" — good cross-citation.
