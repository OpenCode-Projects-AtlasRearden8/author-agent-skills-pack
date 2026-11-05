# Worked Example — Manuscript Consistency Checker

Sample input: a two-chapter slice from a (fictional) coastal mystery, showing the workflow end to end.

## Step 1 — Read and ledger

Sample chapters (excerpted):

**Chapter 3**

> "Marcus Reyes poured the last of the coffee. 'River Bay ferry' he said, 'ran aground the summer of '96. I remember — I was twelve.'"

**Chapter 4**

> "Mark had been riding the Harbor line since the ferry accident in 1998, the year he turned fourteen."

**Chapter 4 (later)**

> "Ellis Bay never froze, not even in the winter of 2001" — spoken by Marcus, the ferry's former deckhand.

**Chapter 5**

> "Marla killed the engine as they drifted past Harbor Pier. River Bay was another thirty miles north."

## Step 2 — Apply rule: "River Bay" vs. "Ellis Bay" vs. "the Harbor line"

The ledger after reading:

```
[Marcus Reyes] | seen ch3, ch4 | forms: Marcus, Mark, M. Reyes | PASS (nickname confirmed ch6: "everyone calls him Mark")
[River Bay ferry accident] | ch3 (1996), ch4 (1998) | status: FLAG-certain
[Ellis Bay] | ch4 | only mention; ch3/ch4 chatter is about River Bay | FLAG-likely
[Harbor Pier / Harbor line] | ch4, ch5 | PASS
[Distance River Bay] | ch5: thirty miles north | note only
```

## Step 3 — Report

```markdown
# Consistency Findings — *Cold Channel* — 2026-11-05

## Summary
1 certain, 2 likely, 1 note.

## Certain
1. **Ferry accident year.** Ch. 3 says Marcus was twelve in the "summer of '96";
   Ch. 4 says he has ridden the line since "the ferry accident in 1998, the year
   he turned fourteen." Both place the accident in his childhood but give
   different years. Suggested fix: pick one year and update both passages.

## Likely
2. **Ellis Bay vs. River Bay.** "Ellis Bay" (ch. 4) appears once; every other
   reference is "River Bay." Possible typo. Question for the author: are these
   two distinct towns, or should ch. 4 read "River Bay"?
3. **Ferry chronology.** If the accident was 1996 and Marcus was 14 in 1998
   (ch. 4), he was riding the line two years before the accident. Resolvable
   but worth a look once finding 1 is settled.

## Notes
4. **Marla / engine in ch. 5** — Marla is introduced without description;
   no conflict, just heads-up for a future pass.
```

## Step 4 — CSV rows (templates/consistency-findings.csv)

```csv
id,section,entity,certainty,quote_a,section_a,quote_b,section_b,suggestion,status
1,ch3/ch4,ferry accident year,certain,"summer of '96","ch3.1","the ferry accident in 1998","ch4.2","pick one year; align both",open
2,ch4,place name,likely,"Ellis Bay","ch4.5","River Bay","ch3.1","confirm town or correct",open
3,ch3/ch4,marcus age vs accident,likely,"aged twelve in 1996","ch3.1","fourteen in 1998; riding since accident","ch4.2","recheck after fix 1",open
4,ch5,new character intro,note,"Marla killed the engine","ch5.1","",,"no conflict",open
```

The author settles #1 (1996), fixes ch. 4, marks rows `resolved`, and reruns the skill before structuring edits.
