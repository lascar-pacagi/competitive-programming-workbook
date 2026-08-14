import argparse
import itertools
import random
from pathlib import Path


def oracle(intervals):
    candidates = sorted({right for _, right in intervals})
    for size in range(len(candidates) + 1):
        for chosen in itertools.combinations(candidates, size):
            if all(any(left <= point <= right for point in chosen)
                   for left, right in intervals):
                return size


def greedy(intervals):
    last = None
    answer = 0
    for left, right in sorted(intervals, key=lambda x: (x[1], x[0])):
        if last is None or last < left:
            last = right
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
    for case in range(args.count):
        if case == 0:
            intervals = [(i, i + 3) for i in range(200000)]
            answer = greedy(intervals)
        else:
            intervals = []
            for _ in range(rng.randint(1, 11)):
                left = rng.randint(-8, 8)
                right = rng.randint(left, 10)
                intervals.append((left, right))
            answer = oracle(intervals)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            str(len(intervals)) + "\n"
            + "\n".join(f"{left} {right}" for left, right in intervals) + "\n"
        )
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
