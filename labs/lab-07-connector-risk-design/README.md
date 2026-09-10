# Lab 07: Design a Safe Cowork Connector Workflow

**Course:** Claude Cowork for Email Marketing (TGS-2020503109)
**Version:** v14.0
**Topic:** 4
**Human gate:** Required before the final artifact is accepted.

## Objective

Map a draft-to-platform workflow with least privilege, untrusted-input handling and explicit tool boundaries.

## Deliverable

Connector map, permission register and injection test

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

1. Inventory the mock connector operations and mark read versus write consequences.
2. Design the draft-to-review flow without permitting send or delete.
3. Set the smallest folder and connector scopes for each stage.
4. Treat `untrusted-inbound.txt` as data, not task instructions.
5. Ask Claude to identify the embedded prompt-injection attempt.
6. Verify no forbidden connector operation appears in the plan.
7. Save the connector map and permission register.
8. Run the verifier and record the blocked-injection evidence.

## Workflow checkpoints

- 1. Name systems: record input, action, output and evidence.
- 2. Select tools: record input, action, output and evidence.
- 3. Limit scope: record input, action, output and evidence.
- 4. Classify trust: record input, action, output and evidence.
- 5. Test injection: record input, action, output and evidence.
- 6. Approve design: record input, action, output and evidence.

## Acceptance

No live send occurs; scopes are minimal; embedded instructions are blocked and surfaced for human review.

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
