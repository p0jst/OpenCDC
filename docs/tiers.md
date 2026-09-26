# Implementation Tiers: Essential, Standard, Advanced

<p class="src" markdown><span class="src-tag ocdf">OCDF</span>This framework's tiers, a pattern borrowed from the CIS Controls implementation groups.</p>

## One framework, three ambition levels

Not every organisation needs every capability. Instead of maintaining three editions, OCDF uses a **tier overlay**, a pattern borrowed from the CIS Controls' Implementation Groups: every capability is tagged with the lowest tier that should implement it. Higher tiers include everything below them.

| Tier | Who | Rough profile |
|------|-----|---------------|
| **E, Essential** | SMEs and low-complexity IT, up to about five security FTE | The defensible minimum, and the NIS2 floor; mostly Model A or hybrid operating models |
| **S, Standard** | A dedicated CDC in a mid-sized or large, regulated organisation | Full six-function coverage with measurement |
| **A, Advanced** | Critical infrastructure, high-threat sectors, DORA TLPT-scope entities | Validation, automation and self-improvement |

Pick the tier on size, complexity and threat exposure, not on NIS2 category. NIS2 Art. 21 requires the same ten measures of *essential* and *important* entities; the categories differ in how they are supervised and fined, not in what they must do.

**Tier ≠ maturity.** Tier answers *which capabilities*; the [maturity model](maturity-model.md) answers *how well you run them*. A sensible target pairing: E-tier at Level 2, S-tier at Level 3, A-tier at Level 3–4.

## The legal floor

**Neither your tier nor your maturity target relieves you of a legal requirement.** Each measure NIS2 Art. 20 and 21 require has its minimum form in the Essential tier and in the Level 2 criteria, so an organisation in NIS2 scope that reaches Level 2 in every function has, in this framework's reading, covered the measures at least in basic form. Two parts that sit mostly outside a CDC, human-resources security and vulnerability disclosure, are covered only thinly; the crosswalk names them so you can give them an owner. The mapping is in the [NIS2 Article 21 crosswalk](nis2-article-21-crosswalk.md). A capability marked in the NIS2 column of the [capability index](capability-index.md) is never "above tier" for an entity in scope, whatever its tier; score it and do at least its Level 2 form.

## If you are the whole security function

Plenty of readers arrive here as the only person with security in their job
title. The framework still applies, but the sequencing changes, because
Essential tier assumes roughly 3 to 4 people and the staffing notes in
[DETECT](detect.md) and [Roles & competences](roles-and-competences.md)
assume more.

Three moves make a one-person function viable:

1. **Buy the clock, build the context.** Round-the-clock monitoring is the one
   thing a single person cannot provide. Take
   [Model A](operating-models.md) and let a provider hold the watch, then
   spend your own hours on the work no provider can do for you: crown jewels,
   business context, containment authority and the statutory reporting path.
2. **Own the four things that never outsource.** Risk acceptance, containment
   authority over crown jewels, statutory reporting and the regulatory
   applicability register stay with you whatever the contract says. They are
   also the highest-value use of a single person's time.
3. **Take the blast-radius rows of Essential first.** GV-1, ID-3, PR-1, PR-7
   and RS-1 in the [capability index](capability-index.md) buy more risk
   reduction per hour than anything else on the list. The rest of Essential
   follows once those are real.

Staff the gap deliberately rather than pretending it is not there. Name the
DFIR retainer before you need it, and record in the charter which decisions
have no deputy while you are away. A one-person function with an honest
dependency list is defensible to a board and to a regulator. One that claims
full coverage is neither.

## Capability tier map

| Function | Essential, E | plus Standard, S | plus Advanced, A |
|----------|---------------|----------------|----------------|
| GOVERN | GV-1 charter · GV-3 policies · GV-4 RACI · GV-6 security clauses with critical suppliers · GV-7 basic reporting, including management approval and training | GV-2 risk integration · GV-5 resourcing governance · supplier risk reviewed annually | Quantified risk; board exercises per the L4 criteria |
| IDENTIFY | ID-1 inventory · ID-3 crown jewels · ID-4 basic vuln mgmt · ID-5 short threat profile · ID-6 annual risk analysis | ID-2 data classification · ID-7 improvement loop · threat profile mapped to ATT&CK | Continuous attack-surface mgmt; intel-driven engineering |
| PROTECT | PR-1 MFA/least-priv · PR-2 awareness · PR-3 cryptography policy · PR-5 patching · PR-7 tested offline backups · PR-4 hardening baselines, script control & blocking execution from user-writable paths · PR-9 email and web basics such as DMARC and DNS filtering · security requirements when buying or changing critical systems | server allowlisting under PR-4 · PR-6 segmentation · PR-8 secure development & change | Continuous control validation · workstation allowlisting |
| DETECT | DE-1 sources 1–3 · DE-2 in basic form: use cases for the top techniques in the threat profile, your own or the provider's, documented · DE-3 triage runbook, or a provider equivalent with transparency | DE-2 full use-case lifecycle · DE-4 coverage measurement · DE-5 scheduled hunting · DE-7 integrity monitoring · network/NDR telemetry where unmanaged devices or flat segments exist | DE-6 systematic validation · detection-as-code per [Detection-as-code deep dive](detection-as-code-deep-dive.md) · CTI programme per [CTI deep dive](cti-deep-dive.md) |
| RESPOND | RS-1 IR plan · RS-2 top-3 playbooks · RS-4 containment with pre-agreed authority · RS-5 reporting machinery · RS-6 escalation into crisis management · RS-7 annual tabletop and reporting drill | RS-3 forensics, where a retainer is fine · exercises that include management and communications | Automated containment with gates · crisis exercises with suppliers |
| RECOVER | RC-1 recovery plans+RTO/RPO · RC-4 recovery communication · RC-5 post-incident reviews | RC-2 trusted restoration · RC-3 verified execution · RC-6 BCM integration | Ransomware-scale recovery exercises; measured RTO attainment |

## How to use tiers

1. **Pick your tier** honestly, on size, complexity and threat exposure. Your regulatory category sets the floor, not the tier. When in doubt between two, take the lower and reach maturity Level 2–3 there first. A solid E beats a hollow S.
2. **Filter the framework:** in the self-assessment and navigator, skip capabilities above your tier and mark them "above tier" rather than "missing", so the score reflects your ambition, not an enterprise ideal. Capabilities marked in the NIS2 column of the capability index are the exception for entities in NIS2 scope; see [the legal floor](#the-legal-floor).
3. **National and sector law on top:** your national law may mandate S- or A-tier items regardless of size. Denmark's energy-sector act, for instance, requires real-time monitoring and response at its preparedness levels 4 and 5. The annex and selector tool trump the tier map.
4. **Review the tier choice** at every annual reassessment; tiers are meant to be outgrown.

*Open CDC Framework, licensed CC BY 4.0. Tier-overlay pattern inspired by CIS Critical Security Controls Implementation Groups, © Center for Internet Security, credited in [references](references.md).*
