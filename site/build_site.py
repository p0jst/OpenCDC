#!/usr/bin/env python3
"""Assemble the MkDocs source tree (_site_src/) from the repository content.

The repo keeps its natural layout (docs/, templates/, tools/, ...); MkDocs wants
one docs_dir. This script stages the content, preserving repo-relative paths so
every internal link keeps working, and adds the website-only landing page and CSS.

Run from the repository root:  python site/build_site.py
Then:                          mkdocs build
"""
import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_site_src"

COPY_DIRS = ["docs", "assessments", "templates", "tools"]
COPY_FILES = ["ABOUT.md", "CONTRIBUTING.md", "CHANGELOG.md", "SECURITY.md", "LICENSE"]

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


# The other checklists and templates keep their tick boxes in the repository,
# where they are copied and filled in. On the website a box cannot be ticked,
# so it looks broken: list items lose the box, empty box cells in tables are
# left blank to fill in, and an inline row of choices reads as a list.
def web_tickboxes(text):
    text = re.sub(r"^(\s*)- \[ \] ", r"\1- ", text, flags=re.M)
    text = text.replace("☑ typically", "Typically")
    def choices(m):
        items = [s.strip() for s in m.group(2).split("☐") if s.strip()]
        return m.group(1) + "one or more of " + ", ".join(items[:-1]) + " or " + items[-1]
    text = re.sub(r"^(.*?:\*\* )((?:☐ [^☐\n|]+){2,})$", choices, text, flags=re.M)
    text = re.sub(r"\| ☐ (?=\|)", "|  ", text)
    return text


def web_pages():
    for page in SRC.rglob("*.md"):
        if page.relative_to(SRC).as_posix() == CHECKLIST:
            continue
        text = page.read_text(encoding="utf-8")
        new = web_tickboxes(text)
        if new != text:
            page.write_text(new, encoding="utf-8")
        leftover = [m for m in ("- [ ]", "☐", "☑") if m in new]
        if leftover:
            raise SystemExit(f"{page.relative_to(SRC)}: website version still contains {leftover}")


# The build path: seven pages that each do one step. On the website each gets a
# line under its title saying which step it is, and a block at the end that
# sends the reader to the next step, so the footer's previous/next links (which
# follow the menu) are not the only way on. Added here rather than in the files,
# because the templates are also downloaded and filled in, and a navigation
# note does not belong in someone's charter.
BUILD_PATH = "docs/build-path.md"
STEPS = [
    ("docs/tiers.md", "Choose your tier"),
    ("assessments/cdc-design-navigator.md", "Run the design workshops"),
    ("templates/cdc-charter-template.md", "Adopt the charter"),
    ("docs/operating-models.md", "Decide the operating model"),
    ("docs/start-here.md", "Work the first 90 days"),
    ("assessments/maturity-self-assessment.md", "Assess where you are"),
    ("templates/annual-calendar-template.md", "Set the operating rhythm"),
]


def rel(src, dst):
    return os.path.relpath(dst, os.path.dirname(src)).replace(os.sep, "/")


def add_step_banners():
    total = len(STEPS)
    for i, (page, title) in enumerate(STEPS, start=1):
        path = SRC / page
        text = path.read_text(encoding="utf-8")
        anchor = f"step-{i}-" + re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        path_link = rel(page, BUILD_PATH)
        top = (f'<p class="opencdc-step" markdown>Build path · step {i} of {total} · '
               f'[See all steps]({path_link}#{anchor})</p>\n')
        if i < total:
            nxt_page, nxt_title = STEPS[i]
            end = (f'<div class="opencdc-step-next" markdown>\n'
                   f'<span>Done with step {i}?</span> '
                   f'[Next: step {i + 1}, {nxt_title} →]({rel(page, nxt_page)})'
                   f' · [Back to the build path]({path_link})\n</div>\n')
        else:
            end = (f'<div class="opencdc-step-next" markdown>\n'
                   f'<span>That was the last step.</span> '
                   f'[What comes after the build path →]({path_link}#after-the-build-path)\n</div>\n')
        lines = text.split("\n")
        h1 = next(n for n, l in enumerate(lines) if l.startswith("# "))
        lines.insert(h1 + 1, "\n" + top)
        text = "\n".join(lines)
        foot = re.search(r"\n(---\n+)?\*(Template from the )?OpenCDC, licensed CC BY 4\.0[^\n]*\*\s*$", text)
        if foot:
            text = text[:foot.start()] + "\n\n" + end + text[foot.start():]
        else:
            text = text.rstrip() + "\n\n" + end
        # The theme's previous/next links follow the menu, not the build path,
        # so on a step page they would point somewhere else than the step box.
        assert not text.startswith("---"), f"{page}: unexpected front matter"
        text = "---\nhide:\n  - footer\n---\n\n" + text
        path.write_text(text, encoding="utf-8")


def main():
    if SRC.exists():
        shutil.rmtree(SRC)
    SRC.mkdir()
    for d in COPY_DIRS:
        shutil.copytree(ROOT / d, SRC / d, ignore=shutil.ignore_patterns(".DS_Store", "*.py", "__pycache__"))
    for f in COPY_FILES:
        p = ROOT / f
        if p.exists():
            shutil.copy2(p, SRC / f)
    checklist = SRC / CHECKLIST
    checklist.write_text(web_checklist(checklist.read_text(encoding="utf-8")), encoding="utf-8")
    web_pages()
    add_step_banners()
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
    # security.txt, RFC 9116. MkDocs skips dot-directories unless mkdocs.yml
    # re-includes them, which exclude_docs does for /.well-known/.
    wk = ROOT / "site" / ".well-known"
    if wk.exists():
        shutil.copytree(wk, SRC / ".well-known")
    n = sum(1 for _ in SRC.rglob("*") if _.is_file())
    print(f"staged {n} files into {SRC.relative_to(ROOT)}/")

if __name__ == "__main__":
    main()
