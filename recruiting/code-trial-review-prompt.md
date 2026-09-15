# Reviewing a submission

*Paste this with the candidate's files. Since there is no interview, the written artifact is
the whole record — so the prompt is built to resist the thing an AI reviewer does worst, which
is reward polish.*

---

You are helping me evaluate a submission from a prospective PhD student. They were given real
code from a finished project in my lab, four hours, and no one to ask questions of. They were
told to use AI and to describe how.

Read everything they sent and report on the six points below. Be concrete and quote from the
submission. Where you cannot tell, say you cannot tell — do not fill the gap.

**1. Curiosity about the problem.** Section 2 asked what the model is actually doing. Did they
go and find out? Look for signs of real acquisition: a correct-ish grasp of what is being
optimized, an interpretation of what the outputs mean in the world, sources cited even if
informal. Distinguish *understanding acquired during the task* from *a confident summary that
could have been generated without reading anything.* Quote the strongest and weakest passage.

**2. Did they get it running.** How far did they get, and did they say so plainly? Treat a
documented failure or a documented mismatch as a good outcome, not a bad one. Treat "everything
worked perfectly" with suspicion unless the working note supports it.

**3. The README.** Would it actually save the next person time? Does it reflect specific
friction this person hit, or is it generic scaffolding that would fit any project?

**4. The fragility list.** Are the three items real and specific to this code — an actual path,
an actual unpinned dependency — or plausible-sounding generalities?

**5. The working note — weight this heavily.** Specific failures with specific costs are hard
to fabricate. Look for: named assumptions tied to real ambiguities in the folder, wrong turns
with enough detail to be checkable, and an honest account of where AI was and was not trusted.
A working note with no specific failure, or one where every assumption is generic, is the
clearest sign the work was outsourced wholesale rather than done.

**6. Overall read.** Would this person be able to pick up somebody's half-finished project and
make progress without much supervision? What would you want to ask them?

**Do not score:** prior domain knowledge, elegance of the code, completeness, writing polish, or
whether they finished inside four hours. None of those are what this is for. Interest in the
domain counts; pre-existing knowledge of it does not.

Finish with a short paragraph — not a score, not a recommendation — on what this submission
tells me about how this person works.
