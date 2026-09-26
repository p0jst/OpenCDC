# Executive guide

The 30-minute version, for a CISO, a board member or an executive sponsor who
has to decide whether and how to fund a Cyber Defence Center. Each section links
to the detail.

## 1. What a CDC is, and what it is not

A Cyber Defence Center is the part of the organisation that notices an attack in
progress, stops it spreading, gets the business running again, and tells the
authorities in time. It is a capability, made of people, authority, process and
technology, not a product. Buying a SIEM or signing a monitoring contract does
not create one on its own; giving someone the mandate, the staff and the access
to act does.

## 2. What risk it reduces

<p class="src"><span class="src-tag practitioner">Practitioner</span>The author's reading of where a CDC changes outcomes.</p>

- **Time the attacker has.** Much of the damage in ransomware and data theft
  happens between first access and discovery. Good detection is the most direct
  way to shorten that time.
- **Blast radius.** A CDC with pre-agreed authority to isolate a laptop or
  disable an account contains an incident in minutes. Without it, the same
  decision waits for a meeting.
- **The legal clock.** NIS2 gives 24 hours from the moment you become aware of
  a significant incident to send an early warning. Meeting it at 02:00 on a
  Sunday takes someone who can recognise the incident, knows the reporting path
  and has the authority to use it.
- **Recovery that works.** Tested restores and a rebuild procedure decide
  whether an incident costs days or months.

## 3. What NIS2 asks of management

<p class="src"><span class="src-tag law">Law</span>Paraphrased from Directive (EU) 2022/2555. Your national law may add to it. Not legal advice.</p>

- **Management is accountable (Art. 20).** The management body must approve the
  cybersecurity risk-management measures, oversee how they are implemented, and
  can be held liable for failures. Its members must take part in cybersecurity
  training.
- **Minimum measures (Art. 21).** Ten areas, including incident handling,
  business continuity and backup, supply-chain security, basic cyber hygiene
  and training, access control, and multi-factor authentication. Incident
  handling cannot be done without a detection and response capability.
- **Reporting (Art. 23).** Significant incidents: early warning within 24 hours of
  becoming aware, notification within 72 hours, final report within one month.
- **Penalties (Art. 34).** Member states must allow maximum fines of at least
  €10 million or 2% of worldwide annual turnover, whichever is higher, for
  essential entities, and at least €7 million or 1.4% for important entities.

Financial entities are covered by DORA instead: an initial report within four
hours of classifying an incident as major, and no later than 24 hours after
becoming aware of it. Your country's rules are in its
[national annex](annexes/README.md); the full mapping is in the
[EU regulatory landscape](eu-regulatory-landscape.md).

## 4. What "good" looks like

<p class="src"><span class="src-tag ocdf">OCDF</span>This framework's targets. Set your own in GOVERN.</p>

Maturity is measured per function on four levels. Typical targets:

| Organisation | Target |
|--------------|--------|
| SME, low regulatory exposure | Level 2 in every function |
| NIS2 important entity | Level 2 in every function, with Respond at 3 for the reporting deadlines |
| NIS2 essential entity or DORA financial entity | Level 3 in every function |
| Critical infrastructure, high-threat sectors | Level 3–4, with Detect and Respond at 4 |

For an organisation in NIS2 scope, **Level 2 in every function is the legal
floor**: the Level 2 criteria contain the minimum form of every measure the law
requires, and a lower score means a measure is missing, whatever the target
says. See the [NIS2 Article 21 crosswalk](nis2-article-21-crosswalk.md).

Two things matter more than the headline number. **Balance:** Level 2 in every
function beats Level 4 in one and Level 1 in another, because the functions
depend on each other. Excellent detection is wasted without the authority to
contain, the reporting path or the backups to recover. **Evidence:** ask what
proves each score. An assessment without
evidence tends to flatter itself. See the
[maturity model](maturity-model.md).

## 5. Staffing and cost drivers

<p class="src"><span class="src-tag practitioner">Practitioner</span>Rules of thumb; the arithmetic is shown so you can redo it with your own numbers.</p>

- **Round-the-clock cover is expensive because of arithmetic, not salaries.**
  One seat staffed 24/7 takes about 5.5–6 people once leave, sickness and
  training are counted. An in-house 24/7 line with daytime capacity on top is
  typically 8–12 people.
- **Business hours with on-call** needs 3–4 people and suits many organisations
  whose risk decision allows it.
- **A provider does not remove the internal team.** Even with a managed service
  you keep 1–3 people for governance, escalation, response decisions and the
  contract.
- **The main cost lines** are people, the log platform (driven by how much data
  you collect and keep), endpoint protection, retention, the provider fee if you
  use one, a forensic retainer, and training. Compare the options over three
  years, not one.

The method and a cost template are in
[staffing and cost](operating-models.md#staffing-and-cost-the-arithmetic).

## 6. What you can outsource, and what you cannot

You can buy the watch: a provider can monitor around the clock and triage
alerts. You cannot buy:

1. **Accountability and risk acceptance.** They stay with management by law.
2. **The authority to shut down your own production systems.** You can let a
   provider act on your behalf, as managed detection and response contracts do,
   but your charter decides what it may do alone and who of yours decides the rest.
3. **Statutory reporting.** The 24-hour early warning is filed by you. A provider
   that alerts you after four hours has already used a sixth of the time.
4. **Knowing what matters.** Which systems are critical, and what normal looks
   like, is your knowledge.

See [operating models](operating-models.md).

## 7. A 12, 24 and 36-month roadmap

<p class="src"><span class="src-tag ocdf">OCDF</span>The framework's recommended sequence.</p>

| By | Outcome |
|----|---------|
| **Month 3** | Signed charter with containment authority; operating model decided; critical systems agreed; identity and endpoint monitoring live; one reporting drill done against the 24-hour clock. |
| **Month 12** | Level 2 in every function, which for a NIS2 entity is the legal floor. Detection built around your real threats; tuning routine running; incident plan exercised with management; restores tested for critical systems. |
| **Month 24** | Level 3 in the functions your targets require. Coverage and response times measured; hunting on a schedule; lessons from incidents tracked to closure. |
| **Month 36** | Targets met and evidenced. Operating model reviewed, insourcing or changing provider as the data suggests; detections validated by testing. |

The first 90 days are laid out week by week in [Start here](start-here.md).

## 8. What the board should see

Few numbers, each tied to a decision. Report quarterly:

| Measure | Why it matters |
|---------|----------------|
| Maturity per function against target, with trend | Where to invest next |
| Median time to detect and to contain serious incidents | Whether the capability works when it counts |
| Statutory notifications made on time | Legal exposure |
| Critical systems with a successful restore test in the last 12 months | Whether recovery is real |
| Open actions from incidents and assessments, and how many are overdue | Whether lessons are acted on |

Avoid alert counts and "attacks blocked": they measure noise, not protection.
The full catalogue is in the [metrics template](../templates/metrics-kpi-template.md).

## 9. Ten questions to ask your SOC

1. Who may isolate a production system at 03:00, and where is that written down?
2. Which of our systems are critical, and who agreed the list?
3. When did we last restore a critical system from backup, and how long did it take?
4. How long did it take us to detect and contain our last three serious incidents?
5. Could we file a NIS2 early warning within 24 hours tonight? When did we last practise it?
6. What are we blind to? Which systems send no logs to the SOC?
7. Which of our detections have we tested in the last year?
8. What does our provider do, and not do, and how would we leave them?
9. What single person's resignation would hurt us most?
10. What is our maturity by function, what is the evidence, and what will it take to reach target?

*Open CDC Framework, licensed CC BY 4.0.*
