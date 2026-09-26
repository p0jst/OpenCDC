#!/usr/bin/env python3
"""Check that the framework's duplicated data has not drifted apart.

Some content necessarily exists in more than one file, because the browser tools
must work as single files without a server. This script fails the site build if
any copy differs from its source:

  1. Maturity criteria: assessments/maturity-self-assessment.md is the source;
     tools/maturity-assessment.html must carry the same criteria, in the same
     order, with the same NIS2 references.
  2. Skill catalogue: tools/skill-matrix.html must list exactly the skills, IDs
     and names of templates/skill-self-assessment.csv and .xlsx.
  3. Country data: docs/annexes/countries.json is the source; the selector,
     the annex index and the annexes must match (tools/build_countries.py --check).
  4. Capability IDs: every GV-1 style ID used in the documents exists in the
     capability index.

Run from the repository root:  python tools/check_consistency.py
"""
import csv
import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []


def criteria_from_checklist():
    text = (ROOT / "assessments" / "maturity-self-assessment.md").read_text(encoding="utf-8")
    out = {}
    for block in re.split(r"^## ", text, flags=re.M)[1:]:
        fid = block.split("\n", 1)[0].strip()
        if fid not in ("GOVERN", "IDENTIFY", "PROTECT", "DETECT", "RESPOND", "RECOVER"):
            continue
        levels = {}
        parts = re.split(r"^\*\*Level (\d)\*\*\s*$", block, flags=re.M)
        for i in range(1, len(parts), 2):
            items = re.findall(r"^- \[ \] (.*?)(?: · \*NIS2 ([^*]+)\*)? — status:", parts[i + 1], re.M)
            levels[parts[i]] = [(t.strip(), r.strip()) for t, r in items]
        out[fid] = levels
    return out


def check_criteria():
    html = (ROOT / "tools" / "maturity-assessment.html").read_text(encoding="utf-8")
    m = re.search(r"const CATALOG = (\{.*?\})\s*\n;", html, re.S)
    if not m:
        errors.append("maturity tool: CATALOG not found")
        return
    tool = {f["id"]: f for f in json.loads(m.group(1))["functions"]}
    md = criteria_from_checklist()
    for fid, levels in md.items():
        f = tool.get(fid)
        if not f:
            errors.append(f"maturity tool: function {fid} missing")
            continue
        for lvl, items in levels.items():
            texts = [t for t, _ in items]
            refs = [r for _, r in items]
            if f["levels"].get(lvl, []) != texts:
                errors.append(f"maturity criteria differ: {fid} level {lvl}")
            if f.get("nis2", {}).get(lvl, [""] * len(refs)) != refs:
                errors.append(f"maturity NIS2 references differ: {fid} level {lvl}")


def check_skills():
    html = (ROOT / "tools" / "skill-matrix.html").read_text(encoding="utf-8")
    tool = re.findall(r'\{"id":"([A-Z]{2}-\d\d)","domain":"[A-Z &]+","name":"([^"]+)"', html)
    rows = csv.reader((ROOT / "templates" / "skill-self-assessment.csv").open(encoding="utf-8-sig"))
    sheet = [(r[0], r[2]) for r in rows if r and re.fullmatch(r"[A-Z]{2}-\d\d", r[0])]
    if tool != sheet:
        errors.append(f"skill catalogue: tool has {len(tool)} skills, CSV has {len(sheet)}, or IDs and names differ")
    with zipfile.ZipFile(ROOT / "templates" / "skill-self-assessment.xlsx") as z:
        shared = z.read("xl/sharedStrings.xml").decode("utf-8") if "xl/sharedStrings.xml" in z.namelist() else ""
        sheets = "".join(z.read(n).decode("utf-8") for n in z.namelist() if n.startswith("xl/worksheets/"))
    xlsx_ids = set(re.findall(r">([A-Z]{2}-\d\d)<", shared + sheets))
    if xlsx_ids != {i for i, _ in sheet}:
        errors.append("skill catalogue: XLSX skill IDs differ from the CSV")


def check_countries():
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "build_countries.py"), "--check"],
                       capture_output=True, text=True)
    if r.returncode:
        errors.append("country data out of date:\n" + r.stdout.strip())


def check_capability_ids():
    index = (ROOT / "docs" / "capability-index.md").read_text(encoding="utf-8")
    known = set(re.findall(r"\*\*((?:GV|ID|PR|DE|RS|RC)-\d)\*\*", index))
    for p in list((ROOT / "docs").glob("*.md")) + list((ROOT / "assessments").glob("*.md")) \
            + list((ROOT / "templates").glob("*.md")) + list((ROOT / "playbooks").glob("*.md")):
        for cid in set(re.findall(r"(?<![\w-])((?:GV|ID|PR|DE|RS|RC)-\d)(?![\d-])", p.read_text(encoding="utf-8"))):
            if cid not in known:
                errors.append(f"unknown capability ID {cid} in {p.relative_to(ROOT)}")


def main():
    check_criteria()
    check_skills()
    check_countries()
    check_capability_ids()
    if errors:
        print("consistency check failed:")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    print("consistency check passed")


if __name__ == "__main__":
    main()
