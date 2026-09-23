# 12 — Roles & Competences, built on the ENISA ECSF

<p class="src" markdown><span class="src-tag standard">Standard</span><span class="src-tag ocdf">OCDF</span>Roles built on the ENISA European Cybersecurity Skills Framework; the CDC mapping and career paths are this framework's.</p>

## Why ECSF as the backbone

This framework's role definitions, job descriptions and career paths are anchored in the **European Cybersecurity Skills Framework (ECSF)**, ENISA's set of **12 cybersecurity professional role profiles**, each defined with a mission, tasks, deliverables, key skills, key knowledge, and e-CF competences linked to EQF learning levels. Using ECSF gives a European CDC three concrete advantages:

1. **A common language** with HR, recruiters, training providers and certification bodies across the EU, where many certifications and university programmes are already mapped to ECSF profiles.
2. **Ready-made building blocks** for job descriptions; see the [ECSF job description template](../templates/job-description-template.md).
3. **Regulatory alignment:** ENISA positions the ECSF as the reference for NIS2-aligned workforce planning; using it makes your staffing evidence legible to authorities.

> **Note:** ENISA is revising the ECSF, adding proficiency levels and alignment with newer EU regulation. Check the ENISA ECSF page for the current version before publishing job descriptions; this document follows the structure of the 2022 release.

## The 12 ECSF profiles

Chief Information Security Officer (CISO) · Cyber Incident Responder · Cyber Legal, Policy & Compliance Officer · Cyber Threat Intelligence Specialist · Cybersecurity Architect · Cybersecurity Auditor · Cybersecurity Educator · Cybersecurity Implementer · Cybersecurity Researcher · Cybersecurity Risk Manager · Digital Forensics Investigator · Penetration Tester.

## Mapping CDC roles to ECSF profiles

A CDC job title rarely equals exactly one ECSF profile. Most operational roles are a **primary profile plus secondary elements**. That is by design; the ECSF User Manual explicitly supports composing profiles.

| CDC role in this framework | Primary ECSF profile | Secondary elements | Framework capabilities |
|---------------------------|----------------------|--------------------|------------------------|
| SOC Analyst, Tier 1/2 | **Cyber Incident Responder** | Cyber Threat Intelligence Specialist | DE-3, RS-1..4 |
| Detection Engineer | **Cybersecurity Implementer** | Cyber Incident Responder, Researcher | DE-1, DE-2, DE-6 |
| Threat Hunter | **Cyber Threat Intelligence Specialist** | Cyber Incident Responder | DE-5, ID-5 |
| CTI Analyst | **Cyber Threat Intelligence Specialist** | — | ID-5 |
| DFIR Specialist | **Digital Forensics Investigator** | Cyber Incident Responder | RS-3, playbooks/ |
| Vulnerability Analyst | **Cybersecurity Implementer** | Penetration Tester | ID-4, PR-5 |
| Security Engineer, platform and EDR | **Cybersecurity Implementer** | Cybersecurity Architect | PR-4, PR-6, DE-1 |
| CDC/SOC Architect | **Cybersecurity Architect** | Implementer | all functions, design |
| CDC Director / SOC Manager | **CISO, scaled** + Cybersecurity Risk Manager | Educator | GV-1..7 |
| Compliance/Reporting Officer | **Cyber Legal, Policy & Compliance Officer** | Risk Manager | GV-3, RS-5, annexes |
| Awareness/Exercise Lead | **Cybersecurity Educator** | — | PR-2, RS-7 |
| Purple/Validation Tester | **Penetration Tester** | Implementer | DE-6, PR-8 |

**Service-management layer for S/A-tier and shared CDCs:** where the CDC runs as a formal service, especially in Model D shared CDCs, add a thin service-management layer distinct from the analyst line: a *service owner* for budget, P&L and prioritisation; a *technical lead* for delivery quality, SLA adherence and the root causes of service degradation; and a *service architect* for roadmap, documentation and change. These compose from ECSF CISO/Risk Manager/Architect elements and prevent the classic failure where senior analysts absorb service management informally until both suffer.

**Minimum viable CDC at Essential tier:** 3–4 people covering Incident Responder, Implementer, and a manager carrying Risk Manager and Compliance elements, with DFIR and Penetration Tester bought as retainers. The ECSF composition model is what makes such multi-hat roles describable and trainable rather than accidental.

## Skills matrix — per person, per profile

For each team member, record against their primary ECSF profile:

