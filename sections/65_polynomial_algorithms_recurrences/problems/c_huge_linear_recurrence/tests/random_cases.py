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
        order = rng.randint(1, 7)
        index = rng.randint(0, 80)
        initial = [rng.randrange(MOD) for _ in range(order)]
        coefficient = [rng.randrange(MOD) for _ in range(order)]
        sequence = initial[:]
        while len(sequence) <= index:
            sequence.append(sum(
                coefficient[j] * sequence[-1 - j] for j in range(order)
            ) % MOD)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{order} {index}\n"
            + " ".join(map(str, initial)) + "\n"
            + " ".join(map(str, coefficient)) + "\n"
        )
        stem.with_suffix(".out").write_text(f"{sequence[index]}\n")


if __name__ == "__main__":
    main()
