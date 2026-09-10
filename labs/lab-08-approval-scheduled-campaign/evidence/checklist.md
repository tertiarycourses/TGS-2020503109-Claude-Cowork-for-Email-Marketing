# Evidence Checklist — Lab 08

- [ ] I used only supplied synthetic data and lab-only folder access.
- [ ] I recorded the approved source files and unresolved assumptions.
- [ ] I verified the produced artifact against the campaign objective and constraints.
- [ ] I exercised the controlled failure without a live send or destructive action.
- [ ] I ran `python3 scripts/verify_lab.py` and captured the PASS output.
- [ ] I made a PASS, REPAIR or STOP decision and named the human owner.
- [ ] I completed the cleanup and revoked temporary access.

Acceptance rule: Exactly one dry-run schedule is recorded for the approved payload; rejection, expiry and retry cases stop safely.
