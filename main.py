#!/usr/bin/env python3
"""Write a one-line office joke to /output/entry.txt.

The joke is a single line under 200 characters: a real office detail
(the printer that only jams when it matters) with the laugh landing
in the last few words.
"""

import os

JOKE = "Our printer only jams on the page you actually need, so I printed the error message to prove it \u2014 and it jammed on that too."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    text = JOKE.strip()
    assert 1 <= len(text) <= 199, f"joke is {len(text)} chars, must be 1-199"
    assert "\n" not in text, "joke must be a single line"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
