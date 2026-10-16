---
name: handoff
description: Write a where-I-left-off note before ending a session. Use when the user types /handoff.
---

# /handoff

Write/overwrite `HANDOFF.md` in the repo root:

```
# Handoff — YYYY-MM-DD
## Done this session
## In progress (state + exact file/line)
## Next steps (ordered)
## Gotchas / don't forget
## How to resume (commands to run)
```

Be concrete: real file paths, commands, numbers. Keep it under ~30 lines. Don't commit it unless asked.
