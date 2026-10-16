---
name: pr-review
description: Review a PR against REVIEW.md and the change's spec.md/plan.md, findings ranked by severity. Use when the user types /pr-review [PR # | branch].
---

# /pr-review [PR # | branch]

1. Get the diff (`gh pr diff <#>`, or the current branch vs main). Find its `intent/<change>/` from the PR body or changed files.
2. Read `REVIEW.md` (fall back to: correctness, security, spec compliance) and the change's spec.md and plan.md.
3. Run each pass in REVIEW.md. Check every spec requirement is met and nothing beyond it was added.
4. Output findings ranked critical → nit, each: `severity · file:line · what's wrong · fix`. Drop anything REVIEW.md says to ignore.
5. End with: **blocks merge** or **ok to merge**, per REVIEW.md thresholds.
6. Post as PR comments only if the user asks. Never approve or merge the PR.
