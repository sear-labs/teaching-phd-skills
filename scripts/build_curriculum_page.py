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
    return s


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
