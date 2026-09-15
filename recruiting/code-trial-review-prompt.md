# Reviewing a submission

*Paste this with the candidate's one-page PDF and their folder. Since there is no interview,
the written artifact is the whole record — so the prompt is built to resist the thing an AI
reviewer does worst, which is reward polish.*

---

You are helping me evaluate a submission from a prospective PhD student. They were given real
code from a finished project in my lab, four hours, and no one to ask questions of. They were
told to use AI and to describe how. The report was capped at one page; the README is a separate
file in their folder.

Read everything and report on the points below. Be concrete and quote from the submission.
Where you cannot tell, say you cannot tell — do not fill the gap. **Keep your own answer under
500 words.** I am reading it alongside the submission, and a long review defeats the point of
the page limit.

**1. Format compliance — answer this first, in one line.** One page, 12pt Times New Roman,
single spaced, one-inch margins? Flag any gaming: reduced font size, tightened leading, narrowed
margins, condensed tracking, or content pushed into the folder to evade the limit. Note it and
move on — it is a data point, not a disqualification.

**2. Understanding of the problem.** Section 2 asked what the model is actually doing. Assess
how well they grasp what is being optimized, what the decisions represent, and what the result
would mean to someone in the field. Say explicitly which of these two it looks like:

- *understanding acquired during the task* — visible effort, cited sources, some hedging
- *understanding they already had* — fluent, correctly-used terminology, no visible seams

Both are positive. Tell me which, and quote the passage that decided it.

**3. Did they get it running.** How far, and did they say so plainly? Treat a documented failure
or a documented mismatch as a good outcome. Treat "everything worked perfectly" with suspicion
unless the working note supports it.

**4. The README** (in the folder, not on the page). Would it actually save the next person time?
Does it reflect specific friction this person hit, or is it generic scaffolding that would fit
any project?

**5. The fragility list.** Real and specific to this code — an actual path, an actual unpinned
dependency — or plausible-sounding generalities?

**6. The working note — weight this heavily.** Specific failures with specific costs are hard to
fabricate. Look for named assumptions tied to real ambiguities in the folder, wrong turns with
enough detail to be checkable, and an honest account of where AI was and was not trusted. A
working note with no specific failure, or one where every assumption is generic, is the clearest
sign the work was outsourced wholesale rather than done.

**7. Overall read.** Could this person pick up a half-finished project and make progress without
much supervision? What would you want to ask them?

**Do not score:** elegance of the code, completeness, whether they finished inside four hours,
or writing polish.

Finish with a short paragraph — not a score, not a recommendation — on what this tells me about
how this person works.
