# Why trust this framework, and where not to

OCDF combines three kinds of material: law and published standards, guidance
from recognised bodies, and one practitioner's judgement about how to build and
run a CDC. They deserve different amounts of trust, so the framework labels
which is which.

## The five labels

Sections that make claims carry a label under their heading:

| Label | What it means | Examples | How far to rely on it |
|-------|---------------|----------|-----------------------|
| <span class="src-tag law">Law</span> | Paraphrased from EU or national legislation | NIS2 Art. 23 reporting deadlines; GDPR Art. 33 | Only as a pointer. Check the article itself and your national law; this is not legal advice |
| <span class="src-tag standard">Standard</span> | Taken from a published standard or framework | The six NIST CSF 2.0 functions; MITRE ATT&CK technique IDs; RFC 3227 order of volatility | As far as you rely on the standard itself |
| <span class="src-tag guidance">Guidance</span> | Good practice published by a recognised body | ENISA, FIRST and CISA publications; SIM3 | Widely accepted, but guidance, not requirement |
| <span class="src-tag ocdf">OCDF</span> | This framework's own design: capability breakdown, tiers, maturity levels and criteria, build order | The four maturity levels; the 90-day plan | A reasoned recommendation. Nobody certifies against it |
| <span class="src-tag practitioner">Practitioner</span> | The author's experience of running a CDC | Staffing estimates; log-source priority; first-hour actions | One experienced person's judgement. Weigh it against your own |

## What has been checked, and what has not

**Checked:**

- The EU legal texts the framework relies on are listed with links to the
  official versions on EUR-Lex in [references and credits](19-references.md).
- The national annexes each show when they were last verified, by whom, and how
  confident that verification is. See the [annex index](annexes/README.md).
- The framework's own documents are consistent with each other: capability IDs,
  maturity criteria and templates match across pages and tools.

**Not checked:**

- **No independent legal review.** The reporting deadlines and national law
  references have been checked by the author, not by a lawyer.
- **No field calibration.** The maturity criteria, the SOC-CMM score translation
  and the staffing figures come from experience, not from measured data across
  many CDCs.
- **One maintainer.** Most national annexes have no second reviewer yet.
- **No listed adopters.** No organisation has yet asked to be named as a user.

## Who is behind it

One practitioner, Frederik B. Krogsgaard, formerly Senior Manager at the Norlys
Cyber Defence Center, who built a 24/7 CDC for critical infrastructure and has
sponsored SIM3 assessments for CSIRT certification. The project is personal and
not affiliated with any employer, NIST, ENISA, MITRE or any authority. See
[About](../ABOUT.md).

## How to use it safely

- Treat **Law** labels as a starting point for your lawyer, not a conclusion.
- Treat **OCDF** and **Practitioner** content as a well-argued proposal. Where
  your context differs, your judgement wins, and the framework says so.
- Cite the version: "Open CDC Framework v1.0.0". Criteria can change between
  versions; the [changelog](../CHANGELOG.md) lists every change to scoring.
- Report errors. Corrections, and second reviewers for the national annexes,
  are the most useful contributions. See [contributing](../CONTRIBUTING.md).

*Open CDC Framework, licensed CC BY 4.0.*
