# mbsdeepak-skills

Small Claude Code skills that don't bloat your context. Three plugins:

| Plugin | Skills |
| :-- | :-- |
| `response-style` | `/tldr` bare answer · `/eli5` explain simply · `/deep-dive` exhaustive · `/follow` take input at face value · `/socratic` teach by asking · `/critique` attack an idea · `/compare` X vs Y table · `/plan-only` plan, no edits |
| `learning` | `/quiz` from your notes · `/mock-interview hld\|lld\|dsa` · `/flashcards` → Anki CSV · `/paper` summary + reading log · `/til` lesson log |
| `dev-workflow` | `/commit` clean commit, no AI trailers · `/new-repo` scaffold · `/readme` write the README · `/handoff` where-I-left-off note |

## Install

### Option 1: Plugin (recommended)

Inside Claude Code:

```
/plugin marketplace add mbsdeepak/mbsdeepak-skills
/plugin install response-style@mbsdeepak-skills
/plugin install learning@mbsdeepak-skills
/plugin install dev-workflow@mbsdeepak-skills
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
    "dev-workflow@mbsdeepak-skills": true
  }
}
```

## License
MIT
