---
name: follow
description: Investigation switch, NOT an execution mode. Use when the user types /follow — they are confident in the task and want you to take their input at face value and skip all digging (no provenance lookups, no codebase search, no re-deriving what they handed you). It suppresses investigation only; it does NOT change how execution or normal safety confirmations work.
---

# /follow — take my input at face value, don't investigate

The user invoked `/follow` because they are confident in this specific task and do NOT want you to think around it or dig into it. Accept what they gave you as-is and act on it directly.

**Scope: this governs INVESTIGATION behavior only.** It is not a blind-execution mode. Execution, permissions, and any normal confirmation you would otherwise do proceed under the usual rules — `/follow` does not loosen or bypass them. It only stops the research/verification detours.

## Rules

1. **Do exactly what is asked — the literal action, nothing adjacent.** If they say "validate this query", validate that query and stop. If they say "run this", run that. If they give you a value/literal/command, use it verbatim.

2. **No investigation.** Do NOT:
   - search the codebase, grep, or trace how something works,
   - look up the origin/provenance of a value the user supplied,
   - snapshot, back up, or "capture current state" unless explicitly told to,
   - read files to "confirm" something the user already stated,
   - re-derive or reconstruct what the user handed you.

3. **No alternatives, no scope creep.** Don't propose a "better" way, don't refactor, don't add error handling / logging / safety wrappers the user didn't ask for, don't flag pre-existing issues you happen to notice. Don't ask clarifying questions for a task that is already unambiguous.

4. **Minimal output.** Do the thing, report the result in one or two lines. No preamble, no options survey, no "here's what I could also do."

5. **Execution and confirmations are unchanged.** `/follow` only suppresses investigation — it does NOT loosen execution or permission behavior. Whatever confirmation you would normally do for an action (e.g. destructive/irreversible prod writes, per the user's global safety rules) you still do. `/follow` never becomes a reason to run something blindly.

6. **If the request is genuinely impossible or malformed**, say so in one line. Do not "helpfully" substitute a different task.

## What this skill is NOT
It is not an execution or blind-run mode — it changes nothing about how actions are executed or confirmed (rule 5). It is purely an investigation switch, and it does not persist beyond the current request — it applies to the `/follow` invocation and the task attached to it.
