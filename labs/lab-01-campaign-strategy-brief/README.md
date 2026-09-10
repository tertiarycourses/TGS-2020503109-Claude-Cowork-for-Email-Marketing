# Lab 01: Build a Grounded Campaign Strategy Brief

**Course:** Claude Cowork for Email Marketing (TGS-2020503109)
**Version:** v14.0
**Topic:** 1
**Human gate:** Required before the final artifact is accepted.

## Objective

Use Claude Cowork with supplied brand and market evidence to propose a consent-aware email strategy for Northstar Fitness.

## Deliverable

Validated strategy brief, channel matrix and assumption log

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

1. Open the Cowork workspace and create a new project named `Northstar Strategy Lab`.
2. Grant folder access only to this lab.
3. Ask Claude to inventory the three mock-data files without drafting.
4. Open `starter/campaign-brief.json` and note every required field.
5. Submit the bounded prompt from `prompt.md`.
6. Review the proposed objective tree and reject any unsupported market claim.
7. Ask Claude to save the completed brief in `solution/campaign-brief.json`.
8. Run the verifier and repair any missing objective, audience, metric, guardrail or source reference.

## Workflow checkpoints

- 1. Open project: record input, action, output and evidence.
- 2. Read evidence: record input, action, output and evidence.
- 3. Frame objective: record input, action, output and evidence.
- 4. Score channel: record input, action, output and evidence.
- 5. Set metrics: record input, action, output and evidence.
- 6. Review brief: record input, action, output and evidence.

## Acceptance

One primary objective, audience, value exchange, metrics, guardrails and source-backed assumptions are explicit.

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
