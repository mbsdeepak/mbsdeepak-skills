
## Change workflow (AI-native SDLC)
Every change lives in `intent/<change>/`: intent.md → spec.md → plan.md → PR → release.
- Only a human sets `status: approved`. Don't start a stage until the previous file is approved.
- Bug fixes: commit a failing test first, then `touch intent/.tests-locked`.
- Never deploy to production. /release-prep prepares; a human writes `.release-authorization`.
- PR reviews follow REVIEW.md. Every incident adds a case to evals/.
