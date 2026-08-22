import argparse
import math
import random
from pathlib import Path


def is_squarefree(value: int) -> bool:
    p = 2
    while p * p <= value:
        if value % (p * p) == 0:
            return False
        p += 1
    return True


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
        answers = [sum(is_squarefree(y) for y in range(1, x + 1))
                   for x in queries]
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(queries)}\n" + " ".join(map(str, queries)) + "\n"
        )
        stem.with_suffix(".out").write_text(
            "\n".join(map(str, answers)) + "\n"
        )


if __name__ == "__main__":
    main()
