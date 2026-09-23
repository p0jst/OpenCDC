# PB-IDC — Incident Response: Identity Compromise

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span><span class="src-tag standard">Standard</span>Response practice from experience; evidence handling follows RFC 3227 and NIST SP 800-86.</p>

> **Status: draft.** Attack-based playbook, published for field review. Tailor it to your identity platform and authority matrix before relying on it, and send corrections via [contributing](../CONTRIBUTING.md).
> **Scope:** A user, administrator or service identity is suspected to be in adversary hands: password spray or stuffing success, MFA fatigue or adversary-in-the-middle phishing, token theft, malicious OAuth consent, or anomalous sign-ins. Related capabilities: PR-1, DE-3, RS-2, RS-4. Examples use Microsoft Entra ID and Active Directory because they are the most common; the steps apply to any identity provider.
> **Legal note:** Sign-in and mailbox data are personal data. Follow your monitoring legal basis under GDPR and involve the DPO where the investigation reaches mailbox content. <!-- law:gdpr -->

## 0. Prerequisites — build these BEFORE the incident

- [ ] Identity logs onboarded to the SIEM with retention beyond the platform default: sign-in logs, directory audit logs, and the cloud audit log. Platform retention can be as short as 7 to 30 days depending on licence, which is often shorter than the time to detection
- [ ] Containment authority for CON-07 (disable account) and CON-08 (revoke sessions) pre-agreed per charter §4, including for privileged and executive accounts
- [ ] A break-glass account that is excluded from the controls you will tighten, monitored, and tested
- [ ] A list of who can reset privileged accounts, and from which clean admin workstations
- [ ] Known-good baselines: conditional access policies, federation trusts, privileged role membership, app registrations and service principals with credentials

## 1. Triage

1. Establish what the adversary has: a password only, a session or refresh token, a registered MFA method, or an application consent. The containment differs for each.
2. Check the identity's privilege. **Any privileged role, or access to identity infrastructure, raises the incident to major**: treat the tenant or domain as potentially compromised and follow [the first hour of a major incident](../docs/respond.md).
3. Scope from the sign-in logs: source IPs, user agents, devices, locations and the first anomalous sign-in. Pivot on those indicators across all identities, because spray and phishing campaigns rarely stop at one account.
4. Classify severity per the IR plan; open the incident record and timeline.

## 2. Containment — order matters

1. **Block sign-in first** (CON-07). Disable the account or block sign-in in the identity provider. This stops new authentication with the stolen password.
2. **Then revoke sessions and refresh tokens immediately** (CON-08). Revoking first while the account is still enabled lets an adversary who holds the password sign straight back in and receive fresh tokens. Access tokens already issued can remain valid until they expire, typically up to an hour unless continuous access evaluation is supported, so keep the account blocked through that window.
3. **Remove adversary persistence in the identity**: MFA methods registered during the compromise window, OAuth app consents granted by the user, app passwords, and new devices joined or registered.
4. **Reset the password from a clean device**, and only then re-enable the account with fresh MFA registration verified out of band, for example in person or by a call to a known number.
5. For **on-premises AD**, disable the account and reset the password twice, allowing replication between resets, where Kerberos ticket reuse is suspected. For privileged or `krbtgt`-level compromise, move to [PB-WSV](PB-WSV-windows-server.md).
6. For **service accounts and workload identities**, rotate the secret or certificate (CON-10) in coordination with the service owner, and review what the identity accessed.

## 3. Evidence acquisition

> Export before retention rolls off. Identity evidence lives in the platform, not on a disk, and it expires on a schedule.

| # | Evidence | Notes |
|---|----------|-------|
| 1 | **Sign-in logs**, interactive and non-interactive, for the account and for the adversary IPs | Non-interactive sign-ins show token replay; they are often not exported by default |
| 2 | **Directory audit logs** | MFA method changes, role assignments, app consents, conditional access and federation changes |
| 3 | **Cloud audit log** for mail, file and collaboration activity | What the identity did with its access: mailbox rules, file downloads, sharing links |
| 4 | **Endpoint evidence** from the user's device | Token theft often starts on the endpoint; use [PB-W11](PB-W11-windows11-laptop.md) or [PB-MAC](PB-MAC-macos-laptop.md) |

## 4. Analysis pointers

- Look for what the adversary set up to come back: mailbox forwarding and inbox rules, new app registrations or service principal credentials, federation or domain changes, conditional access exclusions, and added role members.
- Establish data access during the compromise window. This determines GDPR and NIS2 reporting. <!-- law:gdpr --><!-- law:nis2 -->
- Map to MITRE ATT&CK (Valid Accounts, Steal Application Access Token, Modify Authentication Process) and feed detections back via the use case template.

## 5. Eradication & recovery

- Remove every persistence item found in §4, then re-verify against the baselines from §0.
- Re-enable the account only after a clean device, fresh credentials and out-of-band MFA registration.
- Close the entry path: the phishing kit's domains, the legacy protocol that allowed spray, or the missing conditional access policy.
- Closure criteria: no sign-ins from adversary infrastructure for [14] days across the tenant; lessons-learned filed.

## 6. Reporting hooks

- Personal data accessed → DPO breach assessment under GDPR Art. 33, on a 72 h clock from awareness. <!-- law:gdpr -->
- Significant incident at organisational level → NIS2 early warning ≤ 24 h to the national CSIRT. <!-- law:nis2 -->
- Financial entities: DORA classification and Art. 19 timelines. <!-- law:dora -->

## Sources

- Microsoft incident response playbooks: password spray, token theft, app consent grant. https://learn.microsoft.com/security/operations/incident-response-playbooks
- NIST SP 800-61r3, *Incident Response Recommendations and Considerations for Cybersecurity Risk Management*.
- MITRE ATT&CK, Enterprise matrix: Credential Access and Persistence tactics. https://attack.mitre.org

*Open CDC Framework, licensed CC BY 4.0.*
