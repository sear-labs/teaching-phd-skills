---
title: Sanity checks and orders of magnitude
channel: arithmetic
tier: year 1
milestone: M1
time: 3 hours
prerequisites: none
submit_as: text entry in a WA entry
---

## Why this exists

The errors that survive code review are the ones where **the code is correct and the number is
wrong.** A diff will not catch a capacity in MW that should have been GW, a price in $/tonne
read as $/kg, or a discount rate entered as 7 instead of 0.07. The model runs, converges,
reports a clean objective, and the answer is off by a thousand.

These survive because nobody looked at the number and asked whether it was plausible. That
asking is a skill, it is fast, and almost nobody is taught it.

## External material

None worth assigning as a course. The reference values are in your own field: ERCOT's [grid
reports](https://www.ercot.com/gridinfo) for demand and capacity, the EIA's [Annual Energy
Outlook](https://www.eia.gov/outlooks/aeo/) for costs and generation, USGS [Mineral Commodity
Summaries](https://www.usgs.gov/centers/national-minerals-information-center) for production
volumes and prices. Learn where your field keeps its true numbers; that is most of the skill.

## Governing part

None.

## The mechanic

Three checks, on one of your own results.

**1. Predict before you run.** Write the answer you expect and its order of magnitude, in
advance, in writing. Not precisely — within a factor of ten is the whole point. If you cannot
predict it to a factor of ten, you do not yet understand the model well enough to interpret what
it returns, and that is worth discovering now rather than in a committee meeting.

**2. Check the units, everywhere.** Every input, every output, every axis. MW or MWh. $/MWh or
$/kW-yr. Tonnes or kilotonnes. Nominal or real dollars, and in which year's dollars. Most
order-of-magnitude errors are unit errors wearing a disguise.

**3. Anchor to a published number.** Find one external reference value your result should be
near — a reported ERCOT peak, a published LCOE range, a USGS production figure — and compare.
State the source. If you are off by more than a factor of two, you have either found something
or broken something, and you must say which.

**4. If you ran a solver, read the log rather than the status word.**

`OPTIMAL` is printed by a solver that stopped for any reason it considers acceptable, including
hitting a gap tolerance you set and forgot. Three things to look at every time:

- **The status word against the actual residual.** The standard makes this point in Archetype P:
  read the residual. A status word is the solver's opinion; the residual is a number.
- **The MIP gap you actually achieved**, not the one you asked for. A 15% gap reported as
  optimal is a 15% gap.
- **What the log says when it says infeasible.** Which constraint, at which index. Solvers name
  it, and almost nobody reads far enough to find out.

If you do not run solvers, skip this one and say so.

Then **check one extreme**: what does the model do at zero, or at a very large value? Models
that behave absurdly at the boundary are often subtly wrong in the middle.

## Deliverable

Text entry: the prediction, the actual, the unit audit, the published anchor with its source,
and the extreme-case result.

## Competency check

- [ ] Predicted magnitude written before the run, with a timestamp or commit that proves it
- [ ] Units stated for every input and output involved
- [ ] One published reference value, cited with a source, and the comparison
- [ ] Any discrepancy over a factor of two explained, not waved through
- [ ] One extreme case run and its behaviour described
- [ ] If a solver was used: status word, achieved gap and residual all reported — or an explicit note that no solver was involved

## Log entry

Arithmetic. What you predicted, what you got, and which one was wrong.
