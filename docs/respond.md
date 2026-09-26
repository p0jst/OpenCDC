# RESPOND

## Objective

Contain, eradicate, and communicate during incidents, including meeting EU statutory reporting deadlines, which are among the strictest in the world.

## Core capabilities

<p class="src" markdown><span class="src-tag standard">Standard</span><span class="src-tag ocdf">OCDF</span>Function from NIST CSF 2.0; the capability breakdown and IDs are this framework's.</p>

| ID | Capability | Description |
|----|-----------|-------------|
| RS-1 | Incident response plan | Approved IR plan: definitions, severity classification, roles, escalation, decision authority including who may disconnect production, out-of-band communications. |
| RS-2 | Playbooks | Scenario-specific runbooks for the incident types your threat profile makes most likely, typically phishing/BEC, ransomware, credential compromise and data breach, and often DDoS and supplier compromise. OCDF ships drafts for identity compromise, BEC and ransomware in [playbooks](../playbooks/README.md); the others are on the roadmap, so write them from the external baselines listed there. |
| RS-3 | Incident analysis & forensics | Evidence collection and preservation with chain of custody, forensic imaging capability in-house or retained, root-cause analysis per CSF 2.0 RS.AN. |
| RS-4 | Containment & eradication | Technical ability to isolate hosts, disable accounts, block indicators, and revoke sessions, all with pre-agreed authority. |
| RS-5 | Incident reporting & communication | Internal escalation matrix plus **external statutory reporting**: national CSIRT or competent authority under NIS2, data protection authority under GDPR, sector regulators under DORA, affected data subjects, law enforcement. |
| RS-6 | Crisis management interface | Escalation path from security incident to organisational crisis; link to business continuity structures. |
| RS-7 | Exercises | Tabletop and technical exercises at least annually, including management under the NIS2 training obligation, and statutory-reporting drills. |

## The first hour of a major incident

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span>Lessons from major incidents; agree them in the charter before you need them.</p>

Playbooks handle the specific scenario. These are the estate-wide moves that apply to almost any
major compromise, and the ones most often skipped under pressure. Pre-agree them in charter §4
so they are decisions to *execute*, not decisions to *have*.

- **Do not shut systems down.** Powering off destroys memory evidence, and on a compromised host
  nobody knows what is configured to run at boot. Isolate instead: network containment preserves
  both the machine and the evidence inside it.
- **Cut external connectivity for affected sites.** A deny-all rule at the top of the perimeter
  ruleset, and remote access disabled with it: client VPN, site-to-site tunnels, remote desktop
  and VDI gateways, vendor and out-of-band management paths. Partial isolation that leaves one
  tunnel up is not isolation. The Availability impact is severe, which is exactly why the authority
  has to exist before the night it is needed.
- **Protect the backups before anything else touches them.** Confirm recent restore points exist and
  are readable, then isolate the backup infrastructure. Backup systems are a primary target in
  ransomware operations, and the credentials to reach them are often already held.
- **Freeze anything that expires.** SAN, hypervisor and filesystem snapshots roll off on default
  retention schedules, frequently within days, taking recovery points and evidence with them.
  Extend retention or export copies in the first hour, not the first week.
- **If there is no central logging, start collecting now.** Firewall, directory, hypervisor,
  endpoint, mail and remote-access logs, pulled somewhere the adversary cannot reach. A log not
  collected on day one is not available on day five.
- **Engage counsel, and the insurer if there is a policy** — see below, and do it before the
  technical picture is complete rather than after.

### Counsel and insurance

Involve legal counsel when an incident looks *material*, not when it looks *notifiable*. Two
practical traps, both hard to fix retrospectively:

- **Insurance conditions bind early.** Cyber policies commonly require notification within a short
  window and mandate pre-approved DFIR, negotiation and legal panels. Bringing in your own responder
  first can reduce or void cover. Establish before the incident whether a policy exists, who
  notifies the carrier, within what window, and which vendors it permits, then record it in the IR
  plan alongside the DFIR retainer.
- **Privilege is not uniform across the EU.** Some jurisdictions extend legal professional privilege
  to material prepared for or by external counsel; several member states do not extend it to
  in-house lawyers at all, and the treatment of technical investigation reports differs again. Do
  not assume a report is protected because counsel commissioned it. Settle the position per
  jurisdiction *before* the first report is written.

