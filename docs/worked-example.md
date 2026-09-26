# Worked example: a CDC for a 2,500-person company

!!! warning "Fictional"
    Exempla Parcel A/S does not exist. The organisation, people and numbers below
    are invented to show the framework applied end to end. Use the structure; replace
    every figure with your own.

The rest of the framework says what to do. This page shows what it looks like
when one organisation does it: the decisions, the documents, and the first
quarter's results.

## The organisation

| | |
|---|---|
| **Business** | Parcel sorting and delivery, 14 sites in Denmark, sorting runs through the night |
| **People** | 2,500 employees, of which 4 in IT security today and no SOC |
| **Estate** | 2,000 laptops and desktops, 300 servers (on-premises virtualisation plus Azure), Microsoft 365 and Entra ID, 1,200 handheld scanners under mobile device management |
| **Out of scope** | The sorting-line control systems (OT), run by Operations; the CDC monitors the IT/OT boundary only |
| **Regulation** | NIS2 *important* entity (postal and courier services); GDPR; Danish NIS 2-loven, registered on virk.dk |
| **Budget** | Approved for a CDC of 6 people plus a managed service for nights and weekends |

## The decisions

**Tier: Standard.** A regulated, mid-to-large organisation that needs all six
functions measured, but not the validation and automation depth of Advanced.
See [implementation tiers](tiers.md).

