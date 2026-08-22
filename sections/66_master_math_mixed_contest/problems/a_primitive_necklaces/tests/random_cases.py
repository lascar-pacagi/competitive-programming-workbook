import argparse
import itertools
import random
from pathlib import Path

MOD = 1_000_000_007


def brute(n: int, colors: int) -> int:
    representatives = set()
    for word in itertools.product(range(colors), repeat=n):
        rotations = [word[r:] + word[:r] for r in range(n)]
        if all(rotations[r] != word for r in range(1, n)):
            representatives.add(min(rotations))
    return len(representatives) % MOD


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        queries = [(rng.randint(1, 6), rng.randint(1, 3)) for _ in range(rng.randint(1, 5))]
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(queries)}\n" + "\n".join(f"{n} {c}" for n, c in queries) + "\n"
        )
        stem.with_suffix(".out").write_text(
            "\n".join(str(brute(n, c)) for n, c in queries) + "\n"
        )


if __name__ == "__main__":
    main()
