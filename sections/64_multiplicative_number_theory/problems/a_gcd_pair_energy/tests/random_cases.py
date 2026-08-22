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
        n = rng.randint(2, 18)
        k = rng.randint(0, 8)
        values = [rng.randint(1, 35) for _ in range(n)]
        answer = sum(
            pow(math.gcd(values[i], values[j]), k, MOD)
            for i in range(n)
            for j in range(i + 1, n)
        ) % MOD
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{n} {k}\n" + " ".join(map(str, values)) + "\n"
        )
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
