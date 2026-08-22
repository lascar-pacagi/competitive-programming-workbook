import argparse
import random
from pathlib import Path


def squarefree(x: int) -> bool:
    d = 2
    while d * d <= x:
        if x % (d * d) == 0:
            return False
        d += 1
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    values = [x for x in range(1, 1000) if squarefree(x)]
    for case in range(args.count):
        ranks = [rng.randint(1, 300) for _ in range(rng.randint(1, 12))]
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(ranks)}\n" + "\n".join(map(str, ranks)) + "\n"
        )
        stem.with_suffix(".out").write_text(
            "\n".join(str(values[k - 1]) for k in ranks) + "\n"
        )


if __name__ == "__main__":
    main()
