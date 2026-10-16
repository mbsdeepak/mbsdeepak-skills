---
name: new-repo
description: Scaffold a new git repo. Use when the user types /new-repo <name> [description].
---

# /new-repo <name> [description]

1. Create `<name>/` in the current directory (stop if it exists) and run `git init -b main`.
2. Show `git config user.name` / `user.email` and ask if that's the right identity for this repo. If not, set it with `git config --local`.
3. Add a short `README.md` (title + one-line description) and a `.gitignore` for the likely language.
4. Initial commit: `Initial commit` (no attribution trailers).
5. Ask before creating a remote. If yes, ask public or private, then `gh repo create <name> --<visibility> --source . --remote origin --push`.
