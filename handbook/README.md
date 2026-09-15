# SEAR Lab Research Handbook

Start here.

This is the public handbook for research skills in the SEAR Lab at UT Arlington. If you are a
new PhD student, everything you are expected to be able to demonstrate is on this page, with a
lesson behind each one.

---

## How this works

You keep a weekly research log in three channels — **reading**, **writing**, **arithmetic**.
That is graded every week and it is not going anywhere.

A **skill** below is done *as* one week's log entry, not in addition to it. Pick one, do it on
your own dissertation work, submit it in the channel it belongs to.

A **milestone** is four related skills. When all four are in, you submit an index listing which
week each went in. It is graded complete / redo. **Once you have passed a skill, you never
repeat it** — not this semester, not in year four.

Target two milestones a semester. The full set takes three to four semesters, which puts you
finished around the time you are proposing.

### Two rules

1. **Everything is done on your own work.** Your actual thesis repo, your actual draft, your
   actual data. Not a sample.
2. **Where the [lab code standard](https://github.com/sear-labs/code-standard) governs
   something, the lesson cites the Part and stops.** Go read the Part. This is deliberate: a
   summary reads as complete and stops you looking, so you will not find one here.

---

## M1 — The Workbench · *Year 1*

Getting computation done in the tools you already have open, and the one habit that makes AI
assistance safe: checking the output against something you knew independently.

| Skill | Channel | Turn in as |
|---|---|---|
| [Basic Excel](../skills/01-basic-excel.md) | arithmetic | `.xlsx` in a WA entry |
| [AI prompting](../skills/02-ai-prompting.md) | arithmetic | text entry in a WA entry |
| [Excel with AI assist](../skills/03-excel-ai-assist.md) | arithmetic | `.xlsx` + explanation |
| [Colab with AI assist](../skills/04-colab-ai-assist.md) | arithmetic | Colab share link |

## M2 — Reproducible Code · *Year 1*

The milestone that prevents *"I cannot reproduce my own Chapter 3."* The test at the end is not
a file listing — it is that another student ran your code on their machine and got your number.

**Do [Git and GitHub](../skills/05-git-github.md) first.** Git history is permanent, and a
credential committed once is compromised no matter what you do next. It is the only thing in
these twenty-four skills that cannot be undone afterwards.

| Skill | Channel | Turn in as |
|---|---|---|
| [Git and GitHub](../skills/05-git-github.md) | arithmetic | repo URL + `git check-ignore -v` output |
| [Code folder structure](../skills/06-code-folder-structure.md) | arithmetic | repo URL + what-moved paragraph |
| [Reproducible environments](../skills/07-reproducible-environments.md) | arithmetic | repo URL + partner's signed run log |
| [CLI agents and Claude Code](../skills/08-cli-agents.md) | arithmetic | transcript excerpt + accepted diff |

## M3 — Reading and Citing · *Year 2*

Reading the literature for what it actually shows, finding where it stops, citing it for claims
it genuinely makes, and crediting people honestly.

| Skill | Channel | Turn in as |
|---|---|---|
| [Reading and critiquing papers](../skills/09-critiquing-papers.md) | reading | WR entry, 300–500 words |
| [Literature review and gap-finding](../skills/10-lit-review-gap.md) | reading | PDF: map + gap paragraph |
| [Citation verification](../skills/11-citation-verification.md) | reading | table + updated draft |
| [Research ethics and authorship](../skills/12-ethics-authorship.md) | writing | CRediT statement + evidence circulated |

## M4 — The Manuscript · *Year 2*

Everything between having results and having a document somebody else can read. Aligns with
Report Draft 1 and 2 — take it in the same semester and the work is shared, not doubled.

| Skill | Channel | Turn in as |
|---|---|---|
| [IMRAD structure](../skills/13-imrad.md) | writing | Overleaf link |
| [LaTeX and Overleaf](../skills/14-latex-overleaf.md) | writing | Overleaf link + compiled PDF |
| [Figure and table design](../skills/15-figures-tables.md) | writing | PDF: before, after, caption |
| [Accessibility](../skills/16-accessibility.md) | writing | repo URL |

## M5 — The Review Cycle · *Year 3+*

Everything between "the draft is finished" and "it is out in the world." You review a labmate's
Report Draft 1 and they review yours; each of you then answers the review you received.

| Skill | Channel | Turn in as |
|---|---|---|
| [Reviewing papers](../skills/17-reviewing-papers.md) | reading | structured referee report |
| [Response to reviewers](../skills/18-response-to-reviewers.md) | writing | PDF response letter |
| [Venue selection](../skills/19-venue-selection.md) | writing | one-page memo + cover letter |
| [Conference talk and poster](../skills/20-talk-poster.md) | writing | slides + three questions |

## M6 — Stewardship · *Year 3+*

The loosest grouping of the six. What joins them is that each produces something that outlasts
you in this lab: a citable deposit, a dataset somebody can still find terms for in four years,
an idea written well enough to be funded, and a person who learned to do research because you
scoped their first task properly.

| Skill | Channel | Turn in as |
|---|---|---|
| [Zenodo deposit](../skills/21-zenodo.md) | arithmetic | record URL |
| [Research data management](../skills/22-research-data-management.md) | arithmetic | one-page data statement |
| [Proposal writing fragments](../skills/23-proposal-fragments.md) | writing | PDF to the call's page limits |
| [Mentoring an undergraduate](../skills/24-mentoring.md) | writing | task brief + retrospective |

---

## If you are brand new

1. Read the [code standard's](https://github.com/sear-labs/code-standard) `GETTING-STARTED.md`.
2. Do [Git and GitHub](../skills/05-git-github.md) before you commit anything, anywhere. The
   ordering in that lesson is the point.
3. Then pick anything from M1 or M2.

## Maintenance

Senior students maintain this. If a lesson is wrong, out of date, or assumes something you did
not have, open a PR — that is the intended path, and the [contributing
notes](../README.md#contributing) say what an exemplar needs before it can go in.
