# mbsdeepak-skills

Small Claude Code skills that don't bloat your context. Four plugins:

| Plugin | Skills |
| :-- | :-- |
| `response-style` | `/tldr` bare answer · `/eli5` explain simply · `/deep-dive` exhaustive · `/follow` take input at face value · `/socratic` teach by asking · `/critique` attack an idea · `/compare` X vs Y table · `/plan-only` plan, no edits |
| `learning` | `/quiz` from your notes · `/mock-interview hld\|lld\|dsa` · `/flashcards` → Anki CSV · `/paper` summary + reading log · `/til` lesson log |
| `dev-workflow` | `/commit` clean commit, no AI trailers · `/new-repo` scaffold · `/readme` write the README · `/handoff` where-I-left-off note |
| `ai-sdlc` | `/sdlc-init` · `/intent` · `/spec` · `/build-plan` · `/pr-review` · `/release-prep` · `/band-triage` · `verifier` agent · gate hooks |

## Install

### Option 1: Plugin (recommended)

Inside Claude Code:

```
/plugin marketplace add mbsdeepak/mbsdeepak-skills
/plugin install response-style@mbsdeepak-skills
/plugin install learning@mbsdeepak-skills
/plugin install dev-workflow@mbsdeepak-skills
/plugin install ai-sdlc@mbsdeepak-skills
```

Or run `/plugin` and pick from the marketplace. Get updates with `/plugin marketplace update mbsdeepak-skills`.
Plugin skills may appear namespaced (e.g. `/learning:quiz`) if a name clashes with one of your own.

### Option 2: Copy the skills

No plugin system needed. Copy everything, or just the folders you want:

```
git clone https://github.com/mbsdeepak/mbsdeepak-skills
cp -R mbsdeepak-skills/plugins/*/skills/* ~/.claude/skills/
```

Use `<project>/.claude/skills/` instead to scope them to one project.

### Option 3: Share with a team

Add to your project's `.claude/settings.json`. Teammates are prompted to install when they open the project:

```json
{
  "extraKnownMarketplaces": {
    "mbsdeepak-skills": {
      "source": { "source": "github", "repo": "mbsdeepak/mbsdeepak-skills" }
    }
  },
  "enabledPlugins": {
    "response-style@mbsdeepak-skills": true,
    "learning@mbsdeepak-skills": true,
    "dev-workflow@mbsdeepak-skills": true,
    "ai-sdlc@mbsdeepak-skills": true
  }
}
```

## ai-sdlc: the loop

Based on Anthropic's [AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook).
Every stage commits a file that the next stage reads; a human approves each one.

```
/intent ──► intent.md ──(human approves)──► /spec ──► spec.md ──(human approves)──►
/build-plan ──► plan.md ──(human approves)──► build + verifier ──► PR ──► /pr-review (REVIEW.md)
──(code owner merges)──► /release-prep ──(human writes .release-authorization)──► prod
──► control band breach ──► /band-triage ──► next intent.md ──► …
```

Run `/sdlc-init` once per repo. It creates `intent/`, `REVIEW.md`, `bands.yaml`, `evals/` and a CLAUDE.md section.

**Hooks** (active only in repos with an `intent/` folder; need `python3`):

| Hook | Blocks |
| :-- | :-- |
| `production-gate` | Production deploy commands unless `.release-authorization` has `authorized_by: <name>`. Override what counts as prod in `.claude/prod-patterns.txt` (one regex per line). |
| `guard-edits` | The agent setting `status: approved`, editing an approved intent/spec/plan, writing `.release-authorization`, or editing tests while `intent/.tests-locked` exists. |

Hooks catch the agent's normal file tools and obvious shell commands. They're guardrails, not a security boundary.

### Day-to-day usage

Use the loop for real changes and skip it for small ones.

**Setup, once per repo:** run `/sdlc-init`, fill in the `<...>` placeholders in `REVIEW.md` and `bands.yaml`, and commit. On a shared repo, agree on it with your team first.

**New feature or ticket**
```
/intent #142            → review intent/<change>/intent.md, set status: approved
/spec <change>          → resolve flagged concerns, approve
/build-plan <change>    → check files/order/proof, approve
/build-plan <change>    → run again: builds, runs the verifier, opens the PR
/pr-review              → fix blockers, merge
/release-prep <change>  → a human writes .release-authorization, deploys, deletes it
```
Each approval is a short read. Most of the human time goes into the spec and plan reviews, which is where the decisions get made.

**Bug fix:** same flow, but the plan says "failing test first". Claude commits the failing test and creates `intent/.tests-locked`, so it has to fix the code instead of weakening the test. A human deletes the lock after merge.

**Reviewing a PR,** even outside the loop: `/pr-review 231` gives findings ranked by severity against `REVIEW.md`.

**Alert fires:** `/band-triage p95_latency_ms 2σ "spike after 14:05 deploy"` gives a read-only diagnosis and a draft `intent.md`. Then the owner decides: fix now (continue at `/spec`), schedule it, or dismiss it. Once fixed, add a case to `evals/`.

**Skip the loop** for typos, config bumps, one-line fixes, and refactors with no behaviour change. Just use `/commit`. Rule of thumb: if you'd write a design doc or ticket for it, use the loop.

**Tips**
- Parallel work: one git worktree and one session per change.
- Pausing: `/handoff` before you stop. The `intent/<change>/` files plus `HANDOFF.md` show where you left off.
- If a command name clashes with another skill, use the full form, e.g. `/ai-sdlc:intent`.
- When `/pr-review` keeps flagging noise, add it to `REVIEW.md` under "Ignore". When it misses something, add a repo rule.
- Start with one real ticket on a low-stakes repo to find the rough edges.

## License
MIT
