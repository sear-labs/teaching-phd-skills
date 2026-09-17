#!/usr/bin/env python3
"""Generate handbook/curriculum.html -- the whole curriculum on one skimmable page.

Built from skills/ and milestones/, so it cannot drift from the lessons. Regenerate
after editing any lesson:

    python scripts/build_curriculum_page.py

Different job from handbook/prospective-students.html. That page answers "should I
join this lab"; this one answers "what am I supposed to do this week, and what does
each of these actually involve" -- for somebody already here, comparing 28 options
without opening 28 files.
"""

import html
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "handbook" / "curriculum.html"

# (anchor, file stem, title, when to read it, one-line blurb)
COMPANIONS = [
    ("lab", "sear-lab-domain-knowledge", "SEAR Lab Domain Knowledge",
     "read in week one",
     "What this lab actually studies. Infrastructure has three layers &mdash; physical, digital, "
     "institutional &mdash; and a study that addresses only one of them gets the answer wrong. "
     "Surface level on purpose: each area names the course that goes deep."),
    ("discipline", "engineering-research-domain-knowledge",
     "Engineering Research Domain Knowledge",
     "read later, once the domain is familiar",
     "The questions behind the methods rather than inside them. What counts as evidence when you "
     "cannot run an experiment, and why a discount rate is a claim about how much future people "
     "matter."),
]


def front_matter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    meta = {}
    for line in text[3:end].strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, text[end + 4:].lstrip()


def section(body, heading):
    """Return the text under '## <heading>' up to the next '## '."""
    m = re.search(rf"^## {re.escape(heading)}\s*$", body, re.M | re.I)
    if not m:
        return ""
    rest = body[m.end():]
    nxt = re.search(r"^## ", rest, re.M)
    return (rest[:nxt.start()] if nxt else rest).strip()


def first_sentences(text, n=2):
    """Leading paragraph, trimmed to n sentences. Keeps the failure mode, drops the rest."""
    para = text.split("\n\n")[0].replace("\n", " ").strip()
    parts = re.split(r"(?<=[.!?])\s+", para)
    return " ".join(parts[:n]).strip()


def inline_md(s):
    """Minimal inline markdown -> HTML. Escape first, then re-introduce tags."""
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    # Restore the handful of raw tags our own source uses inside table cells.
    for tag in ("br", "small", "/small", "sup", "/sup"):
        s = s.replace(f"&lt;{tag}&gt;", f"<{tag}>")
    return s


def md_table(text):
    """First GFM pipe table in `text` -> HTML. Returns '' if there is none."""
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("|"):
            rows.append([c.strip() for c in line.strip("|").split("|")])
        elif rows:
            break
    if len(rows) < 3:
        return ""
    head, body = rows[0], rows[2:]          # rows[1] is the --- separator
    th = "".join(f"<th scope='col'>{inline_md(c)}</th>" for c in head)
    trs = []
    for r in body:
        cells = "".join(
            (f"<th scope='row'>{inline_md(c)}</th>" if i == 0
             else f"<td>{inline_md(c)}</td>")
            for i, c in enumerate(r))
        trs.append(f"<tr>{cells}</tr>")
    return (f"<div class='tablewrap'><table class='grid3'>"
            f"<thead><tr>{th}</tr></thead><tbody>{''.join(trs)}</tbody></table></div>")


# Sections that are navigation rather than subject matter.
SKIP_TOPICS = {"where to go deep", "three areas, three layers"}


def is_prose(p):
    """True for an ordinary paragraph. Excludes tables, quotes and list blocks --
    but NOT a paragraph that merely opens in bold, which is most of ours."""
    s = p.strip()
    if not s or s.startswith(("|", ">")):
        return False
    if re.match(r"^([-*+]|\d+\.)\s", s):
        return False
    return True


def companion_topics(body):
    """Every '## heading' with the first sentence under it, skipping table sections."""
    out = []
    for m in re.finditer(r"^## (.+?)\s*$", body, re.M):
        title = m.group(1).strip()
        rest = body[m.end():]
        nxt = re.search(r"^## ", rest, re.M)
        chunk = (rest[:nxt.start()] if nxt else rest).strip()
        para = next((p for p in chunk.split("\n\n") if is_prose(p)), "")
        gist = first_sentences(para, 2)
        # "Why it matters here:" is the useful half when a section leads with it.
        stripped = re.sub(r"^\*\*Why it matters here:\*\*\s*", "", gist)
        if stripped != gist and stripped:
            # The remainder continued a sentence, so it starts lowercase.
            gist = stripped[0].upper() + stripped[1:]
        if gist and title.lower() not in SKIP_TOPICS:
            out.append((title, gist))
    return out


