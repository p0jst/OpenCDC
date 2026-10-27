# Publishing notes and maintainer checklist

Approved project name: Open CDC Framework (OCDF). "Framework" refers to the capability model; SOC leads in the subtitle and metadata for discoverability.

## GitHub repository settings
- Repository name: `OpenCDC`
- Description: "Open CDC Framework (OCDF): an open source framework for building and maturing security operations in the EU, from a two-person IT-security team to a full SOC / Cyber Defence Center. NIST CSF 2.0, CIA triad, NIS2/GDPR/DORA, maturity model, templates, all 27 national annexes."
- Topics: `soc` `security-operations-center` `cyber-defence-center` `csirt` `incident-response` `nist-csf` `nis2` `dora` `gdpr` `detection-engineering` `threat-intelligence` `maturity-model` `blue-team`
  Deliberately no `eu` topic: it is generic, carries enormous unrelated volume, and nobody browsing it is looking for a SOC framework. The European framing is already carried by `nis2`, `dora` and `gdpr`, which are specific enough that anyone arriving through them is in the audience.
- Enable: Pages with source "GitHub Actions", which publishes the website including tools/, plus Discussions and Issues.
  Discussions matter: `CONTRIBUTING.md` tells contributors to open one for field feedback on the maturity criteria.
- Social preview: upload `brand/github-social-preview.png` under **Settings → General → Social preview**. There is no API for this, so it has to be done in the web UI. The website's link previews use a separate card, `assets/social-preview.png`, referenced by the site's Open Graph tags in `overrides/main.html`. Regenerate either if the stat counts change.

## Release history
- `v1.0.0` — 2026-09-02. First stable release.
- `v1.1.0` — 2026-09-23. Usability and scoring release; two DETECT criteria changed.
- `v1.2.0` — 2026-10-11. Review release: criteria set 2 with the NIS2 legal floor at Level 2, 71 criteria; incident handling on DAIR; the IT/OT interface; alert triage and AI in the CDC; the first diagrams; plainer front page and README.
- `v1.3.0` — 2026-10-27. Minor release: security fix for the maturity tool's file import and a pinned website build; vulnerability handling built for exploitation speed, with edge devices under PR-5 and a reworded IDENTIFY L3 criterion; end-to-end check of links, annexes and tools; one path through the framework; references updated and SANS 2026 research applied.

## Community benchmark

- Create the mailbox benchmark@opencdc.org on the opencdc.org domain before announcing the benchmark. The tool and the benchmark page already point to it; the address is set in one place, `BENCH_EMAIL` in `tools/maturity-assessment.html`.
- How to handle contributions: [benchmark contributions guide](benchmark/README.md).

## Outstanding before the next release
1. **Legal review of the reporting-deadline tables** and the national law references. Not done at v1.0.0; the release notes say so explicitly, and the site carries the "not legal advice" line on every page.
2. **Re-verify the flagged annexes** — the index still marks nine as pending or needing verification, FR, IE, LU, ES, PL and NL among them. National transposition of NIS2 is still moving, so this is recurring work rather than a one-off.
3. Announce on community channels before broadcast channels.

## Website platform: Material for MkDocs end of life

Material for MkDocs is in maintenance: its own build notice says critical fixes and security updates continue until 5 May 2027, and names Zensical, from the same team, as the successor. MkDocs 2.0 is announced as incompatible with every current theme and plugin. The site is protected from it for now, because `mkdocs-material` requires `mkdocs<2` and both build packages are pinned in `requirements-site.txt`.

Plan, to finish before May 2027:

1. **Test build on a branch, early 2027.** Install Zensical, build from the existing `mkdocs.yml`, and compare with the current site: page count, `tools/check_consistency.py`, a link check, and screenshots of the home page, one function page and one tool page at desktop and phone width.
2. **Check the three things this site depends on.** The redirects for old addresses, now from `mkdocs-redirects`; the template override in `overrides/main.html` for link previews; and `site/extra.css`, which relies on Material's HTML structure. If Zensical does not yet handle redirects, `site/build_site.py` can write the redirect pages itself.
3. **Switch the workflow** once the test build matches, and record it in the changelog. Keep `mkdocs.yml` rather than converting to Zensical's own format until that format is stable.

## Cutting a release
1. Update the version in seven places: the README badge and its citation line, the citation line in `docs/references.md`, the CHANGELOG heading, where you close `Unreleased` and date it, on the landing page `site/index.md` both the eyebrow line and the version line in the footer box, and `FRAMEWORK_VERSION` in `tools/maturity-assessment.html`, which goes into benchmark contributions and the printed assessment. Then add the release to the history above.
2. Push to `main`; confirm the Pages workflow deployed and the site is live.
3. Create the release on GitHub, tag `vX.Y.Z` targeting `main`, and paste the notes. Keep the status-and-limitations section; it is what stops a reader treating the regulatory content as audited.

Note: the name "OpenSOC" was considered and rejected due to existing use in the security community, namely Recon InfoSec's competition and the former Cisco/Apache Metron project, so do not abbreviate the project that way in materials.
