# Lab 02: Design a Lead Magnet and Drip Lifecycle

**Course:** Claude Cowork for Email Marketing (TGS-2020503109)
**Version:** v14.0
**Topic:** 1
**Human gate:** Required before the final artifact is accepted.

## Objective

Turn a customer tension into a credible lead magnet and five-state lifecycle sequence.

## Deliverable

Lifecycle map, lead-magnet proposition and consent copy

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

1. Create a Cowork task in the same project and select only this lab folder.
2. Read the interview rows and identify repeated needs and barriers.
3. Draft one lead-magnet hypothesis; do not claim medical or guaranteed outcomes.
4. Specify the minimum signup fields and explicit consent wording.
5. Map five lifecycle states with entry, message job and exit rule.
6. Check that unsubscribed and hard-bounce contacts cannot enter any state.
7. Save the lifecycle in `solution/lifecycle.json`.
8. Run the verifier and complete the promise-integrity checklist.

## Workflow checkpoints

- 1. Find tension: record input, action, output and evidence.
- 2. Define asset: record input, action, output and evidence.
- 3. Minimise fields: record input, action, output and evidence.
- 4. Map stages: record input, action, output and evidence.
- 5. Set exits: record input, action, output and evidence.
- 6. Approve promise: record input, action, output and evidence.

## Acceptance

The promise matches the source evidence, consent is explicit and every lifecycle state has entry and exit rules.

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
