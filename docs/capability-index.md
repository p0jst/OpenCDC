# Capability Index

Every capability in the framework, with the document that defines it and the
lowest [implementation tier](10-tiers.md) that should adopt it. The framework
addresses capabilities by ID throughout, so this is the page to come back to
whenever a reference like `PR-7` or `DE-4` appears and you want the detail.

Tier column: **E** Essential, **S** Standard, **A** Advanced. Higher tiers
include everything below them, so an S-tier CDC adopts the E rows too.

| ID | Capability | Function | Tier |
|----|------------|----------|------|
| **GV-1** | CDC charter & mandate | [GOVERN](01-govern.md) | E |
| **GV-2** | Risk management integration | [GOVERN](01-govern.md) | S |
| **GV-3** | Policy framework | [GOVERN](01-govern.md) | E |
| **GV-4** | Roles & accountability | [GOVERN](01-govern.md) | E |
| **GV-5** | Budget & resourcing governance | [GOVERN](01-govern.md) | S |
| **GV-6** | Supply chain risk governance | [GOVERN](01-govern.md) | S |
| **GV-7** | Oversight & reporting | [GOVERN](01-govern.md) | E |
| **ID-1** | Asset inventory | [IDENTIFY](02-identify.md) | E |
| **ID-2** | Data classification | [IDENTIFY](02-identify.md) | S |
| **ID-3** | Crown-jewel analysis | [IDENTIFY](02-identify.md) | E |
| **ID-4** | Vulnerability identification | [IDENTIFY](02-identify.md) | E |
| **ID-5** | Threat landscape & intelligence | [IDENTIFY](02-identify.md) | S |
| **ID-6** | Risk assessment | [IDENTIFY](02-identify.md) | S |
| **ID-7** | Improvement identification | [IDENTIFY](02-identify.md) | S |
| **PR-1** | Identity & access management | [PROTECT](03-protect.md) | E |
| **PR-2** | Awareness & training | [PROTECT](03-protect.md) | E |
| **PR-3** | Data security | [PROTECT](03-protect.md) | S |
| **PR-4** | Platform hardening & secure configuration | [PROTECT](03-protect.md) | S |
| **PR-5** | Vulnerability remediation & patching | [PROTECT](03-protect.md) | E |
| **PR-6** | Network security & segmentation | [PROTECT](03-protect.md) | S |
| **PR-7** | Resilient technology infrastructure | [PROTECT](03-protect.md) | E |
| **PR-8** | Secure development & change | [PROTECT](03-protect.md) | A |
| **PR-9** | Email & web protections | [PROTECT](03-protect.md) | E |
| **DE-1** | Log collection & management | [DETECT](04-detect.md) | E |
| **DE-2** | Detection engineering | [DETECT](04-detect.md) | S |
| **DE-3** | Alert triage & analysis | [DETECT](04-detect.md) | E |
| **DE-4** | Coverage assessment | [DETECT](04-detect.md) | S |
| **DE-5** | Threat hunting | [DETECT](04-detect.md) | A |
| **DE-6** | Detection validation | [DETECT](04-detect.md) | A |
| **DE-7** | Anomaly & integrity monitoring | [DETECT](04-detect.md) | S |
| **RS-1** | Incident response plan | [RESPOND](05-respond.md) | E |
| **RS-2** | Playbooks | [RESPOND](05-respond.md) | E |
| **RS-3** | Incident analysis & forensics | [RESPOND](05-respond.md) | S |
| **RS-4** | Containment & eradication | [RESPOND](05-respond.md) | S |
| **RS-5** | Incident reporting & communication | [RESPOND](05-respond.md) | E |
| **RS-6** | Crisis management interface | [RESPOND](05-respond.md) | A |
| **RS-7** | Exercises | [RESPOND](05-respond.md) | S |
| **RC-1** | Recovery planning | [RECOVER](06-recover.md) | E |
| **RC-2** | Trusted restoration | [RECOVER](06-recover.md) | S |
| **RC-3** | Recovery execution & verification | [RECOVER](06-recover.md) | S |
| **RC-4** | Recovery communication | [RECOVER](06-recover.md) | E |
| **RC-5** | Lessons learned & improvement loop | [RECOVER](06-recover.md) | E |
| **RC-6** | Business continuity integration | [RECOVER](06-recover.md) | S |

## Related indexes

- [Reading guide](README.md) for the order the documents are meant to be read in.
- [Implementation tiers](10-tiers.md) for what E, S and A mean and how to pick yours.
- [Maturity model](08-maturity-model.md) for how well you run the capabilities you have adopted.
- [CIS Controls crosswalk](18-cis-controls-crosswalk.md) to map these capabilities onto CIS Controls v8.1.

*Open CDC Framework, licensed CC BY 4.0. Generated from the capability tables in documents 01 to 06.*
