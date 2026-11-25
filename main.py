#!/usr/bin/env python3
"""The Most Shameless Lie - variant A.

Deterministic, no network, no secrets. Writes the entry text to
/output/entry.txt FIRST, then (best effort) a repo-root copy.
The grader sandbox is read-only, so the repo-root copy is wrapped
in try/except and must never crash the run.
"""

import os

ENTRY = "I read the terms twice."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
