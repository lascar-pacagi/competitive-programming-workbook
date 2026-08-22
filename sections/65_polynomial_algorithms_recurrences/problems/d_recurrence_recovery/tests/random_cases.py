import argparse
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
        order = rng.randint(1, 5)
        roots = rng.sample(range(1, 100), order)
        weights = [rng.randint(1, 100) for _ in range(order)]
        length = rng.randint(2 * order, 2 * order + 8)
        index = rng.randint(0, 1000)
        def term(position: int) -> int:
            return sum(
                weight * pow(root, position, MOD)
                for root, weight in zip(roots, weights)
            ) % MOD
        observed = [term(i) for i in range(length)]
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{length} {index}\n" + " ".join(map(str, observed)) + "\n"
        )
        stem.with_suffix(".out").write_text(f"{order} {term(index)}\n")


if __name__ == "__main__":
    main()
