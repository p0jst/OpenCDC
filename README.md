# Open CDC Framework

**An open source framework for building and maturing Security Operations Centers (SOC) and Cyber Defence Centers (CDC) across the European Union.**

It is for the people who notice cyber attacks and deal with them, whether that is a 24/7 Cyber Defence Center or two people in IT who also run the servers. The framework calls that work a *CDC*, whatever the team is called and however small it is. [Is this for me?](#is-this-for-me)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![Version](https://img.shields.io/badge/version-v1.3.0-blue)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen)

**📖 Read the framework as a website: <https://opencdc.org/>** for searchable docs, interactive tools and template downloads.

---

> **Scope:** this framework targets enterprise IT environments: endpoints, servers, identity, cloud and SaaS. Governance, maturity and response apply to all of them, but the technical depth is uneven: cloud control planes and Microsoft 365 are only covered in general terms. It is *not* designed for OT/ICS, telco core networks, or classified environments; see [About](ABOUT.md) for the reasoning, [what still applies if you run critical infrastructure](ABOUT.md#if-you-run-critical-infrastructure), and [the IT/OT interface](docs/it-ot-interface.md) for what the CDC owns at the boundary.

## Why this framework exists

Teams are asked to "build a SOC" with little to go on, or to "mature" one without any shared idea of what maturity means. NIST CSF 2.0 describes what good security covers, and NIS2, DORA and GDPR say what European organisations are obliged to do. None of them says how to set up the team that does the work, who decides what, or how to tell whether it works.

OCDF tries to fill that gap. It is free, names no vendors, and is written for European law, with notes for all 27 member states. It follows the six CSF functions, says for each capability what it protects in terms of confidentiality, integrity and availability, and scores how well you run it on four maturity levels.

## Is this for me?

Probably, if part of your job is noticing attacks and dealing with them. You do not need a department called SOC or CDC. Every capability is marked with the smallest [tier](docs/tiers.md) it belongs to, so a team of two can see what matters now and what can wait.

| You are | Start here |
|---------|-----------|
| **A small IT-security team**, one to three people with other IT duties too | [If you are the whole security function](docs/tiers.md#if-you-are-the-whole-security-function), then the [first 90 days](docs/start-here.md) and the [regulatory selector](tools/regulatory-profile.html). Leave the deep dives for later |
| **A CISO, board member or sponsor** | The 30-minute [executive guide](docs/executive-guide.md), then the [worked example](docs/worked-example.md) |
| **Building a SOC or CDC**, in-house, with a provider, or both | The seven steps under [How to use it](#how-to-use-it), with [operating models](docs/operating-models.md) for the staffing and budget case |
| **Running one already** | The [maturity self-assessment](tools/maturity-assessment.html), reusing any SOC-CMM, SIM3 or CIS assessment you have, then [running the CDC](docs/cdc-operations.md) |
| **An analyst or engineer** | [Designing alert triage](docs/alert-triage.md), [detection-as-code](docs/detection-as-code-deep-dive.md), the [CTI deep dive](docs/cti-deep-dive.md) and the [playbook templates](templates/scenario-playbook-template.md) |
| **In compliance or legal** | The [EU regulatory landscape](docs/eu-regulatory-landscape.md), the [NIS2 Article 21 crosswalk](docs/nis2-article-21-crosswalk.md) and your [national annex](docs/annexes/README.md) |

New to the terms? [OCDF on one page](docs/one-page.md) explains them in five minutes. [Why trust this framework](docs/trust.md) says which statements are law, which are standards, and which are the author's own judgement.

## How to use it

The same seven steps as *Start building* on the [website](https://opencdc.org/#start-building), which is the one path through the framework:

1. **Choose your tier** in [implementation tiers](docs/tiers.md). Output: target tier. If you are in NIS2 scope, read [the legal floor](docs/tiers.md#the-legal-floor) first.
2. **Run the design workshops** in the [design navigator](assessments/cdc-design-navigator.md), one per function. Output: design gaps logged as backlog items.
3. **Adopt the charter** from the [charter template](templates/cdc-charter-template.md). Output: signed charter with containment authority.
4. **Decide the operating model** in [operating models](docs/operating-models.md). Output: target operating model and staffing numbers.
5. **Work the first 90 days** in [start here](docs/start-here.md); steps 2 to 4 are its first weeks. Use it with your [national annex](docs/annexes/README.md) and the [regulatory selector](tools/regulatory-profile.html). Output: day-90 exit criteria met.
6. **Assess where you are** at day 90 with the [maturity self-assessment tool](tools/maturity-assessment.html) or the printable [checklist](assessments/maturity-self-assessment.md). Output: scored baseline with evidence, and an action plan with owners.
7. **Set the operating rhythm** with the [annual calendar](templates/annual-calendar-template.md) and the [detection use case template](templates/detection-use-case-template.md). Output: annual calendar and a growing detection portfolio.

Then reassess annually, or after major organisational change, and review open actions quarterly.

## Framework structure

The framework is organised around the six functions of NIST CSF 2.0, each mapped to the CIA triad and to EU regulatory requirements:

| Function | Question it answers | Doc |
|----------|--------------------|-----|
| Introduction & design principles | How do I use this framework? | [Introduction](docs/introduction.md) |
| **GOVERN** | Who owns cyber risk, and how are decisions made? | [Govern](docs/govern.md) |
| **IDENTIFY** | What are we defending, and what threatens it? | [Identify](docs/identify.md) |
| **PROTECT** | How do we reduce the likelihood and impact of incidents? | [Protect](docs/protect.md) |
| **DETECT** | How do we find adversary activity quickly? | [Detect](docs/detect.md) |
| **RESPOND** | How do we contain and eradicate threats? | [Respond](docs/respond.md) |
| **RECOVER** | How do we restore services and learn? | [Recover](docs/recover.md) |

Cross-cutting documents, in reading order:

| Document | What it gives you |
|----------|-------------------|
| [CIA triad as a design lens](docs/cia-triad.md) | How Confidentiality, Integrity and Availability drive every CDC decision |
| [Maturity model](docs/maturity-model.md) | Four maturity levels with concrete criteria per function, and how to reuse an existing SOC-CMM, SIM3 or CIS assessment |
| [Implementation tiers](docs/tiers.md) | Essential / Standard / Advanced overlay: which capabilities apply at your size |
| [Start here: the first 90 days](docs/start-here.md) | The first 90 days and first year, in order, with exit criteria and anti-priorities |
| [Operating models](docs/operating-models.md) | MSSP vs tiered vs capability-based, plus shared and community CDCs: trade-offs, what can never be outsourced, and the staffing arithmetic and cost template for the budget round |
| [Roles & competences](docs/roles-and-competences.md) | CDC roles, skills matrix, career paths and hiring, built on the ENISA ECSF |
| [Running the CDC](docs/cdc-operations.md) | The loops that keep a live CDC improving: tuning, detection-as-code, team development, automation guardrails, tool discipline |
| [Designing alert triage](docs/alert-triage.md) | Who may decide what, the minimum triage record, one set of outcomes, what to automate, how quality is checked |
| [AI in the CDC](docs/ai-in-the-cdc.md) | Where AI helps and where to avoid it, by team size; AI in the adversary's hands; AI systems as assets; the AI Act |
| [Deep dive: detection-as-code](docs/detection-as-code-deep-dive.md) | Repo layout, rule YAML anatomy, CI/CD pipeline, honest ATT&CK coverage scoring; for Standard and Advanced tiers |
| [Deep dive: CTI capability](docs/cti-deep-dive.md) | Strategic/operational/tactical intelligence and the interfaces that feed the CDC; for Standard and Advanced tiers |
| [CSIRT community layer](docs/csirt-community.md) | RFC 2350, TF-CSIRT/FIRST, SIM3 crosswalk for certification, living documentation |
| [EU regulatory landscape](docs/eu-regulatory-landscape.md) | NIS2, GDPR, DORA, CRA, CER and ENISA mapped to CDC capabilities |
| [NIS2 Article 21 crosswalk](docs/nis2-article-21-crosswalk.md) | Every NIS2 Art. 20, 21 and 23 obligation mapped to capabilities and to the Level 2 criteria that form the legal floor |
| [NIST CSF 2.0 crosswalk](docs/csf-crosswalk.md) | The 22 CSF 2.0 categories mapped to OCDF capabilities |
| [CIS Controls crosswalk](docs/cis-controls-crosswalk.md) | All 18 CIS Controls with concrete actions per control |
| [References & credits](docs/references.md) | Every source used by this framework |

Practical assets:

- [`templates/`](templates/): the charter, IR plan, detection use case, KPI catalogue, ECSF job description, MSSP requirements checklist, containment action catalogue, scenario and platform playbook templates, controls register, annual operating calendar, and the skill self-assessment sheet as xlsx and csv.
- [`assessments/`](assessments/): the design navigator with its guiding questions per function, and the maturity self-assessment.
- [`tools/regulatory-profile.html`](tools/regulatory-profile.html): an interactive law selector. Tick the laws that apply, covering EU instruments and all 27 member states, and the references show or hide to match. Host via GitHub Pages or open locally.
- [`tools/skill-matrix.html`](tools/skill-matrix.html): the team skill matrix. Team members fill in the self-assessment sheet, the manager uploads the returned files and gets a skills heatmap, gap analysis against role targets, and train/mentor/hire recommendations. Host via GitHub Pages or open locally.
- [`tools/maturity-assessment.html`](tools/maturity-assessment.html): the interactive maturity self-assessment. Score every criterion on a five-point status scale, get automatic staged scoring, a score-vs-target chart, a resume link that restores your progress on any device, and an exportable snapshot to track the trend over time. Host via GitHub Pages or open locally.
- [`docs/annexes/`](docs/annexes/): national annexes for all 27 EU member states. Each annex shows when it was last reviewed, by whom, how confident that review is, and when the next one is due.

## About the author & project

Written by a practitioner who spent a decade in the field, the last four of them building and running a 24/7/365 CDC, and fell into most of the holes this framework now warns about. The author is Frederik B. Krogsgaard, formerly Senior Manager at the Norlys Cyber Defence Center, and the GitHub account p0jst is his. The full story, what is deliberately out of scope, and how the project is maintained: [About](ABOUT.md).

## Contributing

This is a community project. Contributions, translations and national-regulation mappings are very welcome. See [Contributing](CONTRIBUTING.md).

## License

Documentation is licensed under [Creative Commons Attribution 4.0 International](LICENSE), CC BY 4.0.

This framework builds on publicly available works by NIST, ENISA, MITRE, FIRST and others. It is *not* endorsed by or affiliated with any of these organisations. All sources are credited in [references & credits](docs/references.md).
