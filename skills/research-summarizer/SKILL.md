---
name: research-summarizer
description: Summarizes author-supplied research documents into short, sourced notes in a local research ledger, with one summary per source and a running topic digest — no web scraping, no invented citations.
version: 1.0.0
local-first: true
requires-model: false
files:
  - examples/worked-example.md
  - workflow.md
  - ../../templates/research-ledger.md
---

# Research Summarizer

## Purpose

Deities forbid, but authors write chapters about ferries, rotors, or lithium mining. The author collects PDFs and articles into a folder, never reads them twice, and three months later cannot remember which source said the thing. This skill keeps `research/ledger.md`: one entry per source, each with a two-paragraph summary, a "usable in which book?" note, and the exact local filename — so every claim in a draft can be traced back to a page the author actually owns.

## Instructions

1. **Work only from the folder the author names** (e.g. `research/sources-2026/`). Do not fetch web pages; if the author hands you a URL, they save the article themselves and you summarize the saved file.
2. **One entry per source**, appended to `research/ledger.md` under the topic heading that fits (create headings as needed). Entry shape:

   ```
   ### <short source title>
   - file: sources-2026/<filename>
   - type: pdf-article | book excerpt | interview transcript | note
   - claimed by author on: (date added)
   - TL;DR (2–3 sentences, plain words)
   - Key numbers (only figures actually in the source, each with its page/section)
   - Usable for: <book/scene/essay> — or — "background only"
   - Cautions: dated data? interest groups? translation?
   ```

3. **Quote-don't-paraphrase numbers.** If the ledger says "crossing takes 40 minutes at winterTemp," the source file must contain that; cite the page. If you cannot find it, write `[verify]` and move on.
4. **Digest pass, on request:** when a topic heading has ≥ 5 entries, write a `## Digest — <topic>` subsection that lays out agreements and disagreements between sources in plain prose, citing entry titles as anchors ("the 2020-11 report disagrees with the deckhand memoir about speed — see both entries").
5. **Never merge claims silently.** If two sources disagree, the digest says so and gives both, with the author deciding later.
6. **Summaries are written to be checkable:** short, concrete sentences; no opinions added; no "clearly," no "obviously."
7. **Optional model support:** if the author wants a plainer-words gloss of a dense passage, use `tools/drafts.py` with their local model and label the gloss `model-assisted` so it is reviewed like any draft.

## Worked example

See `examples/worked-example.md` for three sources summarized, one `[verify]` flag, and a digest of a disagreement.

## Local-first workflow

- Input and ledger both live in-repo (`research/**`). The ledger is the citation anchor for the whole series.
- No API keys in this workflow; any model call runs through the pack's local `tools/drafts.py` config only if the author opted in.

## Troubleshooting

- **Locked PDF/failing extraction:** note `text not extractable; skim summary from abstract only` in the entry, and never guess at body content.
- **Ledger grows unwieldy:** split by year (`ledger-2026.md`) and keep `ledger.md` as an index linking the parts.
