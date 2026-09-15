# Choosing Tools for Interactive & Computational Work

Notes on when to use which format, where computation should live, and why the
defaults are what they are. Written to be applied to future code and documents.

---

## 1. The core question: where does the computation live?

Everything downstream follows from this. Three places code can run:

| Location | What runs there | Cost / constraint |
|---|---|---|
| **Build time** (your laptop, CI) | Python scripts, data prep, model solves | Runs once, output is frozen |
| **Client** (the user's browser) | JS, WASM | Free to host, but user's CPU/memory; no secrets |
| **Server** (a live process) | Flask/FastAPI/Django, Gurobi, DB queries | Costs money, must stay alive, but unbounded |

"Static site" describes only *how the page was delivered* — prebuilt files
handed to the browser rather than generated per-request. It says **nothing**
about what the JS can do once it lands. JS on a Netlify-hosted page runs in the
exact same engine as JS on any dynamic site.

---

## 2. When you actually need a live server

Reach for a backend only when at least one of these is true:

1. **Compute exceeds the browser** — commercial solvers (Gurobi), large-scale
   simulation, real ML training.
2. **Data too big or too private to ship** — must query a DB rather than
   download it; NDA/IP-restricted data can't sit in client-visible JS.
3. **State must persist** — logins, saved work, multi-user collaboration.
4. **Secrets are involved** — API keys, DB credentials. Anything in client JS is
   readable by anyone who opens dev tools.
5. **Third-party service calls** — payments, email, another org's API.

If none apply, a server is overhead. Note that *user-chosen parameters alone do
not require a server* — `erickjonesphd.com/model` has unpredictable inputs and
recomputes entirely client-side.

---

## 3. Tool classes (vocabulary)

| Class | Purpose | Examples |
|---|---|---|
| Static site generators | Content → prebuilt HTML | Hugo, Astro, Eleventy, Jekyll, Zola, Docusaurus, VitePress, Next.js/Nuxt (SSG mode) |
| CMS / no-code | GUI editing by non-developers, DB-backed | WordPress, Squarespace, Wix, Webflow, Drupal |
| Backend frameworks | Persistent server process | Flask, FastAPI, Django, Express, Rails |
| Python app frameworks | Script → UI, needs live process | Streamlit, Dash, Gradio, Panel |
| Frontend JS frameworks | Stateful client UI | React, Vue, Svelte, Angular |
| Databases | Structured storage/query | Postgres, MySQL, SQLite, MongoDB |
| Serverless / edge | Backend logic, no persistent process | Netlify/Vercel Functions, AWS Lambda, Cloudflare Workers |
| Charting / diagrams | Render data or text as visuals | Chart.js, Plotly.js, D3, Vega-Lite; Mermaid |
| Notebooks | Exploratory compute (not a shipping format) | Jupyter, Colab |
| Client-side compute | Heavy work in the browser | Web Workers, WebAssembly (WASM) |

---

## 4. Client-side compute: Web Workers and WASM

Two different axes — they combine well.

### Web Workers — *keeps the UI responsive*
- A second browser thread. Isolated memory, **no DOM access**, communicates only
  via `postMessage`.
- Does **not** make computation faster; prevents the tab from freezing while it
  runs.
- Use for: long-running loops, parsing large CSVs, Monte Carlo runs, anything
  where the user should still be able to scroll and click.

### WASM — *makes the computation faster*
- Compact, statically typed bytecode compiled from C/C++/Rust/Fortran. The
  browser translates it to machine code in one fast pass, with no type guessing.
- Near-native speed because the types were fixed at compile time — unlike JS
  engines, which speculate about types and must bail out when wrong.
- Use for: real numerical work — solvers, physics, signal processing.

### Rough performance gradient in the browser
- **Trivial:** arithmetic, DOM updates, stock-and-flow models — microseconds.
- **Comfortable (surprisingly so):** 60fps physics engines, Monte Carlo with
  millions of iterations, small/medium matrix math, ML inference (TensorFlow.js,
  ONNX Runtime Web).
- **Risky:** O(n²)+ over 100k+ rows, dense linear algebra at scale.
- **Out:** licensed solvers (Gurobi), research-scale MILP.

### Failure mode
There is **no complexity governor.** The browser will attempt anything:
- Main thread blocked too long → tab freezes → "Page Unresponsive."
- Memory exceeded → tab crashes (much sooner on phones).

The hosting platform does not police this. Keeping it bounded is on the author.

---

## 5. Serverless vs. a "real" server

The difference is **lifecycle, not size.**

- **Real server:** one process, always running, holds in-memory state (open DB
  connections, caches). Costs money idle. → Render, Railway, Fly.io, a VPS.
- **Serverless function:** no persistent process. Spun up per request, runs,
  torn down. **Nothing survives between invocations.** Costs nothing when idle.

This is why Netlify can offer functions while being "static-only" — it isn't
hosting a process, it's routing a request to ephemeral infrastructure for a few
hundred milliseconds. Serverless can hold a *secret* (env var per invocation)
but cannot hold *session state* without an external database.

### Deployment shapes when a real backend is needed
1. **Split (preferred):** static frontend on Netlify + separate API service
   elsewhere; frontend calls it via `fetch("https://api.example.com/...")`.
   Two deployments, two URLs.
2. **Unified:** the backend also serves the frontend files. One URL, simpler
   ops, loses static CDN speed for the frontend.

---

## 6. Escalation ladder

Start at 1. Only move down when a specific trigger from §2 forces it.

1. Vanilla HTML/CSS/JS, static.
2. Same, plus a charting library (Chart.js / Plotly.js).
3. React — when widget state genuinely outgrows plain DOM scripting.
4. Web Worker and/or WASM — heavy compute, still fully static.
5. Serverless function — one secret, one API call, one small persisted value.
6. Real backend (Flask/FastAPI) on a process host — the §2 triggers.
7. Backend + database — persistent multi-user state.

---

## 7. Why Python dominates, and when to leave it

### Why compiled languages are faster
1. **AOT compilation vs. interpretation** — C/Rust compile once to machine code;
   Python interprets its bytecode instruction-by-instruction on every run.
2. **Static vs. dynamic typing** — `x + y` in Python checks types at runtime;
   in C the compiler already emitted the one correct instruction.
3. **Memory management** — refcounting and GC overhead vs. manual (C) or
   compile-time-checked (Rust) memory with zero runtime cost.

"Binary"/"native" = the actual instruction set of a CPU (x86-64, ARM64),
executed directly with no translation layer.

### Why auto-porting Python → C/Rust isn't routine
- **It's a semantics problem, not a translation problem.** Duck typing,
  monkey-patching, generators, dynamic return types — none have clean statically
  typed equivalents. Existing tools are narrow for exactly this reason: Cython
  and mypyc need type annotations; Numba only JITs tightly typed numeric loops.
- **The hot path is usually already compiled.** NumPy, SciPy, pandas, PyTorch
  are C/C++/Fortran underneath (SciPy links LAPACK/BLAS). Python is the
  orchestration layer; rewriting the glue speeds up nothing.
- **The bottleneck is usually human, not CPU.** Optimize language choice only
  after confirming you are actually compute-bound.

Where AI-assisted porting *is* real: legacy C → memory-safe Rust, and inferring
ownership/lifetime annotations. Reached for after a bottleneck is identified.

---

## 8. Historical context (so the defaults make sense)

- Static HTML/CSS/JS is the **original** web, not a new trend.
- ~2003–2015: CMS platforms (WordPress, Squarespace) won because they removed
  the need to write code — the advantage was *no-code*, not *dynamic*.
- ~2010–2020: React et al. won for genuine applications, where plain JS became
  unmanageable at scale.
- ~2013–2021: static site generators returned among developers (the "JAMstack"
  movement) for speed, security, and near-zero hosting cost.
- **What GenAI changed:** it removed the labor cost that made CMS platforms
  necessary for non-developers — not the static/dynamic tradeoff itself.

---

## 9. MCP (Model Context Protocol)

Unrelated to hosting; it is about **how an AI talks to external tools and data.**

- **Problem it solves:** N AI products × M tools previously required a custom
  integration per pair.
- **How:** a tool vendor builds *one* MCP server declaring its capabilities
  (search email, query a DB, create a task); any MCP-compatible client speaks
  the same protocol. Analogous to USB-C, or ODBC/JDBC for databases.
- **Why it's everywhere:** it has become the common plumbing for agentic
  workflows — AI that *does* things across tools rather than only answering.
- Open-sourced by Anthropic; now supported well beyond Anthropic products.

---

## 10. Decision checklist

Before choosing a stack, answer in order:

1. **Who edits the content?** Me + AI → static generator. Non-technical person
   via GUI → CMS.
2. **When does the compute run?** Once at build → Python → static JSON. Per
   user interaction → JS/WASM in browser. Per request with heavy load → server.
3. **Does it touch secrets or private data?** Yes → server or serverless. No →
   client is fine.
4. **Must it remember anything between visits?** Yes → database. No → stateless.
5. **Will the heaviest operation freeze a phone?** If unsure, assume yes →
   Worker, WASM, or move it server-side.

### Standing defaults
- Python for computation and data prep — output to JSON/CSV, not a live process.
- Vanilla JS + a charting library for interactivity; React only when state
  demands it.
- Mermaid for architecture/flow diagrams; not for data-driven models.
- Streamlit/Dash for internal tools only — incompatible with static hosting.
- Markdown for anything meant to be read rather than manipulated.

---

## 11. Tools worth remembering by name

- `highs-js` (npm: `highs`) — HiGHS LP/MILP solver compiled to WASM, runs in the
  browser. Accepts models in **LP format** as a string. MIT licensed.
- `fuglede/highs-wasm` — lower-level HiGHS WASM bindings taking sparse (CSC/CSR)
  constraint matrices directly, for when LP-format string generation is clumsy.
- `glpk.js` — older/smaller LP-MILP option.
- TensorFlow.js / ONNX Runtime Web — ML inference client-side.
- Chart.js, Plotly.js, D3, Vega-Lite — charting, lightest to heaviest.
- Astro, Hugo, Eleventy — static generators.
- Netlify / Vercel / Cloudflare Workers — static + serverless hosting.
- Render / Railway / Fly.io — persistent process hosting.

---

## 12. Ads and analytics on a static site

Core pattern, and it recurs everywhere in §13 too: **a third-party's server
does the dynamic work; your site just embeds a client-side call to it.** An ad
network's JS tag calls their server, which picks the ad (often via a real-time
auction, ~100ms), serves it, and logs the impression — all on their
infrastructure, not yours. Clicks route through their redirect URL, logged the
same way. This is why AdSense, Carbon Ads, EthicalAds, and BuySellAds all run
fine on a fully static Hugo/Jekyll/Astro site.

