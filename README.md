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

## License
MIT
