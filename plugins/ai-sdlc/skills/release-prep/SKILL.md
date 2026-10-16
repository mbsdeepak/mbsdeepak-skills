---
name: release-prep
description: Prepare a merged change for release without deploying to production. Use when the user types /release-prep <change | PR #>.
---

# /release-prep <change | PR #>

1. Check: PR merged, CI green, plan.md proof tests pass. If anything fails, stop and report.
2. Write `intent/<change>/release.md`: what ships, risk, how to verify in prod, rollback steps, which metrics in bands.yaml to watch.
3. You may deploy to non-production environments if the repo has a command for it.
4. Never deploy to production and never write `.release-authorization`. Tell the user: a release manager creates `.release-authorization` with `authorized_by: <name>`, then runs (or lets you run) the prod deploy, and deletes the file afterwards.
