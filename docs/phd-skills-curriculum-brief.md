# PhD Research Skills Curriculum — Design Brief

*A context document to paste at the start of a session generating Canvas lessons and
assignments. It states the situation, the constraints, and the format. It is not itself
a lesson.*

---

## 1. Who this is for

Erick C. Jones Jr., assistant professor, Industrial, Manufacturing and Systems
Engineering (IMSE), UT Arlington. Directs the SEAR Lab. Research spans energy systems
optimization (ERCOT, ReEDS), battery materials and recycling, critical minerals supply
chain MILP, transportation decarbonization, and surrogate modeling.

Students are PhD students in his lab. They take a research class **every semester**,
which is the delivery vehicle for everything below. The lab runs a three-tier structure
(PhD directed research, MS/OPT team projects, undergraduate REU/UROP), so PhD students
are also supervising people beneath them.

**The problem being solved:** these skills have been left to osmosis. Gaps therefore
surface at the worst possible moment — a student who cannot reproduce their own Chapter 3
results, or a submission that stalls on formatting. The goal is to make each skill an
explicit, demonstrated, graded thing.

---

## 2. The existing vehicle: the weekly research log

**This already exists and works. Do not replace it.** Students keep a weekly research log
split into three channels — **reading, writing, arithmetic** — graded every week. At the
end of a semester (and across semesters) students reflect critically on the accumulated
log and can see their own progress in a well-defined way, which is strongly motivating.

What is missing is *explicit instruction*. Students have been taught critical reflection
and nothing else. The skills below have never been taught directly.

**So the curriculum slots into the log rather than sitting beside it.** Each skill belongs
to one of the three channels, and each gets a short "here's how" module the week before it
first appears in the log:

| Channel        | Skills that live here                                                                 |
| -------------- | ------------------------------------------------------------------------------------- |
| **Reading**    | critiquing papers, structured peer review, literature review and gap-finding, citation verification, reading a CFP |
| **Writing**    | IMRAD, LaTeX/Overleaf, response-to-reviewers, figure and caption design, proposal fragments |
| **Arithmetic** | code standard, Git/GitHub, Colab, reproducible environments, Zenodo, Excel, AI-assisted analysis, CLI/agentic tools |

The end-of-semester reflection is unchanged in form. It now reflects on demonstrated
competencies rather than only on effort.

---

## 3. The skill list

### Core (as originally specified)

1. Basic Excel
2. AI prompting
3. Colab with AI assist
4. Excel with AI assist
5. Code folder structure per the lab code standard
6. Git and GitHub
7. Zenodo
8. LaTeX and Overleaf
9. Reading and critiquing papers
10. Reviewing papers — summary, strengths, weaknesses, recommendation
11. Formatting academic papers (IMRAD)
12. Literature review and finding research gaps
13. Advanced AI with tools — CLI agents, Claude Code

### Added

14. **Reproducible environments** — can a labmate run this from a clean machine (pinned
    ranges, a resolved lock, recorded interpreter version, seeds, data paths)
15. **Response-to-reviewers letters and rebuttals**
16. **Figure and table design for publication**
17. **Reference manager discipline + AI-era citation verification** (fabricated references
    are now a real failure mode)
18. **Research data management** — provenance, licensing, what may and may not be deposited
19. **Proposal writing fragments** — project summary, broader impacts, budget justification
20. **Journal and venue selection + submission mechanics** — cover letter, ORCID, preprint
    policy, and journal AI-disclosure policies
21. **Conference talk and poster delivery**
22. **Mentoring an undergraduate** — fits the three-tier lab structure directly
23. **Research ethics and authorship norms**
24. **Accessibility of published notebooks and figures** — see §6, this one has a deadline

---

## 4. The lab code standard, and how it relates to everything else

The standard lives at **https://github.com/sear-labs/code-standard** (`CLAUDE.md`, ~2,700
lines). `GETTING-STARTED.md` is the first-week on-ramp; `NEW-MACHINE.md` sets up a machine.

### 4.1 The rule that constrains this entire curriculum

Part 0 of the standard states:

> A subordinate document may **point at** this one. It may never **restate** it — not a
> summary, not a quick-reference table, not "the short version for convenience."

The stated reason is that a partial restatement *reads as complete and stops the search*.
This was measured, not theorized: copies ran 46 and 28 lines behind, and four scaffolding
templates carried the document's predecessor entirely.

**Therefore: no Canvas assignment, rubric, slide, or handout may paraphrase the standard.**
An assignment teaches the *mechanic* and then cites the governing Part by number. This is a
hard constraint on every artifact generated from this brief. It also makes the assignments
easier to write, because the rules do not have to be re-derived — only pointed at.

### 4.2 How the standard compares to the public references

Assessed against the standard's actual text.

