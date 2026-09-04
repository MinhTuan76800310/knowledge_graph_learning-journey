# SHAFER-01: A Mathematical Theory of Evidence

- **URL:** https://press.princeton.edu/books/paperback/9780691100425/a-mathematical-theory-of-evidence
- **Status:** FETCHED_AND_VERIFIED (Princeton University Press official page; HTTP 200 + metadata confirmed)
- **Used in:** Chapter 6 (English + Vietnamese editions — Pillar 3: Dempster-Shafer evidence theory, §6.11)
- **Document status:** Peer-reviewed monograph, Princeton University Press, 1976, ISBN 978-0-691-10042-5

## What this source establishes for Ch6
The canonical reference for **Dempster-Shafer theory of evidence**: the frame of discernment (Theta), a mass function m: 2^Theta -> [0,1] with m(empty)=0 and sum over subsets = 1, belief Bel(A) = sum of masses of subsets of A, plausibility Pl(A) = 1 - Bel(complement of A), and Dempster's rule of combination with the conflict normaliser 1/(1-K). Cited in §6.11 to justify replacing naive linear confidence averaging with a theory that separates epistemic ignorance (mass on Theta) from aleatoric conflict (mass on the empty intersection).

## Safe simplifications
Stating that mass distributes unit weight over subsets of the frame, and that [Bel(A), Pl(A)] brackets the warranted degree of belief, is safe. Reporting the closed-form combination rule and the Zadeh warning (K -> 1) is standard.

## Dangerous simplifications / limits
Do not present Dempster-Shafer as simply "generalised probability" without noting the debate. Do not silently drop the 1/(1-K) normalisation. Do not turn Dempster's rule into a blind fusion recipe in the book — it is used to explain *why* raw averaging breaks under conflict, and why a KG should keep divergent branches rather than blend them.
