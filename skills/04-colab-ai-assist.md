---
title: Colab with AI assist
channel: arithmetic
tier: year 1
milestone: M1
time: 3 hours
prerequisites: 02-ai-prompting
submit_as: Colab share link (view access) in a WA entry
---

## Why this exists

Colab resets. A notebook that ran in March fails in September because a package moved a
default, and nothing in the notebook records what it was running when the numbers were right.
This is the same failure as "I cannot reproduce my own Chapter 3", arriving early and cheaply.
The habit worth building is one cell wide: record what actually ran, at the top, every time.

## External material

Colab's own [Welcome notebook](https://colab.research.google.com/notebooks/intro.ipynb) covers
the interface — cells, runtime, mounting Drive. It does not cover recording an environment, and
it actively encourages the habit of installing packages ad hoc that this lesson exists to undo.

## Governing part

The standard governs notebooks in **Part 3**, and rules on the boundary between a notebook and
`src/` in **Part 4**. Read them; this lesson will not summarise them.

## The mechanic

Rebuild an analysis you have **already done by hand** — so you know the answer before you start.

- First cell records the Python version and `!pip freeze` output. This is not decoration; it is
  the only thing that will let you explain a divergence later.
- Set a seed for anything stochastic.
- **State the expected answer in a markdown cell before the computation.** Then run it.
- If the numbers differ, reconcile them in the notebook. A divergence you explain is a result.
  A divergence you delete is a future bug.

## Deliverable

Colab share link with **view access enabled** — check this in an incognito window, because a
link that only you can open is the single most common way this gets returned.

## Competency check

- [ ] Link opens for someone who is not the author
- [ ] First cell shows interpreter version and pinned package versions
- [ ] Seed set wherever there is randomness
- [ ] The hand-computed answer appears before the code that recomputes it
- [ ] Any divergence is reconciled in writing, not removed

## Log entry

Arithmetic. Which analysis, and whether the notebook agreed with your hand result.
