# Implementation Tiers: Essential, Standard, Advanced

<p class="src" markdown><span class="src-tag ocdf">OCDF</span>This framework's tiers, a pattern borrowed from the CIS Controls implementation groups.</p>

## One framework, three ambition levels

Not every organisation needs every capability. Instead of maintaining three editions, OCDF uses a **tier overlay**, a pattern borrowed from the CIS Controls' Implementation Groups: every capability is tagged with the lowest tier that should implement it. Higher tiers include everything below them.

| Tier | Who | Rough profile |
|------|-----|---------------|
| **E, Essential** | SMEs, ≤5 security FTE, NIS2 *important* entities, low-complexity IT | The defensible minimum; mostly Model A/hybrid operating models |
| **S, Standard** | Dedicated CDC, NIS2 *essential* entities, regulated mid/large orgs | Full six-function coverage with measurement |
| **A, Advanced** | Critical infrastructure, high-threat sectors, DORA TLPT-scope entities | Validation, automation and self-improvement |

**Tier ≠ maturity.** Tier answers *which capabilities*; the [maturity model](maturity-model.md) answers *how well you run them*. A sensible target pairing: E-tier at Level 2, S-tier at Level 3, A-tier at Level 3–4.

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
| GOVERN | GV-1 charter · GV-3 policies · GV-4 RACI · GV-7 basic reporting | GV-2 risk integration · GV-5 resourcing governance · GV-6 supply chain | Quantified risk; board exercises per the L4 criteria |
| IDENTIFY | ID-1 inventory · ID-3 crown jewels · ID-4 basic vuln mgmt | ID-2 data classification · ID-5 threat profile · ID-6 risk assessment · ID-7 improvement loop | Continuous attack-surface mgmt; intel-driven engineering |
| PROTECT | PR-1 MFA/least-priv · PR-2 awareness · PR-5 patching · PR-7 tested offline backups · PR-9 email and web basics such as DMARC and DNS filtering · script control & blocking execution from user-writable paths | PR-3 data security · PR-4 hardening baselines incl. server allowlisting · PR-6 segmentation | PR-8 secure SDLC · continuous control validation · workstation allowlisting |
| DETECT | DE-1 sources 1–3 · DE-3 triage runbook, or an MSSP equivalent with transparency | DE-2 use-case lifecycle · DE-4 coverage measurement · DE-7 integrity monitoring · network/NDR telemetry where unmanaged devices or flat segments exist | DE-5 hunting · DE-6 systematic validation · detection-as-code per [Detection-as-code deep dive](detection-as-code-deep-dive.md) · CTI programme per [CTI deep dive](cti-deep-dive.md) |
| RESPOND | RS-1 IR plan · RS-2 top-3 playbooks · RS-5 reporting machinery | RS-3 forensics, where a retainer is fine · RS-4 pre-authorised containment · RS-7 annual exercises | RS-6 crisis integration · automated containment with gates |
| RECOVER | RC-1 recovery plans+RTO/RPO · RC-4 recovery communication · RC-5 post-incident reviews | RC-2 trusted restoration · RC-3 verified execution · RC-6 BCM integration | Ransomware-scale recovery exercises; measured RTO attainment |

## How to use tiers

1. **Pick your tier** honestly, on regulatory category, threat exposure and team size. When in doubt between two, take the lower and reach maturity Level 2–3 there first. A solid E beats a hollow S.
2. **Filter the framework:** in the self-assessment and navigator, skip capabilities above your tier and mark them "above tier" rather than "missing", so the score reflects your ambition, not an enterprise ideal.
3. **Regulatory floor:** your national law may mandate S-tier items regardless of size. Denmark's energy-sector act, for instance, pushes DETECT toward A. The annex and selector tool trump the tier map.
4. **Review the tier choice** at every annual reassessment; tiers are meant to be outgrown.

*Open CDC Framework, licensed CC BY 4.0. Tier-overlay pattern inspired by CIS Critical Security Controls Implementation Groups, © Center for Internet Security, credited in [references](references.md).*
