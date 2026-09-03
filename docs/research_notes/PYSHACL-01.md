# PYSHACL-01: pySHACL — A Pure Python SHACL Validator

- **URL:** https://github.com/RDFLib/pySHACL
- **Status:** FETCHED_AND_VERIFIED
- **Used in:** Chapter 5 (English edition — real-world enrichment, §5.6)
- **Document status:** Open-source tool, RDFLib project (stable)

## What this source establishes for Ch5
A pure-Python validator implementing the SHACL 1.0 Recommendation. It executes the exact
target → focus node → path → value node → constraint → result pipeline of §5.6 and produces the
ValidationReport / ValidationResult structure of §5.7. It is the validator used in this book's
own toolchain.

## Safe simplifications
Citing pySHACL as a concrete SHACL 1.0 validator is safe.

## Dangerous simplifications / limits
pySHACL validates; it does not perform OWL reasoning by default. Whether it sees an inferred
graph depends on the effective validation graph the caller feeds it (§5.11) — do not imply it
auto-materializes RDFS/OWL.
