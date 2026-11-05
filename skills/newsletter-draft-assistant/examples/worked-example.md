# Worked Example — Newsletter-Draft Assistant

## Inputs the agent is handed (all local)

`notes/2026-10/notes-lightning.md`:

> Finished the *Cold Channel* Lightning/Whisper blurb tests (see blurb log). One finding so far: launch-week momentum confounds the first read.

`notes/2026-10/notes-manual.md`:

> Reader question I keep getting: "Do I really need an API key to try AI on my own PC?" Answer: no — Ollama runs locally with no key at all. This deserves a short explainer.

`data/launch-dates.md`:

> Cold Channel audiobook: mid-February 2027 (unconfirmed).

## Step 1 — Planner check

`newsletter/planner.md` (from template): greeting → what happened → explainer → book news → links → sign-off. Fit is good; the explainer slot goes to the Ollama question.

## Step 2 — Draft `newsletter/2026-11/draft.md`

```markdown
# The Cold Channel — November 2026

## Hi from Dylan

Two boat-loads of news this month, one short lesson. Let's get to it.

<!-- [begin draft: model-assisted opener reviewed] -->

## What happened in October

- Finished the blurb tests (lightning vs. whisper variants). Early read:
  launch momentum made week one flattering to whichever blurb ran then.
  One more quiet-week test is planned before picking the back-cover text.
- *Cold Channel* audiobook is aiming at mid-February 2027. [check: not
  confirmed yet — treat as "aiming," not promised.]

## The one-minute lesson: AI on your own PC, no key required

A question I hear from beginners a lot: "Do I need to sign up for stuff —
API keys, subscriptions — to try AI on my own computer?" No. Tools like
Ollama run entirely on your machine: download the app, pick a model, type.
Nothing is sent to anyone. That's it. That's the whole trick — the part
everyone assumes is complicated is the part that's just... an app.

## Coming up

The next issue will have the settled blurb read and a chapter-openings
sneak peek. [optional]

## Worth a click
- dylanasdale.github.io — the hub for The Massive AI Manual and these guides.
- Your local server list goes here — one line each on why it's worth your click.

## — Dylan

<!-- [end draft] -->
```

## Final folder layout after the author edits and sends

```
newsletter/2026-11/
├── draft.md      # the near-final copy
├── links.md      # link list used this issue
└── sent.md       # one-line note + send date, filled by the author
```

## Local section

`links.md` in this example:

```markdown
# Links used in 2026-11
- dylanasdale.github.io — hub site for the manual and this letter
```
