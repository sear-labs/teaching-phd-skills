---
title: Accessibility of notebooks and figures
channel: writing
tier: year 2
milestone: M4
time: 3 hours
prerequisites: 18-figures-tables
submit_as: repo URL
---

## Why this exists

This one has a date. The DOJ's 2024 Title II rule makes **WCAG 2.1 Level AA** the standard for
web content a covered entity makes available, and a public university is a covered entity.
For entities serving 50,000 or more people the compliance date is **26 April 2027**. A public
repo with a hosted-notebook badge is web content. Course material is web content.

The practical argument is simpler than the legal one: **alt text is a one-sentence cost at
authoring time and a project in retrospect.** Writing it as you make the figure is free.
Retrofitting it across four years of notebooks is a semester.

No external curriculum teaches this for notebooks. That is why it is here.

## External material

[WebAIM's alternative text guide](https://webaim.org/techniques/alttext/) — the best practical
treatment of what alt text should actually say. The [WCAG 2.1 quick
reference](https://www.w3.org/WAI/WCAG21/quickref/?currentsidebar=%23col_customize&levels=aaa)
filtered to Level AA, for the criteria themselves. Both are written for web pages. Neither
covers notebooks, so the mapping below is the mechanic.

## Governing part

**Part 3** notes the obligation. The standard does not restate the WCAG criteria and neither
does this lesson; go to the source for those.

## The mechanic

Take one public notebook or figure set — the handbook repo itself is a legitimate target if you
do not yet have a public notebook.

- **Alt text describes what the figure *shows*, not what it *is*.** "Bar chart of results" is
  useless. "Lithium demand under three recycling scenarios, diverging after 2032, with the
  high-recycling case 40% below baseline by 2040" is alt text. Write the takeaway.
- **Heading order with no skipped levels.** `#` then `##` then `###`. A screen reader user
  navigates by heading; a skipped level reads as a missing section.
- **No colour-only encoding** — this is the same requirement as skill 15, arriving from a
  different direction. Do both at once.
- **Tables get real header rows.** A markdown table with a header separator row is fine; an image
  of a table is not.
- **Body text contrast at least 4.5:1.** Check it rather than eyeballing it.

## Deliverable

Repo URL.

## Competency check

- [ ] Every figure has alt text naming the trend or takeaway, not the chart type
- [ ] No heading level is skipped anywhere in the notebook
- [ ] Greyscale check passed
- [ ] Tables have header rows and are not images
- [ ] Body text contrast measured at 4.5:1 or better, with the measurement stated

## Log entry

Writing. How long the alt text actually took, and your estimate of what retrofitting your whole
repo would cost.
