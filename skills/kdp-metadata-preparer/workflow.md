# Workflow Notes for the KDP Metadata Preparer

1. Collect inputs: the book title/dir, `canon/factsheet.md`, `blurb-log.csv`, trim/price notes.
2. Draft `metadata/kdp.yaml` from `templates/kdp-metadata.yaml` (pack root).
3. Compute and print counts: title, subtitle, description, each of the 7 keywords; fix overflows before showing the author.
4. Make sure the description HTML uses only `<b> <i> <br> <h4>-<h6> <ul> <ol> <li>`; no links, no claims of bestseller status, no other-author comparisons.
5. Keywords: 7 present, each ≤ 50 chars, no author names, no "free"/"sale", no misleading claims.
6. Print the pre-upload + on-site checklist for the author to walk through manually.
7. The author's post-submission stub file `metadata/kdp-submitted.md` is written by the author only.

Series hygiene: if `metadata/` holds previous books' kdp.yaml files, cross-check series_name and author spellings.
