# Bonus: The model hierarchy

**Pencil, spreadsheet, simulation.** *Optional.* It belongs to no milestone and is not required.
Best taken after *Spreadsheet discipline* and *Sanity checks and orders of magnitude*, and before
you build anything large. About four hours.

## Why this exists

A large model that returns a number has not explained anything. It has produced a number, and the
number is only as trustworthy as your ability to say **why** it came out that way. If you cannot,
you cannot tell a finding from a bug, and neither can your committee.

The cure is old and has three names. The one Jones was taught as a PhD student is
**analytical → numerical → computational**. The plainer ones are **crawl, walk, run**, and the
one this lab uses: **pencil, spreadsheet, simulation.**

- **Pencil.** Strip the problem to the smallest form that still has the mechanism in it, and solve
  that by hand. A closed form, a threshold, a sign, an equilibrium, a scaling law.
- **Spreadsheet.** Step or enumerate that small model numerically, fit it to real data, and check
  it reproduces the pencil result exactly where the pencil result applies.
- **Simulation.** Now run the full computational study, and check that it collapses to the pencil
  result when you switch its extra features off.

The rungs do different jobs, and the job each one does is the reason you need all three. **The
pencil shows the mechanism the big model hides. The big model tests whether the pencil's
simplifications matter.** Neither answers the other's question.

## External material

- I. M. Held, "[The gap between simulation and understanding in climate
  modeling](https://doi.org/10.1175/BAMS-86-11-1609)," *Bulletin of the American Meteorological
  Society* 86(11), 2005. Six pages. The argument that simulation without a hierarchy of simpler
  models behind it produces results nobody understands. **Read this one.**
- N. Jeevanjee, P. Hassanzadeh, S. Hill and A. Sheshadri, "[A perspective on climate model
  hierarchies](https://doi.org/10.1002/2017MS001038)," *Journal of Advances in Modeling Earth
  Systems* 9(4), 2017. What makes a hierarchy useful, with worked examples.
- W. L. Oberkampf and C. J. Roy, *[Verification and Validation in Scientific
  Computing](https://doi.org/10.1017/CBO9780511760396)*, Cambridge, 2010. The chapters on code
  verification: checking a large code against an analytical solution is the standard method,
  not a shortcut.
- G. Pólya, *How to Solve It*, 1945. "Solve a simpler related problem first." The whole idea in
  one heuristic.
- R. W. Hamming's motto, from *Numerical Methods for Scientists and Engineers* (1962): *"The
  purpose of computing is insight, not numbers."*

## Governing part

None.

## A worked example

From Jones's own carbon research. Two equations: atmospheric carbon *C*, a reservoir *R* that
the atmosphere drains into, emissions *E*, and pre-industrial level *C₀*.

    dC/dt = E − k(C − R)
    dR/dt = γ·k(C − R) − μ(R − C₀)

**Pencil.** Set both derivatives to zero. The long-run equilibrium is

    C_eq = C₀ + E(1/k + γ/μ)

and the emissions that hold a target concentration forever are

    E_hold = (C_target − C₀) / (1/k + γ/μ)

That is two resistances in series. Read it and the mechanism is in front of you: CO₂ falls
whenever *E* < *k*(*C* − *R*), and the slower of the two drains sets how much you can emit.
**Each simpler model is this one with a parameter switched off.** Set γ = 0 and the reservoir
never fills, so *C* relaxes toward *C₀* like a one-box model. Set μ = 0 and nothing leaves the
reservoir, a two-box model with no equilibrium at all.

**Spreadsheet.** Step the equations one year at a time. Fit *k*, γ and μ to the Mauna Loa
record by grid search. Then hold *E* constant, run it long, and check the number it settles at
against *C_eq*. If they disagree, one of them is wrong, and you find out which now.

**Simulation.** Cross-check against published climate models, FaIR and Hector. The simple model
says where the balance point is and why. The big models say whether it survives more physics:
temperature feedbacks, ocean layers, a saturating land sink.

## The mechanic

Do this on **your own** dissertation problem. It works for optimization as well as dynamics;
most of this lab's problems are optimization, so there are examples of both below.

**1. Pencil.** Write the smallest version of your problem that still contains the thing you
care about, and solve it by hand. Stop when you have a result in symbols: a closed form, a
threshold, a sign, or a comparative static (which way the answer moves when one input rises).

- *Dynamics:* one or two state variables; find the equilibrium and its stability.
- *Capacity expansion:* one node, one period, two technologies. The screening curve gives the
  capacity factor at which one beats the other, in closed form.
- *Supply chain:* one supplier, one plant, one product. The break-even disruption probability
  at which a second source pays for itself.
- *Network or assignment:* small enough to enumerate, so the optimum is found by inspection and
  its shadow prices read off by hand.

**2. Spreadsheet.** Build that same small model numerically, in a spreadsheet or notebook. Put
real numbers in it, from data where you can. Then **choose one case where the pencil result
applies exactly** and show the two agree to rounding.

**3. Simulation.** Take your full model and **set it to the degenerate case**: switch off the
features the pencil model lacks (one node, one period, one technology, no uncertainty, whatever
applies). It must reproduce the spreadsheet. If your full model cannot be reduced that far, say
which feature cannot be turned off and reduce it as far as it will go.

**4. Write down what each rung showed.** One sentence each: what the pencil made obvious that
the simulation hides, and what the simulation revealed that the pencil got wrong or could not
see. If the answer to the second is "nothing," your full model may not be earning its cost.

If you have not built your full model yet, do rungs 1 and 2 now and write rung 3 as the check
you will run when it exists. That is a pass. The hierarchy is most useful **before** the big
model, not after.

## Deliverable

A one-page PDF: the pencil derivation, the spreadsheet or notebook link, the degenerate-case
comparison table (pencil / spreadsheet / simulation, same inputs, three outputs), and the two
sentences from step 4.

## Competency check

- [ ] The pencil model is stated in symbols and solved by hand, to a closed form, threshold, sign or comparative static
- [ ] Each simpler model is shown to be the full one with something switched off, and what was switched off is named
- [ ] The spreadsheet reproduces the pencil result in at least one case, with the numbers shown
- [ ] The full model, set to the degenerate case, reproduces the spreadsheet, or the feature that cannot be switched off is named and the partial check is shown
- [ ] Any disagreement between rungs is explained, not averaged away
- [ ] One sentence on what the pencil showed that the simulation hides, and one on what the simulation showed that the pencil missed

## Turning it in

**If you do it, do it as one week's arithmetic entry.** Submit it to that week's **WA**
assignment in Canvas, the same one you would have submitted anyway, with the one-page PDF
attached and, in the text box, the pencil result in one line and whether the three rungs agreed.

It does not count toward a milestone and nothing else needs submitting. It is here because it
is how this lab checks a model, including one an AI wrote for you: if the full model, switched
down to the simple case, does not reproduce the hand result, something is wrong, and you now
know where to look.
