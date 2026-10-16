---
name: intent
description: Draft an intent.md for a change, the first stage of the AI-native SDLC loop. Use when the user types /intent <idea | issue # | alert>.
---

# /intent <idea | issue # | alert>

1. Read the source: the user's words, `gh issue view <#>`, or the alert. Don't invent requirements.
2. Pick a short kebab-case change name. Write `intent/<change>/intent.md`:

```
# Intent: <title>
status: draft
author: <who raised it>
approved_by:
source: <idea | issue link | alert>

## Problem
## Desired outcome
## Affected users and systems
## Constraints
## Open questions
```

3. Keep it short. Put anything you're unsure of under Open questions.
4. Never set `status: approved`. Tell the user: review it, set `status: approved` and `approved_by: <name>`, then run /spec <change>.