**"Good Enough Practices in Scientific Computing"** (Wilson et al., PLOS Comp Bio 2017 —
the paper behind Carpentries' project-organization lesson). The standard's Part 1 is close
to a **strict superset**. Both have one-command reproduction, immutable inputs, gitignored
generated files with documented exceptions, a README written for a stranger, meaningful
commits and tags. The standard is tighter everywhere, and Archetype A's three-tier
`data/{raw,interim,processed}` with one-way flow is more specific than anything published.
*Usable as assigned background; a good exercise is asking students to locate where the
standard is stricter and say why.*

**The Turing Way.** Genuine overlap on reproducible environments, version control,
licensing, `CITATION.cff`, Zenodo, and PR governance. The standard is sharper in two
places: the **version DOI vs. concept DOI** distinction (paper cites the version DOI;
`CITATION.cff` carries the concept DOI) and the dependency rule (a **range** so a reader
can install, **plus** a resolved lock recording what actually ran, **plus** the interpreter
version). No Turing Way equivalent exists for Parts 3, 4, 2b, or Archetype P.

**MIT Missing Semester.** Zero content overlap. It teaches the shell and Git fluency the
standard *presumes*. Prerequisite, not duplication — it is what makes
`git check-ignore -v` and "git history is permanent" land as understanding rather than
ritual.

**The Carpentries.** Same relationship. They teach how to do the thing; the standard rules
on how it must be done.

### 4.3 What is original to the standard and has no external substitute

Assignments covering these must be written from scratch. This is where the effort goes.

- **Part 3 — Archetype T**, teaching code. The step-by-step-then-streamlined rule, grounded
  in the *expertise reversal effect*. Includes "the inversion" diagnostic (where does the
  first function longer than ~8 lines sit, as a percentage through the notebook — under 50%
  and it is inverted) and the **leave room** rule for the prose around the code.
- **Part 4 — the boundary.** `src/` is governed by Parts 1–2, `notebooks/` by Part 3,
  neither wins on the other's territory. Plus the **agreement assertion**, the
  **knobs vs. tables** distinction, and the rule that a tolerance must sit between the noise
  and the effect.
- **Archetype P** — reimplementing published models. Reconcile on the objective never the
  solution; grep for variable *bounds* (`.fx`, `.up`, `.lo`) before believing a port is
  complete; read the residual not the status word.
- **Part 2b** — folders that are not repos. The accumulates-vs-persists organizing rule and
  the "would you look for this by *when* or by *what*" test.
- **The naming taxonomy** — including the deliberate inversion (research is
  `subject-method`, teaching is `method-application`, because a researcher searches by
  subject and a student searches by course).
- **Part 2c** — starting and retiring a project, and what trails behind one.

---

## 5. Design principles for the assignments

1. **Every deliverable comes from the student's own dissertation work.** "Restructure your
   actual thesis repo to the standard" beats "restructure this sample repo." PhD students
   correctly read toy exercises as busywork stacked on top of real work.
2. **Pass / redo against a competency checklist, not points.** One demonstration and the
   skill is assumed permanently. This also keeps the grading load survivable.
3. **The assignment is a bridge, never an authority.** Carpentries or Missing Semester
   supplies the mechanic; the student performs it on their own repo; the deliverable is
   checked against a named Part of the standard. See §4.1.
4. **Tier by year.** Year 1 gets setup and hygiene; year 2 gets review, writing, and
   deposit; year 3+ gets proposals, mentoring, and the job market.
5. **Artifacts accumulate into a living lab handbook** that senior students maintain. This
   converts the curriculum into onboarding for every student who follows, which is where
   the real leverage sits.
6. **Keep the AI layer modular.** It will date fastest. Isolate it so it can be replaced
   without touching the rest.

---

## 6. Two items with external deadlines or teeth

**Accessibility (has a date).** The standard's Part 3 notes that a public university is a
Title II entity and the DOJ's 2024 rule makes WCAG 2.1 AA the standard for web content a
covered entity makes available — course material included — from **26 April 2027** for
entities serving 50,000 or more. A public repo with a hosted-notebook badge is web content.
Alt text is a one-sentence cost at authoring time and a project in retrospect. No external
curriculum teaches this for notebooks. Treat it as a real assignment.

**Credentials in git history.** The standard calls this the one mistake that cannot be
undone: `.gitignore` written and *verified* with `git check-ignore -v` **before** the first
commit, and a leaked credential means rotating the credential, not amending the commit. If
one thing in the curriculum has to be taught before anything else, it is the four-step
ordering in `GETTING-STARTED.md`.

---

## 7. What to generate

For each skill, produce a Canvas-ready lesson package:

```
TITLE
CHANNEL            reading | writing | arithmetic
TIER               year 1 | year 2 | year 3+
TIME               realistic hours, stated honestly
PREREQUISITES      other lessons in this curriculum, if any

WHY THIS EXISTS    3–5 sentences. The failure mode it prevents, ideally a concrete
                   one. Not motivational filler.

EXTERNAL MATERIAL  named, linked, with the specific lesson/section — not "see the
                   Carpentries." State what it covers and what it does not.

GOVERNING PART     the Part number of the code standard that rules on this, cited and
                   NOT paraphrased. Omit where no Part governs.

THE MECHANIC       the actual instruction. This is the part that does not exist
                   anywhere else and is the reason the lesson is being written.

DELIVERABLE        performed on the student's own work. State the submission form:
                   repo URL, PDF upload, text entry, or a link to a deposited record.

COMPETENCY CHECK   pass/redo criteria as a short checklist. Each item must be
                   verifiable by looking at the submission — no "demonstrates
                   understanding of."

LOG ENTRY          what the student writes in that week's research log, in the
                   relevant channel.
```

**Additional constraints on generated lessons:**

- Write for a first-year PhD student who has never used a terminal, without condescending
  to a fourth-year who has.
- Where the standard already settles something, cite the Part and stop. Resist the pull to
  helpfully summarize it — that is the exact failure §4.1 describes.
- Prefer one honest mechanic over three alternatives. The standard's own style is to state
  the rule, state the measured failure that produced it, and stop.
- The lab's actual tooling is GAMS, CPLEX, Gurobi, ReEDS, GurobiPy, Python, Excel, and
  Linux servers plus Windows workstations. Examples should use it.

---

## 8. Open decisions (not yet made — ask rather than assume)

- Sequencing across semesters: how many skills per term, and in what order.
- Whether the AI-tooling lessons are a separate track or interleaved.
- Whether the lab handbook is a repo, a Canvas page, or both.
- Whether MS students get a reduced version of the same curriculum.
- How the competency checklist is recorded so it persists across semesters and across the
  multiple sections of the research class.
