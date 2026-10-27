#!/usr/bin/env python3
"""Generate the framework's diagrams as SVG files, one light and one dark copy each.

The diagrams are code so that they stay editable, reviewable in a diff and
consistent in style. Each one is written twice, for light and dark mode, and the
documents embed both with the #gh-light-mode-only / #gh-dark-mode-only
fragments, which GitHub and the website both honour.

The SVGs use no web fonts and no scripts, so they render the same as an <img>
on GitHub, on opencdc.org and in a local clone.

Run from the repository root:  python tools/build_diagrams.py
Output:                         assets/diagrams/<name>-light.svg and -dark.svg
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "diagrams"

FONT = "'IBM Plex Sans', -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"

THEMES = {
    "light": {
        "ink": "#1d2733", "soft": "#5d6975", "line": "#d9d3c4", "card": "#ffffff",
        "eu": "#123a6d", "eu_soft": "#e8eef7", "on_eu": "#ffffff",
        "accent": "#8a1f2d", "accent_soft": "#f6e7e9",
        "warn": "#6b4e16", "warn_soft": "#f5ead3",
        "fn": {"GOVERN": "#123a6d", "IDENTIFY": "#0e6e73", "PROTECT": "#2a6a4f",
               "DETECT": "#6b4e16", "RESPOND": "#8a1f2d", "RECOVER": "#5b3a8f"},
    },
    "dark": {
        "ink": "#e6edf3", "soft": "#9aa7b4", "line": "#3a4a5b", "card": "#1a242f",
        "eu": "#8fb3e3", "eu_soft": "#26354a", "on_eu": "#0d1720",
        "accent": "#e39aa4", "accent_soft": "#3a2329",
        "warn": "#e2c07e", "warn_soft": "#3a3020",
        "fn": {"GOVERN": "#6f9bd6", "IDENTIFY": "#6cc7cc", "PROTECT": "#8fd1b3",
               "DETECT": "#e2c07e", "RESPOND": "#e39aa4", "RECOVER": "#b9a1e0"},
    },
}


class Svg:
    def __init__(self, w, h, title, desc, t):
        self.w, self.h, self.t = w, h, t
        self.parts = []
        self.head = (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-labelledby="title desc" font-family="{FONT}">\n'
            f'<title id="title">{escape(title)}</title>\n<desc id="desc">{escape(desc)}</desc>\n'
            f'<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{t["soft"]}"/></marker>'
            f'<marker id="arr-eu" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{t["eu"]}"/></marker></defs>\n'
        )

    def add(self, s):
        self.parts.append(s)

    def rect(self, x, y, w, h, fill, stroke=None, rx=6, dash=None, sw=1.5):
        st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{st}{da}/>')

    def text(self, x, y, s, size=13, fill=None, weight=400, anchor="start", italic=False):
        fill = fill or self.t["ink"]
        it = ' font-style="italic"' if italic else ""
        self.add(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
                 f'text-anchor="{anchor}"{it}>{escape(s)}</text>')

    def path(self, d, stroke=None, sw=1.6, dash=None, marker="arr", fill="none"):
        stroke = stroke or self.t["soft"]
        da = f' stroke-dasharray="{dash}"' if dash else ""
        mk = f' marker-end="url(#{marker})"' if marker else ""
        self.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{da}{mk}/>')

    def box(self, x, y, w, h, title, sub=None, kind="card"):
        t = self.t
        if kind == "eu":
            self.rect(x, y, w, h, t["eu"])
            tc, sc = t["on_eu"], t["on_eu"]
        elif kind == "gate":
            self.rect(x, y, w, h, t["accent_soft"], t["accent"], sw=2)
            tc, sc = t["ink"], t["soft"]
        elif kind == "soft":
            self.rect(x, y, w, h, t["eu_soft"], t["eu"])
            tc, sc = t["ink"], t["soft"]
        else:
            self.rect(x, y, w, h, t["card"], t["line"])
            tc, sc = t["ink"], t["soft"]
        cx = x + w / 2
        if sub:
            self.text(cx, y + h / 2 - 3, title, 14, tc, 600, "middle")
            self.text(cx, y + h / 2 + 15, sub, 12, sc, 400, "middle")
        else:
            self.text(cx, y + h / 2 + 5, title, 14, tc, 600, "middle")

    def render(self):
        return self.head + "\n".join(self.parts) + "\n</svg>\n"


# ---------------------------------------------------------------- incident flow
# All diagrams are drawn on a 760-unit-wide canvas, close to the website's text
# column, so that 12-15 unit text stays readable when the image is scaled down.
def incident_flow(t):
    s = Svg(760, 640, "How an incident moves",
            "Prepare, then detect, then a verify-and-triage gate with three outcomes: continue, stop or defer. "
            "Continue enters the response loop of scope, contain, eradicate and recover, repeated until no new "
            "evidence appears. Leaving the loop is a written, named decision, followed by a debrief whose lessons "
            "feed back into preparation. Legal clocks run from awareness, not from declaration.", t)
    s.box(20, 40, 190, 64, "Prepare", "plan, playbooks, authority")
    s.box(250, 40, 190, 64, "Detect", "alert, hunt or report")
    s.box(480, 40, 260, 64, "Verify and triage", "is it an incident?", kind="gate")
    s.text(610, 28, "Legal clocks run from awareness", 13, t["accent"], 600, "middle")
    s.path("M210,72 L248,72")
    s.path("M440,72 L478,72")

    # stop and defer
    s.box(505, 150, 110, 56, "Stop", "reason recorded")
    s.box(630, 150, 110, 56, "Defer", "time-boxed")
    s.path("M560,104 L560,148")
    s.path("M660,104 L660,148")
    s.path("M715,150 L715,106", dash="4 4")

    # response loop
    import math
    cx, cy, r = 290, 355, 125
    s.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{t["eu"]}" stroke-width="2"/>')
    for ang in (45, 135, 225, 315):
        a = math.radians(ang)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        dx, dy = -math.sin(a), math.cos(a)
        s.path(f"M{x - dx * 8:.1f},{y - dy * 8:.1f} L{x + dx * 2:.1f},{y + dy * 2:.1f}",
               stroke=t["eu"], sw=2, marker="arr-eu")
    s.text(cx, cy - 12, "Response loop", 16, t["eu"], 600, "middle")
    s.text(cx, cy + 8, "until no new", 13, t["soft"], 400, "middle")
    s.text(cx, cy + 26, "evidence appears", 13, t["soft"], 400, "middle")
    s.box(cx - 54, cy - r - 20, 108, 40, "Scope", kind="soft")
    s.box(cx + r - 54, cy - 20, 108, 40, "Contain", kind="soft")
    s.box(cx - 54, cy + r - 20, 108, 40, "Eradicate", kind="soft")
    s.box(cx - r - 54, cy - 20, 108, 40, "Recover", kind="soft")
    s.path(f"M490,104 L490,{cy - r} L{cx + 56},{cy - r}", stroke=t["eu"], marker="arr-eu")
    s.text(482, 150, "Continue", 13, t["eu"], 600, "end")

    # triggers
    s.rect(492, 270, 248, 168, t["card"], t["line"])
    s.text(506, 296, "Start another pass when", 14, t["ink"], 600)
    for i, line in enumerate(["a new indicator of compromise",
                              "a known indicator out of scope",
                              "eradication fails, reinfection",
                              "the compromise started earlier",
                              "an authority or insurer asks"]):
        y = 322 + i * 24
        s.add(f'<circle cx="511" cy="{y - 4}" r="3" fill="{t["eu"]}"/>')
        s.text(522, y, line, 13, t["ink"])

    # exit and debrief
    s.path(f"M{cx - r},{cy + 20} L{cx - r},528")
    s.box(70, 530, 190, 58, "Exit decision", "written and named")
    s.box(330, 530, 240, 58, "Debrief", "root cause, actions, reports", kind="eu")
    s.path("M260,559 L328,559")
    s.path("M450,588 L450,618 L40,618 L40,106")
    s.text(470, 623, "Lessons feed the next preparation", 13, t["soft"])
    return s


# ------------------------------------------------------------------- tier map
FUNCS = {
    "GOVERN": [("GV-1", "Charter", "E", 0), ("GV-3", "Policies", "E", 1), ("GV-4", "Roles", "E", 0),
               ("GV-6", "Supply chain", "E", 1), ("GV-7", "Oversight", "E", 1),
               ("GV-2", "Risk integration", "S", 0), ("GV-5", "Resourcing", "S", 0)],
    "IDENTIFY": [("ID-1", "Asset inventory", "E", 1), ("ID-3", "Crown jewels", "E", 0),
                 ("ID-4", "Vulnerabilities", "E", 1), ("ID-5", "Threat profile", "E", 0),
                 ("ID-6", "Risk assessment", "E", 1),
                 ("ID-2", "Data classes", "S", 0), ("ID-7", "Improvement", "S", 0)],
    "PROTECT": [("PR-1", "Identity, access", "E", 1), ("PR-2", "Awareness", "E", 1),
                ("PR-3", "Data security", "E", 1), ("PR-4", "Hardening", "E", 1),
                ("PR-5", "Patching", "E", 1), ("PR-7", "Tested backups", "E", 1),
                ("PR-9", "Email and web", "E", 1), ("PR-8", "basic form", "B", 1),
                ("PR-6", "Segmentation", "S", 0), ("PR-8", "Secure change", "S", 1)],
    "DETECT": [("DE-1", "Log collection", "E", 1), ("DE-3", "Triage", "E", 1), ("DE-2", "basic form", "B", 0),
               ("DE-2", "Detection eng.", "S", 0), ("DE-4", "Coverage", "S", 0),
               ("DE-5", "Hunting", "S", 0), ("DE-7", "Integrity checks", "S", 0),
               ("DE-6", "Validation", "A", 0)],
    "RESPOND": [("RS-1", "IR plan", "E", 1), ("RS-2", "Playbooks", "E", 1), ("RS-4", "Containment", "E", 1),
                ("RS-5", "Reporting", "E", 1), ("RS-6", "Crisis interface", "E", 1),
                ("RS-7", "Exercises", "E", 1), ("RS-3", "Forensics", "S", 0)],
    "RECOVER": [("RC-1", "Recovery plans", "E", 1), ("RC-4", "Communication", "E", 0),
                ("RC-5", "Lessons learned", "E", 0),
                ("RC-2", "Trusted restore", "S", 0), ("RC-3", "Verified recovery", "S", 0),
                ("RC-6", "Continuity", "S", 0)],
}


def tier_map(t):
    cw, ch, gap, x0 = 116, 40, 6, 20
    tiers = [("E", "Essential", "the defensible minimum and the NIS2 floor"),
             ("S", "plus Standard", "a dedicated CDC, measured"),
             ("A", "plus Advanced", "validation")]
    rows = {k: max(sum(1 for c in caps if c[2] == k or (k == "E" and c[2] == "B")) for caps in FUNCS.values())
            for k, _, _ in tiers}
    h = 64 + sum(44 + rows[k] * (ch + gap) for k, _, _ in tiers) + 60
    s = Svg(760, h, "Capability tier map",
            "The 43 capabilities by function and by the lowest tier that should adopt them: Essential, "
            "Standard or Advanced. A red dot marks capabilities that carry the NIS2 legal floor; for an entity "
            "in NIS2 scope they are never above tier. DE-2 and PR-8 also have a basic form in Essential.", t)
    for j, fn in enumerate(FUNCS):
        x = x0 + j * (cw + gap)
        s.rect(x, 20, cw, 5, t["fn"][fn], rx=2)
        s.text(x, 46, fn, 13, t["fn"][fn], 700)
    y = 64
    for k, name, sub in tiers:
        s.add(f'<line x1="{x0}" y1="{y}" x2="740" y2="{y}" stroke="{t["line"]}"/>')
        s.text(x0, y + 24, name, 15, t["eu"], 600)
        s.text(x0 + 9 * len(name) + 14, y + 24, sub, 13, t["soft"])
        y += 38
        for j, caps in enumerate(FUNCS.values()):
            x = x0 + j * (cw + gap)
            for i, (cid, label, tier, nis2) in enumerate(c for c in caps if c[2] == k or (k == "E" and c[2] == "B")):
                yy = y + i * (ch + gap)
                if tier == "E":
                    s.rect(x, yy, cw, ch, t["eu"]); c1 = c2 = t["on_eu"]
                elif tier == "S":
                    s.rect(x, yy, cw, ch, t["eu_soft"], t["eu"], sw=1.2); c1, c2 = t["eu"], t["ink"]
                elif tier == "A":
                    s.rect(x, yy, cw, ch, t["card"], t["eu"], dash="5 3", sw=1.2); c1, c2 = t["eu"], t["ink"]
                else:
                    s.rect(x, yy, cw, ch, "none", t["eu"], dash="3 3", sw=1.2); c1, c2 = t["eu"], t["soft"]
                s.text(x + 8, yy + 16, cid, 12, c1, 700)
                s.text(x + 8, yy + 32, label, 12, c2)
                if nis2:
                    s.add(f'<circle cx="{x + cw - 10}" cy="{yy + 11}" r="4.5" fill="{t["accent"]}" '
                          f'stroke="{t["card"] if tier == "E" else "none"}" stroke-width="1.5"/>')
        y += rows[k] * (ch + gap) + 6
    ly = h - 36
    s.add(f'<circle cx="26" cy="{ly - 4}" r="4.5" fill="{t["accent"]}"/>')
    s.text(38, ly, "Carries the NIS2 legal floor: never above tier for an entity in scope", 13, t["soft"])
    s.rect(20, ly + 10, 22, 14, "none", t["eu"], rx=3, dash="3 3", sw=1.2)
    s.text(50, ly + 22, "Basic form already in Essential", 13, t["soft"])
    return s


# -------------------------------------------------------------- decision path
def decision_path(t):
    s = Svg(760, 600, "Choosing an operating model: the decision path",
            "Five questions in order. 1: must log data stay in the organisation or country? If yes, keep those "
            "sources in-house. 2: need out-of-hours detection within six months? If yes, start with a provider and "
            "contract for exit, then continue. 3: can you hire and keep the 9 to 10 people a 24/7 seat takes? If "
            "no, a provider or your operations desk holds nights. 4: can you hire 5 to 8 senior engineers? Yes: "
            "capability-based, model C. Juniors only: tiered, model B. Neither: provider, model A. 5: does triage "
            "need deep business knowledge? If yes, keep that triage in-house whatever the model.", t)
    qs = [(20, "1", "Must any log data stay in the", "organisation or the country?"),
          (112, "2", "Do you need out-of-hours", "detection within six months?"),
          (204, "3", "Can you hire and keep the 9–10", "people one 24/7 seat takes?"),
          (360, "4", "Can you hire 5–8 senior people", "who work with code and automation?"),
          (516, "5", "Does triage need deep", "business knowledge?")]
    for y, n, a, b in qs:
        s.rect(20, y, 360, 64, t["card"], t["line"])
        s.add(f'<circle cx="52" cy="{y + 32}" r="16" fill="{t["eu"]}"/>')
        s.text(52, y + 37, n, 15, t["on_eu"], 700, "middle")
        s.text(82, y + 27, a, 15, t["ink"], 600)
        s.text(82, y + 47, b, 15, t["ink"], 600)
    for y1, y2 in ((84, 110), (176, 202), (268, 358), (424, 514)):
        s.path(f"M200,{y1} L200,{y2}")

    def outcome(y, models, line1, line2, kind="eu"):
        fill, stroke = (t["eu_soft"], t["eu"]) if kind == "eu" else (t["accent_soft"], t["accent"])
        s.rect(470, y, 270, 52, fill, stroke, sw=1.2)
        x = 484
        for m in models:
            w = 12 + 9 * len(m)
            s.add(f'<rect x="{x}" y="{y + 13}" width="{w}" height="26" rx="13" fill="{t["eu"]}"/>')
            s.text(x + w / 2, y + 31, m, 13, t["on_eu"], 700, "middle")
            x += w + 6
        x += 4 if models else 0
        s.text(x, y + 22, line1, 14, t["ink"], 600)
        s.text(x, y + 40, line2, 13, t["soft"])

    def branch(y_from, y_to, label, color=None):
        color = color or t["eu"]
        s.path(f"M380,{y_from} L420,{y_from} L420,{y_to} L468,{y_to}" if y_from != y_to else
               f"M380,{y_from} L468,{y_to}")
        s.text(428, y_to - 6, label, 13, color, 600)

    outcome(26, ["B", "C"], "Keep those in-house", "a provider may watch the rest"); branch(52, 52, "Yes")
    outcome(118, ["A", "A+C"], "Start with a provider", "contract for exit first"); branch(144, 144, "Yes")
    outcome(210, ["A", "A+C"], "Provider holds nights", "or a 24/7 operations desk"); branch(236, 236, "No")
    outcome(306, ["C"], "Capability-based team", "provider or on-call at night")
    outcome(366, ["B"], "Tiered SOC", "juniors trained up the tiers")
    outcome(426, ["A"], "Provider", "with 1–3 internal people")
    s.path("M380,392 L420,392")
    for yy, lab in ((332, "Yes"), (392, "Juniors"), (452, "Neither")):
        s.path(f"M420,392 L420,{yy} L468,{yy}")
        s.text(428, yy - 6, lab, 13, t["eu"], 600)
    outcome(522, [], "Keep that triage in-house", "whatever the model", kind="red")
    branch(548, 548, "Yes", t["accent"])
    return s


# ------------------------------------------------------------------ staffing
def staffing(t):
    s = Svg(760, 480, "Why one 24/7 seat takes about 5.6 people",
            "Example with a Danish full-time contract. One person has 1,924 contract hours a year; after 185 hours "
            "of leave, 67 of public holidays, 59 of sickness and 37 of training, 1,576 hours remain. Covering one "
            "seat around the clock takes 8,760 hours, which is 5.6 people at 1,576 hours each. A 24/7 line with a "
            "second daytime seat, detection engineering and a lead comes to about 9 to 10 people.", t)
    x0, wtot = 20, 720
    s.text(x0, 28, "One full-time person, one year", 16, t["ink"], 600)
    s.text(x0, 48, "Danish 37-hour contract as the example; use your own numbers", 13, t["soft"])
    y, k = 76, wtot / 1924
    x = x0
    for i, v in enumerate((1576, 185, 67, 59, 37)):
        w = v * k
        s.rect(x, y, w, 40, t["eu"] if i == 0 else t["accent_soft"], None if i == 0 else t["card"], rx=2, sw=1)
        if i == 0:
            s.text(x + 14, y + 26, "Available 1,576 h", 15, t["on_eu"], 600)
            end = x + w
        x += w
    s.text(x0 + wtot, y - 8, "1,924 contract hours", 13, t["soft"], 400, "end")
    s.add(f'<path d="M{end + 2},{y + 46} l0,6 L{x0 + wtot},{y + 52} l0,-6" fill="none" stroke="{t["soft"]}"/>')
    s.text(x0 + wtot, y + 70, "Leave 185 · Holidays 67 · Sickness 59 · Training 37", 13, t["soft"], 400, "end")

    y2 = 192
    s.text(x0, y2, "One seat, around the clock", 16, t["ink"], 600)
    s.text(x0, y2 + 20, "24 × 365 = 8,760 hours, in blocks of 1,576 hours", 13, t["soft"])
    k2 = wtot / 8760
    for i in range(6):
        w = min(1576, 8760 - i * 1576) * k2
        x = x0 + i * 1576 * k2
        last = i == 5
        s.rect(x + 1, y2 + 34, w - 2, 40, t["eu_soft"] if last else t["eu"], t["eu"] if last else None, rx=2, sw=1)
        s.text(x + w / 2, y2 + 59, "0.6" if last else f"Person {i + 1}", 14,
               t["eu"] if last else t["on_eu"], 600, "middle")
    s.text(x0 + wtot, y2 + 98, "≈ 5.6 people per seat", 15, t["eu"], 700, "end")

    y3 = 330
    s.text(x0, y3, "A 24/7 in-house line", 16, t["ink"], 600)
    s.text(x0, y3 + 20, "People, on a scale of 0 to 11", 13, t["soft"])
    k3 = wtot / 11
    x = x0
    for v, lab, fill, dash in ((5.6, "24/7 seat 5.6", t["eu"], None), (1.6, "Day seat 1.6", t["eu_soft"], None),
                               (1, "", t["eu_soft"], None), (1, "", "none", "4 3"), (1, "Lead 1", t["eu_soft"], None)):
        w = v * k3
        s.rect(x + 1, y3 + 34, w - 2, 40, fill, None if fill == t["eu"] else t["eu"], rx=2, dash=dash, sw=1)
        if lab:
            s.text(x + w / 2, y3 + 59, lab, 14, t["on_eu"] if fill == t["eu"] else t["ink"], 600, "middle")
        x += w
    s.text(x0 + 8.2 * k3, y3 + 59, "Engineering 1–2", 14, t["ink"], 600, "middle")
    for v in range(12):
        xx = x0 + v * k3
        s.add(f'<line x1="{xx}" y1="{y3 + 78}" x2="{xx}" y2="{y3 + 84}" stroke="{t["soft"]}"/>')
        s.text(xx, y3 + 99, str(v), 12, t["soft"], 400, "middle")
    s.text(x0 + 10.2 * k3, y3 + 26, "≈ 9–10 people", 15, t["eu"], 700, "end")
    s.text(x0, 470, "A second seat at night as well adds about 4 more people.", 13, t["soft"])
    return s


# ------------------------------------------------------------ reporting clocks
def reporting_clocks(t):
    cols = ["Without undue delay", "4 h", "24 h", "72 h", "1 month"]
    x_lab, x0, cw = 20, 150, 118
    rows = [
        ("NIS2", "Art. 23", [(2, "Early warning", "CSIRT or authority"), (3, "Incident notification", ""),
                             (4, "Final report", "from notification"), (0, "Recipients of", "your services")]),
        ("GDPR", "Art. 33–34", [(3, "Supervisory", "authority"), (0, "Data subjects,", "if high risk")]),
        ("DORA", "Art. 19, finance", [(1, "Initial, from", "classification"), (2, "Initial at the", "latest"),
                                      (3, "Intermediate", "report"), (4, "Final report", "")]),
        ("CER", "Art. 15, critical", [(2, "Initial", "notification"), (4, "Detailed report", "")]),
    ]
    rh, top = 78, 88
    h = top + len(rows) * rh + 56
    s = Svg(760, h, "EU reporting clocks after an incident",
            "Deadlines counted from awareness unless noted. NIS2: early warning within 24 hours, incident "
            "notification within 72 hours, final report one month after the notification, and the recipients of "
            "your services without undue delay. GDPR: supervisory authority within 72 hours, data subjects without "
            "undue delay if the risk is high. DORA: initial notification within 4 hours of classification as major "
            "and at the latest 24 hours from awareness, intermediate within 72 hours, final within one month. CER: "
            "initial notification within 24 hours, detailed report within one month.", t)
    s.text(x_lab, 30, "From awareness", 15, t["accent"], 600)
    s.text(x_lab, 50, "Columns are steps, not to scale", 13, t["soft"])
    for i, c in enumerate(cols):
        cx = x0 + i * cw + cw / 2
        s.text(cx, 72, c, 14 if i else 12, t["ink"], 700 if i else 600, "middle")
        s.add(f'<line x1="{cx}" y1="{top - 6}" x2="{cx}" y2="{top + len(rows) * rh - 10}" '
              f'stroke="{t["line"]}" stroke-dasharray="2 4"/>')
    for r, (name, ref, events) in enumerate(rows):
        y = top + r * rh
        s.text(x_lab, y + 30, name, 16, t["eu"], 700)
        s.text(x_lab, y + 49, ref, 12, t["soft"])
        cy = y + 22
        last, first = max(e[0] for e in events), min(e[0] for e in events)
        s.add(f'<line x1="{x0 + first * cw + cw / 2}" y1="{cy}" x2="{x0 + last * cw + cw / 2}" y2="{cy}" '
              f'stroke="{t["eu"]}" stroke-width="2"/>')
        for col, a, b in events:
            cx = x0 + col * cw + cw / 2
            hollow = col == 0
            s.add(f'<circle cx="{cx}" cy="{cy}" r="7" fill="{t["card"] if hollow else t["eu"]}" '
                  f'stroke="{t["eu"]}" stroke-width="2"/>')
            s.text(cx, cy + 26, a, 12, t["ink"], 600, "middle")
            if b:
                s.text(cx, cy + 41, b, 12, t["soft"], 400, "middle")
        if r < len(rows) - 1:
            s.add(f'<line x1="{x_lab}" y1="{y + rh - 4}" x2="740" y2="{y + rh - 4}" stroke="{t["line"]}"/>')
    s.text(x_lab, h - 24, "Open circle: without undue delay. National law may add recipients or detail;",
           12, t["soft"])
    s.text(x_lab, h - 8, "check your annex. Not legal advice.", 12, t["soft"])
    return s


# ------------------------------------------------------------ first 90 days
PLAN_90 = [
    ("Charter drafted, containment authority", 1, 2, "GOVERN", "GATE"),
    ("Regulatory applicability register", 1, 4, "GOVERN", None),
    ("Operating model decided", 2, 6, "GOVERN", None),
    ("Crown jewels agreed with the business", 3, 8, "IDENTIFY", None),
    ("MFA, tested backup, admin paths", 4, 10, "PROTECT", "HARD"),
    ("Identity, endpoint, email logs onboarded", 6, 12, "DETECT", "HARD"),
    ("IR plan, playbooks, reporting drill", 8, 12, "RESPOND", "GATE"),
    ("Baseline maturity assessment", 12, 12, "GOVERN", None),
]


def first_90_days(t):
    x0, wk, lab_w, top, rh = 290, 37, 270, 64, 40
    h = top + len(PLAN_90) * rh + 96
    s = Svg(760, h, "The first 90 days",
            "Week by week: charter drafted in weeks 1 to 2; regulatory applicability register in weeks 1 to 4; "
            "operating model decided in weeks 2 to 6; crown jewels agreed in weeks 3 to 8; MFA, a tested backup "
            "and admin-path segmentation in weeks 4 to 10; identity, endpoint and email logs onboarded in weeks "
            "6 to 12; incident response plan, playbooks and a reporting drill in weeks 8 to 12; baseline maturity "
            "assessment in week 12. Charter sign-off and the reporting drill depend on decisions by others; MFA "
            "and log onboarding depend on work by other teams.", t)
    s.text(20, 28, "Week", 13, t["soft"], 600)
    for w in range(1, 13):
        cx = x0 + (w - 0.5) * wk
        s.text(cx, 28, str(w), 13, t["soft"], 600, "middle")
        s.add(f'<line x1="{x0 + w * wk}" y1="{top - 18}" x2="{x0 + w * wk}" y2="{top + len(PLAN_90) * rh}" '
              f'stroke="{t["line"]}" stroke-dasharray="2 4"/>')
    s.add(f'<line x1="{x0}" y1="{top - 18}" x2="{x0}" y2="{top + len(PLAN_90) * rh}" stroke="{t["line"]}"/>')
    for i, (label, a, b, fn, dep) in enumerate(PLAN_90):
        y = top + i * rh
        s.text(20, y + 21, label, 13, t["ink"])
        bx, bw = x0 + (a - 1) * wk + 2, (b - a + 1) * wk - 4
        s.rect(bx, y + 5, bw, rh - 12, t["fn"][fn], rx=4)
        if dep:
            col = t["accent"] if dep == "GATE" else t["eu"]
            s.rect(bx + bw - 48, y + 10, 42, rh - 22, t["card"], rx=3)
            s.text(bx + bw - 27, y + 23, dep, 10, col, 700, "middle")
    yl = top + len(PLAN_90) * rh
    s.add(f'<path d="M{x0 + 12 * wk},{yl + 6} l7,9 l-7,9 l-7,-9 z" fill="{t["accent"]}"/>')
    s.text(x0 + 12 * wk - 14, yl + 20, "Day 90: exit criteria", 13, t["accent"], 600, "end")
    ly = yl + 50
    x = 20
    for fn in ("GOVERN", "IDENTIFY", "PROTECT", "DETECT", "RESPOND"):
        s.rect(x, ly - 11, 14, 14, t["fn"][fn], rx=3)
        s.text(x + 20, ly, fn.capitalize(), 12, t["soft"])
        x += 32 + 7.5 * len(fn)
    s.text(20, ly + 24, "GATE: another party must decide.  HARD: another team must do the work.", 12, t["soft"])
    return s


# ---------------------------------------------------------------- IT/OT zones
OTX = [
    ("OTX-01", ("Cut supplier", "remote access"), 0),
    ("OTX-02", ("Disable IT accounts", "with DMZ access"), 0),
    ("OTX-03", ("Block a single", "conduit"), 1),
    ("OTX-04", ("Isolate an engineering", "workstation"), 2),
    ("OTX-05", ("Separate IT", "from OT"), 3),
    ("OTX-06", ("Isolate, reboot or", "image an OT asset"), 4),
]


def it_ot_zones(t):
    s = Svg(760, 520, "The IT/OT boundary: who watches and who decides",
            "Three zones. In IT, the CDC decides and acts within its mandate. In the boundary zone, meaning the "
            "IT/OT DMZ and firewalls, jump hosts and remote access, engineering workstations, historians and data "
            "diodes, file transfer and update servers, shared identity and backups of OT configurations, the CDC "
            "monitors and ownership is agreed jointly. In OT, the operator decides and the CDC advises. Containment "
            "decisions move from the CDC to the operator: supplier remote access and IT accounts with DMZ access "
            "are the CDC's call; blocking a conduit needs OT approval; isolating an engineering workstation is "
            "OT's call, advised by the CDC; separating IT from OT is for OT management; any action on an OT asset "
            "follows the vendor procedure. One reporting owner per incident, and the clock starts at awareness on "
            "either side.", t)
    zones = [(20, 200, "IT", "The CDC decides and acts", ["Endpoints and servers", "Identity and cloud", "Mail and web"], "card"),
             (240, 280, "Boundary zone", "The CDC monitors; owners agreed", ["IT/OT DMZ and firewalls", "Jump hosts, remote access", "Engineering workstations", "Historians, data diodes", "File transfer, update servers", "Shared identity and trusts", "Backups of OT configurations"], "soft"),
             (540, 200, "OT", "The operator decides", ["Control systems", "Safety systems", "Field devices"], "card")]
    for x, w, title, sub, items, kind in zones:
        if kind == "soft":
            s.rect(x, 20, w, 250, t["eu_soft"], t["eu"], sw=1.5)
        else:
            s.rect(x, 20, w, 250, t["card"], t["line"])
        s.text(x + 16, 48, title, 16, t["eu"] if kind == "soft" else t["ink"], 700)
        s.text(x + 16, 68, sub, 13, t["soft"])
        for i, it in enumerate(items):
            yy = 100 + i * 23
            s.add(f'<circle cx="{x + 21}" cy="{yy - 4}" r="3" fill="{t["eu"] if kind == "soft" else t["soft"]}"/>')
            s.text(x + 32, yy, it, 13, t["ink"])
    s.path("M222,240 L238,240", stroke=t["accent"], sw=2)
    s.text(130, 255, "most attacks come this way", 12, t["accent"], 600, "middle")
    s.path("M522,240 L538,240", stroke=t["accent"], sw=2)

    s.text(20, 306, "Who decides containment at the boundary", 15, t["ink"], 700)
    stops = ["CDC", "CDC, OT approves", "OT, CDC advises", "OT management", "OT, vendor procedure"]
    colw = 144
    for i, st in enumerate(stops):
        x = 20 + i * colw
        col = t["eu"] if i < 2 else t["accent"]
        s.rect(x + 2, 318, colw - 4, 4, col, rx=2)
        s.text(x + 4, 340, st, 12, col, 700)
    placed = {}
    for cid, (l1, l2), pos in OTX:
        n = placed.get(pos, 0); placed[pos] = n + 1
        x, y = 20 + pos * colw + 2, 352 + n * 60
        col = t["eu"] if pos < 2 else t["accent"]
        s.rect(x, y, colw - 4, 54, t["card"], col, sw=1.2)
        s.text(x + 10, y + 17, cid, 12, col, 700)
        s.text(x + 10, y + 33, l1, 12, t["ink"])
        s.text(x + 10, y + 48, l2, 12, t["ink"])
    s.rect(20, 476, 720, 34, t["accent_soft"], t["accent"], sw=1)
    s.text(380, 498, "Reporting: one owner per incident. The clock starts at awareness on either side.", 13,
           t["ink"], 600, "middle")
    return s


# ------------------------------------------------------------- AI use ratings
AI_USES = [
    ("Summarising alerts", ("Should", "Should", "Should")),
    ("Enrichment and context", ("Should", "Should", "Should")),
    ("Explaining artefacts and log lines", ("Should", "Should", "Can")),
    ("Drafting search queries", ("Should", "Should", "Should")),
    ("Drafting and converting detection rules", ("Can", "Should", "Should")),
    ("Proposing a triage verdict", ("Caution", "Should", "Should")),
    ("Closing alerts without a human", ("Avoid", "Caution", "Caution")),
    ("Investigation support", ("Caution", "Should", "Should")),
    ("Summarising threat intelligence", ("Should", "Should", "Should")),
    ("Drafting reports and reviews", ("Should", "Should", "Should")),
    ("Drafting statutory notifications", ("Caution", "Caution", "Caution")),
    ("Agents investigating on their own", ("Avoid", "Caution", "Can")),
    ("Automated containment", ("Avoid", "Caution", "Caution")),
    ("Training and onboarding material", ("Can", "Should", "Should")),
]


def ai_alt_text():
    cols = ("teams of one to three", "dedicated CDCs", "large CDCs")
    parts = []
    for name, r in AI_USES:
        parts.append(f"{name}: " + ", ".join(f"{v.lower().replace('caution', 'with caution')} for {c}" for v, c in zip(r, cols)))
    return "AI uses rated by team size. " + "; ".join(parts) + "."


def ai_ratings(t):
    styles = {"Should": (t["eu"], None, t["on_eu"]), "Can": (t["eu_soft"], t["eu"], t["eu"]),
              "Caution": (t["warn_soft"], t["warn"], t["warn"]), "Avoid": (t["accent_soft"], t["accent"], t["accent"])}
    labels = {"Should": "Should", "Can": "Can", "Caution": "With caution", "Avoid": "Avoid"}
    x0, cw, top, rh = 330, 136, 58, 32
    h = top + len(AI_USES) * rh + 54
    s = Svg(760, h, "AI uses by team size", ai_alt_text(), t)
    for j, head in enumerate(("1–3 people", "Dedicated CDC", "Large CDC")):
        s.text(x0 + j * cw + cw / 2, 40, head, 14, t["ink"], 700, "middle")
    for i, (name, r) in enumerate(AI_USES):
        y = top + i * rh
        if i % 2 == 0:
            s.rect(14, y, 732, rh, t["eu_soft"] if False else t["card"], rx=4)
        s.text(24, y + 21, name, 13, t["ink"])
        for j, v in enumerate(r):
            fill, stroke, col = styles[v]
            cx = x0 + j * cw + 8
            s.rect(cx, y + 4, cw - 16, rh - 8, fill, stroke, rx=12, sw=1.2)
            s.text(cx + (cw - 16) / 2, y + 21, labels[v], 12, col, 700, "middle")
    ly = top + len(AI_USES) * rh + 30
    s.text(24, ly, "Every use comes with conditions, listed in the table below the chart.", 12, t["soft"])
    return s


# ------------------------------------------------------------ maturity levels
LEVELS = [
    (1, "Initial", ("It happens when", "someone remembers.")),
    (2, "Managed", ("It is written down", "and someone owns it.")),
    (3, "Established", ("It is measured", "and consistent.")),
    (4, "Optimising", ("It improves", "itself.")),
]


def maturity_levels(t):
    s = Svg(760, 350, "The four maturity levels",
            "A staircase of four levels. Level 1, Initial: it happens when someone remembers. Level 2, Managed: "
            "it is written down and someone owns it; Level 2 is also the NIS2 floor. Level 3, Established: it is "
            "measured and consistent. Level 4, Optimising: it improves itself. Scoring is staged: a level counts "
            "only when all its criteria, and those of the levels below, are met.", t)
    bottom, w, gap, x0 = 300, 176, 9, 20
    for i, (n, name, quote) in enumerate(LEVELS):
        x, top = x0 + i * (w + gap), 190 - i * 50
        if n == 2:
            s.rect(x, top, w, bottom - top, t["accent_soft"], t["accent"], sw=2)
            s.text(x + w / 2, top - 12, "NIS2 floor", 13, t["accent"], 700, "middle")
        else:
            s.rect(x, top, w, bottom - top, t["eu_soft"], t["eu"])
        s.text(x + 14, top + 26, f"Level {n}", 15, t["ink"], 700)
        s.text(x + 14, top + 46, name, 13, t["soft"], 600)
        s.text(x + 14, top + 72, quote[0], 13, t["ink"], 400, italic=True)
        s.text(x + 14, top + 90, quote[1], 13, t["ink"], 400, italic=True)
    s.path(f"M{x0},{bottom + 14} L{x0 + 4 * w + 3 * gap},{bottom + 14}", marker="arr")
    s.text(x0, bottom + 40, "Staged scoring: a level counts only when all its criteria, and those of the "
           "levels below, are met.", 12, t["soft"])
    return s


# ---------------------------------------------------- detection-as-code pipeline
def dac_pipeline(t):
    s = Svg(760, 300, "The detection-as-code pipeline",
            "Every merge to main runs four stages: lint and schema validation, unit tests, conversion to the "
            "platform's query language, and a staging deploy with a volume smoke test. Errors in the first "
            "three stages fail the build. Production deploy follows through the platform API, then a nightly "
            "drift check compares the platform with the repository, and emulation validation runs on a "
            "schedule to confirm alerts fire end to end. Adopt stages 1 to 3 first, then 5 and 6, then 7.", t)
    w, h, gap, x0 = 172, 62, 17, 10
    row1 = [("1. Lint and schema", "fields, UUID, ATT&CK IDs"), ("2. Unit tests", "should fire, should not"),
            ("3. Conversion", "Sigma to platform query"), ("4. Staging deploy", "volume smoke test")]
    y1 = 56
    s.text(x0, 30, "Every merge to main", 13, t["soft"], 600)
    s.rect(x0 - 4, y1 - 8, 3 * w + 2 * gap + 8, h + 34, t["accent_soft"], rx=8)
    s.text(x0 + 6, y1 + h + 20, "An error here fails the build", 12, t["accent"], 600)
    for i, (a, b) in enumerate(row1):
        x = x0 + i * (w + gap)
        s.box(x, y1, w, h, a, b)
        if i:
            s.path(f"M{x - gap + 1},{y1 + h / 2} L{x - 2},{y1 + h / 2}")
    y2 = 192
    s.text(x0 + w / 2 + 12, y2 - 30, "After the merge", 13, t["soft"], 600)
    row2 = [("5. Production deploy", "via API, ids recorded", "card"),
            ("6. Drift detection", "nightly diff with repo", "card"),
            ("7. Emulation", "scheduled, end to end", "sched")]
    for i, (a, b, k) in enumerate(row2):
        x = x0 + i * (w + gap)
        if k == "sched":
            s.rect(x, y2, w, h, t["card"], t["eu"], dash="5 4")
            s.text(x + w / 2, y2 + h / 2 - 3, a, 14, t["ink"], 600, "middle")
            s.text(x + w / 2, y2 + h / 2 + 15, b, 12, t["soft"], 400, "middle")
        else:
            s.box(x, y2, w, h, a, b, kind=k)
        if i:
            s.path(f"M{x - gap + 1},{y2 + h / 2} L{x - 2},{y2 + h / 2}", dash="4 4" if k == "sched" else None)
    sx = x0 + 3 * (w + gap) + w / 2
    s.path(f"M{sx},{y1 + h} L{sx},{y2 - 24} L{x0 + w / 2},{y2 - 24} L{x0 + w / 2},{y2 - 2}")
    xn = x0 + 3 * (w + gap)
    s.text(xn, y2 + 20, "Adopt in this order:", 12, t["soft"], 600)
    s.text(xn, y2 + 38, "stages 1 to 3 first,", 12, t["soft"])
    s.text(xn, y2 + 56, "then 5 and 6, then 7.", 12, t["soft"])
    s.text(x0, y2 + h + 32, "Dashed: runs on a schedule, not on every merge.", 12, t["soft"])
    return s


DIAGRAMS = {
    "respond-incident-flow": incident_flow,
    "tiers-capability-map": tier_map,
    "operating-model-decision-path": decision_path,
    "operating-model-staffing": staffing,
    "respond-reporting-clocks": reporting_clocks,
    "start-here-first-90-days": first_90_days,
    "it-ot-zones": it_ot_zones,
    "ai-use-ratings": ai_ratings,
    "maturity-levels": maturity_levels,
    "dac-pipeline": dac_pipeline,
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fn in DIAGRAMS.items():
        for mode, theme in THEMES.items():
            (OUT / f"{name}-{mode}.svg").write_text(fn(theme).render(), encoding="utf-8", newline="\n")
    print(f"wrote {2 * len(DIAGRAMS)} files to {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
