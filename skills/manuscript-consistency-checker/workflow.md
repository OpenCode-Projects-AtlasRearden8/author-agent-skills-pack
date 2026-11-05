# Workflow Notes for the Manuscript Consistency Checker

Intended for agents (and for the author reviewing what an agent will do).

Order of operations:

1. Discover manuscript files (`manuscript/**`, or ask once).
2. Create/refresh `consistency/ledger.md` so a run can resume after a context break.
3. Read and ledger, slice by slice, in order.
4. Compare ledger entries; grade findings (certain / likely / note).
5. Append new rows to `consistency/findings.csv`; never silently overwrite rows from a previous run — add a `rerun` id instead.
6. Write `consistency/findings.md` as a fresh file each run; it is a report, the CSV is the durable log.
7. End with the batch of questions for the author, all in one place.

Out of scope by design: rewriting prose, judging style quality, fact-checking against the real world (this skill checks the book against *itself*).
