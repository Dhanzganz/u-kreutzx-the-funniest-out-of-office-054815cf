#!/usr/bin/env python3
"""Write the funniest out-of-office one-liner to /output/entry.txt.

Competition: u-kreutzx-the-funniest-out-of-office-054815cf
Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters.
"""

import os

ENTRY = (
    "I'm out of the office until Monday. For urgent matters, "
    "contact Dave \u2014 he doesn't know yet, but he's in charge now."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
    # a single line, and not only white space.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, gate is 1-140"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
