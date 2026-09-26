# Open CDC Framework

**An open source framework for building and maturing Security Operations Centers (SOC) and Cyber Defence Centers (CDC) across the European Union.**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![Version](https://img.shields.io/badge/version-v1.1.0-blue)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen)

**📖 Read the framework as a website: <https://opencdc.org/>** for searchable docs, interactive tools and template downloads.

---

> **Scope:** this framework targets **enterprise IT environments**: endpoints, servers, identity, cloud and SaaS. Governance, maturity and response apply to all of them, but the technical depth is uneven: the platform playbooks cover Windows, macOS and Linux, while cloud control planes and Microsoft 365 are only covered in general terms until the cloud profile on the [roadmap](ROADMAP.md) ships. It is **not** designed for OT/ICS, telco core networks, or classified environments; see [About](ABOUT.md) for the reasoning, [what still applies if you run critical infrastructure](ABOUT.md#if-you-run-critical-infrastructure), and the OT profile on the roadmap.

## Why this framework exists

European organisations face a unique combination of pressures: a rapidly evolving threat landscape, a dense regulatory environment of NIS2, DORA, GDPR and CRA, and a persistent shortage of skilled security personnel. Many teams are asked to "build a SOC" with little guidance on where to start, or to "mature" an existing capability without a shared yardstick for what maturity means.

The Open CDC Framework provides a **free, vendor-neutral, community-maintained blueprint** for:

1. **Building** a Cyber Defence Center from the ground up.
2. **Maturing** an existing SOC/CDC against a structured maturity model.
3. **Aligning** operations with the NIST Cybersecurity Framework (CSF) 2.0 and EU regulatory obligations.
4. **Anchoring** every capability in the CIA triad: Confidentiality, Integrity and Availability.

## Framework structure

The framework is organised around the **six functions of NIST CSF 2.0**, each mapped to the CIA triad and to EU regulatory requirements:

| Function | Question it answers | Doc |
|----------|--------------------|-----|
| Introduction & Design Principles | How do I use this framework? | [Introduction](docs/introduction.md) |
| **GOVERN** | Who owns cyber risk, and how are decisions made? | [Govern](docs/govern.md) |
| **IDENTIFY** | What are we defending, and what threatens it? | [Identify](docs/identify.md) |
| **PROTECT** | How do we reduce the likelihood and impact of incidents? | [Protect](docs/protect.md) |
| **DETECT** | How do we find adversary activity quickly? | [Detect](docs/detect.md) |
| **RESPOND** | How do we contain and eradicate threats? | [Respond](docs/respond.md) |
| **RECOVER** | How do we restore services and learn? | [Recover](docs/recover.md) |

Cross-cutting documents, in reading order:

| Document | What it gives you |
|----------|-------------------|
| [CIA Triad as a Design Lens](docs/cia-triad.md) | How Confidentiality, Integrity and Availability drive every CDC decision |
| [Maturity Model](docs/maturity-model.md) | Four maturity levels with concrete criteria per function, and how to reuse an existing SOC-CMM, SIM3 or CIS assessment |
| [Start Here: Prioritisation](docs/start-here.md) | The first 90 days and first year, in order, with exit criteria and anti-priorities |
| [Implementation Tiers](docs/tiers.md) | Essential / Standard / Advanced overlay: which capabilities apply at your size |
| [Operating Models](docs/operating-models.md) | MSSP vs tiered vs capability-based, plus shared and community CDCs: trade-offs, what can never be outsourced, and the staffing arithmetic and cost template for the budget round |
| [Roles & Competences](docs/roles-and-competences.md) | CDC roles, skills matrix, career paths and hiring, built on the ENISA ECSF |
| [Running the CDC](docs/cdc-operations.md) | The loops that keep a live CDC improving: tuning, detection-as-code, team development, automation guardrails, tool discipline |
| [Deep Dive: Detection-as-Code](docs/detection-as-code-deep-dive.md) | Repo layout, rule YAML anatomy, CI/CD pipeline, honest ATT&CK coverage scoring, Advanced tier |
| [Deep Dive: CTI Capability](docs/cti-deep-dive.md) | Strategic/operational/tactical intelligence and the interfaces that feed the CDC, Advanced tier |
| [CSIRT Community Layer](docs/csirt-community.md) | RFC 2350, TF-CSIRT/FIRST, SIM3 crosswalk for certification, living documentation |
| [EU Regulatory Landscape](docs/eu-regulatory-landscape.md) | NIS2, GDPR, DORA, CRA, CER and ENISA mapped to CDC capabilities |
| [NIS2 Article 21 Crosswalk](docs/nis2-article-21-crosswalk.md) | Every NIS2 Art. 20, 21 and 23 obligation mapped to capabilities and to the Level 2 criteria that form the legal floor |
| [NIST CSF 2.0 Crosswalk](docs/csf-crosswalk.md) | The 22 CSF 2.0 categories mapped to OCDF capabilities |
| [CIS Controls Crosswalk](docs/cis-controls-crosswalk.md) | All 18 CIS Controls with concrete actions per control |
| [References & Credits](docs/references.md) | Every source used by this framework |

Practical assets:

- [`templates/`](templates/) — charter, IR plan, detection use case, KPI catalogue, ECSF job description, MSSP requirements checklist, containment action catalogue, controls register, annual operating calendar, skill self-assessment sheet in xlsx and csv.
- [`playbooks/`](playbooks/) — attack-based playbooks for identity compromise, business email compromise and ransomware (drafts for field review), IR + digital forensics playbooks for Windows 11 laptops, macOS laptops, Windows Server including domain controllers, and RHEL-class Linux servers, plus Microsoft and CISA baseline references.
- [`assessments/`](assessments/) — the Design Navigator, with its guiding questions per function, and the maturity self-assessment.
- [`tools/regulatory-profile.html`](tools/regulatory-profile.html) — interactive law selector: tick the laws that apply, covering EU instruments and all 27 member states, and the references show or hide to match. Host via GitHub Pages or open locally.
- [`tools/skill-matrix.html`](tools/skill-matrix.html) — team skill matrix: team members fill in the self-assessment sheet, the manager uploads the returned files and gets a skills heatmap, gap analysis against role targets, and train/mentor/hire recommendations. Host via GitHub Pages or open locally.
- [`tools/maturity-assessment.html`](tools/maturity-assessment.html) — interactive maturity self-assessment: score every criterion on a five-point status scale, get automatic staged scoring, a score-vs-target chart, a resume link that restores your progress on any device, and an exportable snapshot to track the trend over time. Host via GitHub Pages or open locally.
- [`docs/annexes/`](docs/annexes/) — national annexes for all 27 EU member states, status verified July 2026. Each annex shows when it was last verified, by whom, and when the next review is due.

## New readers

- [OCDF on one page](docs/one-page.md): every term in the framework, in five minutes.
- [Executive guide](docs/executive-guide.md): the 30-minute version for a CISO, board member or sponsor.
- [Worked example](docs/worked-example.md): the framework applied to a fictional 2,500-person company, from charter to first board report.
- [Why trust this framework](docs/trust.md): which statements are law, standard, guidance, this framework's design, or the author's experience.

## Who is this for?

- **CISOs and CDC/SOC directors** planning a new capability or a maturity programme.
- **SOC managers and team leads** looking for structure, templates, and metrics.
- **Public sector and critical infrastructure teams** in scope of NIS2 or DORA.
- **SMEs** that need a pragmatic, low-cost starting point.

## How to use it

The same seven steps as *Start building* on the [website](https://opencdc.org/#start-building), the one path through the framework:

1. **Choose your tier** in [implementation tiers](docs/tiers.md). Output: target tier. If you are in NIS2 scope, read [the legal floor](docs/tiers.md#the-legal-floor) first.
2. **Run the design workshops** in the [design navigator](assessments/cdc-design-navigator.md), one per function. Output: design gaps logged as backlog items.
3. **Adopt the charter** from the [charter template](templates/cdc-charter-template.md). Output: signed charter with containment authority.
4. **Decide the operating model** in [operating models](docs/operating-models.md). Output: target operating model and staffing numbers.
5. **Assess where you are** with the [maturity self-assessment tool](tools/maturity-assessment.html) or the printable [checklist](assessments/maturity-self-assessment.md). Output: scored baseline and an owned action plan.
6. **Work the first 90 days** in [start here](docs/start-here.md), with your [national annex](docs/annexes/README.md) and the [regulatory selector](tools/regulatory-profile.html). Output: day-90 exit criteria met.
7. **Set the operating rhythm** with the [annual calendar](templates/annual-calendar-template.md) and the [detection use case template](templates/detection-use-case-template.md). Output: annual calendar and a growing detection portfolio.

Then reassess annually, or after major organisational change, and review open actions quarterly.

## About the author & project

Written by a practitioner who spent a decade in the field, the last four of them building and running a 24/7/365 CDC, and fell into most of the holes this framework now warns about. The author is Frederik B. Krogsgaard, formerly Senior Manager at the Norlys Cyber Defence Center, and the GitHub account p0jst is his. The full story, what is deliberately out of scope, and how the project is maintained: [About](ABOUT.md).

## Contributing

This is a community project. Contributions, translations and national-regulation mappings are very welcome. See [Contributing](CONTRIBUTING.md).

## License

Documentation is licensed under [Creative Commons Attribution 4.0 International](LICENSE), CC BY 4.0.

This framework builds on publicly available works by NIST, ENISA, MITRE, FIRST and others. It is **not** endorsed by or affiliated with any of these organisations. All sources are credited in [references & credits](docs/references.md).
