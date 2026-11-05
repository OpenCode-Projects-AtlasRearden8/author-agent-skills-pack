---
name: blurb-ab-note-taker
description: Tracks back-cover / Amazon blurb experiments A/B style in a single local log, records which text ran where and when, and later joins the results so the author can see what actually sold.
version: 1.0.0
local-first: true
requires-model: false
files:
  - examples/worked-example.md
  - workflow.md
  - ../../templates/blurb-log.csv
---

# Blurb A/B Note-Taker

## Purpose

Authors test blurbs everywhere — Amazon* launch formulas, newsletters, Reddit posts, the back cover — and then forget which version of the blurb was where. This skill keeps one append-only log in the author's repo: every variant, its wording, where it ran, and the result when one exists. Six months later the author can ask "which blurb family worked?" and get an answer from the log instead of from memory.

*All platform names are references into the author's own local files and screenshots — nothing is fetched or posted by this skill.

## Instructions

1. **Find or create `blurb-log.csv`** using `templates/blurb-log.csv` (pack root). All edits are **append-only**: add rows, never rewrite old ones, so the file doubles as a small experiment history.
2. **Log a variant** when the author launches or tests one. Required fields: `slug`, `text` (or `text_file` pointing at a file with the full blurb), `placement` (e.g. `amazon-shot-blurb`, `newsletter-2026-11`, `back-cover`), `date_started`. Optional: `family` (short label like `lightning`, `whisper` — a "family" is a hypothesis, e.g. "short punchy cold-open"), `hypothesis`, `audience`.
3. **Record results** later by appending a result note to the row: impressions/clicks as measured by the author (never scraped), copies sold in the window, or a free-text result like `few comments, low engagement`. Leave `result` empty until real numbers exist, and mark reads as estimates if they are.
4. **Compare**, when asked: group by `family`, list each variant with its result, and give a plain-English read ("Short punchy blurbs drew more click-throughs on the newsletter; the moody whisper variants did better in Reddit, small sample").
5. **Draft new variants** only when asked, staying inside an existing family or starting a new one; keep every draft the agent produces in the same log with source set to `drafted`, so tested and untested text never mixes.
6. **Privacy:** log aggregates, never personal data. A reader's name belongs nowhere in this file.
7. **Honesty guardrail:** never declare a winner from a single impression count or a tiny sample; state the sample size next to every conclusion.

## Worked example

See `examples/worked-example.md` for a filled log with three families, two placements, a result being recorded, and a comparison written off the log.

## Local-first workflow

- `blurb-log.csv` and any `blurbs/*.md` text files live in the author's repo. This skill reads customers' aggregate numbers from files the author imports by hand (e.g. `data/kdp-weekly.csv`); it never logs into any platform.
- Correspondence with platforms is done by the author; the skill only records what happened.

## Troubleshooting

- **Same blurb tested on two placements:** two rows, same `text`, different `slug` suffix (`-a`, `-b`) — comparison is per placement.
- **Author can't remember the exact text used in March:** point at the row's `text_file`; if no file was kept, add a `lost` note row, and from now on always keep the text with the log.
