---
title: CLI agents and Claude Code
channel: arithmetic
tier: year 1
milestone: M2
time: 3 hours
prerequisites: 06-git-github, 02-ai-prompting
submit_as: transcript excerpt plus the accepted diff, in a WA entry
artifact: A **transcript excerpt** plus the **diff you accepted**, with your one-sentence task statement timestamped before the session began
---

## Why this exists

An agent with filesystem access is fast, confident, and wrong often enough to matter — and a
research repo is the most expensive place for that combination, because a plausible edit to an
analysis script produces plausible numbers. The skill being assessed is not prompting. It is
**bounding the task and reading the diff**, which are the two things that make the speed safe.

## External material

[Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code). It covers
operation — what the tool can do, how to run it. It does not rule on what a research repo should
let an agent touch, which is a question the standard answers and the documentation cannot.

## Governing part

Whatever governs the files it touches. **Parts 1–2** for `src/`, **Part 3** for `notebooks/`,
and **Part 4** rules on the boundary between them. An agent does not get an exemption from the
Part that governs the directory it is editing.

## The mechanic

1. **Write the task in one sentence before you start.** If it takes two sentences, it is two
   tasks and you should do the first one.
2. Work on a branch. Always.
3. **Read every line of the diff before accepting it.** Not skim — read. This is the step people
   skip and it is the entire safeguard.
4. Record what it got wrong. Not what it got right; you will remember that. The failure is the
   data.

The honest outcome of this exercise is sometimes "it was faster to do it myself." Report that if
it happens — it is a finding about the boundary of the tool, and it is worth more than a success.

## Deliverable

Transcript excerpt plus the diff you accepted, in that week's WA entry.

## Competency check

- [ ] Task stated in one sentence, timestamped before the session
- [ ] Work done on a branch, not the default branch
- [ ] The full diff is shown and was reviewed line by line
- [ ] At least one thing the agent got wrong is recorded
- [ ] Whatever check the repo already has (tests, an agreement assertion) still passes after the merge

## Turning it in

**This replaces your arithmetic entry for the week you do it.** Submit it to that week's
**WA** assignment in Canvas — the same one you would have submitted anyway. It is not an
extra piece of work on top of the log.

- **In the text box:** the one-sentence task, what it got wrong, and whether it actually saved time.
- **You hand in:** A **transcript excerpt** plus the **diff you accepted**, with your one-sentence task statement timestamped before the session began

You do not submit anything to the milestone yet. When all four skills in **M2** are done, submit the **M2 — Reproducible Code** assignment, which is just
an index saying which week each one went in.
