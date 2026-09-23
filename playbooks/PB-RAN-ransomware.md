# PB-RAN — Incident Response: Ransomware

> **Status: draft.** Attack-based playbook, published for field review. Tailor it to your estate, backup architecture and authority matrix before relying on it, and send corrections via CONTRIBUTING.md.
> **Scope:** Encryption in progress or discovered, a ransom note, or high-confidence precursors such as backup deletion, mass credential dumping or security tooling being disabled. Enterprise IT only: for anything touching OT, operations decides containment; see [ABOUT](../ABOUT.md). Related capabilities: RS-1 to RS-6, RC-1 to RC-3.
> **Legal note:** Assume data was exfiltrated before encryption until you can show otherwise. Most current ransomware operations steal first. <!-- law:gdpr -->

## 0. Prerequisites — build these BEFORE the incident

- [ ] Estate-level containment actions CON-11 to CON-15 pre-authorised per charter §4, and drilled
- [ ] Backups that the domain's administrators cannot delete: offline, immutable or in a separate security domain, with restore tested in the last [six] months
- [ ] An out-of-band communication channel that does not depend on the corporate identity, mail or chat platform
- [ ] DFIR retainer, external counsel and insurer contacts in the IR plan, with the insurer's panel requirements known
- [ ] A recovery order for critical services, agreed with the business in advance and linked to RC-1

## 1. Triage — the first hour

Run [the first hour of a major incident](../docs/05-respond.md) in parallel with triage. In short:

1. **Do not power systems off.** Isolate instead (CON-05, CON-06).
2. **Cut external connectivity and remote access** for affected sites (CON-11, CON-12). Encryption and exfiltration both need the network.
3. **Protect the backups** (CON-13), after confirming recent restore points are readable.
4. **Freeze snapshots** (CON-14) and **start emergency log collection** (CON-15) where there is no central logging.
5. **Move to the out-of-band channel.** Assume the adversary can read corporate mail and chat.
6. **Engage counsel and the insurer** before engaging your own responders if the policy requires its panel.

Then establish scope: which systems are encrypted, which are still spreading, and the ransomware family from the note and file extensions. Family identification tells you whether a free decryptor exists and what the group usually does next.

## 2. Containment

- **Assume the identity plane is compromised.** Ransomware at scale almost always means domain administrator access. Contain per [PB-WSV](PB-WSV-windows-server.md): suspect Tier 0, plan the double `krbtgt` reset, and rotate privileged and service-account credentials from clean admin workstations.
- Block the deployment mechanism: the GPO, scheduled task, remote-management tool or software-distribution job used to push the payload.
- Block known C2 and exfiltration destinations (CON-01 to CON-03), and hunt for them fleet-wide.
- Contain the cloud side too: synchronised identities, cloud backups and SaaS admin accounts reachable with the stolen credentials.

## 3. Evidence acquisition

| # | Evidence | Notes |
|---|----------|-------|
| 1 | **Memory from systems still running**, especially recently infected ones | Encryption keys have occasionally been recovered from memory; capture before any reboot |
| 2 | **A sample of encrypted files and the ransom note** | Needed for family identification and any decryptor |
| 3 | **Domain controller and identity evidence** | See [PB-WSV](PB-WSV-windows-server.md) §3 |
| 4 | **Firewall, proxy and DNS logs** covering the weeks before encryption | The exfiltration usually happened days earlier |
| 5 | **Backup platform logs** | Shows whether and when the adversary reached the backups |

## 4. Analysis pointers

- Find patient zero and the initial access: phishing, an exposed remote-access service, a vulnerable edge device, or stolen credentials. Encryption is the end of the attack, not the start.
- Establish whether and what data left the estate. Leak-site monitoring is useful but not proof; your own egress logs are.
- Map the attack to MITRE ATT&CK and feed the gaps back to DETECT. The precursors were almost always visible.

## 5. Eradication & recovery

- **Recover identity first**: a trusted domain or forest (execute the forest-recovery plan if cleaning is not credible), then infrastructure, then services in the agreed order.
- Restore from backups that pre-date the intrusion, not only the encryption. Scan restored systems before reconnecting them.
- "Integrity before Availability": do not reconnect a restored segment until its identity and management plane are trusted. See [Recover](../docs/06-recover.md).
- **Ransom payment** is a business and legal decision, not a CDC one. Check sanctions exposure with counsel and inform law enforcement. Payment does not remove the need to rebuild, because it does not remove the adversary's access.
- Closure criteria: no adversary activity for [30] days after recovery; initial access closed; lessons-learned filed.

## 6. Reporting hooks

- Significant incident → NIS2 early warning ≤ 24 h to the national CSIRT, notification ≤ 72 h and final report ≤ 1 month. Most ransomware incidents meet the threshold. <!-- law:nis2 -->
- Personal data encrypted or exfiltrated → GDPR Art. 33 within 72 h of awareness; Art. 34 to individuals where the risk is high. Loss of availability alone can be a personal data breach. <!-- law:gdpr -->
- Financial entities: DORA classification and Art. 19 timelines. <!-- law:dora -->
- Law enforcement: report to the national police cybercrime unit. Your national annex lists the contacts.

## Sources

- CISA and partners, *#StopRansomware Guide*. https://www.cisa.gov/stopransomware
- No More Ransom, decryptor collection by Europol and partners. https://www.nomoreransom.org
- ENISA, *Threat Landscape for Ransomware Attacks*. https://www.enisa.europa.eu
- NIST SP 800-61r3; NIST IR 8374, *Ransomware Risk Management*.

*Open CDC Framework, licensed CC BY 4.0.*
