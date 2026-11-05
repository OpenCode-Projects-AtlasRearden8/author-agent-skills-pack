# Worked Example — Research Summarizer

Input folder: `research/sources-2026/` with three files the author saved and named:
`ferry-ops-report-2020.pdf`, `nps-coastal-history.md`, `deckhand-memoir-interview.txt`.

## Appended entries in `research/ledger.md`

```markdown
## Topic: Ferry operations

### Ferry services operational statistics 2020
- file: sources-2026/ferry-ops-report-2020.pdf
- type: pdf-article (publications office)
- TL;DR: Yearbook reporting ferry company counts, tonnage, and passenger flows
  for a country's fleet. Useful for realistic scale, not for drama.
- Key numbers:
  - typical coastal crossing windows: 30–50 min (table 4, p. 17)
  - winter service cutbacks: −18% sailings (p. 23)
- Usable for: Cold Channel book 2, the schedule subplot — background only
- Cautions: 2020 data, pre-service changes; check current year before
  printing any "today" numbers

### Deckhand memoir interview (day-of-accident recollection)
- file: sources-2026/deckhand-memoir-interview.txt
- type: interview transcript
- TL;DR: A deckhand's first-person account of the grounding; emotional
  texture, technical confusion in places.
- Key numbers:
  - "we ran at about eleven knots" (transcript §2) [verify against
    ops-report table 4 — memoir speeds conflict with other sources]
- Usable for: voice and texture for ch. 3 flashback
- Cautions: memory source, decades after; corroborate claims

## Digest — Ferry operations
The ops report's table-four range (30–50 min) covers the crossing the
series uses; the interview's "eleven knots" is not corroborated (see the
[verify] flag). Schedule believability: rely on the report; emotion:
rely on the interview. Both agree winter is the tight season.
```

## What this example shows

- One entry per source; file paths are exact, so any claim traces back.
- Numbers carry their page/section; anything unconfirmed gets `[verify]`.
- The digest contrasts sources instead of averaging them.
- No web access was needed or used; every file was author-supplied.
