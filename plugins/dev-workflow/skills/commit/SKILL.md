---
name: commit
description: Make a clean, focused git commit. Use when the user types /commit — stages only related files and writes a good message with no AI attribution trailers.
---

# /commit

1. Look at `git status` + `git diff`. Stage only the files related to this change; never stage secrets, .env, or large binaries.
2. Match the repo's existing message style (check `git log --oneline -10`). Default: imperative subject ≤ 72 chars; body only if the "why" isn't obvious.
3. No Co-Authored-By / "Generated with" / any attribution trailer.
4. Commit with the repo's configured identity, then show `git log -1 --oneline`.
5. Don't push unless asked.
