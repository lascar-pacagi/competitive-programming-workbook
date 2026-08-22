import argparse
import math
import random
from pathlib import Path


def phi(x: int) -> int:
    return sum(math.gcd(x, value) == 1 for value in range(1, x + 1))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        queries = []
        for _ in range(rng.randint(1, 8)):
            left = rng.randint(1, 150)
            queries.append((left, rng.randint(left, 200)))
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(queries)}\n" + "\n".join(f"{l} {r}" for l, r in queries) + "\n"
        )
        stem.with_suffix(".out").write_text(
            "\n".join(str(sum(phi(x) for x in range(l, r + 1))) for l, r in queries) + "\n"
        )


if __name__ == "__main__":
    main()
