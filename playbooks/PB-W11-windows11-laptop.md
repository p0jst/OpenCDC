# PB-W11 — Incident Response & Digital Forensics: Windows 11 Laptop

> **Scope:** Suspected compromise of a Windows 11 corporate laptop: malware, credential theft, insider cases, ransomware precursors. Related capabilities: RS-2, RS-3, DE-3.
> **Legal note:** Laptop data includes employee personal data. Follow your monitoring legal basis under GDPR, involve the DPO for insider cases, and use the chain-of-custody form for anything that may reach court or a regulator. <!-- law:gdpr -->

## 0. Prerequisites — build these BEFORE the incident

- [ ] EDR deployed with remote isolation and live-response capability
- [ ] BitLocker recovery keys escrowed centrally in AD, Entra or MDM. **Without them, dead-box forensics on an encrypted disk is impossible**
- [ ] Write blocker + sanitised external storage + memory-capture tooling on the jump kit
- [ ] Local admin credentials retrievable per device, via LAPS or an equivalent
- [ ] Chain-of-custody forms and evidence bags/labels

## 1. Triage — do not touch the device yet

1. Pull EDR telemetry, identity logs from Entra ID and AD sign-ins, proxy/DNS for the host, and build the initial timeline **remotely**.
2. Classify severity per the IR plan; open incident record and timeline log.
3. Decide the fork. **Evidence-priority** for insider, legal or major-breach cases means maximum preservation; **containment-priority** for active ransomware means isolate now and preserve what you can.

## 2. Containment

- **Preferred:** EDR network isolation, which preserves memory and disk state and keeps the EDR channel.
- If no EDR: disconnect the network by switching Wi-Fi off or unplugging, but **do not shut down**. RAM and BitLocker state are lost on power-off.
- Disable/lock the user's accounts and **revoke refresh tokens and sessions** in the cloud identity; reset credentials from a clean device only.
- Block identified C2 indicators at proxy/firewall; hunt the same indicators fleet-wide before the adversary knows you know.

## 3. Evidence acquisition — order of volatility per RFC 3227

> Document every action with timestamp and operator in the incident log. Hash everything you collect with SHA-256.

| # | Evidence | How | Windows 11 notes |
|---|----------|-----|------------------|
| 1 | **Memory, RAM** | Capture with a memory acquisition tool run from external media/EDR live response | Capture **before** shutdown. Memory integrity/VBS features can interfere with some tools, so test your tool on your standard image *in advance*. |
| 2 | **Volatile system state** | Live response: network connections, processes, logged-on users, ARP/DNS cache, open handles | Prefer EDR live response over interactive console use, which leaves less footprint. |
| 3 | **Disk image** | Full physical image, or targeted triage collection if scoped | **BitLocker:** image while the volume is unlocked, or ensure the recovery key is in hand. Fast Startup: if enabled, `hiberfil.sys` may contain a memory snapshot, so collect it. |
| 4 | **Cloud/remote artefacts** | Export identity sign-in logs, MDM/Intune device record, OneDrive/SharePoint audit for the user | Often more complete than the device itself; not lost if the device is wiped. |

**Key Windows 11 disk artefacts for the analyst:**

- **Event logs** in `C:\Windows\System32\winevt\Logs`: Security, System, PowerShell/Operational, Sysmon if deployed, WDAC/Defender logs
- **Execution evidence**: Prefetch, Amcache.hve, ShimCache in the SYSTEM hive, SRUM in `SRUDB.dat`, UserAssist
- **Persistence**: Run keys, Scheduled Tasks, Services, WMI subscriptions, Startup folders
- **File activity**: `$MFT`, the USN Journal `$J`, LNK files & Jump Lists, Recycle Bin
- **User context**: NTUSER.DAT, browser history/downloads, PowerShell history in `ConsoleHost_history.txt`

## 4. Analysis pointers

- Build a super-timeline from filesystem metadata, event logs and EDR around the first suspicious event.
- Map findings to MITRE ATT&CK techniques; feed new indicators back to DETECT via the use case template.
- Answer the four regulator questions: initial access, scope, data impact covering what, whose and how much, and containment status. <!-- law:nis2 --><!-- law:gdpr -->

## 5. Eradication & recovery

- Default for confirmed compromise: **reimage from known-good**. Do not "clean" a laptop.
- Rotate all credentials/tokens the user or device held, including saved browser passwords, VPN certs and Wi-Fi PSKs.
- Re-enrol the device, with a new Entra or AD object recommended for serious cases; restore user data from clean backup after scanning.
- Closure criteria: no residual indicators fleet-wide for [7] days; lessons-learned filed.

## 6. Reporting hooks

- Personal data on device likely affected → DPO breach assessment under GDPR Art. 33, on a 72 h clock from awareness. <!-- law:gdpr -->
- If the incident is significant at organisational level → NIS2 early warning ≤ 24 h to national CSIRT. <!-- law:nis2 -->
- Financial entities: DORA classification and Art. 19 timelines. <!-- law:dora -->

## Non-normative open source tooling examples

Memory: WinPmem/DumpIt-class tools · Timeline & artefacts: Plaso/log2timeline, Eric Zimmerman's KAPE-style targeted collection tools, Velociraptor · Analysis: Volatility 3, Autopsy/Sleuth Kit.

## Sources
- NIST SP 800-86, *Guide to Integrating Forensic Techniques into Incident Response*.
- RFC 3227, *Guidelines for Evidence Collection and Archiving*.
- NIST SP 800-61r3. Microsoft public documentation for BitLocker/Windows artefact behaviour.

*Open CDC Framework, licensed CC BY 4.0.*
