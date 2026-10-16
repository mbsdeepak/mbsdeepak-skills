---
name: sdlc-init
description: Set up the AI-native SDLC loop in the current repo. Use when the user types /sdlc-init — creates intent/, REVIEW.md, bands.yaml, evals/ and a CLAUDE.md section.
---

# /sdlc-init

Copy from the `templates/` folder next to this SKILL.md. Never overwrite an existing file; report it as skipped.

1. `intent/` with an empty `.gitkeep`. This folder also switches on the plugin's gate hooks for this repo.
2. `REVIEW.md` ← `templates/REVIEW.md`
3. `bands.yaml` ← `templates/bands.yaml`
4. `evals/README.md` ← `templates/evals-README.md`
5. Append `templates/CLAUDE-sdlc.md` to `CLAUDE.md` (create it if missing; skip if the section is already there).
6. Optional, only if the user's deploy commands don't match the defaults: `.claude/prod-patterns.txt`, one regex per line, for commands that count as production deploys.

Then list what was created and tell the user to fill in the `<...>` placeholders in REVIEW.md and bands.yaml. Don't commit unless asked.
