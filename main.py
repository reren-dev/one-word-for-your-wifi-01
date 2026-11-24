#!/usr/bin/env python3
"""One Word for Your Wi-Fi — entry program.

Writes a single word describing the entrant's Wi-Fi to entry.txt.
Standard library only: no network, no wall clock, no randomness.
"""

import os
import sys

# The word. v2 (revision): "Ghosted" — the Wi-Fi vanishes mid-sentence
# with no explanation, like being ghosted. Funnier and fresher than v1's
# "Flaky": it names the exact lived experience (signal there one second,
# gone the next, no goodbye), lands instantly, and works as a network name.
WORD = "Ghosted"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate(word):
    """The gate allows UTF-8 text of 1 to 20 characters, not only whitespace."""
    if not isinstance(word, str):
        raise ValueError("word must be a string")
    if not word or not word.strip():
        raise ValueError("word must not be empty")
    if len(word) > 20:
        raise ValueError("word must be at most 20 characters")
    if len(word.split()) != 1:
        raise ValueError("word must be exactly one word")
    if not word.isalpha():
        raise ValueError("word must be letters only")
    return word


def main():
    word = validate(WORD)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)
    os.replace(tmp_path, OUTPUT_PATH)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != word:
        raise RuntimeError("verification failed: entry.txt does not match")
    print(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())
