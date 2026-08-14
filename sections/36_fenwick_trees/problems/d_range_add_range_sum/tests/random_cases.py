from __future__ import annotations

import argparse
import random
from pathlib import Path


def write_case(path: Path, n: int, operations: list[tuple[int, ...]], answers: list[int]) -> None:
    lines = [f"{n} {len(operations)}"]
    lines.extend(" ".join(map(str, operation)) for operation in operations)
    path.with_suffix(".in").write_text("\n".join(lines) + "\n", encoding="utf-8")
    path.with_suffix(".out").write_text("\n".join(map(str, answers)) + ("\n" if answers else ""), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    for case_index in range(args.count):
        if case_index == 0:
            n = 200_000
            operations = [(1, 1, n, 1)] * 100_000 + [(2, 1, n)] * 100_000
            answers = [20_000_000_000] * 100_000
        else:
            n = rng.randint(1, 25)
            values = [0] * n
            operations = []
            answers = []
            for _ in range(rng.randint(1, 120)):
                left = rng.randint(1, n)
                right = rng.randint(left, n)
                if rng.random() < 0.62:
                    delta = rng.randint(-30, 40)
                    operations.append((1, left, right, delta))
                    for position in range(left - 1, right):
                        values[position] += delta
                else:
                    operations.append((2, left, right))
                    answers.append(sum(values[left - 1:right]))
        write_case(args.out_dir / f"case{case_index:03d}", n, operations, answers)


if __name__ == "__main__":
    main()
