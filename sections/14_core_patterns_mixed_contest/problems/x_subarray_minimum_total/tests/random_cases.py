import argparse
import random
from pathlib import Path


def oracle(values):
    answer = 0
    for left in range(len(values)):
        minimum = values[left]
        for right in range(left, len(values)):
            minimum = min(minimum, values[right])
            answer += minimum
    return answer


def optimized(values):
    stack = []
    ending_sum = 0
    answer = 0
    for value in values:
        ways = 1
        while stack and stack[-1][0] >= value:
            old_value, old_ways = stack.pop()
            ending_sum -= old_value * old_ways
            ways += old_ways
        stack.append((value, ways))
        ending_sum += value * ways
        answer += ending_sum
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = [[5], [2, 2, 2], [5, 4, 3, 2, 1],
             [1, 2, 3, 4, 5], [3, 1, 2, 1, 4]]

    for case in range(args.count):
        if case < len(fixed):
            values = fixed[case]
        elif case == len(fixed):
            values = [rng.randint(1, 10**6) for _ in range(200000)]
        else:
            values = [rng.randint(1, 12)
                      for _ in range(rng.randint(1, 25))]
        answer = optimized(values) if len(values) > 100 else oracle(values)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(values)}\n" + " ".join(map(str, values)) + "\n")
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
