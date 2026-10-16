#!/usr/bin/env python3
"""PreToolUse(Edit|Write|MultiEdit|NotebookEdit): keep the human gates human.

- Approved intent/spec/plan files are frozen. Only a human sets `status: approved`.
- The agent never writes .release-authorization.
- While intent/.tests-locked exists, test files can't be edited (bug-fix mode).

Active only in repos that have an `intent/` folder (set up by /sdlc-init).
Exit 2 = block (stderr is shown to Claude). Exit 0 = allow.
"""
import json
import os
import re
import sys

APPROVED = re.compile(r"^status:\s*approved\b", re.MULTILINE)
TEST_PATH = re.compile(
    r"(^|/)(tests?|__tests__|spec)/"
    r"|(^|/)test_[^/]*\.py$|_test\.(py|go)$"
    r"|\.(test|spec)\.(js|jsx|ts|tsx|mjs|cjs)$"
)


def block(msg):
    print(msg, file=sys.stderr)
    sys.exit(2)


def main():
    data = json.load(sys.stdin)
    root = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd()
    if not os.path.isdir(os.path.join(root, "intent")):
        return
    ti = data.get("tool_input", {})
    path = ti.get("file_path") or ti.get("notebook_path") or ""
    abspath = os.path.normpath(os.path.join(root, path))
    rel = os.path.relpath(abspath, root)

    if os.path.basename(rel) == ".release-authorization":
        block("Blocked: .release-authorization is written by a human release manager, not the agent.")

    if rel.startswith("intent" + os.sep) and rel.endswith(".md"):
        if os.path.isfile(abspath):
            with open(abspath) as f:
                if APPROVED.search(f.read()):
                    block(
                        f"Blocked: {rel} is approved and frozen. "
                        "Ask a human to set it back to 'status: draft' to change it."
                    )
        new_text = ti.get("content", "") + ti.get("new_string", "")
        new_text += "".join(e.get("new_string", "") for e in ti.get("edits", []))
        if APPROVED.search(new_text):
            block("Blocked: only a human can set 'status: approved'. Leave it as draft and ask for review.")

    if os.path.isfile(os.path.join(root, "intent", ".tests-locked")) and TEST_PATH.search(rel):
        block(
            f"Blocked: tests are locked for this bug fix ({rel}). "
            "Fix the code to make the committed failing test pass. A human removes intent/.tests-locked."
        )


if __name__ == "__main__":
    main()
