# Worked Example — Blurb A/B Note-Taker

The author is testing blurb families for *Cold Channel* on the Amazon detail page and in one newsletter issue.

## Files

- `blurb-log.csv` (the log)
- `blurbs/lightning-cold.md`, `blurbs/whisper-cold.md` (full text lives in files; the log indexes them)

## The log after registering three variants

```csv
id,family,slug,text_file,placement,date_started,result,date_ended,notes
1,lightning,cold-amazon-l,blurbs/lightning-cold.md,amazon-short-blurb,2026-10-14,,, launch variant
2,lightning,cold-news,blurbs/lightning-cold.md,newsletter-2026-10,2026-10-14,,, same text on the newsletter
3,whisper,cold-amazon-w,blurbs/whisper-cold.md,amazon-short-blurb,2026-10-28,,, moody variant after launch
```

## Recording a result (append)

Amazon's dashboard showed 1,042 detail-page visits and 61 sample downloads in the first two weeks for row 1. The author copies the numbers from the dashboard into `data/kdp-weekly.csv` and asks the skill to log them. To keep the log append-only, results are APPENDED as their own rows that reference the original id:

```csv
4,lightning,cold-amazon-l-result,.,amazon-short-blurb,2026-10-14,61 of 1042 sample downloads (measured),2026-10-28,numbers from kdp-weekly.csv; result for id 1
```

Later, when the row closes out, the author may also backfill row 1's `result` and `date_ended` fields — that is an author choice, not a skill rewrite.

## Comparison the skill writes when asked

```markdown
# Blurb A/B read — 2026-11-05

## Family: lightning (2 placements)
- Amazon, weeks 1–2: 61 of 1,042 sample downloads (measured).
- Newsletter: no click data was imported; treat as no signal.

## Family: whisper (1 placement)
- Amazon, weeks 3–4: 44 of 980 sample downloads (measured).

## Read
Lightning had the better download rate where it ran, but it ran during launch
momentum, which is a confound, and whisper has less data. Treat this as "worth
one more quiet-week test," not as a winner.
```

## What this example shows

- One row per variant per placement; results appended as new rows.
- Full blurb text lives in files; the log points to them.
- Results are marked `(measured)` or flagged as estimates.
- No winner is declared from a small or confounded sample.
