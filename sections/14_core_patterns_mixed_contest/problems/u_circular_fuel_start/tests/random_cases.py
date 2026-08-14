import argparse
import random
from pathlib import Path


def oracle(fuel, cost):
    n = len(fuel)
    for start in range(n):
        tank = 0
        valid = True
        for step in range(n):
            i = (start + step) % n
            tank += fuel[i] - cost[i]
            if tank < 0:
                valid = False
                break
        if valid:
            return start
    return -1


def greedy(fuel, cost):
    total = tank = candidate = 0
    for i, (received, spent) in enumerate(zip(fuel, cost)):
        gain = received - spent
        total += gain
        tank += gain
        if tank < 0:
            candidate = i + 1
            tank = 0
    return -1 if total < 0 else candidate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = [([0], [0]), ([1], [2]), ([2, 0], [1, 1]),
             ([0, 3, 0], [1, 1, 1]), ([2, 2, 2], [2, 2, 2])]
    for case in range(args.count):
        if case < len(fixed):
            fuel, cost = fixed[case]
        elif case == len(fixed):
            fuel = [rng.randint(0, 10**9) for _ in range(200000)]
            cost = [rng.randint(0, 10**9) for _ in range(200000)]
        else:
            n = rng.randint(1, 12)
            fuel = [rng.randint(0, 9) for _ in range(n)]
            cost = [rng.randint(0, 9) for _ in range(n)]
        answer = greedy(fuel, cost) if len(fuel) > 20 else oracle(fuel, cost)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(fuel)}\n" + " ".join(map(str, fuel)) + "\n"
            + " ".join(map(str, cost)) + "\n")
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
