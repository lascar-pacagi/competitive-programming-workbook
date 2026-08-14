import argparse
import itertools
import random
from pathlib import Path


def oracle(groups, capacity):
    answer = 0
    choices = [[None] + group for group in groups]
    for selected in itertools.product(*choices):
        weight = sum(item[0] for item in selected if item is not None)
        value = sum(item[1] for item in selected if item is not None)
        if weight <= capacity:
            answer = max(answer, value)
    return answer


def optimized(groups, capacity):
    dp = [0] * (capacity + 1)
    for group in groups:
        next_dp = dp.copy()
        for weight, value in group:
            for used in range(capacity - weight + 1):
                next_dp[used + weight] = max(
                    next_dp[used + weight], dp[used] + value)
        dp = next_dp
    return max(dp)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = [([[(1, 5)]], 1),
             ([[(2, 10), (2, 20)]], 2),
             ([[(3, 9)], [(3, 8)]], 3),
             ([[(5, 100)], [(1, 0), (2, 0)]], 2)]

    for case in range(args.count):
        if case < len(fixed):
            groups, capacity = fixed[case]
        elif case == len(fixed):
            capacity = 5000
            groups = []
            remaining = 2000
            for group_index in range(200):
                count = remaining // (200 - group_index)
                remaining -= count
                groups.append([(rng.randint(1, capacity),
                                rng.randint(0, 10**9))
                               for _ in range(count)])
        else:
            capacity = rng.randint(1, 15)
            groups = []
            for _ in range(rng.randint(1, 5)):
                groups.append([(rng.randint(1, capacity),
                                rng.randint(0, 25))
                               for _ in range(rng.randint(1, 3))])
        total_items = sum(map(len, groups))
        answer = (optimized(groups, capacity) if total_items > 15
                  else oracle(groups, capacity))
        stem = args.out_dir / f"case{case:03d}"
        lines = [f"{len(groups)} {capacity}"]
        for group in groups:
            fields = [str(len(group))]
            for weight, value in group:
                fields.extend((str(weight), str(value)))
            lines.append(" ".join(fields))
        stem.with_suffix(".in").write_text("\n".join(lines) + "\n")
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
