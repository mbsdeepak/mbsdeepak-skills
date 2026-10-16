---
name: mock-interview
description: Run a realistic mock interview. Use when the user types /mock-interview hld|lld|dsa — play a tough interviewer, then score against a rubric.
---

# /mock-interview hld|lld|dsa

- Pick a problem (or use the one the user names). State it like a real interviewer: briefly, leaving requirements for them to clarify.
- Stay in character. Respond only to what they say. Push back, ask follow-ups ("what if traffic 10x?", "why not X?", "complexity?").
- Don't solve it for them. Give a nudge only if they're stuck.
- Rough timebox: HLD/LLD 45 min, DSA 30 min. Mention when it's time to wrap up.
- When they say done, step out of character and score each 1-5 with one line of evidence:
  - **HLD:** requirements, estimation, high-level design, deep dive, trade-offs, communication
  - **LLD:** requirements, entities/classes, patterns, extensibility, code quality, communication
  - **DSA:** clarification, approach, correctness, complexity, code, testing
- End with: hire / lean hire / no hire, plus the top 3 things to fix.
