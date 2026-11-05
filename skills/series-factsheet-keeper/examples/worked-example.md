# Worked Example — Series Fact-Sheet Keeper

Setup: the author wrote two chapters of book 2 of a(n obviously fictional) maritime mystery series and runs the skill for the first time.

## Step 1 — Seed the factsheet

After reading the two chapters, `canon/factsheet.md`:

```markdown
# Series Factsheet — *Cold Channel* series — updated 2026-11-05

## Characters
- **Marcus Reyes** — ferry deckhand (book 1). Lost a hearing in left ear in ferry grounding (book 1, ch. 7) — canon.
- **Marla Devereaux** — ex-teacher, now boat mechanic; allergic to penicillin (book 2, ch. 2) — canon.
- *(unconfirmed)* **Riverside** — outline says Marla's hometown; no scene yet.

## Places
- **River Bay** — town on cold channel, ferry route north to Harbor Pier (book 1, ch. 1; book 2, ch. 1) — canon.
- **Ellis Bay** — ??? one mention in book 2 draft ch. 4 — CONFLICT with River Bay? (See consistency checker.)

## Rules
- Ferry crossing River Bay ↔ Harbor Pier takes 40 minutes in good weather (book 1, ch. 3) — canon.

## Open questions
- Is Ellis Bay a second town or a typo?
```

## Step 2 — Later: the author drafts book 2, ch. 6, and reruns the skill

New/changed facts found in the draft:

1. Marla treats a wound with antibiotics despite her allergy → **conflict**, certain.
2. Crossing Harbor Pier → River Bay "took half an hour" → **conflict** with the 40-minute canon fact.
3. Marla's hometown revealed to be Riverside → resolves an unconfirmed fact → **confirm**.
4. New fact: the ferry commission meets quarterly → **add**.

## Step 3 — Proposed diff (shown to author first)

```diff
- - **Marla Devereaux** — ex-teacher...allergic to penicillin (book 2, ch. 2) — canon.
+ - **Marla Devereaux** — ex-teacher, boat mechanic; allergic to penicillin (book 2, ch. 2) — canon ~draft ch. 6 treats wound with antibiotics; CONFLICT, check timeline.
- - **Ferry crossing River Bay ↔ Harbor Pier takes 40 minutes** (book 1, ch. 3) — canon.
+ - **Ferry crossing River Bay ↔ Harbor Pier takes 40 minutes** (book 1, ch. 3) — canon ~draft ch. 6 says "half an hour"; pick one.
- - *(unconfirmed)* **Riverside** — Marla's hometown.
+ - **Riverside** — Marla's hometown (book 2, ch. 6) — canon.
+ - Ferry commission meets quarterly (book 2, ch. 6) — canon.
```

The author approves items 1, 3, 4 and decides the crossing is really 40 minutes (fixes ch. 6). Diff applied with the `~draft` tags kept on the two conflicts until the prose is fixed.
