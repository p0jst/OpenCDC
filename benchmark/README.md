# Benchmark: maintainer notes

How the community benchmark in the maturity self-assessment is run. The
public explanation is in [the community benchmark](../docs/benchmark.md).

## Receiving contributions

Contributions arrive by email at benchmark@opencdc.org, as a JSON object in
the message body or as an attached `ocdf-benchmark-contribution.json`.

1. Save each one as a separate `.json` file in `benchmark/submissions/`.
   That folder is git-ignored: **never commit raw contributions**.
   Keep the folder, and the mailbox, somewhere backed up and access-controlled.
2. Do not store the sender's address in the file. The mailbox is the only link
   between a contribution and its sender, which is what makes removal on
   request possible.
3. Run the aggregation from the repository root:

       python benchmark/aggregate.py

   It validates every file, reports and skips invalid ones, and rewrites
   `tools/benchmark.json`.
4. Commit and push `tools/benchmark.json`. The tool on the website picks it
   up on the next page load.

## Rules the script enforces

- A group is published only when it has at least `MIN_GROUP` (10)
  contributions. Smaller groups appear only as a count.
- Groups are formed on one attribute at a time (size, NIS2 category, region),
  never combinations, so no group can be narrowed to a few organisations.
- Criteria and scoring are read from `tools/maturity-assessment.html`, so the
  benchmark always scores exactly as the tool does.

## When the criteria change

Each contribution records the framework version and the criteria set,
`criteria_set`. The script aggregates only the current set, `CRITERIA_SET` in
`aggregate.py`, and rejects the rest with a message. Criteria set 2 arrived
with the NIS2 legal floor, after v1.1.0; a set-1 contribution cannot be mapped
reliably, because new Level 2 criteria have no set-1 answer, so ask its sender
to re-score in the current tool. Record every change of set in the changelog
under **Scoring changes**.

## Removal requests

Find the sender's message in the mailbox, delete the matching file from
`benchmark/submissions/`, rerun the script and push.
