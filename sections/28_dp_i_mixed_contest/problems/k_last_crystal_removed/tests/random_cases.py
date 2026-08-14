import argparse
import functools
import random
from pathlib import Path


def oracle(values):
    @functools.lru_cache(None)
    def search(remaining):
        if not remaining:
            return 0
        answer = 0
        for index, value in enumerate(remaining):
            left = remaining[index - 1] if index > 0 else 1
            right = remaining[index + 1] if index + 1 < len(remaining) else 1
            after = remaining[:index] + remaining[index + 1:]
            answer = max(answer, left * value * right + search(after))
        return answer

    return search(tuple(values))


def optimized(values):
    value = [1] + values + [1]
    n = len(values)
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    for gap in range(2, n + 2):
        for left in range(n + 2 - gap):
            right = left + gap
            dp[left][right] = max(
                dp[left][last] + dp[last][right]
                + value[left] * value[last] * value[right]
                for last in range(left + 1, right))
    return dp[0][n + 1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = [[7], [1, 1, 1], [3, 1, 5, 8], [10, 1, 10], [2, 3]]

    for case in range(args.count):
        if case < len(fixed):
            values = fixed[case]
        elif case == len(fixed):
            values = [rng.randint(1, 1000) for _ in range(300)]
        else:
            values = [rng.randint(1, 12)
                      for _ in range(rng.randint(1, 8))]
        answer = optimized(values) if len(values) > 9 else oracle(values)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(values)}\n" + " ".join(map(str, values)) + "\n")
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
