# SPDX-License-Identifier: MIT
"""Copy the finished front-page picture to the grader's output folder.

The picture lives in this repository as entry.png: a newspaper front page
summing up the world news of Friday 20 November 2026, drawn from scratch
with Python's image library. This program only copies those exact bytes to
<output>/entry.png, where <output> is MAKEFUN_OUTPUT_DIR when that
variable is set and /output otherwise.

It uses the Python 3.13 standard library alone. It touches no network, reads
no clock, and reads no file outside this repository, so running it twice
always writes the same bytes.
"""

import hashlib
import os
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def output_dir() -> Path:
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return Path(chosen) if chosen else Path(DEFAULT_OUTPUT_DIR)


def copy_image(source: Path, target: Path) -> int:
    """Copy the picture and check the copy byte for byte.

    Returns the number of bytes written. Exits with an error message when
    the source is missing, empty, or the copy does not match it exactly.
    """
    if not source.is_file():
        print(f"error: source image {source} does not exist", file=sys.stderr)
        raise SystemExit(1)

    data = source.read_bytes()
    if not data:
        print(f"error: source image {source} is empty", file=sys.stderr)
        raise SystemExit(1)

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)

    written = target.stat().st_size
    if written != len(data):
        print(
            f"error: wrote {written} bytes to {target}, "
            f"expected {len(data)}",
            file=sys.stderr,
        )
        raise SystemExit(1)

    if hashlib.sha256(target.read_bytes()).hexdigest() != hashlib.sha256(
        data
    ).hexdigest():
        print(
            f"error: bytes written to {target} differ from source",
            file=sys.stderr,
        )
        raise SystemExit(1)

    return written


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / IMAGE_NAME
    target = output_dir() / IMAGE_NAME

    written = copy_image(source, target)
    print(f"wrote {target} ({written} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
