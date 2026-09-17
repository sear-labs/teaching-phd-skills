# Where we work

**Read this first.** Not because it is graded — it is not — but because almost nothing else in
the lab makes sense until you have it.

This is the surface. Every section ends with the course that goes deep, and those courses are
where you actually learn this material. What follows is the map, not the territory.

---

## The thesis: infrastructure has three layers

Societies thrive or struggle on the infrastructure they build, and that infrastructure is never
only physical. It spans three inseparable layers:

- **Physical** — the systems and hardware that move energy and materials. Plants, lines, cells,
  readers, the experiments that tell you how they behave.
- **Digital** — the models and data that make those flows visible and optimizable. Capacity
  expansion models, supply chain optimisation, surrogates, analytics.
- **Institutional** — the policy, incentives, programs and alignment that decide what actually
  gets built. Markets, standards, tariffs, municipal programs.

**This is the single most useful idea in the lab, and it is a claim, not a taxonomy.** The claim
is that a study which addresses only one layer gets the answer wrong. A battery recovery process
that works at the bench and has no reverse-logistics network is not a solution. A capacity
expansion model that ignores who is permitted to build is not a forecast. A tracking system
nobody is required to use produces no data.

When your work stalls, it is very often because it has quietly become single-layer.

## Three areas, three layers

Everything the lab does sits somewhere in this grid.

| | **Physical** <br><small>systems, hardware, experiments</small> | **Digital** <br><small>models, analytics, decision tools</small> | **Institutional** <br><small>policy, programs, deployment</small> |
|---|---|---|---|
| **Energy systems** | shipboard power and HESM · NAVSEA land-based testing · microgrids from repurposed EV batteries and solar | ReEDS and GCAM · data-centre and AI load growth · transmission expansion under renewable buildout · surrogate optimisation and DACE | Green Warriors weatherization in South Dallas · energy burden and DERs · Powerhouse Texas EPAC · cited in IPCC AR6 WGIII |
| **Critical minerals** | 500+ kWh of recovered EV batteries and motors · shred, grind, sieve · electrical, chemical and powder analysis · 3R-BET | global lithium supply chain optimisation · centralized vs. decentralized black mass · reverse logistics and recycling network design | trade and tariff policy · domestic supply chain security · NAATBatt Track and Trace · geothermal on tribal lands and HUBZones |
| **RFID and asset tracking** | antennas, readers, printers · real-time location systems · circular conveyor and robotic arm · operational hospital beds | plant-level inventory systems · asset performance analytics · set-cover optimisation for reader placement · blockchain provenance | battery track-and-trace standards · community naloxone distribution · pharmaceutical anti-diversion · health asset management |

Find the cell your project sits in. Then find the two cells in your row that it does **not**
address, and be able to say why that is acceptable.

---

## 1. Energy systems

The system that keeps the lights on, and the system this lab models most.

**The short version.** Electricity cannot be stored at scale cheaply, so supply must match demand
continuously, second by second. Everything difficult about power systems follows from that one
constraint. Generation has to be dispatched, transmission has to carry it, and somebody has to
decide who pays for the capacity that sits idle most of the year waiting for the peak.

**What makes Texas unusual**, and why the lab is here: ERCOT covers most of Texas and is *not
synchronously connected* to the rest of the country, which means Texas largely regulates its own
grid. It is an energy-only market — generators are paid for energy produced, not for capacity
held in reserve — which is a live and contested design choice, not a technical fact. Texas is
first in the country in electricity production, and first in both wind and utility solar.

**Where the lab works.** Dense, islanded, high-power loads — shipboard plants through to data
centres. Macro energy-system modelling with ReEDS and GCAM-USA. And the institutional layer
through weatherization, energy burden, and state policy.

**Goes deep:** REE 4301 *Energy Systems Modeling*, with its open-access textbook. Take it.

## 2. Critical mineral supply chains

**End to end and back.** This phrase is the lab's central intellectual claim and it is worth
understanding precisely.

The chain runs mine → processing → manufacturing → deployment → monitoring → remanufacturing and
reuse → recycling — **and then back to materials**, closing the loop. Most research cuts the
chain somewhere and studies a segment. The claim here is that the segments are coupled tightly
enough that studying one in isolation produces answers that do not survive contact with the
others.

**What makes a mineral "critical."** Not rarity. A mineral is critical when it is economically
essential *and* its supply is vulnerable to disruption — which makes criticality a political and
economic judgement, published in lists that governments revise. Lithium, cobalt, nickel, graphite
and the rare earths are the usual battery-relevant names.

**The bottleneck the lab works on physically** is end-of-life recovery: black mass production and
hydrometallurgical recovery of metals from retired lithium-ion batteries. The lab has scaled from
a junkyard Nissan Leaf pack to nineteen retired Workhorse EV batteries.

**Goes deep:** IE 6301 *Critical Mineral Supply Chain Modeling*.

## 3. RFID and asset tracking

> *What cannot be tracked cannot be managed, or improved.*

**The short version.** RFID tags carry an identifier that a reader can interrogate without line
of sight. That single property — no line of sight — is what separates it from a barcode and is
the reason it works for pallets, hospital beds, and battery packs moving through a facility.

**What to understand before you design anything with it.** Passive tags have no battery and are
powered by the reader's field, so read range is bounded by physics rather than by engineering
effort. Metal and liquid detune and absorb. Read rates in a real facility are not the read rates
on a spec sheet, and the gap between them is where most deployments fail. Reader placement is a
coverage problem, which is why it shows up here as set-cover optimisation.

**Why it belongs next to the other two.** A traceable battery is what makes a circular supply
chain auditable rather than aspirational — which is why battery track-and-trace standards are an
active institutional fight, and why the lab sits on the NAATBatt committee for it.

**Goes deep:** ask about current projects; this area is taught through the work rather than a
single course.

---

## Numbers worth carrying

Order-of-magnitude anchors for energy work. Not for precision — for catching a result that is
wrong by a factor of a thousand, which is the failure that survives code review.

| | |
|---|---|
| 1 Quad | 10<sup>15</sup> BTU |
| 1 kWh | 3,412 BTU |
| One US house | ~10<sup>4</sup> kWh/year |
| Homes per Quad | ~10<sup>8</sup> |
| Car travel | ~3,500 BTU per vehicle-mile |

This is the same habit as [sanity checks](../skills/05-sanity-checks.md) in M1 — predict the
magnitude before you run, then check the units.

## Working across borders

The supply chains here cross a dozen jurisdictions with different rules, different data
conventions, and genuinely different ideas about what a deadline means. The lab collaborates
internationally and most of its students trained somewhere other than the United States.

This is learned by paying attention rather than by reading, which is exactly why it is not a
graded skill. But it is not optional, and assuming your own conventions are the default is a
reliable way to lose six weeks.

---

## Where to go deep

| Course | Covers |
|---|---|
| **REE 4301** Energy Systems Modeling | dispatch, capacity expansion, LP and MILP formulations of the grid — with an open-access textbook |
| **IE 6301** Critical Mineral Supply Chain Modeling | the supply chain as an optimisation problem, end to end |
| **IE 5301** Advanced Operations Research | the optimisation methods everything above is built on |
| **IE 3315** Operations Research I | if you have never formulated an LP |

If a section above raised a question this page does not answer, that is the page working
correctly. Go to the course, or ask.

---

*See also [What the Model Assumes](what-the-model-assumes.md) — the questions that sit behind
the methods rather than inside them. Read that one later, when this page has stopped feeling
new.*
