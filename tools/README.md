# Tools

Three single-file, dependency-free pages that run entirely in the browser, with no
account, no server and no data leaving the machine. Each works both online and as
a local file.

## regulatory-profile.html — Tool 01, interactive law selector

**[▸ Open the Regulatory Profile Selector](regulatory-profile.html)**

Users **tick the laws that apply to them**: NIS2, GDPR, DORA, CRA, CER, and national acts such as Denmark's
NIS 2-loven and Lov om styrket beredskab i energisektoren. All regulatory
references in the page show or hide to match the selected profile, and
"Print / save PDF" exports a tailored document.

### Hosting
- Works locally: just open the file in a browser.
- For teams: enable **GitHub Pages** on this repo. The tool is then available
  at `https://<org>.github.io/<repo>/tools/regulatory-profile.html`,
  and for this project at <https://opencdc.org/tools/regulatory-profile.html>.

### Law tagging convention for contributors

Two layers keep the framework filterable:

1. **HTML tool:** any element carries `data-law="nis2 gdpr dk-energi"`, and
   it is visible if ANY of its tagged laws is selected.
2. **Markdown docs:** law-specific sentences carry an HTML comment tag such as
   `<!-- law:nis2 -->` or `<!-- law:dk-nis2 -->`. These are invisible on GitHub
   but machine-readable, so future tooling can filter the plain docs the same way.
   Roadmap v1.1 has a build script that generates per-profile Markdown and PDF.

### Law IDs
`nis2` `gdpr` `dora` `cra` `cer` for EU-wide instruments ·
`dk-nis2` `dk-energi` `dk-tele` `dk-cer` `dk-fin` for Denmark ·
National implementations use `<iso2>-nat`, such as `de-nat` or `fr-nat`, one tag per member state.
Denmark is tagged per act, as `dk-nis2`, `dk-energi`, `dk-tele`, `dk-cer` and `dk-fin`, for the
reference example; contributors adding the same granularity for another country should
follow the pattern `<iso2>-<shortname>`.

## skill-matrix.html — Tool 02, team skill matrix

**[▸ Open the Team Skill Matrix](skill-matrix.html)**

**Maps the skills of a CDC/SOC team.**
Team members each fill in the self-assessment sheet,
either [`templates/skill-self-assessment.xlsx`](../templates/skill-self-assessment.xlsx)
or the [CSV version](../templates/skill-self-assessment.csv), and send it back;
the manager drops the returned files onto the page and gets:

- a **team heatmap** of people against 50 skills in 8 domains, with per-skill coverage,
  *bus factor 1* and *nobody proficient* flags, and mentor markers;
- a **gap analysis** against editable per-role target levels, with defaults derived
  from [`docs/12-roles-and-competences.md`](../docs/12-roles-and-competences.md);
- an **actions view**: whom to train, taking gap and motivation first, which in-house
  mentor pairings close gaps for free, and which skills to hire or buy;
- **snapshot export and import** as JSON, to archive review rounds.

Uploads are cumulative and keyed by the person's name: re-uploading a sheet for
the same person **overwrites their previous answers**, so the picture always
reflects the latest round. All data stays in the manager's browser
localStorage; nothing leaves the page. Skill data is personal data under
GDPR: collect it transparently, use it for development only, keep access limited.

### File format for contributors

The tool reads `.xlsx` natively, using zip plus XML via the browser's built-in
`DecompressionStream`, no libraries, and `.csv`. Parsing is positional-free:
it locates the header row containing `Skill ID`, then matches rows by skill ID
from `GV-01` to `PF-05`, takes the first digit 0–3 found in the level column, and
reads `Name` / `Role` / `Date` from labelled rows above the table. Keep the
skill IDs and the `Skill ID` header intact when translating or re-styling the
sheet. Everything else is free: column order, extra columns, formatting.
The catalogue and default role targets live in one JSON blob at the top of the
page's script. Edit there to localise or extend, and bump the version marker in
both the sheet and the tool if you change skill IDs.

