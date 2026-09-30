# Incident Response Plan — Template

> Related capability: RS-1. Structure informed by NIST SP 800-61r3, the Dynamic Approach to Incident Response (DAIR) and FIRST good practice. Keep this document short, 10–15 pages at most; detail belongs in playbooks.

**Owner:** | **Approved by:** | **Version / date:** | **Exercised on:**

## 1. Definitions & severity classification

| Severity | Definition | Examples | Response target |
|----------|-----------|----------|-----------------|
| P1 — Critical | Confirmed compromise of crown-jewel service, or active widespread attack; major C/I/A impact | Ransomware executing; confirmed exfiltration of special-category data | Immediate, 24/7, crisis interface assessed |
| P2 — High | Confirmed compromise, contained scope | Single compromised admin account | ≤ 1 h engagement |
| P3 — Medium | Probable incident, limited impact | Malware detected and blocked, persistence suspected | Same business day |
| P4 — Low | Policy violation / no material impact | Isolated phishing click, no execution | Routine |

> Classify severity against **CIA impact per affected asset class**, per [CIA as design lens](../docs/cia-triad.md), not against alert volume.
>
> Severity is not regulatory significance. Severity sets how hard the CDC responds; significance, assessed under §4, decides who must be told and by when. Record both in every incident, with different owners.

## 2. Roles

| Role | Person / rotation | Responsibility |
|------|-------------------|----------------|
| Incident Manager | | Coordination, decisions, log of record |
| Technical Lead | | Investigation & containment direction |
| Legal / DPO | | Breach assessment, notification decisions |
| Communications | | Internal & external messaging |
| Executive sponsor | | Crisis escalation, major trade-off approval |
| External counsel | | Privilege position per jurisdiction; regulatory and contractual exposure |
| Cyber insurance contact | | Carrier notification within the policy window; which responder and counsel panels the policy permits |

### Decision authority

> Who may take each decision, who stands in, and what record the decision leaves. Assign by impact, not by seniority, and exercise the matrix so that it matches what happens at night.

| Decision | Authority | Deputy | Record it leaves |
|----------|-----------|--------|------------------|
| Declare an incident and set its severity | Incident Manager | | Incident record with time of declaration |
| Assess regulatory significance and notify authorities | Legal / DPO | | Assessment with time of awareness; reports as submitted |
| Containment beyond the pre-mandated scope | Per CDC charter §4 and the containment catalogue | | Action log entry |
| Observe instead of contain when personal data or an essential service is at risk | Executive sponsor with Legal / DPO | | Signed decision in the case |
| Engage external DFIR, counsel or the insurer's panel | | | Engagement record |
| Public statement | Communications with Legal | Executive sponsor | Approved statement with version |
| Exit the response loop and accept residual risk | Executive sponsor for P1 and P2; Incident Manager for P3 and P4 | | Written exit decision, see §3 |

## 3. Process — how an incident moves

> The steps are not a straight line. Step 3 is repeated as often as the incident needs, and the plan should say so, so that a second or third pass is expected rather than read as failure. See [RESPOND](../docs/respond.md) for the reasoning.

1. **Detection & reporting** — sources: monitoring, users via [report channel], third parties, national CSIRT. Record the time of the first report.
2. **Verify & triage** — within [time box, for example 1 h for a suspected P1 or P2]. Outcome: *continue*, *stop* or *defer*, with the reasoning in the record; a deferral names what is missing and when the next decision is due. On *continue*: open the incident record, start the timeline log, set severity per §1, and present the incident to the decision-maker in §2 with a recommendation. Start the regulatory assessment in §4 now, in parallel, and record the time of awareness.
3. **Response loop** — scope, contain, eradicate and recover, repeated until no new evidence of compromise appears:
    - *Scope:* search the estate for the known indicators; list the affected systems, accounts and data.
    - *Contain:* per playbook; authority per CDC charter §4 and §2 above. Record every action with a timestamp, for evidential integrity. For a major incident, run the estate-wide first-hour actions in [RESPOND](../docs/respond.md) alongside the scenario playbook: do not power systems off, cut external connectivity and remote access, isolate backups, extend snapshot retention, and notify counsel and the insurer.
    - *Eradicate:* a short investigation track to eradicate quickly, and a long track for the root cause, planned against the NIS2 final report date in §4. Preserve evidence with hashing and the chain of custody form: [link].
    - *Recover:* integrity verification before reconnection; credential rotation; the service owner's acceptance; enhanced monitoring for [30] days; see recovery plans.
    - *Start another pass when:* a new indicator is found, a known indicator appears outside the current scope, eradication fails, forensic work changes the timeline, or an authority, the insurer or law enforcement changes what is required. Record the trigger.
