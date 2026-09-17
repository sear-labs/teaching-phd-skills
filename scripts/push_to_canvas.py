#!/usr/bin/env python3
"""Push the curriculum from this repo into a Canvas course.

The repo is the source of truth. Canvas is a delivery copy, regenerated from here.
Edit the Markdown, re-run this, and Canvas catches up. Never edit a generated page in
Canvas directly -- the next run overwrites it.

What it creates
---------------
    1 overview page   the 28-skill tracking table, generated from skills/ and
                      milestones/ so it cannot drift out of sync with them
    28 skill pages    one lesson package each
    2 companion pages the ungraded domain-knowledge pages, lab then discipline
    6 assignments     the milestone gates, pass_fail, in their own group, no due dates
    7 modules         Start Here + M1..M6, each holding its skill pages and its
                      milestone assignment

Modules are created UNGATED on purpose: no prerequisites, no completion requirements,
no sequential progress. A student picks any skill in any order. Canvas modules default
to linear gating, which would lock a fourth-year student behind an Excel lesson.

Idempotent: matches by title and updates in place, so re-running never duplicates.

Publishing
----------
Nothing is published unless you pass --publish. Without it everything is created or
updated invisible to students, which is what you want while drafting.

Usage
-----
    python scripts/push_to_canvas.py --course 277913 --dry-run
    python scripts/push_to_canvas.py --course 277913
    python scripts/push_to_canvas.py --course 277913 --publish

Requires
--------
    pandoc on PATH (Markdown -> HTML)
    CANVAS_TOKEN in the environment, or in the Windows user registry.
    The token is never written to this repo. This repo is public.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HOST = "https://uta.instructure.com"
MILESTONE_GROUP = "Competency Milestones"
MILESTONE_POINTS = 5
OVERVIEW_TITLE = "Research Competency Milestones"

# Ungraded companion pages, in the order a student should meet them: the lab's own
# domain first, the wider discipline second. (file stem, Canvas title)
COMPANION_PAGES = [
    ("sear-lab-domain-knowledge", "SEAR Lab Domain Knowledge"),
    ("engineering-research-domain-knowledge", "Engineering Research Domain Knowledge"),
]

# Titles this curriculum used to publish. Unpublished on every run so a rename does
# not leave the old page live beside the new one -- Canvas has no rename that
# preserves a page, so a retitle always creates a second one.
SUPERSEDED_PAGES = [
    "What We Don't Grade",
    "What the Model Assumes",
    "Where We Work",
]


# --------------------------------------------------------------------------- token

def get_token():
    """Environment first; fall back to the Windows user registry.

    On this machine a long-lived parent process means os.environ can read empty for a
    variable that is genuinely set. An empty env var is not evidence the token is missing.
    """
    tok = os.environ.get("CANVAS_TOKEN")
    if tok:
        return tok
    if sys.platform == "win32":
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as k:
                return winreg.QueryValueEx(k, "CANVAS_TOKEN")[0]
        except OSError:
            pass
    sys.exit("CANVAS_TOKEN not found in environment or registry. Set it; do not paste it.")


# ----------------------------------------------------------------------- markdown

def parse_front_matter(text):
    """Return (dict, body). Front matter is simple `key: value` lines, no nesting."""
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


def md_to_html(md):
    try:
        out = subprocess.run(
            ["pandoc", "--from=gfm", "--to=html", "--wrap=none"],
            input=md, capture_output=True, text=True, encoding="utf-8", check=True,
        )
    except FileNotFoundError:
        sys.exit("pandoc not found on PATH. winget install JohnMacFarlane.Pandoc")
    except subprocess.CalledProcessError as e:
        sys.exit(f"pandoc failed: {e.stderr}")
    return out.stdout.replace("[ ]", "&#9744;")


def load(kind):
    """Load skills/ or milestones/ as [(path, meta, body)], in filename order."""
    out = []
    for f in sorted((REPO / kind).glob("*.md")):
        meta, body = parse_front_matter(f.read_text(encoding="utf-8"))
        out.append((f, meta, body))
    return out


# --------------------------------------------------------------------------- api

class Canvas:
    def __init__(self, token, course, dry_run=False, publish=False):
        self.token = token
        self.course = course
        self.dry_run = dry_run
        self.publish = publish
        self._cache = {}

    def _req(self, method, path, payload=None):
        url = f"{HOST}/api/v1/courses/{self.course}{path}"
        data = json.dumps(payload).encode("utf-8") if payload else None
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header("Authorization", f"Bearer {self.token}")
        if data:
            req.add_header("Content-Type", "application/json; charset=utf-8")
        try:
            with urllib.request.urlopen(req) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            sys.exit(f"{method} {path} -> {e.code}: {e.read().decode('utf-8')[:400]}")

    def get_all(self, path):
        """Paginate. Canvas defaults to 10 per page and silently truncates otherwise."""
        items, page = [], 1
        while True:
            batch = self._req("GET", f"{path}?per_page=100&page={page}")
            if not batch:
                return items
            items.extend(batch)
            if len(batch) < 100:
                return items
            page += 1

    # -- assignment groups --

    def ensure_group(self, name):
        for g in self.get_all("/assignment_groups"):
            if g["name"] == name:
                return g["id"]
        if self.dry_run:
            print(f"  [dry-run] would create assignment group {name!r}")
            return None
        g = self._req("POST", "/assignment_groups", {"name": name, "position": 6})
        print(f"  created assignment group {name!r} (id={g['id']})")
        return g["id"]

    # -- pages --

    def upsert_page(self, title, body):
        """Create or update; returns the page slug so callers can link to it."""
        existing = {p["title"]: p for p in self.get_all("/pages")}
        payload = {"wiki_page": {
            "title": title, "body": body,
            "published": self.publish, "editing_roles": "teachers",
        }}
        if title in existing:
            slug = existing[title]["url"]
            if self.dry_run:
                print(f"  [dry-run] would UPDATE page {title!r}")
                return slug
            self._req("PUT", f"/pages/{slug}", payload)
            print(f"  page  {'PUB ' if self.publish else '    '} {title}")
            return slug
        if self.dry_run:
            print(f"  [dry-run] would CREATE page {title!r}")
            return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        r = self._req("POST", "/pages", payload)
        print(f"  page  NEW  {title}")
        return r["url"]

    # -- assignments --

    def upsert_assignment(self, name, body, group_id):
        existing = {a["name"]: a for a in self.get_all("/assignments")}
        payload = {"assignment": {
            "name": name,
            "description": body,
            "submission_types": ["online_text_entry", "online_url"],
            "grading_type": "pass_fail",
            "points_possible": MILESTONE_POINTS,
            "assignment_group_id": group_id,
            "published": self.publish,
            # No due date: milestones are self-paced by design.
        }}
        if name in existing:
            aid = existing[name]["id"]
            if self.dry_run:
                print(f"  [dry-run] would UPDATE assignment {name!r}")
                return aid
            self._req("PUT", f"/assignments/{aid}", payload)
            print(f"  assn  {'PUB ' if self.publish else '    '} {name}")
            return aid
        if self.dry_run:
            print(f"  [dry-run] would CREATE assignment {name!r}")
            return None
        a = self._req("POST", "/assignments", payload)
        print(f"  assn  NEW  {name}")
        return a["id"]

    # -- modules --

    def upsert_module(self, name, position, items):
        """items: list of ('Page', slug, title) or ('Assignment', id, title).

        Created ungated: no prerequisites, no completion requirements, no sequential
        progress. Students choose order.
        """
        existing = {m["name"]: m for m in self.get_all("/modules")}
        # Publishing is deliberately NOT set here. Publishing a module also publishes
        # every item in it, so it must happen after stale items are pruned -- otherwise
        # a page being retired gets re-published on its way out.
        payload = {"module": {
            "name": name,
            "position": position,
            "require_sequential_progress": False,
            "prerequisite_module_ids": [],
        }}
        if name in existing:
            mid = existing[name]["id"]
            if self.dry_run:
                print(f"  [dry-run] would UPDATE module {name!r} ({len(items)} items)")
                return
            self._req("PUT", f"/modules/{mid}", payload)
        else:
            if self.dry_run:
                print(f"  [dry-run] would CREATE module {name!r} ({len(items)} items)")
                return
            mid = self._req("POST", "/modules", payload)["id"]

        existing_items = self.get_all(f"/modules/{mid}/items")
        have = {i["title"] for i in existing_items}
        wanted = {t for _, _, t in items}

        added = 0
        for kind, ref, title in items:
            if title in have:
                continue
            item = {"type": kind, "title": title, "indent": 1}
            if kind == "Page":
                item["page_url"] = ref
            else:
                item["content_id"] = ref
            self._req("POST", f"/modules/{mid}/items", {"module_item": item})
            added += 1

        # Prune items that are no longer part of this milestone. Without this, a
        # retired skill stays visible in the module long after its lesson is gone.
        pruned = 0
        for i in existing_items:
            if i["title"] not in wanted:
                self._req("DELETE", f"/modules/{mid}/items/{i['id']}")
                pruned += 1

        # Only now is it safe to publish: the stale items are gone, so publishing
        # cascades onto exactly the content this milestone still owns. Canvas also
        # ignores module[published] on create, so this doubles as that fix.
        self._req("PUT", f"/modules/{mid}", {"module": {"published": self.publish}})

        tail = f", {pruned} removed" if pruned else ""
        print(f"  mod   {'PUB ' if self.publish else '    '} {name}"
              f"  ({len(items)} items, {added} new{tail})")

    # -- retired content --

    def retire_orphan_skill_pages(self, keep_titles):
        """Unpublish skill pages whose lesson file no longer exists.

        Unpublish rather than delete: a retired lesson may be worth reinstating, and
        an unpublished page is already invisible to students.
        """
        orphans = [p for p in self.get_all("/pages")
                   if p["title"].startswith("Skill: ") and p["title"] not in keep_titles]
        for p in orphans:
            if self.dry_run:
                print(f"  [dry-run] would RETIRE page {p['title']!r}")
                continue
            self._req("PUT", f"/pages/{p['url']}",
                      {"wiki_page": {"published": False}})
            print(f"  retired  {p['title']}  (unpublished, not deleted)")
        return len(orphans)

    def retire_pages_by_title(self, titles):
        """Unpublish named pages this curriculum no longer publishes.

        Canvas has no rename that preserves a page, so a retitled page leaves the old
        one live. Listing the dead title here retires it on the next run.
        """
        existing = {p["title"]: p for p in self.get_all("/pages")}
        n = 0
        for t in titles:
            p = existing.get(t)
            if not p or not p["published"]:
                continue
            if self.dry_run:
                print(f"  [dry-run] would RETIRE page {t!r}")
            else:
                self._req("PUT", f"/pages/{p['url']}", {"wiki_page": {"published": False}})
                print(f"  retired  page        {t}")
            n += 1
        return n

    def retire_orphan_milestones(self, keep_names, group_id):
        """Unpublish milestone assignments and modules left behind by a rename.

        Renaming a milestone creates a new assignment and module; without this the old
        pair stays published and students see the milestone twice.
        """
        n = 0
        for a in self.get_all("/assignments"):
            if a.get("assignment_group_id") == group_id and a["name"] not in keep_names:
                if self.dry_run:
                    print(f"  [dry-run] would RETIRE assignment {a['name']!r}")
                else:
                    self._req("PUT", f"/assignments/{a['id']}",
                              {"assignment": {"published": False}})
                    print(f"  retired  assignment  {a['name']}")
                n += 1
        for m in self.get_all("/modules"):
            if re.match(r"^M\d+ — ", m["name"]) and m["name"] not in keep_names:
                if self.dry_run:
                    print(f"  [dry-run] would RETIRE module {m['name']!r}")
                else:
                    self._req("PUT", f"/modules/{m['id']}",
                              {"module": {"published": False}})
                    print(f"  retired  module      {m['name']}")
                n += 1
        return n


# ---------------------------------------------------------------- content assembly

def overview_markdown(skills, milestones, slugs, course):
    """Build the tracking table from the source files so it cannot drift."""
    by_ms = {}
    for _, meta, _ in skills:
        by_ms.setdefault(meta["milestone"], []).append(meta)

    out = [
        "There are **24 skills**, grouped into **6 milestones** of four skills each. "
        "You choose which skill to work on and when. Each skill is submitted as one of your "
        "ordinary weekly log entries — Reading (WR), Writing (WW), or Arithmetic (WA). "
        "**There is no extra weekly work.** The skill replaces that week's entry; it does not "
        "stack on top of it.",
        "",
        "When all four skills in a milestone are in, you submit the **milestone assignment**. "
        "That submission is an index, not new work: list which week each skill went in, and "
        "link the artifact. Graded complete / redo. One demonstration and the skill is yours "
        "permanently — it does not repeat in a later semester.",
        "",
        "**Click any skill name below for the full lesson** — why it exists, the external "
        "reading, the mechanic, and the exact checklist it is graded against.",
        "",
        "## Rules",
        "",
        "- **Everything is performed on your own dissertation work.** Not a sample repo, not a "
        "practice paper. Your actual thesis code, your actual draft, your actual data.",
        "- **The four skills in a milestone must be submitted in four different weeks.** You "
        "cannot bank them and dump them in week 14.",
        "- **Target two milestones per semester.** At that pace the full set takes three to "
        "four semesters.",
        "- **Where a skill is governed by the lab code standard, the lesson cites the Part and "
        "stops.** Go read the Part. The lesson will not summarise it for you, deliberately — a "
        "summary reads as complete and stops you looking. Standard: "
        "<https://github.com/sear-labs/code-standard>",
        "- **Order is a suggestion, not a gate.** Nothing is locked. If your research needs M5 "
        "in year one, take M5 in year one.",
        "",
        "---",
        "",
    ]

    for _, mmeta, _ in milestones:
        code = mmeta["milestone"]
        out += [
            f"## {code} — {mmeta['title']}",
            "",
            f"*{mmeta['tier']}*",
            "",
            "| Skill | Channel | Turn in as |",
            "|---|---|---|",
        ]
        for s in by_ms.get(code, []):
            link = f"{HOST}/courses/{course}/pages/{slugs[s['title']]}"
            out.append(f"| [{s['title']}]({link}) | {s['channel']} | {s['submit_as']} |")
        out.append("")
    out += [
        "---",
        "",
        "*The full handbook, including everything above, is public at "
        "<https://github.com/sear-labs/teaching-phd-skills>. Every artifact that passes goes "
        "into it, so the student after you starts from where you finished.*",
    ]
    return "\n".join(out)


def skill_header(meta, course, milestone_titles):
    code = meta.get("milestone", "?")
    return (
        f"*Milestone {code} — {milestone_titles.get(code, '')} &middot; "
        f"{meta.get('channel','?')} channel &middot; {meta.get('tier','?')} &middot; "
        f"{meta.get('time','?')}*\n\n"
        f"**Turn in as:** {meta.get('submit_as','see below')}\n\n"
        f"**Prerequisites:** {meta.get('prerequisites','none')}\n\n"
        f"[&larr; All skills and milestones]"
        f"({HOST}/courses/{course}/pages/research-competency-milestones)\n\n---\n\n"
    )


def milestone_links(mmeta, skills, slugs, course):
    """The clickable lesson list injected into each milestone assignment."""
    code = mmeta["milestone"]
    rows = ["", "## The lessons", "",
            "Each links to the full lesson, including the checklist it is graded against.", ""]
    for _, s, _ in skills:
        if s["milestone"] == code:
            link = f"{HOST}/courses/{course}/pages/{slugs[s['title']]}"
            rows.append(f"- [{s['title']}]({link}) — *{s['channel']}* — {s['submit_as']}")
    rows.append("")
    return "\n".join(rows)


# -------------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--course", required=True, help="Canvas course id")
    ap.add_argument("--dry-run", action="store_true", help="show what would change")
    ap.add_argument("--publish", action="store_true",
                    help="publish everything (visible to students)")
    args = ap.parse_args()

    skills = load("skills")
    milestones = load("milestones")
    milestone_titles = {m["milestone"]: m["title"] for _, m, _ in milestones}

    canvas = Canvas(get_token(), args.course, args.dry_run, args.publish)
    print(f"Course {args.course}"
          f"{'  [DRY RUN]' if args.dry_run else ''}"
          f"{'  [PUBLISHING]' if args.publish else '  [unpublished]'}")

    # 0. Retire first, publish second. Unpublishing a Canvas module cascades to the
    # pages it contains -- so a skill that moved between milestones gets knocked down
    # if retirement runs last. Doing it first means the publishing pass repairs it.
    group_id = canvas.ensure_group(MILESTONE_GROUP)
    keep_ms = {f"{m['milestone']} — {m['title']}" for _, m, _ in milestones}
    keep_sk = {f"Skill: {m['title']}" for _, m, _ in skills}
    print("\nRetiring superseded content:")
    retired = canvas.retire_orphan_milestones(keep_ms, group_id)
    retired += canvas.retire_orphan_skill_pages(keep_sk)
    retired += canvas.retire_pages_by_title(SUPERSEDED_PAGES)
    if not retired:
        print("  (nothing superseded)")

    # 1. Skill pages -- we need their real slugs to link everything else.
    print(f"\nSkill pages ({len(skills)}):")
    slugs = {}
    for _, meta, body in skills:
        title = meta["title"]
        html = md_to_html(skill_header(meta, args.course, milestone_titles) + body)
        slugs[title] = canvas.upsert_page(f"Skill: {title}", html)


    # 2. Overview page, plus the ungraded reading list.
    print("\nStandalone pages:")
    canvas.upsert_page(
        OVERVIEW_TITLE,
        md_to_html(overview_markdown(skills, milestones, slugs, args.course)))

    companions = []
    for stem, title in COMPANION_PAGES:
        f = REPO / "handbook" / f"{stem}.md"
        if not f.exists():
            continue
        body = f.read_text(encoding="utf-8")
        # Drop the leading H1 -- Canvas renders the page title itself.
        body = body.split("\n", 1)[1] if body.startswith("# ") else body
        companions.append((canvas.upsert_page(title, md_to_html(body)), title))

    # 3. Milestone assignments, with clickable lesson lists.
    print(f"\nMilestone assignments ({len(milestones)}):")
    assn_ids = {}
    for _, meta, body in milestones:
        name = f"{meta['milestone']} — {meta['title']}"
        md = body + milestone_links(meta, skills, slugs, args.course)
        assn_ids[meta["milestone"]] = canvas.upsert_assignment(name, md_to_html(md), group_id)

    # 4. Modules -- ungated filing cabinets, appended after the existing ones.
    print("\nModules:")
    base_pos = max([m["position"] for m in canvas.get_all("/modules")] or [0])
    start_items = [("Page", "research-competency-milestones", OVERVIEW_TITLE)]
    start_items += [("Page", slug, title) for slug, title in companions]
    canvas.upsert_module(
        "Competency Milestones — Start Here", base_pos + 1, start_items)
    for n, (_, meta, _) in enumerate(milestones, start=1):
        code = meta["milestone"]
        items = [("Page", slugs[s["title"]], f"Skill: {s['title']}")
                 for _, s, _ in skills if s["milestone"] == code]
        if assn_ids.get(code):
            items.append(("Assignment", assn_ids[code], f"{code} — {meta['title']}"))
        canvas.upsert_module(f"{code} — {meta['title']}", base_pos + 1 + n, items)


    if args.publish:
        print("\nPublished. Students can see all of it now.")
    else:
        print("\nUnpublished — students see none of this. Re-run with --publish when ready.")


if __name__ == "__main__":
    main()
