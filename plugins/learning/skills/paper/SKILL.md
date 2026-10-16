---
name: paper
description: Summarize a research paper and log it. Use when the user types /paper <url | pdf path>.
---

# /paper <url | path>

Read the paper, then output:

- **Problem:** 1-2 lines
- **Method:** 3-5 bullets, the core idea only
- **Key result:** numbers, plus what they compared against
- **Limits:** what it doesn't show / assumptions
- **Worth trying:** one concrete idea or experiment it suggests

Then append one entry to `READING.md` in the current directory (create it if missing):
`- YYYY-MM-DD — [Title](link) — one-line takeaway`
