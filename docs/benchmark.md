# Community benchmark

<p class="src" markdown><span class="src-tag ocdf">OCDF</span>Self-assessed data from organisations that choose to contribute. Context, not a standard.</p>

The [maturity self-assessment](../tools/maturity-assessment.html) can show how
your scores compare with other organisations like yours: the median level per
function, and for each criterion the share of organisations that have it in
place. The figures come from anonymous contributions by the tool's users.

**Status: collecting.** The benchmark opened on 23 September 2026 and has no
published figures yet. They appear group by group as each reaches ten
contributions.

## How to read it

- **It is context, not a target.** Your targets are a risk decision, set in
  GOVERN. Being at the median says nothing about whether that is enough for your
  risks. See [target-setting guidance](08-maturity-model.md#target-setting-guidance).
- **It is self-assessed.** Contributors score themselves, mostly without
  evidence being checked, and organisations that choose to contribute tend to be
  the more mature ones. Expect the figures to run higher than an audited sample.
- **It compares like with like only as far as the groups allow.** Groups are
  formed by number of employees, NIS2 category and region, never combined, so
  that every group stays large enough to be anonymous.

## What a contribution contains

When you choose **Contribute your result anonymously** in the tool, you see the
exact content before anything is sent:

| Included | Not included |
|----------|--------------|
| Number of employees, as a band: 1–49, 50–249, 250–999, 1,000–4,999, 5,000 or more | Your organisation's name |
| NIS2 category: essential, important, not in scope, or not sure | Country (only a broad region) |
| Region: Nordics, Western, Central and Eastern, or Southern Europe, or outside the EU | Evidence notes, owners, due dates |
| Sector, from a short list | Targets and target profile |
| Operating model | Assessors' names, assessment date (only the month) |
| The status of each of the 60 criteria, and whether evidence-based scoring was on | Anything else from your assessment link |
| The month and the framework version | |

Nothing is sent by the tool itself. You email the contribution, or download the
file and send it, to **benchmark@opencdc.org**.

## How contributions are handled

- **Raw contributions are never published.** They are kept by the maintainer,
  outside the public repository, and used only to compute the aggregate.
- **No figure describes fewer than ten organisations.** A group below ten shows
  only how many contributions it has so far.
- **Groups are never combined.** You can compare with organisations of your
  size, or of your NIS2 category, or of your region, but not "your size in your
  region", which could narrow a group to a handful of recognisable organisations.
- **Your email address** is used only to receive the contribution. It is not
  stored with the data or published. Ask for your contribution to be removed at
  any time by writing to the same address.
- **The aggregate is published** as [`tools/benchmark.json`](https://github.com/p0jst/OpenCDC/blob/main/tools/benchmark.json)
  under CC BY 4.0, and recomputed as contributions arrive. The script that
  produces it, [`benchmark/aggregate.py`](https://github.com/p0jst/OpenCDC/blob/main/benchmark/aggregate.py),
  is public, so anyone can check how the figures are made.

## What others have measured

<p class="src" markdown><span class="src-tag guidance">Guidance</span>Other models and surveys, summarised. Their scales and questions differ from OCDF's; do not compare the numbers directly.</p>

Until OCDF's own groups fill up, two published sources give useful context:

- **SOC-CMM maturity report**, published yearly under CC BY-SA 4.0. The 2026
  edition is based on about 200 usable responses combined with anonymised
  assessments from SOC-CMM's partners, and gives average maturity on SOC-CMM's
  0–5 scale by region, sector, SOC size and domain. It also finds that
  self-assessments score higher than third-party assessments, the same caution
  that applies here. Its size bands are the size of the SOC team, not of the
  organisation, and most respondents are outside Europe.
  [SOC-CMM benchmark](https://www.soc-cmm.com/soc-benchmark)
- **ENISA NIS Investments 2025**, a survey of 1,080 organisations in NIS
  sectors across all 27 member states, 17% of them SMEs. It reports practices
  and spending rather than maturity levels. Among its findings: security staff
  make up 10.6% of IT staff, the lowest share it has recorded; the median
  organisation spends 9% of its IT budget on security; 30% had not carried out a
  cybersecurity assessment in the previous 12 months; and 28% take more than
  three months to patch critical vulnerabilities.
  [NIS Investments 2025](https://www.enisa.europa.eu/publications/nis-investments-2025)

*Open CDC Framework, licensed CC BY 4.0.*
