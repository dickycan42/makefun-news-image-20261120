# SPDX-License-Identifier: MIT
"""Deliver the finished front page to the folder the grader reads.

The artwork for this entry is the file entry.png sitting next to this
script: a newspaper front page that rounds up the world news of Friday
20 November 2026. Running this script places an exact copy of that file
at <destination>/entry.png, where <destination> comes from the
MAKEFUN_OUTPUT_DIR environment variable, falling back to /output when
the variable is absent or empty.

Only the Python 3.13 standard library is involved. Nothing is fetched
from the network, no clock is consulted, and nothing outside this
repository is read, so every run produces an identical copy.
"""

import hashlib
import os
import sys
from pathlib import Path

PICTURE_FILENAME = "entry.png"
OUTPUT_ENV_VAR = "MAKEFUN_OUTPUT_DIR"
FALLBACK_DESTINATION = "/output"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def pick_destination() -> Path:
    """Decide where the copy belongs, honouring the environment first."""
    requested = os.environ.get(OUTPUT_ENV_VAR)
    if requested:
        return Path(requested)
    return Path(FALLBACK_DESTINATION)


def fingerprint(blob: bytes) -> str:
    """Return the SHA-256 hex digest of a block of bytes."""
    return hashlib.sha256(blob).hexdigest()


def place_picture(origin: Path, destination: Path) -> int:
    """Write an exact copy of the artwork and prove that it matches.

    The byte count of the copy is returned. The run stops with a message
    on standard error if the artwork is absent, empty, or the copy fails
    to match the original.
    """
    if not origin.is_file():
        print(f"missing artwork: {origin} was not found", file=sys.stderr)
        raise SystemExit(1)

    original = origin.read_bytes()
    if len(original) == 0:
        print(f"nothing to copy: {origin} holds no data", file=sys.stderr)
        raise SystemExit(1)

    if original[: len(PNG_SIGNATURE)] != PNG_SIGNATURE:
        print(
            f"not a PNG picture: {origin} lacks the PNG signature",
            file=sys.stderr,
        )
        raise SystemExit(1)

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(original)

    duplicate = destination.read_bytes()
    if len(duplicate) != len(original):
        print(
            f"copy size mismatch: {destination} holds {len(duplicate)} bytes,"
            f" expected {len(original)}",
            file=sys.stderr,
        )
        raise SystemExit(1)

    if fingerprint(duplicate) != fingerprint(original):
        print(
            f"copy mismatch: {destination} differs from {origin}",
            file=sys.stderr,
        )
        raise SystemExit(1)

    return len(duplicate)


def run() -> int:
    folder = Path(__file__).resolve().parent
    picture = folder / PICTURE_FILENAME
    goal = pick_destination() / PICTURE_FILENAME

    total = place_picture(picture, goal)
    print(f"copied {goal} ({total} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
