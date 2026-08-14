import argparse
import itertools
import random
from pathlib import Path


def oracle(a, b):
    return max(sum(x > y for x, y in zip(permutation, b))
               for permutation in itertools.permutations(a))


def greedy(a, b):
    target = wins = 0
    b = sorted(b)
    for value in sorted(a):
        if value > b[target]:
            target += 1
            wins += 1
            if target == len(b):
                break
    return wins


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = [([1], [1]), ([2, 2], [1, 2]),
             ([-2, -1, 0], [-3, -1, 2]), ([5, 5, 5], [1, 2, 3])]
    for case in range(args.count):
        if case < len(fixed):
            a, b = fixed[case]
        elif case == len(fixed):
            a = [rng.randint(-10**9, 10**9) for _ in range(200000)]
            b = [rng.randint(-10**9, 10**9) for _ in range(200000)]
        else:
            n = rng.randint(1, 8)
            a = [rng.randint(-5, 5) for _ in range(n)]
            b = [rng.randint(-5, 5) for _ in range(n)]
        answer = greedy(a, b) if len(a) > 9 else oracle(a, b)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(a)}\n" + " ".join(map(str, a)) + "\n"
            + " ".join(map(str, b)) + "\n")
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
