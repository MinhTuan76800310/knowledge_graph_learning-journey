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
    """Verify no leaked tool/protocol markers remain in tracked files."""

    FORBIDDEN_PATTERNS = [
        "</content>",
        "</parameter>",
        "<content>",
        "<parameter",
        "assistant to=",
    ]

    def test_no_wrapper_markers_in_tracked_files(self) -> None:
        result = subprocess.run(
            ["git", "ls-files"],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
        )
        assert result.returncode == 0
        tracked = result.stdout.strip().split("\n")

        violations = []
        for fpath in tracked:
            full = ROOT / fpath
            if not full.is_file():
                continue
            # Only check text-like files
            suffix = full.suffix.lower()
            if suffix not in {".md", ".py", ".json", ".toml", ".yml", ".yaml", ".txt", ""}:
                continue
            if fpath.startswith(".venv/") or "__pycache__" in fpath:
                continue
            try:
                text = full.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            for pattern in self.FORBIDDEN_PATTERNS:
                if pattern in text:
                    # Allow legitimate references in prose (e.g., backtick-wrapped)
                    # but flag bare occurrences
                    lines = text.split("\n")
                    for i, line in enumerate(lines, 1):
                        if pattern in line and f"`{pattern}`" not in line:
                            violations.append(f"{fpath}:{i}: {pattern}")

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
