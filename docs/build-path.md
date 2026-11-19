# The build path

<p class="src" markdown><span class="src-tag opencdc">OpenCDC</span><span class="src-tag practitioner">Practitioner</span>The order is OpenCDC's; effort figures are rough, from experience, and depend on how quickly people sign.</p>

> **This is a Build page.** Seven steps, each ending with something you keep. Your [route](find-your-route.md) says which steps apply to you and in what order. Each step links to the page that does the work; that page sends you back here when you are done.

The steps move from broad to concrete: first what you are building, who decides and who does the work, then building it, then running it. Detection rules, playbooks and tooling come inside step 5 and after, once the decisions they depend on exist.

<p class="opencdc-phase">Design</p>

## Step 1: Choose your tier

- **You decide:** how much of OpenCDC applies to you. Essential, Standard or Advanced, on size, complexity and threat exposure.
- **You leave with:** a tier, and the list of capabilities in it.
- **Effort:** an hour.
- **Use:** [Implementation tiers](tiers.md).
- **Done when:** you can say which capabilities you will not build yet, and why.

## Step 2: Run the design workshops

- **You decide:** where the gaps are, one function at a time, with the people who own the answers in the room.
- **You leave with:** written answers per function and a first list of gaps.
- **Effort:** two to four hours per function.
- **Use:** the [design navigator](../assessments/cdc-design-navigator.md).
- **Done when:** every question has an answer, or a named owner and a date.
- **Route A:** the GOVERN questions are enough for now.

## Step 3: Adopt the charter

- **You decide:** what the team is for, what it covers, and what it may do without asking, above all who may isolate a system and who reports to the authorities.
- **You leave with:** a charter signed by management.
- **Effort:** a day to draft. Signing usually takes weeks, so start early.
- **Use:** the [charter template](../templates/cdc-charter-template.md), with your answers from [Find your route](find-your-route.md).
- **Done when:** it is signed, and the people on call know what §4 lets them do.
- **Route C:** check the charter you have for containment authority and the reporting path; those are the parts most often missing.

## Step 4: Decide the operating model

- **You decide:** which hours are covered, and who covers them: your own team, a provider, or both.
- **You leave with:** a decision with the staffing numbers behind it, and for a provider, the requirements to buy against.
- **Effort:** a few weeks, mostly waiting for the coverage-hours decision from management.
- **Use:** [Operating models](operating-models.md), and the [MSSP requirements checklist](../templates/mssp-requirements-checklist.md) if you buy.
- **Done when:** management has accepted the hours that are not covered, in writing.

<p class="opencdc-phase">Build</p>

## Step 5: Work the first 90 days

- **You decide:** nothing new. This is where the decisions from steps 1 to 4 become controls, log sources and a tested plan.
- **You leave with:** MFA coverage measured, a restore proven, identity and endpoint telemetry flowing, an IR plan and a reporting drill done.
- **Effort:** twelve weeks. Steps 2 to 4 are its first weeks, so they overlap.
- **Use:** [The first 90 days](start-here.md).
- **Done when:** the day-90 exit criteria on that page are met.

## Step 6: Assess where you are

- **You decide:** your maturity targets per function, with management.
- **You leave with:** a scored baseline and a gap list with an owner and a date on every line.
- **Effort:** a day with the people who hold the evidence.
- **Use:** the [interactive self-assessment](../tools/maturity-assessment.html), or the [list of criteria](../assessments/maturity-self-assessment.md) to read first.
- **Done when:** the targets are agreed and the gap list is in someone's plan.
- **Route C:** this is your step 1.

<p class="opencdc-phase">Run</p>

## Step 7: Set the operating rhythm

- **You decide:** when the recurring work happens: reviews, tests, exercises and reports.
- **You leave with:** a year's calendar with an owner on each item.
- **Effort:** an hour to fill in; then it runs all year.
- **Use:** the [annual operating calendar](../templates/annual-calendar-template.md).
- **Done when:** the next exercise and the next restore test have a date.

## After the build path

The daily work lives in [Running the CDC](cdc-operations.md), [alert triage](alert-triage.md) and the [deep dives](detection-as-code-deep-dive.md). The [templates](../templates/README.md) are the working documents you will fill in along the way. Reassess at month twelve and set next year's targets from the gaps.

*OpenCDC, licensed CC BY 4.0.*
