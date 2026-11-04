#!/usr/bin/env python3
"""Assemble the MkDocs source tree (_site_src/) from the repository content.

The repo keeps its natural layout (docs/, templates/, tools/, ...); MkDocs wants
one docs_dir. This script stages the content, preserving repo-relative paths so
every internal link keeps working, and adds the website-only landing page and CSS.

Run from the repository root:  python site/build_site.py
Then:                          mkdocs build
"""
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_site_src"

COPY_DIRS = ["docs", "assessments", "templates", "tools"]
COPY_FILES = ["ABOUT.md", "CONTRIBUTING.md", "CHANGELOG.md", "LICENSE"]

# The self-assessment checklist is one file with two readers. In the repository
# it is a form to copy and fill in offline; on the website the interactive tool
# does that, so the page only lists the criteria. Blocks marked offline-only
# are dropped on the website, blocks marked web-only are shown only there, and
# the tick boxes, status and evidence placeholders and score lines are removed.
CHECKLIST = "assessments/maturity-self-assessment.md"


def web_checklist(text):
    text = re.sub(r"<!-- offline-only:begin -->.*?<!-- offline-only:end -->\n?", "", text, flags=re.S)
    text = re.sub(r"<!-- web-only:begin\n(.*?)\nweb-only:end -->", r"\1", text, flags=re.S)
    text = re.sub(r"^- \[ \] (.*?) — status: `…` — evidence: …$", r"- \1", text, flags=re.M)
    text = re.sub(r"^\*\*Function score:.*\n\n?", "", text, flags=re.M)
    leftover = [m for m in ("- [ ]", "status: `", "☐", "offline-only", "web-only") if m in text]
    if leftover:
        raise SystemExit(f"{CHECKLIST}: website version still contains {leftover}")
    return text


def main():
    if SRC.exists():
        shutil.rmtree(SRC)
    SRC.mkdir()
    for d in COPY_DIRS:
        shutil.copytree(ROOT / d, SRC / d, ignore=shutil.ignore_patterns(".DS_Store"))
    for f in COPY_FILES:
        p = ROOT / f
        if p.exists():
            shutil.copy2(p, SRC / f)
    checklist = SRC / CHECKLIST
    checklist.write_text(web_checklist(checklist.read_text(encoding="utf-8")), encoding="utf-8")
    # website-only files
    shutil.copy2(ROOT / "site" / "index.md", SRC / "index.md")
    (SRC / "assets").mkdir()
    shutil.copy2(ROOT / "site" / "extra.css", SRC / "assets" / "extra.css")
    # Everything in assets/ — the self-hosted IBM Plex files and the social
    # preview card. Fonts are staged here (rather than under site/) so that the
    # same relative path (../assets/fonts/) resolves both on the website and
    # when a tool in tools/ is opened straight from a clone of the repository.
    shutil.copytree(ROOT / "assets", SRC / "assets", dirs_exist_ok=True)
    # Custom domain: GitHub Pages (Actions source) needs a CNAME file inside the
    # published artifact on every deploy — it does not persist this on its own.
    cname = ROOT / "site" / "CNAME"
    if cname.exists():
        shutil.copy2(cname, SRC / "CNAME")
    n = sum(1 for _ in SRC.rglob("*") if _.is_file())
    print(f"staged {n} files into {SRC.relative_to(ROOT)}/")

if __name__ == "__main__":
    main()
