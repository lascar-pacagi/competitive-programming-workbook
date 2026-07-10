from __future__ import annotations

import argparse
import random
from pathlib import Path


def maximum_assignment(left: int, right: int, edges: set[tuple[int, int]]) -> int:
    by_left = [[] for _ in range(left + 1)]
    for teammate, card in edges:
        by_left[teammate].append(card)

    def search(teammate: int, used: int) -> int:
        if teammate > left:
            return used.bit_count()
        best = search(teammate + 1, used)
        for card in by_left[teammate]:
            bit = 1 << (card - 1)
            if not used & bit:
                best = max(best, search(teammate + 1, used | bit))
        return best

    return search(1, 0)


def make_case(rng: random.Random) -> tuple[str, str]:
    left, right = rng.randint(1, 6), rng.randint(1, 6)
    edges = {
        (teammate, card)
        for teammate in range(1, left + 1)
        for card in range(1, right + 1)
        if rng.random() < 0.42
    }
    listed = sorted(edges)
    if listed and rng.random() < 0.4:
        listed.append(rng.choice(listed))
    text = f"{left} {right} {len(listed)}\n" + "\n".join(f"{u} {v}" for u, v in listed) + "\n"
    return text, f"{maximum_assignment(left, right, edges)}\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case_id in range(args.count):
        case, expected = make_case(rng)
        (args.out_dir / f"case{case_id:03}.in").write_text(case, encoding="utf-8")
        (args.out_dir / f"case{case_id:03}.out").write_text(expected, encoding="utf-8")


if __name__ == "__main__":
    main()
