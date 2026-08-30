"""Tests for concept dependency registry integrity.

Enforces the invariants from docs/BOOK_PEDAGOGY.md:
  - A concept's first_required_use_chapter must be >= first_explained_chapter
    (you cannot require understanding of something not yet taught)
  - A concept may be mentioned earlier than explained only if incidental_gloss is true
  - Every concept has all required fields
  - explanation_level is one of: intuition, mechanism, application
  - Registry YAML is well-formed

Field semantics:
  first_mentioned_chapter: first textual appearance (may be incidental)
  first_required_use_chapter: first chapter where the reader MUST understand the concept
  first_explained_chapter: chapter where mechanism-level teaching occurs
  incidental_gloss: whether pre-explanation mentions include a minimum local gloss
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
    required = {
        "first_mentioned_chapter",
        "first_required_use_chapter",
        "first_explained_chapter",
        "explanation_level",
        "incidental_gloss",
    }
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


def test_required_use_after_explanation(registry):
    """A concept must be explained by the time it is required.

    Invariant: first_explained_chapter <= first_required_use_chapter

    This is the core pedagogical invariant from BOOK_PEDAGOGY.md §2:
    'Defer Depth, Never Required Understanding.'
    """
    violations = []
    for name, entry in registry.items():
        required = entry["first_required_use_chapter"]
        explained = entry["first_explained_chapter"]
        if explained > required:
            violations.append(
                f"  '{name}': required in Ch{required} but not explained until Ch{explained}"
            )
    assert not violations, "Concepts required before they are explained:\n" + "\n".join(violations)


def test_early_mentions_are_incidental(registry):
    """If a concept is mentioned before it is explained, it must be marked incidental.

    Invariant: if first_mentioned_chapter < first_explained_chapter,
    then incidental_gloss must be true.
    """
    violations = []
    for name, entry in registry.items():
        mentioned = entry["first_mentioned_chapter"]
        explained = entry["first_explained_chapter"]
        incidental = entry.get("incidental_gloss", False)
        if mentioned < explained and not incidental:
            violations.append(
                f"  '{name}': mentioned in Ch{mentioned} but explained in Ch{explained} "
                f"(not marked incidental_gloss)"
            )
    assert not violations, (
        "Concepts mentioned before explanation without incidental gloss:\n" + "\n".join(violations)
    )


def test_mentioned_before_or_when_required(registry):
    """A concept cannot be required before it is even mentioned.

    Invariant: first_mentioned_chapter <= first_required_use_chapter
    """
    violations = []
    for name, entry in registry.items():
        mentioned = entry["first_mentioned_chapter"]
        required = entry["first_required_use_chapter"]
        if mentioned > required:
            violations.append(
                f"  '{name}': required in Ch{required} but not mentioned until Ch{mentioned}"
            )
    assert not violations, "Concepts required before they are mentioned:\n" + "\n".join(violations)


def test_chapter_numbers_are_positive_integers(registry):
    for name, entry in registry.items():
        for field in (
            "first_mentioned_chapter",
            "first_required_use_chapter",
            "first_explained_chapter",
        ):
            val = entry[field]
            assert isinstance(val, int) and val >= 1, f"Concept '{name}' has invalid {field}: {val}"


def test_incidental_concepts_have_notes(registry):
    """Incidental concepts should have notes explaining the minimum gloss provided."""
    violations = []
    for name, entry in registry.items():
        if entry.get("incidental_gloss", False) and not entry.get("notes"):
            violations.append(f"  '{name}': marked incidental but has no notes")
    assert not violations, "Incidental concepts without notes:\n" + "\n".join(violations)


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
