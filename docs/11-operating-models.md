# 11 — Choosing Your Operating Model

> **This is a decision document.** Before designing anything in DETECT or RESPOND, the organisation must choose how 24/7/365 monitoring and alerting will be operated. There are three core archetypes plus a shared/community variant, each with real trade-offs. Related: GOVERN GV-5, navigator question G6, charter template §3/§6.

## The three archetypes

### Model A — MSSP-operated, "telemetry out, alerts in"
Your telemetry, covering identity, endpoint, network and cloud, is forwarded to a Managed Security Service Provider who runs 24/7/365 eyes-on-glass triage and alerts you on qualified incidents. You retain a small internal function, often 1–3 FTE, for governance, escalation reception, and response coordination.

| Pros | Cons |
|------|------|
| 24/7 from day one, without hiring 8–12 FTE | Analysts lack your business context, so expect generic triage on your crown jewels |
| Predictable OPEX; scales up/down contractually | Multi-tenant attention: your P3 competes with another client's P1 |
| Access to scarce skills like DFIR and hunting that you can't retain solo | Telemetry leaves the organisation, so data residency, GDPR processor terms and log ownership must be contractually nailed down |
| Mature process, tooling and threat intel included | Detection logic is often opaque; you can't measure ATT&CK coverage you can't see |
| Fastest route to NIS2 24 h reporting readiness | **Accountability never transfers:** NIS2 Art. 20 liability, risk acceptance and statutory reporting remain yours regardless of contract |
| | Exit is hard: proprietary formats and lost tuning history create lock-in |

**Fits:** SMEs and important entities without security hiring power; organisations needing 24/7 *now*.

