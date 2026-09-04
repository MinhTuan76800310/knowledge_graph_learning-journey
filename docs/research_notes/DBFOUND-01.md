# DBFOUND-01: Foundations of Databases

- **URL:** https://webdam.di.ens.fr/Alice/
- **Status:** FETCHED_AND_VERIFIED (free online edition; authors Serge Abiteboul, Richard Hull, Victor Vianu; Addison-Wesley, 1995, ISBN 0-201-53930-5)
- **Used in:** Chapter 5 (English + Vietnamese editions — Pillar 2 Part 2: Datalog foundations, §5.16)
- **Document status:** Peer-reviewed textbook, Addison-Wesley 1995

## What this source establishes for Ch5
The canonical reference for Datalog's **three equivalent semantics** — model-theoretic (the minimal Herbrand model M(P) as the intersection of all Herbrand models satisfying P and containing D), proof-theoretic (finite derivations), and fixpoint (lfp(T_P)) — and the theorem that they coincide. It also establishes Datalog's **PTIME-complete data complexity** and **EXPTIME-complete combined complexity**, and the safeness / range-restriction condition that guarantees termination. Cited in §5.16 to justify the equivalence M(P) = derivable facts = lfp(T_P) and the complexity figures.

## Safe simplifications
Stating that the three semantics coincide for (safe, function-free) Datalog is safe and is the textbook result. Reporting data complexity as PTIME-complete and combined complexity as EXPTIME-complete is the standard, stable result.

## Dangerous simplifications / limits
Do not present the three-way equivalence as holding for arbitrary first-order logic or for Datalog with function symbols or unsafe rules — it is specifically for safe, function-free Datalog. Do not conflate data complexity (program fixed) with combined complexity (program + data vary); the chapter's practical claim ("cheap once the rules are fixed") rests on the data-complexity figure, not the combined one. This is a databases textbook, not an RDF/OWL entailment reference.
