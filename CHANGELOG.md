# Changelog — Open CDC Framework

## Unreleased

Changes from a second, deliberately critical review by a senior SOC manager:

- **Staffing and cost, with the arithmetic.** [Operating models](docs/11-operating-models.md) gains "Staffing and cost: the arithmetic": how many people one seat takes around the clock, worked through step by step with inputs to replace; how the 8–12 FTE figure for a 24/7 line is built; how to make the lone night analyst safe; the cost lines to estimate, and what to watch for in each; and a three-year comparison table across the operating models. The staffing notes in DETECT and Model B now link to it.
- **ATT&CK coverage metric tightened.** The metrics template now counts only techniques in your threat profile at level 3 on the honesty scale from the detection-as-code deep dive, drops the fixed 70% target in favour of a trend with the uncovered techniques named, and adds whole-matrix coverage and rule counts to the anti-patterns.
- **Roadmap renumbered.** The planned releases after v1.0.0 were labelled v0.2 and v0.3; they are now v1.1 and v1.2, and the roadmap explains how releases are numbered. References in ABOUT, README, the landing page, the tools README and the IR plan template follow.

### Scoring changes

Two DETECT criteria changed. Assessments made under v1.0.0 can move, so compare with care:

- **Level 3:** "24/7 monitoring, in-house or hybrid" becomes "Coverage hours meet the risk-based target set in GOVERN; out-of-hours escalation tested twice a year". Maturity measures how well detection works; how many hours a day someone watches is a risk decision. Under the old wording a well-run business-hours team, the capability-based Model C the framework itself describes, could never pass Level 2 in DETECT. The maturity model gains "Coverage hours are a target, not a level", with typical targets per organisation type. A DETECT score can rise under the new wording; it cannot fall.
- **Level 2:** "≥ 20 documented use cases mapped to ATT&CK" becomes "Use cases documented for the top techniques in the threat profile, each with owner, ATT&CK mapping and runbook". A rule count is the vanity metric the framework warns against elsewhere. A team with twenty unfocused rules may now fail this criterion; one with fewer rules aimed at its real threats may now pass.

The interactive self-assessment keeps the same number and order of criteria, so existing resume links and snapshots still open; a criterion marked implemented under the old wording keeps that status and should be re-checked against the new one.

- **Maturity self-assessment redesigned as a workspace**, inspired by the SIM3 self-assessment tool. Criteria sit on the left with one tab per function, each tab showing the function's level and how many criteria are met. A results panel on the right stays in view and updates on every click: target profiles as buttons, summary tiles, and three views: the score chart, the Result table, and a new **Open actions** list of the criteria still missing to reach your targets, each of which jumps to the criterion. Status is set with one click on a five-button row instead of a dropdown. On phones the results move below the criteria, with a summary bar pinned to the bottom of the screen. Scoring, resume links and snapshot files are unchanged, so existing links and exports keep working.

Changes from a practitioner review of the site: a CDC manager from critical infrastructure read it cold and listed what would stop them relying on it.

- **Critical infrastructure and OT.** ABOUT gains "If you run critical infrastructure": what applies as written, what the CDC should own at the IT/OT boundary even without an OT profile, and what does not transfer. The OT/ICS profile moves from "Later" to v1.2 on the roadmap. The landing page and README link to the new section.
- **Annex currency.** All 27 national annexes open with a status block: last verified, verified by, second reviewer and next review due. The annex index shows the same columns under a "one reviewer so far" warning and commits to re-verification at least every six months.
- **Reusing past assessments.** The maturity model gains a SOC-CMM → OCDF mapping by aspect, a rough and explicitly uncalibrated score translation, and pointers to the existing SIM3 and CIS Controls crosswalks.
- **Attack-based playbooks**, published as drafts for field review: PB-IDC identity compromise, PB-BEC business email compromise and PB-RAN ransomware. They sit above the platform playbooks and hand off to them. PB-IDC fixes the containment order explicitly: block sign-in first, then revoke sessions immediately, because revoking while the account is enabled lets a password holder sign straight back in.
- **Trust signals.** The landing page shows the version and a "How current is this?" box. ABOUT gains "Maintainers and adoption", which states that there is one maintainer, that p0jst is the author, and invites teams to ask to be listed as users.
- **Author bio** updated to "formerly Senior Manager at the Norlys Cyber Defence Center" on the About page, README and landing page.

