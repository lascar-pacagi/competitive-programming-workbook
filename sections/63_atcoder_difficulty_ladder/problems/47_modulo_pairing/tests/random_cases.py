from __future__ import annotations

import argparse
import random
from pathlib import Path


def brute_path_cover(n: int, edges: list[tuple[int, int]]) -> int:
    """Independent tiny oracle: enumerate edge sets that can be disjoint paths."""
    most_joins = 0
    for mask in range(1 << len(edges)):
        incoming = [0] * n
        outgoing = [0] * n
        valid = True
        for index, (start, end) in enumerate(edges):
            if not ((mask >> index) & 1):
                continue
            outgoing[start] += 1
            incoming[end] += 1
            if outgoing[start] > 1 or incoming[end] > 1:
                valid = False
                break
        if valid:
            most_joins = max(most_joins, mask.bit_count())
    return n - most_joins


def small_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 7)
    possible = [(start, end) for start in range(n) for end in range(start + 1, n)]
    rng.shuffle(possible)
    edges = [edge for edge in possible[:10] if rng.random() < 0.55]
    answer = brute_path_cover(n, edges)
    case = f"{n} {len(edges)}\n" + "\n".join(f"{start + 1} {end + 1}" for start, end in edges)
    if edges:
        case += "\n"
    return case, f"{answer}\n"


def scale_case() -> tuple[str, str]:
    """A maximum-size chain has one path in every valid cover."""
    n = 2_000
    edges = (f"{vertex} {vertex + 1}" for vertex in range(1, n))
    return f"{n} {n - 1}\n" + "\n".join(edges) + "\n", "1\n"


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
