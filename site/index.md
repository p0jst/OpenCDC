---
title: Home
hide:
  - navigation
  - toc
---

<div class="ocdf-hero" markdown>

<p class="ocdf-eyebrow"><span>v1.1.0</span> · <span>Open source, CC BY 4.0</span> · <span>Built for the EU</span></p>

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

    The operational detail: [detection](docs/detect.md),
    [detection-as-code](docs/detection-as-code-deep-dive.md), the
    [CTI capability](docs/cti-deep-dive.md) and the
    [IR playbooks](playbooks/README.md).

    [Running the CDC →](docs/cdc-operations.md)

-   :material-scale-balance:{ .lg .middle } **Compliance or legal**

    ---

    NIS2, GDPR, DORA, CRA and CER mapped to CDC capabilities, national annexes
    for all 27 member states, and a selector that shows only the laws that
    apply to you.

    [EU regulatory landscape →](docs/eu-regulatory-landscape.md)

</div>

## What you get

Not just pages read once — working through OCDF produces a stack of concrete
artefacts you take into your own documentation system and governance process:

<div class="ocdf-outputs" markdown>

- **CDC charter** — mandate, scope and containment authority, signed before anything is bought. [Template](templates/cdc-charter-template.md)
- **Target operating model** — in-house, MSSP, hybrid or shared, with the staffing arithmetic behind it. [Operating models](docs/operating-models.md)
- **Capability baseline** — where you stand today, function by function, with evidence behind every score. [Maturity self-assessment](tools/maturity-assessment.html)
- **90-day action plan** — every gap with an owner and a due date. [Start here](docs/start-here.md)
- **Regulatory applicability profile** — which of NIS2, GDPR, DORA, CRA and CER actually apply to you, and your national annex. [Regulatory profile selector](tools/regulatory-profile.html)
- **Detection portfolio** — use cases prioritised by your own threat profile, not a generic checklist. [Detection-as-code](docs/detection-as-code-deep-dive.md)
- **Annual operating calendar** — the recurring work that keeps a CDC from decaying after go-live. [Template](templates/annual-calendar-template.md)
- **Evidence register** — what backs every maturity score, exportable as a spreadsheet for board reporting. [Maturity self-assessment](tools/maturity-assessment.html)

</div>

## The framework in one picture

<p class="ocdf-dimensions-intro">OCDF has four independent dimensions — mix and match them for your organisation:</p>

<div class="ocdf-dimensions" markdown>
<div markdown><b>What</b><span>6 functions</span></div>
<div markdown><b>How much</b><span>E · S · A tier</span></div>
<div markdown><b>How well</b><span>L1–L4 maturity</span></div>
<div markdown><b>Proof</b><span>Evidence</span></div>
</div>

<div class="ocdf-map" markdown>

<div class="m-govern" markdown>
[**GOVERN** · mandate, risk, roles, budget, oversight](docs/govern.md)
</div>

<div class="m-flow" markdown>
<div markdown>[**IDENTIFY**<br><span>what we defend and what threatens it</span>](docs/identify.md)</div>
<div markdown>[**PROTECT**<br><span>reduce likelihood and blast radius</span>](docs/protect.md)</div>
<div markdown>[**DETECT**<br><span>find adversary activity fast</span>](docs/detect.md)</div>
<div markdown>[**RESPOND**<br><span>contain, eradicate, report</span>](docs/respond.md)</div>
<div markdown>[**RECOVER**<br><span>restore trusted service, learn</span>](docs/recover.md)</div>
</div>

<p class="m-loop">↺ Lessons learned in RECOVER feed the next round of IDENTIFY</p>

<p class="m-lenses" markdown>
Seen through the [**CIA triad**](docs/cia-triad.md) and the
[**regulatory layer**](docs/eu-regulatory-landscape.md) (NIS2, GDPR, DORA,
CRA, CER and 27 national annexes) · sized by [**tier**](docs/tiers.md)
(E · S · A) · scored by [**level**](docs/maturity-model.md) (1–4) · proven
with [**evidence**](tools/maturity-assessment.html) · built in the order
people › process › technology.
</p>

