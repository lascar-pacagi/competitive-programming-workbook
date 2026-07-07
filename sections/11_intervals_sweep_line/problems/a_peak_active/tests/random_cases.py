from __future__ import annotations

import argparse
import random
from pathlib import Path


def brute(intervals: list[tuple[int, int]]) -> int:
    best = 0
    for x in [v for interval in intervals for v in interval]:
        active = sum(1 for l, r in intervals if l <= x < r)
        best = max(best, active)
    return best


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 15)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        n = rng.randint(1, 12)
        intervals: list[tuple[int, int]] = []
        for _ in range(n):
            l = rng.randint(-10, 10)
            r = l + rng.randint(1, 8)
            intervals.append((l, r))
        lines.append(str(n))
        lines.extend(f"{l} {r}" for l, r in intervals)
        answers.append(str(brute(intervals)))
    return "\n".join(lines) + "\n", "\n".join(answers) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        inp, out = build_case(rng)
        stem = args.out_dir / f"case_{i:03d}"
        stem.with_suffix(".in").write_text(inp, encoding="utf-8")
        stem.with_suffix(".out").write_text(out, encoding="utf-8")


if __name__ == "__main__":
    main()