4. **Exit** — the loop ends by a written decision of the authority in §2: the indicators met, the residual risks accepted, the name of the decision-maker, and the date and time.
5. **Debrief** — remove, or make permanent through change management, the temporary containment actions, accounts and monitoring; consolidate the record; blameless review within [10] working days for P1/P2; root cause and actions tracked in [system]; final reports per §4.

## 4. Statutory notification decision tree

> Prepare per-jurisdiction contact sheet and report templates as annexes. Deadlines below are EU-level; verify national transposition.

- **Personal data breach?** → DPO assesses risk → if notifiable: DPA within **72 h of awareness** under GDPR Art. 33; data subjects if high risk, under Art. 34. Document all breaches, including non-notified.
- **NIS2 significant incident?** → early warning to national CSIRT **≤ 24 h**, notification ≤ 72 h, final report ≤ 1 month, per Art. 23.
- **Significant for the recipients of our services?** → inform affected customers without undue delay, with the measures they can take, per NIS2 Art. 23(1)–(2).
- **DORA major incident at a financial entity?** → initial notification ≤ 4 h from classification as major and no later than 24 h from awareness; intermediate report ≤ 72 h; final report ≤ 1 month, per Art. 19.
- **Critical entity under CER, essential service disrupted?** → initial notification to the CER competent authority ≤ 24 h, detailed report ≤ 1 month, per CER Art. 15.
- **Our definition of "significant":** … *write here the NIS2 Art. 23(3) criteria as your country or, for digital entities, Implementing Regulation (EU) 2024/2690 defines them, and link it to the severity classes in §1.*
- **Law enforcement?** → decision by [role]; national cybercrime unit contact: […].

## 5. Communications

- Out-of-band channel, assuming email and chat are compromised: […]
- Holding statement templates: [annex]
- Spokesperson: only [role]; TLP 2.0 governs technical information sharing.

## 6. Playbook index

> `PB-01`…`PB-06` below are placeholder IDs for **your own** playbooks, so rename them to your scheme. Write each from the [scenario playbook template](scenario-playbook-template.md), and the host-level forensics from the [platform playbook template](platform-playbook-template.md).

| Scenario | Playbook | Last exercised |
|----------|----------|----------------|
| Ransomware | PB-01 | |
| Business email compromise / phishing | PB-02 | |
| Credential / identity compromise | PB-03 | |
| Personal data breach | PB-04 | |
| DDoS | PB-05 | |
| Supplier / third-party compromise | PB-06 | |

## 7. Exercise & review schedule

- Tabletop incl. management: at least annually; the NIS2 Art. 20 training obligation supports this.
- Exercise decisions, not only steps: at least once a year, run a scenario at a realistic pace, out of hours, in which the decision-makers in §2 must decide on incomplete information and the plan meets a situation it did not foresee.
- Technical exercise / reporting drill: [cadence].
- Plan review: annually and after each P1/P2 incident.

---
*Template from the Open CDC Framework, licensed CC BY 4.0. Informed by NIST SP 800-61r3, DAIR, GDPR, NIS2 and DORA. Verify legal specifics with counsel.*
