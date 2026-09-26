# OCDF on one page

<p class="src" markdown><span class="src-tag ocdf">OCDF</span>A summary of this framework's terms.</p>

The framework uses a handful of ideas many times over. Learn these and every
other page reads faster.

## How the pieces fit

1. **Pick a tier** (Essential, Standard or Advanced). It decides *which*
   capabilities apply to an organisation of your size and exposure.
2. **Build the capabilities** in the six functions, in the order the
   [first 90 days](start-here.md) sets out, people and process before tools.
3. **Measure how well you run them** on four maturity levels, criterion by
   criterion, with evidence.
4. **Give every gap an owner and a date**, and reassess once a year.

Around all of it sit two lenses: the **CIA triad**, which says what each
capability protects, and the **regulatory layer**, which says which laws
require it.

## The terms

| Term | What it means | Where it lives |
|------|---------------|----------------|
| **CDC** | Cyber Defence Center: the organisational capability that governs, prevents, detects, responds and recovers. Used interchangeably with SOC here. | [Introduction](introduction.md) |
| **Six functions** | Govern, Identify, Protect, Detect, Respond, Recover, taken from NIST CSF 2.0. Govern sits above the other five. | [Govern](govern.md) to [Recover](recover.md) |
| **Capability** | Something the CDC must be able to do, with an ID such as `DE-2` (detection engineering). 43 in total. | [Capability index](capability-index.md) |
| **Tier E · S · A** | Essential, Standard, Advanced. Which capabilities apply at your size. Higher tiers include the lower ones. | [Implementation tiers](tiers.md) |
| **Level 1–4** | Initial, Managed, Established, Optimising. How well you run the capabilities you have. Staged: a level counts only when every criterion at it and below is met. Level 2 contains the NIS2 floor. | [Maturity model](maturity-model.md) |
| **Criterion status** | Each maturity criterion is scored on five states, from *not considered* to *implemented & evidenced*. Only the top two count, or only the top one with evidence-based scoring. | [Scoring method](maturity-model.md#criterion-status-scale) |
| **Evidence** | The document, export or test result that proves a criterion. Without it, a self-assessment is an opinion. | [Self-assessment tool](../tools/maturity-assessment.html) |
| **Operating model** | Who runs the watch: a provider (A), an in-house tiered SOC (B), an in-house capability-based team (C), a hybrid, or a shared CDC (D). | [Operating models](operating-models.md) |
| **[GATE] [HARD] [SOFT]** | How much a capability depends on another department: a decision it must take, work it must do, or input that improves the result. | [Introduction](introduction.md#dependency-markers-gate-hard-soft) |
| **CIA mapping** | Whether a capability mainly protects confidentiality, integrity or availability. | [CIA triad](cia-triad.md) |
| **Regulatory hooks** | The NIS2, GDPR, DORA and related articles each function helps you meet. | Each function document; [NIS2 Article 21 crosswalk](nis2-article-21-crosswalk.md); [EU landscape](eu-regulatory-landscape.md) |
| **National annex** | NIS2 status, authorities and reporting channels for one member state. | [Annexes](annexes/README.md) |
| **ECSF roles** | The European Cybersecurity Skills Framework profiles the CDC's roles are built on. | [Roles & competences](roles-and-competences.md) |
| **Source labels** | Law · Standard · Guidance · OCDF · Practitioner: where a statement's authority comes from. | [Why trust this framework](trust.md) |

## What you get

- **Guidance:** the six function documents, the build order, operating models,
  roles, and deep dives on running the CDC, detection-as-code and threat
  intelligence.
- **Templates:** charter, incident response plan, detection use case, metrics,
  job description, MSSP checklist, containment actions, controls register and
  annual calendar. [All templates](../templates/index.md)
- **Playbooks:** three by attack and four by platform. [Playbooks](../playbooks/README.md)
- **Browser tools:** regulatory profile selector, team skill matrix and maturity
  self-assessment. [Tools](../tools/README.md)
- **A worked example** of a fictional organisation using all of the above.
  [Worked example](worked-example.md)

## Three rules the whole framework follows

1. **Mandate before machinery.** Authority, scope and budget come before tools.
2. **Evidence over assertion.** A capability that cannot be shown to work does
   not count.
3. **Balanced beats spiky.** Level 2 in every function is worth more than Level 4
   detection on top of Level 1 governance, because the functions depend on each
   other: detection is wasted without the authority to contain and the backups to
   recover. For a NIS2 entity, Level 2 everywhere is also the legal floor.

*Open CDC Framework, licensed CC BY 4.0.*
