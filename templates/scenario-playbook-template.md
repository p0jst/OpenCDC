# Scenario Playbook — Template

> Related capabilities: RS-2, RS-4, RS-5. One playbook per incident type your threat profile makes likely, at least ransomware, business email compromise, identity compromise and personal data breach. Copy this file once per scenario, fill in every `[…]`, and delete the guidance lines in italics when you are done. Write it for the worst night: an analyst who has never run this scenario must be able to follow it alone at 03:00.

## Metadata

| Field | Value |
|-------|-------|
| ID | PB-[XX], matching the playbook index in your IR plan §6 |
| Scenario | [e.g. ransomware, business email compromise] |
| Owner | [named person] |
| Version / last reviewed | [ ] |
| Last exercised | [date and exercise type] |
| Related platform playbooks | [PB-… for the host types this scenario usually involves] |

## Scope and triggers

- **What starts this playbook:** […] *The alerts, reports or observations that should make an analyst open it. Include precursors, not only the incident itself.*
- **What it does not cover:** […] *Hand-offs to other playbooks, and any environment where the actions below are unsafe, such as OT.*
- **Default severity:** [P1–P4], per IR plan §1
- **Legal note:** […] *For example: assume data was exfiltrated until shown otherwise; involve the DPO when employee data is examined.*

## 0. Prerequisites — build these before the incident

*List what must already exist for the steps below to work. Every unchecked box is a gap to put in the backlog.*

- [ ] Containment actions this playbook needs, pre-authorised in the [containment action catalogue](containment-action-catalogue-template.md): [CON-…]
- [ ] Log sources and detections the triage steps rely on: […]
- [ ] Out-of-band communication channel: […]
- [ ] External contacts in the IR plan: [DFIR retainer, counsel, insurer, supplier contacts]
- [ ] […]

## 1. Triage — the first hour

*Numbered steps, in order. For a major incident, run the estate-wide first-hour actions in [RESPOND](../docs/respond.md) alongside these.*

1. […]
2. […]
3. […]

**Decision point:** […] *The fork that decides the rest of the response, for example evidence-priority versus containment-priority, and who makes that call.*

**Scope questions to answer:** […] *Which systems, accounts and data are affected, and how you find out.*

## 2. Containment

| Step | Action | Catalogue ID | Who may decide | Notes |
|------|--------|--------------|----------------|-------|
| 1 | […] | CON-[…] | [CDC / service owner / management] | […] |
| 2 | […] | CON-[…] | […] | […] |
| 3 | […] | CON-[…] | […] | […] |

*Say what to contain in the identity plane and in the cloud, not only on hosts.*

## 3. Evidence acquisition

*Order of volatility per RFC 3227. Hash everything you collect, record every action with time and operator, and use your chain-of-custody form.*

| # | Evidence | Where it lives | How to collect | Notes |
|---|----------|----------------|----------------|-------|
| 1 | […] | […] | […] | […] |
| 2 | […] | […] | […] | […] |
| 3 | […] | […] | […] | […] |

## 4. Analysis pointers

- **Initial access:** […] *Where to look for how the adversary got in.*
- **Impact:** […] *How to establish what was accessed, changed or taken, and from which logs.*
- **ATT&CK mapping:** […] *Techniques to confirm, and the detection gaps to feed back to DETECT.*

## 5. Eradication & recovery

- **Order of recovery:** […] *Identity and management plane first where they were touched, then services in the order agreed in RC-1.*
- **Eradication steps:** […]
- **Conditions before reconnecting:** […] *Integrity before availability.*
- **Closure criteria:** no adversary activity for [ ] days; initial access closed; lessons-learned filed.

## 6. Reporting hooks

*Fill in from your IR plan §4 and your national annex. Keep the clock and the recipient on the same line.*

| Trigger | Regime | Deadline | Recipient | Owner |
|---------|--------|----------|-----------|-------|
| Significant incident | NIS2 or national act | Early warning ≤ 24 h, notification ≤ 72 h, final report ≤ 1 month | [ ] | [ ] |
| Personal data breach | GDPR Art. 33 / 34 | ≤ 72 h from awareness | [supervisory authority] | [DPO] |
| […] | […] | […] | […] | […] |

## 7. Lessons learned

- Review held: [date], actions tracked in: [link]
- Changes to this playbook since the last incident or exercise: […]

## Baselines to draw on

Public collections that are useful starting points for filling in the steps above. They are baselines, so adjust them to your estate, tooling, authority matrix and reporting duties before relying on them:

- Microsoft incident response playbooks: https://learn.microsoft.com/security/operations/incident-response-playbooks
- CISA, Federal Government Cybersecurity Incident and Vulnerability Response Playbooks: https://www.cisa.gov/resources-tools/resources/federal-government-cybersecurity-incident-and-vulnerability-response-playbooks
- CISA and partners, #StopRansomware Guide: https://www.cisa.gov/stopransomware

When importing from any of them: replace product assumptions with your stack, align severities with IR plan §1, insert your containment mandates, add your statutory reporting hooks, and exercise the result once before you need it.

*Open CDC Framework, licensed CC BY 4.0.*
