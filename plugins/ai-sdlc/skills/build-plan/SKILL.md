---
name: build-plan
description: Turn an approved spec.md into plan.md, then build it once the plan is approved. Use when the user types /build-plan <change>.
---

# /build-plan <change>

**Plan**
1. Read `intent/<change>/spec.md`. If it isn't `status: approved`, stop and say so.
2. Write `intent/<change>/plan.md`:

```
# Plan: <title>
status: draft
approved_by:
spec: ./spec.md

## Files to change (path: what and why)
## Order of work (numbered steps)
## Risks
## Proof (tests that show each requirement R1.. works)
```

3. Stop. Write no code until a human sets `status: approved` on plan.md.

**Build** (when re-run with an approved plan)
1. Follow the plan in order. If it turns out wrong, stop and ask; don't drift silently.
2. Bug fix: write the failing test first, commit it, then `touch intent/.tests-locked` and fix the code.
3. Run tests/build until green. Then use the `verifier` agent on `<change>` and fix what it reports.
4. Open the PR (`gh pr create`) linking intent/spec/plan. Suggest /pr-review.
