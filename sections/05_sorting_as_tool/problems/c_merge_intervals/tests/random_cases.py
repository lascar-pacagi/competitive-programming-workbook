from __future__ import annotations

import argparse
import random
from pathlib import Path


def merge(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    intervals = sorted(intervals)
    merged: list[tuple[int, int]] = []
    for l, r in intervals:
        if not merged or l > merged[-1][1] + 1:
            merged.append((l, r))
        else:
            old_l, old_r = merged[-1]
            merged[-1] = (old_l, max(old_r, r))
    return merged


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 12)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        n = rng.randint(1, 80)
        intervals: list[tuple[int, int]] = []
        lines.append(str(n))
        for _ in range(n):
            l = rng.randint(-50, 50)
            r = l + rng.randint(0, 20)
            intervals.append((l, r))
            lines.append(f"{l} {r}")
        merged = merge(intervals)
        answers.append(str(len(merged)))
        answers.extend(f"{l} {r}" for l, r in merged)
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

