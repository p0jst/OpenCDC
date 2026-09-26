# PROTECT

## Objective

Reduce the likelihood and blast radius of incidents through preventive controls. The CDC does not usually *operate* all preventive controls, since IT and platform teams often do, but it must *influence, verify and monitor* them. Protection failures become detection and response workload.

## Core capabilities

<p class="src" markdown><span class="src-tag standard">Standard</span><span class="src-tag ocdf">OCDF</span>Function from NIST CSF 2.0; the capability breakdown and IDs are this framework's.</p>

| ID | Capability | Description |
|----|-----------|-------------|
| PR-1 | Identity & access management | Centralised identity, MFA that is phishing-resistant for admins, least privilege, joiner/mover/leaver process, quarterly dormant-account review, service-account inventory with owners, privileged access management. The CDC's own platforms, meaning the SIEM, EDR console, automation and case tooling, are among the most privileged systems in the estate: separate admin accounts, phishing-resistant MFA and logging of the CDC's own actions apply to them first. |
| PR-2 | Awareness & training | Role-based security training; phishing simulations; specific training for developers and admins; management training under the NIS2 Art. 20 obligation. |
| PR-3 | Data security | Encryption at rest and in transit, key management, data loss prevention proportionate to classification. |
| PR-4 | Platform hardening & secure configuration | Hardening baselines such as CIS Benchmarks, configuration monitoring, EDR and endpoint protection deployment, and **application control**, covered below. |
| PR-5 | Vulnerability remediation & patching | Risk-based patching SLAs; emergency patch process for actively exploited vulnerabilities. |
| PR-6 | Network security & segmentation | Zoning/segmentation, restricted admin paths, secure remote access, egress control. |
| PR-7 | Resilient technology infrastructure | Backups that are tested, with an offline or immutable copy; redundancy for critical services; capacity management per CSF 2.0 PR.IR. |
| PR-8 | Secure development & change | Secure SDLC requirements, change management, and pre-production security testing where software is developed in-house. |
| PR-9 | Email & web protections | DMARC in enforcing mode with SPF and DKIM on all sending domains, mail gateway with attachment controls, protective DNS filtering for all endpoints including remote, and managed browser baseline. The dominant initial-access vector deserves its own preventive row, not just a detection log source. |

### Application control and allowlisting — part of PR-4

Software inventory under ID-1 and CIS Controls 1–2 has an enforcement half that is often skipped: only authorized software, libraries and scripts may execute, following the logic of CIS safeguards 2.5–2.7. Application control is among the highest-impact preventive controls available. Most commodity malware and many ransomware chains simply fail on a host that refuses to run unapproved binaries and scripts. A pragmatic adoption path:

1. Start where it's easiest and matters most: servers. Server workloads change rarely; allowlisting a domain controller, a backup server or a payment application host is far more tractable than a developer laptop, and those are the hosts where execution control buys the most.
2. Audit mode first: run the platform's application control mechanism in audit/log-only mode, build the ruleset from observed reality, then enforce. Weeks in audit, not months.
3. Script control counts: constraining script interpreters and unsigned scripts blocks a large share of initial-access tradecraft even where full binary allowlisting is out of reach.
4. Workstations pragmatically: publisher/path-based rules plus blocking execution from user-writable locations gives much of the benefit at a fraction of the maintenance; full allowlisting on standard-build workstations is an A-tier ambition.
5. Feed DETECT: application-control audit and block events are a first-class log source: every block is prevention, and every audit-mode "would have blocked" is a free detection.

Ownership follows the SIEM pattern in [Detect](detect.md): platform teams operate the mechanism; the CDC sets the policy intent, monitors the events and owns exceptions. Each exception gets an owner and an expiry, the same discipline as detection suppressions.

## CIA mapping

<p class="src" markdown><span class="src-tag ocdf">OCDF</span>This framework's mapping of each capability to confidentiality, integrity and availability.</p>