## v1.0.0 — 2026-09-02

First stable release. The framework is content-complete across all six functions, the regulatory layer and the practical assets; see the release notes for status and limitations, in particular that the reporting-deadline tables have not had independent legal review and nine national annexes still carry verification flags.

Since the v0.1-rc1 freeze candidate:

- **Persistent previous/next bar.** A slim bar slides in once you are past the first screenful of a page and hides again when the footer cards come into view, so the two never compete; it also steps aside for the mobile drawer and the search overlay. Built from MkDocs' own page order in `overrides/main.html` rather than scraped from the DOM.
- **More filename links rewritten as prose.** The earlier sweep only matched paths beginning `../`, so same-directory references such as `[10-tiers.md](10-tiers.md)` survived in body text. Twenty-one more rewritten, including the shared "Credits" footer across the ten numbered documents. Filenames are kept where the filename is the point: the README's document tables and the annex index's file column.

- **"Edit this page" action removed** via `content.action.edit`: the pencil beside each page heading read as interface clutter. `site/hooks.py`, which existed only to repoint that action for the two website-only pages, goes with it; `edit_uri` stays in `mkdocs.yml` with a note, so re-enabling is a one-line change.

- **Continue-reading navigation made visible.** The documents are numbered and meant to be read in order, so the previous/next links are a primary control, but Material renders them small and low-contrast inside the dark footer, where they are easy to miss entirely. They now sit on the page ground as cards matching the rest of the site, with the direction label in the accent red and a hover lift. On narrow screens the two cards stack and both stay labelled. Material hides the previous title by default, which with card styling left an empty box holding one arrow.

- **Link previews**: `assets/social-preview.png`, a 2560x1280 card in the site's own palette, typography and blueprint texture, plus Open Graph and Twitter card tags via a small theme override in `overrides/main.html`, so a link to opencdc.org shared into Slack, LinkedIn or a chat renders as a card rather than a bare URL. The same file is what should be uploaded as the repository's GitHub social preview.

- **Heading permalinks turned off** via `toc.permalink: false`: the paragraph-mark anchor that appeared beside every heading on hover read as a stray glyph rather than an affordance. Heading ids are still generated, so every section stays linkable. The table of contents links to each one and puts the anchor in the address bar.

- **RESPOND gains "the first hour of a major incident"** — the estate-wide moves that sit above any single playbook and are most often skipped under pressure: do not power systems off; cut external connectivity with a perimeter deny-all *including* VPN, site-to-site, RDP/VDI gateways and vendor/out-of-band paths; verify and then isolate backups; extend snapshot retention before defaults roll it off; and stand up emergency log collection where there is no aggregator. Plus a **counsel and insurance** subsection: cyber policies commonly mandate notification windows and pre-approved responder panels, and using your own first can reduce cover. Legal privilege over investigation reports is not uniform across member states either. Settle both before an incident, not during one.
- **RECOVER** notes that the recovery path is decided during response: pre-intrusion snapshots are often the cleanest restore point and expire on schedule regardless of the open incident.
- **Containment action catalogue** gains five estate-level rows, CON-11 to CON-15: perimeter deny-all, remote-access disable, backup isolation, snapshot-retention extension and emergency log collection. These are the actions whose authority most needs pre-agreeing.
- **IR plan template**: external counsel and cyber insurance contacts added to the roles table, and the containment step points at the first-hour actions.

