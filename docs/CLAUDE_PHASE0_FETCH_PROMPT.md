# Continue Phase 0 without web_search

The search-engine tool is failing. This is NOT permission to use model memory as a substitute for research.

I have provided two local files:

- `KG_SOURCE_PACK.md`
- `kg_sources.json`

Treat `kg_sources.json` as the machine-readable source manifest and `KG_SOURCE_PACK.md` as the human-readable policy/read-order.

## Your job

Continue Phase 0 research by fetching the exact canonical URLs from the manifest directly.

Do NOT call web search unless it becomes available again. Search is optional; direct URL retrieval is sufficient.

Use direct HTTP retrieval via whichever capability works in this environment:
- `curl -L`
- `wget`
- Python `httpx` / `requests`
- a direct URL fetch/open tool

If one mechanism fails, try another direct-fetch mechanism.

## Hard rule

For every source:

FETCH SUCCESS
→ inspect actual retrieved content
→ extract metadata/status/concepts
→ write research notes
→ cite canonical URL

FETCH FAILURE
→ record `FETCH_FAILED`
→ include HTTP/error evidence
→ try an explicitly listed alternative source if one exists
→ DO NOT fill the missing content from model memory

Model prior knowledge may help formulate questions, but it must not be presented as verified Phase 0 research.

## Start with P0 sources only

Do not fetch all sources blindly.

First fetch the P0 subset in the reading order documented in `KG_SOURCE_PACK.md`.

For W3C specifications, explicitly capture:
- specification title
- exact version/family
- publication date
- W3C status (Recommendation, Candidate Recommendation, Working Draft, Note, etc.)
- latest-version URL
- previous-version/history URL when relevant
- which material is stable curriculum vs emerging material

Never mix RDF 1.1 and RDF 1.2 behavior silently.

## Copyright rule

Do not commit full copies of copyrighted books, papers, Stanford notes, videos, or large third-party documentation.

You may:
- fetch/read them for research
- store metadata
- store your own research notes
- store short necessary excerpts where legally appropriate
- paraphrase with citations

You must not reproduce substantial source text or copyrighted figures.

## Research index

Create `docs/source_index.json` with one record per fetched source:

- id
- canonical_url
- fetched_at
- http_status
- final_url
- title
- authors_or_org
- source_type
- document_status
- publication_or_version_date
- sha256 if a permitted local snapshot was cached
- chapters
- key_concepts
- research_notes_path
- fetch_status

## Research notes

Create one concise note per P0 source under:

`docs/research_notes/<SOURCE_ID>.md`

Each note must answer:

1. What question does this source help the book answer?
2. What are the key concepts?
3. What claims/definitions are safe to rely on?
4. What assumptions or scope limitations exist?
5. Which chapters should use it?
6. What must NOT be inferred from it?
7. What experiments does it motivate?
8. Canonical URL and exact version/status.

## Required outputs before Chapter 1 writing

Update/create:

- `docs/SOURCES.md`
- `docs/SOURCE_MATRIX.md`
- `docs/RESEARCH_LOG.md`
- `docs/CURRICULUM_RATIONALE.md`
- `docs/source_index.json`
- `docs/research_notes/*.md`

Then produce a short Phase 0 checkpoint showing:
- fetched successfully
- fetch failed
- source/status conflicts found
- curriculum decisions changed because of evidence
- missing research questions

Do NOT write Chapter 1 until the P0 source audit is complete.

Do NOT say “verified against my cutoff” when you did not fetch the source. Verification means you retrieved the current source or its current publication-history page.

Begin by reading `kg_sources.json`, selecting P0 entries, and fetching them directly.
