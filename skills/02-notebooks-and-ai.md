---
title: Notebooks and AI assistance
channel: arithmetic
tier: year 1
milestone: M1
time: 4 hours
prerequisites: none
submit_as: notebook link (view access) plus the verification table, in a WA entry
---

## Why this exists

The failure mode is not a bad answer. It is a plausible one. A model will hand you a GurobiPy
snippet setting a variable bound that does not exist in your model, or a citation to a paper
nobody wrote, in the same confident register it uses when it is right. Students who have never
systematically checked a model's output learn to trust it at the scale of small questions and
then apply that trust to a thesis chapter.

Notebooks add their own version. Colab resets; a notebook that ran in March fails in September
because a package moved a default, and nothing records what it was running when the numbers were
right.

## External material

Anthropic's [prompt engineering
guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) covers
getting a better answer. It does not cover finding out whether the answer is true. Colab's
[welcome notebook](https://colab.research.google.com/notebooks/intro.ipynb) covers the
interface, and actively encourages the ad-hoc installs this lesson exists to undo.

## Governing part

The standard governs notebooks in **Part 3**, and rules on the boundary between a notebook and
`src/` in **Part 4**.

## The mechanic

**Rebuild an analysis you have already done by hand,** so you know the answer before you start.

Record the environment in the first cell — Python version and `!pip freeze`. This is not
decoration; it is the only thing that will let you explain a divergence later. Set a seed.
State the expected answer in a markdown cell **before** the computation, then run it.

If the numbers differ, reconcile them in the notebook. A divergence you explain is a result. A
divergence you delete is a future bug.

**Along the way, run three prompts that differ in structure, not wording:** the bare task; the
task plus what the model needs to know about your system; the same plus an explicit instruction
to flag what it is unsure about.

Then build the table that is actually the deliverable. One row per factual claim across all
three outputs: the claim, a mark of **verified / unverified / wrong**, and *how you checked*.
"It looked right" is not a check.

## Deliverable

Notebook share link with **view access enabled** — test it in an incognito window, because a
link only you can open is the most common reason this comes back. Plus the verification table.

## Competency check

- [ ] Link opens for someone who is not the author
- [ ] First cell shows interpreter version and pinned package versions; seed set
- [ ] The hand-computed answer appears before the code that recomputes it
- [ ] Any divergence reconciled in writing, not removed
- [ ] Three structurally different prompts, not rewordings
- [ ] Every factual claim is a row, each naming a specific verification method
- [ ] At least one claim identified as wrong or unverifiable

## Turning it in

**This replaces your arithmetic entry for the week you do it.** Submit it to that week's
**WA** assignment in Canvas — the same one you would have submitted anyway. It is not an
extra piece of work on top of the log.

- **In the text box:** whether the notebook agreed with your hand result, and what the model got wrong.
- **Include or attach:** notebook link (view access) plus the verification table, in a WA entry

You do not submit anything to the milestone yet. When all five skills in **M1** are done, submit the **M1 — The Workbench** assignment, which is just
an index saying which week each one went in.
