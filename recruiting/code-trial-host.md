# Running the code trial — instructions for the host

*For the current lab member whose code is being used, and who is running the trial.*

You are doing three separate jobs here, and they need to stay separate in your head: you
**prepare** the material, you **invite** the candidate, and you **debrief** them afterwards.
Budget about three hours total, most of it in Part A.

If these jobs end up split between two people, Part A belongs to whoever wrote the code and
Parts B–D to whoever is doing the outreach.

---

## Part A — Choose and prepare the code

This is the part with real consequences, so it comes first and gets the most space.

### A1. Pick retired code, not live code

Use something from a **finished or published project.** Not the pipeline you are actively
working in, and not anything feeding a paper under review.

Two reasons. A candidate producing useful output on live code is doing unpaid work for the
lab, which is not something we want to be true. And retired code can be shared without anyone
having to think hard about what happens if it leaks.

Good candidates: the analysis behind a published paper, a model you have since replaced, a
one-off study that is closed out.

### A2. The data must be publicly redistributable

Go through every data file you are about to include and answer, in writing, where it came
from and what it arrived under.

**Exclude, without exception:**

- ERCOT data held under a use agreement
- Anything from an industry partner under NDA
- Unpublished results, including intermediate outputs that imply them
- Anything you cannot name a licence for

If that empties the folder, use **synthetic data** instead — generate a small input file with
the same shape and dtypes, commit it, and say plainly in the README that it is synthetic.
A candidate cannot tell the difference and does not need to.

If you find yourself reasoning toward "it is probably fine" — it is not. Ask Jones.

### A3. Ship a copy, not a clone

**This is the step that goes wrong.** Cleaning up the current files does nothing about the
history. `git log -p` hands over every version of every file ever committed, including the
credential somebody removed in 2024 and the data file that was deleted the next day.

So:

1. Make a **new empty folder.**
2. **Copy** in only the files you want shared. Do not copy `.git`.
3. `git init` fresh, if you want it to be a repo at all. One commit.

Do not clone, do not branch, do not "delete the sensitive files and push." Copy.

### A4. Sweep the copy

In the new folder, before it goes anywhere:

```bash
grep -rIn -iE "password|secret|token|api[_-]?key|wlsaccessid|licenseid" .
grep -rIn -E "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(edu|com|org)" .
grep -rIn -E "C:\\\\Users|/home/[a-z]+|/Users/" .
```

The third one catches absolute paths, which leak machine names and usernames and are also the
single most common reason code will not run for somebody else.

Then read the file list yourself. Tooling catches patterns; you catch the thing that is only
obviously wrong to a person.

### A5. Know the answer before they do

Run the whole thing yourself, from the clean folder, ideally on a different machine or a fresh
environment.

Write down three things:

- **The number or figure** you want them to reproduce, and where it lives.
- **How long it took you**, honestly, including the environment fighting.
- **Everything you had to already know** to make it work. This list is the answer key. Every
  item on it is something the candidate will have to discover, and it is what makes their
  questions in Part C interpretable rather than just noise.

If it takes *you* more than ninety minutes, the task is too big. Cut it down.

---

## Part B — The invitation

Send this yourself, from your own address. It should read as an invitation from a colleague,
not a summons from an institution.

**Say:**

- Who you are, and that you are the person whose project this would pick up
- That this is a chance to see the kind of work the lab does before committing to anything
- Four hours, hard cap, and that you mean the cap
- That AI use is expected and should be described, not hidden
- Roughly when a 30-minute conversation would happen afterwards
- That they can say no, or say "not right now", with no consequence

**Do not say:**

- Anything implying this decides admission, unless Jones has told you it does
- "Take as long as you need" — that is how a four-hour task becomes a twenty-hour one
- Anything about other candidates

**Give them a week**, and ask which day works rather than assigning one. Someone with a job or
caring responsibilities needs to be able to pick their evening.

If they decline or go quiet, let it go and tell Jones. A non-response is information about
their availability, not about their ability.

---

## Part C — The trial and the debrief

### While they are working

**Do not help.** But **do answer clarifying questions**, and this is the important part:

> **Log every question they have to ask you.**

Each one is a defect in your README, and the list is worth more to the lab than the trial
result. That is the same mechanic as the reproducible-environments skill in the curriculum —
a question the reader has to ask is a documentation failure, not a reader failure.

Do not treat a question as a mark against them. A candidate who asks three sharp questions is
usually doing better than one who asks none and quietly guesses.

### The debrief — 30 minutes, and this is the real test

The artifact tells you less than the conversation does. A decent AI can produce a plausible
README. It cannot sit on a call and explain why a choice was made.

Ask these, in roughly this order, and let them talk:

1. **"Walk me through what this code actually does."** — Comprehension. Listen for whether they
   understood the shape of it or only the file names.
2. **"What did you try that didn't work?"** — The best question on the list. Anyone who did the
   work has an answer. Anyone who did not, does not.
3. **"Where did you use AI, and where did you decide not to trust it?"** — The second half is
   what you are listening for. "I used it for everything and checked nothing" and "I didn't use
   it at all" are both weak answers.
4. **"What would you change about how this repo is organised?"** — Judgment. There is no right
   answer; there is an answer that shows they formed a view.
5. **"What did you assume?"** — The strongest candidates volunteer an assumption they are
   uneasy about.

### Reading the result

| Strong | Weak |
|---|---|
| Says plainly what they could not get working | Claims everything worked |
| Describes a wrong turn and what it cost | Presents a clean linear story |
| Names where they checked the AI and where they did not | Cannot separate their work from the model's |
| Asked good questions partway through | Asked nothing, guessed, said nothing about guessing |
| Stopped at four hours and said what was left | Spent fifteen hours and did not mention it |

**Not a signal:** whether they knew anything about energy systems, batteries, or optimization.
That is what they are coming here to learn. If you find yourself scoring domain knowledge,
stop — the task was built so that it should not be possible.

---

## Part D — What to send Jones

Half a page, within two days while it is fresh:

- Did they get it running? How far?
- The list of questions they had to ask you (Part C) — these are getting fixed either way
- Your honest read on the five debrief questions
- Whether you would want them picking up your project
- Anything that made you uncomfortable

Send the same half-page to the candidate too, minus the last two items. They spent four hours;
they are owed a response that is more than "thanks, we will be in touch."

---

## The things not to do

- **Do not use their output.** Not the README, not the fixes. If it is genuinely good and you
  want it, ask them, credit them, and tell them you are using it.
- **Do not let this run long.** If they are at hour ten, that is your failure to cap it, and
  you should say so to them directly.
- **Do not make it a gate you were not authorised to make.** You are gathering information for
  Jones. He decides.
