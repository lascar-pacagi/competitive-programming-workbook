from __future__ import annotations

import argparse
import random
from pathlib import Path


def small_case(rng: random.Random) -> tuple[str, str]:
    """Independent oracle: maintain a literal list and scan it left to right."""
    n = rng.randint(1, 16)
    q = rng.randint(1, 35)
    capacities = [rng.randint(0, 12) for _ in range(n)]
    current = capacities[:]
    operations: list[str] = []
    answers: list[str] = []
    for _ in range(q):
        if rng.random() < 0.45:
            index = rng.randint(1, n)
            value = rng.randint(0, 12)
            current[index - 1] = value
            operations.append(f"1 {index} {value}")
        else:
            need = rng.randint(1, 14)
            answer = 0
            for index, value in enumerate(current, start=1):
                if value >= need:
                    answer = index
                    break
            answers.append(str(answer))
            operations.append(f"2 {need}")
    case = f"{n} {q}\n" + " ".join(map(str, capacities)) + "\n"
    case += "\n".join(operations) + "\n"
    return case, "\n".join(answers) + ("\n" if answers else "")


def scale_case() -> tuple[str, str]:
    """A non-enumerable workload with a directly known expected output."""
    n = q = 200_000
    operations: list[str] = []
    for index in range(1, 100_001):
        operations.append(f"1 {index} 1")
        operations.append("2 1")
    case = f"{n} {q}\n" + "0 " * (n - 1) + "0\n"
    case += "\n".join(operations) + "\n"
    return case, "1\n" * 100_000


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
