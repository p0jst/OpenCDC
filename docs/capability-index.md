# Capability Index

<p class="src" markdown><span class="src-tag ocdf">OCDF</span></p>

Every capability in the framework, with the document that defines it and the
lowest [implementation tier](tiers.md) that should adopt it. The framework
addresses capabilities by ID throughout, so this is the page to come back to
whenever a reference like `PR-7` or `DE-4` appears and you want the detail.

Tier column: **E** Essential, **S** Standard, **A** Advanced. Higher tiers
include everything below them, so an S-tier CDC adopts the E rows too. The NIS2
column marks the capabilities that carry the legal floor: the article or
Art. 21(2) point whose minimum they deliver. For an entity in NIS2 scope a marked
capability is never "above tier"; do at least its Level 2 form. PR-8 is the one
marked capability above Essential, because only its basic form, security
requirements when buying or changing critical systems, is part of the floor. See
[the legal floor](tiers.md#the-legal-floor) and the
[NIS2 Article 21 crosswalk](nis2-article-21-crosswalk.md). On the website,
filter by function or by your tier to see just what applies to you.

<div class="cap-filter" id="cap-filter" hidden>
  <label>Function <select id="cf-fn"><option value="">All</option><option>GOVERN</option><option>IDENTIFY</option><option>PROTECT</option><option>DETECT</option><option>RESPOND</option><option>RECOVER</option></select></label>
  <label>Applies at my tier <select id="cf-tier"><option value="">Any</option><option value="E">Essential</option><option value="S">Standard</option><option value="A">Advanced</option></select></label>
  <label>Search <input type="search" id="cf-q" placeholder="e.g. backup, identity"></label>
  <output id="cf-count"></output>
</div>

| ID | Capability | Function | Tier | NIS2 |
|----|------------|----------|------|------|
| **GV-1** | CDC charter & mandate | [GOVERN](govern.md) | E |  |
| **GV-2** | Risk management integration | [GOVERN](govern.md) | S |  |
| **GV-3** | Policy framework | [GOVERN](govern.md) | E | 21(2)(a) |
| **GV-4** | Roles & accountability | [GOVERN](govern.md) | E |  |
| **GV-5** | Budget & resourcing governance | [GOVERN](govern.md) | S |  |
| **GV-6** | Supply chain risk governance | [GOVERN](govern.md) | E | 21(2)(d) |
| **GV-7** | Oversight & reporting | [GOVERN](govern.md) | E | Art. 20, 21(2)(f) |
| **ID-1** | Asset inventory | [IDENTIFY](identify.md) | E | 21(2)(i) |
| **ID-2** | Data classification | [IDENTIFY](identify.md) | S |  |
| **ID-3** | Crown-jewel analysis | [IDENTIFY](identify.md) | E |  |
| **ID-4** | Vulnerability identification | [IDENTIFY](identify.md) | E | 21(2)(e) |
| **ID-5** | Threat landscape & intelligence | [IDENTIFY](identify.md) | E |  |
| **ID-6** | Risk assessment | [IDENTIFY](identify.md) | E | 21(2)(a) |
| **ID-7** | Improvement identification | [IDENTIFY](identify.md) | S |  |
| **PR-1** | Identity & access management | [PROTECT](protect.md) | E | 21(2)(i), (j) |
| **PR-2** | Awareness & training | [PROTECT](protect.md) | E | 21(2)(g) |
| **PR-3** | Data security | [PROTECT](protect.md) | E | 21(2)(h) |
| **PR-4** | Platform hardening & secure configuration | [PROTECT](protect.md) | E | 21(2)(g) |
| **PR-5** | Vulnerability remediation & patching | [PROTECT](protect.md) | E | 21(2)(e) |
| **PR-6** | Network security & segmentation | [PROTECT](protect.md) | S |  |
| **PR-7** | Resilient technology infrastructure | [PROTECT](protect.md) | E | 21(2)(c) |
| **PR-8** | Secure development & change | [PROTECT](protect.md) | S | 21(2)(e), basic form |
| **PR-9** | Email & web protections | [PROTECT](protect.md) | E | 21(2)(g) |
| **DE-1** | Log collection & management | [DETECT](detect.md) | E | 21(2)(b) |
| **DE-2** | Detection engineering | [DETECT](detect.md) | S |  |
| **DE-3** | Alert triage & analysis | [DETECT](detect.md) | E | 21(2)(b) |
| **DE-4** | Coverage assessment | [DETECT](detect.md) | S |  |
| **DE-5** | Threat hunting | [DETECT](detect.md) | S |  |
| **DE-6** | Detection validation | [DETECT](detect.md) | A |  |
| **DE-7** | Anomaly & integrity monitoring | [DETECT](detect.md) | S |  |
| **RS-1** | Incident response plan | [RESPOND](respond.md) | E | 21(2)(b) |
| **RS-2** | Playbooks | [RESPOND](respond.md) | E | 21(2)(b) |
| **RS-3** | Incident analysis & forensics | [RESPOND](respond.md) | S |  |
| **RS-4** | Containment & eradication | [RESPOND](respond.md) | E | 21(2)(b) |
| **RS-5** | Incident reporting & communication | [RESPOND](respond.md) | E | Art. 23 |
| **RS-6** | Crisis management interface | [RESPOND](respond.md) | E | 21(2)(c) |
| **RS-7** | Exercises | [RESPOND](respond.md) | E | 21(2)(b), (f) |
| **RC-1** | Recovery planning | [RECOVER](recover.md) | E | 21(2)(c) |
| **RC-2** | Trusted restoration | [RECOVER](recover.md) | S |  |
| **RC-3** | Recovery execution & verification | [RECOVER](recover.md) | S |  |
| **RC-4** | Recovery communication | [RECOVER](recover.md) | E |  |
| **RC-5** | Lessons learned & improvement loop | [RECOVER](recover.md) | E |  |
| **RC-6** | Business continuity integration | [RECOVER](recover.md) | S |  |

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
- [Implementation tiers](tiers.md) for what E, S and A mean and how to pick yours.
- [Maturity model](maturity-model.md) for how well you run the capabilities you have adopted.
- [NIS2 Article 21 crosswalk](nis2-article-21-crosswalk.md) for the legal floor behind the NIS2 column.
- [NIST CSF 2.0 crosswalk](csf-crosswalk.md) to map these capabilities onto the CSF 2.0 categories.
- [CIS Controls crosswalk](cis-controls-crosswalk.md) to map these capabilities onto CIS Controls v8.1.

*Open CDC Framework, licensed CC BY 4.0. Generated from the capability tables in the six function documents (Govern through Recover).*