</div>

Every function has the same parts: capabilities with IDs such as `DE-2`,
maturity criteria per level, EU regulatory hooks, and a table of the other
departments it depends on. [OCDF on one page](docs/one-page.md) explains all
the terms in five minutes.

## See OCDF in action

A fictional 2,500-person parcel company goes from fragmented security work to
a structured, evidenced CDC: tier decision, operating model, signed charter,
first 90 days with owners, a ten-detection portfolio and the first board
report — see every step in the [worked example](docs/worked-example.md).

<div class="ocdf-example" markdown>

<div class="ocdf-example__before" markdown>
<p class="ocdf-example__label">Before</p>

- Fragmented responsibilities
- No clear containment authority
- Reactive detection
- Undefined regulatory ownership
</div>

<div class="ocdf-example__arrow" aria-hidden="true">→</div>

<div class="ocdf-example__after" markdown>
<p class="ocdf-example__label">After</p>

- Defined mandate and charter
- Chosen operating model
- Capability baseline and 90-day plan
- Maturity targets and evidence
</div>

</div>

[Explore the worked example →](docs/worked-example.md){ .md-button .md-button--primary }

## Start building

Seven steps, each with the page or tool that does it. See them carried out for a
fictional 2,500-person organisation in the [worked example](docs/worked-example.md).

<div class="ocdf-path" markdown>

1.  **Choose your tier.** Essential, Standard or Advanced decides how much of the
    framework applies to you. [Implementation tiers](docs/tiers.md)
2.  **Run the design workshops.** Six workshops, one per function, surface your
    gaps and the decisions nobody has taken yet. [Design navigator](assessments/cdc-design-navigator.md)
3.  **Adopt the charter.** Mandate, scope and containment authority, signed
    before anything is bought. [CDC charter](templates/cdc-charter-template.md)
4.  **Decide the operating model.** In-house, provider or hybrid, with the
    staffing arithmetic and a cost template. [Operating models](docs/operating-models.md)
5.  **Assess where you are.** Score the maturity criteria and give every gap an
    owner and a due date. [Maturity self-assessment](tools/maturity-assessment.html)
6.  **Work the first 90 days.** The order of work, week by week, with exit
    criteria. [Start here](docs/start-here.md)
7.  **Set the operating rhythm.** The recurring work that keeps a CDC from
    decaying, and a detection portfolio that grows from your threat profile.
    [Annual calendar](templates/annual-calendar-template.md) ·
    [Detection use case](templates/detection-use-case-template.md)

</div>

The [templates](templates/index.md) are plain documents to copy and adapt. The
three [browser tools](tools/README.md) run entirely in your browser: nothing you
enter is sent anywhere. The whole framework is on [GitHub](https://github.com/p0jst/OpenCDC)
under CC BY 4.0, also as a
[zip download](https://github.com/p0jst/OpenCDC/archive/refs/heads/main.zip).

<div class="ocdf-meta" markdown>

**Version 1.1.0**, released 23 September 2026 ([changelog](CHANGELOG.md)) ·
written and maintained by one practitioner, Frederik B. Krogsgaard, formerly
Senior Manager at the Norlys Cyber Defence Center. Each national annex states
when it was last reviewed and how confident that review is; see
[why you can, and cannot, rely on this framework](docs/trust.md).

**Scope: enterprise IT** — endpoints, servers, identity, cloud and SaaS. Not
designed for OT/ICS, telco core networks or classified environments ([why](ABOUT.md));
running critical infrastructure, see
[the IT/OT boundary](ABOUT.md#if-you-run-critical-infrastructure) (an OT
profile is on the [roadmap](ROADMAP.md)). Orientation only, not legal advice.

</div>
