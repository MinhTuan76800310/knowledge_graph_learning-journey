# ADR-002: Neo4j Version for Executable Textbook

**Date:** 2026-08-25
**Status:** Accepted
**Context:** Chapter 2 requires a reproducible Neo4j instance for Property Graph experiments (2-4, 2-5, 2-6).

## Decision

Pin Neo4j Docker image to `neo4j:5.26.30-community` (exact version tag).

Update `docker-compose.yml` from floating `neo4j:5-community` to exact `neo4j:5.26.30-community`.

## Rationale

1. **Reproducibility:** Floating tags (`5-community`) resolve to different versions over time, breaking experiment reproducibility for readers who clone the repo months later.
2. **Community Edition:** Sufficient for all Chapter 2 experiments (basic Cypher, property graph modeling). No Enterprise features needed.
3. **No APOC required:** Basic property-graph and Cypher experiments in Chapter 2 do not require APOC procedures. Remove `NEO4J_PLUGINS=["apoc"]` from docker-compose.yml.
4. **Version selection:** Neo4j 5.26 is the current LTS release line. Tag `5.26.30-community` is the latest patch verified to exist on Docker Hub (2026-08-25). Note: `5.26.0-community` does NOT exist as a Docker Hub tag.
5. **LTS stability:** The 5.26 LTS line receives extended support, ensuring security patches without breaking changes.

## Compatibility Considerations

- Neo4j Python Driver 6.2.0 (installed) is compatible with Neo4j Server 5.x and 4.4
- Cypher syntax used in Chapter 2 experiments targets core Cypher features stable across 5.x releases
- Neo4j has transitioned to calendar versioning (2025.x, 2026.x) for newer releases; 5.26 remains the LTS anchor
- GQL conformance features are documented but not required for basic experiments

## Upgrade Policy

- Update the pinned version only when:
  - A security patch requires it
  - A new Chapter needs a feature unavailable in the current version
  - The current version reaches end-of-life
- Always update via PR with test verification
- Document the change in this ADR
- Verify the new tag exists on Docker Hub before committing

## Consequences

- Readers get identical Neo4j behavior regardless of when they run `docker compose up`
- CI/CD produces deterministic results
- Minor version updates require explicit decision rather than happening silently
- No APOC dependency simplifies the Docker setup

## Sources

- N4J-08: Neo4j Docker documentation (https://neo4j.com/docs/operations-manual/current/docker/)
- Docker Hub tag verification: https://hub.docker.com/_/neo4j/tags (checked 2026-08-25)
