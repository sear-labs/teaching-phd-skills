#!/usr/bin/env python3
"""Remove the duplicated UTA template modules and pages from a Canvas course.

The course shell was imported more than once, leaving an exact duplicate set of
modules (Instructor Information / Getting Started / [TEMPLATE] Module 1) whose items
point at "-2"/"-3"/"-4" suffixed copies of every template page. Students currently see
two identical "Getting Started" modules.

Safe by default: prints a plan and changes nothing. Pass --delete to act.

Bodies of every page it would remove are already archived in
records/template-pages-backup.json -- re-run scripts/push_to_canvas.py's backup path,
or restore by POSTing those bodies back, if anything turns out to have been wanted.

Usage
-----
    python scripts/dedupe_canvas_templates.py --course 277913
    python scripts/dedupe_canvas_templates.py --course 277913 --delete
"""

import argparse
import json
import sys
import urllib.error
import urllib.request

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from push_to_canvas import get_token, HOST  # noqa: E402

# The duplicate module set. Verified 2026-09-15: same names, same item counts, and
# lower-numbered twins at 1445002 / 1445004 / 1445006 which are kept.
DUP_MODULE_IDS = [1482702, 1482703, 1482704]


def req(token, method, url):
    r = urllib.request.Request(url, method=method)
    r.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(r) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"  ! {method} {url.rsplit('/', 2)[-2:]} -> {e.code}")
        return None


def get_all(token, base, path):
    out, page = [], 1
    while True:
        batch = req(token, "GET", f"{base}{path}?per_page=100&page={page}")
        if not batch:
            return out
        out.extend(batch)
        if len(batch) < 100:
            return out
        page += 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", required=True)
    ap.add_argument("--delete", action="store_true", help="actually delete")
    args = ap.parse_args()

    token = get_token()
    base = f"{HOST}/api/v1/courses/{args.course}"

    pages = get_all(token, base, "/pages")
    dupes = [p for p in pages
             if p["url"].rstrip("234").endswith("-") and not p["url"].startswith("skill-")]
    # rstrip above is too loose; match the real suffix pattern instead
    import re
    dupes = [p for p in pages
             if re.search(r"-[234]$", p["url"]) and not p["url"].startswith("skill-")]

    mods = get_all(token, base, "/modules")
    to_del_mods = [m for m in mods if m["id"] in DUP_MODULE_IDS]

    print(f"Course {args.course}")
    print(f"  pages now:            {len(pages)}")
    print(f"  duplicate pages:      {len(dupes)}  ({sum(p['published'] for p in dupes)} published)")
    print(f"  duplicate modules:    {len(to_del_mods)}")
    for m in to_del_mods:
        print(f"      id={m['id']}  items={m['items_count']}  published={m['published']}  {m['name']}")
    print(f"  pages after cleanup:  {len(pages) - len(dupes)}")

    if not args.delete:
        print("\nDry run. Nothing changed. Re-run with --delete to apply.")
        return

    # Modules first: removing a module that points at a page avoids leaving a broken item
    # visible to students between the two loops.
    print("\nDeleting duplicate modules...")
    for m in to_del_mods:
        if req(token, "DELETE", f"{base}/modules/{m['id']}") is not None:
            print(f"  removed module {m['id']}  {m['name']}")

    print("\nDeleting duplicate pages...")
    n = 0
    for p in dupes:
        if req(token, "DELETE", f"{base}/pages/{p['url']}") is not None:
            n += 1
    print(f"  removed {n} pages")

    after = get_all(token, base, "/pages")
    print(f"\nPages now: {len(after)}")


if __name__ == "__main__":
    main()
