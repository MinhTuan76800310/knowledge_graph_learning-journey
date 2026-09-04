# SROIQ-01: Even More Irresistible SROIQ

- **URL:** https://dblp.org/rec/conf/kr/HorrocksKS06
- **Status:** FETCHED_AND_VERIFIED
- **Used in:** Chapter 4 (English + Vietnamese editions - Pillar 2: Complexity Landscape & Logic Decidability)
- **Document status:** KR 2006, AAAI Press, pp. 57-67

## What this source establishes for Ch4
Defines the DL SROIQ and proves that its reasoning problems are N2EXPTIME-complete. SROIQ extended with concrete datatype domains is the DL underlying OWL 2 DL. Cited to justify the statement "OWL 2 DL = SROIQ(D)" and the N2EXPTIME-combined-complexity cell in the §4.12 complexity spectrum.

## Safe simplifications
Saying "SROIQ(D) corresponds to OWL 2 DL" is safe. OWL 2 Direct Semantics is standardly described as closely aligned with SROIQ extended with datatype/punning features.

## Dangerous simplifications / limits
Do not confuse N2EXPTIME-combined with EXPTIME-data complexity; do not claim that every OWL 2 DL reasoner has N2EXPTIME *typical* runtime — this is worst-case complexity, not practical performance.
