# Review policy

Used by /pr-review and by human reviewers. Edit freely.

## Passes
1. Correctness: logic bugs, edge cases, error handling
2. Security: authn/authz, injection, secrets, PII in logs
3. Spec compliance: does the diff do what spec.md says, and only that? Does it follow plan.md?

## Severity
- critical: data loss, security hole, prod outage risk → blocks merge
- major: wrong behaviour, missing tests for new logic → blocks merge
- minor: unclear naming, small inefficiency → comment only
- nit: style → skip (the linter handles it)

## Repo rules
- <add rules a generic reviewer wouldn't know>

## Ignore
- Generated files, lockfiles, vendored code
