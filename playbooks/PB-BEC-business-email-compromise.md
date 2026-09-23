# PB-BEC — Incident Response: Business Email Compromise

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span><span class="src-tag standard">Standard</span>Response practice from experience; evidence handling follows RFC 3227 and NIST SP 800-86.</p>

> **Status: draft.** Attack-based playbook, published for field review. Tailor it to your mail platform, finance processes and authority matrix before relying on it, and send corrections via [contributing](../CONTRIBUTING.md).
> **Scope:** A mailbox is compromised, or impersonated, to redirect payments, request data or phish onward: invoice and payment-redirection fraud, CEO fraud, supplier account takeover, and internal phishing from a trusted sender. Related capabilities: PR-9, DE-3, RS-2, RS-5. For the underlying account takeover, run [PB-IDC](PB-IDC-identity-compromise.md) alongside this playbook.
> **Legal note:** Mailbox content is personal data, often about third parties. Involve the DPO before reviewing message content and keep the review to what the investigation needs. <!-- law:gdpr -->

## 0. Prerequisites — build these BEFORE the incident

- [ ] A **payment-fraud hotline**: the bank's fraud and recall contact for each account the organisation pays from, known to finance and to the CDC. Recall success drops sharply within hours
- [ ] A finance rule that bank-detail changes are verified by calling a number already on file, never one in the email
- [ ] Mail audit logging enabled with retention beyond default, including mailbox item access where your platform supports it
- [ ] Authority to block senders and purge messages tenant-wide (CON-09) pre-agreed per charter §4
- [ ] DMARC, SPF and DKIM on your own domains, with DMARC reports reviewed

## 1. Triage — money first

1. **Has money moved, or is a payment about to?** If yes, finance calls the bank's fraud line **now** to stop or recall it, before any technical step. Then report to the police, because many banks require a police reference for recall.
2. Determine the variant: your mailbox compromised, a supplier's mailbox compromised, or a look-alike domain with no compromise at all. Header analysis and sign-in logs answer this.
3. Identify every recipient of the fraudulent thread, internal and external.

## 2. Containment

1. For a **compromised internal mailbox**: contain the identity per [PB-IDC](PB-IDC-identity-compromise.md). Block sign-in first, then revoke sessions immediately.
2. **Remove the adversary's mail persistence**: inbox rules that hide, move or delete replies; external forwarding; delegates added; and connected apps with mail permissions.
3. **Purge and block** (CON-09): remove the fraudulent and onward-phishing messages from all mailboxes, and block the sender and any look-alike domains.
4. **Warn the other side.** Tell affected customers and suppliers through a verified channel, not by replying to the thread, that messages from the period may be fraudulent.
5. For a **compromised supplier**: stop payments to changed bank details and inform the supplier through a known contact. Their incident is theirs to run; your exposure is the payments.

## 3. Evidence acquisition

| # | Evidence | Notes |
|---|----------|-------|
| 1 | **The fraudulent messages with full headers**, exported in original format | Headers establish whether the sender was compromised or spoofed |
| 2 | **Mailbox audit log**: rule creation, forwarding changes, items accessed and sent | Shows what the adversary read, which drives the data-breach assessment |
| 3 | **Sign-in and directory audit logs** | See [PB-IDC](PB-IDC-identity-compromise.md) §3 |
| 4 | **Payment records** and bank correspondence | Needed for the police report, the insurer and any recall |

## 4. Analysis pointers

- Reconstruct the timeline from first access to the fraudulent request. Adversaries often read a mailbox for weeks to learn payment cycles and tone.
- Establish which messages and attachments were accessed: contracts, invoices and personal data of customers or employees.
- Check for onward phishing from the compromised mailbox to your customers and suppliers. It turns your incident into theirs.

## 5. Eradication & recovery

- Confirm all mail persistence is removed and the identity is clean per PB-IDC.
- Review and correct any bank details changed in the finance system during the compromise window.
- Close the entry path: MFA gaps, legacy protocols, or the missing external-sender tag.
- Closure criteria: no adversary access for [14] days; all affected counterparties informed; lessons-learned filed.

## 6. Reporting hooks

- Payment fraud → police report and bank fraud process, in parallel with the investigation.
- Personal data accessed → DPO breach assessment under GDPR Art. 33, on a 72 h clock from awareness. <!-- law:gdpr -->
- Significant incident at organisational level → NIS2 early warning ≤ 24 h to the national CSIRT. <!-- law:nis2 -->
- Financial entities: DORA classification and Art. 19 timelines. <!-- law:dora -->
- Cyber insurance: notify within the policy window; see [counsel and insurance](../docs/respond.md).

## Sources

- Microsoft incident response playbooks: phishing investigation and compromised mailbox. https://learn.microsoft.com/security/operations/incident-response-playbooks
- Europol, public guidance on CEO fraud and invoice fraud. https://www.europol.europa.eu
- NIST SP 800-61r3.

*Open CDC Framework, licensed CC BY 4.0.*
