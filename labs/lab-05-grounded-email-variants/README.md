# Lab 05: Draft Grounded Email Variants

**Course:** Claude Cowork for Email Marketing (TGS-2020503109)
**Version:** v14.0
**Topic:** 3
**Human gate:** Required before the final artifact is accepted.

## Objective

Create welcome and launch email variants from a campaign brief, product facts and brand rubric.

## Deliverable

Two complete email variants, claim map and editorial scorecard

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

1. Create a Cowork project with the supplied brief and brand guidelines.
2. Ask Claude to list approved factual sources and unresolved information.
3. Draft one welcome email and one launch email with a single CTA.
4. Require subject, preview, text-first body, CTA and accessibility fields.
5. Create a claim map linking every factual statement to a file and field.
6. Score both drafts against the supplied editorial rubric.
7. Revise once without changing the approved offer.
8. Save the final bundle and run the verifier.

## Workflow checkpoints

- 1. Load brief: record input, action, output and evidence.
- 2. Read brand: record input, action, output and evidence.
- 3. Draft schema: record input, action, output and evidence.
- 4. Map claims: record input, action, output and evidence.
- 5. Score quality: record input, action, output and evidence.
- 6. Revise once: record input, action, output and evidence.

## Acceptance

Each email has one CTA, accessible structure, supported claims and a passed brand/compliance scorecard.

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
