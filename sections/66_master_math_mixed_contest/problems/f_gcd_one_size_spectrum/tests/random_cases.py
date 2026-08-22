import argparse
import itertools
import math
import random
from pathlib import Path

MOD = 998_244_353


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        n = rng.randint(1, 13)
        values = [rng.randint(1, 24) for _ in range(n)]
        answer = []
        for size in range(1, n + 1):
            count = 0
            for chosen in itertools.combinations(values, size):
                gcd = 0
                for value in chosen:
                    gcd = math.gcd(gcd, value)
                count += gcd == 1
            answer.append(count % MOD)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{n}\n" + " ".join(map(str, values)) + "\n"
        )
        stem.with_suffix(".out").write_text(" ".join(map(str, answer)) + "\n")


if __name__ == "__main__":
    main()
