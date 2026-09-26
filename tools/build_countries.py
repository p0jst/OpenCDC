#!/usr/bin/env python3
"""Generate every copy of the national-annex data from one source.

docs/annexes/countries.json is the only place country facts are edited. This
script writes them into:

  - tools/regulatory-profile.html   the COUNTRIES object the selector renders from
  - docs/annexes/README.md          the status table between the countries markers
  - docs/annexes/annex-<iso>.md     the status line, review table and, except for
                                    Denmark, the NIS2 implementation table

Hand-written parts of each annex, such as the country notes, are left alone.

Run from the repository root:
    python tools/build_countries.py           rewrite the generated parts
    python tools/build_countries.py --check   exit 1 if anything is out of date
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "docs" / "annexes" / "countries.json"
SELECTOR = ROOT / "tools" / "regulatory-profile.html"
INDEX = ROOT / "docs" / "annexes" / "README.md"
ANNEX = ROOT / "docs" / "annexes" / "annex-{}.md"

BEGIN, END = "<!-- countries:begin -->", "<!-- countries:end -->"
DEFAULT_DISCLAIMER = (
    "Community-maintained orientation. This is **not legal advice**; verify against "
    "the official gazette and authority guidance before relying on it. Corrections "
    "welcome, see [contributing](../../CONTRIBUTING.md)."
)


def selector_data(countries):
    out = {}
    for iso, c in countries.items():
        e = {"n": c["name"], "status": c["status"], "law": c["law"],
             "auth": c["authority"], "csirt": c["csirt"], "link": c["link"]}
        for k in ("note", "acts", "reporting", "hooks"):
            if k in c:
                e[k] = c[k]
        out[iso] = e
    return out


def short(month_year):
    month, year = month_year.split()
    return month[:3] + " " + year


def index_table(countries):
    rows = ["| Country | Status | Confidence | Last reviewed | Second reviewer | Next review | Annex |",
            "|---------|--------|------------|---------------|-----------------|-------------|-------|"]
    for iso, c in countries.items():
        rows.append("| {} | {} | {} | {} | {} | {} | [Open](annex-{}.md) |".format(
            c["name"], c["status"], c["confidence"], short(c["last_reviewed"]),
            c["second_reviewer"], short(c["next_review"]), iso))
    return "\n".join(rows)


def annex_block(iso, c):
    second = "**Wanted**, see [CONTRIBUTING](../../CONTRIBUTING.md)" \
        if c["second_reviewer"] == "Wanted" else c["second_reviewer"]
    lines = [
        "> **Status as of {}:** {}. {}".format(c["last_reviewed"], c["status"],
                                              c.get("disclaimer", DEFAULT_DISCLAIMER)),
        "",
        "| Review | Status |",
        "|--------|--------|",
        "| Confidence | [{}](README.md#confidence-levels) |".format(c["confidence"]),
        "| Checked line by line against the legal text | {} |".format(c["checked_against_legal_text"]),
        "| Reviewed by a lawyer | {} |".format(c["lawyer_reviewed"]),
        "| Last reviewed | {} |".format(c["last_reviewed"]),
        "| Reviewed by | {} |".format(c["reviewed_by"]),
        "| Second reviewer | {} |".format(second),
        "| Next review due | {} |".format(c["next_review"]),
    ]
    if iso != "dk":
        lines += [
            "",
            "## NIS2 implementation",
            "",
            "| Field | Value |",
            "|-------|-------|",
            "| Implementing law | {} |".format(c["law"]),
            "| Competent authority | {} |".format(c["authority"]),
            "| National CSIRT / reporting | {} |".format(c["csirt"]),
            "| Official starting point | {} |".format(c["link"]),
        ]
    return "\n".join(lines)


def replace_block(text, block, path):
    pattern = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.S)
    if not pattern.search(text):
        raise SystemExit("missing countries markers in " + str(path))
    return pattern.sub(lambda _: BEGIN + "\n" + block + "\n" + END, text, count=1)


def main():
    check = "--check" in sys.argv
    countries = json.loads(DATA.read_text(encoding="utf-8"))
    targets = {}

    html = SELECTOR.read_text(encoding="utf-8")
    data = json.dumps(selector_data(countries), ensure_ascii=False, indent=1)
    new_html, n = re.subn(r"const COUNTRIES = \{.*?\};\n",
                          lambda _: "const COUNTRIES = " + data + ";\n", html, count=1, flags=re.S)
    if n != 1:
        raise SystemExit("COUNTRIES object not found in " + str(SELECTOR))
    targets[SELECTOR] = (html, new_html)

    idx = INDEX.read_text(encoding="utf-8")
    targets[INDEX] = (idx, replace_block(idx, index_table(countries), INDEX))

    for iso, c in countries.items():
        p = Path(str(ANNEX).format(iso))
        t = p.read_text(encoding="utf-8")
        targets[p] = (t, replace_block(t, annex_block(iso, c), p))

    stale = [p for p, (old, new) in targets.items() if old != new]
    if check:
        for p in stale:
            print("out of date:", p.relative_to(ROOT))
        if stale:
            print("run: python tools/build_countries.py")
            sys.exit(1)
        print("country data in sync")
        return
    for p in stale:
        p.write_text(targets[p][1], encoding="utf-8")
    print("updated {} file(s)".format(len(stale)))


if __name__ == "__main__":
    main()