- **New platform playbook: `playbooks/PB-WSV-windows-server.md`** — Windows Server, including domain controllers. Same structure as the existing three: prerequisites, triage, containment, RFC 3227 acquisition table, artefacts, analysis, eradication and reporting hooks. The server-specific weight sits where it belongs: Tier 0 blast radius, the identity-fabric consequences of a DC compromise, AD-specific evidence such as `ntds.dit`, SYSVOL, replication metadata and DCSync-shaped access, ADCS as a persistence path, and a recovery section that covers the double `krbtgt` reset and when to stop cleaning and execute the forest-recovery plan. Wired into the playbook index, the site nav, the landing page, the root README and the IR plan template.
- **Roadmap**: added "more platform playbooks" to v0.2 with candidate targets.

- **Fixed lists that never rendered as lists.** Twenty-four blocks across nine documents had no blank line between the lead-in sentence and the first bullet, which GitHub's renderer tolerates but Python-Markdown does not, so on the website they collapsed into run-on paragraphs. Worst affected were the whole maturity self-assessment checklist, with all 60 criteria run together as prose, the three platform playbooks' artefact lists, and the charter's containment-authority lists. All 75 built pages now verify clean.
- **Checkboxes render as checkboxes** via `pymdownx.tasklist`: the reference checklists showed a literal `[ ]` before every line. They are still not tickable in the browser, which is what the interactive tool is for, but they read as a checklist now.
- The three playbooks' artefact lists lead with a bold category such as **Event logs** or **Persistence**, so they can be scanned, and inline `code` sits tighter in the surrounding text.

- **Document numbers moved out of the page titles**: the numbered framework documents are staged for the website with their leading number lifted into a small kicker above the heading, reading "Document 11" and linked to the reading guide, so the title reads as a title. The number stays visible and searchable, since 56 in-prose cross-references cite documents by number, but it no longer arrives as the first word a reader sees when they land from the navigation. The repository markdown keeps its numbered headings, where the number carries the file's reading order.

- **Typography and link legibility**: the site and the three tools now use **IBM Plex Sans / IBM Plex Mono**, self-hosted from `assets/fonts/` under OFL-1.1. No request reaches a third-party font CDN, which keeps the site's own privacy posture intact. Latin, Latin-extended, Greek and Cyrillic subsets are included so the native-language law names in the national annexes render in the same face; anything outside them falls back to the system stack. Links now carry a **persistent underline**: the navy reads at 10.9:1 against the paper but only 1.85:1 against body text, so colour alone was not a reliable signal that something was a link, where WCAG 1.4.1 asks for 3:1. Navigation, buttons and heading anchors stay undecorated. The permalink anchor is hidden in the landing-page hero, where the page has no table of contents to link into.

- **Site-wide review fixes**: bare URLs throughout the references and the 27 national annexes now render as real links via `pymdownx.magiclink`, covering 218 external links across 53 hosts that were previously plain text; the interactive-tools page is reachable from the sidebar again, since Material was hoisting it into the section title, and now links to each of the three tools; the "edit this page" action on the two website-only pages points at their real sources in `site/` through `site/hooks.py`; README points at opencdc.org rather than the github.io address; reassessment cadence is stated the same way in the README, the design navigator and the maturity model, as annually with quarterly action reviews; `tools/README.md` is ordered Tool 01 → 02 → 03; and the maturity tool's print stylesheet matches the other two.

- **Five-point status scale in the maturity self-assessment**, replacing the yes/no checkbox: *not considered · planned · partially in place · implemented · implemented & evidenced*. Only the top two count towards a level, so staged scoring is unchanged; the lower states drive a new progress view: a hatched segment on the score chart showing how far into the next level each function has come, a "planned or partly in place" tile, and a per-function breakdown in the Result table. An evidence-based scoring toggle counts only "implemented & evidenced", the reading to use when the assessment leaves the room. Documented as part of the scoring method in `docs/08-maturity-model.md`, mirrored as a status slot per criterion in `assessments/maturity-self-assessment.md`. Existing snapshots, browser copies and resume links keep working, and a ticked box reads as "implemented".

- **Navigation in the interactive tools**: all three tools now carry a breadcrumb bar back to the framework. They are standalone pages outside the MkDocs theme, so they had no header, logo or way home.

