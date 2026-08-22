import argparse
import itertools
import random
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=30)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    for case in range(args.count):
        low = rng.randint(-4, 1)
        high = rng.randint(low, 5)
        n = rng.randint(1, 7)
        items = [(rng.randint(-7, 8), rng.randint(1, 6)) for _ in range(n)]
        best = None
        for chosen in itertools.combinations_with_replacement(
            range(low, high + 1), n
        ):
            cost = sum(w * abs(b - a) for (a, w), b in zip(items, chosen))
            if best is None or cost < best:
                best = cost

        text = f"{n} {low} {high}\n"
        text += "".join(f"{a} {w}\n" for a, w in items)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(text)
        stem.with_suffix(".out").write_text(f"{best}\n")


if __name__ == "__main__":
    main()
