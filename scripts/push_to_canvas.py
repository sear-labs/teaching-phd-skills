#!/usr/bin/env python3
"""Push skill pages and milestone assignments from this repo into a Canvas course.

The repo is the source of truth. Canvas is a delivery copy. Edit the Markdown here,
re-run this, and Canvas catches up. Never edit a generated page in Canvas directly --
the next run will overwrite it.

Idempotent: matches existing Canvas objects by title and updates them in place, so
re-running does not create duplicates.

Everything is created UNPUBLISHED. Publishing is a human decision, made in Canvas.

Usage
-----
    python scripts/push_to_canvas.py --course 277913 --dry-run
    python scripts/push_to_canvas.py --course 277913
    python scripts/push_to_canvas.py --course 277913 --only skills

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
import urllib.parse
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HOST = "https://uta.instructure.com"
MILESTONE_GROUP = "Competency Milestones"
MILESTONE_POINTS = 5


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
    """Markdown -> HTML via pandoc. GFM in, Canvas-safe HTML out."""
    try:
        out = subprocess.run(
            ["pandoc", "--from=gfm", "--to=html", "--wrap=none"],
            input=md, capture_output=True, text=True, encoding="utf-8", check=True,
        )
    except FileNotFoundError:
        sys.exit("pandoc not found on PATH. winget install JohnMacFarlane.Pandoc")
    except subprocess.CalledProcessError as e:
        sys.exit(f"pandoc failed: {e.stderr}")
    # Canvas renders unchecked task-list items as literal brackets; make them checkboxes.
    return out.stdout.replace("[ ]", "&#9744;")


# --------------------------------------------------------------------------- api

class Canvas:
    def __init__(self, token, course, dry_run=False):
        self.token = token
        self.course = course
        self.dry_run = dry_run

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
        existing = {p["title"]: p for p in self.get_all("/pages")}
        payload = {"wiki_page": {
            "title": title, "body": body,
            "published": False, "editing_roles": "teachers",
        }}
        if title in existing:
            if self.dry_run:
                print(f"  [dry-run] would UPDATE page {title!r}")
                return
            r = self._req("PUT", f"/pages/{existing[title]['url']}", payload)
            print(f"  updated page  {title}")
        else:
            if self.dry_run:
                print(f"  [dry-run] would CREATE page {title!r}")
                return
            r = self._req("POST", "/pages", payload)
            print(f"  created page  {title}  ->  {HOST}/courses/{self.course}/pages/{r['url']}")

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
            "published": False,
            # No due date: milestones are self-paced by design.
        }}
        if name in existing:
            if self.dry_run:
                print(f"  [dry-run] would UPDATE assignment {name!r}")
                return
            self._req("PUT", f"/assignments/{existing[name]['id']}", payload)
            print(f"  updated assn  {name}")
        else:
            if self.dry_run:
                print(f"  [dry-run] would CREATE assignment {name!r}")
                return
            a = self._req("POST", "/assignments", payload)
            print(f"  created assn  {name}  ->  {HOST}/courses/{self.course}/assignments/{a['id']}")


# -------------------------------------------------------------------------- main

def push_skills(canvas):
    files = sorted((REPO / "skills").glob("*.md"))
    print(f"\nSkills ({len(files)}):")
    for f in files:
        meta, body = parse_front_matter(f.read_text(encoding="utf-8"))
        title = meta.get("title", f.stem)
        header = (
            f"*Milestone {meta.get('milestone','?')} &middot; "
            f"{meta.get('channel','?')} channel &middot; {meta.get('tier','?')} &middot; "
            f"{meta.get('time','?')}*\n\n"
            f"**Turn in as:** {meta.get('submit_as','see below')}\n\n"
            f"**Prerequisites:** {meta.get('prerequisites','none')}\n\n---\n\n"
        )
        canvas.upsert_page(f"Skill: {title}", md_to_html(header + body))


def push_milestones(canvas):
    group_id = canvas.ensure_group(MILESTONE_GROUP)
    files = sorted((REPO / "milestones").glob("*.md"))
    print(f"\nMilestones ({len(files)}):")
    for f in files:
        meta, body = parse_front_matter(f.read_text(encoding="utf-8"))
        name = f"{meta.get('milestone','M?')} — {meta.get('title', f.stem)}"
        canvas.upsert_assignment(name, md_to_html(body), group_id)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--course", required=True, help="Canvas course id")
    ap.add_argument("--dry-run", action="store_true", help="show what would change")
    ap.add_argument("--only", choices=["skills", "milestones"], help="push just one kind")
    args = ap.parse_args()

    canvas = Canvas(get_token(), args.course, args.dry_run)
    print(f"Course {args.course}{'  [DRY RUN]' if args.dry_run else ''}")
    if args.only != "milestones":
        push_skills(canvas)
    if args.only != "skills":
        push_milestones(canvas)
    print("\nEverything created unpublished. Publish from Canvas when you have read it.")


if __name__ == "__main__":
    main()
