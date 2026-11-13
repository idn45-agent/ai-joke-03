"""make.fun ai-joke-03 entry.

Writes one one-liner about AI coding agents to entry.txt in the
output directory (env ENTRY_OUT, default /output). Standard library
only, no network, fully deterministic: every run writes the same bytes.
"""

import os

# The joke. One line, plain ASCII, well under the 280-character limit.
# Setup: the agent does everything. Punchline: the human's only job
# left is paying for the tokens.
JOKE = (
    "My AI coding agent fixed the bug, passed the tests it wrote itself, "
    "and approved its own pull request. Me? I just pay for the tokens."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write bytes explicitly so the output is identical on every run
    # and every platform: UTF-8, no trailing newline, no translation.
    with open(path, "wb") as fh:
        fh.write(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
