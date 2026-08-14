from __future__ import annotations

import argparse
import random
from pathlib import Path


def small_case(rng: random.Random) -> tuple[str, str]:
    """Independent oracle: apply operations to a literal salary list."""
    n = rng.randint(1, 18)
    q = rng.randint(1, 40)
    salaries = [rng.randint(-15, 15) for _ in range(n)]
    current = salaries[:]
    operations: list[str] = []
    answers: list[str] = []
    for _ in range(q):
        if rng.random() < 0.48:
            employee = rng.randint(1, n)
            value = rng.randint(-20, 20)
            current[employee - 1] = value
            operations.append(f"! {employee} {value}")
        else:
            low = rng.randint(-25, 20)
            high = rng.randint(low, 25)
            answers.append(str(sum(low <= value <= high for value in current)))
            operations.append(f"? {low} {high}")
    case = f"{n} {q}\n" + " ".join(map(str, salaries)) + "\n"
    case += "\n".join(operations) + "\n"
    return case, "\n".join(answers) + ("\n" if answers else "")


def scale_case() -> tuple[str, str]:
    """Large mixed workload; expected counts follow directly from the updates."""
    n = q = 200_000
    salaries = list(range(1, n + 1))
    operations: list[str] = []
    answers: list[str] = []
    for employee in range(1, 100_001):
        operations.append(f"! {employee} 1000000000")
        operations.append("? 1000000000 1000000000")
        answers.append(str(employee))
    case = f"{n} {q}\n" + " ".join(map(str, salaries)) + "\n"
    case += "\n".join(operations) + "\n"
    return case, "\n".join(answers) + "\n"


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
