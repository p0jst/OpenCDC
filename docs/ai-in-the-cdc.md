# AI in the CDC

<p class="src" markdown><span class="src-tag ocdf">OCDF</span><span class="src-tag practitioner">Practitioner</span>This framework's guidance on AI in security operations; the regulatory section is paraphrased law and marked as such.</p>

> AI touches a CDC in three ways: as a tool the team uses, as a tool the adversary uses, and as a set of systems the organisation runs and must protect. Most guidance covers only the first. This document covers all three, and says what changes with team size, because a two-person IT-security team and a 24/7 CDC should not adopt AI the same way.

## Principles

These hold at every size and in every use below.

1. **A person is accountable for every decision.** AI may gather, summarise, draft and propose. The decision to close, declare, contain or report stays with a named person, and the case shows who.
2. **The process comes first.** AI applied to an untuned rule set or an unwritten playbook speeds up the noise. A task that cannot be done by hand from a written procedure is not ready for AI.
3. **Output is a hypothesis until checked.** A model's finding counts as evidence only after a person has checked it against the source data, and the case records how.
4. **Data classification decides the platform.** Alerts, logs and incident data are usually personal data and often confidential. Which data may go to which AI service is decided before use, not during an incident.
5. **Record what the AI did.** Which findings came from a model, which were accepted or rejected, and by whom. This is what makes AI use auditable and its error rate measurable.

## How team size changes the picture

The same use of AI carries different value and different risk depending on who uses it. Team size here is a rough guide; the [implementation tiers](tiers.md) are related but not the same thing.

| | One to three people | A dedicated CDC | A large or multi-team CDC |
|---|---------------------|-----------------|---------------------------|
| How AI usually arrives | Built into tools already in use: the EDR, the mail platform, the office suite, the provider's service | A mix of built-in features and an approved general-purpose assistant | Built-in features, approved assistants, and pipelines the team builds and runs itself |
| Where it helps most | Time: summarising, drafting, explaining unfamiliar artefacts, writing queries | Consistency and throughput: enrichment, summaries, rule drafting, report drafts | Scale: automated first-pass triage, investigation support, detection engineering at volume |
| The main risk | Nobody else is there to catch a wrong answer | Uneven use: each analyst uses it differently and nobody measures it | Automation nobody looks at, and analysts who never learn the craft because the model always drafts first |
| What to settle first | Which tools may see which data, and the vendor's terms for that data | A short AI use policy for the team, and the record in the case | Governance of automated decisions, measured error rates, and a training path that does not depend on the model |
| Realistic ambition | Assisted work by one person, always reviewed by that person | Assisted work across the team, measured | Automated steps with gates, measured and sampled |

Mid-sized teams often carry the most risk. They have the ambitions of large teams but rarely the capacity to measure and govern what they adopt. If that describes you, adopt fewer uses and measure each one.

## Uses, by team size

The scale used below:

- **Must** — do this if you use AI at all.
- **Should** — good value at this size; adopt when the conditions hold.
- **Can** — worthwhile where the conditions hold, but not a priority.
- **With caution** — possible, but only with the guardrails named in the conditions column.
- **Avoid** — the risk outweighs the gain at this size.

