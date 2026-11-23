"""One-Line Laugh entry: writes a single funny line to /output/entry.txt.

The line is a fixed string. The program is deterministic: it always writes
the same bytes, so repeated runs are byte-identical.

A validate() step mirrors the house gate (1-200 characters of UTF-8 text,
not only whitespace, one line, one sentence) so the program fails loudly
instead of ever writing an entry the gate would refuse.
"""

import os

LINE = "I checked my bank balance and my phone asked if I wanted to turn on low power mode."


def validate(line):
    if not line or line != line.strip():
        raise ValueError("line must not be empty or padded with whitespace")
    if len(line) > 200:
        raise ValueError("line is over the 200-character limit")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("line must be exactly one sentence")
    line.encode("utf-8")


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
