# PB-LNX — Incident Response & Digital Forensics: RHEL-class Linux Enterprise Server

<p class="src" markdown><span class="src-tag practitioner">Practitioner</span><span class="src-tag standard">Standard</span>Response practice from experience; evidence handling follows RFC 3227 and NIST SP 800-86.</p>

> **Scope:** Suspected compromise of an enterprise RHEL-class Linux server, and by extension SLES or Ubuntu Server with path adjustments. Covers webshells, cryptominers, rootkits, lateral movement, ransomware on file/virtualisation servers. Related capabilities: RS-2, RS-3, DE-3.
> **Servers ≠ laptops:** containment decisions have direct **Availability** impact on business services. The pre-agreed authority matrix in the CDC charter §4 governs who may isolate what. <!-- law:nis2 -->

## 0. Prerequisites

- [ ] auditd or an equivalent with a meaningful ruleset, forwarding to central logging, because local logs on a rooted box are untrustworthy
- [ ] journald/syslog forwarded centrally; NTP/chrony verified, since evidence timelines die without time sync
- [ ] Out-of-band access via iLO, iDRAC, BMC or the hypervisor console, documented per server
- [ ] Known-good static binaries kit, busybox-class or vendored coreutils, on read-only media, assuming on-host binaries are trojaned
- [ ] For VMs: rights and procedure to **snapshot with memory** at the hypervisor
- [ ] LUKS keys/escrow documented where disk encryption is used

## 1. Triage — remote and central first

1. Work from **central** logs first: forwarded auth events from `/var/log/secure`, auditd, netflow and EDR. The host copy may be manipulated.
2. Identify the service impact tier and its crown-jewel link. This decides the containment authority path.
3. Fork: evidence-priority vs availability-priority. Active ransomware encrypting an NFS export, for instance, means isolate immediately.

## 2. Containment

- **VM:** hypervisor-level **snapshot including memory first**, then network-isolate at the virtual switch/security group. This is the cleanest evidence and containment combination available anywhere.
- **Physical:** isolate at switch port/firewall; keep power on. Use BMC console for access if SSH is untrusted.
- Do **not** kill suspicious processes or reboot before volatile collection. Rootkit persistence may be memory-only, and reboot destroys it as well as tipping off the adversary.
- Freeze credentials: disable implicated accounts, remove authorized_keys additions, rotate the secrets the server held: DB credentials, API keys and service accounts. Check your secrets manager audit log.

## 3. Evidence acquisition — order of volatility per RFC 3227

> Run collection with known-good binaries, output to remote or external storage, never to the evidence disk; hash everything, log every command with timestamp.

| # | Evidence | How | RHEL notes |
|---|----------|-----|------------|
| 1 | **Memory** | VM: hypervisor snapshot to a .vmem-class file. Physical: kernel-module or /proc/kcore-based acquisition, AVML/LiME-class | Secure Boot/lockdown mode may block unsigned modules; AVML-style userspace tools avoid this. Test per RHEL major version in advance. |
| 2 | Volatile state | From known-good binaries: `ps`, `ss -tunap`, `lsof`, loaded modules via `lsmod` and `/proc/modules`, mounts, users via `w`, iptables/nftables rules, environment of suspicious PIDs from `/proc/<pid>/environ`, `/proc/<pid>/exe`, `maps` and deleted-but-running binaries | `/proc/<pid>/exe` recovers deleted running malware, so collect before killing anything. |
| 3 | Logs & audit | `journalctl` export, `/var/log/` covering secure, audit/audit.log, cron, httpd/nginx and application logs, auditd raw logs | Compare host copies against central copies; deltas are themselves findings, and an Integrity concern. |
| 4 | Disk | LVM snapshot then image the snapshot, which minimises downtime, or dd/ewf image via boot from external media; VM: copy virtual disks from the snapshot | Record LUKS status; image while unlocked or with key escrowed. |
| 5 | Platform/cloud | Hypervisor/cloud audit logs, config management history showing what the host *should* look like, backup catalogues | Config management diffs from Ansible or Satellite are gold for spotting unauthorised change. |

**Key Linux artefacts:**

- **Accounts & access**: `/etc/passwd|shadow|group`, sudoers and sudoers.d, `~/.ssh/authorized_keys` for all users, last/btmp/wtmp/lastlog, PAM configs
- **Persistence**: cron across all crontabs and /etc/cron.*, **systemd units & timers** including user units in `~/.config/systemd/user`, rc.local, `/etc/ld.so.preload` & LD_PRELOAD, shell profiles/rc files, udev rules, malicious PAM modules, SSH forced commands
- **Execution/history**: shell histories for all users including root, noting gaps and `HISTFILE` tampering, `/tmp`,`/dev/shm`,`/var/tmp` contents, auditd execve records
- **Package integrity**: `rpm -Va` against a trusted rpmdb, which flags modified binaries, a classic rootkit tell
- **Web tier**: webroot diff vs deployment source to catch webshells, access logs around first-touch
- **Containers**: `podman/docker ps -a`, images, overlay diffs, container logs, since a "clean host" may have a dirty container

## 4. Analysis pointers

- Timeline: filesystem metadata + auditd + central auth logs + application logs; pivot on first anomalous auth or exploit signature.
- Rootkit checks: kernel taint in `/proc/sys/kernel/tainted`, hidden PIDs by comparing a `/proc` walk against `ps`, `rpm -Va`, `ld.so.preload`.
- Determine data impact: what data did the service hold/process, was there staging or exfil such as large outbound transfers or archive files in tmp? This feeds breach notification decisions. <!-- law:gdpr -->

## 5. Eradication & recovery

- **Rebuild from known-good** images or config management. Never trust a "cleaned" server that had root-level compromise.
- Redeploy from IaC/config management; restore data from backups **after integrity verification**, following the Recover principle of Integrity before Availability.
- Rotate every secret the host could read; re-issue host keys/certs; review trust relationships across NFS exports, SSH trust and service mesh certs.
- Fleet hunt: run the same indicator/persistence checks across all similar servers before closing.

## 6. Reporting hooks

- Service disruption or data impact on essential/important services → NIS2 Art. 23 clock, early warning within 24 h. <!-- law:nis2 -->
- Personal data in scope in databases, logs or user content → GDPR Art. 33/34 via DPO. <!-- law:gdpr -->
- Financial entities → DORA Art. 19. <!-- law:dora -->

## Non-normative open source tooling examples

Memory: AVML, LiME, Volatility 3 · Collection: Velociraptor, the Unix-like Artifacts Collector UAC, osquery · Disk/timeline: Sleuth Kit, Plaso · Integrity: AIDE, `rpm -Va`.

## Sources
- NIST SP 800-86; RFC 3227; NIST SP 800-61r3.
- Red Hat public documentation on auditd, LVM snapshots and systemd: https://docs.redhat.com

*Open CDC Framework, licensed CC BY 4.0.*
