---
title: Git and GitHub
channel: arithmetic
tier: year 1
milestone: M2
time: 4 hours
prerequisites: none
submit_as: repo URL plus pasted git check-ignore -v output
---

## Why this exists

**Do this one before anything else in M2.** Git history is permanent. A credential committed
once is compromised even if the next commit removes it, even if you force-push, even if the
repo was private at the time — and the fix is rotating the credential, not amending the commit.
This lab keeps Gurobi WLS credentials and ERCOT data under use agreements in the same
directories as code. It is the only mistake on this list of twenty-four that cannot be undone
afterwards, which is why the ordering below is not a suggestion.

## External material

[MIT Missing Semester](https://missing.csail.mit.edu/), lectures 1 (shell) and 6 (version
control). It teaches the fluency the standard presumes — what a commit actually is, why history
is a graph. It is a prerequisite, not a duplicate: it rules on nothing about how your repo must
be laid out.

## Governing part

`GETTING-STARTED.md` in the standard gives the four-step ordering. **Part 1** governs the repo
itself. Read them directly — the ordering is the entire point and a paraphrase of it here would
be exactly the failure Part 0 describes.

## The mechanic

On your actual dissertation code, in this order and no other:

1. Write `.gitignore`.
2. Verify it with `git check-ignore -v <path>` for **every** data file and credential file —
   one invocation per path. The `-v` flag prints which rule matched. No output means no rule
   matched, which means the file is not ignored.
3. Run `git status` and read every line. Anything listed is about to become public forever.
4. Only now, the first commit.

Then work normally for at least five commits, with messages that say **why**, not what. `git
diff` already says what.

## Deliverable

Repo URL plus the pasted `git check-ignore -v` output.

## Competency check

- [ ] Repo URL resolves
- [ ] `git check-ignore -v` output pasted, showing a matched rule for every data and credential path
- [ ] Searching the full history for your own credential variable names returns nothing
- [ ] At least five commits whose messages state a reason
- [ ] `git status` on a clean checkout is empty

## Log entry

Arithmetic. What you nearly committed and did not.
