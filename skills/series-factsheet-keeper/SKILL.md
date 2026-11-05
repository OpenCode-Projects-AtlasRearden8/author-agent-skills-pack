---
name: series-factsheet-keeper
description: Maintains a living canon factsheet for a book series — characters, places, dates, abilities, and rules of the world — updated after each writing session so later books stay consistent with earlier ones.
version: 1.0.0
local-first: true
requires-model: false
files:
  - examples/worked-example.md
  - workflow.md
  - ../../templates/series-factsheet.md
---

# Series Fact-Sheet Keeper

## Purpose

A series is a promise to the reader: what happened in book two must still be true in book five. This skill keeps one plain `factsheet.md` file in the author's repo that records every canon fact, where it was established, and how confident the entry is. Before drafting, the agent (or author) reads the factsheet; after drafting, the agent proposes updates.

## Instructions

1. **Locate or create the factsheet** at `canon/factsheet.md`. If none exists, copy the structure from `templates/series-factsheet.md` (in the pack root `templates/` folder) and seed it from the existing published material the author points to.
2. **Entry format** — one fact per bullet, in this shape:

   ```
   - **[2008-04] Whistler loses his left ear** (book 1, ch. 7) — canon.
   - **Halloran can read five languages** (book 2, ch. 12) — canon → book 4, ch. 3 conflicts (draft: she stumbles over a French note).
   - *(unconfirmed)* **Riverside burns in book 3** — mentioned in outline only; decide before drafting ch. 20.
   ```

   The bracketed tag always names the source: book + chapter. `canon` means established in published text; `draft` means it contradicts canon; `unconfirmed` means outline/notes only.
3. **Add and update, never delete history.** A corrected entry gets a `~corrected book 4, ch. 2` tag on the same line; the old line stays until the author purges it.
4. **Watch for these categories:** characters (names, ages, injuries, skills, relationships), geography (map facts, travel times), organizations and rules (magic systems, laws, guild ranks), dates and ages, family trees.
5. **After a drafting session:** read the new chapters, list every *new* fact that deserves an entry and every *possible conflict* with existing entries, and propose the diff. Do not commit the diff to the factsheet until the author approves — factsheet edits change canon, which is the author's call.
6. **Before a drafting session:** print a short "canon relevant to this scene" briefing if the author asks for one (e.g., only facts about Whistler and Riverside).
7. **Keep it fast to read.** Group by section (Characters / Places / Timeline / Rules / Open questions). One file, no wiki sprawl.

## Worked example

See `examples/worked-example.md` for a factsheet seeded from two chapters of a series, including a conflict, an unconfirmed fact, and the proposed diff after a new chapter is drafted.

## Local-first workflow

- The factsheet is a single Markdown file in the author's repo — plain text, greppable, readable in any editor. No database, no cloud service.
- Facts are quoted with book + chapter so the author can verify every line against their own files.
- If the author uses a local model for flavor text or summaries, route it through `tools/drafts.py` in this pack (Ollama-friendly, keyless). Canon itself never leaves the repo.

## Troubleshooting

- **Factsheet grows too large:** split per book (`canon/book-3.md`) and keep `canon/factsheet.md` as the index of permanent facts.
- **Two sources conflict:** record both with a `[CONFLICT]` tag and surface it in the weekly review — never silently pick a winner.
