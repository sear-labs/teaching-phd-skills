---
title: LaTeX and Overleaf
channel: writing
tier: year 2
milestone: M4
time: 4 hours
prerequisites: 13-imrad, 11-citation-verification
submit_as: Overleaf link plus compiled PDF
---

## Why this exists

Submissions stall on formatting, and they stall late — at the point where the science is done
and the only thing between you and a submitted paper is a template you have never opened. The
second failure is quieter: a journal template is a **contract about length**, and a draft
written in Word at 1.15 spacing has no idea whether it fits. Finding out at submission that you
are four pages over means cutting under deadline, which means cutting badly.

## External material

Overleaf's [Learn LaTeX in 30
minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes) — syntax, environments,
compiling. It covers the language. It does not cover journal templates or managing a
bibliography at the scale of a real paper, both of which are below.

## Governing part

None.

## The mechanic

1. **The real journal's official template**, downloaded from the journal, named in your
   submission. Not a generic article class, not a template from a different journal that looks
   similar. IEEE, Elsevier, and INFORMS classes all differ in ways that matter.
2. **Your actual draft** in it, not lorem ipsum.
3. **BibTeX exported from your reference manager.** Not typed by hand — hand-typed entries are
   where the failures from skill 11 reappear.
4. **Compile with zero errors.** Then read the warnings, which is the step everyone skips.
   Overfull hbox warnings are how you find out a table is wider than the column.
5. Check the page count against the journal's stated limit.

## Deliverable

Overleaf link plus the compiled PDF.

## Competency check

- [ ] The template is the journal's official one, named
- [ ] Compiles with zero errors
- [ ] Warnings read, and any overfull box in a figure or table resolved
- [ ] Bibliography generated from a `.bib` file, not hand-written
- [ ] Page count stated against the journal's limit

## Log entry

Writing. Which journal's template, and how far over or under the limit you landed.
