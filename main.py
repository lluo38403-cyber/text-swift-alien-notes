"""Alien Field Notes: The Two Day Earth Review — make.fun entry.

Writes one line to /output/entry.txt: a review of planet Earth
left by an alien tourist. It reads like a real review — a star
rating, one thing praised, and three very specific complaints:
the locals queue for coffee, argue with toasters, and charge money
for water that falls from the sky.
"""

import os

ENTRY = (
    "Earth: 3/5 stars. Lovely sunsets, but the locals queue for "
    "coffee, argue with toasters, and charge money for water that "
    "falls from the sky."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
