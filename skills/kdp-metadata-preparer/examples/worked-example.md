# Worked Example — KDP Metadata Preparer

Fictional paperback+ebook: *Cold Channel*, book 1 of the Harbor Line mysteries by Dylan Asdale. Sources: `canon/factsheet.md`, `blurb-log.csv` (lightning family won the quiet-week retest), the author's trim notes (5×8" paperback).

## `metadata/kdp.yaml`

```yaml
title: Cold Channel
subtitle: A Harbor Line Mystery
author: Dylan Asdale
series_name: Harbor Line
series_number: 1
language: English
publication_date: 2027-03-10  # [check] date not final
adult_content: no
trim_size: 5x8 in  # from author notes; double-check on KDP paperback wizard
keywords:
  - phrase: amateur sleuth small town
    reason: genre expectation; readers search town-noir terms
    length: 29
  - phrase: cold case mystery
    reason: matches the 1996 ferry accident spine
    length: 18
  - phrase: ferry town murder mystery
    reason: specific setting hook
    length: 26
  - phrase: quiet coastal crime series
    reason: "coastal" audience overlap
    length: 27
  - phrase: cozy-adjacent noir
    reason: tone bridge between genres
    length: 18
  - phrase: independent series starter
    reason: book 1 positioning
    length: 27
  - phrase: kindle unlimited mystery
    reason: KU readers filter on this
    length: 25
book_description: |
  <b>A cold case runs aground.</b><br><br>
  Marcus Reyes has spent twenty years deckhanding the River Bay ferry,
  telling himself the summer of '96 was just an accident. Then Marla
  Devereaux, a boat mechanic with a talent for engines and an allergy
  to authority, finds the date carved on a hull panel that should not
  exist.<br><br>
  <i>Harbor Line book 1.</i> A quiet coastal mystery about the stories
  a small town tells itself in order to keep its morning schedule.
categories:
  - suggestion: Mystery & Thrillers > Cozy Mysteries
  - suggestion: Mystery & Thrillers > Small Town & Rural
  - note: pick 2–3 on the KDP site, mirrored for ebook categories
pricing:
  note: stub only — verify 60% royalty tier math on the KDP site before print; no prices stored in repo files
```

## Count table the skill prints when it finishes

```
title            12/200   ok
subtitle         21/200   ok
description    397/4000   ok (350-ish words trimmed to fit the read-more fold)
keyword 1        29/50    ok   (7 of 7 keywords present)
keyword 2..7     18–27    ok
```

## Checklist printed after the YAML validates

```
Pre-upload (have ready)
[ ] Interior manuscript EPUB, spellcheck pass complete (consistency findings all resolved)
[ ] Cover: ebook JPG, paperback full-wrap PDF at 5x8" trim
[ ] ISBN choice: free KDP or author-owned

On kdp.amazon.com (manual walkthrough)
[ ] Paperback + ebook tabs: enter title/subtitle exactly as in kdp.yaml
[ ] Keywords: paste in the order above
[ ] Description: paste the HTML block; preview it
[ ] Categories: pick from the suggestions list
[ ] Adult flag: no; pricing: verify royalty math on site
[ ] After publish: write metadata/kdp-submitted.md stub
```

## What this example shows

- Justifications sit next to keywords so the author can veto with a reason.
- HTML is restricted to the allowed set; links and `<h1>` never appear.
- Counts are computed, not eyeballed.
- Nothing about tax, bank, or real submission credentials is stored.
