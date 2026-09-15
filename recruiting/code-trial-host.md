# Preparing the handoff folder

*For the lab member whose code is being used. This should take about 45 minutes, and then
you are done.*

Your job is to hand over a folder. You are not running an exercise, not tracking anyone's
time, not answering questions while they work, and not writing anything up afterwards. Make
the folder, send it, forget about it.

---

## 1. Pick code you already know works

**First choice: your own PyPSA work.** Something of yours that is done, that you already know
produces a particular result. That is the whole qualification — you know what it does and you
know what comes out.

Do not re-verify it, do not time yourself, do not tidy it up. Messy is fine and honestly more
useful: the point is to see how someone handles a real project rather than a prepared one.

**Not** the pipeline you are working in now, and not anything feeding a paper under review.

### If you would rather not use your own

Borrow one of Jones's public repos instead. Download it, run it once so you know the answer,
send it. These are already public and already cleaned, so **steps 3 and 4 below are done for
you — skip straight to step 5.**

- [`lithium-optsc-energies-2024`](https://github.com/sear-labs/lithium-optsc-energies-2024) —
  the MILP behind Jones (2024), *Energies*. Reproduces the published objective, and it is
  verifiable **without a commercial solver**, so the candidate does not need a Gurobi licence.
- [`der-decomp-iise-2020`](https://github.com/sear-labs/der-decomp-iise-2020) — distributed
  energy resource capacity expansion. Ships synthetic inputs rather than the licensed Pecan
  Street data.

They are also the **shape** to aim for if you use your own: a closed-out project, a known
output, and data that can be handed to a stranger without anyone having to think about it.

## 2. Write down what it outputs

One or two lines, in a text file or the email. Whatever the code actually produces:

- an objective value
- a decision vector, or the part of one that matters
- a metric vector, a summary table, a figure

Enough that someone can tell whether they got the same thing. If the output is long, point at
the file rather than pasting it.

Send this to Jones as well — it is his answer key.

## 3. Make the folder by copying, not cloning

**This is the one step that matters.** Cleaning up the current files does nothing about the
history: `git log -p` hands over every version of every file ever committed, including things
deleted years ago.

1. New empty folder.
2. **Copy** in the files you want to share. Not `.git`.
3. Zip it.

Do not clone. Do not "delete the sensitive files and push."

## 4. Sixty-second sweep

In the new folder:

```bash
grep -rIn -iE "password|secret|token|api[_-]?key|wlsaccessid|licenseid" .
```

Then look at the data files and ask one question: **is any of this under an agreement?** ERCOT
data held under a use agreement, anything from an industry partner, unpublished results.

If yes, either drop that file or swap in a small synthetic input with the same shape — and say
so in a one-line note. A candidate cannot tell and does not need to.

If you are reasoning toward "it is probably fine," ask Jones instead.

## 5. Send it

The folder, the expected output, and `code-trial-candidate.md`.

Something like this — adjust it to sound like you:

> Hi [name],
>
> I am a PhD student in Erick Jones's lab at UTA, working on power system modelling. Jones
> mentioned you are considering joining us, so I thought it would be more useful to show you
> what the work actually looks like than to describe it.
>
> Attached is code from a project of mine that is finished, along with a short brief. It should
> take about four hours and the brief means that cap seriously — please stop at four even if
> things are unfinished.
>
> One thing worth saying up front: **I will not be able to answer questions while you work.**
> That is deliberate rather than unfriendly. Where something is unclear, make a call and write
> down what you assumed — the brief asks for exactly that, and your assumptions are part of
> what gets read.
>
> No rush, and it is completely fine to say this is not a good time.
>
> [your name]

If they email you a question anyway, *"have a go and write down what you assumed"* is a
complete answer.

---

**That is the end of your involvement.** Anything that arrives back goes to Jones.
