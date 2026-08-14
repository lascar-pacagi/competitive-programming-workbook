from __future__ import annotations

import argparse
import random
from pathlib import Path


def brute_force(a: int, b: int, m: int) -> int:
    """Independent small oracle: test residues in increasing order."""
    for x in range(m):
        if (a * x - b) % m == 0:
            return x
    return -1


def write_case(path: Path, queries: list[tuple[int, int, int]], answers: list[int]) -> None:
    input_lines = [str(len(queries))]
    input_lines.extend(f"{a} {b} {m}" for a, b, m in queries)
    path.with_suffix(".in").write_text("\n".join(input_lines) + "\n", encoding="utf-8")
    path.with_suffix(".out").write_text(
        "\n".join(map(str, answers)) + "\n", encoding="utf-8"
    )


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
            # The answer is known directly: x = b because a = 1.
            queries = [(1, i % 1_000_000_000 + 1, 1_000_000_000) for i in range(200_000)]
            answers = [b for _, b, _ in queries]
        else:
            query_count = rng.randint(1, 25)
            queries = []
            answers = []
            for _ in range(query_count):
                m = rng.randint(1, 70)
                a = rng.randint(1, 70)
                b = rng.randint(1, 70)
                queries.append((a, b, m))
                answers.append(brute_force(a, b, m))
        write_case(args.out_dir / f"case{case_index:03d}", queries, answers)


if __name__ == "__main__":
    main()
