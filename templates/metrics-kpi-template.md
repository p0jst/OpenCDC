# CDC Metrics & KPI Catalogue — Template

> Related capabilities: GV-7, DE-4, RS-*, RC-5. Pick **few metrics you will act on** over many you will only report. Every metric below lists the decision it should drive. If you wouldn't change anything based on it, don't collect it.

## Governance & coverage — GOVERN and IDENTIFY

| Metric | Definition | Example target | Decision it drives |
|--------|-----------|------------------|--------------------|
| Asset inventory accuracy | % sampled assets correctly recorded | > 90% | Invest in discovery/CMDB reconciliation |
| Log source coverage | % of priority-1 and priority-2 sources onboarded per the docs/04 priority list | 100% P1, > 90% P2 | Onboarding backlog priority |
| Maturity score trend | OCDF level per function, assessed annually | +1 level on 2 weakest functions/yr | Budget allocation |
| Training completion | % staff / % management completing role-based training | > 95% | NIS2 Art. 20 evidence; awareness focus |

## Detection — DETECT

| Metric | Definition | Example target | Decision it drives |
|--------|-----------|------------------|--------------------|
| MTTD | Median time from first malicious activity to detection, measured per confirmed incident | Trend ↓ | Detection engineering priorities |
| ATT&CK coverage | % of the techniques in your threat profile at level 3 on the honesty scale in the [detection-as-code deep dive](../docs/14-detection-as-code-deep-dive.md) §4: detection deployed, log source live, and fired in test within 12 months | Trend ↑; always report the uncovered techniques by name | Use-case backlog |
| Detection validation rate | % production detections tested and fired in the last 12 months | 100% | Purple-team scheduling |
| False-positive rate | FP / total alerts per use case | Per-UC threshold | Tuning / retirement |
| Triage SLA adherence | % alerts acknowledged within severity SLA | > 95% | Staffing model |

## Response — RESPOND

| Metric | Definition | Example target | Decision it drives |
|--------|-----------|------------------|--------------------|
| MTTC | Median time detection → containment for P1 and P2 | Trend ↓ | Containment automation, authority gaps |
| Statutory reporting timeliness | % notifications within the legal deadline for NIS2 24h, GDPR 72h and DORA | 100% | Reporting drill frequency |
| Playbook coverage | % of P1/P2 incidents handled with an existing playbook | > 80% | Playbook backlog |
| Exercise cadence | Exercises held vs. planned, including management participation | 100% | Governance escalation |

## Recovery & learning — RECOVER

| Metric | Definition | Example target | Decision it drives |
|--------|-----------|------------------|--------------------|
| Restore test success | % crown-jewel services with successful restore test in 12 months | 100% | Backup architecture investment |
| RTO attainment | Measured recovery time vs. agreed RTO in tests/incidents | 100% within RTO | DR investment |
| Lessons-learned closure | % post-incident actions closed within due date | > 90% | Improvement-loop health, a Level 4 indicator |

## Anti-patterns — do not use these as KPIs

- **Alert volume**, as in "we handled 40,000 alerts", rewards noise.
- **Blocked attacks count** from perimeter devices, an unfalsifiable vanity metric.
- **Tickets closed per analyst** — incentivises shallow triage.
- **ATT&CK coverage across the whole matrix, or counted from rule tags alone.** A percentage of all techniques says nothing about your threats, and a tagged rule that never fired in test is not coverage.
- **Number of use cases or rules.** More rules is more to maintain, not more protection.

## Reporting cadence

- Operational dashboard: weekly, CDC internal.
- Management report: monthly, covering incidents, SLA and coverage deltas.
- Executive and board report: quarterly, covering maturity trend, top risks and statutory compliance posture.

---
*Template from the Open CDC Framework, licensed CC BY 4.0.*
