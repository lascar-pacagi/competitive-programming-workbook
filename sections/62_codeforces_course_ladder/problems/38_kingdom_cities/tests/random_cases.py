from __future__ import annotations

import argparse
import random
from pathlib import Path


def solve_slow(labels: list[int], parents: list[int], node: int, distance: int) -> int:
    answer = labels[node]
    for _ in range(distance):
        node = parents[node]
        if node == 0:
            return -1
        answer = min(answer, labels[node])
    return answer


def write_case(
    path: Path,
    labels: list[int],
    parents: list[int],
    queries: list[tuple[int, int]],
    answers: list[int],
) -> None:
    n = len(labels) - 1
    lines = [f"{n} {len(queries)}", " ".join(map(str, labels[1:]))]
    lines.append(" ".join(str(parents[node]) for node in range(2, n + 1)))
    lines.extend(f"{node} {distance}" for node, distance in queries)
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
            n = 200_000
            labels = [0] + [1] * n
            parents = [0] * (n + 1)
            for node in range(2, n + 1):
                parents[node] = node - 1
            queries = [(n, n - 1)] * 200_000
            answers = [1] * 200_000
        else:
            n = rng.randint(1, 40)
            labels = [0] + [rng.randint(-50, 60) for _ in range(n)]
            parents = [0] * (n + 1)
            for node in range(2, n + 1):
                parents[node] = rng.randint(1, node - 1)
            queries = [(rng.randint(1, n), rng.randint(0, n + 4)) for _ in range(rng.randint(1, 80))]
            answers = [solve_slow(labels, parents, node, distance) for node, distance in queries]
        write_case(args.out_dir / f"case{case_index:03d}", labels, parents, queries, answers)


if __name__ == "__main__":
    main()
