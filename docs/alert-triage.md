# Designing alert triage

<p class="src" markdown><span class="src-tag ocdf">OCDF</span><span class="src-tag practitioner">Practitioner</span>This framework's design decisions for DE-3, from operating practice.</p>

> Triage is where detection meets response. DE-3 in [Detect](detect.md) asks for a documented triage process, and the verify-and-triage gate in [Respond](respond.md#verify-and-triage) says what triage must decide. This document covers the decisions a CDC has to make for that step to work the same way every time, whoever or whatever does the triage: a person on shift, a provider under Model A, or an automated pipeline.

Most triage problems are not analyst problems. They come from decisions nobody made: who may close what, what a closed alert must show, which outcomes exist and where each one goes next. Make the five decisions below once, write them into the triage runbook, and revisit them at the annual review.

## Decision 1: who may decide what

In a tiered model the answer is built into the structure. In a [capability-based model](operating-models.md) and in small teams it is not, so it has to be written down.

| Decision | Who should hold it | Notes |
|----------|-------------------|-------|
| Close an alert as false positive | Any analyst on the rota | Subject to sampled peer review, see decision 5 |
| Close an alert as true positive without impact | Any analyst, after a scoping check | The scoping check confirms that nothing else was reached |
| Defer an alert | Any analyst | Must name what is missing, who is getting it and when the next decision is due |
| Declare an incident and open the response loop | The analyst who found it, without asking permission | The incident manager then sets severity per IR plan §1 |
| Start the regulatory significance assessment | Legal or the DPO, informed by the analyst | Runs in parallel with verification, not after it; see [Respond](respond.md#verify-and-triage) |
| Auto-close without a human | Nobody by default | Only for named rules, as a suppression with owner, review sample and expiry; see [Running the CDC](cdc-operations.md) §4 |

Two points matter more than the rest. Declaring an incident must never require someone's permission, because that is how incidents wait in a queue overnight. And under Model A, the contract must say which of these decisions the provider holds and which come back to you; the [MSSP requirements checklist](../templates/mssp-requirements-checklist.md) is the place to settle it.

## Decision 2: the minimum triage record

A closed alert with no reasoning cannot feed tuning, cannot be peer reviewed, and cannot be defended to a regulator who asks when the organisation first had reasonable grounds. Decide what every triaged alert records. Eight questions make a workable minimum:

| # | Question | What it establishes | Typical sources | What the answer decides |
|---|----------|---------------------|-----------------|-------------------------|
| 1 | Who is involved? | The identity behind the activity, account state, privilege and owner | Identity provider, directory, privileged access records, joiner and leaver records | Whether a privileged, service or departed account raises priority |
| 2 | Where did it happen? | The endpoint, server, application or cloud tenant, and its criticality | Asset inventory per ID-1, crown-jewel list per ID-3, EDR, cloud console | Blast radius and which owner to involve |
| 3 | What happened? | The concrete event: logon, process, file or network activity | The raw event and the detection rule itself | Whether the rule fired for the reason it was written |
| 4 | What is different? | Deviation from normal for this identity, asset or peer group | Historical logs, behaviour baselines | Whether this is an anomaly or established behaviour |
| 5 | When did it happen? | Time and sequence, against working hours, change windows and maintenance | Change calendar, ticketing, log timestamps | Whether timing explains or aggravates the activity |
| 6 | What supports or contradicts it? | Corroborating and contradicting evidence | Related alerts, other log sources, threat intelligence | Confidence in the verdict |
| 7 | How did it get there? | The first visible steps of an attack chain, mapped to ATT&CK techniques | Process lineage, authentication history, network flows | Whether to look for earlier or later stages |
| 8 | Why does it matter? | Business and security impact if the activity is malicious | Crown jewels, data classification per ID-2, business impact | Urgency, and input to the regulatory assessment |

Triage answers question 7 only far enough to decide. Reconstructing the whole attack belongs to the response loop.

The same record applies when a machine does the triage. An automated or AI-assisted verdict that cannot answer these questions in the case is not a verdict; see [AI in the CDC](ai-in-the-cdc.md).

## Decision 3: one set of outcomes

Triage has three outcomes, defined in [Respond](respond.md#verify-and-triage): continue, stop or defer. Every case then closes under the [closure taxonomy](respond.md#case-closure-taxonomy). Use these two lists and no others, so that tuning, metrics and statistics count the same things.

| Triage outcome | Closes as | Next step |
|----------------|-----------|-----------|
| Continue | True positive with impact | Response loop; reporting duties assessed |
| Continue, with a scoping check | True positive without impact | Confirm nothing else was reached, then close; feed detection gaps back to DE-2 |
| Stop | False positive, reason *rule defect* | Close and flag for tuning |
| Stop | False positive, reason *benign activity* | The rule matched what it was written for, but the activity is legitimate; close, and if it recurs, an exception with owner and expiry |
| Defer | Indeterminate, if the time-box runs out | Record which data was missing; recurring gaps go to the log-source and detection backlog |

The reason field on false positives is what makes the tuning loop work. A rule defect is fixed in the rule. Benign activity is handled by a scoped exception, or accepted as noise the team has chosen to live with. Mixing the two hides which rules are broken.

## Decision 4: what to automate and what to keep

Not every question carries the same judgement. Decide per question where the answer comes from.

| Questions | Typical source of the answer | Why |
|-----------|------------------------------|-----|
| 1, 2, 5 | Enrichment, delivered inside the alert before a human looks at it | Lookups against inventory, identity and calendars; high value and low risk to automate |
| 3, 6 | Enrichment proposes, the analyst confirms | Machines gather related events well, but whether they belong together is a judgement |
| 4, 7, 8 | The analyst, assisted | These are the questions where context the systems do not hold decides the answer |

This split is the order of work in [Running the CDC](cdc-operations.md) §4: automate enrichment before decisions. A team that automates questions 4, 7 and 8 before 1, 2 and 5 has automated the wrong end.

## Decision 5: how triage quality is checked

Speed is easy to measure and easy to buy with shortcuts. Decide how quality is checked as well:

- **Peer review on a sample.** A fixed share of closed false positives, for example five per analyst per month, reviewed by a colleague against the triage record. In a one-person function, ask the provider or a peer organisation to review a sample each quarter.
- **Reopened cases.** The rate of cases stopped or deferred at triage that come back as incidents, already in the [metrics catalogue](../templates/metrics-kpi-template.md).
- **Time-box adherence.** Deferred cases that passed their next decision date without a decision. Each one is a potential problem with the legal clocks, which start at awareness.
- **Record completeness.** Share of closed alerts with all eight questions answered or explicitly marked not applicable.

## How team size changes this

| | One to three people | A dedicated CDC | A large or multi-team CDC |
|---|---------------------|-----------------|---------------------------|
| Who triages | Often the provider under Model A; you triage what it escalates | Analysts on a rota | Analysts on a rota, often with an automated first pass |
| What to write down first | Decision 1 and the provider's duty to deliver the triage record with every escalation | All five decisions in the triage runbook | All five, plus the rules for automated triage |
| The main risk | Nobody checks the closures, because there is nobody else | Inconsistent closures between analysts | Automation closing alerts nobody ever looks at |

## Triage record template

Copy into the case-management system as a form, or use as a checklist. Fields may be filled by enrichment, but a named person confirms the verdict.

```
Alert ID:
Detection rule:
Triaged by:                        Human / automated, reviewed by:
Triage started / decided:

1. Who:
2. Where:
3. What:
4. What is different:
5. When:
6. Supports or contradicts:
7. Chain indicators, ATT&CK techniques:
8. Impact if malicious:

Triage outcome:   continue / stop / defer
Closes as:        true positive with impact / true positive without impact /
                  false positive: rule defect / false positive: benign activity /
                  indeterminate
Reasoning:
If deferred: missing data, owner, next decision due:
Handed over to / tuning flag raised:
```

## Sources

- NIST CSF 2.0, CSWP 29: DE.AE adverse event analysis and RS.MA incident management. https://doi.org/10.6028/NIST.CSWP.29
- Joshua Wright, *Dynamic Incident Response*, SANS Institute, 2026, for the verify-and-triage gate this document builds on. https://dynamicincidentresponse.com
- MITRE ATT&CK®. https://attack.mitre.org
- The eight questions follow a widely used analyst checklist of who, what, where, when and impact, adapted here; no single original source is known.

*Open CDC Framework, licensed CC BY 4.0. Credits: [References & credits](references.md).*
