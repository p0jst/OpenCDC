# 04 — DETECT

## Objective

Find adversary and anomalous activity fast enough to limit damage. Detection is the operational heart of a CDC: log collection, detection engineering, triage, and threat hunting.

## Core capabilities

<p class="src" markdown><span class="src-tag standard">Standard</span><span class="src-tag ocdf">OCDF</span>Function from NIST CSF 2.0; the capability breakdown and IDs are this framework's.</p>

| ID | Capability | Description |
|----|-----------|-------------|
| DE-1 | Log collection & management | Prioritised onboarding of log sources, covering identity, endpoint, network, cloud, email and critical applications, into a central platform; retention policy; time synchronisation; log integrity protection. |
| DE-2 | Detection engineering | A managed lifecycle for detection use cases: idea → develop → test → deploy → tune → retire. Each use case mapped to MITRE ATT&CK techniques and to the threat profile from IDENTIFY. |
| DE-3 | Alert triage & analysis | Documented triage process, severity matrix, enrichment with asset criticality, identity context and threat intel, and escalation criteria. |
| DE-4 | Coverage assessment | Periodic measurement of detection coverage against ATT&CK and against crown-jewel assets; gap-driven engineering backlog. |
| DE-5 | Threat hunting | Hypothesis-driven hunts based on threat intel; findings convert into new detections. |
| DE-6 | Detection validation | Testing that detections actually fire: unit tests, purple teaming, adversary emulation. |
| DE-7 | Anomaly & integrity monitoring | File/configuration integrity monitoring, identity anomaly detection, and monitoring of the CDC's own infrastructure. |

## Log source onboarding priority — greenfield guidance

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span>The author's ordering by detection value.</p>

1. **Identity** — directory and IdP authentication, privileged actions; the highest detection value per gigabyte.
2. **Endpoint**, meaning EDR telemetry, for process, persistence and lateral-movement visibility.
3. **Email & web gateway** — dominant initial access vectors.
4. **Cloud control plane**, meaning IaaS and SaaS audit logs. Often forgotten, increasingly critical.
5. **Network**, covering firewall, DNS, VPN, netflow and NDR where deployed, for breadth and containment context. Network Detection and Response earns its place precisely where EDR cannot go: unmanaged and unmanageable devices such as IoT, printers, medical and lab equipment, legacy appliances and BYOD; east-west visibility for lateral movement between segments, and as an integrity check on endpoint coverage, since a host talking on the network with no EDR heartbeat is itself a finding. Its limits belong in the same breath: pervasive encryption reduces payload inspection to metadata/behavioural analysis, it sees flows rather than process context, and it is a complement to endpoint and identity telemetry, not a substitute. Decision guide: the more unmanaged devices and flat legacy segments you have, the earlier NDR climbs this priority list; in a fully managed, well-segmented, cloud-heavy estate it stays at 5.
6. **Critical applications & databases** — crown-jewel specific.

**Remote and hybrid work note:** architectures retrofitted from on-prem assumptions go blind the moment a laptop leaves the VPN. Prioritise location-independent telemetry, since EDR and identity-provider logs follow the user everywhere, and verify that endpoint telemetry reaches you off-network before declaring source 1–2 coverage complete. The same applies per cloud/SaaS tenant: coverage is per environment, not per organisation.

## Owning the SIEM platform, in-house or cloud

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span></p>

A SIEM that nobody clearly owns decays into an unpatched, undersized liability, and it is itself a crown jewel, holding your most sensitive telemetry and your detection logic. Before go-live, settle ownership in writing:

| Layer | Typical owner, on-prem or self-hosted | Covers |
|-------|--------------------------------------|--------|
| Hardware & capacity | Infrastructure team | Physical/virtual hosts, storage, network, capacity planning against ingest growth |
| Operating system | Infrastructure team | OS patching, hardening baseline, backup of the platform itself, monitoring of host health |
| SIEM application | CDC | Application upgrades and patching, configuration, data onboarding/parsers, detection content, retention settings, health of the ingest pipeline |
| Access & platform security | CDC, verified independently | Admin access through PAM, audit logging of the SIEM itself, integrity of stored logs |

The traditional split, where infrastructure maintains the server and OS and the CDC maintains the SIEM platform itself, works well, but only if the interface is explicit: agree patching SLAs for the underlying stack, since an unpatched SIEM host is a high-value target, plus capacity review cadence and who is paged when ingest stops at 02:00. Record the split in the charter's interfaces section and give the platform its own recovery plan under RC-1: losing the SIEM during an incident means going blind at the worst moment.

**Cloud-hosted SIEM:** hosting in the cloud buys convenience, elasticity and no hardware ownership, but be clear-eyed that you are shipping your telemetry into a cloud you do not own. Security logs are among the most sensitive data an organisation produces: they contain personal data, which under GDPR requires a processor agreement, residency and a transfer mechanism; they also carry authentication patterns, internal hostnames and, in aggregate, a map of your defences. So decide deliberately which data may leave the estate: classify log sources before onboarding, consider filtering or pseudonymising high-sensitivity fields, check sector and national residency constraints against your national annex, and confirm export and exit terms so the data remains yours in practice, not just in contract; the data-and-exit sections of the MSSP checklist apply almost unchanged to SIEM SaaS. Hybrid patterns, with sensitive sources retained in a local tier and the rest in cloud, are legitimate and common.