### Hosting
- Works locally: just open the file in a browser, no internet needed.
- For teams: enable **GitHub Pages**. The tool is then available at
  `https://<org>.github.io/<repo>/tools/skill-matrix.html`,
  for this project <https://opencdc.org/tools/skill-matrix.html>, and the download
  links to the templates resolve automatically.

## maturity-assessment.html — Tool 03, interactive maturity self-assessment

**[▸ Open the Maturity Self-Assessment](maturity-assessment.html)**

Turns [`assessments/maturity-self-assessment.md`](../assessments/maturity-self-assessment.md)
into something you actually fill out, instead of a markdown checklist whose
boxes cannot be ticked in the browser. All 60 criteria across the
six CSF functions get a status of their own and an optional evidence field.

The layout is a workspace, in the spirit of the SIM3 self-assessment tool:
criteria on the left, one tab per function showing its level and progress, and
a results panel on the right that stays in view and updates on every click.
The results panel has three views: the score chart (click a function to open
it), the Result table, and **Open actions**, the criteria still missing to reach
your targets, each of which jumps straight to the criterion. On a phone the
results sit below the criteria, with a summary bar pinned to the bottom of the
screen.

- **Five-point status per criterion** — not considered / planned / partially in
  place / implemented / implemented & evidenced, so work in flight is visible
  without distorting the score. A toggle switches between counting
  "implemented" and the stricter evidence-based reading that counts only
  "implemented & evidenced". See the status scale in
  [`docs/08-maturity-model.md`](../docs/08-maturity-model.md).
- **Staged auto-scoring**, exactly as the maturity model defines it: a function
  reaches Level *N* only when every criterion at *N* and every level below it is
  met, with no averaging up. The three lower states never move the level; they drive
  a separate progress view instead: a hatched segment on the score chart showing
  how far into the next level the function has come, and a per-function
  breakdown in the Result table.
- **Owner and due date per criterion.** Every gap can carry who owns it and by
  when; the Open actions list shows them, counts the gaps still without an owner,
  and **exports the action plan as a spreadsheet file** (semicolon-separated
  with a byte-order mark, so it opens in columns in Excel, including Danish and
  other comma-decimal locales).
- **Target profiles** from [`docs/08-maturity-model.md`](../docs/08-maturity-model.md)'s
  target-setting table, covering SME, NIS2 important and essential, and critical infrastructure,
  pre-fill a target per function, individually adjustable.
- **Score chart** — current level vs. target, per function, plus a Result table
  and an Open actions list showing exactly which unmet criteria stand between
  you and your targets.
- **Resume link** — the full assessment, meaning answers, evidence notes, targets and
  the header fields, is encoded into the page's URL fragment, so the address bar
  always holds a unique link that restores exactly the current state. Copy it,
  mail it to yourself or paste it into a ticket, and continue later on any
  device or browser, with no account, no cookie and no server. The fragment is never
  sent in an HTTP request, so the data stays with whoever holds the link.
- **Snapshot export and import** as JSON, so you can date and keep assessments in
  version control to track the trend, per the reassessment cadence in the
  maturity model doc. Prefer this over the link for long-term archiving, and
  for assessments with long evidence notes, since links past ~2 000 characters are
  mangled by some mail clients, and the tool warns when that happens.

All data stays in the browser, in localStorage plus the resume link. Nothing is
sent anywhere.

### Hosting
- Works locally: just open the file in a browser, no internet needed.
- For teams: enable **GitHub Pages**. The tool is then available at
  `https://<org>.github.io/<repo>/tools/maturity-assessment.html`,
  and for this project at <https://opencdc.org/tools/maturity-assessment.html>.

### File format for contributors

Criteria are embedded as one JSON blob at the top of the page's script, in the
same order as `assessments/maturity-self-assessment.md`. If you edit the
criteria text in that document, mirror the change in the tool's embedded data
and vice versa. The two are meant to read identically; there is currently no
build step that generates one from the other.
