#!/usr/bin/env python3
"""One-Line Roast entry: writes a single roast line to /output/entry.txt.

The roast targets a gadget used every day: the robot vacuum that has
mapped the whole apartment yet still attacks the same chair leg.
"""

import os

ROAST = (
    "My robot vacuum has a perfect map of my apartment and still "
    "body-slams the same chair leg every morning \u2014 it doesn't clean "
    "my floors, it settles scores."
)


def main():
    text = ROAST.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"roast must be 1-200 characters, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
