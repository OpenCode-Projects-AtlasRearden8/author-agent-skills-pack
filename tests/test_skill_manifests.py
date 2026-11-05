"""Manifest and pack-integrity tests for the author-agent-skills-pack.

Run from anywhere: `pytest` (see pytest.ini). No network access is required
or used; the drafting helper is only exercised in --dry-run mode.
"""

from __future__ import annotations

import json
import pathlib
import subprocess
import sys

from manifest_bundle_helpers import (
    EXPECTED_SKILLS,
    NAME_RE,
    REQUIRED_SECTIONS,
    ROOT,
    SEMVER_RE,
    TOOLS_DIR,
    TEMPLATES_DIR,
    load_manifest,
    parse_frontmatter,
    skill_dirs,
)


def test_exactly_the_pack_six_skills_exist() -> None:
    found = {d.name for d in skill_dirs()}
    assert found == EXPECTED_SKILLS, f"expected the six pack skills, got {found}"


def test_every_skill_manifest_is_well_formed() -> None:
    for d in skill_dirs():
        meta, _body = load_manifest(d)
        for field in ("name", "description", "version"):
            assert field in meta and str(meta[field]).strip(), f"{d.name}: missing {field}"
        assert NAME_RE.match(meta["name"]), f"{d.name}: bad frontmatter name {meta['name']!r}"
        assert meta["name"] == d.name, f"{d.name}: frontmatter name != folder name"
        assert SEMVER_RE.match(meta["version"]), f"{d.name}: version not semver"
        assert meta["description"].strip().endswith("."), f"{d.name}: description must be a full sentence"
        assert "local-first" in meta, f"{d.name}: missing local-first flag"


def test_every_skill_has_required_sections_and_pack_wiring() -> None:
    for d in skill_dirs():
        _, body = load_manifest(d)
        for section in REQUIRED_SECTIONS:
            assert section in body, f"{d.name}/SKILL.md: missing section '{section}'"
        assert "examples/" in body, f"{d.name}: SKILL.md does not wire to examples/"


def test_manifest_files_list_resolves_to_real_files() -> None:
    for d in skill_dirs():
        meta, _ = load_manifest(d)
        files = meta.get("files")
        assert isinstance(files, list) and files, f"{d.name}: 'files' list missing or empty"
        for rel in files:
            path = (d / rel).resolve()
            assert path.is_file(), f"{d.name}: frontmatter files entry does not exist: {rel}"


def test_examples_contain_worked_example_content() -> None:
    for d in skill_dirs():
        examples = list((d / "examples").glob("*.md"))
        assert examples, f"{d.name}: examples/ folder is empty"
        text = "\n".join(p.read_text(encoding="utf-8") for p in examples)
        assert "## " in text, f"{d.name}: example has no markdown sections"


def test_shared_templates_exist_and_are_referenced_by_skills() -> None:
    expected = {
        "consistency-findings.csv",
        "series-factsheet.md",
        "blurb-log.csv",
        "newsletter-planner.md",
        "kdp-metadata.yaml",
        "research-ledger.md",
    }
    present = {p.name for p in TEMPLATES_DIR.iterdir() if p.is_file()}
    assert expected <= present, f"missing templates: {expected - present}"
    for template in expected:
        referenced = any(
            f"../templates/{template}" in (d / "SKILL.md").read_text(encoding="utf-8")
            for d in skill_dirs()
        )
        assert referenced, f"{template} is not referenced from any SKILL.md via ../templates/"


def test_pack_readme_and_license() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "Asdale Dynamics, LLC" in readme
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    assert "Copyright (c) 2026 Asdale Dynamics, LLC" in license_text
    assert "Permission is hereby granted, free of charge" in license_text


def test_drafting_helper_is_keyless_and_local_first() -> None:
    cfg = json.loads((TOOLS_DIR / "drafting-config.json").read_text(encoding="utf-8"))
    assert cfg["api_key"] == "", "config must never store an API key"
    assert cfg["base_url"].startswith("http://127.0.0.1") or cfg["base_url"].startswith("http://localhost"), (
        "default base_url should be local-first"
    )


def test_drafts_py_dry_run_works() -> None:
    proc = subprocess.run(
        [
            sys.executable,
            "tools/drafts.py",
            "draft",
            "--dry-run",
            "--system",
            "plain, warm, beginner-safe",
            "Say hello to a beginner reader in one short sentence.",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert proc.returncode == 0, proc.stderr or proc.stdout
    assert "DRY-RUN" in proc.stdout
    assert '"role": "user"' in proc.stdout
    assert proc.stdout.count('"model"') == 1


def test_drafts_py_shows_config_shape() -> None:
    proc = subprocess.run(
        [sys.executable, "tools/drafts.py", "--show-config"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert proc.returncode == 0, proc.stderr
    snap = json.loads(proc.stdout)
    assert snap["api_key"] == "" and snap["base_url"].startswith("http://127.0.0.1")


def test_drafts_py_init_writes_config(tmp_path: pathlib.Path) -> None:
    target = tmp_path / "sub" / "cfg.json"
    proc = subprocess.run(
        [sys.executable, "tools/drafts.py", "init", "--config", str(target)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert proc.returncode == 0, proc.stderr
    cfg = json.loads(target.read_text(encoding="utf-8"))
    assert cfg["api_key"] == "" and "base_url" in cfg and "model" in cfg


def test_no_api_key_shaped_secrets_anywhere_in_pack() -> None:
    offenders: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.resolve().parent == pathlib.Path(__file__).resolve().parent:
            continue  # this test file itself contains the marker strings
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for marker in ("sk-", "AKIA", "ghp_"):
            if marker in text:
                offenders.append(f"{path.relative_to(ROOT)} contains {marker!r}")
    assert not offenders, f"possible secrets in pack files: {offenders}"


def test_status_md_exists_with_core_sections() -> None:
    status = (ROOT / "STATUS.md").read_text(encoding="utf-8")
    for heading in ("What was built", "How to run", "Verification", "Known gaps"):
        assert heading.lower() in status.lower(), f"STATUS.md missing section `{heading}`"


def test_parser_roundtrip_on_every_manifest() -> None:
    for d in skill_dirs():
        raw = (d / "SKILL.md").read_text(encoding="utf-8")
        meta, body = parse_frontmatter(raw)
        assert body.strip(), f"{d.name}: empty body"
        assert isinstance(meta.get("files"), list)
