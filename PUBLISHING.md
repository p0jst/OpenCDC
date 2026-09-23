# Publishing notes — maintainer checklist

Approved project name: Open CDC Framework (OCDF). "Framework" refers to the capability model; SOC leads in the subtitle and metadata for discoverability.

## GitHub repository settings
- Repository name: `OpenCDC`
- Description: "Open CDC Framework (OCDF): an open source framework for building and maturing SOCs / Cyber Defence Centers in the EU. NIST CSF 2.0, CIA triad, NIS2/GDPR/DORA, maturity model, playbooks, all 27 national annexes."
- Topics: `soc` `security-operations-center` `cyber-defence-center` `csirt` `incident-response` `nist-csf` `nis2` `dora` `gdpr` `detection-engineering` `threat-intelligence` `maturity-model` `blue-team`
  Deliberately no `eu` topic: it is generic, carries enormous unrelated volume, and nobody browsing it is looking for a SOC framework. The European framing is already carried by `nis2`, `dora` and `gdpr`, which are specific enough that anyone arriving through them is in the audience.
- Enable: Pages with source "GitHub Actions", which publishes the website including tools/, plus Discussions and Issues.
  Discussions matter: `CONTRIBUTING.md` tells contributors to open one for field feedback on the maturity criteria.
- Social preview: upload `assets/social-preview.png` under **Settings → General → Social preview**. There is no API for this, so it has to be done in the web UI; the same image is served at `https://opencdc.org/assets/social-preview.png` and is referenced by the site's Open Graph tags in `overrides/main.html`. Regenerate it if the stat counts change.

## Release history
- `v1.0.0` — 2026-09-02. First stable release.
- `v1.1.0` — 2026-09-23. Usability and scoring release; two DETECT criteria changed.

## Community benchmark

- Create the mailbox **benchmark@opencdc.org** on the opencdc.org domain before announcing the benchmark. The tool and the benchmark page already point to it; the address is set in one place, `BENCH_EMAIL` in `tools/maturity-assessment.html`.
- How to handle contributions: [benchmark/README.md](benchmark/README.md).

## Outstanding before the next release
1. **Legal review of the reporting-deadline tables** and the national law references. Not done at v1.0.0; the release notes say so explicitly, and the site carries the "not legal advice" line on every page.
2. **Re-verify the flagged annexes** — the index still marks nine as pending or needing verification, FR, IE, LU, ES, PL and NL among them. National transposition of NIS2 is still moving, so this is recurring work rather than a one-off.
3. Announce on community channels before broadcast channels.

## Cutting a release
1. Update the version in six places: the README badge, the **Released** section of the ROADMAP, the citation line in `docs/19-references.md`, the CHANGELOG heading, where you close `Unreleased` and date it, and on the landing page `site/index.md` both the eyebrow line and the "How current is this" box. Then add the release to the history above.
2. Push to `main`; confirm the Pages workflow deployed and the site is live.
3. Create the release on GitHub, tag `vX.Y.Z` targeting `main`, and paste the notes. Keep the status-and-limitations section; it is what stops a reader treating the regulatory content as audited.

Note: the name "OpenSOC" was considered and rejected due to existing use in the security community, namely Recon InfoSec's competition and the former Cisco/Apache Metron project, so do not abbreviate the project that way in materials.
