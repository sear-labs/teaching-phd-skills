---
title: Excel with AI assist
channel: arithmetic
tier: year 1
milestone: M1
time: 2 hours
prerequisites: 01-basic-excel, 02-ai-prompting
submit_as: .xlsx plus written explanation, in a WA entry
---

## Why this exists

AI is very good at generating Excel formulas, and very good at generating ones that are
subtly wrong: an absolute reference that should have been relative, a range that stops one
row above the last data row, a lookup that silently returns the first match when you needed
the exact one. The formula runs. It produces a number. Nothing announces the error. If you
cannot read the formula back in your own words, you have no way to catch it.

## External material

None beyond skills 01 and 02. This one is deliberately short and deliberately uncomfortable.

## Governing part

None.

## The mechanic

Pick something you genuinely could not write yourself — a nested `INDEX`/`MATCH`, a dynamic
array formula, a small VBA macro. Have it generated.

Then, before you trust it:

1. **Annotate every argument in your own words.** Not the documentation's words. If you cannot
   say what an argument does, you do not yet have the formula, you have a guess that works.
2. **Break it on purpose.** Change one input — delete a row, add a duplicate key, blank a cell.
   Write down what you predict the formula will return *before* you run it. Then run it.

The prediction step is the assessment. Getting it right means you understand the formula.
Getting it wrong is more useful, and you should say so rather than quietly fixing the note.

## Deliverable

The `.xlsx` plus the annotation and the prediction, in that week's WA entry.

## Competency check

- [ ] The formula or macro works on the real data
- [ ] Every argument annotated in the student's own words
- [ ] A specific break was applied, described
- [ ] The prediction was written before the result, and both are shown

## Log entry

Arithmetic. What you could not have written yourself, and whether your prediction held.
