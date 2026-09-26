# National Annex — Denmark

<!-- countries:begin -->
> **Status as of September 2026:** In force. Community-maintained orientation, the reference annex for the framework. This is **not legal advice**; verify against retsinformation.dk and samsik.dk before relying on it. Corrections welcome, see [contributing](../../CONTRIBUTING.md).

| Review | Status |
|--------|--------|
| Confidence | [Maintainer reviewed](README.md#confidence-levels) |
| Checked line by line against the legal text | No |
| Reviewed by a lawyer | No |
| Last reviewed | September 2026 |
| Reviewed by | Frederik B. Krogsgaard, maintainer |
| Second reviewer | **Wanted**, see [CONTRIBUTING](../../CONTRIBUTING.md) |
| Next review due | March 2027 |
<!-- countries:end -->

## The Danish implementation landscape

Denmark implemented NIS2 and CER through a **family of laws** in force since 2025, rather than a single act:

| Law | Covers | In force | Selector tag |
|-----|--------|----------|--------------|
| **NIS 2-loven**: Lov nr. 434 af 6. maj 2025, *Lov om foranstaltninger til sikring af et højt cybersikkerhedsniveau* | Horizontal NIS2 implementation for most sectors | 1 July 2025 | `dk-nis2` |
| **Lov om styrket beredskab i energisektoren**: Lov nr. 258 af 6. marts 2025, detailed in *bekendtgørelse om modstandsdygtighed og beredskab i energisektoren*, BEK nr. 260/2025 | Energy sector. Combines the cyber side of NIS2 and the physical side of CER into one regime, supervised by Energistyrelsen. Requirements scale with five preparedness levels and go beyond the EU minimum at the top levels | 7 March 2025 | `dk-energi` |
| **Lov om sikkerhed og beredskab i telesektoren**, L142 | Telecom sector NIS2 implementation | 1 July 2025 | `dk-tele` |
| **CER-loven**, *lov om kritiske enheders modstandsdygtighed* | Physical resilience of critical entities across ~11 sectors | 1 July 2025 | `dk-cer` |
| **Lov om finansiel virksomhed § 333 et seq.** | Financial sector, aligned with DORA | — | `dk-fin` |

> Note on naming: "Lov om styrket beredskab" in Danish practice usually refers to the **energy-sector** act above; the NIS 2-loven and CER-loven are separate acts. If your organisation spans sectors, several regimes can apply simultaneously. The NIS 2-loven explicitly yields to the energy, tele and financial acts for entities they cover, per § 1, stk. 2.

## Key Danish specifics for your CDC

1. **Registration duty:** entities covered by the NIS 2-loven must register on **virk.dk**. The initial deadline was 1 October 2025, and new entities register when they come into scope.
2. **Incident reporting channel:** entities under the NIS 2-loven and the tele act report significant incidents via **virk.dk**; the national CSIRT function is performed by **Center for Cybersikkerhed (CFCS)**, which has been part of **Styrelsen for Samfundssikkerhed (SAMSIK)** since January 2025. Energy-sector entities report to **Energistyrelsen** instead. Timelines follow the NIS2 pattern in both channels: early warning ≤ 24 h, notification or status ≤ 72 h, final report ≤ 1 month.
3. **Authorities to know:**
   - **Styrelsen for Samfundssikkerhed (SAMSIK)** — overall coordination and cross-sector guidance, incorporating CFCS for technical advisory and incident reception, at samsik.dk/nis2
   - **Sector-responsible authorities** supervise their own sectors: Digitaliseringsstyrelsen for digital sectors, Energistyrelsen for energy, Finanstilsynet for finance, Trafikstyrelsen for transport
4. **Guidance materials:** SAMSIK publishes cross-cutting NIS2 vejledninger structuring measures as *skal* meaning must, *bør* meaning should with deviations justified, and *kan* meaning may. That is a useful evidence structure for your maturity assessments; map OCDF capability evidence to the skal and bør items.
5. **Energy-sector extras** under Lov om styrket beredskab i energisektoren. Each entity is placed on one of five preparedness levels, set by the category of its installations, and the requirements scale with the level. As summarised from BEK 260: real-time monitoring at level 5, the largest installations and transmission operators; IT/OT network segmentation at levels 4 and 5; annual exercises at levels 3 to 5; security clearance for key personnel at the highest levels; and at levels 4 and 5 a preparedness and cyber coordinator who is separate from the management approving the plans. Supervision runs yearly at levels 4 and 5 and less often below. Confirm your level with Energistyrelsen, then set DETECT and GOVERN targets to match: Level 3–4 at the top levels, the ordinary targets below them.

## CDC checklist for Denmark

- [ ] GOVERN: applicability determined per legal entity and sector, NIS 2-loven versus the sector acts, and recorded in the regulatory applicability register
- [ ] Registered on virk.dk where required
- [ ] Reporting procedure drilled against the right channel, virk.dk or Energistyrelsen, with the 24 h early-warning clock
- [ ] Energy sector: preparedness level confirmed with Energistyrelsen and the level's requirements mapped to your targets
- [ ] Sector authority contact list maintained; relationship established with SAMSIK before an incident
- [ ] Datatilsynet contact and GDPR Art. 33 flow prepared. This runs in parallel with NIS2 reporting
- [ ] SAMSIK vejledninger mapped to your control evidence across skal, bør and kan

## Sources

- Lov nr. 434 af 6. maj 2025, the NIS 2-loven: https://www.retsinformation.dk/eli/lta/2025/434
- Lov nr. 258 af 6. marts 2025, lov om styrket beredskab i energisektoren: https://www.retsinformation.dk/eli/lta/2025/258
- Energistyrelsen, lov om styrket beredskab i energisektoren: https://ens.dk/forsyning-og-forbrug/lov-om-styrket-beredskab-i-energisektoren
- Styrelsen for Samfundssikkerhed, CFCS part of SAMSIK: https://samsik.dk/artikler/2025/03/center-for-cybersikkerhed-er-en-del-af-styrelsen-for-samfundssikkerhed/
- Styrelsen for Samfundssikkerhed, NIS2 guidance: https://samsik.dk/nis2
- Digitaliseringsstyrelsen NIS2 news on the 1 July 2025 entry into force: https://digst.dk
- NIS2-tjek self-assessment: https://nis2tjek.sikkerdigital.dk

*Open CDC Framework, licensed CC BY 4.0. Contributions correcting or extending this annex are welcome.*
