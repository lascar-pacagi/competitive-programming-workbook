from __future__ import annotations

import argparse
import random
from pathlib import Path


def best_subset(values: list[int], limit: int) -> int:
    n = len(values)
    best = 0
    for mask in range(1 << n):
        total = 0
        for i, value in enumerate(values):
            if mask & (1 << i):
                total += value
        if total <= limit and total > best:
            best = total
    return best


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 12)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        n = rng.randint(0, 16)
        values = [rng.randint(0, 200) for _ in range(n)]
        if rng.random() < 0.2:
            limit = 0
        elif rng.random() < 0.4:
            limit = sum(values)
        else:
            limit = rng.randint(0, max(0, sum(values) + 20))
        lines.append(f"{n} {limit}")
        lines.append(" ".join(map(str, values)))
        answers.append(str(best_subset(values, limit)))
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

