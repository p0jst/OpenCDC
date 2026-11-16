# RECOVER

## Objective

Restore affected services in a trustworthy state, communicate honestly during restoration, and convert every incident into institutional learning.

## Core capabilities

<p class="src" markdown><span class="src-tag standard">Standard</span><span class="src-tag ocdf">OCDF</span>Function from NIST CSF 2.0; the capability breakdown and IDs are this framework's.</p>

| ID | Capability | Description |
|----|-----------|-------------|
| RC-1 | Recovery planning | Documented recovery plans for crown-jewel services with RTO/RPO targets agreed with the business; restoration ordering based on dependencies carried over from IDENTIFY. |
| RC-2 | Trusted restoration | Verify integrity of backups and systems *before* reconnecting, assuming ransomware persistence; rebuild-from-known-good procedures; credential rotation as standard recovery step. |
| RC-3 | Recovery execution & verification | Ability to execute restores at scale. Before a system returns to production, re-check that the root cause is fixed and persistence removed, test function and security controls, obtain the service owner's acceptance, and monitor the restored system with the incident's detections for a set period, typically 30 days. |
| RC-4 | Recovery communication | Status communication to internal stakeholders, customers and authorities, meaning the final NIS2 and DORA reports, and the public where relevant, per CSF 2.0 RC.CO. |
| RC-5 | Lessons learned & improvement loop | Closing an incident properly: temporary containment, accounts and monitoring removed or made permanent, and the case, chat and notes consolidated into one record. Then blameless post-incident reviews, held against the decision log rather than the outcome, with tracked actions; findings feed the improvement backlog per CSF 2.0 ID.IM, and update playbooks, detections and controls. |
| RC-6 | Business continuity integration | CDC recovery plans aligned with enterprise BCM/DR; joint exercises. |

> **The recovery path is decided during response, not during recovery.** Snapshot and backup
> retention defaults are measured in days: the SAN, hypervisor or filesystem snapshot taken before
> the intrusion is often the cleanest recovery point available, and it expires on schedule whether
> or not there is an incident open. Extending retention and isolating backup infrastructure belong
> in the first hour of response, covered in [RESPOND](respond.md). By the time this function starts,
> the options have already narrowed to whatever survived.

## Reviewing decisions, not outcomes

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span>From running post-incident reviews.</p>

A post-incident review knows how the incident ended. The people who made the decisions did not. Judged with that knowledge, a sound decision with a bad result looks like a mistake, and a poor one that happened to work looks like good judgement.

Take a common case. An analyst isolates a server at night on partial evidence. In the morning it proves to be a false positive, and the business has lost several hours of service. If the review calls that an error, the team learns to wait for certainty before acting. An adversary benefits from every hour a defender spends waiting for certainty.

