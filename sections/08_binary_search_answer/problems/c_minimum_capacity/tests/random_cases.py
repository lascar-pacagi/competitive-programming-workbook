from __future__ import annotations

import argparse
import random
from pathlib import Path


def days_needed(weights: list[int], capacity: int) -> int:
    days = 1
    cur = 0
    for w in weights:
        if cur + w <= capacity:
            cur += w
        else:
            days += 1
            cur = w
    return days


def brute(weights: list[int], days: int) -> int:
    for cap in range(max(weights), sum(weights) + 1):
        if days_needed(weights, cap) <= days:
            return cap
    raise AssertionError("unreachable")


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 12)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        n = rng.randint(1, 12)
        d = rng.randint(1, 20)
        weights = [rng.randint(1, 20) for _ in range(n)]
        lines.append(f"{n} {d}")
        lines.append(" ".join(map(str, weights)))
        answers.append(str(brute(weights, d)))
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

