#!/usr/bin/env python3
"""Aggregate maturity-assessment contributions into tools/benchmark.json.

Raw contributions stay private: keep them in benchmark/submissions/ (git-ignored)
and publish only the output of this script. Groups smaller than MIN_GROUP are
left out entirely, so no published figure describes fewer than MIN_GROUP
organisations.

Run from the repository root:
    python benchmark/aggregate.py                 # reads benchmark/submissions/*.json
    python benchmark/aggregate.py path/to/folder  # or another folder
"""
import json
import re
import statistics
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOL = ROOT / "tools" / "maturity-assessment.html"
OUT = ROOT / "tools" / "benchmark.json"
MIN_GROUP = 10
# Criteria set 2 arrived with the NIS2 legal floor at Level 2; set-1 statuses mean different criteria.
CRITERIA_SET = 2

SIZES = ["1-49", "50-249", "250-999", "1000-4999", "5000+"]
NIS2 = ["essential", "important", "not-in-scope", "unsure"]
REGIONS = ["Nordics", "Western Europe", "Central and Eastern Europe", "Southern Europe", "Outside the EU"]
MODELS = ["A", "B", "C", "hybrid", "D", "none"]
SECTORS = ["Energy", "Transport", "Finance and insurance", "Health", "Water and waste", "Digital infrastructure and ICT services",
           "Public administration", "Manufacturing", "Postal and courier", "Food", "Research and education", "Other"]


def load_catalog():
    """Read the criteria straight from the tool, so the two cannot drift apart."""
    html = TOOL.read_text(encoding="utf-8")
    m = re.search(r"const CATALOG = (\{.*?\})\s*\n;", html, re.S)
    if not m:
        sys.exit("could not find CATALOG in " + str(TOOL))
    return json.loads(m.group(1))["functions"]


def criteria_order(funcs):
    """Same order as critList() in the tool: function, then level 2, 3, 4."""
    out = []
    for f in funcs:
        for lvl in ("2", "3", "4"):
            for i, _ in enumerate(f["levels"].get(lvl, [])):
                out.append((f["id"], int(lvl), i))
    return out


def level(funcs, order, statuses, fid, strict):
    """Staged scoring, exactly as in the tool."""
    met = lambda s: s == 4 if strict else s >= 3
    by_key = {k: statuses[i] for i, k in enumerate(order)}
    f = next(x for x in funcs if x["id"] == fid)
    score = 1
    for lvl in (2, 3, 4):
        items = f["levels"].get(str(lvl), [])
        if items and all(met(by_key[(fid, lvl, i)]) for i in range(len(items))):
            score = lvl
        else:
            break
    return score


def validate(c, n_criteria):
    if c.get("ocdf_benchmark") != 1:
        return "not an OCDF benchmark contribution"
    if c.get("criteria_set", 1) != CRITERIA_SET:
        return f"made against criteria set {c.get('criteria_set', 1)}; only set {CRITERIA_SET} is aggregated, so ask the contributor to re-score"
    s = c.get("statuses", "")
    if len(s) != n_criteria or not re.fullmatch(r"[0-4]+", s):
        return f"statuses must be {n_criteria} digits 0-4"
    for field, allowed in (("size", SIZES), ("nis2", NIS2), ("region", REGIONS), ("model", MODELS), ("sector", SECTORS)):
        if c.get(field) not in allowed:
            return f"{field} must be one of {allowed}"
    return None


def summarise(funcs, order, group):
    levels = {}
    for f in funcs:
        vals = [level(funcs, order, [int(x) for x in c["statuses"]], f["id"], c.get("evidence_based", False)) for c in group]
        levels[f["id"]] = {
            "median": statistics.median(vals),
            "distribution": [vals.count(l) for l in (1, 2, 3, 4)],
        }
    n = len(group)
    in_place = [round(100 * sum(1 for c in group if int(c["statuses"][i]) >= 3) / n) for i in range(len(order))]
    evidenced = [round(100 * sum(1 for c in group if int(c["statuses"][i]) == 4) / n) for i in range(len(order))]
    return {"n": n, "levels": levels, "in_place_pct": in_place, "evidenced_pct": evidenced}


def main():
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "benchmark" / "submissions"
    funcs = load_catalog()
    order = criteria_order(funcs)
    good, rejected = [], []
    for p in sorted(folder.glob("*.json")) if folder.exists() else []:
        try:
            c = json.loads(p.read_text(encoding="utf-8"))
        except ValueError as e:
            rejected.append((p.name, f"not valid JSON: {e}"))
            continue
        err = validate(c, len(order))
        (rejected.append((p.name, err)) if err else good.append(c))

    groups = []
    candidates = [("all", "all", good)]
    candidates += [("size", s, [c for c in good if c["size"] == s]) for s in SIZES]
    candidates += [("nis2", k, [c for c in good if c["nis2"] == k]) for k in NIS2]
    candidates += [("region", r, [c for c in good if c["region"] == r]) for r in REGIONS]
    for by, key, members in candidates:
        if len(members) >= MIN_GROUP:
            groups.append({"by": by, "key": key, **summarise(funcs, order, members)})

    out = {
        "generated": date.today().isoformat(),
        "min_group": MIN_GROUP,
        "contributions": len(good),
        # counts per group, so the tool can say "n = 3 so far" without
        # publishing any figure about a group below the threshold
        "counts": {
            "size": {s: sum(1 for c in good if c["size"] == s) for s in SIZES},
            "nis2": {k: sum(1 for c in good if c["nis2"] == k) for k in NIS2},
            "region": {r: sum(1 for c in good if c["region"] == r) for r in REGIONS},
        },
        "groups": groups,
    }
    OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(f"{len(good)} contributions used, {len(rejected)} rejected, {len(groups)} groups published -> {OUT.relative_to(ROOT)}")
    for name, why in rejected:
        print(f"  rejected {name}: {why}")


if __name__ == "__main__":
    main()
