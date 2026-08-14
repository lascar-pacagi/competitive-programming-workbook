from __future__ import annotations

import argparse
import random
from collections import deque
from pathlib import Path


def oracle(target: int, coins: list[int]) -> int:
    """Breadth-first search over reachable amounts for tiny independent cases."""
    distance = [-1] * (target + 1)
    distance[0] = 0
    queue = deque([0])
    while queue:
        amount = queue.popleft()
        if amount == target:
            return distance[amount]
        for coin in coins:
            next_amount = amount + coin
            if next_amount <= target and distance[next_amount] == -1:
                distance[next_amount] = distance[amount] + 1
                queue.append(next_amount)
    return -1


def write_case(
    out_dir: Path, number: int, target: int, coins: list[int], expected: int | None = None
) -> None:
    stem = out_dir / f"case{number:03d}"
    stem.with_suffix(".in").write_text(
        f"{target} {len(coins)}\n" + " ".join(map(str, coins)) + "\n",
        encoding="utf-8",
    )
    if expected is None:
        expected = oracle(target, coins)
    stem.with_suffix(".out").write_text(f"{expected}\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    for case in range(args.count):
        if case == 0:
            write_case(args.out_dir, case, 200_000, [1, 49_999, 50_000, 50_001], 4)
        else:
            target = rng.randint(0, 80)
            coins = [rng.randint(1, 50) for _ in range(rng.randint(1, 8))]
            write_case(args.out_dir, case, target, coins)


if __name__ == "__main__":
    main()
