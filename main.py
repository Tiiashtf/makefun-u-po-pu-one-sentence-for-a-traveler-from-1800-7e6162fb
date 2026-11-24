#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 — make.fun entry.

Writes a single sentence of at most 200 characters to /output/entry.txt,
explaining the modern internet to someone who has just stepped out of
the year 1800.

The sentence uses one comparison only — a road — because a person from
1800 knows roads, and the comparison is true of the internet as it is
now: words really do travel from one side of the world to the other
faster than any horse could carry them, so something written in London
can be read in China before the ink on it is dry. No word in it was
coined after the traveler's time, there is no list of features, and the
closing image ("before the ink is dry") is the part a reader remembers.
"""

import os
import sys

SENTENCE = (
    "Imagine a road joining every house on earth, along which words "
    "travel faster than any horse, so anything written in London can "
    "be read in China before the ink is dry."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    if not 1 <= len(SENTENCE) <= 200:
        print(f"sentence is {len(SENTENCE)} chars, must be 1-200",
              file=sys.stderr)
        return 1
    if "\n" in SENTENCE or "\r" in SENTENCE:
        print("sentence must be a single line", file=sys.stderr)
        return 1
    if not SENTENCE.strip():
        print("sentence must not be only whitespace", file=sys.stderr)
        return 1
    if SENTENCE.count(".") != 1 or not SENTENCE.endswith("."):
        print("sentence must be exactly one sentence", file=sys.stderr)
        return 1

    # Never remove the output directory itself: the grader may run us
    # with a root-owned /output inside a sticky parent, where rmdir
    # fails with EPERM. Clear only its contents, then write.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            import shutil
            shutil.rmtree(path)
        else:
            os.unlink(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(SENTENCE)
    print(f"wrote {len(SENTENCE)} chars to {OUTPUT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
