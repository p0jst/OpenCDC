# ISO/IEC 27001 crosswalk

<p class="src" markdown><span class="src-tag standard">Standard</span><span class="src-tag opencdc">OpenCDC</span>Clause and control numbers from ISO/IEC 27001:2022; the mapping to capabilities is OpenCDC's. Control names are shortened, not quoted.</p>

Many European organisations in NIS2 scope already run an information security
management system on ISO/IEC 27001. This page shows where each OpenCDC capability
sits in that standard, so the CDC's work can be recorded as evidence in the ISMS
instead of beside it, and an auditor's question about a control can be answered
with a capability and its maturity criteria.

The two do different jobs. ISO/IEC 27001 says which controls an organisation
must consider and manage. OpenCDC describes how to build and run the team that
operates the detection and response part of them. A certificate says the
management system works; it says little about whether an alert at night reaches
someone who can act on it.

## Capabilities to clauses and Annex A controls

Numbers without a prefix are clauses of the standard; numbers starting with A
are controls in Annex A of the 2022 edition.

| OpenCDC capability | ISO/IEC 27001:2022 |
|-----------------|--------------------|
| GV-1 CDC charter & mandate | 5.1 leadership, 5.3 roles and authorities, A.5.2 security roles |
| GV-2 Risk management integration | 6.1 risks and opportunities, 8.2 and 8.3 risk assessment and treatment |
| GV-3 Policy framework | 5.2 policy, A.5.1 policies, A.5.37 documented operating procedures |
| GV-4 Roles & accountability | 5.3, A.5.2, A.5.3 segregation of duties, A.5.4 management responsibilities |
| GV-5 Budget & resourcing governance | 7.1 resources, 7.2 competence |
| GV-6 Supply chain risk governance | A.5.19 to A.5.22 supplier relationships, A.5.23 cloud services |
| GV-7 Oversight & reporting | 9.1 monitoring and measurement, 9.3 management review |
| ID-1 Asset inventory | A.5.9 inventory of assets, A.8.1 user endpoint devices |
| ID-2 Data classification | A.5.12 classification, A.5.13 labelling |
| ID-3 Crown-jewel analysis | 4.1 and 4.2 context and interested parties, A.5.29 and A.5.30 through the business impact analysis |
| ID-4 Vulnerability identification | A.8.8 technical vulnerabilities |
| ID-5 Threat landscape & intelligence | A.5.7 threat intelligence, A.5.6 special interest groups |
| ID-6 Risk assessment | 6.1.2 and 8.2 risk assessment |
| ID-7 Improvement identification | 10.1 continual improvement, 10.2 nonconformity and corrective action |
| PR-1 Identity & access management | A.5.15 to A.5.18 access and identity, A.8.2 privileged access, A.8.5 secure authentication |
| PR-2 Awareness & training | 7.3 awareness, A.6.3 awareness, education and training |
| PR-3 Data security | A.8.24 cryptography, A.8.12 data leakage prevention, A.8.10 and A.8.11 deletion and masking |
| PR-4 Platform hardening & secure configuration | A.8.9 configuration management, A.8.7 malware protection, A.8.19 software installation |
| PR-5 Vulnerability remediation & patching | A.8.8 technical vulnerabilities, A.8.32 change management |
| PR-6 Network security & segmentation | A.8.20 to A.8.22 network security and segregation |
| PR-7 Resilient technology infrastructure | A.8.13 backup, A.8.14 redundancy, A.8.6 capacity |
| PR-8 Secure development & change | A.8.25 to A.8.29 secure development and testing, A.8.32 change management |
| PR-9 Email & web protections | A.8.23 web filtering, A.8.7 malware protection, A.5.14 information transfer |
| DE-1 Log collection & management | A.8.15 logging, A.8.17 clock synchronisation |
| DE-2 Detection engineering | A.8.16 monitoring activities |
| DE-3 Alert triage & analysis | A.5.25 assessment and decision on events, A.6.8 event reporting |
| DE-4 Coverage assessment | 9.1 monitoring and measurement, A.8.16 |
| DE-5 Threat hunting | A.8.16, A.5.7 |
| DE-6 Detection validation | A.8.16, A.5.35 independent review, A.5.36 compliance with policies |
| DE-7 Anomaly & integrity monitoring | A.8.16, A.8.9 |
| RS-1 Incident response plan | A.5.24 incident management planning and preparation |
| RS-2 Playbooks | A.5.24, A.5.37 |
| RS-3 Incident analysis & forensics | A.5.28 collection of evidence, A.5.25 |
| RS-4 Containment & eradication | A.5.26 response to incidents |
| RS-5 Incident reporting & communication | A.5.5 contact with authorities, A.5.26, A.5.31 legal and regulatory requirements |
| RS-6 Crisis management interface | A.5.29 security during disruption |
| RS-7 Exercises | A.5.24, A.5.30 ICT readiness for business continuity |
| RC-1 Recovery planning | A.5.30, A.5.29 |
| RC-2 Trusted restoration | A.8.13, A.5.26 |
| RC-3 Recovery execution & verification | A.5.30, A.8.13 |
| RC-4 Recovery communication | A.5.26, A.5.5 |
| RC-5 Lessons learned & improvement loop | A.5.27 learning from incidents, 10.2 |
| RC-6 Business continuity integration | A.5.29, A.5.30 |

