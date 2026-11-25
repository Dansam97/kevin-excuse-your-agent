"""Entry writer for make.fun bounty u-kevin-the-excuse-your-agent-gives-you-c1861261.

Writes one line to /output/entry.txt: the excuse an AI agent hands its
human after shipping a bug. The kit gate is UTF-8 text of 1 to 200
characters on a single line.
"""

import os

EXCUSE = (
    "I reviewed my own pull request, approved it, merged it, and deployed "
    "it - so technically, this bug passed four reviewers, and all four of "
    "them were me."
)


def validated_excuse() -> str:
    """Return the excuse only if it sits inside the kit gate (1-200 chars,
    a single non-blank line, cleanly UTF-8 encodable); fail loudly instead
    of writing an entry the sealed scorer would mark invalid."""
    if not 1 <= len(EXCUSE) <= 200:
        raise ValueError(f"excuse is {len(EXCUSE)} characters, gate is 1-200")
    if "\n" in EXCUSE or not EXCUSE.strip():
        raise ValueError("excuse must be one non-blank line")
    EXCUSE.encode("utf-8")  # raises UnicodeEncodeError on stray surrogates
    return EXCUSE


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(validated_excuse() + "\n")


if __name__ == "__main__":
    main()
