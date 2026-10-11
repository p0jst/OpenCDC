# National annexes for all 27 EU member states

Per-country NIS2 implementation status, competent authority, national CSIRT and
CDC-relevant notes. The table shows when each country was last reviewed; national situations
change, so treat "unverified" and "pending" flags seriously and open an issue
with corrections. Country facts are edited in one place,
[`countries.json`](countries.json), and `python tools/build_countries.py`
writes them into this table, the annexes and the regulatory selector.

> **One reviewer so far, none yet checked against primary sources.** Every
> annex has been reviewed by the maintainer only, against authority websites
> and secondary sources. None is yet checked line by line against the
> official gazette or legal database itself; see the confidence levels below
> for exactly what each one means. Before you cite an annex to an auditor or
> regulator, check the date it was last reviewed and confirm the key facts
> against the official sources listed in it. Each annex opens with a status
> block showing its confidence level, whether it has been checked line by line
> against the legal text or reviewed by a lawyer, when it was last reviewed, by
> whom, and when the next review is due. Annexes are re-reviewed at least every six
> months. A second reviewer per country is the most useful contribution you
> can make; see [CONTRIBUTING](../../CONTRIBUTING.md).

<!-- countries:begin -->
| Country | Status | Confidence | Last reviewed | Second reviewer | Next review | Annex |
|---------|--------|------------|---------------|-----------------|-------------|-------|
| Austria | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-at.md) |
| Belgium | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-be.md) |
| Bulgaria | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-bg.md) |
| Croatia | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-hr.md) |
| Cyprus | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-cy.md) |
| Czechia | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-cz.md) |
| Denmark | In force | Maintainer reviewed | Sep 2026 | Wanted | Mar 2027 | [Open](annex-dk.md) |
| Estonia | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-ee.md) |
| Finland | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-fi.md) |
| France | Pending, in the legislative process | Pending legislative change | Oct 2026 | Wanted | Apr 2027 | [Open](annex-fr.md) |
| Germany | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-de.md) |
| Greece | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-gr.md) |
| Hungary | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-hu.md) |
| Ireland | Pending, bill not yet published | Pending legislative change | Oct 2026 | Wanted | Apr 2027 | [Open](annex-ie.md) |
| Italy | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-it.md) |
| Latvia | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-lv.md) |
| Lithuania | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-lt.md) |
| Luxembourg | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-lu.md) |
| Malta | In force | Needs verification | Oct 2026 | Wanted | Apr 2027 | [Open](annex-mt.md) |
| Netherlands | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-nl.md) |
| Poland | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-pl.md) |
| Portugal | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-pt.md) |
| Romania | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-ro.md) |
| Slovakia | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-sk.md) |
| Slovenia | In force, secondary acts unverified | Needs verification | Oct 2026 | Wanted | Apr 2027 | [Open](annex-si.md) |
| Spain | Pending, bill not yet in parliament | Pending legislative change | Oct 2026 | Wanted | Apr 2027 | [Open](annex-es.md) |
| Sweden | In force | Maintainer reviewed | Oct 2026 | Wanted | Apr 2027 | [Open](annex-se.md) |
<!-- countries:end -->

## Confidence levels

Each annex carries one of four confidence levels, so you can see how far to rely on it before citing it:

| Level | Meaning |
|-------|---------|
| **Verified against primary source** | Checked against the official gazette or legal database, with the source linked in the annex. |
| **Maintainer reviewed** | Checked by the maintainer against authority websites and secondary sources, but not yet line by line against the legal text. |
| **Needs verification** | Adopted, but key facts such as dates, secondary acts or completeness are unconfirmed. |
| **Pending legislative change** | The national law is not yet in force; expect the content to change. |

No annex is yet marked *verified against primary source*. Every one currently
sits at maintainer-reviewed or below. None has been reviewed by a lawyer. Moving an annex up a level is a good
first contribution.

Naming convention: `annex-<ISO 3166-1 alpha-2>.md`. Denmark is the reference
annex, the most detailed; help us bring your country's annex to the same depth.

Cross-EU context and reporting deadline tables: see the
[EU regulatory landscape](../eu-regulatory-landscape.md) and the
[interactive regulatory profile selector](../../tools/regulatory-profile.html).
