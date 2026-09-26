# National Annex — Spain

<!-- countries:begin -->
> **Status as of September 2026:** Pending, awaiting verification. Community-maintained orientation. This is **not legal advice**; verify against the official gazette and authority guidance before relying on it. Corrections welcome, see [contributing](../../CONTRIBUTING.md).

| Review | Status |
|--------|--------|
| Confidence | [Pending legislative change](README.md#confidence-levels) |
| Checked line by line against the legal text | No |
| Reviewed by a lawyer | No |
| Last reviewed | September 2026 |
| Reviewed by | Frederik B. Krogsgaard, maintainer |
| Second reviewer | **Wanted**, see [CONTRIBUTING](../../CONTRIBUTING.md) |
| Next review due | March 2027 |

## NIS2 implementation

| Field | Value |
|-------|-------|
| Implementing law | Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad, still in legislative process as of mid-2026; verify. The European Commission referred the country to the Court of Justice of the EU on 9 July 2026 for failing to transpose NIS2. |
| Competent authority | Expected: National Cybersecurity Centre coordination; CCN for the public sector, INCIBE for private entities and citizens, sector authorities |
| National CSIRT / reporting | CCN-CERT, INCIBE-CERT, ESPDEF-CERT |
| Official starting point | https://www.incibe.es |
<!-- countries:end -->

## Country notes for your CDC

Existing ENS (Esquema Nacional de Seguridad, RD 311/2022) already imposes NIST-like controls for public sector and suppliers. Comply with ENS now; it will carry most of the NIS2 weight.

## Standard checklist for all countries

- [ ] GOVERN: applicability determined per legal entity and sector, and recorded in the regulatory applicability register
- [ ] Entity registration completed with the national authority where required
- [ ] RESPOND: incident-reporting procedure drilled against the national channel and the 24 h early-warning clock
- [ ] Contact established with the national CSIRT *before* the first incident
- [ ] Data protection authority contact and GDPR Art. 33 flow prepared. This runs in parallel with NIS2 reporting
- [ ] National guidance and frameworks mapped to your control evidence, per the note above

## Selector tag

Tick "Spain" in `tools/regulatory-profile.html` to include this country's references under the `es-nat` tag.

*Open CDC Framework, licensed CC BY 4.0.*
