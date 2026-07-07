from __future__ import annotations

import argparse
import random
from pathlib import Path


def solve(values: list[int], limit: int) -> tuple[int, int]:
    best_len = 0
    best_start = 0
    for l in range(len(values)):
        total = 0
        for r in range(l, len(values)):
            total += values[r]
            if total <= limit:
                length = r - l + 1
                start = l + 1
                if length > best_len or (length == best_len and start < best_start):
                    best_len = length
                    best_start = start
    return best_len, best_start


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 20)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        n = rng.randint(1, 100)
        values = [rng.randint(0, 20) for _ in range(n)]
        if rng.random() < 0.2:
            limit = 0
        else:
            limit = rng.randint(0, max(0, sum(values) + 10))
        lines.append(f"{n} {limit}")
        lines.append(" ".join(map(str, values)))
        length, start = solve(values, limit)
        answers.append(f"{length} {start}")
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

