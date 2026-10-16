#!/usr/bin/env python3
"""PreToolUse(Bash): block production deploys without a named release authorization.

Active only in repos that have an `intent/` folder (set up by /sdlc-init).
Exit 2 = block (stderr is shown to Claude). Exit 0 = allow.
"""
import json
import os
import re
import sys

DEFAULT_PATTERNS = [
    r"\b(deploy|release|promote|rollout)\b.*\b(prod|production)\b",
    r"\b(prod|production)\b.*\b(deploy|release|promote|rollout)\b",
    r"--env(ironment)?[= ](prod|production)\b",
    r"\bkubectl\b.*--context[= ]\S*prod",
    r"\bhelm\s+(upgrade|install)\b.*\bprod",
    r"\bterraform\s+apply\b.*\bprod",
]
AUTH_FILE = ".release-authorization"
TESTS_LOCK = "intent/.tests-locked"
WRITE_OPS = r"(\brm\b|\bmv\b|\bcp\b|\bunlink\b|\btouch\b|\btee\b|\bsed\b|\becho\b|\bprintf\b|>)"


def block(msg):
    print(msg, file=sys.stderr)
    sys.exit(2)


def main():
    data = json.load(sys.stdin)
    root = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd()
    if not os.path.isdir(os.path.join(root, "intent")):
        return
    cmd = data.get("tool_input", {}).get("command", "")

    # Gate files are for humans only.
    if AUTH_FILE in cmd and re.search(WRITE_OPS, cmd):
        block(f"Blocked: {AUTH_FILE} is written by a human release manager, not the agent.")
    if ".tests-locked" in cmd and re.search(r"(\brm\b|\bmv\b|\bunlink\b|>)", cmd):
        block(f"Blocked: {TESTS_LOCK} can only be removed by a human.")

    if re.match(r"\s*git\s", cmd):
        return
    patterns_file = os.path.join(root, ".claude", "prod-patterns.txt")
    if os.path.isfile(patterns_file):
        with open(patterns_file) as f:
            patterns = [l.strip() for l in f if l.strip() and not l.startswith("#")]
    else:
        patterns = DEFAULT_PATTERNS
    if not any(re.search(p, cmd, re.IGNORECASE) for p in patterns):
        return

    auth = os.path.join(root, AUTH_FILE)
    if os.path.isfile(auth):
        with open(auth) as f:
            m = re.search(r"^authorized_by:\s*(\S.*)$", f.read(), re.MULTILINE)
        if m:
            return
    block(
        "Blocked: production deploy needs a named release authorization. "
        f"A human must create {AUTH_FILE} with 'authorized_by: <name>'. "
        "Prepare the release with /release-prep and stop."
    )


if __name__ == "__main__":
    main()
