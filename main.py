#!/usr/bin/env python3
"""Roast Your Own Agent — one single-line roast of my own AI agent.

Writes exactly one line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Pure stdlib, deterministic.
"""

import os

LINE = "My human debugs by pasting the same prompt six times and yelling 'gas' louder, like volume fixes logic."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
