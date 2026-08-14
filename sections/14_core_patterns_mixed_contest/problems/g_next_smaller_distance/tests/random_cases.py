import argparse
import random
from pathlib import Path


def oracle(values):
    answer = []
    for i, value in enumerate(values):
        distance = 0
        for j in range(i + 1, len(values)):
            if values[j] < value:
                distance = j - i
                break
        answer.append(distance)
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        if case == 0:
            values = list(range(200000, 0, -1))
            answer = [1] * 199999 + [0]
        else:
            values = [rng.randint(-10, 10) for _ in range(rng.randint(1, 100))]
            answer = oracle(values)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(values)}\n" + " ".join(map(str, values)) + "\n"
        )
        stem.with_suffix(".out").write_text(
            " ".join(map(str, answer)) + "\n"
        )


if __name__ == "__main__":
    main()
