from __future__ import annotations

import argparse
import random
from pathlib import Path


def write_case(
    path: Path,
    values: list[int],
    queries: list[tuple[int, int]],
    answers: list[int],
) -> None:
    lines = [f"{len(values)} {len(queries)}", " ".join(map(str, values))]
    lines.extend(f"{left} {right}" for left, right in queries)
    path.with_suffix(".in").write_text("\n".join(lines) + "\n", encoding="utf-8")
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
            n = 200_000
            q = 200_000
            period = 1_000
            values = [index % period for index in range(n)]
            queries = []
            answers = []
            for index in range(q):
                left = 1 + (index * 997) % n
                available = n - left + 1
                length = 1 + (index * 7_919) % available
                right = left + length - 1
                queries.append((left, right))
                answers.append(min(length, period))
        else:
            n = rng.randint(1, 80)
            values = [rng.randint(-12, 12) for _ in range(n)]
            queries = []
            answers = []
            for _ in range(rng.randint(1, 120)):
                left = rng.randint(1, n)
                right = rng.randint(left, n)
                queries.append((left, right))
                answers.append(len(set(values[left - 1 : right])))
        write_case(args.out_dir / f"case{case_index:03d}", values, queries, answers)


if __name__ == "__main__":
    main()
