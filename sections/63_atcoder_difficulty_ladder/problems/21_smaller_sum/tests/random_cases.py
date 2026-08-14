from __future__ import annotations

import argparse
import math
import random
from pathlib import Path


def brute_multiplier(value: int) -> int:
    """Try multipliers directly; suitable only for the tiny random range."""
    multiplier = 1
    while True:
        root = math.isqrt(value * multiplier)
        if root * root == value * multiplier:
            return multiplier
        multiplier += 1


def write_case(out_dir: Path, number: int, values: list[int], answers: list[int]) -> None:
    stem = out_dir / f"case{number:03d}"
    stem.with_suffix(".in").write_text(
        f"{len(values)}\n" + "\n".join(map(str, values)) + "\n",
        encoding="utf-8",
    )
    stem.with_suffix(".out").write_text(
        "\n".join(map(str, answers)) + "\n", encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    for case in range(args.count):
        if case == 0:
            values = [999_983] * 200_000
            answers = [999_983] * 200_000
        else:
            values = [rng.randint(1, 300) for _ in range(rng.randint(1, 30))]
            answers = [brute_multiplier(value) for value in values]
        write_case(args.out_dir, case, values, answers)


if __name__ == "__main__":
    main()
