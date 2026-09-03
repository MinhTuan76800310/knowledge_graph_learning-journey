# SHCTS-01: SHACL Test Suite (W3C Data Shapes)

- **URL:** https://w3c.github.io/data-shapes/data-shapes-test-suite/
- **Status:** FETCHED_AND_VERIFIED
- **Used in:** Chapter 5 (English edition — real-world enrichment, §5.6, §5.7)
- **Document status:** W3C Data Shapes conformance test suite (stable)

## What this source establishes for Ch5
The official SHACL conformance test suite: it runs each validator against shared shapes and data
and checks the produced report. It makes questions like "does my validator implement `sh:class`
subclass semantics?" (§5.6) testable rather than a matter of guessing.

## Safe simplifications
Citing the SHACL test suite as the conformance reference for SHACL 1.0 is safe.

## Dangerous simplifications / limits
It tests conformance to the SHACL spec, not the correctness of any particular modeling choice.
Passing the suite does not mean a shape is a good shape.
