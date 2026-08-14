from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path

MOD = 1_000_000_007


def brute_force(red: int, blue: int) -> int:
    """Independent tiny oracle: enumerate labeled orders directly."""
    people = list(range(red + blue))
    is_red = [person < red for person in people]
    answer = 0
    for order in itertools.permutations(people):
        if all(not (is_red[order[i]] and is_red[order[i + 1]]) for i in range(len(order) - 1)):
            answer += 1
    return answer % MOD


def write_case(path: Path, queries: list[tuple[int, int]], answers: list[int]) -> None:
    lines = [str(len(queries))]
    lines.extend(f"{red} {blue}" for red, blue in queries)
    path.with_suffix(".in").write_text("\n".join(lines) + "\n", encoding="utf-8")
    path.with_suffix(".out").write_text("\n".join(map(str, answers)) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    for case_index in range(args.count):
        if case_index == 0:
            # Directly known impossible queries exercise the full I/O bound.
            queries = [(1_000_000, 0)] * 200_000
            answers = [0] * 200_000
        else:
            query_count = rng.randint(1, 16)
            queries = []
            answers = []
            for _ in range(query_count):
                red = rng.randint(0, 4)
                blue = rng.randint(0, 8 - red)
                queries.append((red, blue))
                answers.append(brute_force(red, blue))
        write_case(args.out_dir / f"case{case_index:03d}", queries, answers)


if __name__ == "__main__":
    main()
