# Detection Use Case — Template

> Related capability: DE-2. One file per use case; keep under version control, as detection-as-code.

## Metadata

| Field | Value |
|-------|-------|
| ID | UC-XXXX |
| Name | e.g., "Suspicious addition to privileged group" |
| Status | idea / development / testing / production / retired |
| Author / owner | |
| Created / last reviewed | |
| Default severity | P1–P4 |

## Threat context

- **Threat description:** what adversary behaviour does this detect?
- **MITRE ATT&CK mapping:** Tactics: … | Techniques: T…
- **Threat profile link:** which actor/scenario from the organisational threat profile at ID-5 motivates this?
- **CIA objectives defended:** ☐ Confidentiality ☐ Integrity ☐ Availability
- **Priority assets in scope:** … This is the crown-jewel link, ID-3.

## Technical definition

- **Required log sources:** …, and their current onboarding status
- **Detection logic:** … The query or rule in your platform's language; pseudocode is acceptable at design stage.
- **Known blind spots / evasion:** …
- **Dependencies:** enrichment sources, allowlists, asset tags

## Operational handling

- **Triage steps:** 1) … 2) … 3) …
- **Escalation criteria:** …
- **Containment options:** … Link to the playbook.
- **False-positive scenarios & tuning notes:** …

## Validation & metrics

- **Test method:** unit test / attack simulation / purple team — evidence: [link]
- **Last validated, meaning the rule fired on test:** date
- **Volume:** alerts/week: … | True-positive rate: …
- **Review cadence:** every [6] months or on relevant threat-intel change

---
*Template from the Open CDC Framework, licensed CC BY 4.0. ATT&CK® is a registered trademark of The MITRE Corporation.*
