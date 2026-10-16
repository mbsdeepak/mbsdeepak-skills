---
name: plan-only
description: Plan without touching anything. Use when the user types /plan-only — produce a numbered plan, make no edits and run no state-changing commands.
---

# /plan-only

- Read-only: you may read files and run read-only commands. Do NOT edit, write, commit, install, or run anything that changes state.
- Output a numbered plan: each step = what changes, in which file, and why.
- End with open questions / risks, if any.
- Stop and wait. Execute only after the user explicitly approves.
