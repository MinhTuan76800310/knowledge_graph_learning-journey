"""Tests for concept dependency registry integrity.

Enforces the invariants from docs/BOOK_PEDAGOGY.md:
  - No concept is used before it is explained (unless marked incidental_gloss)
  - Every concept has both first_used_chapter and first_explained_chapter
  - explanation_level is one of: intuition, mechanism, application
  - Registry YAML is well-formed
"""

from pathlib import Path

import pytest
import yaml

REGISTRY_PATH = Path(__file__).resolve().parent.parent / "book" / "concept_registry.yaml"
VALID_LEVELS = {"intuition", "mechanism", "application"}


@pytest.fixture(scope="module")
def registry():
    """Load the concept registry once for all tests."""
    assert REGISTRY_PATH.exists(), f"Registry not found at {REGISTRY_PATH}"
    with open(REGISTRY_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    assert "concepts" in data, "Registry must have top-level 'concepts' key"
    return data["concepts"]


def test_registry_not_empty(registry):
    assert len(registry) > 0, "Registry must contain at least one concept"


def test_all_concepts_have_required_fields(registry):
    required = {"first_used_chapter", "first_explained_chapter", "explanation_level", "incidental_gloss"}
    for name, entry in registry.items():
        missing = required - set(entry.keys())
        assert not missing, f"Concept '{name}' missing fields: {missing}"


def test_explanation_levels_are_valid(registry):
    for name, entry in registry.items():
        level = entry.get("explanation_level")
        assert level in VALID_LEVELS, (
            f"Concept '{name}' has invalid explanation_level '{level}'; "
            f"must be one of {VALID_LEVELS}"
        )


def test_no_unexplained_usage(registry):
    """A concept cannot be used before it is explained unless marked incidental."""
    violations = []
    for name, entry in registry.items():
        used = entry["first_used_chapter"]
        explained = entry["first_explained_chapter"]
        incidental = entry.get("incidental_gloss", False)
        if used < explained and not incidental:
            violations.append(
                f"  '{name}': used in Ch{used} but explained in Ch{explained} "
                f"(not marked incidental_gloss)"
            )
    assert not violations, (
        "Concepts used before explanation without incidental gloss:\n"
        + "\n".join(violations)
    )


def test_explained_before_or_when_used(registry):
    """Explanation chapter must be >= usage chapter."""
    violations = []
    for name, entry in registry.items():
        used = entry["first_used_chapter"]
        explained = entry["first_explained_chapter"]
        if explained < used:
            violations.append(
                f"  '{name}': explained in Ch{explained} but first used in Ch{used}"
            )
    assert not violations, (
        "Concepts explained after first use (impossible):\n"
        + "\n".join(violations)
    )


def test_chapter_numbers_are_positive_integers(registry):
    for name, entry in registry.items():
        for field in ("first_used_chapter", "first_explained_chapter"):
            val = entry[field]
            assert isinstance(val, int) and val >= 1, (
                f"Concept '{name}' has invalid {field}: {val}"
            )


def test_incidental_concepts_have_notes(registry):
    """Incidental concepts should have notes explaining the minimum gloss provided."""
    violations = []
    for name, entry in registry.items():
        if entry.get("incidental_gloss", False) and not entry.get("notes"):
            violations.append(f"  '{name}': marked incidental but has no notes")
    assert not violations, (
        "Incidental concepts without notes:\n" + "\n".join(violations)
    )


def test_no_duplicate_concept_names(registry):
    """YAML keys are unique by definition, but verify no near-duplicates."""
    names = list(registry.keys())
    lower_names = [n.lower() for n in names]
    seen = set()
    duplicates = []
    for n in lower_names:
        if n in seen:
            duplicates.append(n)
        seen.add(n)
    assert not duplicates, f"Near-duplicate concept names (case-insensitive): {duplicates}"
