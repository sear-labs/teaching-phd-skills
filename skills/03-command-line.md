---
title: The command line and a remote machine
channel: arithmetic
tier: year 1
milestone: M1
time: 5 hours
prerequisites: none
submit_as: terminal transcript plus retrieved output, in a WA entry
---

## Why this exists

This lab runs Linux servers alongside Windows workstations, and the jobs that matter — a ReEDS
run, a large MILP, a parameter sweep — do not belong on your laptop. They outlive your battery,
your commute, and the moment your machine decides to install an update.

It is also a hard prerequisite. The code standard **presumes** shell fluency rather than
teaching it, and skills 05 and 08 both assume you already have it. A student who cannot move a
file to a server is blocked on their first week in a way nobody diagnoses, because it looks like
slowness rather than a missing skill.

## External material

[MIT Missing Semester](https://missing.csail.mit.edu/), lectures 1 and 2 — the shell, and shell
tooling. This is the best free treatment of the subject and it is genuinely short. It teaches
the shell in general; it knows nothing about UTA's cluster, which is the second half below.

Your cluster's own documentation for the scheduler. Ask which one the lab uses before you start
— the commands differ and guessing wastes an afternoon.

## Governing part

None. `NEW-MACHINE.md` in the standard covers setting a machine up, which overlaps.

## The mechanic

**Locally, first.** Navigate without a file browser. Pipe one command into another. Redirect
output to a file. Find a string in a directory tree you did not write. These four cover most of
what you will ever need.

**Then a machine that is not yours.** A lab server or UTA HPC:

1. `ssh` in.
2. Move a file **both directions** — up and back. Getting results off the machine is the half
   people forget, and it is the half that matters at 2am before a deadline.
3. **Run something that survives you disconnecting.** A scheduler submission, or `tmux` /
   `screen`. Then close your laptop, go away, come back, and collect the output.
4. Read the log it produced, including the part where it complains.

That third step is the point of the lesson. Everything else is convenience; that one is the
difference between a job you can run and a job you can only babysit.

## Deliverable

A terminal transcript — paste it, screenshots are not searchable — plus the output file you
retrieved from the remote machine.

## Competency check

- [ ] Local: navigation, a pipe, a redirect, and a recursive search, all shown
- [ ] `ssh` to a lab server or HPC node, shown
- [ ] A file moved to the remote machine **and** a result moved back
- [ ] A job that survived a disconnection, with evidence it did — the submission, then the output
- [ ] The log read, with one line quoted that you had to look up

## Turning it in

**This replaces your arithmetic entry for the week you do it.** Submit it to that week's
**WA** assignment in Canvas — the same one you would have submitted anyway. It is not an
extra piece of work on top of the log.

- **In the text box:** what you ran remotely, and what broke the first time.
- **Include or attach:** terminal transcript plus retrieved output, in a WA entry

You do not submit anything to the milestone yet. When all five skills in **M1** are done, submit the **M1 — The Workbench** assignment, which is just
an index saying which week each one went in.
