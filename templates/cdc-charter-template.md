# CDC charter template

> Related capability: GV-1. Delete guidance in blockquotes before publishing.

| Document owner | Approved by | Version and date | Review cycle |
|----------------|-------------|------------------|--------------|
|  |  |  | Annually |

## 1. Mission
> One paragraph: why does the CDC exist, in business terms.

The Cyber Defence Center protects the confidentiality, integrity and availability of [ORGANISATION]'s information, systems and services by governing, preventing, detecting, responding to and recovering from cyber threats.

- **Why now:** the reason this charter is written today, such as a law that applies, an incident, a request from the board or a customer, or the wish to run the team better: …

## 2. Scope
- **Organisational scope:** legal entities / business units covered: …
- **Geographical scope / jurisdictions:** … This drives the regulatory reporting map.
- **Technical scope:** on-prem / cloud / OT / SaaS / endpoints: …
- **Explicitly out of scope:** …, and who covers it

## 3. Services provided
> Align with FIRST CSIRT Services Framework categories where useful.

| Service | Coverage hours | SLA/OLA |
|---------|---------------|---------|
| Security monitoring & triage | e.g., 24/7 or 8×5 + on-call | e.g., P1 acknowledged ≤ 15 min |
| Incident response | | |
| Threat intelligence | | |
| Vulnerability management | | |
| Detection engineering | | |
| Security advisory | | |

## 4. Authority
> The most important section. Without pre-agreed authority, response stalls.

The CDC is authorised, without prior approval, to:

- [ ] Isolate endpoints and servers up to tier [X] criticality
- [ ] Disable user and service accounts on confirmed compromise
- [ ] Block network indicators, whether IP, domain or hash, at security controls
- [ ] Access logs and forensic data on any in-scope system, subject to the data-handling rules in §7

Actions a provider may take on the CDC's behalf without prior approval, if a provider is used: … List them here, no wider than the list above, and match the provider contract.

Actions requiring approval from [ROLE]:

- [ ] Isolation of tier-1 crown-jewel production services
- [ ] External statutory notifications, with approval by legal and the DPO, and execution by the CDC
- [ ] Engagement of external DFIR retainer

A decision taken within this authority, on the information available at the time and recorded in the incident's decision log, is supported by management whatever the outcome. Post-incident reviews judge the decision against what was known when it was made, not against how the incident ended.

## 5. Reporting line & governance
- CDC Director reports to: …
- Executive reporting: [cadence] to [body], covering maturity, incidents, risk and KPIs.
- Escalation to crisis management when: … State the criteria here.

## 6. Resourcing
- Approved headcount and roles: …
- Sourcing model: in-house / hybrid / MSSP for [functions]
- Implementation tier and twelve-month ambition: Essential, Standard or Advanced, and the maturity level aimed for in twelve months: …
- Budget cycle and owner: …

## 7. Data handling & privacy
- Legal basis and purpose limitation for security monitoring data: …
- Retention: security logs [X months], case data [X years]
- Access to monitoring data restricted to: …; DPO consulted on new intrusive sources.
- Information sharing: FIRST's TLP 2.0 is used for all shared threat information.

## 8. Interfaces
| Party | Interface |
|-------|-----------|
| IT operations / infrastructure | containment execution, restoration; hardware & OS ownership for the monitoring platform, covering patching SLA and capacity; application layer owned by the CDC |
| Legal / DPO | breach assessment, notifications |
| Communications | external comms during incidents |
| National CSIRT | NIS2 reporting, advisories |
| HR | insider cases, disciplinary process |

## 9. Review
This charter is reviewed [annually] and after any major incident or organisational change.

---
*Template from OpenCDC, licensed CC BY 4.0.*
