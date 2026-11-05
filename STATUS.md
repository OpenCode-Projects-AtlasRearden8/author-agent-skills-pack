# STATUS.md — author-agent-skills-pack

_Last updated: 2026-11-05_

## What was built

A local-first pack of six tested agent skills for authors (writers using agentic
CLIs), each a folder with a `SKILL.md` manifest (YAML frontmatter: `name`,
`description`, `version`, `local-first`, file map), agent notes (`workflow.md`),
and Markdown worked examples:

1. `skills/manuscript-consistency-checker` — internal consistency findings
   (certain/likely/note), ledger + report + CSV, never edits prose. Examples:
   full worked example, chapter-by-chapter timeline table.
2. `skills/series-factsheet-keeper` — living series canon factsheet
   (`canon/factsheet.md`) with book+chapter citations and author-approved diffs.
3. `skills/blurb-ab-note-taker` — append-only blurb variant log
   (`blurb-log.csv`), placements, honest result notes, plain comparisons.
4. `skills/newsletter-draft-assistant` — per-issue drafts from local notes
   (`newsletter/<yyyy-mm>/draft.md`) with `[check]`/`[optional]` seams; never sends.
5. `skills/kdp-metadata-preparer` — KDP-ready `metadata/kdp.yaml` (7 keywords ≤
   50 chars, description HTML within allowed tags, computed length counts,
   paste-ready checklist).
6. `skills/research-summarizer` — sourced research ledger (`research/ledger.md`)
   with page-cited key numbers, `[verify]` flags, and topic digests.

Shared pieces:

- `templates/` — seed files all skills reference
  (`consistency-findings.csv`, `series-factsheet.md`, `blurb-log.csv`,
  `newsletter-planner.md`, `kdp-metadata.yaml`, `research-ledger.md`).
- `tools/drafts.py` (+ `tools/drafting-config.json`) — optional keyless drafting
  helper for any OpenAI-compatible endpoint; default is Ollama at
  `http://127.0.0.1:11434/v1`; standard library only; supports `init`, `models`,
  `draft`, `--dry-run`, and streaming.
- `tests/test_skill_manifests.py` (+ `tests/manifest_bundle_helpers.py`) —
  manifest validation and pack-integrity tests (no PyYAML dependency; no network).
- `README.md` (credits Asdale Dynamics, LLC), `LICENSE` (MIT, "Copyright (c)
  2026 Asdale Dynamics, LLC"), `pytest.ini`, `.gitignore`.

All six skills keep their output in-repo (`consistency/`, `canon/`, `newsletter/`,
`metadata/`, `research/`, `blurb-log.csv`); nothing is uploaded, auto-sent, or
fetched; no secrets or personal data in any file.

## How to run it

- Use a skill: point your agentic CLI at this repo (or copy a `skills/<name>/`
  folder plus `templates/` into your book repo) and ask for the skill by name.
- Optional drafting (local/OpenAI-compatible, keyless):
  ```bash
  python3 tools/drafts.py init            # write default Ollama config
  python3 tools/drafts.py models
  python3 tools/drafts.py draft --dry-run --system "plain, warm" "Hello"
  python3 tools/drafts.py draft --system "plain, warm" "Open a newsletter gently"
  ```
- Validate the pack: `pytest` (config `pytest.ini`; also `pytest tests/`).

## Verification results

Environment: Python 3.13.5, pytest 9.1.1, Linux. Git repo initialized locally.

- `python3 -m pytest` — **14 passed** (manifest shape, six-skill roster, semver,
  section structure, all frontmatter `files:` entries resolve on disk, worked
  examples present, all six templates referenced via `../templates/...`,
  README credit + MIT LICENSE line config keyless + local-first, `drafts.py`
  `--dry-run` and `--show-config` subprocess tests, init round-trip,
  secret-string scan, STATUS.md sections, frontmatter parser round-trip).
- `python3 tools/drafts.py --show-config` — prints the expected config shape
  (`api_key` empty, `base_url` local).
- `python3 tools/drafts.py draft --dry-run ...` — prints the payload without
  sending anything (verified manually and via pytest).
- Manual mock-server check: an ephemeral local OpenAI-compatible stub on
  `127.0.0.1` answered non-dry-run `draft` and `models` calls correctly
  (endpoint path `/chat/completions` + `/models`, OpenAI response shape).
- Fix loop history: initial run had 3 failures (missing STATUS.md;
  frontmatter `../templates/` paths resolving one directory too short — changed
  to `../../templates/`; argparse requiring a subcommand before `--show-config`
  — subparsers now optional). All fixed; final suite green.

## Known gaps

- `pytest` validates manifests and pack wiring; it does not "run" the skills
  themselves — skills are instructions for agentic CLIs, so correctness of an
  authoring session is judged by the worked examples.
- The drafting helper's `models`/`draft` paths are exercised only via `--dry-run`
  in CI-safe tests plus the manual mock-server check above; a live Ollama run
  depends on the author's local server and model inventory.
- No skills for pricing/tax math on KDP (intentionally out of scope; KDP shows
  royalty math on-site). No eBay/reselling or bookkeeping skills in this pack.
- KDP's own form rules evolve; the limits encoded (title/subtitle ≤ 200 chars,
  description ≤ 4,000 chars, 7 keywords ≤ 50 chars, allowed HTML subset) should
  be re-checked against KDP help pages before a real submission.
- No CI workflow file; tests are meant to be run locally (`pytest`).