## CIA mapping

<p class="src" markdown><span class="src-tag ocdf">OCDF</span>This framework's mapping of each capability to confidentiality, integrity and availability.</p>

| Capability | C | I | A | Rationale |
|-----------|---|---|---|-----------|
| DE-1 Log management | ○ | ● | ○ | Log **integrity** is itself a control objective, since tampered logs destroy investigations and their evidential value. |
| DE-2/DE-4 Use cases & coverage | ● | ● | ● | Exfiltration detections serve C; tampering/ransomware detections serve I/A. Balance the portfolio against your threat profile. |
| DE-3 Triage | ● | ● | ● | Severity matrix should explicitly weigh CIA impact per asset class. |
| DE-7 Integrity monitoring | ○ | ● | ○ | Direct Integrity control. |

## Roles & staffing

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span>Staffing figures are practitioner estimates; the arithmetic is under staffing and cost in document 11.</p>

- **Tier 1/2 analysts**, or a tierless model at higher maturity, for triage and investigation.
- **Detection engineers** — use case lifecycle; in small teams combined with analyst role.
- **Threat hunter** — Level 3+ capability.
- Minimum viable team for business-hours monitoring: **3–4 FTE**. One seat staffed around the clock takes roughly **5.5–6 FTE** once leave, sickness and training are counted, so a 24/7 in-house line with daytime capacity on top lands at **8–12 FTE**, and even then nights are usually a single analyst. The arithmetic, and what to do about the lone night analyst, is in [staffing and cost](11-operating-models.md#staffing-and-cost-the-arithmetic). Below that, consider hybrid or MSSP models, which is a governance decision; see GOVERN GV-5.

## Maturity criteria

<p class="src" markdown><span class="src-tag ocdf">OCDF</span>This framework's criteria, informed by the NIST CSF tiers. Not a certification standard.</p>

Maturity measures how well detection works, not how many hours a day someone watches. Coverage hours are a target set by risk; see [coverage hours are a target, not a level](08-maturity-model.md#coverage-hours-are-a-target-not-a-level). A business-hours team with strong engineering can reach Level 3 if business hours plus tested on-call is what its risk decision calls for.

| Level | Criteria |
|-------|----------|
| **1 — Initial** | Perimeter and AV alerts reviewed reactively; no central log platform or minimal sources; no documented use cases. |
| **2 — Managed** | Central log platform with priority sources 1–3 onboarded; use cases documented for the top techniques in the threat profile, each with owner, ATT&CK mapping and runbook; triage runbook; defined coverage hours with on-call. |
| **3 — Established** | Detection engineering lifecycle with version control and testing; coverage measured against ATT&CK and crown jewels; enrichment automated; regular hunting; coverage hours meet the risk-based target set in GOVERN, with out-of-hours escalation tested; MTTD tracked. |
| **4 — Optimising** | Continuous detection validation through purple teaming and emulation; detection-as-code with CI/CD; hunting output systematically converted to detections; coverage and false-positive rates trended and drive backlog. |

## EU regulatory hooks

<p class="src" markdown><span class="src-tag law">Law</span>Paraphrased from the legal texts. Check the article itself and your national law; not legal advice.</p>

- **NIS2 Art. 21(2)(b)** — incident handling implies detection capability; **Art. 23** reporting deadlines, with early warning within 24h, are only achievable with functioning detection.
- **GDPR Art. 33** — 72-hour breach notification to the supervisory authority starts at *awareness*; detection speed directly determines compliance feasibility.
- **DORA Art. 10** — financial entities must have mechanisms to promptly detect anomalous activities.
- **GDPR & employee monitoring** — security monitoring of user activity must respect data protection: define purpose limitation, retention, and access controls for security logs; involve the DPO. Log data about employees is personal data.

## External dependencies

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span>Typical dependencies from experience; yours will differ.</p>

| Dependency | Party | Type | Agree up front |
|-----------|-------|------|----------------|
| Log source enablement and forwarding | System/application owners | [HARD] | Onboarding SLA per source; the priority list above as the queue |
| SIEM hardware and OS layer, self-hosted | Infrastructure team | [HARD] | Ownership split per the SIEM section above; paging path when ingest stops |
| Network taps/span or NDR sensor placement | Network team | [HARD] | Placement plan tied to segments and blind spots |
| Approval of privacy-intrusive sources such as endpoint content and mail inspection | DPO | [GATE] | Assessment criteria and turnaround pre-agreed |
| Business context for tuning: what is normal here? | Application owners | [SOFT] | Named contact per crown jewel |

## Sources

- NIST CSF 2.0, CSWP 29: DETECT function. https://doi.org/10.6028/NIST.CSWP.29
- MITRE ATT&CK®. https://attack.mitre.org
- MITRE, *11 Strategies of a World-Class Cybersecurity Operations Center*, Knerler, Parker & Zimmerman, 2nd ed. https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center
- NIST SP 800-92, *Guide to Computer Security Log Management*.
- NIS2: Directive (EU) 2022/2555 Art. 21, 23; GDPR Art. 33; DORA Art. 10.

*Open CDC Framework, licensed CC BY 4.0. Credits: [References & credits](19-references.md).*
