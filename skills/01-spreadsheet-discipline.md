---
title: Spreadsheet discipline
channel: arithmetic
tier: year 1
milestone: M1
time: 3 hours
prerequisites: none
submit_as: .xlsx plus the annotation, in a WA entry
---

## Why this exists

Spreadsheets are where most lab data first lands and where most silent errors are born: a
formula dragged one row short, a sort that moved one column and not its neighbours, a constant
typed into a cell six months ago that nobody can now explain. Reviewers never see the
spreadsheet — they see the number it produced. And AI is very good at generating Excel formulas,
and equally good at generating ones that are subtly wrong: an absolute reference that should
have been relative, a lookup returning the first match when you needed the exact one. The
formula runs. It produces a number. Nothing announces the error.

## External material

Microsoft's [Excel training](https://support.microsoft.com/excel) — the XLOOKUP, PivotTable and
named-range lessons. It covers the mechanics of each feature. It says nothing about how a
spreadsheet should be organised when the output is going into a paper, which is the mechanic
below.

## Governing part

None directly. Once the spreadsheet is an input to a repo, the standard's rule on immutable
inputs (Part 1) governs the file.

## The mechanic

One real dataset from your own work. Not a sample.

**Structure it so every number is traceable.**

1. Raw data on its own sheet, never edited. Not a correction, not a unit change.
2. Name the range.
3. Every transformation on a second sheet, referencing the first by name.
4. One pivot answering a question you actually have.
5. One chart with labelled axes and units.

The rule underneath: **any cell a reader cannot trace back to the raw sheet is a number you
cannot defend.** A bare constant inside a formula is the usual way that happens — put it in a
labelled cell and reference it.

**Then get AI to write something you could not have written yourself** — a nested
`INDEX`/`MATCH`, a dynamic array, a small VBA macro. Before you trust it:

- **Annotate every argument in your own words.** Not the documentation's. If you cannot say what
  an argument does, you do not have the formula, you have a guess that works.
- **Break it on purpose.** Delete a row, add a duplicate key, blank a cell. Write your predicted
  output *before* running it.

Getting the prediction wrong is more useful than getting it right, and you should say so rather
than quietly fixing the note.

## Deliverable

The `.xlsx` plus the annotation and the prediction, in that week's WA entry.

## Competency check

- [ ] Raw sheet exists and no formula writes to it
- [ ] At least one named range used in a formula
- [ ] No bare numeric constant inside a formula except 0, 1, and documented unit conversions
- [ ] One pivot answering a stated question; one chart with axes labelled and units given
- [ ] An AI-generated formula, with every argument annotated in the student's own words
- [ ] A deliberate break, with the prediction shown before the result

## Turning it in

**This replaces your arithmetic entry for the week you do it.** Submit it to that week's
**WA** assignment in Canvas — the same one you would have submitted anyway. It is not an
extra piece of work on top of the log.

- **In the text box:** what you could not have written yourself, whether your prediction held, and one
error the structure caught.
- **Include or attach:** .xlsx plus the annotation, in a WA entry

You do not submit anything to the milestone yet. When all five skills in **M1** are done, submit the **M1 — The Workbench** assignment, which is just
an index saying which week each one went in.
