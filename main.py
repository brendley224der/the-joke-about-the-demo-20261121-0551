#!/usr/bin/env python3
"""Write one joke about working beside AI coding agents.

The joke is a single line, written to /output/entry.txt (or to the
directory named by ENTRY_OUTPUT_DIR when run outside the sandbox).
Pure standard library only; the output is fully deterministic, and
the text is held to the competition's own gate before it is written.
"""

import os
import sys

JOKE = (
    "My AI coding agent demoed the app live, fixed a bug mid-sentence, "
    "then thanked the audience for not noticing it had written the bug itself."
)

MAX_CHARS = 280


def validate(text):
    """Return the gate verdict for a candidate entry text."""
    if not text or text != text.strip():
        return "text must not be empty or padded with whitespace"
    if len(text) > MAX_CHARS:
        return "text is longer than %d characters" % MAX_CHARS
    return None


def write_entry(text, out_dir):
    """Write the validated text to <out_dir>/entry.txt as UTF-8."""
    problem = validate(text)
    if problem is not None:
        print("gate: " + problem, file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("wrote %s (%d characters)" % (path, len(text)))
    return 0


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    return write_entry(JOKE.strip(), out_dir)


if __name__ == "__main__":
    raise SystemExit(main())
