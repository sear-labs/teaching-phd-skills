---
title: AI prompting
channel: arithmetic
tier: year 1
milestone: M1
time: 2 hours
prerequisites: none
submit_as: text entry in a WA entry
---

## Why this exists

The failure mode is not a bad answer. It is a plausible one. A model will hand you a GAMS
snippet that sets a variable bound which does not exist in your model, or a citation to a
paper that was never written, in the same confident register it uses when it is right.
Students who have never systematically checked a model's output learn to trust it — and the
trust is calibrated at the scale of small questions, then applied to a thesis chapter. This
exercise builds the checking habit while the stakes are still nothing.

## External material

Anthropic's prompt engineering documentation,
[docs.anthropic.com](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) —
structure, examples, giving the model room to reason. It covers how to get a better answer.
It does not cover how to find out whether the answer is true, which is the part that matters
here.

## Governing part

None.

## The mechanic

Pick one real task from your research — a formula you need, a literature question, a piece of
GurobiPy you would otherwise write by hand.

Run three prompts that differ in **structure**, not wording:

1. Bare: the task, nothing else.
2. With context: the task plus what the model needs to know about your system.
3. With context plus an explicit instruction to flag what it is unsure about.

Then build the table that is actually the deliverable. One row per factual claim across all
three outputs: the claim, a mark of **verified / unverified / wrong**, and *how you checked*.
"It looked right" is not a check.

## Deliverable

Text entry in that week's WA entry: the three prompts, the three outputs, and the
verification table.

## Competency check

- [ ] Three prompts differing structurally, not by rewording
- [ ] Every factual claim in the outputs appears as a row
- [ ] Each row names a specific verification method (ran it, looked up the DOI, checked the docs)
- [ ] At least one claim identified as wrong or unverifiable

## Log entry

Arithmetic. What you asked, what it got wrong, and how long the checking took relative to
doing it yourself.
