# Email: Jones → the lab member preparing the folder

*Copy, paste, fill the brackets.*

---

**Subject:** Handoff folder for a prospective student — about 45 minutes

Hi [name],

I have been talking to a prospective PhD student, and rather than trade paragraphs about
research interests I would rather show them what the work actually looks like. The plan is to
hand them a finished project, ask them to get it running, work out what it does, and write up
one page on it.

Would you put the handoff folder together? I would like it to be **your PyPSA work** —
something of yours that is done and that you already know produces a particular result.

**Your part is about 45 minutes and it ends when you hit send:**

1. **Pick something finished.** Not what you are writing up now. Do not clean it up — messy is
   genuinely more useful here, because the point is to see how someone handles a real project
   rather than a prepared one.
2. **Write me one or two lines on what it outputs** — objective value, dispatch, LMPs, whatever
   the right summary is. That is my answer key, so send it to me as well as keeping it with the
   folder.
3. **Copy the files into a fresh folder — copy, do not clone.** This is the one step that
   matters. Cleaning up the current files does nothing about the history; `git log -p` hands
   over every version of every file ever committed. New empty folder, copy in what you want to
   share, leave `.git` behind, zip it.
4. **Sixty-second check.** Grep for credentials, and glance at the data files to confirm nothing
   is under an agreement. If anything is, drop it or swap in a small synthetic input.
5. **Send it to them** with the attached brief, and tell them plainly that you will not be
   answering questions while they work. That is deliberate — their assumptions are part of what
   I want to read.

**That is all of it.** No interview, no grading, no tracking how long they take, nothing to
write up afterwards. Whatever comes back comes to me.

Full instructions are in `recruiting/code-trial-host.md`, including a draft of the email to
send them so you do not have to compose it. If you would rather not use your own work, two of
my public repos are already cleaned up and would do fine — they are listed in there.

Their contact is [email]. No rush — sometime in the next week or two.

And thank you. This is genuinely more useful to me than another statement of purpose.

Erick

---

*Attach: the candidate brief (`code-trial-candidate.md`), and send or link
`code-trial-host.md`.*
