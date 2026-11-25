#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes one line of famous last words, a tombstone epitaph of at most
150 characters, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Stdlib only. Deterministic: the same line on every run.
"""

import os

ENTRY = "I died as I lived: mid-sentence, interrupting someone, and absolutely right."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
