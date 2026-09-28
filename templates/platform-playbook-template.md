# Platform Response & Forensics Playbook — Template

> Related capabilities: RS-3, RS-4, DE-3. One playbook per platform you have to investigate, for example your standard laptop image, your server operating systems, your domain controllers and your cloud tenant. Scenario playbooks point here when the work moves to a specific host. Copy this file once per platform, fill in every `[…]`, and delete the guidance lines in italics when you are done. Test every collection step on your own standard build before an incident, not during one.

## Metadata

| Field | Value |
|-------|-------|
| ID | PB-[XX] |
| Platform | [e.g. Windows 11 laptop, standard image vX] |
| Owner | [named person] |
| Version / last reviewed | [ ] |
| Collection steps last tested on | [build or image version, date] |

## Scope

- **Covers:** […] *Which devices or systems, and which suspected compromises.*
- **Does not cover:** […] *Anything where isolation, reboot or live response is unsafe, such as OT assets.*
- **Legal note:** […] *Personal data on the device, monitoring legal basis, when to involve the DPO or HR.*

## 0. Prerequisites — build these before the incident

- [ ] Remote isolation and live-response capability: [tool, and who holds access]
- [ ] Disk encryption recovery keys retrievable: [where they are escrowed]
- [ ] Local administrator credentials retrievable per device: [method]
- [ ] Collection kit: [write blocker, sanitised storage, memory-capture tool tested on this build]
- [ ] Chain-of-custody form and evidence labels: [location]
- [ ] […]

## 1. Triage — before touching the device

1. […] *What you can pull remotely first: endpoint telemetry, identity logs, network logs.*
2. […]
3. **Decision point:** evidence-priority or containment-priority, decided by [role]. *Evidence-priority for insider, legal or major-breach cases; containment-priority when harm is spreading.*

## 2. Containment

| Option | How on this platform | Preserves memory? | Notes |
|--------|----------------------|-------------------|-------|
| Network isolation | […] | [yes / no] | […] |
| Account and session revocation | […] | — | […] |
| Power-off | *Normally avoid: state is lost.* | no | […] |
| […] | […] | […] | […] |

## 3. Evidence acquisition — order of volatility per RFC 3227

*Hash everything with SHA-256, record time and operator for every action.*

| # | Evidence | How to collect on this platform | Platform notes |
|---|----------|---------------------------------|----------------|
| 1 | Memory | […] | […] *Capture before any shutdown.* |
| 2 | Volatile system state | […] | […] |
| 3 | Disk image or targeted triage collection | […] | […] *Encryption: image while unlocked, or have the key in hand.* |
| 4 | Local logs | […] | […] *Which logs, and where they roll over.* |
| 5 | Central logs for this host | […] | […] |
| 6 | […] | […] | […] |

## 4. Analysis pointers

- **Key artefacts on this platform:** […] *Execution, persistence, logons, file access, network activity.*
- **Known pitfalls:** […] *Features of this build that hide or destroy evidence.*
- **Tools your team uses:** […] *Non-normative; list what you have tested.*

## 5. Eradication & recovery

- **Default for confirmed compromise:** [reimage from known-good / rebuild] *Do not "clean" unless you can justify it.*
- **Credentials to rotate:** […] *Everything the user or device held, including tokens and certificates.*
- **Re-enrolment:** […]
- **Closure criteria:** no residual indicators for [ ] days; lessons-learned filed.

## 6. Reporting hooks

*Link to the scenario playbook's reporting table rather than repeating it. Add only what is specific to this platform.*

- […]

*Open CDC Framework, licensed CC BY 4.0.*
