from __future__ import annotations

import argparse
import random
from pathlib import Path


def brute(n: int, edges: list[tuple[int, int]]) -> list[int]:
    answer = [0] * n
    for mask in range(1 << n):
        if any((mask >> left) & 1 and (mask >> right) & 1 for left, right in edges):
            continue
        size = mask.bit_count()
        for vertex in range(n):
            if (mask >> vertex) & 1:
                answer[vertex] = max(answer[vertex], size)
    return answer


def path_answer(n: int, vertex: int) -> int:
    left_available = max(0, vertex - 2)
    right_available = max(0, n - vertex - 1)
    return 1 + (left_available + 1) // 2 + (right_available + 1) // 2


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    for case_number in range(args.count):
        if case_number == 0:
            n = 200_000
            edges = [(vertex, vertex + 1) for vertex in range(1, n)]
            answer = [path_answer(n, vertex) for vertex in range(1, n + 1)]
        else:
            n = rng.randint(1, 13)
            edges = [(vertex, rng.randint(1, vertex - 1)) for vertex in range(2, n + 1)]
            answer = brute(n, [(left - 1, right - 1) for left, right in edges])

        base = args.out_dir / f"case{case_number:03d}"
        base.with_suffix(".in").write_text(
            str(n) + "\n" + "\n".join(f"{left} {right}" for left, right in edges) + "\n"
        )
        base.with_suffix(".out").write_text(" ".join(map(str, answer)) + "\n")


if __name__ == "__main__":
    main()
