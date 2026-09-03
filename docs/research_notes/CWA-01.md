# CWA-01: On Closed World Data Bases (Reiter)

- **URL:** https://doi.org/10.1007/978-1-4684-3384-5_3
- **Status:** FETCHED_AND_VERIFIED (verified via Springer record)
- **Used in:** Chapter 5 (English edition — real-world enrichment, §5.9, §5.10)
- **Document status:** Peer-reviewed book chapter, in Logic and Data Bases (Gallaire & Minker, eds.), pp. 55–76, 1978
- **Author:** Raymond Reiter

## What this source establishes for Ch5
The precise origin of the Closed World Assumption: anything not derivable from the database is
taken as false. SHACL's count constraints (absence of a value node fails `minCount`) evoke this
*flavor*, but SHACL is not CWA in Reiter's logical sense — it makes no truth claim, only a
structural conformance judgment. This is exactly the conformance ≠ truth boundary of §5.8.

## Safe simplifications
Citing Reiter 1978 as the formal origin of the CWA is safe.

## Dangerous simplifications / limits
Do NOT say "SHACL = OWL + CWA" (that is the misconception §5.6/§5.9 rejects). Reiter's CWA is a
logical operator on a database; SHACL's absence-fails-minCount is a validation rule on a supplied
graph. The chapter uses Reiter to locate the intuition, not to equate the two.
