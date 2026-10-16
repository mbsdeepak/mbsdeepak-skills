---
name: band-triage
description: Triage a control-band breach and write the next intent.md, closing the AI-native SDLC loop. Use when the user types /band-triage <metric> <sigma> [alert details].
---

# /band-triage <metric> <sigma> [details]

Read `bands.yaml` for the metric's owner and the tier rules.

- **Tier 1 (1σ):** log only. Report it in one line and stop.
- **Tier 2 (2σ):** diagnose with read-only actions (logs, metrics, recent deploys, `git log`). Change nothing.
- **Tier 3 (3σ):** diagnose as above, then you may suggest one of: run a runbook listed in bands.yaml, or a fix that goes through the normal loop (intent → spec → plan → PR). Don't run anything without the user's OK.

For tier 2 and 3, write `intent/<change>/intent.md` (same format as /intent) with `source: band breach <metric> <sigma>`, the evidence, the likely cause, and confidence. Add a note that an eval case should be added to `evals/` once fixed.

End with the owner from bands.yaml and the choice for them: fix now, schedule, or dismiss (dismissals help tune the bands).
