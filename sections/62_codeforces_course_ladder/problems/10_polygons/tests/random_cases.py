from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path


def exhaustive_oracle(n: int, k: int, total: int) -> str:
    candidates = [vector for vector in itertools.product(range(k + 1), repeat=n) if sum(vector) == total]
    return "-1" if not candidates else " ".join(map(str, min(candidates)))


def scale_answer(n: int, k: int, total: int) -> str:
    if total > n * k:
        return "-1"
    answer = []
    for index in range(n):
        value = max(0, total - (n - index - 1) * k)
        answer.append(value)
        total -= value
    return " ".join(map(str, answer))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    for case_id in range(args.count):
        if case_id == 0:
            rows = [(200_000, 1, 100_000)]
            answers = [scale_answer(*rows[0])]
        else:
            rows = [(rng.randint(1, 8), rng.randint(0, 5), rng.randint(0, 45)) for _ in range(rng.randint(1, 12))]
            answers = [exhaustive_oracle(*row) for row in rows]
        inp = str(len(rows)) + "\n" + "\n".join(f"{n} {k} {total}" for n, k, total in rows) + "\n"
        stem = args.out_dir / f"case{case_id:03d}"
        stem.with_suffix(".in").write_text(inp, encoding="utf-8")
        stem.with_suffix(".out").write_text("\n".join(answers) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
