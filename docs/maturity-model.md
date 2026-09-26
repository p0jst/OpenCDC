# Maturity Model

<p class="src" markdown><span class="src-tag ocdf">OCDF</span>This framework's model, informed by the NIST CSF tiers and CMMI. Not a certification standard.</p>

## Design

The OCDF maturity model defines **four levels**, applied to each of the six CSF functions. The level names and philosophy are informed by the NIST CSF 2.0 **Tiers** of Partial, Risk Informed, Repeatable and Adaptive, and by the general structure of CMMI-style capability maturity models; teams already using Rob van Os's **SOC-CMM** will find the levels easy to cross-map.

We deliberately use four levels rather than five: in practice the difference between "defined" and "quantitatively managed" is where most models lose their audience.

## The levels

| Level | Name | One-line test |
|-------|------|---------------|
| **1** | Initial | "It happens when someone remembers." Activities are reactive, undocumented, person-dependent. |
| **2** | Managed | "It's written down and someone owns it." Core processes documented, approved, and executed; coverage partial. |
| **3** | Established | "It's measured and consistent." Processes are integrated, coverage is broad, metrics exist, and output of one function feeds another. |
| **4** | Optimising | "It improves itself." Data-driven, validated, trended; lessons systematically change the system. |

The scored criteria for every function live in one place, the [maturity self-assessment](../assessments/maturity-self-assessment.md); the [interactive tool](../tools/maturity-assessment.html) carries the same text. The function documents link there rather than keeping their own copy.

**Level 2 is also the NIS2 floor.** The Level 2 criteria include the minimum form of every measure NIS2 Art. 20 and 21 require, marked with the article they serve. An entity in NIS2 scope should treat Level 2 in every function as the least it can defend, whatever its target; see the [NIS2 Article 21 crosswalk](nis2-article-21-crosswalk.md).

## Relationship to tiers

Tier, set in [implementation tiers](tiers.md), selects *which* capabilities apply; maturity measures *how well* you run the selected set. Score only capabilities at or below your tier, and write "above tier" in the evidence field of a criterion that belongs to a higher tier, so a reader can tell a deliberate choice from a gap. Two limits apply: a criterion that carries the NIS2 floor is never above tier for an entity in scope, and a function only reaches a level when all its criteria at that level are met, so an above-tier criterion caps that function's level. Set the function's target below that level.

## Scoring method

1. For each function, work through its criteria in the [self-assessment checklist](../assessments/maturity-self-assessment.md) or the [interactive tool](../tools/maturity-assessment.html).
2. Score each criterion on the five-point status scale below rather than as a yes/no tick.
3. A level is achieved only when **all** criteria of that level and the levels below are met. That is "staged" scoring, with no averaging up.
4. Record evidence for each criterion: documents, screenshots, metric exports. In the author's experience, an assessment without recorded evidence tends to come out about a level higher than one that has to show its evidence. That is an observation, not a measured figure.
5. Plot the six function scores as a radar/spider profile. **A balanced Level 2 beats a spiky profile with Level 4 detection and Level 1 governance.** The functions depend on each other: excellent detection is wasted without the authority to contain, the reporting path to meet the legal clock, or the backups to recover. A weak function caps what the strong ones can deliver.

### Criterion status scale

A binary tick answers "is this done?" and nothing else. It cannot tell a
capability nobody has considered from one that is three weeks from delivery,
and both look identical in a board report. Score each criterion on five states
instead:

| Status | Meaning | Counts towards the level? |
|--------|---------|---------------------------|
| **Not considered** | Not looked at; no decision taken either way. | No |
| **Planned** | Agreed and scheduled, not yet started. | No |
| **Partially in place** | In place for part of the estate, or done informally / inconsistently. | No |
| **Implemented** | In place and operating across the intended scope. | **Yes** |
| **Implemented & evidenced** | Implemented, with evidence recorded and, where the criterion says so, signed off or reviewed within the stated period. | **Yes** |

The three lower states never move the score. They exist so that progress is
visible between assessments: a function sitting at Level 2 with four Level 3
criteria *planned* is in a different position from one at Level 2 with four
*not considered*, and the improvement backlog should say so. Resist the urge to
average them into a percentage. Partial credit is exactly how a spiky profile
gets reported as a healthy one. Report them as counts, such as "three of five Level 3
criteria met, one partly in place", never as a weighted score.

**Evidence-based scoring.** Counting only *implemented & evidenced* is the
stricter reading, and the one to use when the assessment will be shown to an
auditor, a regulator or a board. Expect it to lower a first self-assessment, often by a
level in the author's experience; that gap is the point, not a failure of the method. The
[interactive tool](../tools/maturity-assessment.html) has a toggle for both
readings, and a criterion's status travels with its evidence note.

