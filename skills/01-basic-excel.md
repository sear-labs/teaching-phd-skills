---
title: Basic Excel
channel: arithmetic
tier: year 1
milestone: M1
time: 3 hours
prerequisites: none
submit_as: .xlsx attached to a WA entry
---

## Why this exists

Spreadsheets are where most lab data first lands, and where most silent errors are born: a
formula dragged one row short, a sort that moved one column and not its neighbours, a
constant typed into a cell six months ago that nobody can now explain. Reviewers never see
the spreadsheet. They see the number it produced. The difference between a number you can
defend and a number you can only reproduce by remembering what you clicked is structure.

## External material

Microsoft's own Excel training, [support.microsoft.com/excel](https://support.microsoft.com/excel) —
specifically the XLOOKUP, PivotTable, and named-range lessons. It covers the mechanics of each
feature well. It says nothing about how a spreadsheet should be organised when the output is
going into a paper, which is the whole of the mechanic below.

## Governing part

None directly. If the spreadsheet is an input to a repo, the standard's rule on immutable
inputs (Part 1) governs the file once it lands there.

## The mechanic

Take one real dataset from your own work — not a sample.

1. Raw data goes on its own sheet and is never edited. Not a correction, not a unit change.
2. Give that range a name.
3. Every transformation happens on a second sheet, referencing the first by name.
4. Build one pivot that answers a question you actually have.
5. Build one chart with labelled axes and units.

The rule underneath all five: **any cell a reader cannot trace back to the raw sheet is a
number you cannot defend.** A hard-coded constant inside a formula is the most common way
that happens — put it in a labelled cell and reference it.

## Deliverable

The `.xlsx`, attached to that week's WA entry.

## Competency check

- [ ] A raw sheet exists and no formula writes to it
- [ ] At least one named range is used in a formula
- [ ] No bare numeric constant inside a formula except 0, 1, and unit conversions documented on a sheet
- [ ] One pivot table, answering a stated question
- [ ] One chart with both axes labelled and units given

## Log entry

Arithmetic. Which dataset, what question the pivot answered, and one error the structure
caught that you would otherwise have shipped.