Firms specialising in incident response can coordinate carriers, responders and notifications while
the CDC keeps working the incident. Identify one alongside the DFIR retainer, not during a P1.

## EU statutory reporting timelines — build these into playbooks

<p class="src" markdown><span class="src-tag law">Law</span>From the legal texts; national transpositions may add detail. Not legal advice.</p>

| Regime | Trigger | Deadline | Recipient |
|--------|---------|----------|-----------|
| **NIS2 Art. 23** | Significant incident | **Early warning ≤ 24 h**; incident notification ≤ 72 h; final report ≤ 1 month | National CSIRT / competent authority |
| **GDPR Art. 33** | Personal data breach posing a risk to individuals | **≤ 72 h from awareness** | Data protection authority |
| **GDPR Art. 34** | High risk to individuals | Without undue delay | Affected data subjects |
| **NIS2 Art. 23(1)–(2)** | Significant incident likely to affect the recipients of your services; significant cyber threat | Without undue delay | The affected recipients of your services, with the measures they can take |
| **DORA Art. 19** | Major ICT-related incident at financial entities | Initial ≤ 4 h from classification / ≤ 24 h from awareness; intermediate ≤ 72 h; final ≤ 1 month | Competent financial authority |
| **CER Art. 15** | Incident that significantly disrupts, or could significantly disrupt, an essential service of a designated critical entity | Initial notification ≤ 24 h from awareness; detailed report ≤ 1 month | Competent authority under the national CER law |

**What counts as significant.** Under NIS2 Art. 23(3) an incident is significant if it has caused or can cause severe operational disruption or financial loss to the entity, or considerable material or non-material damage to others. Commission Implementing Regulation (EU) 2024/2690 sets concrete thresholds for digital infrastructure and digital service providers, and many member states publish guidance for other sectors. Write the definition that applies to you into the IR plan's severity classification, so the on-call analyst does not have to interpret the directive at 03:00.

> Member-state transpositions of NIS2 may add national specifics, such as a different recipient for one sector, so maintain a country annex for each jurisdiction you operate in. In Denmark, for example, energy-sector entities report to Energistyrelsen rather than via virk.dk. Community contributions of national annexes are welcome; see CONTRIBUTING.

## Case closure taxonomy

<p class="src" markdown><span class="src-tag ocdf">OCDF</span></p>

Standardise how every case closes. It is the foundation of honest metrics, tuning feedback and comparable statistics: **true positive with impact**, where a CIA attribute was breached, making it an incident whose reporting duties must be assessed; **true positive without impact**, where there was malicious intent but no harm done; **indeterminate**; or **false positive**, which feeds the tuning loop in [Running the CDC](cdc-operations.md). For incident-type classification, the open VERIS vocabulary of malware, hacking, social, misuse, error, physical and environmental keeps year-over-year and peer statistics comparable.

## CIA mapping

<p class="src" markdown><span class="src-tag ocdf">OCDF</span>This framework's mapping of each capability to confidentiality, integrity and availability.</p>

| Capability | C | I | A | Rationale |
|-----------|---|---|---|-----------|
| RS-2 Playbooks | ● | ● | ● | Ransomware playbooks defend A/I; breach playbooks defend C. |
| RS-3 Forensics | ○ | ● | ○ | Evidence integrity through hashing and chain of custody is an Integrity discipline. |
| RS-4 Containment | ● | ● | ● | Containment trades short-term Availability for protection of C and I, so the decision authority for that trade-off must be pre-agreed at GOVERN level. |
| RS-1 IR plan | ● | ● | ● | The plan's severity classes should weigh impact per objective, so the response matches what is at stake. |
| RS-5 Reporting & communication | ● | ○ | ○ | Reporting channels carry sensitive incident detail; the GDPR duties it serves are about Confidentiality breaches. |
| RS-6 Crisis interface | ○ | ○ | ● | Escalates when an incident threatens the continuity of the business, an Availability decision. |
| RS-7 Exercises | ○ | ○ | ○ | An enabler: exercise the scenario that threatens your dominant objective, usually ransomware for A and I, breach for C. |

*● primary, ○ secondary or indirect. Rows where all three are ○ are enablers: they protect nothing themselves, but the others depend on them.*

## Roles & staffing

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span>Staffing figures are practitioner estimates; the arithmetic is under staffing and cost in [Operating models](operating-models.md).</p>