## Target-setting guidance

| Organisation type | Suggested target profile |
|-------------------|--------------------------|
| SME, low regulatory exposure | Level 2 across all functions |
| NIS2 *important* entity | Level 2 across all functions as the floor, with RESPOND at 3 for the reporting deadlines |
| NIS2 *essential* entity / DORA financial entity | Level 3 across all functions |
| Critical infrastructure, high-threat sectors | Level 3–4, prioritising DETECT/RESPOND at 4 |

Targets are risk decisions. Set them in GOVERN, with executive sign-off. Above the legal floor at Level 2, the difference between the rows is exposure and scrutiny, not law: essential entities are supervised before the fact, and the sectors in the last row are the ones attackers pick.

### Coverage hours are a target, not a level

How many hours a day someone watches the alerts is a risk decision, not a measure of maturity. An 8×5 team with tested on-call and strong engineering can be better run than a 24/7 line that only forwards tickets. The criteria therefore ask whether coverage hours **meet the target you set**, not whether they are 24/7.

Set the target in GOVERN alongside the maturity targets, and record it in the charter's service table:

| Organisation type | Typical coverage-hours target |
|-------------------|-------------------------------|
| SME, low regulatory exposure | Business hours, with on-call or an MSSP out of hours |
| NIS2 *important* entity | Out-of-hours detection of serious alerts by MSSP, NOC or on-call, with a responder who can start the 24 h early-warning process at any hour |
| NIS2 *essential* entity / DORA financial entity | 24/7 detection, in-house or hybrid, with a named responder reachable around the clock |
| Critical infrastructure, high-threat sectors | 24/7 detection and 24/7 response authority, including for OT boundary events |

National or sector law can set the floor for you: Danish energy-sector entities at preparedness levels 4 and 5, for example, have a statutory duty to monitor and respond in real time; see the [Danish annex](annexes/annex-dk.md). Where the law sets it, the target is not a choice.

## Reassessment cadence

- Full assessment: **annually**, or after major organisational change.
- Progress review on open improvement actions: **quarterly**.
- Track the score trend, not just the snapshot. The improvement *rate* is itself a Level 4 indicator.

## Relationship to other models

| Model | Relationship |
|-------|--------------|
| **NIST CSF 2.0 Tiers** | OCDF levels are function-scoped rather than organisation-scoped, but philosophically aligned, Tier 1↔L1 through Tier 4↔L4. |
| **SOC-CMM** | Much finer-grained, with 5 domains, ~25 aspects and continuous scoring. Recommended as a deep-dive follow-up once OCDF assessment identifies weak functions. To reuse an existing SOC-CMM assessment, see the mapping below. SOC-CMM © Rob van Os, available free at soc-cmm.com. |
| **CMMI** | Conceptual ancestor of all staged maturity models; not security-specific. |
| **ENISA CSIRT Maturity Framework** | Focused on national/sectoral CSIRTs; relevant if your CDC provides CSIRT services externally. Based on the Open CSIRT Foundation's SIM3. |

## Comparing with other organisations

The [self-assessment tool](../tools/maturity-assessment.html) can compare your
scores with other organisations of the same size, NIS2 category or region, using
contributions from its users, published only as aggregates. The comparison is context, not a target:
set targets from your own risks, as above. How it works, what a contribution
contains, and what other published surveys have found in the meantime:
[community benchmark](benchmark.md).

## Reusing an existing SOC-CMM or SIM3 assessment

Many teams arrive at OCDF with an assessment they have already paid for, in time or money. It should not be thrown away. The mappings below let you carry its evidence across and use its results as a starting hypothesis for the OCDF scores.

### SOC-CMM → OCDF

SOC-CMM groups its aspects into five domains. The table maps each aspect to the OCDF capabilities and documents where the same ground is covered.

