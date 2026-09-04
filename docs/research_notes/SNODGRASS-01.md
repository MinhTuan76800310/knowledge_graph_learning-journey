# SNODGRASS-01: Developing Time-Oriented Database Applications in SQL

- **URL:** https://www2.cs.arizona.edu/~rts/tdbbook
- **Status:** FETCHED_AND_VERIFIED (author's own page serves the book PDF; Open Library confirms title + author Richard T. Snodgrass)
- **Used in:** Chapter 6 (English + Vietnamese editions — Pillar 3: bitemporal coordinate grid, §6.7)
- **Document status:** Peer-reviewed monograph, Morgan Kaufmann, 1999, ISBN 978-1-55860-436-0

## What this source establishes for Ch6
The foundational treatment of **temporal databases**: valid time (when a fact holds in the world) versus transaction/system time (when the database recorded it), the bitemporal model that keeps both, and the append-only discipline that lets a system answer retrospective queries ("what did we believe at time T about the year V?"). Cited in §6.7 to ground the 2D Bitemporal Coordinate Grid and the non-destructive view of temporal claim storage.

## Safe simplifications
Stating that valid time records world-truth while transaction time records system-knowledge is safe. Representing a bitemporal claim as a rectangle R = [Tv-, Tv+] x [Ttx-, Ttx+] is a standard conceptual device.

## Dangerous simplifications / limits
Do not present the 2D rectangle as a W3C standard — it is a pedagogical model. Do not conflate system time with assertion time when the distinction matters operationally. OWL-Time supplies vocabulary, not temporal semantics; the temporal annotations in the book remain application conventions.
