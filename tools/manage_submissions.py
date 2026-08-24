"""Create and maintain a private overlay of personal course submissions.

The overlay mirrors each problem path below the course root. The local judge
automatically reads it when the default `.submissions` directory exists, or
when CP_SUBMISSIONS_DIR names another directory.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CPP_STUB = """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // TODO: solve the problem.
    return 0;
}
"""
PYTHON_STUB = """import sys


def main() -> None:
    # TODO: solve the problem.
    pass


if __name__ == "__main__":
    main()
"""


def submission_files() -> list[Path]:
    return sorted(
        path
        for path in (ROOT / "sections").rglob("solve.*")
        if path.name in {"solve.cpp", "solve.py"}
    )


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve_destination(raw: str) -> Path:
    destination = Path(raw).expanduser()
    if not destination.is_absolute():
        destination = ROOT / destination
    return destination.resolve()


def copy_submissions(destination: Path, overwrite: bool) -> tuple[int, int]:
    copied = 0
    preserved = 0
    for source in submission_files():
        relative = source.relative_to(ROOT)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and not overwrite:
            preserved += 1
            continue
        shutil.copy2(source, target)
        if digest(source) != digest(target):
            raise RuntimeError(f"backup verification failed for {relative}")
        copied += 1
    return copied, preserved


def reset_public_stubs() -> int:
    reset = 0
    for path in submission_files():
        expected = CPP_STUB if path.suffix == ".cpp" else PYTHON_STUB
        if path.read_text(encoding="utf-8") != expected:
            path.write_text(expected, encoding="utf-8")
            reset += 1
    return reset


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "command",
        choices=("seed", "migrate"),
        help=(
            "seed copies only missing files; migrate copies public solve files "
            "and resets them to TODO stubs"
        ),
    )
    parser.add_argument(
        "--destination",
        default=".submissions",
        help="overlay root (default: .submissions)",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="allow migrate to replace existing overlay files",
    )
    args = parser.parse_args()
    destination = resolve_destination(args.destination)

    existing = [
        destination / source.relative_to(ROOT) for source in submission_files()
        if (destination / source.relative_to(ROOT)).exists()
    ]
    if args.command == "migrate" and existing and not args.overwrite:
        parser.error(
            f"refusing to overwrite {len(existing)} existing overlay file(s) in "
            f"{destination}; make a backup and rerun with --overwrite only if "
            "that is intentional"
        )

    copied, preserved = copy_submissions(
        destination,
        overwrite=args.command == "migrate" and args.overwrite,
    )
    print(f"Verified {copied} copied submission file(s) in {destination}.")
    if preserved:
        print(f"Preserved {preserved} existing overlay file(s).")

    if args.command == "migrate":
        reset = reset_public_stubs()
        print(f"Reset {reset} public solve file(s) to standard TODO stubs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