- **Resume links in the maturity self-assessment**: the tool now encodes the whole assessment, meaning answers, evidence notes, targets and header fields, into the page's URL fragment, so you get a unique link that restores exactly where you left off. Copy it, mail it to yourself, share it with a colleague; works on any device or browser without an account, a cookie or a server, and the fragment is never sent in an HTTP request. Highlighted as a "Save & resume" panel at the top of the tool, with a warning when evidence notes push the link past ~2 000 characters.

- **Website look & feel**: refreshed theme in `site/extra.css` and a refreshed landing page: full-width hero with an at-a-glance stat strip, feature cards with icon chips and hover lift, a "Where to begin" three-step section, and tightened typography, tables and admonitions. Same minimal, document-like identity; no new dependencies or webfonts.

- **Interactive maturity self-assessment**, Tool 03: `tools/maturity-assessment.html`, the maturity checklist filled out in the browser instead of as inert markdown checkboxes. Real checkboxes with evidence fields for all 60 criteria, staged auto-scoring per the maturity model's rules, target-profile presets from `docs/08-maturity-model.md`, a score-vs-target chart, a Result table naming exactly which criteria block the next level, and JSON snapshot export/import for tracking the trend. `assessments/maturity-self-assessment.md` now links to it at the top; landing page's "Assess your maturity" button points to it directly.

- **Website**: the framework now publishes as an MkDocs Material documentation site via GitHub Actions, with a landing page, full-text search and theming to match the tools; `site/` holds the landing page, theme CSS and staging script, `mkdocs.yml` the nav, `.github/workflows/publish-site.yml` the deployment. Repo layout and all links unchanged.

- **Team skill mapping** added to the Roles & Competences layer:
  - `templates/skill-self-assessment.xlsx`, with a CSV version alongside it. A 47-skill self-assessment sheet across 8 domains: the six CSF functions plus Platform & Automation and Professional Skills, rated 0–3 on the framework scale with a per-skill "want to grow?" flag
  - `tools/skill-matrix.html`, Tool 02. A single-file, dependency-free team skill matrix: upload returned sheets cumulatively, overwriting per person; team heatmap with coverage/bus-factor flags, gap analysis against editable per-role targets, train/mentor/hire action view, JSON snapshot export/import
  - New "Team skill mapping" section in `docs/12-roles-and-competences.md`, covering process, cadence, GDPR ground rules and hiring hook

## v0.1-rc1 — freeze candidate, 2026-07-15

Project name approved: Open CDC Framework (OCDF). First feature-complete release candidate. Contents:

- Six NIST CSF 2.0 function documents with CIA mapping, four-level maturity criteria, EU regulatory hooks, and external-dependency tables using the [GATE], [HARD] and [SOFT] convention
- Design layer: CIS-ordered Start Here prioritisation, E/S/A implementation tiers, operating models covering MSSP, tiered, capability-based and shared CDC, ECSF-based roles and competences
- Operations layer: tuning loop, detection-as-code plus an engineering deep dive with Sigma/YAML, CI/CD and honest ATT&CK coverage scoring, a CTI deep dive across the strategic, operational and tactical levels, automation & AI-triage guardrails, tool portfolio discipline, SIEM ownership incl. cloud data considerations
- Community layer: RFC 2350, TF-CSIRT/FIRST, SIM3 crosswalk, living-documentation controls, annual calendar
- Regulatory layer: EU landscape across NIS2, GDPR, DORA, CRA and CER; 27 national annexes with status verified July 2026; interactive law selector, CIS Controls v8 crosswalk with concrete actions
- Practical assets: 9 templates, 3 platform IR/forensics playbooks for Win11, macOS and RHEL; design navigator, maturity self-assessment

Known pre-v1.0 work: fill ABOUT placeholders; legal review of reporting-deadline tables and national law references; re-verify the "pending" annexes for FR, IE, LU, ES, PL and NL; set final repository URL in docs/19-references.md citation line.