| SOC-CMM domain | SOC-CMM aspect | OCDF capabilities | Where in OCDF |
|----------------|----------------|-------------------|---------------|
| Business | Business drivers | GV-2, ID-3 | [Govern](govern.md), [Identify](identify.md) |
| Business | Customers | GV-1, GV-7 | [Govern](govern.md) |
| Business | Charter | GV-1 | [Charter template](../templates/cdc-charter-template.md) |
| Business | Governance | GV-4, GV-5, GV-7 | [Govern](govern.md) |
| Business | Privacy & policy | GV-3, PR-3 | [Govern](govern.md), [EU regulatory landscape](eu-regulatory-landscape.md) |
| People | Employees | GV-5 | [Roles & competences](roles-and-competences.md) |
| People | Roles & hierarchy | GV-4 | [Operating models](operating-models.md), [Roles & competences](roles-and-competences.md) |
| People | People management | GV-5 | [Roles & competences](roles-and-competences.md), [Running the CDC](cdc-operations.md) |
| People | Knowledge management | RS-2 | [Running the CDC](cdc-operations.md), [CSIRT community layer](csirt-community.md) |
| People | Training & education | GV-5 | [Roles & competences](roles-and-competences.md), [team skill matrix](../tools/skill-matrix.html) |
| Process | SOC management | GV-7, RC-5 | [Running the CDC](cdc-operations.md) |
| Process | Operations & facilities | GV-5, PR-1 | [Operating models](operating-models.md), [Running the CDC](cdc-operations.md), [CIA triad: the CDC applies it to itself](cia-triad.md#6-the-cdc-applies-the-triad-to-itself) |
| Process | Reporting & communication | GV-7, RS-5, RC-4 | [Metrics & KPI template](../templates/metrics-kpi-template.md) |
| Process | Use case management | DE-2, DE-4 | [Detect](detect.md), [Detection use case template](../templates/detection-use-case-template.md) |
| Process | Detection engineering & validation | DE-2, DE-6 | [Detection-as-code deep dive](detection-as-code-deep-dive.md) |
| Technology | SIEM / analytics tooling | DE-1, DE-2 | [Detect](detect.md) |
| Technology | IDPS and network tooling | DE-7, PR-6 | [Detect](detect.md), [Protect](protect.md) |
| Technology | Automation & orchestration | RS-4 | [Running the CDC](cdc-operations.md) |
| Services | Security monitoring | DE-1, DE-3, DE-4 | [Detect](detect.md) |
| Services | Security incident management | RS-1 to RS-7 | [Respond](respond.md) |
| Services | Security analytics and forensics | RS-3, DE-3 | [Respond](respond.md), [Playbooks](../playbooks/README.md) |
| Services | Threat intelligence | ID-5 | [CTI deep dive](cti-deep-dive.md) |
| Services | Threat hunting | DE-5 | [Detect](detect.md) |
| Services | Vulnerability management | ID-4, PR-5 | [Identify](identify.md), [Protect](protect.md) |
| Services | Log management | DE-1 | [Detect](detect.md) |

*Aspect names are paraphrased from SOC-CMM 2.x and may differ from the current release; consult soc-cmm.com for the authoritative list. OCDF's RECOVER function has no close SOC-CMM equivalent, so score it directly.*

**Translating scores, as a rough guide only.** SOC-CMM scores maturity continuously from 0 to 5; OCDF uses four staged levels. As a starting hypothesis, an aspect scoring below 1.5 suggests OCDF Level 1, 1.5 to 2.5 suggests Level 2, 2.5 to 3.5 suggests Level 3, and above 3.5 suggests Level 4. This translation is not calibrated against real paired assessments. Two cautions apply:

- **Take the lowest, not the average.** OCDF scoring is staged. If a function maps to several SOC-CMM aspects, the weakest one is the best predictor of the OCDF level.
- **Carry the evidence, then re-score.** The value of an earlier assessment is its evidence: documents, interviews, metric exports. Attach that evidence to the OCDF criteria and score the criteria directly. Do not report a translated number as an OCDF score.

### SIM3 and CIS Controls

- **SIM3**, for teams with a TF-CSIRT or ENISA-style assessment: the crosswalk is in the [CSIRT community layer](csirt-community.md), section 3. SIM3's emphasis on documented, reviewed and independently verified process maps most closely to the *implemented & evidenced* status above.
- **CIS Controls**, for teams with a CIS IG1–IG3 self-assessment: see the [CIS Controls crosswalk](cis-controls-crosswalk.md).

## Sources

- NIST CSF 2.0, CSWP 29: Tiers concept. https://doi.org/10.6028/NIST.CSWP.29
- R. van Os, *SOC-CMM: Capability Maturity Model for Security Operations Centers*. https://www.soc-cmm.com
- ENISA, *CSIRT Maturity Framework*. https://www.enisa.europa.eu
- Open CSIRT Foundation, *SIM3 v2 interim: Security Incident Management Maturity Model*, 2023. https://opencsirt.org/csirt-maturity/sim3-and-references/
- CMMI Institute, *Capability Maturity Model Integration*.

*Open CDC Framework, licensed CC BY 4.0. Credits: [References & credits](references.md).*
