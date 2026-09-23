# Playbooks

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span><span class="src-tag standard">Standard</span>Response practice from experience; evidence handling follows RFC 3227.</p>

Two kinds of playbook: **by attack**, for what you reach for first when the call comes in, and **by platform**, for the forensics on a specific machine. Attack playbooks point to the platform ones where the work moves to a host.
All are vendor-neutral; open source tooling examples are non-normative.

## By attack

| ID | Scenario | Status | File |
|----|----------|--------|------|
| PB-IDC | Identity compromise: stolen passwords, tokens, MFA or app consent | Draft | [PB-IDC-identity-compromise.md](PB-IDC-identity-compromise.md) |
| PB-BEC | Business email compromise and payment fraud | Draft | [PB-BEC-business-email-compromise.md](PB-BEC-business-email-compromise.md) |
| PB-RAN | Ransomware | Draft | [PB-RAN-ransomware.md](PB-RAN-ransomware.md) |

Drafts are published for field review: usable, but not yet checked by anyone other than the maintainer. Corrections and your own lessons are welcome via CONTRIBUTING.md.

## By platform

| ID | Platform | File |
|----|----------|------|
| PB-W11 | Windows 11 laptop | PB-W11-windows11-laptop.md |
| PB-MAC | macOS laptop, Intel & Apple Silicon | PB-MAC-macos-laptop.md |
| PB-WSV | Windows Server, including domain controllers | PB-WSV-windows-server.md |
| PB-LNX | Linux enterprise server, RHEL-class | PB-LNX-rhel-server.md |

**Scope: enterprise IT only.** These playbooks must not be applied to OT/ICS or telco core systems unadapted, because isolation and live-response actions can be unsafe there.

## External baseline playbooks

Two public playbook collections are recommended as starting points alongside the platform playbooks here, with the important caveat that they are baselines: the reader must adjust and tailor them to their own environment, tooling, authority matrix and reporting obligations before relying on them.

- Microsoft incident response playbooks: practical, scenario-based runbooks for phishing, password spray, app consent grant, token theft and compromised applications, strongest for Microsoft-centric estates. https://learn.microsoft.com/security/operations/incident-response-playbooks
- CISA, Federal Government Cybersecurity Incident and Vulnerability Response Playbooks: clear, tool-neutral incident and vulnerability response workflows that adapt well outside the US federal context. https://www.cisa.gov/resources-tools/resources/federal-government-cybersecurity-incident-and-vulnerability-response-playbooks

Adaptation checklist when importing any external playbook: replace product assumptions with your stack; align severities with your IR plan §1; insert your containment mandates from the containment action catalogue; add your statutory reporting hooks for NIS2, GDPR, DORA and your national annex; and exercise it once before you need it.

Shared principles: order of volatility per RFC 3227, chain of custody, hash
everything, "Integrity before Availability" on recovery, and GDPR-aware
handling of employee/personal data. See docs/05-respond.md and 06-recover.md.
