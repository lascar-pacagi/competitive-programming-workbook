import argparse
import itertools
import random
from pathlib import Path


def brute(machines, wanted):
    best = None
    ranges = [range(low, high + 1) for a, b, low, high in machines]
    for allocation in itertools.product(*ranges):
        if sum(allocation) != wanted:
            continue
        cost = sum(
            a * value * value + b * value
            for value, (a, b, _, _) in zip(allocation, machines)
        )
        best = cost if best is None else min(best, cost)
    return "IMPOSSIBLE" if best is None else str(best)


def small_case(rng):
    n = rng.randint(1, 6)
    machines = []
    for _ in range(n):
        low = rng.randint(0, 2)
        high = rng.randint(low, 4)
        machines.append((rng.randint(1, 5), rng.randint(-8, 8), low, high))
    wanted = rng.randint(0, 4 * n + 2)
    lines = [f"{n} {wanted}"]
    lines.extend(f"{a} {b} {low} {high}" for a, b, low, high in machines)
    return "\n".join(lines) + "\n", brute(machines, wanted) + "\n"


def scale_case():
    n = 200_000
    wanted = 100_000
    lines = [f"{n} {wanted}"]
    lines.extend(f"1 {index} 0 1" for index in range(n))
    expected = wanted * (wanted + 1) // 2
    return "\n".join(lines) + "\n", f"{expected}\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case_id in range(args.count):
        case, expected = (
            scale_case() if case_id == 0 else small_case(rng)
        )
        stem = f"case_{case_id:03d}"
        (args.out_dir / f"{stem}.in").write_text(case)
        (args.out_dir / f"{stem}.out").write_text(expected)


if __name__ == '__main__':
    main()
