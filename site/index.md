---
title: Home
hide:
  - navigation
  - toc
---

<div class="ocdf-hero" markdown>

<p class="ocdf-eyebrow"><span>v1.0.0</span> · <span>Open source</span> · <span>CC BY 4.0</span> · <span>Vendor-neutral</span> · <span>Built for the EU</span></p>

# Build and mature your Cyber Defence Center

<p class="ocdf-lead" markdown>
**A free, practitioner-written framework for Security Operations Centers and
Cyber Defence Centers in the European Union.** It sits between the standards and
your organisation: NIST CSF 2.0 says what the security areas are, NIS2 says what
you are obliged to do, and this framework says how to build and run the CDC that
gets it done.
</p>

<div class="ocdf-cta" markdown>
[Start building](#start-building){ .md-button .md-button--primary }
[OCDF on one page](docs/one-page.md){ .md-button }
[Assess your maturity](tools/maturity-assessment.html){ .md-button }
</div>

<div class="ocdf-stats" markdown>
<div markdown><b>6</b><span>CSF functions</span></div>
<div markdown><b>4</b><span>Maturity levels</span></div>
<div markdown><b>27</b><span>National annexes</span></div>
<div markdown><b>3</b><span>Browser tools</span></div>
</div>

</div>

## Where are you coming from?

<div class="grid cards ocdf-roles" markdown>

-   :material-briefcase-outline:{ .lg .middle } **CISO or executive**

    ---

    The 30-minute version: why a CDC, what NIS2 asks of management, staffing
    and cost drivers, what you can and cannot outsource, and the questions to
    ask your SOC.

    [Executive guide →](docs/executive-guide.md)

-   :material-shield-account-outline:{ .lg .middle } **SOC or CDC manager**

    ---

    Build and mature the function: the first 90 days in order, the operating
    model decision, the templates, and a maturity assessment that turns into an
    action plan.

    [Start building →](#start-building)

-   :material-console:{ .lg .middle } **Analyst or engineer**

    ---

    The operational detail: [running the CDC](docs/13-cdc-operations.md),
    [detection-as-code](docs/14-detection-as-code-deep-dive.md), the
    [CTI capability](docs/15-cti-deep-dive.md) and the
    [IR playbooks](playbooks/README.md).

    [Detect →](docs/04-detect.md)

-   :material-scale-balance:{ .lg .middle } **Compliance or legal**

    ---

    NIS2, GDPR, DORA, CRA and CER mapped to CDC capabilities, national annexes
    for all 27 member states, and a selector that shows only the laws that
    apply to you.

    [EU regulatory landscape →](docs/17-eu-regulatory-landscape.md)

</div>

## The framework in one picture

<div class="ocdf-map" markdown>

<div class="m-govern" markdown>
[**GOVERN** · mandate, risk, roles, budget, oversight](docs/01-govern.md)
</div>

<div class="m-flow" markdown>
<div markdown>[**IDENTIFY**<br><span>what we defend and what threatens it</span>](docs/02-identify.md)</div>
<div markdown>[**PROTECT**<br><span>reduce likelihood and blast radius</span>](docs/03-protect.md)</div>
<div markdown>[**DETECT**<br><span>find adversary activity fast</span>](docs/04-detect.md)</div>
<div markdown>[**RESPOND**<br><span>contain, eradicate, report</span>](docs/05-respond.md)</div>
<div markdown>[**RECOVER**<br><span>restore trusted service, learn</span>](docs/06-recover.md)</div>
</div>

<p class="m-loop">↺ Lessons learned in RECOVER feed the next round of IDENTIFY</p>

<div class="m-lenses" markdown>
<div markdown>[**CIA triad** · every capability states whether it protects confidentiality, integrity or availability](docs/07-cia-triad.md)</div>
<div markdown>[**Regulatory layer** · NIS2, GDPR, DORA, CRA, CER and 27 national annexes](docs/17-eu-regulatory-landscape.md)</div>
</div>

<div class="m-measure" markdown>
<div markdown>[**Tier E · S · A**<br><span>which capabilities apply at your size</span>](docs/10-tiers.md)</div>
<div markdown>[**Level 1–4**<br><span>how well you run them</span>](docs/08-maturity-model.md)</div>
<div markdown>[**Evidence**<br><span>what proves it to an auditor</span>](tools/maturity-assessment.html)</div>
</div>

<p class="m-base">Built in the order People › Process › Technology</p>

</div>

Every function has the same parts: capabilities with IDs such as `DE-2`,
maturity criteria per level, EU regulatory hooks, and a table of the other
departments it depends on. [OCDF on one page](docs/one-page.md) explains all
the terms in five minutes.

## Start building

Seven steps, each with the page or tool that does it. See them carried out for a
fictional 2,500-person organisation in the [worked example](docs/worked-example.md).

<div class="ocdf-path" markdown>

1.  **Choose your tier.** Essential, Standard or Advanced decides how much of the
    framework applies to you. [Implementation tiers](docs/10-tiers.md)
2.  **Run the design workshops.** Six workshops, one per function, surface your
    gaps and the decisions nobody has taken yet. [Design navigator](assessments/cdc-design-navigator.md)
3.  **Adopt the charter.** Mandate, scope and containment authority, signed
    before anything is bought. [CDC charter](templates/cdc-charter-template.md)
4.  **Decide the operating model.** In-house, provider or hybrid, with the
    staffing arithmetic and a cost template. [Operating models](docs/11-operating-models.md)
5.  **Assess where you are.** Score the maturity criteria and give every gap an
    owner and a due date. [Maturity self-assessment](tools/maturity-assessment.html)
6.  **Work the first 90 days.** The order of work, week by week, with exit
    criteria. [Start here](docs/09-start-here.md)
7.  **Set the operating rhythm.** The recurring work that keeps a CDC from
    decaying, and a detection portfolio that grows from your threat profile.
    [Annual calendar](templates/annual-calendar-template.md) ·
    [Detection use case](templates/detection-use-case-template.md)

</div>

All [templates](templates/index.md) and the three
[browser tools](tools/README.md) work offline, and nothing you enter leaves your
browser. The whole framework is on [GitHub](https://github.com/p0jst/OpenCDC)
under CC BY 4.0, also as a
[zip download](https://github.com/p0jst/OpenCDC/archive/refs/heads/main.zip).

!!! info "How current is this, and who wrote it?"
    **Version 1.0.0**, released 2 September 2026; see the [changelog](CHANGELOG.md).
    Written and maintained by one practitioner, Frederik B. Krogsgaard, formerly
    Senior Manager at the Norlys Cyber Defence Center. Each national annex shows
    when it was last verified and how confident that verification is.
    [Why you can, and cannot, rely on this framework](docs/trust.md) sets out
    which statements are law, which are standards and which are the author's own
    judgement.

!!! note "Scope"
    The framework targets **enterprise IT environments**: endpoints, servers,
    identity, cloud and SaaS. It is not designed for OT/ICS, telco core networks or
    classified environments; see [About](ABOUT.md) for the reasoning. Running
    critical infrastructure? Read
    [what still applies at the IT/OT boundary](ABOUT.md#if-you-run-critical-infrastructure);
    an OT profile is planned for v1.2. Orientation only, not legal advice.