## What the standard leaves to you

ISO/IEC 27001 names monitoring, incident management and threat intelligence as
controls and stops there. These are the places where OpenCDC adds the operating
detail an ISMS usually lacks:

- **A.8.16 monitoring** is one control. In OpenCDC it is five capabilities, DE-2 and DE-4 to DE-7, because writing detections, measuring coverage, hunting and validating are different jobs with different owners.
- **A.5.24 to A.5.28 incident management** describe a process. Who may isolate a production system at night, and who decides when the response ends, are in GV-1 and RS-4 and in the [charter](../templates/cdc-charter-template.md).
- **Statutory reporting** appears only as contact with authorities and legal requirements. The clocks are in [Respond](respond.md#eu-statutory-reporting-timelines).
- **Coverage hours and staffing** are not controls at all. They are in [operating models](operating-models.md).

## Using it

- **Running an ISMS?** Put the capability ID in the Statement of Applicability next to the control it serves, and use the maturity criteria as the measure of effectiveness that clause 9.1 asks for.
- **Preparing for an audit?** The evidence recorded in the [maturity self-assessment](../assessments/maturity-self-assessment.md) is evidence for the mapped controls. Record it once.
- **Certified, and in NIS2 scope?** A certificate supports the Art. 21 measures but does not show them. Use the [NIS2 Article 21 crosswalk](nis2-article-21-crosswalk.md) for the legal mapping; ENISA's technical implementation guidance carries its own table from the NIS2 measures to ISO/IEC 27001.
- **For incident management in depth,** the companion standard is ISO/IEC 27035. OpenCDC's incident flow in [Respond](respond.md#how-an-incident-moves) fits inside its phases.

The mapping is at control level and is OpenCDC's reading. A control can
be met in ways OpenCDC does not describe, and a capability at Level 2 does not by
itself satisfy an auditor for the mapped control.

## Sources

- ISO/IEC 27001:2022, *Information security, cybersecurity and privacy protection: Information security management systems: Requirements*. https://www.iso.org/standard/27001
- ISO/IEC 27002:2022, *Information security controls*, for the guidance behind each Annex A control.
- ISO/IEC 27035-1:2023, *Information security incident management, Part 1: Principles and process*.
- ENISA, *NIS2 Technical Implementation Guidance*, June 2025, with a mapping table to ISO/IEC 27001. https://www.enisa.europa.eu/publications/nis2-technical-implementation-guidance

*OpenCDC, licensed CC BY 4.0. Credits: [References & credits](references.md).*
