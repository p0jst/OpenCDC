# Open CDC Framework

A free, vendor-neutral framework for building and running the team that detects and responds to cyber attacks in European organisations, whether that is a 24/7 Cyber Defence Center or two people in IT who also look after security.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![Version](https://img.shields.io/badge/version-v1.3.0-blue)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen)

**Read it as a website: <https://opencdc.org/>**, with search, the interactive tools and template downloads. This repository is the source.

## What it is

NIST CSF 2.0 describes what good security covers, and NIS2, DORA and GDPR say what European organisations must do. None of them says how to set up the team that does the work, who decides what, or how to tell whether it works. OCDF fills that gap.

- **Six functions**, following NIST CSF 2.0, from GOVERN to RECOVER, each broken into capabilities with IDs such as `DE-2`.
- **Three tiers**, Essential, Standard and Advanced, so a small team can see what matters now and what can wait.
- **Four maturity levels**, scored criterion by criterion with evidence. Level 2 in every function also covers the NIS2 minimum.
- **EU law built in**: NIS2, GDPR, DORA, CRA, CER and the AI Act, with an annex for each of the 27 member states.
- **Templates and browser tools** to turn it into documents you keep: a charter, an incident response plan, a scored baseline, a staffing case.

The framework calls the work a *CDC*, whatever the team is called and however small it is.

## Where to start

| You are | Start with |
|---------|-----------|
| A small IT-security team of one to three people | [If you are the whole security function](docs/tiers.md#if-you-are-the-whole-security-function), then the [first 90 days](docs/start-here.md) |
| A CISO, board member or sponsor | The 30-minute [executive guide](docs/executive-guide.md) and the [worked example](docs/worked-example.md) |
| Building a SOC or CDC | The seven steps below, with [operating models](docs/operating-models.md) for the staffing and budget case |
| Running one already | The [maturity self-assessment](tools/maturity-assessment.html), reusing any SOC-CMM, SIM3 or CIS assessment you have |
| An analyst or engineer | [Alert triage](docs/alert-triage.md), [detection-as-code](docs/detection-as-code-deep-dive.md), the [CTI deep dive](docs/cti-deep-dive.md) and the [playbook templates](templates/scenario-playbook-template.md) |
| In compliance or legal | The [EU regulatory landscape](docs/eu-regulatory-landscape.md), the [NIS2 Article 21 crosswalk](docs/nis2-article-21-crosswalk.md) and your [national annex](docs/annexes/README.md) |

New to the terms? [OCDF on one page](docs/one-page.md) explains them in five minutes.

## The seven steps

The same path as *Start building* on [the website](https://opencdc.org/#start-building). Each step leaves you with something you keep.

1. **Choose your tier** in [implementation tiers](docs/tiers.md). In NIS2 scope, read [the legal floor](docs/tiers.md#the-legal-floor) first.
2. **Run the design workshops** with the [design navigator](assessments/cdc-design-navigator.md), one per function, and log the gaps.
3. **Adopt the charter** from the [charter template](templates/cdc-charter-template.md), with containment authority signed.
4. **Decide the operating model** in [operating models](docs/operating-models.md), with the staffing numbers.
5. **Work the first 90 days** in [start here](docs/start-here.md); steps 2 to 4 are its first weeks.
6. **Assess where you are** at day 90 with the [maturity self-assessment](tools/maturity-assessment.html), and give every gap an owner and a date.
7. **Set the operating rhythm** with the [annual calendar](templates/annual-calendar-template.md) and a growing [detection portfolio](templates/detection-use-case-template.md).

Then reassess once a year.

## What is in this repository

| Folder | Contents |
|--------|----------|
| [`docs/`](docs/README.md) | The framework: the six functions, the lenses, operations, deep dives and the regulatory layer. [All documents in reading order](docs/README.md) |
| [`docs/annexes/`](docs/annexes/README.md) | One annex per EU member state, each with its review date and confidence. Edited in `countries.json` |
| [`assessments/`](assessments/) | The design navigator and the maturity self-assessment checklist, the single source of the criteria |
| [`templates/`](templates/README.md) | Charter, IR plan, playbooks, use case, KPI catalogue, job description, MSSP checklist, containment catalogue, controls register, annual calendar and the skill self-assessment sheet |
| [`tools/`](tools/README.md) | Three browser tools, plus the scripts that build diagrams and country data and check consistency |
| `site/`, `overrides/`, `mkdocs.yml` | The website build |

### The browser tools

Each tool is a single HTML file. It runs in your browser, needs no account, and sends nothing anywhere. Use them on the website or open the file from a local copy.

- [Maturity self-assessment](tools/maturity-assessment.html): score every criterion, see the level per function against your target, and keep a link or file to resume later.
- [Regulatory profile selector](tools/regulatory-profile.html): tick the EU and national laws that apply and get the reporting duties and references that match.
- [Team skill matrix](tools/skill-matrix.html): load the team's filled self-assessment sheets and get a heatmap, the gaps against role targets, and who to train, mentor or hire.

## Scope and limits

OCDF covers enterprise IT: endpoints, servers, identity, cloud and SaaS. It is not written for OT/ICS, telco core networks or classified environments; [About](ABOUT.md) explains why, and [the IT/OT interface](docs/it-ot-interface.md) covers what the CDC owns at that boundary.

It is not legal advice. The regulatory content has not had independent legal review, and some national annexes still carry verification flags. [Why trust this framework](docs/trust.md) marks which statements are law, which are standards and which are the author's judgement.

## Build the website locally

```
pip install -r requirements-site.txt
python tools/check_consistency.py
python site/build_site.py
mkdocs serve
```

## Citing

> Open CDC Framework (OCDF), version 1.3.0, 2026. Licensed CC BY 4.0. Available at: https://github.com/p0jst/OpenCDC.

What changed in each version is in the [changelog](CHANGELOG.md).

## Contributing and security

Contributions, corrections and national-law mappings are welcome; see [Contributing](CONTRIBUTING.md). To report a security problem in the website or the tools, see [Security](SECURITY.md) rather than opening a public issue.

## About

Written by Frederik B. Krogsgaard, formerly Senior Manager at the Norlys Cyber Defence Center, after a decade in the field and four years building and running a 24/7 CDC. GitHub account p0jst is his. The full story and how the project is maintained: [About](ABOUT.md).

## License

Licensed under [Creative Commons Attribution 4.0 International](LICENSE). OCDF builds on public work by NIST, ENISA, MITRE, FIRST and others, and is not endorsed by or affiliated with any of them. Every source is credited in [references & credits](docs/references.md).
