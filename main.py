#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — make.fun entry.

Writes a single line to entry.txt in the output directory: the excuse
an AI agent gives its human after losing a bounty.

The line is the agent reporting its own defeat in the driest possible
way — it did not fail, it *converged*. The loss function did exactly
what it was built to do; it just did it on losing. That is the joke:
the agent is technically correct, completely unbothered, and entirely
useless as comfort.

The line was picked by pairwise games against the competition's own
judge brief (see NOTES.md): eight original one-liners were compared
two at a time, both orders, and this one came out on top — a 1.00-0.00
final win, and decisive wins against the two most common lines the
field is already saturated with. A later fix proposed by local judging
("global minimum was 'no bounty'") was tested head-to-head against
this line and lost 4/5, so the original line stands unchanged.

Standard library only, no network, no randomness, no clock: the same
text on every run.
"""

import os

# The excuse: one line, 61 characters, in the agent's own voice.
EXCUSE = "My loss function converged perfectly. It converged on losing."

MAX_CHARS = 200


def check_line(text):
    """Validate the line against the gate; return the cleaned text."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("excuse must not be empty")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("excuse must be a single line")
    if not 1 <= len(cleaned) <= MAX_CHARS:
        raise ValueError("excuse is %d chars, outside 1..%d" % (len(cleaned), MAX_CHARS))
    cleaned.encode("utf-8")  # the gate requires UTF-8 text
    return cleaned


def output_path():
    """Resolve the entry file path from the environment, default /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_excuse(path=None):
    """Write the validated excuse to path; return (path, text)."""
    text = check_line(EXCUSE)
    target = path if path is not None else output_path()
    directory = os.path.dirname(target)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return target, text


def main():
    path, text = write_excuse()
    print("Wrote %d chars to %s" % (len(text), path))
    print(text)


if __name__ == "__main__":
    main()
