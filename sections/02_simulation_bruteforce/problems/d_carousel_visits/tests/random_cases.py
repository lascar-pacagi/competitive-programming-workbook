from __future__ import annotations

import argparse
import random
from pathlib import Path


def answer(n: int, pos: int, moves: str) -> str:
    visits = [0] * (n + 1)
    visits[pos] += 1
    for move in moves:
        pos = 1 if move == "R" and pos == n else pos + 1 if move == "R" else n if pos == 1 else pos - 1
        visits[pos] += 1
    best = max(range(1, n + 1), key=lambda slot: (visits[slot], -slot))
    return f"{pos} {best}"


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
            n = 100_000
            pos = 50_000
            moves = "R" * 100_000
            stem = args.out_dir / f"case_{case:03d}"
            stem.with_suffix(".in").write_text(
                f"1\n{n} {pos} {moves}\n", encoding="utf-8"
            )
            stem.with_suffix(".out").write_text(
                answer(n, pos, moves) + "\n", encoding="utf-8"
            )
            continue
        t = rng.randint(1, 25)
        lines = [str(t)]
        out = []
        for _ in range(t):
            n = rng.randint(1, 80)
            pos = rng.randint(1, n)
            moves = "".join(rng.choice("LR") for _ in range(rng.randint(1, 120)))
            lines.append(f"{n} {pos} {moves}")
            out.append(answer(n, pos, moves))
        stem = args.out_dir / f"case_{case:03d}"
        stem.with_suffix(".in").write_text("\n".join(lines) + "\n", encoding="utf-8")
        stem.with_suffix(".out").write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
