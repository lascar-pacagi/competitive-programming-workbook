from __future__ import annotations

import argparse
import random
from pathlib import Path


def brute(values: list[int], minimum_length: int, maximum_length: int) -> int:
    answer = -10**30
    for left in range(len(values)):
        total = 0
        for right in range(left, len(values)):
            total += values[right]
            if minimum_length <= right - left + 1 <= maximum_length:
                answer = max(answer, total)
    return answer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    for case_number in range(args.count):
        if case_number == 0:
            n, minimum_length, maximum_length = 200_000, 50_000, 150_000
            values = [1] * n
            answer = maximum_length
        else:
            n = rng.randint(1, 30)
            minimum_length = rng.randint(1, n)
            maximum_length = rng.randint(minimum_length, n)
            values = [rng.randint(-15, 15) for _ in range(n)]
            answer = brute(values, minimum_length, maximum_length)
        base = args.out_dir / f"case{case_number:03d}"
        base.with_suffix(".in").write_text(
            f"{n} {minimum_length} {maximum_length}\n" + " ".join(map(str, values)) + "\n"
        )
        base.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
