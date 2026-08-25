"""Automated repository integrity tests.

These tests verify structural consistency of the repository without
requiring network access. They guard against regression of issues
found during Phase 0.5–0.7 audits.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TestSourceIndexIntegrity:
    """Verify docs/source_index.json is well-formed and consistent."""

    def test_source_index_parses(self) -> None:
        idx_path = ROOT / "docs" / "source_index.json"
        assert idx_path.exists(), "docs/source_index.json must exist"
        data = json.loads(idx_path.read_text(encoding="utf-8"))
        assert "sources" in data
        assert len(data["sources"]) > 0

    def test_source_ids_unique(self) -> None:
        idx_path = ROOT / "docs" / "source_index.json"
        data = json.loads(idx_path.read_text(encoding="utf-8"))
        ids = [s["id"] for s in data["sources"]]
        assert len(ids) == len(set(ids)), f"Duplicate source IDs found: {ids}"

    def test_research_note_paths_exist(self) -> None:
        idx_path = ROOT / "docs" / "source_index.json"
        data = json.loads(idx_path.read_text(encoding="utf-8"))
        missing = []
        for s in data["sources"]:
            note_path = s.get("research_note_path", "")
            if note_path and not (ROOT / note_path).exists():
                missing.append(note_path)
        assert not missing, f"Missing research notes: {missing}"


class TestWrapperArtifacts:
    """Verify no leaked tool/protocol markers remain in repository files.

    Scans the full working tree (not only git-tracked files) so that newly
    generated files are caught before commit. A regression on 2026-08-25
    leaked a closing tag into a freshly created checkpoint document that a
    tracked-files-only scan could not see at test time.
    """

    FORBIDDEN_PATTERNS = [
        "</content>",
        "</parameter>",
        "<content>",
        "<parameter",
        "assistant to=",
    ]

    SCAN_SUFFIXES = {".md", ".py", ".json", ".toml", ".yml", ".yaml", ".txt", ".bib", ".sh", ""}
    SKIP_DIRS = {
        ".git",
        ".venv",
        "venv",
        "node_modules",
        "__pycache__",
        "dist",
        ".pytest_cache",
        ".research",
    }

    def test_no_wrapper_markers_in_repository_files(self) -> None:
        violations = []
        for full in ROOT.rglob("*"):
            if not full.is_file():
                continue
            rel = full.relative_to(ROOT)
            if any(part in self.SKIP_DIRS for part in rel.parts):
                continue
            # This test file legitimately contains the patterns as literals.
            if rel == Path("tests/test_repo_integrity.py"):
                continue
            if full.suffix.lower() not in self.SCAN_SUFFIXES:
                continue
            try:
                text = full.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            for pattern in self.FORBIDDEN_PATTERNS:
                if pattern in text:
                    lines = text.split("\n")
                    for i, line in enumerate(lines, 1):
                        # Allow backtick-wrapped references in prose describing the cleanup
                        if pattern in line and f"`{pattern}`" not in line:
                            violations.append(f"{full.relative_to(ROOT)}:{i}: {pattern}")

        assert not violations, "Wrapper artifacts found:\n" + "\n".join(violations[:20])


class TestResearchCacheIgnored:
    """Verify .research/cache/ is properly gitignored."""

    def test_research_cache_is_ignored(self) -> None:
        result = subprocess.run(
            ["git", "check-ignore", ".research/cache/test.html"],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
        )
        assert result.returncode == 0, ".research/cache/ must be listed in .gitignore"


class TestShaqlContradictions:
    """Verify no stale SHACL contradiction patterns remain."""

    STALE_PATTERNS = [
        "no 1.2 draft exists",
        "no 1.2 exists yet",
        "1.2 does not exist",
        "Not yet published",
    ]

    def test_no_stale_shacl_claims(self) -> None:
        docs_dir = ROOT / "docs"
        violations = []
        for md_file in docs_dir.rglob("*.md"):
            # Historical phase reports document past findings; skip them.
            if md_file.name.startswith("PHASE"):
                continue
            text = md_file.read_text(encoding="utf-8", errors="ignore")
            lower = text.lower()
            for pattern in self.STALE_PATTERNS:
                if pattern.lower() in lower:
                    rel = md_file.relative_to(ROOT)
                    violations.append(f"{rel}: contains '{pattern}'")
        assert not violations, "Stale SHACL claims found:\n" + "\n".join(violations)


class TestJsonFilesParseable:
    """Verify all JSON source files parse successfully."""

    def test_all_json_files_parse(self) -> None:
        json_files = list(ROOT.glob("docs/**/*.json")) + list(ROOT.glob("*.json"))
        failures = []
        for jf in json_files:
            if ".venv" in str(jf) or "node_modules" in str(jf):
                continue
            try:
                json.loads(jf.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                failures.append(f"{jf.relative_to(ROOT)}: {e}")
        assert not failures, "JSON parse failures:\n" + "\n".join(failures)
