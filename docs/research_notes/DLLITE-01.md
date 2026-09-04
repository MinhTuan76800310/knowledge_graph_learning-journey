# DLLITE-01: Tractable Reasoning and Efficient Query Answering in Description Logics: The DL-Lite Family

- **URL:** https://doi.org/10.1007/s10817-007-9078-x
- **Status:** FETCHED_AND_VERIFIED
- **Used in:** Chapter 4 (English + Vietnamese editions - Pillar 2: Complexity Landscape & Logic Decidability)
- **Document status:** Journal of Automated Reasoning 39(3):385-429, Springer, 2007

## What this source establishes for Ch4
Defines the DL-Lite family and proves that conjunctive query answering is first-order rewritable, giving AC0 data complexity and NP-complete combined complexity. This is the theoretical basis of OWL 2 QL. Cited to justify the AC0/NP cells in the §4.12 complexity spectrum and the claim that QL queries can be rewritten to plain SQL/First-Order.

## Safe simplifications
Stating "OWL 2 QL is built on DL-Lite and supports FO-rewritable query answering" is safe.

## Dangerous simplifications / limits
AC0 data complexity refers to query answering with a fixed TBox; combined complexity is NP-complete. Do not imply that *all* reasoning over OWL 2 QL is AC0 or that FO-rewritability applies to arbitrary expressive queries.
