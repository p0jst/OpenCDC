# Find your route

<p class="src" markdown><span class="src-tag opencdc">OpenCDC</span><span class="src-tag practitioner">Practitioner</span>The routes are OpenCDC's; the questions come from starting cyber defence teams of very different sizes.</p>

> **This is a Build page.** Build pages ask you to decide something and leave you with a document. Learn pages, such as [OpenCDC on one page](one-page.md) and the [worked example](worked-example.md), explain OpenCDC and ask nothing of you. Read those whenever you like; you do not need them to start here.

Most of OpenCDC is the same for everyone. Where you start, what you skip for now and how far you go is not. Answer the five questions below before you open anything else, and write the answers down. They take half an hour, and step 3 of the build path, the charter, uses them.

## Five questions to answer first

### 1. Why are you doing this now?

| If the main reason is | Then |
|-----------------------|------|
| A law applies, or may apply: NIS2, DORA or a national rule | Run the [regulatory selector](../tools/regulatory-profile.html) first. Reporting readiness moves to the front of your first 90 days, because the 24-hour early warning has to work before your first significant incident, not after it. |
| An incident or a near miss | Do not wait for the design work. This week, check two things: who may isolate a system at night, and who reports to the authorities. They are §4 of the [charter](../templates/cdc-charter-template.md) and the decision table in the [IR plan](../templates/incident-response-plan-template.md). Then take your route. |
| The board, a customer or an auditor asked | Find out what evidence they expect. The maturity baseline in step 6 is usually the thing to show, so plan towards it. |
| You run a team and want it better | Take route C. |

### 2. How many people work on security, and how much of their time?

This decides your route more than anything else.

- **One to three people, with security alongside other work.** Route A.
- **A team being built, or a few people with security as their job.** Route B.
- **A team that has run detection and response for a year or more,** your own or through a provider you manage closely. Route C.

### 3. What exists already?

- **Nothing written down.** Start at step 1 of your route.
- **A provider or a SIEM, but nobody owns the result.** That is common and fixable. Your step 4 is a review of what you have bought, using the [MSSP requirements checklist](../templates/mssp-requirements-checklist.md), not a new decision.
- **A working team.** Route C. Assess first, decide after.

### 4. Which hours must someone be watching?

You do not answer this alone; it is a risk decision for management. Ask the business what happens if an attack starts at 02:00 on a Saturday and nobody looks until Monday. [Operating models](operating-models.md) shows the staffing arithmetic: covering every hour of the year takes far more people than most organisations expect, which is why most small and mid-sized teams buy the night shift.

### 5. Where do you want to be in twelve months?

Pick one, and say it out loud to whoever funds you:

- **Able to detect the common attacks and report on time.** Essential tier, maturity Level 2.
- **A measured function that covers all six areas and improves on its own data.** Standard tier, Level 3.
- **Validated and largely automated, for critical infrastructure or a high-threat sector.** Advanced tier, Level 3 to 4.

Pairings and the reasoning behind them are in [implementation tiers](tiers.md).

## Three trade-offs to decide on purpose

Teams that skip these end up deciding them by accident.

- **Buy or build.** Round-the-clock watching, forensics and threat intelligence can be bought. Knowing your business, holding containment authority and reporting to regulators cannot. Decide which is which before you hire or sign.
- **Mandate first, or quick wins first.** Both, in parallel. Get the charter signed, but do not let MFA, a tested backup and the first log sources wait for it. The [first 90 days](start-here.md) run them side by side.
- **Breadth or depth.** Cover all six functions in their minimum form before you go deep in one. A strong detection team without a recovery plan fails in the same incident as a weak one.

## Your route

<div class="grid cards opencdc-routes" markdown>

-   **A. Small IT team**{ #route-a }

    ---

    One to three people, security is part of the job. Essential tier.

    1. [Step 1](build-path.md#step-1-choose-your-tier): read *If you are the whole security function*.
    2. [Step 3](build-path.md#step-3-adopt-the-charter): a short charter, with containment authority and the reporting path.
    3. [Step 4](build-path.md#step-4-decide-the-operating-model): decide what to buy, usually a provider for the hours you cannot cover. If the provider may act for you, add that to §4 of the charter.
    4. [Step 5](build-path.md#step-5-work-the-first-90-days): MFA, a tested restore and the first log sources come first.
    5. [Step 6](build-path.md#step-6-assess-where-you-are): Essential capabilities only.
    6. [Step 7](build-path.md#step-7-set-the-operating-rhythm): a light yearly rhythm.

    **Skip for now:** most of step 2. Do the GOVERN questions and leave the rest until a second person joins.

-   **B. Starting a SOC or CDC**{ #route-b }

    ---

    A team being built, or a few people with security as their job. Usually Standard tier.

    All seven steps of the [build path](build-path.md), in order. Steps 2 to 4 are the first weeks of the 90-day plan in step 5, so they overlap in time.

    **Skip for now:** threat hunting, SOAR and detection-as-code pipelines. The first 90 days lists what not to do in year one, and why.

-   **C. Running one already**{ #route-c }

    ---

    A team that has run for a year or more. Standard or Advanced tier.

    1. [Step 6](build-path.md#step-6-assess-where-you-are) first: score what you have. Reuse a SOC-CMM, SIM3 or CIS assessment where you have one.
    2. [Step 1](build-path.md#step-1-choose-your-tier): check that your tier matches what you actually run.
    3. [Step 2](build-path.md#step-2-run-the-design-workshops): workshops only for the functions that scored lowest.
    4. [Step 3](build-path.md#step-3-adopt-the-charter): check that the charter grants containment authority and names who reports. These are the gaps most often found in running teams.
    5. [Step 7](build-path.md#step-7-set-the-operating-rhythm): compare your rhythm with the calendar.

    **Skip:** step 4 unless you are changing model, and step 5. Go next to [Running the CDC](cdc-operations.md) and the deep dives.

</div>

When the answers point two ways, take the smaller route and step up later. Stepping up from A to B is cheap. Unwinding a design that was too big for the team is not.

*OpenCDC, licensed CC BY 4.0.*