| Use | One to three people | Dedicated CDC | Large CDC | Conditions |
|-----|---------------------|---------------|-----------|------------|
| Summarising an alert or a cluster of alerts | Should | Should | Should | The summary links to the underlying events; nobody closes on the summary alone |
| Enrichment and context assembly | Should, via the tools you have | Should | Should | Deterministic lookups first; AI for what lookups cannot assemble |
| Explaining an unfamiliar artefact, script or log line | Should | Should | Can | Checked against the source; no sensitive data to unapproved services |
| Drafting search queries | Should | Should | Should | The query is read and understood before it is run |
| Drafting and converting detection rules, such as to Sigma | Can | Should | Should | Peer review and a test that makes the rule fire, per [Detection-as-code](detection-as-code-deep-dive.md) |
| Proposing a triage verdict | With caution | Should | Should | The [minimum triage record](alert-triage.md#decision-2-the-minimum-triage-record) is filled; a person decides; disagreement rate is logged |
| Closing alerts without a human | Avoid | With caution | With caution | Named rules only, as a suppression with owner, review sample and expiry; never for anything that could be reportable |
| Investigation support: logs, scripts, malware | With caution | Should | Should | Findings recorded with how they were verified; malware only to platforms approved for it |
| Summarising threat intelligence and translating reports | Should | Should | Should | The summary keeps the source and its TLP marking |
| Drafting management reports and post-incident reviews | Should | Should | Should | The author reads and owns the result |
| Drafting statutory notifications under NIS2, GDPR or DORA | With caution | With caution | With caution | Draft only; legal or the DPO reviews; never submitted automatically |
| Agents that investigate across systems on their own | Avoid | With caution | Can | Read-only rights, own identity, every action logged, a person reviews before anything changes |
| Automated containment | Avoid | With caution | With caution | Only actions marked automatic in the [containment action catalogue](../templates/containment-action-catalogue-template.md): reversible, low blast radius, never on crown jewels |
| Training and onboarding material | Can | Should | Should | Juniors also work cases without the model; see below |

## What every team must have

If the team uses AI at all, these are the minimum. Several are legal duties, not preferences; see [the regulatory section](#what-the-law-says).

- **A short AI use policy for the CDC**, under GV-3: which tools are approved, for which tasks, with which data classes. One page is enough for a small team.
- **A data rule.** Which data classes may go to which service, and on which terms. Incident data usually requires a processor agreement and an EU/EEA basis for any transfer; see [Running the CDC](cdc-operations.md) §4.
- **A named person for every decision**, and the case showing who it was.
- **A record of AI-assisted findings** in the case, with how each was verified.
- **AI literacy for the people who use it**, proportionate to their role and to what the tools do.
- **The provider's terms checked**: whether your data is used for training, where it is processed, how long it is kept, and how you get it out. Under Model A, ask the same of your provider about the AI it uses on your data.

## What to avoid at any size

- Closing as false positive anything that could start a reporting clock, on an AI verdict alone.
- Pasting incident data, credentials or personal data into services outside your approved terms.
- Treating model output as evidence without checking it against the source.
- Automated containment on crown jewels, or any automated action without a tested way back.
- Using AI output on employees' behaviour as the basis for HR action without a person's independent review; see the regulatory section.
- Buying a product for its AI claims. Procure against capabilities, per [Running the CDC](cdc-operations.md) §5, and ask the vendor for measured error rates on data like yours.

## Small teams: making it work

For a team of one to three, AI is mostly something that arrives inside tools already bought. The work is less about choosing uses and more about controlling the ones that come switched on.

- **Inventory what is already on.** Many security and office products now include AI features by default. List them, and check what data each one sends where.
- **Use AI to buy time, not to replace review.** Summaries, drafts and explanations save the most hours with the least risk. Verdicts and closures are where a single person has no second pair of eyes.
- **Ask your provider.** If a provider triages for you, ask how it uses AI on your alerts, what its error rate is, and how you see which closures were automated.
- **Keep the record short but real.** One line in the case saying what the AI proposed and what you decided is enough.

## Larger teams: what changes at scale

- **Measure like a control.** Disagreement rate between AI proposals and final dispositions, error rate on a sampled set of AI-assisted closures, and analyst time saved. The KPIs in [Running the CDC](cdc-operations.md) §4 apply.
- **Give agents identities.** Every AI agent or pipeline that touches systems runs under its own non-human identity with least privilege under PR-1, and its actions are logged like any administrator's.
- **Protect the craft.** If the model always drafts first, juniors stop learning to triage. Keep part of every analyst's work unassisted, and use exercises under RS-7 that are run without AI.
- **Version and test prompts and pipelines** that make decisions, in the same way as detection rules, with peer review and regression tests on known cases.
- **Plan for the model to be wrong or unavailable.** Every automated step needs a manual fallback that the team has actually practised.

## AI in the adversary's hands

The tools available to defenders are available to attackers. For a CDC this mostly changes priorities, not processes.

| What changes | What it means for the CDC | Where in the framework |
|--------------|---------------------------|------------------------|
| Phishing and pretexting are better written and better targeted. ENISA's 2025 threat landscape reports AI-supported phishing as more than 80 percent of observed social engineering | Detection based on poor language loses value. Weight sender, infrastructure and behaviour signals over content, and stop teaching users to look for spelling errors | PR-2, PR-9, DE-2 |
| Voice and video can be faked convincingly | Payment changes, helpdesk resets and access requests need verification through a separate, known channel, never the one the request arrived on | PR-1, GV-3 |
| Exploits and tooling can be produced faster | The window between disclosure and exploitation narrows. Prioritise remediation on known exploitation and exposure | ID-4, PR-5 |
| Attacker capability is spread more widely | Revisit the threat profile: less capable actors may now attempt techniques that were out of their reach | ID-5 |

## AI systems as assets to protect

AI systems the organisation runs are in scope for the CDC like any other system. This is enterprise IT and inside the framework's scope.

- **Inventory them** under ID-1: AI services in use, approved and unapproved, the agents and integrations built on them, and the API keys and tokens they hold. Unapproved use is a visibility gap, not only a policy breach.
- **Classify what they hold.** Prompt and response logs often contain the most sensitive data the organisation has. Apply data classification under ID-2 and retention rules accordingly.
- **Control what they can do.** Agents with broad rights turn a manipulated prompt into an action. Least privilege under PR-1, and human approval for changes, limit the damage.
- **Log them** under DE-1: who used which AI service, what an agent did, and which tools it called. Without it, an AI-related incident cannot be investigated.
- **Detect misuse.** Use cases for prompt injection attempts, unusual data volumes to AI services, and agents acting outside their normal pattern. The OWASP and MITRE ATLAS references below describe the techniques.
- **Write a playbook** from the [scenario playbook template](../templates/scenario-playbook-template.md) if your threat profile makes it likely: data leaked through an AI service, or a compromised agent or integration.

## What the law says

<p class="src" markdown><span class="src-tag law">Law</span>Paraphrased from the legal texts. Check the text itself and your national law; not legal advice. Points marked as interpretation are this framework's reading.</p>

**AI Act, Regulation (EU) 2024/1689**, as amended by the Digital Omnibus on AI, Regulation (EU) 2026/1744. A CDC that uses AI tools is normally a *deployer* under the Act; it becomes a *provider* only if it builds an AI system and puts it into service under its own name.

- **AI literacy, Art. 4**, applies since 2 February 2025: providers and deployers take measures to support AI literacy among the staff who operate and use AI systems, considering their role and the context of use.
- **Prohibited practices, Art. 5**, apply since 2 February 2025. For a CDC the relevant one is Art. 5(1)(f): AI systems that infer the emotions of people in the workplace are prohibited, except for medical or safety reasons. Insider-risk products that claim to read sentiment or emotional state from employees' communications fall close to this line.
- **High-risk systems, Annex III point 4**, include AI used to monitor and evaluate the performance and behaviour of people in work relationships. After the Omnibus, the high-risk obligations for Annex III systems apply from 2 December 2027.
- **Interpretation:** whether security monitoring that profiles employees' behaviour, such as user and entity behaviour analytics, falls under Annex III point 4 is not settled. Its purpose is security, not evaluating work, but it analyses the behaviour of identifiable employees. Assess each such tool before 2 December 2027, record the reasoning, and involve the DPO and legal. If a tool is high-risk, deployer duties under Art. 26 follow, including informing workers' representatives and affected workers before use at the workplace.

**GDPR, Regulation (EU) 2016/679.**

- An AI service that processes incident data on your behalf is a processor under Art. 28; transfers outside the EU/EEA need a basis under Chapter V.
- Behaviour analytics on employees usually requires a data protection impact assessment under Art. 35.
- Art. 22 limits decisions based solely on automated processing that significantly affect a person. *Interpretation:* temporary security measures such as revoking a session are generally not such decisions, but an AI finding that leads to disciplinary or HR action should pass through a person's independent review.

**NIS2, Directive (EU) 2022/2555.** AI providers are suppliers like any other: their security, their terms and their incident notification belong in supply chain security under Art. 21(2)(d), and AI features in systems you buy fall under security in acquisition under Art. 21(2)(e). See GV-6 and the [NIS2 Article 21 crosswalk](nis2-article-21-crosswalk.md).

**National employment law** may require notice to or consultation with employee representatives before new monitoring is introduced, as described in [Respond](respond.md). AI-based monitoring is no exception.

## Where this fits in the maturity model

The maturity criteria do not score AI use, and AI is not a way to skip a level. A team at Level 1 that adopts AI is a Level 1 team with faster tools. The criteria AI affects are the ones it depends on: a documented triage runbook and severity matrix in DETECT, the containment mandates in RESPOND, and data classification in IDENTIFY. Get those to Level 2 first.

## Sources

- AI Act: Regulation (EU) 2024/1689. https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Digital Omnibus on AI: Regulation (EU) 2026/1744, amending the AI Act. https://eur-lex.europa.eu/eli/reg/2026/1744/oj
- GDPR: Regulation (EU) 2016/679, Art. 22, 28, 35 and Chapter V. https://eur-lex.europa.eu/eli/reg/2016/679/oj
- NIS2: Directive (EU) 2022/2555, Art. 21(2)(d) and (e). https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- ENISA, *ENISA Threat Landscape 2025*. https://www.enisa.europa.eu/topics/cyber-threats/threat-landscape
- OWASP GenAI Security Project, *Top 10 for LLM Applications*, for risks such as prompt injection and excessive agency. https://genai.owasp.org
- MITRE ATLAS, *Adversarial Threat Landscape for Artificial-Intelligence Systems*. https://atlas.mitre.org

*Open CDC Framework, licensed CC BY 4.0. Credits: [References & credits](references.md).*