### Old-school vs. self-rolled vs. network
| Approach | Where tracking lives | What you get | Effort |
|---|---|---|---|
| Static rotating banner, no tracking | Nowhere | Ad displays, no metrics — the newspaper model | Trivial |
| Self-rolled | Serverless function + a tiny counter (Netlify Functions + Upstash Redis, Supabase) | Views *and* clicks (same fetch-on-load / redirect-through-a-function pattern for both) — but you own turning raw counts into a report | Small |
| Third-party ad network | Their servers | Full dashard: impressions, viewability, clicks, frequency, conversions, fraud filtering, ready-made reports | A script tag |

### What ad networks track beyond raw clicks/views
Viewability (≥50% visible for ≥1s, not just present in the HTML), unique
reach/frequency, device/browser/rough geo, cross-site conversions (via a pixel
on the advertiser's own site), bot/fraud filtering, automatic A/B creative
testing.

### Cookie/tracking status (checked Sept 2026)
Google reversed its plan to kill third-party cookies — announced April 2025 it
would keep them on by default with a user opt-out, and shut down most of the
Privacy Sandbox replacement APIs that October. Safari/Firefox/Brave still block
third-party cookies by default (~17–20% of traffic). Same-site view/click
counting was never cookie-dependent, so none of this affects the basic
mechanism above — only cross-site frequency/conversion tracking.

### Worth paying for?
Ad network payouts scale with traffic; at low-traffic/local scale they're
typically fractions of a cent per view — often not worth the tracking overhead
or the cookie-consent burden it puts on a small site. A flat local sponsorship
rate (the newspaper model) is usually the better fit until traffic genuinely
supports network-level demand.

---

## 13. Other things assumed to need a dynamic backend, and don't

Same pattern as §12 throughout: outsource the dynamic part to a third party,
keep the site static.

| Assumed to need a server | Static-compatible via | How |
|---|---|---|
| Contact forms | Netlify Forms, Formspree | Form POSTs to their endpoint; they email you the submission |
| Site search | Pagefind, Lunr.js, Fuse.js | Search index built at compile time, shipped as a static file, searched in-browser |
| Comments | giscus, Utterances | Comments stored as GitHub issues via GitHub's API |
| Newsletter signup | Mailchimp/ConvertKit embed | Form posts straight to their API |
| Checkout/payments | Stripe Checkout, Snipcart | Client JS hands off to a hosted payment page |
| Login/accounts | Clerk, Auth0, Supabase Auth | Client SDK handles auth; a serverless function checks the token only when needed |
| Non-technical content editing | Headless CMS (Decap/Netlify CMS, Sanity) | GUI editor; saving triggers a rebuild, output stays plain files |
| RSVP with a hard capacity cap | Serverless function + a small DB (Supabase, Airtable) | The one real exception — two simultaneous submissions must not both win the last slot, so this needs an actual counter somewhere |

**Genuine exception, no way around it:** anything needing a held-open
connection — live chat, live-updating scores, multiplayer state. Serverless
functions spin up and die per request, so they can't hold a connection open;
this needs either a real persistent process or a managed real-time service
(Pusher, Ably) — the same "outsource it" trick one more time.
