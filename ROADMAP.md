# Roadmap

## v1.0.0 — current, released 2026-09-02
Core framework: six CSF 2.0 functions with CIA mapping, maturity criteria, EU hooks and external-dependency tables. Design layer: start-here prioritisation, E/S/A tiers, operating models including MSSP and shared CDCs, ECSF-based roles. Operations layer: tuning, detection-as-code with its deep dive, the CTI deep dive, automation guardrails, tool discipline. Community layer: RFC 2350, TF-CSIRT/FIRST, SIM3 crosswalk, controls register, annual calendar. Regulatory layer: EU landscape, 27 national annexes, interactive law selector, CIS Controls crosswalk. Practical assets: 9 templates, 4 platform playbooks, design navigator, maturity self-assessment. Plus a published website with three dependency-free browser tools: regulatory profile selector, team skill matrix and maturity self-assessment.

## v0.2
- [ ] More platform playbooks. Candidates: Kubernetes/container platforms, network devices, hypervisors, Microsoft 365 / Entra ID tenants, and a general cloud-workload playbook
- [ ] Scenario playbooks: take the three attack-based drafts (identity compromise, business email compromise, ransomware) out of draft after field review, then add insider data theft, supplier compromise and cloud-tenant takeover
- [ ] Build script: generate per-profile Markdown and PDF from law tags
- [ ] Machine-readable maturity assessment in YAML, plus a scoring script

## v0.3
- [ ] Crosswalks: OCDF ↔ ISO/IEC 27001 Annex A ↔ NIS2 Art. 21(2)(a–j) ↔ DORA
- [ ] Non-normative tooling appendix listing open source options per capability
- [ ] First translations
- [ ] OT/ICS extension profile: the IT/OT boundary, safety-first containment, OT monitoring and CER alignment. Moved up from "Later"; until it ships, see [If you run critical infrastructure](ABOUT.md#if-you-run-critical-infrastructure)
- [ ] Verify the SOC-CMM → OCDF mapping in the [maturity model](docs/08-maturity-model.md#reusing-an-existing-soc-cmm-or-sim3-assessment) against the current SOC-CMM release, and calibrate the score translation with teams that have run both
- [ ] A named second reviewer for every national annex

## Later
- [ ] AI/agent platform profile: detection and response for AI agents, MCP servers and agent skills, once the standards settle. Tracking the OWASP Agentic Skills Top 10, at incubator stage with v1.0 in public review as of 2026, and not yet stable enough to build normative guidance on.
- [ ] Cloud-native CDC profile
- [ ] Community maturity benchmark, anonymised