**Operating model: A+C hybrid.** Worked through the
[decision path](operating-models.md#decision-path):

1. No log data is legally barred from leaving the company, so a provider is possible.
2. Sorting runs through the night, so an attack at 02:00 hits operations at
   once; noticing it at 07:00 would be too late. Out-of-hours detection is
   needed within six months.
3. Six approved posts cannot staff a 24/7 seat, which takes about 5.6 people on
   its own ([the arithmetic](operating-models.md#staffing-and-cost-the-arithmetic)).
   So a provider holds the watch from 17:00 to 07:00 and at weekends.
4. The four existing staff are senior, and the estate is mostly Microsoft cloud
   and automatable, so the daytime team is capability-based (Model C) rather than
   tiered.

**The team.** One CDC manager; three analysts who own cases from triage to
closure; one detection engineer; one analyst for threat intelligence and
vulnerabilities. Weekdays 07:00–17:00 there are two people on triage. The
analysts and the detection engineer share an on-call rota, one week in four, to
receive escalations from the provider at night.

**Maturity targets**, set with the executive board:

| Govern | Identify | Protect | Detect | Respond | Recover |
|--------|----------|---------|--------|---------|---------|
| 3 | 2 | 3 | 3 | 3 | 2 |

Detect and Respond at 3 because of the night operation and the reporting clock;
Govern and Protect at 3 because identity is the main attack path into a Microsoft
estate. Identify and Recover stay at 2 for year one, a decision recorded as an
accepted risk.

**Coverage-hours target:** out-of-hours detection by the provider, with an
internal responder reachable within 30 minutes around the clock. See
[coverage hours are a target, not a level](maturity-model.md#coverage-hours-are-a-target-not-a-level).

## The charter, as signed

An excerpt of the filled-in [charter template](../templates/cdc-charter-template.md).

**§3 Services**

| Service | Coverage hours | SLA |
|---------|---------------|-----|
| Security monitoring and triage | 24/7: CDC weekdays 07–17, provider otherwise | P1 acknowledged ≤ 15 min; provider escalates P1/P2 to on-call ≤ 15 min |
| Incident response | 24/7 via on-call | Responder engaged ≤ 30 min for P1 |
| Detection engineering | Weekdays | New detection for a confirmed gap ≤ 10 working days |
| Threat intelligence and vulnerability management | Weekdays | Critical advisories assessed ≤ 1 working day |

**§4 Authority.** The CDC may, without prior approval:

- isolate laptops, desktops and servers outside the sorting hubs' tier-1 list
- disable user accounts and revoke sessions on suspected compromise, in that order
- block domains, IP addresses and file hashes at the security controls
- read logs and forensic data on any in-scope system, under the rules in §7

The provider may, at night, isolate laptops and disable standard user accounts;
anything else it escalates to the on-call responder.

Needs approval first:

- isolating a tier-1 sorting-hub server: Head of Operations on duty
- statutory notifications: General Counsel and DPO approve, or their named deputies out of hours; the CDC files
- engaging the forensic retainer: CDC manager, informing the CISO

## The first 90 days

Following [Start here](start-here.md), with named owners.

| Weeks | What happened | Owner |
|-------|---------------|-------|
| 1–2 | Design workshops for Govern; charter drafted and signed in week 4 | CDC manager, CISO |
| 1–4 | Regulatory applicability register; virk.dk registration confirmed | Compliance lead |
| 2–6 | Operating model decided; provider selected against the [MSSP checklist](../templates/mssp-requirements-checklist.md) | CDC manager, Procurement |
| 3–8 | Critical services agreed with the business: sorting control, route planning, customer tracking, payroll | CISO, business owners |
| 4–10 | MFA enforced for all remote and admin access; one immutable backup copy restore-tested | IAM lead, Infrastructure |
| 6–12 | Entra ID, endpoint and Microsoft 365 logs onboarded and sent to the provider | Detection engineer |
| 6 | Executive board approves the security measures; board cybersecurity training booked for week 14 | CISO |
| 8–12 | Incident plan v1; ransomware, data-breach and identity playbooks adopted; tabletop exercise with management and a NIS2 reporting drill against the 24-hour clock | CDC manager, Legal |
| 12 | Baseline maturity assessment; action plan published | CDC manager |

**Deliberately not done in year one:** penetration testing, a threat-hunting
programme, a SOAR platform, and a threat intelligence platform. The foundations
come first.

## The detection portfolio after 90 days

Chosen from the threat profile, which puts identity attacks, business email
compromise and ransomware at the top. See the
[detection use case template](../templates/detection-use-case-template.md).

| ID | Detection | ATT&CK | Log source | Status |
|----|-----------|--------|------------|--------|
| UC-01 | Sign-in from an unfamiliar country followed by a mailbox rule change | T1078.004, T1114.003 | Entra ID, Microsoft 365 | Deployed, validated |
| UC-02 | Repeated MFA prompts denied, then one accepted | T1621 | Entra ID | Deployed, validated |
| UC-03 | Password spray against many accounts from one source | T1110.003 | Entra ID | Deployed, validated |
| UC-04 | User consents to an unverified application with mail access | T1528 | Entra ID audit | Deployed, not yet validated |
| UC-05 | New inbox rule forwarding to an external address | T1114.003 | Microsoft 365 | Deployed, validated |
| UC-06 | Account added to a privileged group outside change windows | T1098 | Active Directory, Entra ID | Deployed, validated |
| UC-07 | LSASS memory read by an unusual process | T1003.001 | Endpoint | Deployed, validated |
| UC-08 | Volume shadow copies deleted | T1490 | Endpoint | Deployed, validated |
| UC-09 | Remote desktop from a workstation to a server | T1021.001 | Endpoint, firewall | In tuning |
| UC-10 | Many files renamed with a new extension in a short time | T1486 | Endpoint | Deployed, not yet validated |

Ten detections, seven of them validated by firing in test. A small portfolio aimed at the real threats,
rather than a large imported rule set nobody has tested.

## The maturity baseline and action plan

The assessment at week 12, scored with evidence, and the gaps turned into owned
actions. This is the output of the
[maturity self-assessment](../tools/maturity-assessment.html) with owners and
due dates filled in.

| Function | Level now | Target |
|----------|-----------|--------|
| Govern | 1 | 3 |
| Identify | 1 | 2 |
| Protect | 2 | 3 |
| Detect | 2 | 3 |
| Respond | 2 | 3 |
| Recover | 1 | 2 |

Govern, Identify and Recover sit below Level 2, which for a NIS2 entity is the legal floor: each has a measure the law requires that is not yet in place even in basic form. Those actions go first. An excerpt of the action plan, seven of the open actions:

| Criterion missing | Status | Evidence so far | Owner | Due |
|-------------------|--------|-----------------|-------|-----|
| Govern L2 · NIS2: security requirements in contracts with critical suppliers | Partially in place | The provider contract has them; 3 of 11 other critical suppliers reviewed | Procurement lead | Q1 |
| Govern L2 · NIS2: management body trained within 12 months | Planned | Board training booked for week 14 | CISO | Q1 |
| Identify L2 · NIS2: automated asset discovery on core networks | Partially in place | Endpoint inventory only; servers in a spreadsheet | Infrastructure lead | Q1 |
| Recover L2 · NIS2: a crown-jewel service restored end to end against its RTO | Partially in place | Payroll database restored, not timed against its RTO; route planning not yet tested | Infrastructure lead | Q1 |
| Detect L3: detection lifecycle with version control and testing | Planned | Rules in a repository, no tests yet | Detection engineer | Q2 |
| Respond L3: containment authority technically tested | Partially in place | Laptop isolation tested; server isolation not | CDC manager | Q1 |
| Govern L3: quarterly reporting to executive management | Planned | First report scheduled | CISO | Q1 |

## The first quarterly board report

Illustrative figures, in the shape the [executive guide](executive-guide.md)
recommends.

| Measure | This quarter | Trend | Comment |
|---------|--------------|-------|---------|
| Functions at or above target | 0 of 6 | New baseline | Plan above closes Identify and Recover gaps in Q1 |
| Median time to detect, serious incidents | 6 h (2 incidents) | New baseline | Both were phishing leading to mailbox access |
| Median time to contain, serious incidents | 40 min | New baseline | Account disabled and sessions revoked by the on-call responder |
| Statutory notifications on time | 2 of 2 | — | NIS2 early warning after 9 hours. GDPR: one mailbox held customer data and was notified to Datatilsynet after 50 hours; the other was assessed and documented as not notifiable, per Art. 33(5) |
| Critical services with a restore test in 12 months | 1 of 4 | — | Route planning, tracking and payroll scheduled |
| Overdue actions | 0 | — | |

## What to take from it

- The operating model came from constraints, not preference: budget for six
  people and a night operation made the hybrid the only fit.
- The charter's authority section did the most work. The two serious incidents
  were contained in minutes because nobody had to ask.
- The portfolio stayed small and tested. Coverage grows from the threat profile,
  not from importing rules.
- Every gap has a name and a date next to it. That is what turned the maturity
  score into a plan, and the gaps below the legal floor went to the top of it.
- The two incidents were detected after six hours, not minutes. Fast containment
  saved them; detection speed is where the next quarter's engineering goes.

*Open CDC Framework, licensed CC BY 4.0. All organisations, people and figures on this page are fictional.*
