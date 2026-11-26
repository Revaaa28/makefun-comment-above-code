#!/usr/bin/env python3
"""The Comment Above the Code — make.fun entry.

Writes one line, at most 200 characters, as the comment a developer left
above fragile production code, to /output/entry.txt.
"""

import os

LINE = "// Do not delete. The tests pass only because this function exists. The tests do not test this function."
EXPECTED_LEN = 104


def validate_entry(text: str) -> None:
    """Gate: UTF-8 text of 1 to 200 characters, not whitespace-only, one line."""
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be whitespace-only"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) == EXPECTED_LEN, f"expected {EXPECTED_LEN} chars, got {len(text)}"


def main() -> None:
    validate_entry(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verify: what the grader reads must be byte-identical.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == LINE, "read-back mismatch"


if __name__ == "__main__":
    main()
