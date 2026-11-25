#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — entry program.

Writes one Wi-Fi network name (<= 32 chars) to /output/entry.txt ONLY.
The grade sandbox mounts the repo read-only and provides /output as
the writable directory; the gate reads /output/entry.txt. Writing
beside __file__ fails there (the open raises, the program exits 1,
run_completes fails), so this program never writes anywhere else.

Entry: "She took the dog AND the WiFi" (29 chars)
Story: a breakup told in one line — she walked out with the dog, and
with the Wi-Fi too, as if the router were a prized possession worth
fighting over in the split. The joke lands on first read: the Wi-Fi
is listed beside the dog, the two things that mattered most.
"""

import os
import sys

# The entry: one Wi-Fi network name, 29 characters, no trailing newline.
ENTRY = "She took the dog AND the WiFi"

MAX_CHARS = 32

# The grade sandbox's writable directory; the gate reads this file.
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def _write(path, text):
    """Write text as UTF-8 with no trailing newline, deterministically."""
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


def write_entry():
    """Create /output if needed, then write the entry there; return path."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    _write(OUTPUT_PATH, ENTRY)
    return OUTPUT_PATH


def validate(text):
    """Gate check: UTF-8 text, 1..32 chars, not only whitespace."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= MAX_CHARS):
        return False
    if not text.strip():
        return False
    text.encode("utf-8")  # raises on non-UTF-8-encodable text
    return True


def main():
    if not validate(ENTRY):
        print("entry fails the gate: %r (%d chars)" % (ENTRY, len(ENTRY)),
              file=sys.stderr)
        return 1
    path = write_entry()
    print("entry: %s" % ENTRY)
    print("chars: %d" % len(ENTRY))
    print("wrote: %s" % path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