def checklist(text):
    return [inline_md(m.group(1).strip())
            for m in re.finditer(r"^- \[ \] (.+)$", text, re.M)]


def load(kind):
    out = []
    for f in sorted((REPO / kind).glob("*.md")):
        meta, body = front_matter(f.read_text(encoding="utf-8"))
        out.append((f, meta, body))
    return out


def main():
    skills = load("skills")
    milestones = load("milestones")
    if not skills or not milestones:
        sys.exit("no skills or milestones found")

    by_ms = {}
    for f, meta, body in skills:
        by_ms.setdefault(meta["milestone"], []).append((f, meta, body))

    nav, sections = [], []
    for _, mm, mbody in milestones:
        code = mm["milestone"]
        group = by_ms.get(code, [])
        nav.append(f'<a href="#{code.lower()}"><span class="nc">{code}</span>'
                   f'{html.escape(mm["title"])}</a>')

        # Milestone blurb: first paragraph after the "**Tier:**" line.
        after = mbody.split("**Tier:**", 1)[-1]
        blurb = first_sentences(after.split("\n\n", 1)[-1], 3)

        cards = []
        for f, s, b in group:
            num = f.stem.split("-", 1)[0]
            why = first_sentences(section(b, "Why this exists"))
            deliverable = first_sentences(section(b, "Deliverable"), 1) \
                or s.get("submit_as", "")
            checks = checklist(section(b, "Competency check"))
            items = "".join(f"<li>{c}</li>" for c in checks)
            cards.append(f"""      <article class="skill" id="s{num}">
        <div class="num">{num}</div>
        <div class="sk">
          <h3>{html.escape(s["title"])}</h3>
          <p class="meta"><span class="ch ch-{s.get('channel','')}">{html.escape(s.get('channel',''))}</span>
            <span>{html.escape(s.get('time','') )}</span>
            <span>prereq: {inline_md(s.get('prerequisites','none'))}</span></p>
          <p class="why">{inline_md(why)}</p>
          <p class="deliv"><strong>Turn in</strong> {inline_md(s.get('submit_as',''))}</p>
          <details><summary>Passes when &mdash; {len(checks)} checks</summary>
            <ul>{items}</ul></details>
        </div>
      </article>""")

        sections.append(f"""    <section id="{code.lower()}">
      <div class="mshead">
        <h2><span class="mcode">{code}</span> {html.escape(mm["title"])}</h2>
        <p class="tier">{html.escape(mm.get("tier",""))} &middot; {len(group)} skills</p>
      </div>
      <p class="blurb">{inline_md(blurb)}</p>
{chr(10).join(cards)}
    </section>""")

    # The two ungraded pages. Listed after the milestones, marked as ungraded, in the
    # order a student should meet them: this lab first, the wider discipline second.
    for anchor, stem, title, when, blurb in COMPANIONS:
        f = REPO / "handbook" / f"{stem}.md"
        if not f.exists():
            continue
        body = f.read_text(encoding="utf-8")
        nav.append(f'<a href="#{anchor}" class="nu"><span class="nc">&mdash;</span>'
                   f'{html.escape(title.split(" Domain")[0])}</a>')
        topics = "".join(
            f"<li><h4>{inline_md(t)}</h4><p>{inline_md(g)}</p></li>"
            for t, g in companion_topics(body))
        sections.append(f"""    <section id="{anchor}" class="companion">
      <div class="mshead">
        <h2><span class="ungraded">ungraded</span> {html.escape(title)}</h2>
        <p class="tier">{html.escape(when)}</p>
      </div>
      <p class="blurb">{blurb}</p>
      {md_table(body)}
      <ul class="topics">{topics}</ul>
      <p class="deliv"><a href="{stem}.md">Read the full page &rarr;</a></p>
    </section>""")

    page = TEMPLATE.format(
        count=len(skills),
        nav="\n      ".join(nav),
        sections="\n".join(sections),
    )
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO)}  ({len(skills)} skills, "
          f"{len(milestones)} milestones, {len(page):,} bytes)")


