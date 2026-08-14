from __future__ import annotations

import argparse
import random
from pathlib import Path


def feasible(tasks: list[tuple[int, int]]) -> bool:
    elapsed = 0
    for duration, deadline in sorted(tasks, key=lambda task: task[1]):
        elapsed += duration
        if elapsed > deadline:
            return False
    return True


def brute(tasks: list[tuple[int, int]]) -> int:
    best = 0
    n = len(tasks)
    for mask in range(1 << n):
        chosen = [tasks[index] for index in range(n) if (mask >> index) & 1]
        if feasible(chosen):
            best = max(best, len(chosen))
    return best


def small_case(rng: random.Random) -> tuple[str, str]:
    """Independent tiny oracle: enumerate task subsets and test EDD feasibility."""
    n = rng.randint(1, 15)
    tasks = [(rng.randint(1, 12), rng.randint(1, 35)) for _ in range(n)]
    answer = brute(tasks)
    case = str(n) + "\n" + "\n".join(f"{duration} {deadline}" for duration, deadline in tasks) + "\n"
    return case, f"{answer}\n"


def scale_case() -> tuple[str, str]:
    """Long impossible jobs followed by 100,000 jointly feasible short jobs."""
    impossible = 100_000
    feasible_count = 100_000
    tasks = ["2 1"] * impossible + ["1 100000"] * feasible_count
    return f"{len(tasks)}\n" + "\n".join(tasks) + "\n", f"{feasible_count}\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for number in range(args.count):
        case, expected = scale_case() if number == 0 else small_case(rng)
        (args.out_dir / f"case_{number:03d}.in").write_text(case)
        (args.out_dir / f"case_{number:03d}.out").write_text(expected)


if __name__ == "__main__":
    main()
