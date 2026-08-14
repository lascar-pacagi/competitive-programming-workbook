import argparse
import itertools
import random
from pathlib import Path


def oracle(durations, limit):
    return max(len(chosen) for size in range(len(durations) + 1)
               for chosen in itertools.combinations(durations, size)
               if sum(chosen) <= limit)


def greedy(durations, limit):
    total = answer = 0
    for duration in sorted(durations):
        if total + duration > limit:
            break
        total += duration
        answer += 1
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = [([10], 9), ([5, 5, 5], 15), ([9, 1, 2, 3], 6)]
    for case in range(args.count):
        if case < len(fixed):
            durations, limit = fixed[case]
        elif case == len(fixed):
            durations = [rng.randint(1, 10**9) for _ in range(200000)]
            limit = 10**18
        else:
            durations = [rng.randint(1, 30)
                         for _ in range(rng.randint(1, 15))]
            limit = rng.randint(1, 100)
        answer = greedy(durations, limit) if len(durations) > 20 else oracle(
            durations, limit)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(durations)} {limit}\n"
            + " ".join(map(str, durations)) + "\n")
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
