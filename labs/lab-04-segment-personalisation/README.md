# Lab 04: Create Explainable Segments and Personalisation

**Course:** Claude Cowork for Email Marketing (TGS-2020503109)
**Version:** v14.0
**Topic:** 2
**Human gate:** Required before the final artifact is accepted.

## Objective

Create reproducible audience segments and a safe personalisation matrix from the cleaned mock audience.

## Deliverable

Segment manifest, member preview and fallback matrix

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

1. Use the cleaned audience artifact from the starter folder.
2. Define three segment rules using status, interest and lifecycle only.
3. Ask Claude to preview member IDs and counts before producing copy.
4. Verify every segment excludes suppression states and consent gaps.
5. Resolve overlap with an explicit priority rule.
6. Create a personalisation matrix with a safe generic fallback.
7. Save `solution/segment-manifest.json`.
8. Run the verifier and sample-check every included member.

## Workflow checkpoints

- 1. Choose signal: record input, action, output and evidence.
- 2. Write rule: record input, action, output and evidence.
- 3. Preview cohort: record input, action, output and evidence.
- 4. Check overlap: record input, action, output and evidence.
- 5. Set fallback: record input, action, output and evidence.
- 6. Approve use: record input, action, output and evidence.

## Acceptance

Rules reproduce member counts, suppressed contacts are excluded and sensitive attributes are not used.

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
