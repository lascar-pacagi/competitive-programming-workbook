import argparse
import collections
import random
from pathlib import Path


def oracle(cost, k):
    dp = [0] * len(cost)
    dp[0] = cost[0]
    for i in range(1, len(cost)):
        dp[i] = cost[i] + min(dp[max(0, i - k):i])
    return dp[-1]


def optimized(cost, k):
    dp = [0] * len(cost)
    dp[0] = cost[0]
    candidates = collections.deque([0])
    for i in range(1, len(cost)):
        while candidates[0] < i - k:
            candidates.popleft()
        dp[i] = cost[i] + dp[candidates[0]]
        while candidates and dp[candidates[-1]] >= dp[i]:
            candidates.pop()
        candidates.append(i)
    return dp[-1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = [([7], 1), ([5, -10, 5], 2), ([1, 2, 3, 4], 1),
             ([8, 7, 6, 5], 20), ([0, 0, 0, 0], 2)]

    for case in range(args.count):
        if case < len(fixed):
            cost, k = fixed[case]
        elif case == len(fixed):
            cost = [rng.randint(-10**9, 10**9) for _ in range(200000)]
            k = rng.randint(1, 200000)
        else:
            cost = [rng.randint(-30, 30)
                    for _ in range(rng.randint(1, 35))]
            k = rng.randint(1, 40)
        answer = optimized(cost, k) if len(cost) > 100 else oracle(cost, k)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(cost)} {k}\n" + " ".join(map(str, cost)) + "\n")
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
