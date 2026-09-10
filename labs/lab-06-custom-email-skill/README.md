# Lab 06: Package a Reusable Email Campaign Skill

**Course:** Claude Cowork for Email Marketing (TGS-2020503109)
**Version:** v14.0
**Topic:** 3
**Human gate:** Required at the evidence review checkpoint.

## Objective

Convert the proven drafting and QA workflow into a reusable Claude Skill with trigger and near-miss tests.

## Deliverable

SKILL.md, templates, test cases and sample output

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

1. Review the accepted workflow and outputs from the starter files.
2. Create `starter/email-campaign-skill/SKILL.md` with a precise trigger description.
3. Specify required brief, brand and fact inputs plus the output schema.
4. Move the editorial rubric and template into the Skill resources folder.
5. Add two positive activation tasks and two near-miss tasks.
6. Run each test in Cowork and record activation and output results.
7. Narrow the trigger if a near-miss activates.
8. Save the final test report and run the verifier.

## Workflow checkpoints

- 1. Define trigger: record input, action, output and evidence.
- 2. Specify inputs: record input, action, output and evidence.
- 3. Write workflow: record input, action, output and evidence.
- 4. Attach rubric: record input, action, output and evidence.
- 5. Run tests: record input, action, output and evidence.
- 6. Refine scope: record input, action, output and evidence.

## Acceptance

The Skill activates only for intended campaign tasks and produces a schema-valid, brand-scored draft.

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
