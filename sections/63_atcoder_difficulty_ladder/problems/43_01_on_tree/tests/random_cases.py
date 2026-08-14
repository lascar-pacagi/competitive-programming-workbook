from __future__ import annotations

import argparse
import random
from pathlib import Path


MOD = 1_000_000_007


def enumerate_partitions(n: int, teams: int) -> int:
    """Independent tiny oracle: enumerate canonical restricted-growth strings."""
    if n == 0:
        return int(teams == 0)

    answer = 0

    def visit(position: int, largest_label: int) -> None:
        nonlocal answer
        if position == n:
            answer += largest_label + 1 == teams
            return
        upper_label = min(largest_label + 1, teams - 1)
        for label in range(upper_label + 1):
            visit(position + 1, max(largest_label, label))

    visit(1, 0)  # The first person is in canonical team 0.
    return answer


def small_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 9)
    teams = rng.randint(1, n)
    return f"{n} {teams}\n", f"{enumerate_partitions(n, teams) % MOD}\n"


def scale_case() -> tuple[str, str]:
    """Fixed maximum-size instance with independently precomputed output."""
    return "2000 1000\n", "163743874\n"


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
