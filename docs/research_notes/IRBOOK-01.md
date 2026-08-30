# IRBOOK-01: Introduction to Information Retrieval (Manning, Raghavan & Schutze, 2008)

- **Primary reference:** Manning, C.D., Raghavan, P. & Schutze, H. (2008). Introduction to Information Retrieval. Cambridge University Press.
- **URL:** https://nlp.stanford.edu/IR-book/
- **Status:** FETCHED_AND_VERIFIED (open online edition, 2026-08-30)
- **Used in:** Chapter 9
- **Canonical topic:** Classical information retrieval: indexes, weighting, ranking, evaluation

## Key Points

- IR pipeline: documents -> tokenization -> inverted index -> query processing -> ranked results.
- tf-idf weighting: term frequency within a document x inverse document frequency across the collection.
- Evaluation: precision = fraction of retrieved that is relevant; recall = fraction of relevant that is retrieved; ranked metrics include precision@k, recall@k, MRR, nDCG.
- "Information need" (the user's real need) vs "query" (the expression) vs "document" (the candidate) — a key distinction for Ch9's question interpretation.

## Semantic Contract

- Retrieval evaluation measures ranking quality against relevance judgments; relevance judgments are annotations, not ground truth about the world.
- Precision and recall trade off; neither is a truth measure.
- MUST NOT: equate information need with query text; treat relevance as truth; skip recall for high-stakes epistemic retrieval.