TEMPLATE = """<title>The Whole Curriculum</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Serif:ital,wght@0,400;0,600;1,400&display=swap">
<style>
  :root {{
    --paper:#FAFAF7; --surface:#F2F2EE; --ink:#101C24; --body:#2A3A44; --muted:#5A6B74;
    --rule:#D9DBD5; --rule-soft:#E8E9E4; --accent:#0E5A60; --accent-dim:#4A858A; --signal:#B06A2C;
    --display:"IBM Plex Serif",Georgia,serif;
    --sans:"IBM Plex Sans",-apple-system,"Segoe UI",Helvetica,Arial,sans-serif;
    --mono:"IBM Plex Mono",ui-monospace,Consolas,monospace;
  }}
  @media (prefers-color-scheme: dark) {{
    :root:not([data-theme="light"]) {{
      --paper:#0B1418; --surface:#121F25; --ink:#EDF1F1; --body:#C2CFD4; --muted:#8A9BA3;
      --rule:#24343C; --rule-soft:#1A2930; --accent:#5FB3B8; --accent-dim:#3E7D82; --signal:#D6944E;
    }}
  }}
  :root[data-theme="dark"] {{
    --paper:#0B1418; --surface:#121F25; --ink:#EDF1F1; --body:#C2CFD4; --muted:#8A9BA3;
    --rule:#24343C; --rule-soft:#1A2930; --accent:#5FB3B8; --accent-dim:#3E7D82; --signal:#D6944E;
  }}
  * {{ box-sizing:border-box; }}
  body {{ background:var(--paper); color:var(--body); font-family:var(--sans);
         font-size:16px; line-height:1.6; -webkit-font-smoothing:antialiased; }}
  .wrap {{ max-width:56rem; margin:0 auto; padding-inline:22px; padding-block:0 72px; }}

  header {{ padding-block:38px 20px; border-bottom:1px solid var(--rule); }}
  .kicker {{ font-family:var(--mono); font-size:11.5px; letter-spacing:.14em;
             text-transform:uppercase; color:var(--accent); margin:0 0 10px; }}
  h1 {{ font-family:var(--display); font-weight:600; font-size:clamp(1.9rem,4.4vw,2.6rem);
        line-height:1.12; letter-spacing:-.016em; color:var(--ink); margin:0; text-wrap:balance; }}
  .standfirst {{ font-family:var(--display); font-size:1.04rem; line-height:1.56;
                 margin:16px 0 0; max-width:40rem; }}

  nav {{ position:sticky; top:0; z-index:5; display:flex; flex-wrap:wrap; gap:6px;
         padding-block:12px; margin-bottom:8px; background:var(--paper);
         border-bottom:1px solid var(--rule-soft); }}
  nav a {{ font-family:var(--mono); font-size:12px; text-decoration:none; color:var(--body);
           padding:5px 9px; border:1px solid var(--rule-soft); border-radius:2px; }}
  nav a:hover {{ border-color:var(--accent); color:var(--accent); }}
  nav a:focus-visible {{ outline:2px solid var(--signal); outline-offset:2px; }}
  nav .nc {{ color:var(--signal); font-weight:500; margin-right:6px; }}
  nav .nu {{ border-style:dashed; }}

  section {{ margin-top:46px; scroll-margin-top:64px; }}
  .mshead {{ display:flex; flex-wrap:wrap; align-items:baseline; gap:8px 16px;
             padding-bottom:8px; border-bottom:2px solid var(--ink); }}
  h2 {{ font-family:var(--display); font-weight:600; font-size:1.5rem; color:var(--ink);
        margin:0; letter-spacing:-.012em; }}
  .mcode {{ font-family:var(--mono); color:var(--signal); font-size:1.15rem; margin-right:6px; }}
  .tier {{ font-family:var(--mono); font-size:11.5px; letter-spacing:.07em;
           text-transform:uppercase; color:var(--muted); margin:0; }}
  .blurb {{ font-family:var(--display); font-size:1.02rem; color:var(--body);
            margin:14px 0 4px; max-width:40rem; }}

  .skill {{ display:grid; grid-template-columns:2.6rem 1fr; gap:0 14px;
            padding-block:18px; border-bottom:1px solid var(--rule-soft); }}
  .num {{ font-family:var(--mono); font-size:13px; color:var(--accent-dim);
          font-variant-numeric:tabular-nums; padding-top:3px; }}
  h3 {{ font-family:var(--display); font-weight:600; font-size:1.12rem; color:var(--ink);
        margin:0 0 5px; line-height:1.25; }}
  .meta {{ display:flex; flex-wrap:wrap; gap:5px 12px; font-family:var(--mono);
           font-size:11px; color:var(--muted); margin:0 0 9px; }}
  .ch {{ text-transform:uppercase; letter-spacing:.08em; color:var(--signal); }}
  .why {{ margin:0 0 7px; max-width:38rem; }}
  .deliv {{ margin:0; font-size:14.5px; color:var(--muted); max-width:38rem; }}
  .deliv strong {{ color:var(--ink); font-weight:600; }}

  details {{ margin-top:9px; }}
  summary {{ font-family:var(--mono); font-size:11.5px; letter-spacing:.05em;
             color:var(--accent); cursor:pointer; padding:3px 0; }}
  summary:focus-visible {{ outline:2px solid var(--signal); outline-offset:2px; }}
  details ul {{ margin:8px 0 2px; padding-left:1.1rem; }}
  details li {{ font-size:14px; margin-bottom:4px; color:var(--body); }}

  /* --- the two ungraded pages --- */
  .companion {{ background:var(--surface); padding:2px 22px 24px; margin-top:52px;
                border-top:2px solid var(--signal); }}
  .companion .mshead {{ border-bottom:1px solid var(--rule); }}
  .ungraded {{ font-family:var(--mono); font-size:10.5px; letter-spacing:.12em;
               text-transform:uppercase; color:var(--signal); border:1px solid var(--signal);
               border-radius:2px; padding:2px 6px; margin-right:9px;
               vertical-align:middle; font-weight:500; }}
  .topics {{ list-style:none; margin:18px 0 0; padding:0;
             display:grid; gap:14px 28px; }}
  .topics h4 {{ font-family:var(--display); font-weight:600; font-size:1rem;
                color:var(--ink); margin:0 0 3px; }}
  .topics p {{ margin:0; font-size:14.5px; color:var(--body); max-width:38rem; }}

  .tablewrap {{ overflow-x:auto; margin:18px 0 4px; }}
  .grid3 {{ border-collapse:collapse; width:100%; min-width:40rem; font-size:13px; }}
  .grid3 th, .grid3 td {{ border:1px solid var(--rule); padding:8px 10px;
                          vertical-align:top; text-align:left; }}
  .grid3 thead th {{ font-family:var(--mono); font-size:11px; letter-spacing:.06em;
                     text-transform:uppercase; color:var(--accent); font-weight:500; }}
  .grid3 thead th small {{ display:block; font-size:10px; letter-spacing:0;
                           text-transform:none; color:var(--muted); margin-top:2px; }}
  .grid3 tbody th {{ font-family:var(--display); font-size:14px; color:var(--ink);
                     white-space:nowrap; }}
  .grid3 td {{ color:var(--body); }}

  code {{ font-family:var(--mono); font-size:.88em; background:var(--surface);
          padding:1px 4px; border-radius:2px; }}
  a {{ color:var(--accent); text-underline-offset:2px; }}
  footer {{ margin-top:48px; padding-top:18px; border-top:1px solid var(--rule-soft);
            font-family:var(--mono); font-size:11.5px; color:var(--muted); }}

  @media (max-width:640px) {{
    .skill {{ grid-template-columns:1fr; gap:4px; }}
    .num {{ padding-top:0; }}
  }}
</style>

<div class="wrap">
  <header>
    <p class="kicker">SEAR Lab &middot; UT Arlington</p>
    <h1>The whole curriculum, on one page</h1>
    <p class="standfirst">All {count} skills with what each one is for, what you hand in, and the
      checklist it is graded against. Built for choosing what to do this week without opening
      {count} files. Every lesson exists in full in the handbook; this is the index.</p>
  </header>

  <nav aria-label="Milestones">
      {nav}
  </nav>

{sections}

  <footer>
    Generated from the lesson files &mdash; do not edit by hand.
    github.com/sear-labs/teaching-phd-skills
  </footer>
</div>
"""


if __name__ == "__main__":
    main()
