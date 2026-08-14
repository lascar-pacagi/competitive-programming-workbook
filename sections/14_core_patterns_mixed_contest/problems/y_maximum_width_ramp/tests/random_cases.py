import argparse
import random
from pathlib import Path


def oracle(values):
    answer = 0
    for i in range(len(values)):
        for j in range(i, len(values)):
            if values[i] <= values[j]:
                answer = max(answer, j - i)
    return answer


def optimized(values):
    candidates = []
    for i, value in enumerate(values):
        if not candidates or value < values[candidates[-1]]:
            candidates.append(i)
    answer = 0
    for j in range(len(values) - 1, -1, -1):
        while candidates and values[candidates[-1]] <= values[j]:
            answer = max(answer, j - candidates.pop())
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = [[7], [1, 2, 3, 4], [4, 3, 2, 1], [2, 2, 2],
             [9, 8, 1, 0, 1, 9], [-3, 5, -2, 4]]

    for case in range(args.count):
        if case < len(fixed):
            values = fixed[case]
        elif case == len(fixed):
            values = [rng.randint(-10**9, 10**9) for _ in range(200000)]
        else:
            values = [rng.randint(-15, 15)
                      for _ in range(rng.randint(1, 35))]
        answer = optimized(values) if len(values) > 100 else oracle(values)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(values)}\n" + " ".join(map(str, values)) + "\n")
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
