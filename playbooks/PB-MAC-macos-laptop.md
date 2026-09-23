# PB-MAC — Incident Response & Digital Forensics: macOS Laptop

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span><span class="src-tag standard">Standard</span>Response practice from experience; evidence handling follows RFC 3227 and NIST SP 800-86.</p>

> **Scope:** Suspected compromise of a corporate macOS laptop on Apple Silicon or Intel. Related capabilities: RS-2, RS-3, DE-3.
> **Legal note:** Employee personal data considerations apply as on Windows: legal basis, DPO involvement, chain of custody. <!-- law:gdpr -->

## 0. Prerequisites

- [ ] MDM enrolment with remote lock and isolate, required for many response actions on modern macOS
- [ ] EDR with macOS live-response support
- [ ] **FileVault recovery keys escrowed in MDM**, same rule as BitLocker: no key, no dead-box analysis
- [ ] A dedicated analysis Mac, since target disk and share mode acquisition require Apple hardware
- [ ] Volume-owner and admin credentials strategy documented, as Apple Silicon requires volume owner auth for some operations

## 1. Platform realities to internalise before responding

- **Apple Silicon changes forensics.** Traditional full memory acquisition is effectively unavailable on Apple Silicon without specialised solutions; prioritise **live collection via EDR** and treat the unified logs + cloud telemetry as your primary record.
- **System Integrity Protection, SIP,** limits what even root can touch. That is good for evidence integrity and limiting for some tools.
- **TCC**, the privacy consent database, governs what your collection tooling may access. Pre-approve your forensic and EDR tools via MDM PPPC profiles *in advance* or collection will silently fail.
- **Sealed system volume:** the OS volume is cryptographically sealed; malware lives in the Data volume, LaunchAgents/Daemons, and user context, so scope collection accordingly.

## 2. Triage — remote first

1. Pull EDR telemetry, IdP sign-ins, MDM device record, and unified log excerpts remotely.
2. Check XProtect/Gatekeeper/quarantine events for the suspicious file's provenance.
3. Classify severity; choose evidence-priority vs containment-priority fork.

## 3. Containment

- EDR network isolation preferred; otherwise MDM-based network restriction or physical disconnect.
- **Do not power off** if live collection is still possible. Volatile data and decrypted FileVault state are lost with it.
- Block the user's sign-in, then revoke their cloud sessions and tokens immediately; rotate credentials from a clean device. Revoking while the account is still enabled lets a password holder sign straight back in.
- If the device may be remotely wiped by the adversary, as in a stolen Apple ID or MDM compromise, isolate from network *and* record MDM/Apple ID state immediately.

## 4. Evidence acquisition — order of volatility

| # | Evidence | How | macOS notes |
|---|----------|-----|-------------|
| 1 | Volatile state | EDR live response: processes, connections, launchd jobs, kexts/system extensions, logged-in users | Prefer scripted collection to interactive use. |
| 2 | **Unified logs** | `log collect`, which creates a `.logarchive` | The single richest macOS source; collect early, because it rolls over. |
| 3 | Targeted triage collection | Collect the key artefact paths listed below, with hashing | Faster and often sufficient vs full image. |
| 4 | Disk image | Image the **Data volume** while unlocked, or full APFS acquisition on an analysis Mac in target or share mode | FileVault: unlocked-state acquisition or escrowed key required. APFS snapshots can preserve pre-incident state, so check `tmutil listlocalsnapshots /`. |
| 5 | Cloud artefacts | IdP logs, MDM record, iCloud/Drive/SaaS audit as applicable | Survives device wipe. |

**Key macOS artefacts:**

- **Persistence**: `/Library/LaunchDaemons`, `/Library/LaunchAgents`, `~/Library/LaunchAgents`, login items in `BackgroundItems-v*.btm`, configuration profiles, cron/periodic
- **Execution & provenance**: the quarantine database `com.apple.LaunchServices.QuarantineEventsV2`, Gatekeeper/XProtect logs, `ExecPolicy`/CoreAnalytics
- **User activity**: `KnowledgeC.db`, Spotlight shortcuts, shell history in `~/.zsh_history`, Recent items, browser data
- **Filesystem**: FSEvents in `/System/Volumes/Data/.fseventsd`, APFS snapshots
- **Security state**: TCC.db for what had which permissions, sudo log entries in unified log

## 5. Analysis pointers

- Reconstruct provenance: quarantine db → what was downloaded from where; unified log → what executed with what parent.
- Verify persistence exhaustively, as macOS malware overwhelmingly lives in launchd items and profiles.
- Map to the ATT&CK macOS matrix; feed indicators to DETECT.

## 6. Eradication & recovery

- Confirmed compromise → **erase and reprovision** with Erase All Content and Settings followed by MDM re-enrolment; don't hand-clean.
- Rotate credentials, tokens, and certificates present on the device; review the user's OAuth grants.
- Verify restored device: clean EDR baseline, expected profiles only, TCC grants reviewed.

## 7. Reporting hooks

- GDPR Art. 33/34 assessment via DPO where personal data affected. <!-- law:gdpr -->
- NIS2 Art. 23 timelines if organisationally significant. <!-- law:nis2 -->
- DORA Art. 19 for financial entities. <!-- law:dora -->

## Non-normative open source tooling examples

Triage/collection: Velociraptor, osquery, Aftermath-class collectors, the built-in `log collect` · Analysis: mac_apt, APOLLO for pattern-of-life from KnowledgeC, Sleuth Kit/Autopsy for APFS.

## Sources
- NIST SP 800-86; RFC 3227; NIST SP 800-61r3.
- Apple Platform Security Guide, covering FileVault, SIP, the sealed volume and Gatekeeper. https://support.apple.com/guide/security/

*Open CDC Framework, licensed CC BY 4.0.*
