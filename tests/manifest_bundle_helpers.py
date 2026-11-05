"""Shared helpers for validating the skill pack's SKILL.md manifests."""

from __future__ import annotations

import pathlib
import re
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
TOOLS_DIR = ROOT / "tools"
TEMPLATES_DIR = ROOT / "templates"

EXPECTED_SKILLS = {
    "manuscript-consistency-checker",
    "series-factsheet-keeper",
    "blurb-ab-note-taker",
    "newsletter-draft-assistant",
    "kdp-metadata-preparer",
    "research-summarizer",
}

REQUIRED_SECTIONS = ("## Purpose", "## Instructions", "## Worked example", "## Local-first workflow")
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Tiny YAML-subset parser good enough for the pack's SKILL.md headers.

    Supports `key: value` scalars and `key:` followed by `  - item` lists —
    the exact shape the manifests use — so the tests pass without PyYAML.
    """
    if not text.startswith("---"):
        raise AssertionError("SKILL.md must start with a --- frontmatter block")
    closing = text.find("\n---", 3)
    if closing == -1:
        raise AssertionError("frontmatter has no closing --- line")
    block = text[4:closing].splitlines()
    body = text[closing + 4 :].lstrip("-\n")

    meta: dict[str, Any] = {}
    current_key: str | None = None
    for raw in block:
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        list_match = re.match(r"^\s+- (.*)$", raw)
        if list_match and current_key:
            item = list_match.group(1).strip().strip('"').strip("'")
            meta[current_key].append(item)
            continue
        key, sep, value = raw.partition(":")
        if not sep:
            raise AssertionError(f"unparseable frontmatter line in SKILL.md: {raw!r}")
        key, value = key.strip(), value.strip()
        if value:
            meta[key] = value.strip().strip('"').strip("'")
        else:
            meta[key] = []
        current_key = key
    return meta, body


def skill_dirs() -> list[pathlib.Path]:
    return sorted(
        d
        for d in SKILLS_DIR.iterdir()
        if d.is_dir() and not d.name.startswith((".", "_")) and (d / "SKILL.md").is_file()
    )


def load_manifest(skill_dir: pathlib.Path) -> tuple[dict[str, Any], str]:
    return parse_frontmatter((skill_dir / "SKILL.md").read_text(encoding="utf-8"))
