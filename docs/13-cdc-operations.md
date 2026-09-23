# 13 — Running the CDC: Tuning, Detection-as-Code, and Team Development

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span>Operating practice from running a CDC.</p>

> The build documents 01–06 describe *what* to establish. This document describes three operational loops that determine whether the CDC improves or decays after go-live. It targets S-tier and above; E-tier teams apply the tuning loop in simplified form or demand it of their MSSP.

## 1. The alert tuning loop

Untuned detection rots: alert volume grows, true-positive rate falls, analysts numb out, and the one real alert drowns. Tuning is a **workflow with governance**, not an occasional cleanup.

**The loop, on a weekly cadence:**

1. **Measure per use case:** alerts/week, true-positive rate, time-to-triage. The use-case template's metrics block is the record.
2. **Triage feedback channel:** every closed alert carries a disposition: TP, FP-tunable, FP-accepted or benign-true-positive. Analysts flag tuning candidates in one click; friction here kills the loop.
3. **Weekly tuning review, 30–60 min:** detection engineer and senior analyst walk the worst offenders: top noise, zero-fire rules, missed-detection post-mortems.
4. **Change with review:** every tuning change is a reviewed commit, as in detection-as-code, with rationale. "Who silenced this and why" must be answerable a year later.
5. **Suppression governance:** suppressions/allowlists carry an owner and an expiry date; expired suppressions resurface automatically. Unowned permanent suppressions are how real intrusions get pre-silenced.
6. **Retire honestly:** a rule that never fires and fails validation is either broken, so fix it, or worthless, so retire it. A large "just in case" rule set is operational debt.

**Guardrails:** noisy-rule tuning must not quietly narrow detection scope, so validate after tuning by firing the test again. Track the portfolio FP rate and alerts-per-analyst-shift; both trending up = intervention.

## 2. Detection-as-code

Treat detections like software, because they are.

| Practice | Concretely |
|----------|-----------|
| Version control | Every rule lives in a git repo; the SIEM is a deployment target, not the source of truth |
| Vendor-neutral format | Author in Sigma where feasible; convert per platform. Your detection portfolio then survives a SIEM migration or an MSSP exit |
| Peer review | No rule reaches production without a second pair of eyes for logic, performance and evasion |
| Testing | Each rule ships with a test: log sample or scripted attack emulation that must make it fire. CI runs tests on every change |
| CI/CD deployment | Merge to main → pipeline validates syntax, runs tests, deploys to the platform. Manual console edits are drift, so forbid them or auto-reconcile |
| Metadata as code | ATT&CK mapping, CIA objective, owner, severity, references live in the rule file, as the use-case template fields, made machine-readable |
| Runbook next to rule | Triage steps versioned alongside the detection they serve |

Full engineering manual covering repo layout, rule YAML anatomy, pipeline stages and ATT&CK coverage scoring: [Deep dive: detection-as-code](14-detection-as-code-deep-dive.md).

**Adoption path:** at S, rules in git with peer review and quarterly manual validation → at A, full CI/CD with automated tests and drift detection. Even the S step alone ends the "who changed this rule" archaeology.

## 3. Developing the team — the third loop

Roles, skills matrices and career paths live in [Roles & competences](12-roles-and-competences.md); this section is the operating cadence that keeps them real:

- **Onboarding runway:** a new analyst gets a named mentor, a 30/60/90-day plan tied to ECSF skills, and shadow-shifts before solo shifts. Throwing juniors at a live queue on day 3 is how you train your competitors' future staff.
- **Continuous practice:** monthly internal purple-team hour, where validation doubles as training · every post-incident review names a teaching point · rotate analysts through detection engineering weeks to break queue monotony.
- **Protect the night shift:** cap consecutive nights, guarantee recovery days, rotate fairly, and measure attrition and absence as leading indicators. In a capability-based model, measure on-call load per person.
- **Certification budget with direction:** map training spend to ECSF skill gaps from the twice-yearly matrix review, not to whichever course is loudest.
- **Exit interviews feed GOVERN:** attrition causes are a CDC risk register item, not an HR footnote.

## 4. Automation and AI-assisted triage — with guardrails

Automation is how a small team survives alert volume without burning out its analysts; done wrong, it automates the noise. Order of operations matters:

1. Tune first, automate second. Automating triage on an untuned rule set industrialises false positives. Run the tuning loop in §1 until the portfolio's signal quality justifies automation.
2. Automate enrichment before decisions. The highest-value, lowest-risk automation is context assembly: asset criticality, identity context, recent related alerts and intel hits, all delivered inside the alert before a human looks at it. This alone often halves triage time.
3. Automate response actions with approval gates by tier. Fully automatic for reversible, low-blast-radius actions on pre-mandated scopes, such as blocking a hash or revoking a session; human-approved for isolation of servers; never automatic on crown jewels. Mirror the containment action catalogue's mandate column.
4. AI-assisted triage is useful, with rules. Language-model assistance can summarise alert clusters, draft investigation notes, and propose verdicts. Guardrails: the model proposes, the analyst disposes, with verdicts remaining human for anything that closes as true-positive-with-impact or triggers reporting duties; log model suggestions vs. final dispositions and audit the disagreement rate; never paste sensitive case data into services outside your data-handling terms, on the same classification discipline as cloud SIEM telemetry in doc 04; and treat "auto-closed by AI" as a suppression, with owner, review sample and expiry.
5. Measure automation like a control: % alerts auto-enriched · % auto-closed with sampled QA error rate · analyst minutes saved per week · rollback count on automated actions.

A playbook that cannot be executed manually should not be automated yet. Automation encodes a working process, it does not substitute for one.

## 5. Tool portfolio discipline

Mature SOCs commonly accumulate 15–25 tools with overlapping functions and thin integrations; every extra console adds swivel-chair time, licence cost, patching surface and one more place logs die in a silo. Counter it structurally:

- Procure against capabilities, not features: every tool must map to a capability ID in this framework and name the tool it replaces or the gap it closes. "Also does X" is not a requirement match.
- One place to work: alerts from every tool land in the central platform, the SIEM or case-management system, with two-way status sync. A tool whose alerts can only be seen in its own console is a silo by construction, and its detections never enter coverage measurement, per doc 14 §4.
- Annual portfolio review, set in the annual calendar: per tool, capability served, unique telemetry or action it provides, integration status, utilisation, cost. Kill or consolidate anything failing two of five. Overlap is a decision to make consciously, not a default to drift into.
- Exit-aware from purchase: log formats exportable, detections portable through Sigma, per doc 14, API-first, on the same portability logic as the MSSP checklist.
- Count the metric: number of consoles an analyst must touch to close a median case. Target: falling.

## KPIs for these loops — add to the metrics catalogue

Portfolio FP rate trend · % suppressions with owner+expiry · % rules with passing tests · median time from tuning-flag to change · analyst attrition on a rolling 12 m · % staff with current skills-matrix review · % alerts auto-enriched · auto-close QA error rate · consoles-per-median-case.

## Sources
- Sigma project, a generic detection rule format: https://github.com/SigmaHQ/sigma
- MITRE, *11 Strategies of a World-Class Cybersecurity Operations Center*, 2nd ed., on staffing, retention and engineering.
- NIST CSF 2.0 ID.IM on improvement; the loops above are its operationalisation.

*Open CDC Framework, licensed CC BY 4.0.*
