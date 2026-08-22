import argparse
import math
import random
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for case in range(args.count):
        queries = [(rng.randint(1, 120), rng.randint(1, 120))
                   for _ in range(rng.randint(1, 15))]
        answers = [sum(math.gcd(x, y) == 1
                       for x in range(1, a + 1)
                       for y in range(1, b + 1)) for a, b in queries]
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(queries)}\n" +
            "\n".join(f"{a} {b}" for a, b in queries) + "\n"
        )
        stem.with_suffix(".out").write_text(
            "\n".join(map(str, answers)) + "\n"
        )


if __name__ == "__main__":
    main()
