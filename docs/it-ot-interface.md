# The IT/OT Interface

<p class="src" markdown><span class="src-tag ocdf">OCDF</span><span class="src-tag practitioner">Practitioner</span><span class="src-tag law">Law</span>The split of responsibilities and the boundary controls are this framework's and come from running a CDC for critical infrastructure; the Danish energy rules are paraphrased from BEK 260. Not legal advice.</p>

> **This is not an OT profile.** OCDF stays scoped to enterprise IT. This document defines what a CDC owns at the boundary to operational technology, and how it hands over to the people who run the plant, the grid or the network. It exists because the law does not split IT from OT, and because most attacks on OT arrive through IT. Everything below the IT/OT DMZ remains outside OCDF; use IEC 62443, NIST SP 800-82 and your vendors' procedures there.

## Why the boundary is the CDC's problem

Three facts put the boundary inside the CDC's scope, even when OT itself is not.

- **The law regulates the entity, not a network.** NIS2 Art. 21 asks for measures that protect the network and information systems the entity uses to provide its services. For a utility, those are largely OT. In Denmark, the energy-sector act and BEK 260 make no IT/OT distinction at all; see [Danish energy sector](#danish-energy-sector-what-this-covers-and-what-it-does-not) below.
- **The reporting clock does not care where the incident started.** The 24 h early warning runs from the moment the entity becomes aware. If the operator in the control room notices first, the clock is already running, and the CDC is usually the function that owns the report.
- **Attacks cross the boundary from the IT side.** Identity, remote access, supplier connections, engineering workstations and the historian layer are the usual paths. Protecting those paths is ordinary CDC work, done with the capabilities OCDF already describes.

A CDC that stops at the IT edge without saying so leaves management believing the regulated scope is covered. Write the boundary into the charter instead, per [GV-1](govern.md) and navigator question G2.

## Who owns what

The principle: **the CDC watches and advises across the boundary; the OT operator decides below it.** In OT, safety and availability outrank evidence, and the people accountable for the physical process must hold that decision.

| Area | CDC | OT operations | Agreed jointly |
|------|-----|---------------|----------------|
| Conduit register | Maintains it, verifies it against observed traffic | Confirms purpose and owner of each conduit | Review cadence, at least yearly |
| Monitoring of the boundary zone | Owns log sources, detections and triage | Provides context, maintenance windows and vendor schedules | Which OT events are forwarded to the CDC |
| Monitoring inside OT | — | Owns it, or its specialist provider does | How OT alerts reach the CDC's reporting owner |
| Containment on the IT side of the DMZ | Acts within its mandate, per the containment catalogue | Informed without delay | Actions that change OT availability, see below |
| Containment below the DMZ | Advises | Decides and executes | The decision path and who is on call |
| Statutory reporting | Owns the report and the clock | Supplies facts on operational impact | One named reporting owner per incident |
| Exercises | Plans the cyber scenario | Plans the operational consequences | At least one joint exercise a year |

Record the split in the [CDC charter](../templates/cdc-charter-template.md) §2 and §4, and give both sides a named deputy. An agreement that exists only between two managers fails the first time one of them is on holiday.

## The boundary zone

The boundary zone is everything that connects IT to OT, or lets a person or supplier reach OT from outside it. In most estates it includes:

- the IT/OT DMZ and its firewalls
- jump hosts and remote-access gateways used to reach OT, including vendor and out-of-band access
- engineering workstations and the accounts used on them
- historians, data diodes and the replication paths that feed IT from OT
- file transfer points, patch staging and anti-malware update servers serving OT
- directory trusts and any identity shared between IT and OT
- backup systems that hold OT configurations and project files

### Conduit register

Keep a register with one row per conduit. It is the IT/OT extension of the asset inventory in [ID-1](identify.md), and the scope of your segmentation work in [PR-6](protect.md).

| Field | Example |
|-------|---------|
| Conduit ID | CDT-07 |
| From and to | IT server VLAN to OT DMZ historian |
| Direction and protocols | Outbound from OT only, OPC UA over TLS |
| Purpose | Production data for planning and billing |
| Business owner and technical owner | Named people, not teams |
| Remote party | Supplier name, where one is involved |
| Monitoring source | DMZ firewall logs, historian authentication log |
| Last verified | Date, and how: observed traffic or configuration review |

A conduit that carries traffic but has no row is a finding. A row that has seen no traffic for a year is a candidate for closure.

### What to monitor first

Onboard the boundary in this order. Each source protects the paths into OT without requiring OT expertise in the CDC.

| Priority | Log source | What it shows | Capability |
|----------|------------|---------------|------------|
| 1 | Remote-access gateways and jump hosts | Who connected to OT, from where, when, and for how long | [DE-1](detect.md) |
| 2 | Identity for accounts with OT DMZ access | Logons, new privileges, changes to group membership | [DE-1](detect.md), [PR-1](protect.md) |
| 3 | IT/OT DMZ firewalls | New flows, denied flows, rule changes | [DE-1](detect.md), [PR-6](protect.md) |
| 4 | Engineering workstations | Process, script and USB activity; project file changes | [DE-1](detect.md) |
| 5 | File transfer and update servers serving OT | What was moved into OT, and by whom | [DE-1](detect.md) |

### Detections at the boundary

Start with a small set that fits the boundary's low noise. Traffic across a well-run conduit is regular, so deviations are meaningful.

- a remote session to OT outside an agreed maintenance window, or from an unexpected source
- an IT credential, or a credential used in IT the same day, logging on in the OT DMZ
- a flow across a conduit that is not in the register, or in the wrong direction
- a change to a DMZ firewall rule without a matching change record
- an engineering workstation running tools it does not normally run, or reaching the internet
- a supplier account used by more than one person, or active after the supplier's work order closed

Map them in [detection-as-code](detection-as-code-deep-dive.md) like any other rule. For techniques beyond the boundary, MITRE ATT&CK for ICS is the appropriate matrix; OCDF's ATT&CK coverage work covers the enterprise matrix only.

## Escalation and joint incident handling

Agree in advance what makes the CDC call OT operations, and what makes OT operations call the CDC. Both lists belong in the [incident response plan](../templates/incident-response-plan-template.md).

**The CDC escalates to OT operations** when an incident touches an account, host or conduit in the boundary zone, when a supplier with OT access is compromised, or when a major IT incident may require separating IT from OT.

**OT operations escalates to the CDC** when it sees an event it cannot explain as a fault: unexpected setpoint or logic changes, loss of view or control, unknown devices, or remote sessions no one requested. The operator does not need to decide whether it is a cyber incident. That is the CDC's job, and the reporting clock is why the call must come early.

During a joint incident, run one bridge with a CDC incident lead and an OT lead. The CDC lead owns investigation and reporting; the OT lead owns every decision that affects the physical process. Escalation into crisis management follows [RS-6](respond.md).

## Containment across the boundary

Extend the [containment action catalogue](../templates/containment-action-catalogue-template.md) with a boundary section. The rows below are a starting set; the decisive column is who decides.

| ID | Action | Decided by | Precondition | Notes |
|----|--------|------------|--------------|-------|
| OTX-01 | Disable supplier or vendor remote access to OT | CDC, OT informed | None | Enumerate every path in the conduit register first; CON-12 covers the IT side |
| OTX-02 | Disable or reset IT accounts with OT DMZ access | CDC, OT informed | Check that no running operation depends on a logged-on session | Service accounts need the OT technical owner |
| OTX-03 | Block a single conduit at the DMZ firewall | CDC with OT approval | OT confirms the process tolerates loss of that data flow | A historian feed is usually safe to cut; a control path is not |
| OTX-04 | Isolate an engineering workstation | OT, advised by CDC | No active engineering work in progress | Preserve the project files before reimaging |
| OTX-05 | Separate IT from OT entirely | OT management | Manual or island operation is prepared and staffed | Exercise this before you need it; it is the OT equivalent of CON-11 |
| OTX-06 | Isolate, reboot, scan or image an OT asset | OT, under vendor procedure | Safety assessment | Never a CDC action; endpoint tooling and active scans can stop a process |

Write the actions the CDC may never take on its own into the charter explicitly. In an operational environment, the list of forbidden actions matters as much as the list of permitted ones.

## Reporting: who starts the clock

Awareness can arise on either side of the boundary. To avoid two partial reports or none:

1. Name one reporting owner per incident, normally the CDC incident lead, per [RS-5](respond.md).
2. Agree that OT operations passes any unexplained event to the CDC within the time your reporting duty allows, and in practice within the hour, with a timestamp for when it was first noticed. That timestamp may be your awareness time.
3. Keep report templates that include operational impact: which service, which area, how many customers, how long.
4. Check which recipients apply. Under NIS2 it is the CSIRT or competent authority; a designated critical entity also reports under CER Art. 15; national law may name a different recipient for one sector.

In Denmark, energy-sector entities report to Energistyrelsen, and to the CSIRT when network and information security was compromised; electricity, gas and hydrogen entities also alert Energinet, per BEK 260 §§ 77–79. See the [Danish annex](annexes/annex-dk.md).

## Exercises

Run at least one joint exercise a year in which an IT incident threatens to cross into OT, per [RS-7](respond.md). A useful scenario is a compromised supplier account with remote access to OT, detected by the CDC at night. It tests the conduit register, the escalation lists, the containment decisions in OTX-01 to OTX-05 and the reporting clock in one sitting. Include the OT decision-makers, not only their engineers.

## Danish energy sector: what this covers and what it does not

Lov om styrket beredskab i energisektoren and BEK 260 apply to the whole entity. This document lets a CDC show which of the cyber requirements it meets at the boundary, and which must be met by OT operations or a specialist provider. The table covers the requirements summarised in the [Danish annex](annexes/annex-dk.md); it is not a complete reading of the order.

| Requirement | Reference | Covered by OCDF with this document | Remains outside OCDF |
|-------------|-----------|------------------------------------|----------------------|
| Segmentation of supply-critical systems behind a DMZ or equivalent; physical separation at levels 4 and 5 | BEK 260 § 62 | Monitoring of the DMZ and conduits; the conduit register as evidence of what crosses | Segmentation design and the separation inside OT |
| Real-time logging, monitoring and response at levels 4 and 5, with 13 months' retention and handover within 24 h | BEK 260 §§ 66–69 | IT and the boundary zone: log sources, detections, retention, response | Monitoring of the OT networks themselves |
| Preparedness exercises, and a yearly recovery exercise of supply-critical systems at levels 4 and 5 | BEK 260 § 21 | The joint cyber exercise; the IT side of recovery | Recovery of OT systems and manual operation |
| Incident reporting to Energistyrelsen, the CSIRT and Energinet | BEK 260 §§ 77–79 | Reporting ownership, awareness time and templates | — |
| Coordinators independent of the management body at levels 4 and 5 | BEK 260 | Governance roles, per [GV-4](govern.md) | — |
| Physical security and the CER side of the regime | Lov nr. 258/2025 | — | All of it |

If your CDC is the IT security service that receives logs under §§ 66–69, confirm with Energistyrelsen and your preparedness level which systems that duty covers before you promise it.

## Checklist

- [ ] Boundary written into the CDC charter, with the actions the CDC may never take below the DMZ
- [ ] Conduit register complete, each conduit with a business and technical owner, verified against observed traffic
- [ ] Remote-access gateways, jump hosts, DMZ firewalls and engineering workstations onboarded as log sources
- [ ] Boundary detections in production and tested
- [ ] Escalation lists in both directions agreed and in the IR plan, with named on-call contacts on both sides
- [ ] Containment catalogue extended with the boundary actions and their decision owners
- [ ] One reporting owner per incident, and awareness time defined across the boundary
- [ ] Joint IT/OT exercise held in the last 12 months, with OT decision-makers present
- [ ] Energy sector: preparedness level known, and the split between OCDF and OT coverage recorded against BEK 260

## Sources

- Directive (EU) 2022/2555, NIS2, Art. 21 and 23: https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- Directive (EU) 2022/2557, CER, Art. 15: https://eur-lex.europa.eu/eli/dir/2022/2557/oj
- Lov nr. 258 af 6. marts 2025, lov om styrket beredskab i energisektoren: https://www.retsinformation.dk/eli/lta/2025/258
- BEK nr. 260 af 6. marts 2025, bekendtgørelse om modstandsdygtighed og beredskab i energisektoren: https://www.retsinformation.dk/eli/lta/2025/260
- ISA/IEC 62443 series of standards: https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards
- NIST SP 800-82 Rev. 3, *Guide to Operational Technology Security*: https://csrc.nist.gov/pubs/sp/800/82/r3/final
- MITRE ATT&CK for ICS: https://attack.mitre.org/matrices/ics/

*Open CDC Framework, licensed CC BY 4.0.*
