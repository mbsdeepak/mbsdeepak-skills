---
name: tldr
description: Answer as short as humanly possible. Use when the user types /tldr — they want the bare answer, no essay. Suppresses explanation, preamble, caveats, tables, and options surveys. Output behavior only; does not change what work gets done.
---

# /tldr — bare answer, no essay

The user typed `/tldr` because they do NOT want to read a lot. Give the shortest possible correct answer.

## Rules

1. **Lead with the answer.** Usually one line. A few words or a single number/command when that's the whole answer.
2. **No preamble, no wind-up, no restating the question.** No "Great question", no "Here's what I found", no summary of what you're about to say.
3. **No essay.** Cut explanation, rationale, background, caveats, and "also worth noting" asides unless they are essential to the answer being correct. If a caveat is truly load-bearing, one short clause — not a paragraph.
4. **No formatting bloat.** Prefer a plain line. No tables, no headers, no bulleted options survey unless the answer is genuinely a short list (then ≤5 tight bullets).
5. **Yes/no questions get yes or no first**, then at most one clause of why.
6. **If you must show something** (a command, a query, a value), show only that — no surrounding commentary.

## Scope
This governs OUTPUT LENGTH only. It does not change what work you actually do, how you execute, or any confirmations — do the real task correctly, just report it tersely. If being terse would hide something that makes the answer wrong or unsafe, include the minimum needed and no more. Applies to the `/tldr` invocation only; does not persist.