- **Incident manager/commander** — coordinates; distinct from technical lead in larger incidents.
- **Technical responders** — often the same analysts as DETECT.
- **Legal/DPO and communications** — mandatory members of the extended IR team.
- **Retainers** — consider an external DFIR retainer at Level 2+ if in-house forensics is not viable, and identify external counsel on the same basis.

## Maturity criteria

<p class="src" markdown><span class="src-tag ocdf">OCDF</span>This framework's criteria. Not a certification standard.</p>

The criteria that score RESPOND are kept in one place for all six functions: the [maturity self-assessment, RESPOND](../assessments/maturity-self-assessment.md#respond), with the same text in the [interactive tool](../tools/maturity-assessment.html). Its Level 2 criteria include the minimum form of NIS2 Art. 21(2)(b) and (c), and Art. 23, marked there; see the [NIS2 Article 21 crosswalk](nis2-article-21-crosswalk.md). How levels are scored is in the [maturity model](maturity-model.md).

## EU regulatory hooks

<p class="src" markdown><span class="src-tag law">Law</span>Paraphrased from the legal texts. Check the article itself and your national law; not legal advice.</p>

- **NIS2 Art. 21(2)(b)** incident handling; **Art. 23** reporting; see the table above.
- **GDPR Art. 33/34** — breach notification; document *all* breaches internally, even those not notified, per Art. 33(5).
- **DORA Art. 17–19** — ICT incident management, classification and reporting for financial entities.
- **ENISA / national CSIRT good practice** — align severity taxonomies with your national CSIRT's scheme where one exists to ease reporting.

## External dependencies

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span>Typical dependencies from experience; yours will differ.</p>

| Dependency | Party | Type | Agree up front |
|-----------|-------|------|----------------|
| Containment beyond pre-mandated scope, the crown jewels | Service owner / executive per charter §4 | [GATE] | Decision criteria plus deputy; drill it, because this gate at 03:00 is the whole point of the charter |
| Execution of containment and restoration actions | IT operations | [HARD] | 24/7 reachability; actions from the containment catalogue rehearsed |
| Notification decisions for GDPR, NIS2 and press | Legal / DPO / communications | [GATE] | Draft templates pre-approved; who can be woken |
| External statements and customer communication | Communications | [HARD] | Holding statements ready; single spokesperson rule |
| Insider-related cases | HR + legal | [GATE] | Process agreed before the first case, incl. evidence handling |
| Forensics beyond in-house capability | External DFIR retainer | [HARD] | Retainer signed, response time, onboarding pack ready |
| Cyber insurance notification and approved vendors | Insurer via risk/finance | [GATE] | Whether a policy exists, who notifies, within what window, which responder and counsel panels it permits; engaging outside the panel can reduce cover |
| Legal privilege position and external counsel | Legal, external where required | [GATE] | Settled per jurisdiction before the first investigation report is written |
| Estate-wide network containment: perimeter deny-all, remote access off | Network/IT operations + executive per charter §4 | [GATE] | Who may order it, who executes it out of hours, and how long it can stand |
| Backup isolation and snapshot retention extension | Backup/storage owner | [HARD] | Reachable 24/7; defaults roll off in days |

## Sources

- NIST SP 800-61 Rev. 3, *Incident Response Recommendations and Considerations for Cybersecurity Risk Management*, 2025. https://doi.org/10.6028/NIST.SP.800-61r3
- NIST CSF 2.0, CSWP 29: RESPOND function.
- FIRST, *Computer Security Incident Response Team Services Framework* v2.1. https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1
- NIS2: Directive (EU) 2022/2555 Art. 23; Commission Implementing Regulation (EU) 2024/2690; GDPR Art. 33–34; DORA: Regulation (EU) 2022/2554 Art. 17–19; CER: Directive (EU) 2022/2557 Art. 15.
- VERIS, the *Vocabulary for Event Recording and Incident Sharing*. https://verisframework.org
- Microsoft incident response playbooks: baseline runbooks; adapt them to your environment. https://learn.microsoft.com/security/operations/incident-response-playbooks
- CISA, *Federal Government Cybersecurity Incident and Vulnerability Response Playbooks*, 2021. https://www.cisa.gov

*Open CDC Framework, licensed CC BY 4.0. Credits: [References & credits](references.md).*
