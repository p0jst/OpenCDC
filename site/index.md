---
title: Home
hide:
  - navigation
  - toc
---

<div class="ocdf-hero" markdown>

<p class="ocdf-eyebrow"><span>v1.2.0</span> · <span>Open source, CC BY 4.0</span> · <span>Built for the EU</span></p>

# Build and mature your cyber defence

<p class="ocdf-lead" markdown>
**A free framework for the people who detect and respond to cyber attacks in
European organisations.** That might be a 24/7 Cyber Defence Center, or two
people in IT who also look after security. The standards describe what good
security covers, and NIS2 says what you are obliged to do. Neither tells you
how to set up and run the team that does the work. That is what this framework
is for. [Is this for me?](#is-this-for-me)
</p>

<div class="ocdf-cta" markdown>
[Start building](#start-building){ .md-button .md-button--primary }
[Understand OCDF in 5 minutes](docs/one-page.md){ .md-button }
</div>

<ul class="ocdf-assure">
<li>No account</li>
<li>Tools run in your browser</li>
<li>Plain documents you own</li>
</ul>

<div class="ocdf-stats" markdown>
<div markdown><b>6</b><span>CSF functions</span></div>
<div markdown><b>4</b><span>Maturity levels</span></div>
<div markdown><b>27</b><span>National annexes</span></div>
<div markdown><b>3</b><span>Browser tools</span></div>
</div>

</div>

## Is this for me?

Probably, if part of your job is noticing attacks and dealing with them. The
framework calls that work a *CDC*, whatever your team is called and however
small it is. Every capability is marked with the smallest
[tier](docs/tiers.md) it belongs to, so a team of two can see what matters now
and what can wait.

<div class="grid cards ocdf-roles" markdown>

-   :material-account-wrench-outline:{ .lg .middle } **A small IT-security team**

    ---

    One to three people, and security is only part of the job. Start with what
    to buy rather than build, and the four things nobody can do for you.

    [Start small →](docs/tiers.md#if-you-are-the-whole-security-function)

-   :material-briefcase-outline:{ .lg .middle } **CISO or executive**

    ---

    Thirty minutes on what a CDC is for, what NIS2 expects of management, what
    it costs, and what to ask the people running it.

    [Executive guide →](docs/executive-guide.md)

-   :material-hammer-wrench:{ .lg .middle } **Building a SOC or CDC**

    ---

    You have a mandate and a budget, or soon will. Seven steps take you from a
    signed charter to a team with a working routine.

    [Start building →](#start-building)

-   :material-chart-timeline-variant:{ .lg .middle } **Running one already**

    ---

    Score what you have against the maturity criteria, reusing any SOC-CMM,
    SIM3 or CIS assessment, and turn the gaps into a plan.

    [Maturity self-assessment →](tools/maturity-assessment.html)

-   :material-console:{ .lg .middle } **Analyst or engineer**

    ---

    The daily work: [triage](docs/alert-triage.md),
    [detection-as-code](docs/detection-as-code-deep-dive.md),
    [threat intelligence](docs/cti-deep-dive.md) and the
    [playbook templates](templates/scenario-playbook-template.md).

    [Running the CDC →](docs/cdc-operations.md)

-   :material-scale-balance:{ .lg .middle } **Compliance or legal**

    ---

    Which of NIS2, GDPR, DORA, CRA and CER apply to you, what they ask of a
    CDC, and the national rules in all 27 member states.

    [EU regulatory landscape →](docs/eu-regulatory-landscape.md)

</div>

## The framework in one picture

<p class="ocdf-dimensions-intro">Every capability in OCDF is described in three ways:</p>

<div class="ocdf-dimensions" markdown>
<div markdown><b>What</b><span>6 functions</span><i>Cover all six</i></div>
<div markdown><b>How much</b><span>E · S · A tier</span><i>You choose</i></div>
<div markdown><b>How well</b><span>L1–L4 maturity</span><i>Scored against set criteria</i></div>
</div>

<div class="ocdf-map" markdown>

<div class="m-govern" markdown>
[**GOVERN**<br><span>mandate, risk, roles, budget, oversight</span>](docs/govern.md)
</div>

<div class="m-flow" markdown>
<div markdown>[**IDENTIFY**<br><span>what we defend and what threatens it</span>](docs/identify.md)</div>
<div markdown>[**PROTECT**<br><span>reduce likelihood and blast radius</span>](docs/protect.md)</div>
<div markdown>[**DETECT**<br><span>find adversary activity fast</span>](docs/detect.md)</div>
<div markdown>[**RESPOND**<br><span>contain, eradicate, report</span>](docs/respond.md)</div>
<div markdown>[**RECOVER**<br><span>restore trusted service, learn</span>](docs/recover.md)</div>
</div>

<p class="m-loop"><span class="m-loop-label" aria-hidden="true">Lessons learned</span><span class="m-loop-text">↺ Lessons learned in RECOVER feed the next round of IDENTIFY</span></p>

<p class="m-lenses" markdown>
Each capability is also read through the [**CIA triad**](docs/cia-triad.md)
and the [**regulatory layer**](docs/eu-regulatory-landscape.md): NIS2, GDPR,
DORA, CRA, CER and the national rules of all 27 member states. People and
process come before technology in every build sequence.
</p>

</div>

Every function page has the same parts: capabilities with IDs like `DE-2`,
maturity criteria, the EU rules that apply, and the other departments it
depends on. Reaching Level 2 in every function also covers what NIS2 requires,
as the [NIS2 Article 21 crosswalk](docs/nis2-article-21-crosswalk.md) shows. If
the terms are new, [OCDF on one page](docs/one-page.md) explains them in five
minutes.

## Start building

Seven steps, from deciding how much of the framework you need to the routine
that keeps the work going. Each one leaves you with a document you keep: a
signed charter, a scored baseline, a plan with names and dates on it. They go
into your own document system and governance process, and none of them depends
on this website.

<div class="ocdf-path" markdown>

<p class="ocdf-phase">Design</p>

1.  **Choose your tier.** Essential, Standard or Advanced decides how much of the
    framework applies to you. [Implementation tiers](docs/tiers.md)
    <span class="ocdf-output">Output: target tier</span>
2.  **Run the design workshops.** Six workshops, one per function, surface your
    gaps and the decisions nobody has taken yet. [Design navigator](assessments/cdc-design-navigator.md)
    <span class="ocdf-output">Output: design gaps logged as backlog items</span>
3.  **Adopt the charter.** Mandate, scope and containment authority, signed
    before anything is bought. [CDC charter](templates/cdc-charter-template.md)
    <span class="ocdf-output">Output: signed charter</span>
4.  **Decide the operating model.** In-house, provider or hybrid, with the
    staffing arithmetic and a cost template. [Operating models](docs/operating-models.md)
    <span class="ocdf-output">Output: target operating model and staffing numbers</span>

<p class="ocdf-phase">Build</p>

5.  **Assess where you are.** Score the maturity criteria and give every gap an
    owner and a due date. [Maturity self-assessment](tools/maturity-assessment.html)
    <span class="ocdf-output">Output: scored baseline with evidence, and an action plan with owners</span>
6.  **Work the first 90 days.** The order of work, week by week, with exit
    criteria. [Start here](docs/start-here.md)
    <span class="ocdf-output">Output: day-90 exit criteria met</span>

<p class="ocdf-phase">Run</p>

7.  **Set the operating rhythm.** The recurring work that keeps a CDC from
    decaying, and a detection portfolio that grows from your threat profile.
    [Annual calendar](templates/annual-calendar-template.md) ·
    [Detection use case](templates/detection-use-case-template.md)
    <span class="ocdf-output">Output: annual calendar and a growing detection portfolio</span>

</div>

## See it worked through

Exempla Parcel is invented, but its starting point is common: 2,500
employees, sorting that runs all night, four people in IT security and no SOC.
The [worked example](docs/worked-example.md) takes it through the seven steps,
from the tier decision to its first board report.

<div class="ocdf-case" markdown>

<ul class="ocdf-case__facts">
<li><b>2,500</b> employees</li>
<li><b>14</b> sites, night operations</li>
<li>NIS2 <b>important</b> entity</li>
<li><b>Standard</b> tier</li>
<li><b>Hybrid</b> operating model</li>
</ul>

<div class="ocdf-example" markdown>

<div class="ocdf-example__before" markdown>
<p class="ocdf-example__label">Before</p>

- Security spread across four people, with no shared plan
- No agreement on who may contain what
- Alerts looked at when someone had time
- Nobody named for NIS2 reporting
</div>

<div class="ocdf-example__arrow" aria-hidden="true"></div>

<div class="ocdf-example__after" markdown>
<p class="ocdf-example__label">After</p>

- A signed charter with containment authority
- A daytime team, and a provider for nights
- A scored baseline and a 90-day plan
- Maturity targets agreed with the board
</div>

</div>

<div class="ocdf-levels" role="img" aria-label="Maturity after 12 weeks. Govern level 1, target 3. Identify level 1, target 2. Protect level 2, target 3. Detect level 2, target 3. Respond level 2, target 3. Recover level 1, target 2." markdown>
<p class="ocdf-levels__title">Maturity after 12 weeks <span><i class="now"></i>Level now <i class="target"></i>Target</span></p>
<div><b>Govern</b><span><i class="n"></i><i></i><i class="t"></i><i></i></span></div>
<div><b>Identify</b><span><i class="n"></i><i class="t"></i><i></i><i></i></span></div>
<div><b>Protect</b><span><i class="n"></i><i class="n"></i><i class="t"></i><i></i></span></div>
<div><b>Detect</b><span><i class="n"></i><i class="n"></i><i class="t"></i><i></i></span></div>
<div><b>Respond</b><span><i class="n"></i><i class="n"></i><i class="t"></i><i></i></span></div>
<div><b>Recover</b><span><i class="n"></i><i class="t"></i><i></i><i></i></span></div>
<p class="ocdf-levels__scale" aria-hidden="true"><span>L1</span><span>L2</span><span>L3</span><span>L4</span></p>
</div>

</div>

[Read the worked example →](docs/worked-example.md){ .md-button }

The [templates](templates/index.md) are plain documents to copy and change.
The three [browser tools](tools/README.md) run entirely in your browser, and
nothing you type into them is sent anywhere. Everything is on
[GitHub](https://github.com/p0jst/OpenCDC) under CC BY 4.0, or as a
[zip download](https://github.com/p0jst/OpenCDC/archive/refs/heads/main.zip).

<div class="ocdf-meta" markdown>

**Version 1.2.0**, released 11 October 2026. See the [changelog](CHANGELOG.md).
Written and maintained by Frederik B. Krogsgaard, formerly Senior Manager at
the Norlys Cyber Defence Center, as an independent personal project. Each
national annex says when it was last reviewed and how confident that review
is, and [why trust this framework](docs/trust.md) sets out what you can and
cannot rely on.

**Scope: enterprise IT.** Endpoints, servers, identity, cloud and SaaS, with
limited cloud-specific depth so far. It is not designed for OT/ICS, telco core
networks or classified environments, and [About](ABOUT.md) explains why. If you
run critical infrastructure, see
[what still applies](ABOUT.md#if-you-run-critical-infrastructure) and
[the IT/OT interface](docs/it-ot-interface.md). Orientation only, not legal
advice.

</div>
