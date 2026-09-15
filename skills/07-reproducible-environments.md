---
title: Reproducible environments
channel: arithmetic
tier: year 1
milestone: M2
time: 4 hours (plus your partner's 1 hour)
prerequisites: 06-code-folder-structure
submit_as: repo URL plus your partner's signed run log
---

## Why this exists

There is exactly one test of whether an environment is reproducible, and it is not a file
listing. It is: **a labmate ran it and got your number.** Everything else is a proxy. This lab's
stack makes the proxy especially untrustworthy — Gurobi, CPLEX and GAMS all change behaviour
across versions in ways that move a solution without producing an error, and ReEDS carries its
own version-sensitive assumptions.

## External material

[The Turing Way](https://book.the-turingway.org/reproducible-research/renv), reproducible
environments chapter. It covers the concepts and the tooling landscape well. The standard is
sharper on what specifically has to be recorded, and that specificity is the thing being graded
here — read the standard's dependency rule directly.

## Governing part

The standard's dependency rule. It states what must be recorded and in what combination; this
lesson deliberately does not restate it.

## The mechanic

Pair with another student in the class.

Your partner, **on their own machine**, working from your README alone, reproduces one named
figure from your work. You may not help. You may not be in the room. Any question they have to
ask you is a defect in the README, and it goes in the log.

They write the run log: what they ran, what broke, what they had to guess. They sign it. If the
number differs, that is not automatically a failure — but you must state a tolerance and say
whether the divergence sits inside it. A tolerance chosen after seeing the divergence is not a
tolerance.

## Deliverable

Repo URL plus your partner's signed run log.

## Competency check

- [ ] Partner reproduced the named figure on their own machine, or the divergence is explained
- [ ] Stated tolerance appears before the comparison, not after
- [ ] Solver version and interpreter version both recorded in the repo
- [ ] Every question the partner had to ask is listed as a README defect
- [ ] README updated in response

## Log entry

Arithmetic. What your partner could not do without asking you.
