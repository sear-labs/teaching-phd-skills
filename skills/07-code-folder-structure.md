---
title: Code folder structure
channel: arithmetic
tier: year 1
milestone: M2
time: 4 hours
prerequisites: 06-git-github
submit_as: repo URL plus one paragraph on what moved where
---

## Why this exists

"I cannot reproduce my own Chapter 3" is the concrete failure this prevents, and it has a
specific mechanism: processed data overwrote raw data, or a script's output became its own
input, and now there is no path back to the numbers in the draft. It surfaces at the worst
possible moment — during revisions, under a deadline, when the person who could explain the
directory is you eight months ago.

## External material

Wilson et al., ["Good Enough Practices in Scientific
Computing"](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510),
PLOS Computational Biology 2017 — section 3, project organisation. This is the paper behind the
Carpentries lesson. It is genuinely good and the standard's Part 1 is close to a strict superset
of it.

## Governing part

**Part 1**, and **Archetype A**.

## The mechanic

Restructure your actual thesis repo to the archetype. Not a copy, not a sample — the one your
chapter depends on.

Then the second half, which is the part that teaches: read Wilson et al. §3, and **find two
places where the standard is stricter.** State each in one sentence, with one sentence on why
the extra strictness exists. You are not being asked to agree with it; you are being asked to
notice it, because a rule you have located yourself is one you will follow when nobody is
checking.

## Deliverable

Repo URL, plus one paragraph on what moved where, plus the two stricter-points.

## Competency check

- [ ] Repo layout matches the archetype
- [ ] Nothing under the raw tier is written by any script (verify, do not assert)
- [ ] README is usable by someone who has never seen the project
- [ ] Two places the standard is stricter than Wilson et al., identified and explained

## Log entry

Arithmetic. What moved, and what you found in the old layout that you had forgotten was there.
