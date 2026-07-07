from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path


def compatible(chosen: tuple[tuple[int, int], ...]) -> bool:
    ordered = sorted(chosen, key=lambda p: p[0])
    for i in range(1, len(ordered)):
        if ordered[i - 1][1] > ordered[i][0]:
            return False
    return True


def brute(intervals: list[tuple[int, int]]) -> int:
    best = 0
    for r in range(len(intervals) + 1):
        for chosen in itertools.combinations(intervals, r):
            if compatible(chosen):
                best = max(best, r)
    return best


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 10)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        n = rng.randint(1, 10)
        intervals: list[tuple[int, int]] = []
        for _ in range(n):
            start = rng.randint(-10, 10)
            end = start + rng.randint(1, 8)
            intervals.append((start, end))
        lines.append(str(n))
        lines.extend(f"{start} {end}" for start, end in intervals)
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

