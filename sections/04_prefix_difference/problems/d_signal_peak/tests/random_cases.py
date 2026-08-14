from __future__ import annotations

import argparse
import random
from pathlib import Path


def brute(n: int, operations: list[tuple[int, int, int]]) -> tuple[int, int]:
    values = [0] * n
    for left, right, delta in operations:
        for index in range(left - 1, right):
            values[index] += delta
    best = max(values)
    return best, values.index(best) + 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)

    for case_id in range(args.count):
        if case_id == 0:
            n = q = 200_000
            operations = [(1, n, 1)] * q
        else:
            n = rng.randint(1, 60)
            q = rng.randint(1, 80)
            operations = []
            for _ in range(q):
                left = rng.randint(1, n)
                right = rng.randint(left, n)
                operations.append((left, right, rng.randint(-30, 30)))
        best, position = brute(n, operations) if case_id else (q, 1)
        lines = [f"{n} {q}"]
        lines.extend(f"{left} {right} {delta}" for left, right, delta in operations)
        stem = args.out_dir / f"case_{case_id:03d}"
        stem.with_suffix(".in").write_text("\n".join(lines) + "\n", encoding="utf-8")
        stem.with_suffix(".out").write_text(f"{best} {position}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
