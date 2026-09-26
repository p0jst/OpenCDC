# NIST CSF 2.0 Crosswalk

<p class="src" markdown><span class="src-tag standard">Standard</span><span class="src-tag ocdf">OCDF</span>Categories from NIST CSF 2.0; the mapping to capabilities is this framework's.</p>

OCDF takes its six functions from NIST CSF 2.0, but breaks each function into its
own capabilities, `GV-1` to `RC-6`, rather than reusing the CSF's 22 categories.
The IDs look alike and mean different things: OCDF's `PR-1` is a capability,
CSF's `PR.AA` is a category. This page maps one onto the other, so an assessment
in either language can be read in the other.

The mapping is at category level. CSF subcategories are finer than OCDF
capabilities, and a subcategory-level mapping would suggest a precision the
framework does not claim. Every OCDF capability appears at least once below.

| CSF 2.0 category | What it covers | OCDF capabilities |
|------------------|----------------|-------------------|
| **GV.OC** Organizational Context | Mission, stakeholders, legal and regulatory requirements, critical services | GV-1, GV-2, ID-3 |
| **GV.RM** Risk Management Strategy | Risk appetite, tolerance and the strategy that applies them | GV-2 |
| **GV.RR** Roles, Responsibilities, and Authorities | Accountability, leadership, resourcing and roles | GV-4, GV-5 |
| **GV.PO** Policy | Cybersecurity policy, established, communicated and reviewed | GV-3 |
| **GV.OV** Oversight | Results of risk management used to adjust strategy | GV-7 |
| **GV.SC** Cybersecurity Supply Chain Risk Management | Supplier requirements, due diligence and monitoring | GV-6 |
| **ID.AM** Asset Management | Hardware, software, services, data and their criticality | ID-1, ID-2, ID-3 |
| **ID.RA** Risk Assessment | Vulnerabilities, threat intelligence, threats and their likelihood and impact | ID-4, ID-5, ID-6 |
| **ID.IM** Improvement | Improvements from evaluations, tests, exercises and operations | ID-7, DE-4, DE-6, RS-7, RC-5 |
| **PR.AA** Identity Management, Authentication, and Access Control | Identities, authentication and least privilege | PR-1 |
| **PR.AT** Awareness and Training | Awareness and role-based training | PR-2 |
| **PR.DS** Data Security | Data at rest, in transit and in use; backups | PR-3, PR-7 |
| **PR.PS** Platform Security | Configuration, software maintenance, logging, secure development | PR-4, PR-5, PR-8, PR-9 |
| **PR.IR** Technology Infrastructure Resilience | Network protection, resilience and capacity | PR-6, PR-7 |
| **DE.CM** Continuous Monitoring | Monitoring networks, users, services and technology for adverse events | DE-1, DE-7 |
| **DE.AE** Adverse Event Analysis | Analysing, correlating and declaring incidents | DE-2, DE-3, DE-5 |
| **RS.MA** Incident Management | Executing the response plan, triage, escalation | RS-1, RS-2, RS-6 |
| **RS.AN** Incident Analysis | Investigation, root cause, evidence integrity | RS-3 |
| **RS.CO** Incident Response Reporting and Communication | Notifying stakeholders and authorities | RS-5 |
| **RS.MI** Incident Mitigation | Containment and eradication | RS-4 |
| **RC.RP** Incident Recovery Plan Execution | Restoring assets, verifying integrity, declaring recovery | RC-1, RC-2, RC-3, RC-6 |
| **RC.CO** Incident Recovery Communication | Communicating recovery activities and progress | RC-4 |

## Using it

- **Arriving with a CSF assessment?** Its category results are a starting
  hypothesis for the OCDF criteria under the mapped capabilities. Carry the
  evidence across and score the criteria directly, as for SOC-CMM in the
  [maturity model](maturity-model.md#reusing-an-existing-soc-cmm-or-sim3-assessment).
- **Reporting to someone who speaks CSF?** Report the OCDF function levels, which
  are the CSF functions, and use this table when they ask where a category sits.
- **Profiles.** CSF 2.0 builds current and target *profiles* from categories; an
  OCDF self-assessment with targets per function is the same idea at function
  level.

## Sources

- NIST, *The NIST Cybersecurity Framework (CSF) 2.0*, NIST CSWP 29, February 2024. https://doi.org/10.6028/NIST.CSWP.29

*Open CDC Framework, licensed CC BY 4.0. Credits: [References & credits](references.md).*
