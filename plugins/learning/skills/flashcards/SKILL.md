---
name: flashcards
description: Turn a doc into Anki flashcards. Use when the user types /flashcards <doc> — writes a Q/A CSV ready for Anki import.
---

# /flashcards <doc>

- Read the doc. Make one card per atomic fact, definition, trade-off, or "why".
- Short questions; answers under ~25 words. No duplicate cards.
- Write `<doc-name>.flashcards.csv` next to the doc: two columns `question,answer`, no header, properly quoted.
- Report the path and card count. Anki: File → Import, comma separator.
