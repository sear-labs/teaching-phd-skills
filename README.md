# PhD Research Skills — SEAR Lab

Twenty-four research skills, grouped into six competency milestones, delivered through the
weekly research log in IE 6999. This repository is the **source of truth**; Canvas is a
delivery copy, regenerated from here.

**Students start at [`handbook/README.md`](handbook/README.md).**

---

## The shape of it

Students keep a weekly research log split into three channels — **reading, writing,
arithmetic** — graded every week. That already existed and works. This curriculum slots into
it rather than sitting beside it.

A **skill** is performed as one week's ordinary log entry. There is no extra weekly work: the
skill replaces that week's entry, it does not stack on top of it.

A **milestone** is a group of related skills. When they are all in, the student submits an index
saying which week each went in. Graded complete / redo. One demonstration and the skill is
held permanently — it does not repeat in a later semester.

| | | | |
|---|---|---|---|
| **M1** | The Workbench | 5 | Spreadsheets · Notebooks+AI · Command line · LaTeX · Sanity checks |
| **M2** | Reproducible Code | 4 | Git · Folder structure · Environments · CLI agents |
| **M3** | Reading and Reasoning | 5 | Critique · Gap-finding · Logic · Claim/reason/evidence · Claim precision |
| **M4** | The Manuscript | 5 | IMRAD · Citations · Authorship · Figures · Accessibility |
| **M5** | The Review Cycle | 5 | Refereeing · Rebuttal · Venue · Talk · Defending |
| **M6** | Stewardship | 4 | Zenodo · Data management · Proposals · Mentoring |

Twenty-eight skills. Target two milestones per semester; the full set takes three to four
semesters.

Nothing is gated — no prerequisites, no completion requirements, no sequential progress. The
tiers are advice about a sensible order, not locks, because the course runs every semester with
a mixed cohort and any fixed schedule is wrong for most of the room.

**Two ungraded companion pages**, narrowing from general to lab-specific. Both ship as Canvas
pages with no assignment attached.

- [`handbook/where-we-work.md`](handbook/where-we-work.md) — the lab. Infrastructure's three
  layers, the three research areas laid against them, and which course goes deep on each.
  **Read in week one**; surface level on purpose.
- [`handbook/what-the-model-assumes.md`](handbook/what-the-model-assumes.md) — the questions
  behind the methods. Philosophy of science, the normative content of modelling choices, policy
  literacy, field history, economics. **Read later**, once the domain is familiar.

## Layout

```
skills/        24 lesson packages, one per skill
milestones/    6 milestone definitions and their gates
handbook/      the public-facing entry point
exemplars/     passed student artifacts, with permission
records/       Canvas exports (gitignored — may contain student names)
scripts/       the Canvas generators
docs/          design brief and background notes
```

## Regenerating Canvas

```bash
python scripts/push_to_canvas.py --course 277913 --dry-run
python scripts/push_to_canvas.py --course 277913
```

Idempotent — matches by title and updates in place, so re-running never duplicates.
Everything is created **unpublished**; publishing is a decision made in Canvas.

Requires `pandoc` on PATH and `CANVAS_TOKEN` in the environment. **The token is never
written to this repository.** This repository is public.

Edit the Markdown here and re-run. Do not edit a generated page in Canvas — the next run
overwrites it.

## Two rules this repository follows

**It points at the code standard and never restates it.** A skill file says "governed by
Part 1" and links to <https://github.com/sear-labs/code-standard>. It does not summarise
what Part 1 says. Part 0 of the standard forbids this, and the stated reason is measured
rather than theoretical: a partial restatement reads as complete and stops the search.

**Every deliverable is performed on the student's own dissertation work.** Not a sample repo,
not a practice paper. PhD students correctly read toy exercises as busywork stacked on top of
real work, and a restructured sample repo teaches nothing about the repo the thesis depends on.

## Contributing

Senior students maintain this. The intended loop: you pass a milestone, your artifact goes
into `exemplars/` with your permission, and the student after you starts from where you
finished instead of from zero.

Two things to check before opening a PR that adds an exemplar:

- The student whose work it is has given written permission.
- It contains no unpublished results and no data under a restriction. See
  [`skills/22-research-data-management.md`](skills/22-research-data-management.md) — that
  skill's whole subject is answering this question before rather than after.

## Accessibility

This is a public repository belonging to a Title II entity, so it is in scope for
[`skills/16-accessibility.md`](skills/16-accessibility.md) — WCAG 2.1 AA from 26 April 2027.
It is a legitimate target for a student taking that skill, and is the intended first one.
