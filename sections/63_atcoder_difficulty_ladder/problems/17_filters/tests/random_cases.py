from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path


def brute_force(score: list[int], edges: list[tuple[int, int]]) -> int:
    """Independent oracle: explicitly examine each subset and each edge."""
    n = len(score)
    answer = 0
    for chosen in range(1 << n):
        if any(((chosen >> u) & 1) and ((chosen >> v) & 1) for u, v in edges):
            continue
        answer = max(answer, sum(score[i] for i in range(n) if (chosen >> i) & 1))
    return answer


def write_case(path: Path, score: list[int], edges: list[tuple[int, int]], answer: int) -> None:
    lines = [f"{len(score)} {len(edges)}", " ".join(map(str, score))]
    lines.extend(f"{u + 1} {v + 1}" for u, v in edges)
    path.with_suffix(".in").write_text("\n".join(lines) + "\n", encoding="utf-8")
    path.with_suffix(".out").write_text(f"{answer}\n", encoding="utf-8")


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
            # A scale case checks 64-bit totals and the full 2^20 state space.
            score = [1_000_000_000] * 20
            edges: list[tuple[int, int]] = []
            answer = 20_000_000_000
        else:
            n = rng.randint(1, 12)
            score = [rng.randint(-30, 50) for _ in range(n)]
            edges = [
                (u, v)
                for u, v in itertools.combinations(range(n), 2)
                if rng.random() < 0.32
            ]
            answer = brute_force(score, edges)
        write_case(args.out_dir / f"case{case_index:03d}", score, edges, answer)


if __name__ == "__main__":
    main()
