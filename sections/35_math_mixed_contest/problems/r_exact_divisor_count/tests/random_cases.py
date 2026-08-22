import argparse
import math
import random
from pathlib import Path


def divisor_count(value):
    result = 0
    for divisor in range(1, math.isqrt(value) + 1):
        if value % divisor == 0:
            result += 1 + (divisor * divisor != value)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for case in range(args.count):
        queries = [(rng.randint(1, 2500), rng.randint(1, 12))
                   for _ in range(rng.randint(1, 20))]
        answers = [sum(divisor_count(value) == k for value in range(1, n + 1))
                   for n, k in queries]
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(queries)}\n" +
            "\n".join(f"{n} {k}" for n, k in queries) + "\n"
        )
        stem.with_suffix(".out").write_text(
            "\n".join(map(str, answers)) + "\n"
        )


if __name__ == "__main__":
    main()
