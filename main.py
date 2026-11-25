#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — entry program.

Writes one Wi-Fi network name (<= 32 chars) to entry.txt next to this
file, and also to /output/entry.txt when that sandbox output directory
is available (the grader's gate reads /output/entry.txt).

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

def _write(path, text):
    """Write text as UTF-8 with no trailing newline, deterministically."""
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


def _output_paths():
    """entry.txt beside this file, plus the grader's /output/entry.txt.

    The shared local /output is only touched when it does not already
    hold somebody else's entry: if /output/entry.txt exists with
    different bytes, leave it alone (another builder is using it).
    In the grader sandbox /output is private to this run, so the
    write lands there as the gate expects.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    paths = [os.path.join(here, "entry.txt")]
    shared = "/output/entry.txt"
    try:
        if os.path.isdir("/output"):
            if not os.path.exists(shared):
                paths.append(shared)
            else:
                with open(shared, "rb") as fh:
                    if fh.read() == ENTRY.encode("utf-8"):
                        paths.append(shared)
    except OSError:
        pass
    return paths


def write_entry():
    """Write the entry to every output path; return the paths written."""
    written = []
    for path in _output_paths():
        _write(path, ENTRY)
        written.append(path)
    return written


MAX_CHARS = 32


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
    written = write_entry()
    print("entry: %s" % ENTRY)
    print("chars: %d" % len(ENTRY))
    for path in written:
        print("wrote: %s" % path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
