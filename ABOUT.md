# About this project

## Why this framework exists

I have worked numerous years with critical infrastructure in cyber security. I started where many readers of this framework are now: as one of a few analysts in a large organisation, spending most of the time on reactive firefighting with little room to address root causes. After spending two years as the lead for DFIR I took over as manager, and over the following eighteen months the team developed from that starting point into a process-driven Cyber Defence Center with 24/7/365 in-house monitoring, organised as a capability-based, tierless SOC rather than a tiered one. Analysts own their cases end-to-end. The trade-offs behind that choice are the ones described in [Choosing your operating model](docs/operating-models.md), Model C.

I have also served as both main and secondary sponsor in SIM3 assessments for national and international CSIRT teams pursuing TF-CSIRT certifications. Working on the sponsor side of maturity assessments across different teams shaped this framework's emphasis on living documentation, independent verification, and evidence over assertion; see [the CSIRT community layer](docs/csirt-community.md).

Along the way I encountered most of the problems this framework now addresses. Among them:

- as three analysts we treated firefighting as the normal state; the underlying problem was not workload but that no one had the mandate to pause triage long enough to fix root causes
- we acquired technology before we had the mandate, and spent a year establishing authority we should have had in writing from the start
- we onboarded log sources by what was easy rather than by detection value, and paid for volume that taught us very little
- and many others.

Each of these was avoidable with the kind of structured, practitioner-written guide I was looking for at the time and could not find. This project is an attempt to write it, and to make it freely available so other teams, mainly in Europe, do not have to learn the same lessons the painful way.

## Who I am

- Frederik B. Krogsgaard, formerly Senior Manager at the Norlys Cyber Defence Center, where I spent six years building and running monitoring for critical infrastructure
- Certifications: SANS LDR553 Cyber Incident Management, LDR551 GSOM Building and Leading Security Operations Centers, FOR500 Windows Forensics, Application of the MITRE ATT&CK Framework, Investigation Theory, Effective Information Security Writing, Kusto Query Language for Security Analysts, and others.
- Feel free to reach out at https://www.linkedin.com/in/frederikbogeskov/

This is a personal, community-driven project. It is not affiliated with, endorsed by, or the position of any current or former employer, nor of NIST, ENISA, MITRE, or any authority referenced in it.

## What this project is — and is not

In scope: building and maturing a CDC/SOC for organisations mainly across the EU, in enterprise IT environments: endpoints, servers, identity, cloud/SaaS and enterprise networks. This is not limited to the EU, but my experience and knowledge of building SOC/CDC outside of the EU is limited.

Explicitly out of scope for now:

- OT/ICS environments: industrial control systems, SCADA, building automation. OT monitoring, safety-first response and the Purdue-model realities differ fundamentally from IT, and applying IT playbooks to OT can be dangerous. An OT extension profile is on the [roadmap](ROADMAP.md).
- Telco core networks, covering signalling, RAN and lawful intercept environments. These are regulated separately in most member states and operationally distinct.
- Defence/classified environments and other regimes with their own mandatory frameworks.

If you work in those domains, the GOVERN and maturity-model thinking still transfers. The technical content, meaning the PROTECT, DETECT and RESPOND playbooks, stays IT-specific.

## If you run critical infrastructure

Most of my career was spent in critical infrastructure, so I know the uncomfortable part of the scope line above: for a utility, the crown jewels are usually OT, and a framework that stops at the IT boundary covers less of what keeps you awake. Until the OT profile ships, this is how I would use OCDF in a CI setting.

What applies as written:

- **GOVERN, in full.** Mandate, charter, containment authority and reporting lines are no different for OT; if anything the authority question is sharper, because the CDC must know which actions it may *never* take on its own in an operational environment.
- **The IT side of the IT/OT boundary.** Most OT incidents still arrive through IT: identity, remote access, supplier connections, engineering workstations and the historian or DMZ layer. Identity-first log onboarding, remote-access containment (CON-12) and backup isolation (CON-13) protect OT by protecting the paths into it.
- **The maturity model, operating models, roles and the regulatory layer.** NIS2, CER and the national annexes apply to the organisation, not to one network.

What the CDC should own at the boundary, even without an OT profile:

- a current map of every IT/OT conduit, including supplier and vendor remote-access paths, with a named owner for each
- monitoring of the conduits themselves: the IT/OT DMZ, jump hosts, engineering workstations and remote-access gateways
- a written agreement with operations on who decides OT containment. The CDC advises; the plant or grid operator decides, because safety and availability outrank evidence in OT
- a joint exercise at least once a year where an IT incident threatens to cross into OT

What does **not** transfer: the platform playbooks. Isolating, rebooting or live-imaging an OT asset can have physical consequences. Use sector guidance (for example IEC 62443 and the ISA/IEC and ENISA OT material) and your vendors' procedures for anything below the DMZ.

In Denmark, energy-sector entities also fall under *Lov om styrket beredskab i energisektoren*, which scales its requirements over five preparedness levels and at the top levels goes beyond the EU baseline, with real-time monitoring, IT/OT segmentation and security clearance for key personnel; see the [Danish annex](docs/annexes/annex-dk.md). The OT/ICS extension profile is on the [roadmap](ROADMAP.md).

## Maintainers and adoption

The GitHub account [p0jst](https://github.com/p0jst) is mine. Today the framework has one maintainer, and I would rather say that plainly than let it be discovered. What that means in practice:

- **Every page is dated.** The national annexes carry a status block with the date they were last verified, who verified them and when the next review is due. An annex without a second reviewer says so.
- **Releases are versioned.** The current version is on the front page and in the [changelog](CHANGELOG.md); cite the version when you cite the framework.
- **Reviewers wanted.** A second reviewer per national annex, and practitioners willing to check the maturity criteria against their own CDC, would do more for the framework's credibility than anything I can write. See [Contributing](CONTRIBUTING.md).

**Using OCDF?** If your team uses the framework and is willing to be listed, open an issue or a discussion. No organisation is listed here until it has asked to be.

## How you can help

Corrections, national annex updates, translations, and above all your own pitfalls; see [Contributing](CONTRIBUTING.md). If this framework spares your team one of the mistakes above, it has done its job.

Frederik B. Krogsgaard, 2026
