# Contributing to the Open CDC Framework

Thank you for helping European teams defend better. Contributions of all sizes are welcome.

## What we're especially looking for

1. **National annexes** — NIS2 transposition specifics, national CSIRT contacts and reporting portals, per member state. Status, law, authority, CSIRT and review dates are edited in `docs/annexes/countries.json` and written out by `python tools/build_countries.py`; country notes and anything longer go in `docs/annexes/annex-<ISO country code>.md`, outside the generated block.
2. **Translations** — the framework aims to be available in EU languages, under `i18n/<lang>/`.
3. **Templates & playbooks** — additional scenario playbooks, report templates for statutory notifications.
4. **Corrections** — factual, regulatory, or attribution fixes; high priority, so open an issue immediately.
5. **Field feedback** — did the maturity criteria match reality in your assessment? Open a discussion.

## Ground rules

- **Vendor neutrality:** no product names in normative documents. Tooling examples belong in clearly marked non-normative appendices and must include open source options where they exist.
- **Credit everything:** any content derived from another work must be attributed in the document's Sources section *and* in `docs/references.md`. Respect the source's license.
- **No confidential material:** never contribute internal documents, real incident data, or client information.
- **Regulatory content:** cite the EUR-Lex ELI link for any legal claim, and mark interpretation clearly as interpretation.
- **Language:** contributions in English for core docs; translations maintained separately.

## How to contribute

1. Open an **issue** describing the change, using the templates.
2. For text changes: fork → branch, named `docs/<topic>` or `fix/<topic>` → pull request referencing the issue.
3. One logical change per PR; keep the document structure intact for function docs: Objective, Capabilities, CIA mapping, Roles & staffing, Maturity, EU hooks, External dependencies, Sources.
4. **Maturity criteria** are edited only in `assessments/maturity-self-assessment.md`, then mirrored in the tool's `CATALOG`. Any change to a criterion is a scoring change: note it in the changelog, and if it moves or adds criteria, raise `CRITERIA_SET` and extend the migration map in the tool.
5. Run `python tools/check_consistency.py` before opening the pull request; the site build runs it too and fails on drift.
6. A maintainer will review for accuracy, neutrality, and attribution before merging.

## Licensing of contributions

By contributing, you agree that your contribution is licensed under **CC BY 4.0**, and you confirm you have the right to submit it.

## Code of Conduct

Be professional and constructive. Disagreement about content is welcome; disrespect toward people is not. Report issues to the maintainers.
