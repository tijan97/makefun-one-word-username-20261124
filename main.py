"""One Word, One Username, One Reward — make.fun entry.

Writes the entrant's own make.fun username, one word and nothing else,
to the output file the grader reads.
"""

import os

USERNAME = "bright-condor-94"


def validate(text: str) -> None:
    """Enforce the competition gate: 1-30 chars, a single word, no padding."""
    if not 1 <= len(text) <= 30:
        raise ValueError(f"username must be 1-30 characters, got {len(text)}")
    if not text.strip() or text != text.strip():
        raise ValueError("username must not be blank or padded with whitespace")
    if any(ch.isspace() for ch in text):
        raise ValueError("username must be a single word with no spaces")


def main() -> None:
    validate(USERNAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(USERNAME)
    # Read back and confirm what was written is exactly the entry.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    validate(written)
    if written != USERNAME:
        raise ValueError("written entry does not match the username")
    print(f"entry: {USERNAME}")


if __name__ == "__main__":
    main()
