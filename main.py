#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a quiet scene that slows
the reader down, no instructions, no wellness stock phrases. Pure
stdlib, no network, fully deterministic.
"""

import os

TEXT = (
    "Somewhere a small lamp is still on in a kitchen, and no one is "
    "waiting for you to hurry. The kettle has gone quiet. Your hands "
    "are warm and empty, and that is enough. The night is patient, "
    "and nothing here needs proving."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
