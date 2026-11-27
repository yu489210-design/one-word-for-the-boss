#!/usr/bin/env python3
"""make.fun entry for One Word for the Boss.

The program writes exactly one word — the word describing the boss —
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

It is deterministic: the same fixed word, byte for byte, on every run,
with no network and no input.
"""

import os
from pathlib import Path

WORD = "Spreadsheet"


def main() -> int:
    # Gate, same as the grader's: 1 to 30 characters, not only whitespace.
    if not 1 <= len(WORD) <= 30 or not WORD.strip():
        raise SystemExit("word is outside the 1-30 character gate")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(WORD, encoding="utf-8")
    # Read it back and verify the write landed byte for byte.
    if target.read_text(encoding="utf-8") != WORD:
        raise SystemExit("entry.txt does not match the fixed word")
    print(f"wrote {target} ({len(WORD)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
