import argparse
import math
import random
from pathlib import Path

MOD = 1_000_000_007


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        queries = [rng.randint(1, 250) for _ in range(rng.randint(1, 12))]
        answers = [
            sum(
                sum(math.gcd(x, value) == 1 for x in range(1, value + 1))
                for value in range(1, n + 1)
            ) % MOD
            for n in queries
        ]
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(queries)}\n" + "\n".join(map(str, queries)) + "\n"
        )
        stem.with_suffix(".out").write_text("\n".join(map(str, answers)) + "\n")


if __name__ == "__main__":
    main()
