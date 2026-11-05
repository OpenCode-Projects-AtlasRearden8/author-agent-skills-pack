# Author Agent Skills Pack

A collection of tested agent skills for writers who use agentic CLIs (Claude Code,
Codex, OpenCode, and friends). Each skill is a folder with a `SKILL.md` manifest,
step-by-step instructions, and a worked example — written plain, warm, and
beginner-friendly, in the spirit of *The Massive AI Manual*.

**Local-first by design.** Manuscripts, canon factsheets, blurb logs, newsletters,
KDP metadata, and research notes all live as ordinary files in **your** repo.
Nothing is uploaded, nothing auto-sends, and the optional drafting helper needs
**no API keys** (it defaults to a local Ollama server).

## The six skills

| Skill | What it does | Writes to (local files) |
|---|---|---|
| `skills/manuscript-consistency-checker` | Finds name/timeline/place contradictions inside a manuscript; certain/likely/note findings, never edits prose | `consistency/findings.md`, `consistency/findings.csv` |
| `skills/series-factsheet-keeper` | Keeps a series canon factsheet; proposes a diff after each drafting session, you approve | `canon/factsheet.md` |
| `skills/blurb-ab-note-taker` | Append-only log of blurb variants, placements, and results so you can see what actually sold | `blurb-log.csv`, `blurbs/*.md` |
| `skills/newsletter-draft-assistant` | Drafts a 400–600 word issue from local notes, with `[check]`/`[optional]` seams; never sends | `newsletter/<yyyy-mm>/draft.md` |
| `skills/kdp-metadata-preparer` | Assembles KDP-ready metadata (7 keywords, description HTML, categories) with computed length checks and a paste-ready checklist | `metadata/kdp.yaml` |
| `skills/research-summarizer` | Summarizes author-supplied research files into a sourced, page-cited ledger with topic digests | `research/ledger.md` |

Every skill's `SKILL.md` frontmatter (name, description, version, `local-first`,
file map) is validated by the included pytest suite.

## How to use a skill

1. Point your agentic CLI at this repo (or copy a `skills/<name>/` folder into
   your project and keep the pack's `templates/` beside it).
2. Ask for the skill by name, e.g. *"Run the manuscript consistency checker on
   manuscript/."* The `SKILL.md` Instructions section tells the agent what to do;
   the worked `examples/` show it what "done" looks like.
3. The skill writes its plain-text findings next to your books. You review,
   edit, and decide everything — agents draft, you approve.

## Optional drafting with a local model (no keys)

The helpers in `tools/drafts.py` call any OpenAI-compatible endpoint for
optional flavor text — the default config points at Ollama on your own machine:

```bash
python3 tools/drafts.py init                 # write tools/drafting-config.json
python3 tools/drafts.py models               # list what your server offers
python3 tools/drafts.py draft --dry-run --system "plain, warm" "Hello!"
python3 tools/drafts.py draft --system "plain, warm, beginner-safe" \
    "Open a newsletter with two friendly sentences."
```

- Default: `http://127.0.0.1:11434/v1` (Ollama). Edit `tools/drafting-config.json`
  to point at LM Studio, llama.cpp, vLLM, or a hosted OpenAI-compatible API.
- **No API key is required or stored.** `tools/drafts.py` is standard-library only.
- Network use is optional and opt-in per run; `--dry-run` previews the payload.

## Tests

```bash
pytest            # or: pytest tests/
```

The suite validates every `SKILL.md` manifest (frontmatter shape, semver,
real file references), the six-skill roster, template cross-references, the
keyless config, the helper's dry-run behavior, and scans the pack for
API-key-shaped strings. Verified with Python 3.13 / pytest 9.1.

## Layout

```
skills/            one folder per skill: SKILL.md, workflow.md (agent notes), examples/
templates/         seed files the skills copy into your book repo
tools/             drafts.py + drafting-config.json (keyless, Ollama-friendly)
tests/             pytest manifest validation
```

And when you use it inside a book project, the skills keep those files
there — e.g. `consistency/`, `canon/`, `newsletter/`, `metadata/`, `research/`.

## Who made this

Built by **Asdale Dynamics, LLC** (Dylan Asdale — nurse turned AI author;
*The Massive AI Manual*, dylanasdale.github.io). Asdale Dynamics, LLC makes
beginner-friendly AI education, books, and practical local-first tools.

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 Asdale Dynamics, LLC.
Use it, remix it, ship it. No warranty; none of this is publishing, legal,
or medical advice.
