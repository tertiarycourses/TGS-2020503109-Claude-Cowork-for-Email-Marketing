# Lab 08: Control an Approved Scheduled Campaign

**Course:** Claude Cowork for Email Marketing (TGS-2020503109)
**Version:** v14.0
**Topic:** 4
**Human gate:** Required before the final artifact is accepted.

## Objective

Create a dry-run automation contract that binds human approval to a frozen content and audience payload.

## Deliverable

Workflow YAML, content hash, approval receipt and run log

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

1. Open the approved draft and mock connector registry.
2. Generate a canonical payload containing draft ID, segment ID, subject and CTA.
3. Calculate the SHA-256 hash with `scripts/hash_payload.py`.
4. Create an approval receipt containing the hash, approver, decision and expiry.
5. Run a dry-run schedule only after hash equality and expiry checks pass.
6. Repeat with an altered subject and confirm the workflow blocks.
7. Repeat the same run key and confirm no duplicate schedule record appears.
8. Run the verifier and preserve the terminal run log.

## Workflow checkpoints

- 1. Build draft: record input, action, output and evidence.
- 2. Freeze payload: record input, action, output and evidence.
- 3. Request approval: record input, action, output and evidence.
- 4. Verify hash: record input, action, output and evidence.
- 5. Dry-run schedule: record input, action, output and evidence.
- 6. Log outcome: record input, action, output and evidence.

## Acceptance

Exactly one dry-run schedule is recorded for the approved payload; rejection, expiry and retry cases stop safely.

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
