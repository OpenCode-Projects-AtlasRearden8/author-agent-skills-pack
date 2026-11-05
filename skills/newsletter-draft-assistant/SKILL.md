---
name: newsletter-draft-assistant
description: Drafts an author newsletter issue from local notes into a plain-Markdown folder layout — planner, draft, links — ready for the author to paste into their email tool.
version: 1.0.0
local-first: true
requires-model: false
files:
  - examples/worked-example.md
  - workflow.md
  - ../../templates/newsletter-planner.md
---

# Newsletter-Draft Assistant

## Purpose

Turn scattered writing-session notes, launch news, and one "story from the desk" into a short, warm newsletter draft the author can finish in ten minutes. Output is plain Markdown in the author's repo, one folder per issue — no auto-sending, ever.

## Instructions

1. **Start from `newsletter/planner.md`** (create from `templates/newsletter-planner.md` in the pack root if missing). It holds the recurring skeleton: greeting, what happened this month, a reader-friendly explainer, one book news item, links, sign-off.
2. **Gather material locally only:** recent `notes/*.md`, the series factsheet if one exists (`canon/factsheet.md`), launch dates, and the author's link list. Nothing from the web unless the author supplies a URL.
3. **Draft into `newsletter/<yyyy-mm>/draft.md`:**
   - Voice: "like a friend would" — plain English, short sentences, never condescending, no hype words ("revolutionary," "limited time" are out).
   - Length target: 400–600 words for the base issue. Cut before you add.
   - One theme per issue. If notes suggest three themes, propose the other two for future planners.
   - Every external link gets a one-line "why this is worth your click."
   - No personal data: subscribers are never named; "a reader wrote in…" only when the author confirms.
4. **Mark seams clearly.** Unverified facts get `[check]`; optional paragraphs get `[optional]`; the author removes the brackets or the text.
5. **Draft-generation hygiene:** paragraphs the model wrote are wrapped in `[begin draft]/[end draft]` comments so quality review stays honest; both skill-written and model-written text is shown to the author as a draft to edit, never as final copy.
6. **Keep per-issue state in the folder:** `draft.md`, `links.md`, and a `sent.md` stub next to the final copy after the author sends it. The `sent.md` note goes into future issues' "what happened" section.
7. **Never send.** The author's mail tool of choice does that.

## Worked example

See `examples/worked-example.md` for a full issue built from three notes, a factsheet, and a link list — planner, draft with seams, and the final file layout.

## Optional drafting with a local model

For tone-safe filler (openers, transitions), you may call `tools/drafts.py` from this pack with a local Ollama model (`base_url: http://127.0.0.1:11434/v1` by default) or any OpenAI-compatible endpoint the author configures in `tools/drafting-config.json`. No API key is required or stored. Any network call is optional and initiated only when the author asks for a model draft.

## Local-first workflow

- Everything lives in the repo: `newsletter/**` per issue, `notes/**`, `canon/**`.
- Metrics (opens, clicks) are only ever imported by the author into `data/newsletter-metrics.csv`; the skill reads that file if asked about a past issue, never a server.

## Troubleshooting

- **Issue reads stiff:** rewrite the opener last, and say the point in nine words or fewer.
- **Author runs two newsletters (series vs. AI guides):** two planner files (`planner-series.md`, `planner-ai.md`) and two folders per month; never mix audiences in one draft.
