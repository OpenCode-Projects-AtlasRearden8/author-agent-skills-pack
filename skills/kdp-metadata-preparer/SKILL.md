---
name: kdp-metadata-preparer
description: Assembles complete KDP-ready metadata for a book — title, subtitle, description with HTML, keywords, categories, age/territory flags — as a reviewable YAML file and a paste-ready checklist.
version: 1.0.0
local-first: true
requires-model: false
files:
  - examples/worked-example.md
  - workflow.md
  - ../../templates/kdp-metadata.yaml
---

# KDP Metadata Preparer

## Purpose

Getting a book onto Kindle Direct Publishing stumbles on the small fields: the seven keyword slots, the right categories, the description HTML, the age-appropriateness flags. This skill fills `metadata/kdp.yaml` for one book from the author's local files (factsheet, blurb log, draft cover notes), checks every field against current KDP limits, and prints a step-by-step checklist for the author to walk through on kdp.amazon.com by hand. The skill never logs into any site.

## Instructions

1. **Read the local sources:** the book's `canon/factsheet.md` (if the series keeper is in use), `blurb-log.csv` (a winning family gives the description spine), and the author's notes on the trim size / pricing call.
2. **Produce `metadata/kdp.yaml`** following `templates/kdp-metadata.yaml` (pack root). Required fields:
   - `title`, `subtitle` (subtitle optional but recommended), `author`, `language`.
   - `book_description` (Amazon allows up to 4,000 characters; we aim for 200–350 words) with the first 110 words doing all the work — the "read more" fold eats the rest.
   - Allowed HTML in descriptions: `<b>`, `<i>`, `<br>`, `<h4>`–`<h6>`, `<ul>`, `<ol>`, `<li>`. No `<h1>`–`<h3>`, no CSS, no links.
   - `keywords`: exactly **7** keyword phrases the author chooses, each ≤ 50 characters. Keywords must reflect the *genre expectation*, not random famous names; no competitor author names, no "free," nothing misleading.
   - `categories`: 2–3 candidates listed as suggestions — final choice happens on the KDP site by the author.
   - `publication_date`, `adult_content: no/yes` (flag honestly), `territorial_rights` note, `pricing` stub (KDP prints the royalty math itself; keep the stub as a reminder to check the 60% list-price tiers).
3. **Verify character counts programmatically, not by eye.** Count title (≤ 200), subtitle (≤ 200), description (≤ 4,000), each keyword (≤ 50), and print the counts in a small table when you finish.
4. **Print the checklist** the author will walk through on the KDP site, split pre-upload ("things to have ready: cover PDF/EPUB at correct trim, interior file, ISBN choice") and during ("enter the 7 keywords in this order," "enter description in the description box, not the bookshelf notes").
5. **Mark unverified claims** with a `[check]` comment in the YAML (launch dates, comparisons like "readers of X will love this" — comparisons to other authors are not allowed in keywords anyway).
6. **No invented facts, no secrets:** pricing decisions, tax, and bank details never appear in any file this skill writes.

## Worked example

See `examples/worked-example.md` for a complete `kdp.yaml` for a fictional title, including the seven keywords with their justifications, the description with allowed HTML, the count table, and the checklist.

## Local-first workflow

- Input and output files are all in-repo: `metadata/kdp.yaml` is the artifact; a sibling `metadata/kdp-submitted.md` gets a stub for the author to tick by hand after they walk Amazon kindly.
- Submissions are manual by the human at kdp.amazon.com; the skill's job ends at "paste-ready."

## Troubleshooting

- **Series book:** add `series_name` and `series_number`; check consistency with the previous book's metadata file so series pagination lines up.
- **Description rejected by Amazon:** usually a forbidden tag or a claim of bestseller status; strip claims, keep tone honest.
