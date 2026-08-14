from __future__ import annotations

import argparse
import random
from pathlib import Path


def brute(profit: list[int], rules: list[tuple[int, int]]) -> int:
    best = 0
    n = len(profit)
    for mask in range(1 << n):
        if any((mask >> project) & 1 and not ((mask >> prerequisite) & 1) for project, prerequisite in rules):
            continue
        best = max(best, sum(value for index, value in enumerate(profit) if (mask >> index) & 1))
    return best


def small_case(rng: random.Random) -> tuple[str, str]:
    """Independent tiny oracle: enumerate every selected-project subset."""
    n = rng.randint(1, 10)
    profit = [rng.randint(-12, 15) for _ in range(n)]
    rules: list[tuple[int, int]] = []
    for project in range(n):
        for prerequisite in range(n):
            if project != prerequisite and rng.random() < 0.16:
                rules.append((project, prerequisite))
    answer = brute(profit, rules)
    case = f"{n} {len(rules)}\n" + " ".join(map(str, profit)) + "\n"
    case += "\n".join(f"{project + 1} {prerequisite + 1}" for project, prerequisite in rules)
    if rules:
        case += "\n"
    return case, f"{answer}\n"


def scale_case() -> tuple[str, str]:
    """Large independent prerequisite pairs with a directly known optimum."""
    n = 200
    pairs = n // 2
    profit = [5] * pairs + [-3] * pairs
    rules = (f"{project} {project + pairs}" for project in range(1, pairs + 1))
    case = f"{n} {pairs}\n" + " ".join(map(str, profit)) + "\n"
    case += "\n".join(rules) + "\n"
    return case, f"{2 * pairs}\n"


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
