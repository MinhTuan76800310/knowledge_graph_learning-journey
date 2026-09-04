# JOSANG-01: Subjective Logic — A Formalism for Reasoning Under Uncertainty

- **URL:** https://link.springer.com/book/10.1007/978-3-319-42337-1
- **Status:** FETCHED_AND_VERIFIED (Crossref DOI 10.1007/978-3-319-42337-1 resolves; Springer title/author/year confirmed)
- **Used in:** Chapter 6 (English + Vietnamese editions — Pillar 3: Subjective Logic, §6.11)
- **Document status:** Peer-reviewed monograph, Springer International Publishing, 2016

## What this source establishes for Ch6
The **Subjective Logic** formalism: an opinion vector omega_x = (b_x, d_x, u_x, a_x) with b_x + d_x + u_x = 1 (belief, disbelief, uncertainty, base rate); barycentric coordinates on the 2-simplex; reference probability P(x) = b_x + a_x u_x; and the **consensus fusion operator** (circleplus) that combines two independent opinions and provably shrinks uncertainty u when sources agree. Cited in §6.11 to bridge Dempster-Shafer interval reasoning into a programmable opinion model with a concrete worked example on the Mechanism KG.

## Safe simplifications
Reporting that an opinion is a four-tuple constrained to the simplex, and that consensus fusion reduces uncertainty when independent sources agree, is safe. Using the expectation P(x) = b_x + a_x u_x is standard.

## Dangerous simplifications / limits
Do not reduce Subjective Logic to ordinary probability — the explicit uncertainty mass u_x is the whole point. Do not treat the base rate a_x as ignorable; it drives the expectation whenever u > 0. Do not present fusion as free of assumptions: it presumes source independence, exactly the assumption the echo-chamber warning in §6.5 makes fragile.