| Dimension | Source | Levels |
|-----------|--------|--------|
| ECSF key skills | ECSF Role Profiles doc, per profile | none / basic / proficient / can mentor |
| ECSF key knowledge | ECSF Role Profiles doc | same scale |
| e-CF competences | listed per profile, such as C.4 Problem Management for Incident Responder | e-1..e-5 |
| Platform-specific skills | your stack: SIEM query language, EDR, cloud | same scale |

Review twice yearly; gaps drive the training budget and the exercise programme. **Career paths follow profile adjacency:** Tier 1 → Tier 2, deepening Incident Responder → Detection Engineer as Implementer, or Threat Hunter as CTI Specialist → Architect or Manager. Published paths are your cheapest retention tool in the EU talent market.

## Team skill mapping — from self-assessment to team picture

The skills matrix above is a per-person exercise. To turn it into a **team picture** showing where the gaps are, who can mentor whom, and what to look for in your next hire, the framework ships a ready-made loop:

1. **Distribute** the self-assessment sheet to every team member: [`templates/skill-self-assessment.xlsx`](../templates/skill-self-assessment.xlsx), or the [CSV version](../templates/skill-self-assessment.csv) for plain-text environments. It covers **50 skills in 8 domains**, being the six CSF functions plus *Platform & Automation* and *Professional Skills*, rated on the framework scale of 0 none · 1 basic · 2 proficient · 3 can mentor, plus a "want to grow?" flag per skill. Filling it in takes about 15 minutes. Skill IDs have two digits, such as `GV-01`; they are grouped by function but are not the capability IDs such as `GV-1` used elsewhere in the framework.
2. **Collect** the returned files and upload them into [`tools/skill-matrix.html`](../tools/skill-matrix.html), the interactive Team Skill Matrix, Tool 02. Uploads are cumulative: each file adds or **updates** one person, so re-running the exercise simply overlays the new answers on the old ones. All data stays in the manager's browser; nothing is sent anywhere.
3. **Read** the four views the tool produces:
   - **Team heatmap** — who can do what, per-skill coverage, *bus factor 1* flags where only one person is proficient, and *nobody proficient* flags on skills the team's roles need;
   - **Gap analysis** — each person against the **target level for their role**. Defaults are derived from the role table above; adjust them to your organisation in the tool;
   - **Actions** — a train / mentor / hire triage: motivated learners below target, in-house mentor pairings of a level-3 person with a colleague who has a gap, and skills nobody holds that should shape the next job description or MSSP contract;
   - **Role targets** — the editable expectation matrix itself.

**Cadence:** run the exercise at the twice-yearly review, after every significant team change, and before drafting a hiring plan or training budget. Export a JSON snapshot from the tool per round to track progression over time.

**Ground rules that make it work:** answers are self-assessed and *developmental*. Never use them for performance evaluation or ranking, say so explicitly when distributing the sheet, and let people see their own data. Under GDPR, skill records are personal data: state the purpose, which is competence development and staffing, keep access to the uploaded set limited to the direct manager, and delete superseded snapshots. Managers who want an independent check can validate self-ratings in the next 1:1 or through the exercise programme rather than by editing the sheets.

Hiring hook: a skill flagged *nobody proficient*, or *bus factor 1* on a critical capability, goes verbatim into the key-skills section of the [job description template](../templates/job-description-template.md), or into the [MSSP requirements checklist](../templates/mssp-requirements-checklist.md) if you buy it as a service instead.

## Hiring with ECSF

1. Pick the primary profile + secondary elements from the table above.
2. Generate the job description from the [template](../templates/job-description-template.md); mission and tasks come almost verbatim from the ECSF profile, customised with your scope.
3. Screen against ECSF key skills/knowledge, not tool-brand checklists. Tools change, competences transfer.
4. State the EQF/e-CF level honestly; over-levelled ads are why junior-friendly roles get zero junior applicants.

## Sources

- ENISA, *European Cybersecurity Skills Framework (ECSF): Role Profiles*, September 2022. https://www.enisa.europa.eu/publications/european-cybersecurity-skills-framework-role-profiles
- ENISA, *ECSF User Manual*, September 2022. https://www.enisa.europa.eu/publications/european-cybersecurity-skills-framework-ecsf-user-manual
- ENISA ECSF topic page with the current version, xlsx and json downloads, and translations: https://www.enisa.europa.eu/topics/skills-and-competences/skills-development/european-cybersecurity-skills-framework-ecsf
- European e-Competence Framework (e-CF, EN 16234-1) and European Qualifications Framework (EQF), the competence and level systems ECSF builds on.

*Open CDC Framework, licensed CC BY 4.0. ECSF © ENISA, referenced with attribution; ENISA does not endorse this project.*
