# Workflow Notes for the Blurb A/B Note-Taker

Registering a variant:

1. Confirm or create `blurb-log.csv` from `templates/blurb-log.csv` (pack root).
2. Save the full blurb text as `blurbs/<slug>.md` in the author's repo.
3. Append one row: id, family, slug, text_file, placement, date_started, empty result, empty date_ended, notes.
4. If it is an agent-drafted variant, also append `source: drafted` to the notes so drafts never mix with tested text silently.

Recording a result:

1. Read only local files the author imported (e.g. `data/kdp-weekly.csv`).
2. Append a result row referencing the original id; add `(measured)` for real numbers or `(estimate)` for rough ones.
3. Never copy reader names, emails, or account data into the log.

Comparing:

1. Group rows by family; group results by placement.
2. State sample sizes; flag confounds (launch timing, price changes, ads running).
3. End with at most one recommendation, phrased as a next test, never as a proven rule.
