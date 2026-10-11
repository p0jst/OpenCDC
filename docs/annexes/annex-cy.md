# National Annex — Cyprus

<!-- countries:begin -->
> **Status as of October 2026:** In force. Community-maintained orientation. This is **not legal advice**; verify against the official gazette and authority guidance before relying on it. Corrections welcome, see [contributing](../../CONTRIBUTING.md).

| Review | Status |
|--------|--------|
| Confidence | [Maintainer reviewed](README.md#confidence-levels) |
| Checked line by line against the legal text | No |
| Reviewed by a lawyer | No |
| Last reviewed | October 2026 |
| Reviewed by | Frederik B. Krogsgaard, maintainer |
| Second reviewer | **Wanted**, see [CONTRIBUTING](../../CONTRIBUTING.md) |
| Next review due | April 2027 |

## NIS2 implementation

| Field | Value |
|-------|-------|
| Implementing law | Security of Networks and Information Systems (Amendment) Law of 2025, N. 60(I)/2025, amending Law 89(I)/2020 to transpose NIS2, in force 25 April 2025 |
| Competent authority | Digital Security Authority (DSA / Αρχή Ψηφιακής Ασφάλειας) |
| National CSIRT / reporting | CSIRT-CY, part of the DSA |
| Official starting point | https://dsa.cy |
<!-- countries:end -->

## Country notes for your CDC

Cyprus is stricter than the directive on reporting. The early warning is due within 6 hours, not 24, and the final report within 15 days of restoring the affected system, not one month; while an incident is still open, a progress report is due every 15 days. If a Cypriot entity is in scope, build the 6-hour clock into the IR plan and the on-call runbook rather than relying on the EU default. The DSA is both the competent authority and the national CSIRT.

## Standard checklist for all countries

- [ ] GOVERN: applicability determined per legal entity and sector, and recorded in the regulatory applicability register
- [ ] Entity registration completed with the national authority where required
- [ ] RESPOND: incident-reporting procedure drilled against the national channel and Cyprus's 6 h early-warning clock
- [ ] Contact established with the national CSIRT *before* the first incident
- [ ] Data protection authority contact and GDPR Art. 33 flow prepared. This runs in parallel with NIS2 reporting
- [ ] National guidance and frameworks mapped to your control evidence, per the note above

## Selector tag

Tick "Cyprus" in `tools/regulatory-profile.html` to include this country's references under the `cy-nat` tag.

*Open CDC Framework, licensed CC BY 4.0.*