| Capability | C | I | A | Rationale |
|-----------|---|---|---|-----------|
| PR-1 IAM | ● | ● | ○ | Access control is the primary confidentiality/integrity control. |
| PR-3 Data security | ● | ● | ○ | Encryption serves C; signing/hashing serves I. |
| PR-4 Hardening & app control | ○ | ● | ● | Configuration/execution integrity reduces exploitability; app control directly caps ransomware blast radius, serving A. |
| PR-6 Segmentation | ● | ○ | ● | Contains lateral movement for C and limits outage blast radius for A. |
| PR-9 Email/web protections | ● | ● | ○ | Cuts phishing and BEC for C, and malware delivery for I, at the front door; DMARC also protects your domain's authenticity toward others. |
| PR-7 Backups/redundancy | ○ | ● | ● | The core Availability control; immutable backups also protect Integrity against ransomware encryption/tampering. |
| PR-2 Awareness | ● | ● | ○ | Phishing and social engineering target credentials and payments first, which are Confidentiality and Integrity. |
| PR-5 Patching | ● | ● | ● | Unpatched exploitable software threatens all three; prioritise by the objective the exposed asset carries. |
| PR-8 Secure development & change | ○ | ● | ○ | Change control and code review protect the Integrity of what runs in production. |

*● primary, ○ secondary or indirect. Rows where all three are ○ are enablers: they protect nothing themselves, but the others depend on them.*

## Roles & staffing

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span>Staffing figures are practitioner estimates; the arithmetic is under staffing and cost in [Operating models](operating-models.md).</p>

- **IT/platform teams** operate most controls; the CDC defines requirements and verifies via posture monitoring.
- **Security engineers** in the CDC own EDR, hardening verification, and control telemetry.
- **Awareness lead** — often shared with HR/communications.

## Maturity criteria

<p class="src" markdown><span class="src-tag ocdf">OCDF</span>This framework's criteria. Not a certification standard.</p>

The criteria that score PROTECT are kept in one place for all six functions: the [maturity self-assessment, PROTECT](../assessments/maturity-self-assessment.md#protect), with the same text in the [interactive tool](../tools/maturity-assessment.html). Its Level 2 criteria include the minimum form of NIS2 Art. 21(2)(c), (e), (g), (h) and (j), marked there; see the [NIS2 Article 21 crosswalk](nis2-article-21-crosswalk.md). How levels are scored is in the [maturity model](maturity-model.md).

## EU regulatory hooks

<p class="src" markdown><span class="src-tag law">Law</span>Paraphrased from the legal texts. Check the article itself and your national law; not legal advice.</p>

- **NIS2 Art. 21(2)** — explicitly requires, among others: (g) basic cyber hygiene practices and cybersecurity training; (h) policies and procedures on the use of cryptography and, where appropriate, encryption; (i) human resources security, access control policies and asset management; (j) MFA or continuous authentication solutions, where appropriate.
- **Commission Implementing Regulation (EU) 2024/2690** — technical requirements detailing NIS2 Art. 21 measures for digital infrastructure entities; useful as a control checklist even outside its formal scope.
- **GDPR Art. 32** — encryption and pseudonymisation named as example measures.
- **DORA Art. 9** — protection and prevention measures for financial entities.
- **CIS Benchmarks / ENISA guidance** — recommended hardening baselines.

## External dependencies

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span>Typical dependencies from experience; yours will differ.</p>

| Dependency | Party | Type | Agree up front |
|-----------|-------|------|----------------|
| Operation of most preventive controls: patching, hardening, backups | IT/platform teams | [HARD] | Control requirements set by CDC; SLAs and coverage telemetry back to CDC |
| MFA and identity control rollout | Identity/IAM team | [HARD] | Rollout order, admins first; exception governance |
| Segmentation and network changes | Network team | [HARD] | Zone model ownership; change lead times |
| Emergency change approval for critical patches | Change advisory board | [GATE] | Pre-approved emergency path with post-hoc review |
| Application-control exceptions | Platform teams + CDC | [GATE] | Exception owner + expiry, CDC veto on tier-0 |
| Awareness programme delivery | HR / communications | [SOFT] | CDC provides content priorities from incident data |

## Sources

- NIST CSF 2.0, CSWP 29: PROTECT function. https://doi.org/10.6028/NIST.CSWP.29
- NIST SP 800-53 Rev. 5, *Security and Privacy Controls*. https://doi.org/10.6028/NIST.SP.800-53r5
- CIS, *CIS Critical Security Controls*, especially Controls 1–2 including the software allowlisting safeguards 2.5–2.7, and *CIS Benchmarks*. https://www.cisecurity.org
- NIS2: Directive (EU) 2022/2555, Art. 21; Implementing Regulation (EU) 2024/2690; GDPR Art. 32; DORA Art. 9.

*Open CDC Framework, licensed CC BY 4.0. Credits: [References & credits](references.md).*
