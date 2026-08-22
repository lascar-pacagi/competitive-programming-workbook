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
        maximum = rng.randint(1, 25)
        n = rng.randint(2, 20)
        values = [rng.randint(1, maximum) for _ in range(n)]
        answer = [0] * (maximum + 1)
        for i in range(n):
            for j in range(i + 1, n):
                lcm = values[i] // math.gcd(values[i], values[j]) * values[j]
                if lcm <= maximum:
                    answer[lcm] += 1
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{n} {maximum}\n" + " ".join(map(str, values)) + "\n"
        )
        stem.with_suffix(".out").write_text(
            " ".join(str(x % MOD) for x in answer[1:]) + "\n"
        )


if __name__ == "__main__":
    main()
