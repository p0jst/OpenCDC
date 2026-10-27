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
| PR-5 | Vulnerability remediation & patching | Prioritise by known exploitation and exposure before CVSS: a known-exploited vulnerability on an asset reachable from the internet goes first. Risk-based patching SLAs cover the rest, with an emergency patch process for actively exploited vulnerabilities. Edge devices need more than a deadline, covered below. |
| PR-6 | Network security & segmentation | Zoning/segmentation, restricted admin paths, secure remote access, egress control. |
| PR-7 | Resilient technology infrastructure | Backups that are tested, with an offline or immutable copy; redundancy for critical services; capacity management per CSF 2.0 PR.IR. |
| PR-8 | Secure development & change | Secure SDLC requirements, change management, and pre-production security testing where software is developed in-house. |
| PR-9 | Email & web protections | DMARC in enforcing mode with SPF and DKIM on all sending domains, mail gateway with attachment controls, protective DNS filtering for all endpoints including remote, and managed browser baseline. The dominant initial-access vector deserves its own preventive row, not just a detection log source. |

### Application control and allowlisting under PR-4

Software inventory under ID-1 and CIS Controls 1–2 has an enforcement half that is often skipped: only authorized software, libraries and scripts may execute, following the logic of CIS safeguards 2.5–2.7. Application control is among the highest-impact preventive controls available. Most commodity malware and many ransomware chains simply fail on a host that refuses to run unapproved binaries and scripts. A pragmatic adoption path:

1. Start where it's easiest and matters most: servers. Server workloads change rarely; allowlisting a domain controller, a backup server or a payment application host is far more tractable than a developer laptop, and those are the hosts where execution control buys the most.
2. Audit mode first: run the platform's application control mechanism in audit/log-only mode, build the ruleset from observed reality, then enforce. Weeks in audit, not months.
3. Script control counts: constraining script interpreters and unsigned scripts blocks a large share of initial-access tradecraft even where full binary allowlisting is out of reach.
4. Workstations pragmatically: publisher/path-based rules plus blocking execution from user-writable locations gives much of the benefit at a fraction of the maintenance; full allowlisting on standard-build workstations is an A-tier ambition.
5. Feed DETECT: application-control audit and block events are a first-class log source: every block is prevention, and every audit-mode "would have blocked" is a free detection.

Ownership follows the SIEM pattern in [Detect](detect.md): platform teams operate the mechanism; the CDC sets the policy intent, monitors the events and owns exceptions. Each exception gets an owner and an expiry, the same discipline as detection suppressions.

### Edge devices under PR-5

VPN gateways, firewalls, remote-access portals and other internet-facing appliances are where exploitation now often arrives on the day a vulnerability is disclosed, or before it. A patching SLA measures the time from disclosure to fix. For these devices that window may not exist. ENISA's 2026 threat landscape found a vulnerability exploited in 60% of the unauthorised-access incidents where the way in was known, although the way in was known for only a small share. Plan on the basis that an edge device can be exploited while fully patched:

1. Keep an edge inventory under ID-1 and ID-4: every internet-facing appliance and exposed application, with owner, version and where its vendor publishes advisories.
2. Agree in advance what to do when there is no patch yet: disable the affected feature, restrict access to known source addresses, or take the device offline. Who may order it sits with emergency change approval under external dependencies below.
3. Keep management interfaces off the internet, and give appliance admin accounts phishing-resistant MFA under PR-1.
4. Check for compromise after patching. A patch closes the hole; it does not remove an intruder who used it first. Review the device's logs, configuration and outbound connections against the vendor's or national CSIRT's indicators, back to the disclosure date or earlier where exploitation is known to predate it.
5. Monitor the device as a target, not only as a log source. The edge devices note in [Detect](detect.md) says how.

Patching still matters: many exploited vulnerabilities are first exploited weeks, months or years after disclosure, and the SLA is what closes them. The point is that for the edge, the SLA alone is not the control.

### When findings outrun the patch cycle

AI-assisted discovery is producing new vulnerabilities faster than a cycle of scan, ticket and monthly patch can absorb; NIST reports CVE submissions up 263% from 2020 to 2025. SANS calls the response VulnOps: vulnerability handling run as a continuous decision loop with named owners rather than as a ticket queue. What OCDF takes from it:

1. **Agree three paths in advance.** Each fix goes one way: patched automatically, tested then deployed, or decided by hand. A named person owns every decision on the third path and every exception.
2. **Count real closure.** A finding moved to an exception or a risk acceptance is not closed. Report the exception queue next to the closure rate, so accepted risk cannot grow unseen.
3. **Let AI recommend, not deploy.** It can triage and propose; a person approves what changes.
4. **Start with one loop.** One platform or product family first, such as browsers or one server build; prove it works, then extend.

## CIA mapping

<p class="src" markdown><span class="src-tag ocdf">OCDF</span>This framework's mapping of each capability to confidentiality, integrity and availability.</p>

| Capability | C | I | A | Rationale |
|-----------|---|---|---|-----------|
| PR-1 IAM | ● | ● | ○ | Access control is the primary confidentiality/integrity control. |
| PR-2 Awareness | ● | ● | ○ | Phishing and social engineering target credentials and payments first, which are Confidentiality and Integrity. |
| PR-3 Data security | ● | ● | ○ | Encryption serves C; signing/hashing serves I. |
| PR-4 Hardening & app control | ○ | ● | ● | Configuration/execution integrity reduces exploitability; app control directly caps ransomware blast radius, serving A. |
| PR-5 Patching | ● | ● | ● | Unpatched exploitable software threatens all three; prioritise by the objective the exposed asset carries. |
| PR-6 Segmentation | ● | ○ | ● | Contains lateral movement for C and limits outage blast radius for A. |
| PR-7 Backups/redundancy | ○ | ● | ● | The core Availability control; immutable backups also protect Integrity against ransomware encryption/tampering. |
| PR-8 Secure development & change | ○ | ● | ○ | Change control and code review protect the Integrity of what runs in production. |
| PR-9 Email/web protections | ● | ● | ○ | Cuts phishing and BEC for C, and malware delivery for I, at the front door; DMARC also protects your domain's authenticity toward others. |

*● primary, ○ secondary or indirect. Rows where all three are ○ are enablers: they protect nothing themselves, but the others depend on them.*

## Roles & staffing

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span>Typical roles from practice. Staffing figures and their arithmetic are under staffing and cost in [Operating models](operating-models.md).</p>

- **IT and platform teams** — operate most controls; the CDC defines requirements and verifies them through posture monitoring.
- **Security engineers** — in the CDC; own EDR, hardening verification and control telemetry.
- **Awareness lead** — often shared with HR or communications.

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
- SANS Institute, *VulnOps Field Guide*, August 2026, and *VulnOps: A CISO's Guide to Starting Implementation*. https://www.sans.org/white-papers/vulnops-field-guide · https://www.sans.org/blog/vulnops-cisos-guide-to-starting-implementation
- NIST, *NIST Updates NVD Operations to Address Record CVE Growth*, 15 April 2026. https://www.nist.gov/itl/nvd
- ENISA, *ENISA Threat Landscape 2026*, September 2026, covering 2025. https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026
- ENISA, *NIS2 Technical Implementation Guidance* on Implementing Regulation (EU) 2024/2690, June 2025, with evidence examples and a mapping table. https://www.enisa.europa.eu/publications/nis2-technical-implementation-guidance

*Open CDC Framework, licensed CC BY 4.0. Credits: [References & credits](references.md).*
