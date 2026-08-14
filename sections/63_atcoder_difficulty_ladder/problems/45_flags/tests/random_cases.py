from __future__ import annotations

import argparse
import random
from pathlib import Path


def brute(s: str) -> int:
    for length in range(len(s) - 1, 0, -1):
        seen: set[str] = set()
        for left in range(len(s) - length + 1):
            piece = s[left : left + length]
            if piece in seen:
                return length
            seen.add(piece)
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case_number in range(args.count):
        if case_number == 0:
            s = "a" * 200_000
            answer = len(s) - 1
        else:
            s = "".join(rng.choice("abcd") for _ in range(rng.randint(1, 35)))
            answer = brute(s)
        base = args.out_dir / f"case{case_number:03d}"
        base.with_suffix(".in").write_text(s + "\n")
        base.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
