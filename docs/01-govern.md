# 01 — GOVERN

> *"The organization's cybersecurity risk management strategy, expectations, and policy are established, communicated, and monitored."* Paraphrased from NIST CSF 2.0, GOVERN function

## Objective

Establish the mandate, accountability, and decision-making structures that let the CDC operate with authority. GOVERN was elevated to a standalone function in CSF 2.0 precisely because technical capability without governance fails: budgets erode, escalation paths blur, and management accountability, now legally required under NIS2 Art. 20, is absent.

## Core capabilities

<p class="src" markdown><span class="src-tag standard">Standard</span><span class="src-tag ocdf">OCDF</span>Function from NIST CSF 2.0; the capability breakdown and IDs are this framework's.</p>

| ID | Capability | Description |
|----|-----------|-------------|
| GV-1 | CDC charter & mandate | A signed document defining the CDC's mission, scope covering business units, geographies and asset classes, authority such as the right to isolate systems, and reporting line. |
| GV-2 | Risk management integration | The CDC feeds into and consumes from the enterprise risk register; cyber risk appetite is defined by leadership. |
| GV-3 | Policy framework | Security policies for acceptable use, logging, access and incident response exist, are approved, versioned, and reviewed at least annually. |
| GV-4 | Roles & accountability | RACI covering CISO, CDC director, analysts, IT operations, legal/DPO, communications, and executive management. |
| GV-5 | Budget & resourcing governance | Multi-year funding model; staffing plan; sourcing strategy across in-house, hybrid and MSSP. |
| GV-6 | Supply chain risk governance | Third-party and supplier cyber risk requirements, contract clauses, and monitoring, per CSF 2.0 GV.SC and NIS2 Art. 21(2)(d). |
| GV-7 | Oversight & reporting | Regular reporting to executive management and, where applicable, the board; management approval and training obligations under NIS2 Art. 20. |

## CIA mapping

<p class="src" markdown><span class="src-tag ocdf">OCDF</span>This framework's mapping of each capability to confidentiality, integrity and availability.</p>

| Capability | C | I | A | Rationale |
|-----------|---|---|---|-----------|
| GV-1 Charter | ● | ● | ● | Governance protects all three objectives by ensuring someone is accountable for each. |
| GV-2 Risk mgmt | ● | ● | ● | Risk appetite statements should be expressed per CIA objective, such as "no tolerance for integrity loss in payment data". |
| GV-3 Policies | ● | ● | ○ | Data classification and access policies primarily serve Confidentiality and Integrity. |
| GV-6 Supply chain | ● | ● | ● | Suppliers can compromise any objective; availability of outsourced services is a distinct risk. |

*● primary, ○ secondary*

## Roles & staffing

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span>Staffing figures are practitioner estimates; the arithmetic is under staffing and cost in document 11.</p>

- **Executive sponsor**, a board member or C-level, owns cyber risk acceptance.
- **CISO / Head of Security** — owns the policy framework.
- **CDC Director / SOC Manager** — owns the charter execution and reports maturity.
- **GRC / Legal / DPO** — owns regulatory interpretation for GDPR Art. 33 breach notification and NIS2 reporting.

## Maturity criteria

<p class="src" markdown><span class="src-tag ocdf">OCDF</span>This framework's criteria, informed by the NIST CSF tiers. Not a certification standard.</p>

| Level | Criteria |
|-------|----------|
| **1 — Initial** | Informal mandate; security reports into IT; policies exist but are outdated; no defined risk appetite. |
| **2 — Managed** | Signed CDC charter; annual policy review; basic RACI; ad-hoc executive reporting. |
| **3 — Established** | Cyber risk integrated in enterprise risk management; quarterly board reporting; supply-chain security clauses in contracts; budget planned over 2+ years. |
| **4 — Optimising** | Risk-based resource allocation with quantified risk; governance KPIs trended; management trained and tested through board-level crisis exercises; continuous alignment with regulatory change. |

## EU regulatory hooks

<p class="src" markdown><span class="src-tag law">Law</span>Paraphrased from the legal texts. Check the article itself and your national law; not legal advice.</p>

- **NIS2 Directive (EU) 2022/2555, Art. 20** — management bodies must *approve* cybersecurity risk-management measures, *oversee* their implementation, and *follow training*; managers can be held liable.
- **NIS2 Art. 21(1)** — requires an "all-hazards" risk-based approach proportionate to the entity's exposure.
- **DORA (EU) 2022/2554, Art. 5** — for financial entities, the management body bears final responsibility for ICT risk management.
- **GDPR Art. 24 & 32** — controller accountability and "appropriate technical and organisational measures".
- **ENISA NCSS & sectoral guidance** — national cybersecurity strategy alignment for public bodies.

## External dependencies

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span>Typical dependencies from experience; yours will differ.</p>

| Dependency | Party | Type | Agree up front |
|-----------|-------|------|----------------|
| Cyber risk acceptance and charter sign-off | Executive sponsor / board | [GATE] | Who signs, who deputises, review cadence |
| Regulatory interpretation of NIS2, GDPR and DORA applicability | Legal / DPO | [GATE] | Turnaround time for applicability questions |
| Multi-year budget and headcount | Finance / executive management | [HARD] | Budget cycle timing; who defends the case |
| Security clauses in supplier contracts | Procurement / legal | [HARD] | Standard clause set; CDC review step in tenders |
| Role definitions and hiring support | HR | [SOFT] | Use of ECSF-based job descriptions, doc 12 |

## Sources

- NIST, *The NIST Cybersecurity Framework (CSF) 2.0*, NIST CSWP 29, February 2024. https://doi.org/10.6028/NIST.CSWP.29
- NIS2: Directive (EU) 2022/2555. https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- DORA: Regulation (EU) 2022/2554. https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- GDPR: Regulation (EU) 2016/679. https://eur-lex.europa.eu/eli/reg/2016/679/oj

*Open CDC Framework, licensed CC BY 4.0. Credits: [References & credits](19-references.md).*
