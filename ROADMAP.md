# Roadmap

Planned work is grouped by priority, not by version number, so plans can move without renumbering. With one maintainer, *Next* is what is being worked on; *After that* depends on contributors; *Ideas* are not planned. Releases are numbered from v1.0.0 upwards when they ship; any change to a maturity criterion is listed under **Scoring changes** in the [changelog](CHANGELOG.md), so an assessment made under an earlier version can still be compared.

## Released

**v1.1.0, 23 September 2026 (current).** Landing page by role, OCDF on one page, executive guide, worked example, source labels and annex confidence levels, operating-model decision path, staffing and cost arithmetic, attack-based playbooks as drafts, owners and due dates in the maturity tool, and two changed DETECT criteria. See the [changelog](CHANGELOG.md).

**v1.0.0, 2 September 2026.** Core framework: six CSF 2.0 functions with CIA mapping, maturity criteria, EU hooks and external-dependency tables. Design layer: start-here prioritisation, E/S/A tiers, operating models including MSSP and shared CDCs, ECSF-based roles. Operations layer: tuning, detection-as-code with its deep dive, the CTI deep dive, automation guardrails, tool discipline. Community layer: RFC 2350, TF-CSIRT/FIRST, SIM3 crosswalk, controls register, annual calendar. Regulatory layer: EU landscape, 27 national annexes, interactive law selector, CIS Controls crosswalk. Practical assets: 9 templates, 4 platform playbooks, design navigator, maturity self-assessment. Plus a published website with three dependency-free browser tools: regulatory profile selector, team skill matrix and maturity self-assessment.

## Next
- [ ] More platform playbooks, Microsoft 365 / Entra ID tenants first, then network devices, hypervisors, Kubernetes/container platforms and a general cloud-workload playbook
- [ ] Scenario playbooks: take the three attack-based drafts (identity compromise, business email compromise, ransomware) out of draft after field review, then add supplier compromise, DDoS, insider data theft and cloud-tenant takeover, the scenarios RS-2 names that OCDF does not yet ship
- [ ] Build script: generate per-profile Markdown and PDF from law tags
- [ ] Machine-readable framework in YAML: capabilities, criteria, tiers and regulatory hooks, plus a scoring script. This also lets the capability index filter by regulation and maturity level, not only by function and tier
- [ ] Filled-in examples of the charter, incident response plan and quarterly report, taken from the [worked example](docs/worked-example.md)
- [ ] More worked examples at other sizes: a 50-person company with one security person, a 500-person company on a managed service, and a 20,000-person group with an in-house 24/7 line

## After that
- [ ] Community benchmark: first published figures, as groups reach ten contributions. Collection opened in v1.1.0; see [community benchmark](docs/benchmark.md)
- [ ] Crosswalks to ISO/IEC 27001 Annex A and DORA; the NIS2 Art. 21 and CSF 2.0 crosswalks shipped
- [ ] Non-normative tooling appendix listing open source options per capability
- [ ] First translations
- [ ] OT/ICS extension profile: the IT/OT boundary, safety-first containment, OT monitoring and CER alignment. Until it ships, see [If you run critical infrastructure](ABOUT.md#if-you-run-critical-infrastructure)
- [ ] Verify the SOC-CMM → OCDF mapping in the [maturity model](docs/maturity-model.md#reusing-an-existing-soc-cmm-or-sim3-assessment) against the current SOC-CMM release, and calibrate the score translation with teams that have run both
- [ ] A named second reviewer for every national annex, and the first annexes moved up to *verified against primary source*
- [ ] Cloud CDC profile: identity and Microsoft 365, the AWS, Azure and GCP control planes, workload identities, service principals and OAuth applications, CI/CD and secrets, cloud logging, short-lived workloads, CSPM/CNAPP, and cloud-native incident response

## Ideas, not planned

Kept so the thinking is not lost. None of these starts before the items above, and each needs a contributor or a clear demand.

- [ ] AI/agent platform profile: detection and response for AI agents, MCP servers and agent skills, once the standards settle. Tracking the OWASP Agentic Skills Top 10, at incubator stage with v1.0 in public review as of 2026, and not yet stable enough to build normative guidance on.
- [ ] CDC builder: answer a few questions about your organisation, such as size, country, regulation, estate and staff, and get a blueprint: the capabilities that apply, a 90-day plan, roles, KPIs, templates and a maturity target. It would be built on the machine-readable framework under *Next*, so it cannot start before that
