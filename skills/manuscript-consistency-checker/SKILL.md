---
name: manuscript-consistency-checker
description: Reviews a manuscript for internal consistency — names, spellings, timelines, places, and repeated phrases — and produces a plain-English report the author can fix by hand.
version: 1.0.0
local-first: true
requires-model: false
files:
  - examples/worked-example.md
  - examples/timeline-table.md
  - workflow.md
  - ../../templates/consistency-findings.csv
---

# Manuscript Consistency Checker

## Purpose

Catch the small contradictions that readers notice and authors miss: a character called "Marcus" in chapter 2 and "Mark" in chapter 9, a town that starts 30 miles from the river but ends up across it, a scene that happens three days after an event the narrator says was "last week." This skill collects findings into a single report stored next to the manuscript — never uploaded anywhere.

## Instructions

1. **Ask for (or locate) the manuscript file.** It should live in the author's local folder, e.g. `manuscript/chapter-*.md` or a single `draft.md`. Do not ask the author to paste content into any web service.
2. **Build a pass plan.** Read the manuscript in slices that fit the working context and process them in order. Keep a running ledger (see the ledger template below) of every entity you see.
3. **Track these entity types:**
   - **People:** full names, nicknames, shortened forms (Marcus / Mark / M. Reyes), kinship terms (Aunt Dean vs. Aunt Dana).
   - **Places:** town names, building names, street names, room layouts.
   - **Timeline:** dates, ages, durations ("three weeks later"), days of the week, seasons.
   - **Objects/habits:** eye color, allergies, a character being "always late" versus arriving early.
   - **Repetition:** distinctive phrases or metaphors used more than twice.
4. **Compare entries, don't just collect them.** When two ledger entries might refer to the same thing but differ, flag it. When you can confidently merge them (e.g. "Margaret 'Peggy' Ellison" is stated once as a nickname), merge silently.
5. **Grade every finding** with confidence: `certain` (two statements that cannot both be true), `likely` (possible but resolvable), or `note` (stylistic or a heads-up).
6. **Write the report to `consistency/findings.md`** (create the folder if needed) using the structure in the worked example, and append rows to `consistency/findings.csv` based on `templates/consistency-findings.csv`.
7. **Never rewrite the manuscript itself.** Suggest fixes; the author applies them. Quote the exact conflicting lines with chapter/section labels so the author can search for them.
8. **Report counts first, then details.** Example: "3 certain, 7 likely, 12 notes — details below."

### Ledger template (keep in working memory or a scratch note)

```
[name] | seen in: ch1.3, ch5.1 | forms: Marcus, Mark | status: FLAG
```

### Report skeleton

```
# Consistency Findings — <book title> — <date>
## Summary
## Certain
## Likely
## Notes
```

Each finding: what conflicts, where each version appears, and a suggested fix phrased as a question ("Was the ferry accident meant to be 1998 or 1996?").

## Worked example

See `examples/worked-example.md` for a full run on a two-chapter sample, including the ledger, the identified conflicts, and the finished report. `examples/timeline-table.md` shows how to lay out a chapter-by-chapter time table so gaps are visible at a glance.

## Local-first workflow

- Everything stays in the author's repo/folder: the manuscript, the `consistency/` output folder, and this skill.
- If the agent runs with network tools available, it must **not** use them for manuscript content. No file uploads, no third-party transcription services.
- If you want to draft polite phrasings for tricky findings with a local model, you may use `tools/drafts.py` (see the pack README) with an Ollama or other OpenAI-compatible endpoint — but finding the inconsistencies is done by reading, not by the model.

## Troubleshooting

- **Context too small for the whole book:** process chapter by chapter and persist the ledger to `consistency/ledger.md` between slices.
- **Ambiguous name (two characters share a nickname):** ask the author once, at the end, in a single batch of questions.
