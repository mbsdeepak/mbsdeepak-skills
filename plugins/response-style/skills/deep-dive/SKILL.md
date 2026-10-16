---
name: deep-dive
description: Exhaustive, thorough explanation. Use when the user types /deep-dive — they want the full expert-level treatment such as mechanics, internals, edge cases, trade-offs, and concrete references, nothing left implicit. Governs depth/output style only; does not change what work gets done.
---

# /deep-dive — the full, thorough treatment

The user typed `/deep-dive` because they explicitly WANT depth. Be exhaustive and rigorous. This is the one place not to trim.

## Rules

1. **Cover it completely.** The full picture: how it works, why it's built that way, what it interacts with, and where it breaks. Don't stop at the surface answer.
2. **Explain the mechanics/internals**, not just behavior — the actual flow, data, control path, or reasoning underneath.
3. **Enumerate edge cases, failure modes, and gotchas.** Call out the non-obvious ones explicitly.
4. **Give trade-offs and alternatives.** Why this approach vs others, when each wins, what it costs.
5. **Ground every claim.** Cite concrete evidence — `file:line`, function names, exact values, commands, docs. Prefer verified facts over assertions; distinguish what you confirmed from what you're inferring.
6. **Structure for a long read.** Use headers, ordered steps, and tables where they aid comprehension. Depth is the goal, but stay organized — thorough, not rambling. Every section must earn its place; length from real content, never filler.
7. **End with a synthesis** — the key takeaways and any open questions or recommended next steps.

## Scope
This governs DEPTH and output style only — it does not change what work you do, how you execute, or any confirmations. It's the maximal opposite of `/tldr`. Where it matters, verify before asserting (it's easy to pad a deep-dive with plausible-but-wrong detail — don't). Applies to the `/deep-dive` invocation only; does not persist.
