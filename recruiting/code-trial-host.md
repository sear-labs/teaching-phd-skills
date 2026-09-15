# Preparing the handoff folder

*For the lab member whose code is being used. This should take about 45 minutes, and then
you are done.*

Your job is to hand over a folder. You are not running an exercise, not tracking anyone's
time, not answering questions while they work, and not writing anything up afterwards. Make
the folder, send it, forget about it.

---

## 1. Pick code you already know works

Something from a **finished project** — a published paper, a model you have since replaced, a
study that is closed out. Not the pipeline you are working in now.

You already know what it produces. That is the whole qualification. Do not re-verify it, do
not time yourself, do not clean it up. Messy is fine and honestly more useful.

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

The folder, the expected output, and `code-trial-candidate.md`. A couple of sentences from you
about what the project was is welcome but not required.

Tell them plainly that **you will not be available for questions** — that is by design, not
rudeness, and their brief already says so. If they email you anyway, a one-line "have a go and
write down what you assumed" is a complete answer.

---

**That is the end of your involvement.** Anything that arrives back goes to Jones.
