# Capability Index

Every capability in the framework, with the document that defines it and the
lowest [implementation tier](10-tiers.md) that should adopt it. The framework
addresses capabilities by ID throughout, so this is the page to come back to
whenever a reference like `PR-7` or `DE-4` appears and you want the detail.

Tier column: **E** Essential, **S** Standard, **A** Advanced. Higher tiers
include everything below them, so an S-tier CDC adopts the E rows too. On the
website, filter by function or by your tier to see just what applies to you.

<div class="cap-filter" id="cap-filter" hidden>
  <label>Function <select id="cf-fn"><option value="">All</option><option>GOVERN</option><option>IDENTIFY</option><option>PROTECT</option><option>DETECT</option><option>RESPOND</option><option>RECOVER</option></select></label>
  <label>Applies at my tier <select id="cf-tier"><option value="">Any</option><option value="E">Essential</option><option value="S">Standard</option><option value="A">Advanced</option></select></label>
  <label>Search <input type="search" id="cf-q" placeholder="e.g. backup, identity"></label>
  <output id="cf-count"></output>
</div>

| ID | Capability | Function | Tier |
|----|------------|----------|------|
| **GV-1** | CDC charter & mandate | [GOVERN](01-govern.md) | E |
| **GV-2** | Risk management integration | [GOVERN](01-govern.md) | S |
| **GV-3** | Policy framework | [GOVERN](01-govern.md) | E |
| **GV-4** | Roles & accountability | [GOVERN](01-govern.md) | E |
| **GV-5** | Budget & resourcing governance | [GOVERN](01-govern.md) | S |
| **GV-6** | Supply chain risk governance | [GOVERN](01-govern.md) | S |
| **GV-7** | Oversight & reporting | [GOVERN](01-govern.md) | E |
| **ID-1** | Asset inventory | [IDENTIFY](02-identify.md) | E |
| **ID-2** | Data classification | [IDENTIFY](02-identify.md) | S |
| **ID-3** | Crown-jewel analysis | [IDENTIFY](02-identify.md) | E |
| **ID-4** | Vulnerability identification | [IDENTIFY](02-identify.md) | E |
| **ID-5** | Threat landscape & intelligence | [IDENTIFY](02-identify.md) | S |
| **ID-6** | Risk assessment | [IDENTIFY](02-identify.md) | S |
| **ID-7** | Improvement identification | [IDENTIFY](02-identify.md) | S |
| **PR-1** | Identity & access management | [PROTECT](03-protect.md) | E |
| **PR-2** | Awareness & training | [PROTECT](03-protect.md) | E |
| **PR-3** | Data security | [PROTECT](03-protect.md) | S |
| **PR-4** | Platform hardening & secure configuration | [PROTECT](03-protect.md) | S |
| **PR-5** | Vulnerability remediation & patching | [PROTECT](03-protect.md) | E |
| **PR-6** | Network security & segmentation | [PROTECT](03-protect.md) | S |
| **PR-7** | Resilient technology infrastructure | [PROTECT](03-protect.md) | E |
| **PR-8** | Secure development & change | [PROTECT](03-protect.md) | A |
| **PR-9** | Email & web protections | [PROTECT](03-protect.md) | E |
| **DE-1** | Log collection & management | [DETECT](04-detect.md) | E |
| **DE-2** | Detection engineering | [DETECT](04-detect.md) | S |
| **DE-3** | Alert triage & analysis | [DETECT](04-detect.md) | E |
| **DE-4** | Coverage assessment | [DETECT](04-detect.md) | S |
| **DE-5** | Threat hunting | [DETECT](04-detect.md) | A |
| **DE-6** | Detection validation | [DETECT](04-detect.md) | A |
| **DE-7** | Anomaly & integrity monitoring | [DETECT](04-detect.md) | S |
| **RS-1** | Incident response plan | [RESPOND](05-respond.md) | E |
| **RS-2** | Playbooks | [RESPOND](05-respond.md) | E |
| **RS-3** | Incident analysis & forensics | [RESPOND](05-respond.md) | S |
| **RS-4** | Containment & eradication | [RESPOND](05-respond.md) | S |
| **RS-5** | Incident reporting & communication | [RESPOND](05-respond.md) | E |
| **RS-6** | Crisis management interface | [RESPOND](05-respond.md) | A |
| **RS-7** | Exercises | [RESPOND](05-respond.md) | S |
| **RC-1** | Recovery planning | [RECOVER](06-recover.md) | E |
| **RC-2** | Trusted restoration | [RECOVER](06-recover.md) | S |
| **RC-3** | Recovery execution & verification | [RECOVER](06-recover.md) | S |
| **RC-4** | Recovery communication | [RECOVER](06-recover.md) | E |
| **RC-5** | Lessons learned & improvement loop | [RECOVER](06-recover.md) | E |
| **RC-6** | Business continuity integration | [RECOVER](06-recover.md) | S |

<script>
/* Filter the capability table in place. The filter bar stays hidden when
   scripts are off, and the full table remains readable either way. */
(function(){
  const bar = document.getElementById("cap-filter");
  if(!bar) return;
  const table = bar.parentElement.querySelector("table");
  if(!table) return;
  bar.hidden = false;
  const rows = [...table.tBodies[0].rows];
  const rank = {E:1, S:2, A:3};
  const fn = document.getElementById("cf-fn"), tier = document.getElementById("cf-tier"),
        q = document.getElementById("cf-q"), out = document.getElementById("cf-count");
  function apply(){
    const f = fn.value, tr = tier.value, s = q.value.trim().toLowerCase();
    let shown = 0;
    for(const r of rows){
      const c = r.cells;
      const ok = (!f || c[2].textContent.trim() === f)
        && (!tr || rank[c[3].textContent.trim()] <= rank[tr])
        && (!s || r.textContent.toLowerCase().includes(s));
      r.hidden = !ok; if(ok) shown++;
    }
    out.textContent = shown + " of " + rows.length + " capabilities";
  }
  [fn, tier].forEach(e => e.addEventListener("change", apply));
  q.addEventListener("input", apply);
  apply();
})();
</script>

## Related indexes

- [Reading guide](README.md) for the order the documents are meant to be read in.
- [Implementation tiers](10-tiers.md) for what E, S and A mean and how to pick yours.
- [Maturity model](08-maturity-model.md) for how well you run the capabilities you have adopted.
- [CIS Controls crosswalk](18-cis-controls-crosswalk.md) to map these capabilities onto CIS Controls v8.1.

*Open CDC Framework, licensed CC BY 4.0. Generated from the capability tables in documents 01 to 06.*
