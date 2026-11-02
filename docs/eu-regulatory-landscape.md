# EU regulatory landscape for CDC and SOC teams

<p class="src" markdown><span class="src-tag law">Law</span>Paraphrased from the legal texts. Check the text itself and your national law; not legal advice.</p>

> ⚠️ **This is orientation, not legal advice.** Directives are transposed into national law with variations; always verify against your member state's implementation and consult legal counsel.

## The core instruments

### NIS2: Directive (EU) 2022/2555
The horizontal cybersecurity law for the EU. Transposition deadline was 17 October 2024; several member states transposed late, so check national status.

- **Scope, per Art. 2 and Annexes I–II:** *essential* and *important* entities across 18 sectors, covering energy, transport, health, digital infrastructure, ICT service management, public administration, manufacturing of critical products and more, generally medium-sized and above, with exceptions.
- **Key CDC-relevant obligations:**
    - Art. 20 covers management accountability and training.
    - Art. 21 sets minimum risk-management measures; the list in points (a)–(j) reads like a CDC capability checklist: risk analysis, incident handling, continuity/backup/DR, supply chain, secure development/acquisition, effectiveness assessment, hygiene & training, cryptography, HR/access control, MFA.
    - Art. 23 governs incident reporting: early warning ≤ 24 h, notification ≤ 72 h, final report ≤ 1 month, to the national CSIRT or competent authority.
- **Framework mapping:** every OCDF function document has an "EU regulatory hooks" section referencing the relevant NIS2 articles.
- **Changes proposed, not yet law:** on 20 January 2026 the Commission proposed targeted NIS2 amendments, COM(2026) 13, on scope, a new small mid-cap category, ransomware reporting and cross-border supervision. Separately, the Digital Omnibus of November 2025, COM(2025) 837, proposes a single entry point at ENISA for incident reports under NIS2, GDPR, DORA, eIDAS and CER. It would also change GDPR breach notification to the authority: only breaches likely to be high risk, within 96 hours instead of 72. As of October 2026 both proposals are still being negotiated. Today's rules apply in full until amendments are adopted and, for NIS2, transposed, so keep the 72-hour GDPR clock and build reporting on today's national channels, not on a single entry point that does not yet exist.

### GDPR: Regulation (EU) 2016/679
Applies to virtually every CDC because security operations process personal data, logs above all, and security incidents often involve personal data breaches.

- Art. 32 covers security of processing, the legal anchor for "appropriate measures", explicitly including the ability to ensure confidentiality, integrity, availability and resilience. The triad is in the law.
- Art. 33/34 cover 72-hour breach notification and data-subject communication.
- Art. 30 covers records of processing, reusable as data inventory input.
- **The CDC as data processor problem:** security monitoring processes employee personal data. Define legal basis, purpose limitation, retention and access for security telemetry, and involve your DPO when onboarding intrusive log sources such as endpoint telemetry and email content inspection.

### DORA: Regulation (EU) 2022/2554
Digital operational resilience for the financial sector, applicable since 17 January 2025. Directly applicable regulation, with no transposition. ICT risk management in Art. 5–16, incident classification and reporting in Art. 17–23, resilience testing including threat-led penetration testing or TLPT in Art. 24–27, and ICT third-party risk in Art. 28–44.

### CRA: Cyber Resilience Act, Regulation (EU) 2024/2847
Security requirements for products with digital elements placed on the EU market; main obligations apply from 11 December 2027, and the manufacturers' duty to report actively exploited vulnerabilities and severe incidents has applied since 11 September 2026. CDC relevance: procurement leverage, and manufacturer reporting duties if your organisation ships digital products.

### CER: Directive (EU) 2022/2557
Resilience of critical entities, the physical, all-hazards counterpart of NIS2. Relevant for critical infrastructure operators' crisis-management interface.

### AI Act: Regulation (EU) 2024/1689
Rules for AI systems placed on the market or used in the EU, amended by the Digital Omnibus on AI, Regulation (EU) 2026/1744. AI literacy under Art. 4 and the prohibited practices under Art. 5 have applied since 2 February 2025; the obligations for high-risk systems listed in Annex III apply from 2 December 2027. CDC relevance: a CDC using AI tools is normally a deployer; emotion recognition in the workplace is prohibited; AI that monitors and evaluates the behaviour of people at work is listed as high-risk, and whether employee behaviour analytics for security falls under that listing is not settled. See [AI in the CDC](ai-in-the-cdc.md#what-the-law-says).

### Cybersecurity Act: Regulation (EU) 2019/881
ENISA's permanent mandate and the EU cybersecurity certification framework, such as EUCC. Relevant for procurement and assurance. A revision, COM(2026) 11, was proposed in January 2026 and is under negotiation.

## Key institutions for a CDC to know

| Institution | Why it matters to your CDC |
|-------------|----------------------------|
| **National CSIRTs** | Your NIS2 reporting counterpart; advisory feeds; incident support. Build the relationship *before* the incident. |
| **ENISA** | Threat landscape reports, good-practice guides, CSIRT maturity resources. |
| **CSIRTs Network & EU-CyCLONe** | EU-level operational and crisis cooperation networks, mostly of indirect relevance, via your national CSIRT. |
| **Data Protection Authority** | GDPR Art. 33 notifications; guidance on monitoring vs. privacy. |
| **Sector regulators** | National financial supervisors for DORA, for example. |

## Practical compliance pattern for a CDC

1. **Determine applicability at GOVERN.** Which regimes apply, in which member states, for which legal entities. Output: a regulatory applicability register.
2. **Map obligations to capabilities.** Use the [NIS2 Article 21 crosswalk](nis2-article-21-crosswalk.md) and the "EU regulatory hooks" section in each function document.
3. **Prepare reporting machinery at RESPOND.** Contact lists, report templates per regime, and drilled procedures. Deadlines are too short to improvise.
4. **Evidence continuously.** NIS2 Art. 21(2)(f) requires *assessing the effectiveness* of measures, and your maturity assessments and metrics, in the templates, are that evidence.

## Sources

- NIS2: Directive (EU) 2022/2555: https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- GDPR: Regulation (EU) 2016/679: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- DORA: Regulation (EU) 2022/2554: https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- CRA: Regulation (EU) 2024/2847: https://eur-lex.europa.eu/eli/reg/2024/2847/oj
- CER: Directive (EU) 2022/2557: https://eur-lex.europa.eu/eli/dir/2022/2557/oj
- AI Act: Regulation (EU) 2024/1689: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Digital Omnibus on AI: Regulation (EU) 2026/1744: https://eur-lex.europa.eu/eli/reg/2026/1744/oj
- **Cybersecurity Act**: Regulation (EU) 2019/881: https://eur-lex.europa.eu/eli/reg/2019/881/oj
- ENISA: https://www.enisa.europa.eu
- European Commission, NIS2 targeted amendments COM(2026) 13 and revised Cybersecurity Act COM(2026) 11, 20 January 2026. https://digital-strategy.ec.europa.eu/en/policies/cybersecurity-act
- ENISA, *NIS2 Technical Implementation Guidance* on Implementing Regulation (EU) 2024/2690, June 2025, with evidence examples and a mapping table. https://www.enisa.europa.eu/publications/nis2-technical-implementation-guidance

*Open CDC Framework, licensed CC BY 4.0. Credits: [References & credits](references.md).*
