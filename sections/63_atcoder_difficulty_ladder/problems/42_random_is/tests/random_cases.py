from __future__ import annotations

import argparse
import random
from functools import lru_cache
from pathlib import Path


def brute(moves: tuple[int, ...], piles: tuple[int, ...]) -> bool:
    @lru_cache(maxsize=None)
    def winning(state: tuple[int, ...]) -> bool:
        for index, stones in enumerate(state):
            for move in moves:
                if move <= stones:
                    next_state = list(state)
                    next_state[index] -= move
                    if not winning(tuple(sorted(next_state))):
                        return True
        return False

    return winning(tuple(sorted(piles)))


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
            moves = [1]
            piles = list(range(200_000))
            answer = "WIN" if sum(stones & 1 for stones in piles) % 2 else "LOSE"
        else:
            moves = sorted(rng.sample(range(1, 6), rng.randint(1, 4)))
            piles = [rng.randint(0, 8) for _ in range(rng.randint(1, 5))]
            answer = "WIN" if brute(tuple(moves), tuple(piles)) else "LOSE"
        base = args.out_dir / f"case{case_number:03d}"
        base.with_suffix(".in").write_text(
            f"{len(moves)} {len(piles)}\n" + " ".join(map(str, moves)) + "\n" + " ".join(map(str, piles)) + "\n"
        )
        base.with_suffix(".out").write_text(answer + "\n")


if __name__ == "__main__":
    main()
