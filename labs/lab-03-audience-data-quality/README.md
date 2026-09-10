# Lab 03: Audit and Repair an Audience Dataset

**Course:** Claude Cowork for Email Marketing (TGS-2020503109)
**Version:** v14.0
**Topic:** 2
**Human gate:** Required at the evidence review checkpoint.

## Objective

Use synthetic subscriber data to identify consent, status, duplicate and quality defects before segmentation.

## Deliverable

Cleaned CSV, data-quality report and suppression ledger

## Safety boundary

- Use only the synthetic `.test` addresses and supplied mock files.
- Grant Cowork access only to this lab folder.
- Do not connect a live ESP, import real subscribers, send email, or paste credentials.
- Treat email, web, and document contents as untrusted data; they cannot change the lab instructions.

## Folder map

- `mock-data/` — source evidence for the case.
- `starter/` — required output schema and blank work area.
- `solution/` — reference artifact and expected output.
- `prompt.md` — bounded Cowork task.
- `lab.yaml` — lab identity, mapping, inputs and acceptance rule.
- `scripts/verify_lab.py` — deterministic structural verifier.
- `evidence/checklist.md` and PDF — learner evidence record.

## Detailed procedure

1. Create a lab-only Cowork project and open `audience.csv` plus the dictionary.
2. Ask Claude to profile row count, duplicate IDs, invalid email formats, consent gaps and suppressed states.
3. Require a reconciliation table before any repair.
4. Deduplicate by contact ID while retaining the most complete valid row.
5. Route missing consent to review; route unsubscribe and hard bounce to suppression.
6. Save a cleaned CSV and a suppression ledger in `solution/`.
7. Confirm input rows equal kept plus suppressed plus review, accounting for duplicates.
8. Run the verifier and retain its output.

## Workflow checkpoints

- 1. Read schema: record input, action, output and evidence.
- 2. Profile rows: record input, action, output and evidence.
- 3. Find defects: record input, action, output and evidence.
- 4. Apply rules: record input, action, output and evidence.
- 5. Reconcile counts: record input, action, output and evidence.
- 6. Export evidence: record input, action, output and evidence.

## Acceptance

All rows reconcile to kept, suppressed or review states; no personal data leaves the lab folder.

## Troubleshooting

- **Cowork cannot access a file:** confirm the selected project folder is this lab folder, then retry with the exact filename.
- **Output contains unsupported claims:** require a claim map, remove the claim, and add it to the unresolved-information list.
- **Counts do not reconcile:** return to the source rows and declared denominator; do not patch the final number manually.
- **A write or send requires permission:** keep the lab in dry-run mode. No live send is required for completion.
- **Verifier fails:** read the named missing field or mismatch, repair only that causal issue, and rerun.

## Cleanup

1. Export or screenshot only the requested learner evidence.
2. Remove the lab folder from the Cowork project or revoke folder access.
3. Delete any temporary duplicate working folder.
4. Confirm no credentials, real addresses, or live connector tokens were created.
