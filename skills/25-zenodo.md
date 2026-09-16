---
title: Zenodo deposit
channel: arithmetic
tier: year 3+
milestone: M6
time: 2 hours
prerequisites: 06-git-github, 07-code-folder-structure
submit_as: Zenodo record URL
---

## Why this exists

A paper that says "code available on request" is a paper whose code will not be available in
four years, because the student has graduated and the laptop is gone. A deposit makes it
citable and permanent. The part students get wrong is not the deposit — Zenodo's GitHub
integration is close to one click — it is which of the two DOIs goes where, and getting that
backwards means your paper cites a moving target or your citation file pins a snapshot nobody
should be citing.

## External material

[Zenodo's GitHub integration
guide](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content)
for the mechanics of linking a repo and triggering a deposit from a release. [The Turing
Way](https://book.the-turingway.org/reproducible-research/rdm/rdm-persistent.html) on persistent
identifiers for the concepts.

## Governing part

The standard rules on the **version DOI versus concept DOI** distinction, and on what
`CITATION.cff` carries. **This distinction is the entire skill** and is deliberately not
restated here — go and read it before you deposit, not after.

## The mechanic

1. Link the repo to Zenodo.
2. **Tag a release.** The deposit captures the tag, so tag something you would want a stranger to
   run.
3. Collect both DOIs.
4. Put each in the place the standard specifies.
5. Verify `CITATION.cff` parses — GitHub shows a "Cite this repository" button when it does, and
   silently shows nothing when it does not, which is how a broken file goes unnoticed for a year.

## Deliverable

Zenodo record URL.

## Competency check

- [ ] Record URL resolves and the archive contains the tagged release
- [ ] Both DOIs present and placed per the standard
- [ ] `CITATION.cff` parses — the GitHub "Cite this repository" button appears
- [ ] The paper's data-availability statement cites the correct one of the two

## Log entry

Arithmetic. Which DOI you would have used in the paper before reading the standard.
