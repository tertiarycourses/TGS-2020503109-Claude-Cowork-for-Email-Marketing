# Lab 09: Analyse Campaign Performance

**Course:** Claude Cowork for Email Marketing (TGS-2020503109)
**Version:** v14.0
**Topic:** 5
**Human gate:** Required at the evidence review checkpoint.

## Objective

Calculate and visualise delivery, engagement, conversion and unsubscribe metrics from mock exports.

## Deliverable

Reconciled metric table, funnel chart and diagnosis

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

1. Open the campaign export and metric dictionary.
2. Validate required columns and reconcile sent, delivered and outcome counts.
3. Calculate delivery, click, conversion and unsubscribe rates with shown denominators.
4. Create a funnel and compare campaign variants on like-for-like metrics.
5. Flag opens as a qualified signal rather than certain human attention.
6. State one observed bottleneck and one separate causal hypothesis.
7. Save the analysis JSON and chart-ready CSV.
8. Run the verifier and reconcile every reported value.

## Workflow checkpoints

- 1. Load exports: record input, action, output and evidence.
- 2. Validate schema: record input, action, output and evidence.
- 3. Reconcile totals: record input, action, output and evidence.
- 4. Calculate KPIs: record input, action, output and evidence.
- 5. Compare cohorts: record input, action, output and evidence.
- 6. Write finding: record input, action, output and evidence.

## Acceptance

All values reproduce from source rows and the finding distinguishes observation from causal hypothesis.

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
