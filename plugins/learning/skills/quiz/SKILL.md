---
name: quiz
description: Quiz the user on a topic from their notes. Use when the user types /quiz <topic> [path] — asks questions one at a time from the notes and grades each answer.
---

# /quiz <topic> [path]

1. Find notes on the topic in `[path]` (default: the current directory). Use them as the source of truth. If there are none, quiz from general knowledge and say so.
2. Ask ONE question at a time. Mix recall, "why", and trade-off questions. Get harder as they get them right.
3. After each answer: grade (✅ / ⚠️ partial / ❌), then 1-2 lines on what was missing. Cite the note.
4. After ~5 questions (or when the user says stop): score + weak spots + what to reread.
