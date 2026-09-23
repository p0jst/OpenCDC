# 17 — EU Regulatory Landscape for CDC/SOC Teams

<p class="src" markdown><span class="src-tag law">Law</span>Paraphrased from the legal texts. Check the text itself and your national law; not legal advice.</p>

> ⚠️ **This is orientation, not legal advice.** Directives are transposed into national law with variations; always verify against your member state's implementation and consult legal counsel.

## The core instruments

### NIS2 — Directive (EU) 2022/2555
The horizontal cybersecurity law for the EU. Transposition deadline was **17 October 2024**; several member states transposed late, so check national status.

- **Scope, per Art. 2 and Annexes I–II:** *essential* and *important* entities across 18 sectors, covering energy, transport, health, digital infrastructure, ICT service management, public administration, manufacturing of critical products and more, generally medium-sized and above, with exceptions.
- **Key CDC-relevant obligations:**
  - Art. 20 covers management accountability and training.
  - Art. 21 sets minimum risk-management measures; the list in points (a)–(j) reads like a CDC capability checklist: risk analysis, incident handling, continuity/backup/DR, supply chain, secure development/acquisition, effectiveness assessment, hygiene & training, cryptography, HR/access control, MFA.
  - Art. 23 governs incident reporting: **early warning ≤ 24 h**, notification ≤ 72 h, final report ≤ 1 month, to the national CSIRT or competent authority.
- **Framework mapping:** every OCDF function document has an "EU regulatory hooks" section referencing the relevant NIS2 articles.

### GDPR — Regulation (EU) 2016/679
Applies to virtually every CDC because security operations process personal data, logs above all, and security incidents often involve personal data breaches.

- Art. 32 covers security of processing, the legal anchor for "appropriate measures", explicitly including the ability to ensure confidentiality, **integrity, availability and resilience**. The triad is in the law.
- Art. 33/34 cover 72-hour breach notification and data-subject communication.
- Art. 30 covers records of processing, reusable as data inventory input.
- **The CDC as data processor problem:** security monitoring processes employee personal data. Define legal basis, purpose limitation, retention and access for security telemetry, and involve your DPO when onboarding intrusive log sources such as endpoint telemetry and email content inspection.

### DORA — Regulation (EU) 2022/2554
Digital operational resilience for the **financial sector**, applicable since **17 January 2025**. Directly applicable regulation, with no transposition. ICT risk management in Art. 5–16, incident classification and reporting in Art. 17–23, resilience testing including threat-led penetration testing or TLPT in Art. 24–27, and ICT third-party risk in Art. 28–44.

### CRA — Cyber Resilience Act, Regulation (EU) 2024/2847
Security requirements for **products with digital elements** placed on the EU market; main obligations apply from **December 2027**, with vulnerability/incident reporting obligations for manufacturers starting earlier, in September 2026. CDC relevance: procurement leverage, and manufacturer reporting duties if your organisation ships digital products.

### CER — Directive (EU) 2022/2557
Resilience of critical entities, the physical, all-hazards counterpart of NIS2. Relevant for critical infrastructure operators' crisis-management interface.

### Cybersecurity Act — Regulation (EU) 2019/881
ENISA's permanent mandate and the EU cybersecurity certification framework, such as EUCC. Relevant for procurement and assurance.

## Key institutions for a CDC to know

| Institution | Why it matters to your CDC |
|-------------|----------------------------|
| **National CSIRTs** | Your NIS2 reporting counterpart; advisory feeds; incident support. Build the relationship *before* the incident. |
| **ENISA** | Threat landscape reports, good-practice guides, CSIRT maturity resources. |
| **CSIRTs Network & EU-CyCLONe** | EU-level operational and crisis cooperation networks, mostly of indirect relevance, via your national CSIRT. |
| **Data Protection Authority** | GDPR Art. 33 notifications; guidance on monitoring vs. privacy. |
| **Sector regulators** | National financial supervisors for DORA, for example. |

## Practical compliance pattern for a CDC

1. **Determine applicability** at GOVERN: which regimes apply, in which member states, for which legal entities. Output: a regulatory applicability register.
2. **Map obligations to capabilities**: use the "EU regulatory hooks" sections in docs 01–06 as a starting crosswalk.
3. **Prepare reporting machinery** at RESPOND: contact lists, report templates per regime, and drilled procedures. Deadlines are too short to improvise.
4. **Evidence continuously**: NIS2 Art. 21(2)(f) requires *assessing the effectiveness* of measures, and your maturity assessments and metrics, in the templates, are that evidence.

## Sources

- NIS2: Directive (EU) 2022/2555: https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- GDPR: Regulation (EU) 2016/679: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- DORA: Regulation (EU) 2022/2554: https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- CRA: Regulation (EU) 2024/2847: https://eur-lex.europa.eu/eli/reg/2024/2847/oj
- CER: Directive (EU) 2022/2557: https://eur-lex.europa.eu/eli/dir/2022/2557/oj
- **Cybersecurity Act**: Regulation (EU) 2019/881: https://eur-lex.europa.eu/eli/reg/2019/881/oj
- ENISA: https://www.enisa.europa.eu

*Open CDC Framework, licensed CC BY 4.0. Credits: [References & credits](19-references.md).*
