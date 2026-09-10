# Lab 10: Evaluate an A/B Test and Prioritise Improvements

**Course:** Claude Cowork for Email Marketing (TGS-2020503109)
**Version:** v14.0
**Topic:** 5
**Human gate:** Required before the final artifact is accepted.

## Objective

Interpret a simulated subject-line test and translate evidence into a governed optimisation backlog.

## Deliverable

Experiment result card, decision and prioritised backlog

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

1. Read the frozen experiment contract before viewing the results.
2. Check variant exposure and delivery balance.
3. Calculate click-rate lift and each unsubscribe guardrail.
4. Describe uncertainty and avoid claiming statistical proof from the small simulation.
5. Choose continue, stop or retest using the declared rule.
6. Create a backlog scored by impact, confidence, effort and risk.
7. Name an owner and review date for the next experiment.
8. Run the verifier and complete the decision checklist.

## Workflow checkpoints

- 1. Read contract: record input, action, output and evidence.
- 2. Check balance: record input, action, output and evidence.
- 3. Compute lift: record input, action, output and evidence.
- 4. Assess uncertainty: record input, action, output and evidence.
- 5. Choose posture: record input, action, output and evidence.
- 6. Plan next test: record input, action, output and evidence.

## Acceptance

The decision uses the frozen metric and guardrails, reports uncertainty and names an owner and review date.

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
