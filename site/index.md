---
title: Home
hide:
  - navigation
  - toc
---

<div class="ocdf-hero" markdown>

<p class="ocdf-eyebrow"><span>Written for NIS2, DORA and GDPR</span> · <span>All 27 EU member states</span></p>

# Build and mature your cyber defence

<p class="ocdf-lead" markdown>
A free framework for the people who detect and respond to cyber attacks, from
a 24/7 Cyber Defence Center to two people in IT. Standards say what security
covers and NIS2 says what you must do. Neither says how to set up and run the
team that does the work. OCDF does.
</p>

<div class="ocdf-cta" markdown>
[Start building](#start-building){ .md-button .md-button--primary }
[Understand OCDF in 5 minutes](docs/one-page.md){ .md-button }
</div>

<ul class="ocdf-assure">
<li>Free to use and adapt, also commercially</li>
<li>No account; tools run in your browser</li>
<li>Vendor-neutral</li>
</ul>

</div>

## Is this for me?

Yes, if part of your job is noticing attacks and dealing with them, whatever
your team is called. Every capability is marked with the smallest
[tier](docs/tiers.md) it belongs to, so a team of two sees what matters now.

<div class="grid cards ocdf-roles" markdown>

-   :material-account-wrench-outline:{ .lg .middle } **A small IT-security team**

    ---

    One to three people with other duties. What to buy rather than build, and
    the four things nobody can do for you.

    [Start small →](docs/tiers.md#if-you-are-the-whole-security-function)

-   :material-briefcase-outline:{ .lg .middle } **CISO or executive**

    ---

    Thirty minutes on what a CDC is for, what NIS2 expects of management, and
    what it costs.

    [Executive guide →](docs/executive-guide.md)

-   :material-hammer-wrench:{ .lg .middle } **Building a SOC or CDC**

    ---

    Seven steps from a signed charter to a team with a working routine.

    [Start building →](#start-building)

-   :material-chart-timeline-variant:{ .lg .middle } **Running one already**

    ---

    Score what you have, reusing any SOC-CMM, SIM3 or CIS assessment, and turn
    the gaps into a plan.

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

    Which EU laws apply to you, what they ask of a CDC, and the national rules
    in all 27 member states.

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
and the [**regulatory layer**](docs/eu-regulatory-landscape.md). Level 2 in
every function covers what NIS2 requires, as the
[NIS2 Article 21 crosswalk](docs/nis2-article-21-crosswalk.md) shows.
</p>

</div>

## Start building

Each step leaves you with a document you keep: a signed charter, a scored
baseline, a plan with names and dates.

<div class="ocdf-path" markdown>

<p class="ocdf-phase">Design</p>

1.  [**Choose your tier**](docs/tiers.md): how much of the framework applies to you.
2.  [**Run the design workshops**](assessments/cdc-design-navigator.md): one per function, to find the gaps.
3.  [**Adopt the charter**](templates/cdc-charter-template.md): mandate and containment authority, signed first.
4.  [**Decide the operating model**](docs/operating-models.md): in-house, provider or hybrid, with the staffing numbers.

<p class="ocdf-phase">Build</p>

5.  [**Work the first 90 days**](docs/start-here.md): steps 2 to 4 are its first weeks.
6.  [**Assess where you are**](tools/maturity-assessment.html): at day 90, with an owner and a date on every gap.

<p class="ocdf-phase">Run</p>

7.  [**Set the operating rhythm**](templates/annual-calendar-template.md): the recurring work that keeps a CDC from decaying.

</div>

## See it worked through

An invented company with a common starting point: four people in IT security,
no SOC, and operations that run all night. The worked example takes it
through the seven steps to its first board report.

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

<div class="ocdf-meta" markdown>

**Version 1.3.0**, released 27 October 2026 · [Changelog](CHANGELOG.md) ·
[Source on GitHub](https://github.com/p0jst/OpenCDC).
Written by Frederik B. Krogsgaard, formerly Senior Manager at the Norlys Cyber
Defence Center, as an independent project.
[Why trust this framework](docs/trust.md) says what you can and cannot rely on.

**Scope: enterprise IT.** Not designed for OT/ICS, telco core networks or
classified environments; see [About](ABOUT.md) and
[the IT/OT interface](docs/it-ot-interface.md).

</div>
