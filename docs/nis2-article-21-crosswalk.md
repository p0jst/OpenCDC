# NIS2 Article 21 Crosswalk

<p class="src" markdown><span class="src-tag law">Law</span><span class="src-tag ocdf">OCDF</span>Obligations paraphrased from Directive (EU) 2022/2555; the mapping to capabilities and criteria is this framework's. Not legal advice.</p>

This page answers the question an auditor or a supervisory authority asks first:
*where in your CDC is each NIS2 measure?* It maps Articles 20, 21 and 23 to the
OCDF capabilities that deliver them and to the Level 2 criteria that make up the
minimum.

## The rule behind the mapping

NIS2 requires the same measures of *essential* and *important* entities. The
categories differ in supervision, ex ante or ex post, and in the maximum fines,
not in what an entity must do. OCDF therefore puts the minimum form of every
measure into the **Essential tier** and the **Level 2 criteria**:

- Reaching **Level 2 in every function** covers each measure below at least in
  basic form, in this framework's reading, apart from the two gaps named under
  the table.
- A capability that carries the legal floor is never "above tier" for an entity
  in NIS2 scope, whatever tier it picked. See [the legal floor](tiers.md#the-legal-floor).
- Level 3 and 4 criteria go further than the law asks. They are risk decisions,
  not obligations.

Two cautions. Art. 21(1) asks for measures that are *appropriate and
proportionate* to the entity's risk, so "basic form" is the least a supervisor
will accept, not a safe harbour. And national transpositions can add to the
list; check your [national annex](annexes/README.md).

## Articles 20 and 21

| Obligation | What it asks, paraphrased | OCDF capabilities | Level 2 criteria that meet the minimum |
|------------|---------------------------|-------------------|----------------------------------------|
| **Art. 20(1)** Governance | The management body approves the cybersecurity risk-management measures, oversees their implementation and can be held liable | GV-1, GV-7 | GOVERN: management body has approved the measures and completed training |
| **Art. 20(2)** Training | Members of the management body follow training; employees are encouraged to receive similar training regularly | GV-7, PR-2 | GOVERN: management training within 12 months · PROTECT: awareness training for all staff |
| **Art. 21(1)** Approach | Appropriate and proportionate technical, operational and organisational measures, based on an all-hazards approach | GV-2, ID-6 | IDENTIFY: risk analysis performed and approved within 12 months |
| **21(2)(a)** | Policies on risk analysis and information system security | GV-3, ID-6 | GOVERN: security policies approved and reviewed · IDENTIFY: risk analysis |
| **21(2)(b)** | Incident handling | DE-1, DE-3, RS-1, RS-2, RS-4, RS-7 | DETECT: central log platform, triage runbook · RESPOND: approved IR plan, playbooks, tabletop exercise |
| **21(2)(c)** | Business continuity, such as backup management and disaster recovery, and crisis management | PR-7, RC-1, RS-6 | PROTECT: restore tested, offline or immutable copy · RECOVER: recovery plans with RTO/RPO, one crown-jewel service restored against its RTO · RESPOND: escalation into crisis management |
| **21(2)(d)** | Supply chain security, including the security of relationships with direct suppliers and service providers | GV-6 | GOVERN: security requirements in contracts with critical suppliers; list of critical suppliers |
| **21(2)(e)** | Security in acquiring, developing and maintaining systems, including vulnerability handling and disclosure | ID-4, PR-5, PR-8 in basic form | IDENTIFY: quarterly vulnerability scanning · PROTECT: patching SLA; security requirements when buying or changing critical systems |
| **21(2)(f)** | Policies and procedures to assess the effectiveness of the measures | GV-7, RS-7 | GOVERN: effectiveness assessed annually and reported to management |
| **21(2)(g)** | Basic cyber hygiene practices and cybersecurity training | PR-2, PR-4, PR-9 | PROTECT: hardening baselines; awareness training for all staff |
| **21(2)(h)** | Policies and procedures on cryptography and, where appropriate, encryption | PR-3 | PROTECT: cryptography policy covering data in transit and at rest |
| **21(2)(i)** | Human resources security, access control policies and asset management | ID-1, PR-1 | IDENTIFY: automated asset discovery · PROTECT: MFA for remote and administrative access |
| **21(2)(j)** | Multi-factor or continuous authentication, secured voice, video and text communications, and secured emergency communications where appropriate | PR-1, RS-1 | PROTECT: MFA for remote and administrative access · RESPOND: the IR plan's out-of-band communications |

**Gaps to close yourself.** Two parts of the list are only partly inside a CDC's
remit and OCDF covers them thinly: *human resources security* in (i), such as
joiner, mover and leaver processes and screening, and *vulnerability disclosure*
in (e), meaning a way for outsiders to report a vulnerability to you. Assign both
an owner in GV-4.

## Article 23: reporting

| Obligation | Deadline | OCDF | Level 2 criteria |
|------------|----------|------|------------------|
| Early warning of a significant incident | ≤ 24 h from becoming aware | RS-5 | RESPOND: statutory contacts and templates prepared; reporting drill within 12 months |
| Incident notification | ≤ 72 h from becoming aware | RS-5 | as above |
| Final report | ≤ 1 month after the notification | RS-5, RC-5 | RECOVER: post-incident review process defined |
| Informing recipients of your services of significant incidents likely to affect them, and of measures they can take against a significant threat | Without undue delay | RS-5, RC-4 | RESPOND: statutory contacts and templates, which should include customer templates |

What makes an incident *significant*: it has caused or can cause severe
operational disruption or financial loss to the entity, or considerable material
or non-material damage to others, per Art. 23(3). For digital infrastructure and
digital service providers, Commission Implementing Regulation (EU) 2024/2690 sets
concrete thresholds; many member states publish their own guidance for the rest.
Record in the IR plan which definition applies to you.

## Using it

- Keep this page open while you score the [maturity self-assessment](../assessments/maturity-self-assessment.md):
  every Level 2 criterion that serves a NIS2 measure is marked there with its reference.
- For the evidence, use the same record the self-assessment asks for. Art. 21(2)(f)
  is itself met by assessing effectiveness and reporting it; the self-assessment
  is that assessment.
- Commission Implementing Regulation (EU) 2024/2690 details the Art. 21 measures
  for digital infrastructure and digital service providers. Even outside its scope,
  it is the most concrete published checklist of what the measures mean.

## Sources

- NIS2: Directive (EU) 2022/2555, Art. 20, 21, 23 and 34. https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- Commission Implementing Regulation (EU) 2024/2690. https://eur-lex.europa.eu/eli/reg_impl/2024/2690/oj

*Open CDC Framework, licensed CC BY 4.0. Credits: [References & credits](references.md).*
