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
    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for case in range(args.count):
        queries = [rng.randint(1, 300) for _ in range(rng.randint(1, 25))]
        values = []
        for n in queries:
            values.append(sum(math.gcd(i, n) == 1 for i in range(1, n + 1)))
        prefix = []
        total = 0
        for n in range(1, max(queries) + 1):
            total += sum(math.gcd(i, n) == 1 for i in range(1, n + 1))
            prefix.append(total % MOD)
        answers = [prefix[n - 1] for n in queries]
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(queries)}\n" + " ".join(map(str, queries)) + "\n"
        )
        stem.with_suffix(".out").write_text(
            "\n".join(map(str, answers)) + "\n"
        )


if __name__ == "__main__":
    main()