Hold the review against the [decision log](respond.md#keep-a-decision-log) instead. For each decision that mattered, ask:

- What did the team know at that moment, and what could it reasonably have found out in the time available?
- Was the decision within the authority set in the charter and the IR plan?
- Given what was known, was it a reasonable choice among the options?
- What would have led to a better decision: other information, a different threshold, a clearer mandate, or a faster route to the decision-maker?

The fourth question is where the improvements come from. They usually change the system around the decision, such as a log source, a severity threshold or an entry in the containment catalogue, rather than the person who took it.

Blameless does not mean without accountability. A decision that ignored information the team had, or went beyond the mandate, is a finding. A decision that was reasonable on what was known is not, whatever it cost, and the review should say so in writing. Management sets this standard by how it responds to the first costly false positive. Agree it in advance in the [charter](../templates/cdc-charter-template.md), so the analyst on the night shift knows it before acting.

## CIA mapping

<p class="src" markdown><span class="src-tag ocdf">OCDF</span>This framework's mapping of each capability to confidentiality, integrity and availability.</p>

| Capability | C | I | A | Rationale |
|-----------|---|---|---|-----------|
| RC-1 Recovery planning | ○ | ○ | ● | RTO/RPO are Availability commitments. |
| RC-2 Trusted restoration | ○ | ● | ● | Restoring a backdoored system restores the breach: **Integrity verification before Availability restoration** is the core principle of this function. |
| RC-3 Verified execution | ○ | ● | ● | Recovery is declared complete only when integrity checks pass, then service returns. |
| RC-4 Communication | ● | ○ | ○ | Recovery comms must not leak sensitive investigation details, which is the Confidentiality of incident data. |
| RC-5 Lessons learned | ○ | ○ | ○ | An enabler: it serves whichever objective the incident breached. |
| RC-6 BCM integration | ○ | ○ | ● | Business continuity is the organisation's Availability plan; the CDC plugs into it. |

*● primary, ○ secondary or indirect. Rows where all three are ○ are enablers: they protect nothing themselves, but the others depend on them.*

## Roles & staffing

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span>Typical roles from practice. Staffing figures and their arithmetic are under staffing and cost in [Operating models](operating-models.md).</p>

- **Service and platform owners** — execute restoration; the CDC verifies the systems are clean.
- **Incident manager** — remains accountable until the closure criteria are met.
- **BCM coordinator** — the interface to continuity management.

## Maturity criteria

<p class="src" markdown><span class="src-tag ocdf">OCDF</span>This framework's criteria. Not a certification standard.</p>

The criteria that score RECOVER are kept in one place for all six functions: the [maturity self-assessment, RECOVER](../assessments/maturity-self-assessment.md#recover), with the same text in the [interactive tool](../tools/maturity-assessment.html). Its Level 2 criteria include the minimum form of NIS2 Art. 21(2)(c), marked there; see the [NIS2 Article 21 crosswalk](nis2-article-21-crosswalk.md). How levels are scored is in the [maturity model](maturity-model.md).

## EU regulatory hooks

<p class="src" markdown><span class="src-tag law">Law</span>Paraphrased from the legal texts. Check the article itself and your national law; not legal advice.</p>

- **NIS2 Art. 21(2)(c)** — business continuity, backup management, disaster recovery, and crisis management are explicitly required measures.
- **NIS2 Art. 23** — the final report, due within 1 month, must include root cause, mitigation, and cross-border impact where applicable.
- **DORA Art. 11–12** — response and recovery plans, backup policies and restoration procedures for financial entities, with testing obligations.
- **GDPR Art. 32(1)(c)** — "the ability to restore the availability and access to personal data in a timely manner" is a named legal requirement.

## External dependencies

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span>Typical dependencies from experience; yours will differ.</p>

| Dependency | Party | Type | Agree up front |
|-----------|-------|------|----------------|
| RTO/RPO targets accepted | Business service owners | [GATE] | Signed per crown jewel; revisited after exercises |
| Restoration execution | Service/platform owners | [HARD] | Rebuild procedures rehearsed jointly |
| Reconnection of restored systems | CDC integrity verification | [GATE] | Cleanliness criteria checklist; CDC sign-off before reconnect |
| Return to production | Service owner | [GATE] | Acceptance test and signed acceptance per system, including known limitations accepted |
| Business continuity alignment and joint exercises | BCM function | [HARD] | Shared scenario set; annual joint exercise |
| Supplier recovery dependencies | Vendors / procurement | [SOFT] | Recovery commitments in contracts where feasible |

## Sources

- NIST CSF 2.0, CSWP 29: RECOVER function. https://doi.org/10.6028/NIST.CSWP.29
- NIST SP 800-34 Rev. 1, *Contingency Planning Guide for Federal Information Systems*.
- NIS2: Directive (EU) 2022/2555 Art. 21(2)(c), 23; DORA: Regulation (EU) 2022/2554 Art. 11–12; GDPR Art. 32.

*Open CDC Framework, licensed CC BY 4.0. Credits: [References & credits](references.md).*
