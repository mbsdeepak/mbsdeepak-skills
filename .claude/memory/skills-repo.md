---
name: skills-repo
description: Two skill repos — ~/projects/skills (public-ready generic plugin marketplace) and ~/projects/personal-skills (mbsdeepak-specific, symlinked into ~/.claude/skills); both local git only
metadata:
  type: project
---

Set up 2026-10-16. `~/projects/skills` is pushed to **github.com/mbsdeepak/mbsdeepak-skills** (public, tag v0.1.0, Verified); marketplace name `mbsdeepak-skills`, installed from GitHub. personal-skills is still local only. Submitting to Anthropic directory (clau.de/plugin-directory-submission) must be done by the user signed in as mbsdeepak3@gmail.com, NOT the amnic work account.

- `~/projects/skills`: Claude Code **plugin marketplace** named `mbsdeepak-skills`, MIT. Plugins (v0.2.0): `ai-sdlc` (sdlc-init, intent, spec, build-plan, pr-review, release-prep, band-triage + verifier agent + python3 hooks production-gate/guard-edits, active only in repos with `intent/`; based on Anthropic AI-native SDLC playbook), `response-style` (tldr, eli5, deep-dive, follow, socratic, critique, compare, plan-only), `learning` (quiz, mock-interview, flashcards, paper, til), `dev-workflow` (commit, new-repo, readme, handoff). Added via `claude plugin marketplace add mbsdeepak/mbsdeepak-skills` and all 3 installed at user scope. Nothing personal in it apart from the author field. Check it with `claude plugin validate .`.
- `~/projects/personal-skills`: commit, new-repo, quiz, paper, til (versions with personal paths and identity), plus slack-message and resume-ats-eval. `install.sh` symlinks them into `~/.claude/skills`. Plain `/commit` etc. resolve to these; the plugin versions are reached as `/dev-workflow:commit`.
- The original global copies were moved to `~/.claude/skills/.trash/2026-10-16-moved-to-repos/`. The amnic-*, gitnexus-* and synced skills were left alone.
- resume-ats-eval stays personal until the HackerRank rubric's license is checked.

**Why:** user wants generic skills publishable to a marketplace, kept simple ("don't bloat them up").
**How to apply:** keep every skill short. Add generic skills to the marketplace repo and anything that uses the user's paths or identity to personal-skills. Verify signing with `git cat-file -p HEAD | grep "BEGIN SSH SIGNATURE"` (`--show-signature` fails locally). See [[personal-github-identity]].
