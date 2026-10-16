---
name: spec
description: Turn an approved intent.md into spec.md (requirements + design). Use when the user types /spec <change>.
---

# /spec <change>

1. Read `intent/<change>/intent.md`. If it isn't `status: approved`, stop and say so.
2. Read the relevant code, CLAUDE.md, and any policy skills (security, compliance, UX) the repo has.
3. Write `intent/<change>/spec.md`:

```
# Spec: <title>
status: draft
approved_by:
intent: ./intent.md

## Requirements
- R1 ... (testable, numbered)
## Out of scope
## Design (components, data, APIs, key decisions + why)
## Risks
## Flagged concerns (policy conflicts, security, open decisions; who should resolve each)
```

4. Flag concerns instead of silently deciding them. Never set `status: approved`; tell the user to approve it (with a tech lead for risky work), then run /build-plan <change>.