### Model B — In-house tiered SOC, Tier 1 → 2 → 3
The classical pyramid: Tier 1 does front-line triage on shift, escalates to Tier 2 investigators, with Tier 3 for hunting, DFIR and engineering behind them. Sustained 24/7 in-house realistically requires **8–12 FTE** for the shift line with daytime capacity on top, and that still means one analyst alone at night; see [staffing and cost](#staffing-and-cost-the-arithmetic).

| Pros | Cons |
|------|------|
| Full business context in every triage decision | High fixed cost; hard business case below large-enterprise scale |
| Full control of detection logic, coverage measurement, and data | Tier 1 burnout/attrition is the classic failure mode: repetitive work, night shifts, EU talent shortage |
| Clear entry-level career ladder, which helps recruitment | Tiers create hand-off friction and "ticket tennis"; knowledge concentrates at the top |
| Telemetry never leaves the organisation | Slow to build: 12–24 months to a functioning 24/7 line |
| Institutional knowledge compounds internally | Quality depends on runbooks; weak runbooks turn Tier 1 into an expensive routing layer |

**Fits:** large/essential entities, high-confidentiality sectors, organisations at Level 3+ ambitions with hiring power.

### Model C — In-house capability-based, "tierless"
No tiers: analysts own alerts end-to-end, from detect through investigate to contain, organised by *capability*, meaning detection engineering, hunting and response, rather than seniority layers. Heavy investment in automation/SOAR replaces the Tier 1 filter. Often run 8×5 plus on-call, or follow-the-sun in multinationals.

| Pros | Cons |
|------|------|
| Richer work → better retention than a Tier 1 line | Requires all-senior hiring, which is expensive and scarce; no junior entry ramp unless you deliberately build one |
| No hand-off losses; ownership drives quality | 24/7 coverage is the hard problem: on-call fatigue or follow-the-sun complexity |
| Automation-first mindset compounds efficiency | Demands mature engineering culture, meaning detection-as-code and SOAR, from day one |
| Detection engineering and response cross-pollinate naturally | Small teams are fragile: two resignations can break coverage |

**Fits:** engineering-strong organisations, cloud-native environments, teams of ~5–8 senior FTE that accept on-call rather than shift coverage.

## Hybrid patterns — the most common EU reality

- **A+C:** MSSP runs the 24/7 night/weekend watch; the internal capability-based team owns detection engineering, business-context triage in daytime, and all response decisions. Often the best cost/quality point.
- **A+B:** MSSP as Tier 1, internal Tier 2/3. Works only if the escalation interface is drilled and the MSSP's output quality is measured.
- **Follow-the-sun, on Model C:** for multinationals with 3+ regions, giving coverage without night shifts, at coordination cost.
- **Existing 24/7 operations as first line:** if the organisation already runs a 24/7 NOC/operations desk, train it to receive security alerts out of hours and wake the CDC's on-duty officer against defined criteria. Cheap night coverage without a security night shift, but invest in crisp escalation criteria and drill them, or the desk becomes a bottleneck.
- **Shared / community CDC, Model D:** one CDC serving several constituent organisations such as shared service centres, sector cooperatives and municipal partnerships, a common European pattern. It combines Model B/C internally with an MSSP-like *external* interface per constituent, so it needs both the in-house discipline of B/C **and** the contractual clarity of Model A: per-constituent containment mandates from the containment action catalogue template, per-constituent reporting and SLAs, strict data separation between constituents, and an RFC 2350-style public service description. Statutory reporting duties remain with each constituent entity.

## What can NEVER be outsourced, in any model

1. **Risk acceptance and management accountability** — NIS2 Art. 20 liability sits with your management, full stop.
2. **Containment authority over crown jewels** — the MSSP may recommend; who may isolate your production is a charter §4 decision.
3. **Statutory reporting** — the 24 h early warning is filed by *you*; an MSSP SLA of "notify within 4 h" already spent a sixth of your clock.
4. **The regulatory applicability register and this framework's GOVERN function.**

## Decision path

<p class="src" markdown><span class="src-tag ocdf">OCDF</span>A sequence of constraints, not a score. Work down it and stop where a question decides the answer.</p>

The operating model is usually decided by one or two hard constraints, not by adding up preferences. Take the questions in order:

1. **Is any log data legally or contractually barred from leaving the organisation or the country?**
   Yes → keep those sources in-house (**B** or **C**). A provider can still hold the watch over everything else, as a hybrid.
2. **Do you need out-of-hours detection within six months?**
   Yes → start with a provider (**A**, or **A+C** if you already have a team), and contract for exit from day one: log ownership, portable detections, a transition clause. Then continue down the path to decide what comes after.
3. **Can you hire and keep the roughly 9–10 people a single 24/7 seat takes, with daytime capacity on top?** See [the arithmetic](#staffing-and-cost-the-arithmetic).
   No → a provider holds nights and weekends (**A** or **A+C**). If you already run a 24/7 operations desk, it can be the out-of-hours first line instead.
4. **Do you have, or can you hire, 5–8 senior people who work with version control and automation?**
   Yes → a capability-based team (**C**), with a provider or on-call for nights.
   No, but you can hire and train juniors → a tiered SOC (**B**).
   Neither → **A**, with 1–3 internal people.
5. **Does triage need deep business knowledge**, such as bespoke applications, fraud patterns or systems next to OT?
   Yes → whatever the model, keep triage of those alerts in-house.

Two things to settle whichever way the path goes:

- **Budget shape.** Provider fees are predictable operating cost; an in-house team is headcount. Finance often has a preference; find out before you design around it.
- **The three-year view.** Operating models are three-year decisions. If you start with a provider, write the conditions for insourcing, or for changing provider, into the contract now.

**Record the decision** in the CDC charter, §3 services and §6 resourcing, with rationale and a review date. Operating models are 3-year decisions, not permanent ones. If choosing Model A, use the [MSSP requirements checklist](../templates/mssp-requirements-checklist.md) before signing anything.

## Staffing and cost: the arithmetic

A budget round needs numbers, and the numbers that matter most are specific to your country, your contracts and your estate. This section gives the method and the formulas; put your own figures in. Where it quotes a figure, the figure is an input you should replace, not a benchmark.

### How many people one seat takes

A *seat* is one analyst at the console at any given moment. Covering one seat around the clock means covering every hour of the year; each person you employ works far fewer than that.

| Step | Formula | Example, Danish full-time contract |
|------|---------|------------------------------------|
| Hours to cover per seat | 24 × 365 | 8,760 h |
| Contract hours per FTE | weekly hours × 52 | 37 × 52 = 1,924 h |
| minus annual leave | your leave entitlement | 5 weeks: −185 h |
| minus public holidays on weekdays | your calendar | ~9 days: −67 h |
| minus sickness | your absence rate | ~8 days: −59 h |
| minus training and exercises | your training plan | 5 days: −37 h |
| **Available hours per FTE** | | **≈ 1,576 h** |
| **FTE per 24/7 seat** | 8,760 ÷ available hours | **≈ 5.6** |

Replace every number in the example column with your own. With six weeks of leave, or a higher absence rate, the answer moves towards 6. It never gets close to the "four or five people on a rota" that 24/7 plans often assume.

Then build the line from seats:

| Line | Hours per year | FTE, using 1,576 h |
|------|----------------|--------------------|
| One seat, 24/7 | 8,760 | 5.6 |
| A second seat, weekdays 07–17 | 250 days × 10 h = 2,500 | 1.6 |
| Detection engineering, off the shift rota | — | 1–2 |
| Team lead or manager | — | 1 |
| **Total** | | **≈ 9–10** |

That is where the framework's 8–12 FTE for a 24/7 in-house line comes from. A second seat at night as well adds another 4 FTE. Two further constraints bite in practice: the EU Working Time Directive and national rules limit night work and require rest periods, which shapes the rota, and a rota with fewer than about six people leaves no slack when someone resigns.

**The lone night analyst.** With one 24/7 seat, nights and weekends are a single person. Decide deliberately how that is made safe:

- a named second-line responder on call, with a response-time target, and an automatic escalation to them if a P1 alert is not acknowledged in time
- no containment action on crown jewels taken alone at night; record in the [containment action catalogue](../templates/containment-action-catalogue-template.md)'s notes column which actions need a second person
- a welfare check-in and a clear rule for when to wake the on-call lead, so the analyst is never deciding alone whether something is serious enough
- or an A+C hybrid, where a provider with several analysts on shift holds the night and your team holds the day

### What it costs

Build the cost from lines you can each defend separately. A single "SOC budget" number is the one finance will cut first.

| Cost line | How to estimate it | Watch for |
|-----------|--------------------|-----------|
| **People** | FTE × fully loaded annual cost. Fully loaded means salary plus employer costs, pension, shift and on-call allowances, equipment and training; ask finance for your organisation's multiplier | Shift and on-call allowances are often left out and can be significant; recruitment fees and time-to-hire |
| **SIEM or log platform** | Measure ingest, don't guess: sample two weeks of your priority log sources and extrapolate GB per day. Then apply the vendor's model: per GB ingested, per event rate, per asset or per user | Growth as sources are added; hot versus archive retention priced differently; parsing or search charged separately |
| **Log retention** | GB per day × retention days × storage price, for each storage tier | Retention set by law or policy, not by what the licence includes |
| **EDR** | Endpoints and servers × price per agent | Server and cloud workloads often priced differently from laptops |
| **MSSP** | Quote against your measured inventory and ingest. Common models: per endpoint or asset, per user, per GB or event rate, or a flat tier | What is included: triage only, or response actions too; ingest caps and overage; onboarding fees; data return and exit costs |
| **Internal team alongside an MSSP** | 1–3 FTE for governance, escalation, response and contract management | This line is often forgotten in "buy" business cases, and the MSSP cannot replace it |
| **DFIR retainer** | Retainer fee plus pre-paid or discounted hours | Whether unused hours roll over; response-time guarantees |
| **Training and exercises** | Per FTE per year, plus tabletop and technical exercises | Certification renewals; time away from the rota, already counted above |
| **Engineering tooling** | Repositories, CI, test environments, automation platform | Usually small; skipped at a price |

### Comparing the options over three years

Operating models are three-year decisions, so compare them over three years, not one. Year one carries the build cost; for an in-house line it can take 12–24 months to reach full strength, and you pay for an MSSP or overtime in the meantime.

| Cost line | Model A: MSSP | Model B: tiered in-house | Model C: capability-based | A+C hybrid |
|-----------|---------------|--------------------------|---------------------------|------------|
| People | | | | |
| Platform and licences | | | | |
| Log retention | | | | |
| MSSP fees | | | | |
| DFIR retainer | | | | |
| Training and exercises | | | | |
| One-off build and onboarding | | | | |
| Exit or transition cost at year 3 | | | | |
| **Total, years 1–3** | | | | |

Fill in all four columns even when the answer looks obvious. The comparison is what convinces a board, and it records why the choice was made when it is reviewed in three years.

## Maturity note

The maturity model applies to **outcomes, not employment contracts**: with an MSSP you still score DETECT on *measured* coverage, validation and MTTD, which means your contract must give you visibility into detection logic and metrics. If it doesn't, your maturity ceiling is Level 2 by construction.

## Sources
- MITRE, *11 Strategies of a World-Class Cybersecurity Operations Center*, 2nd ed., on sourcing and tiering.
- NIST CSF 2.0, GV.SC on cybersecurity supply chain risk management.
- NIS2: Directive (EU) 2022/2555 Art. 20–21, 23.

*Open CDC Framework, licensed CC BY 4.0.*
