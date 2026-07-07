from __future__ import annotations

import argparse
import math
import random
from pathlib import Path


MOD = 1_000_000_007


def solve(case: str) -> str:
    h, w, r, c = map(int, case.split())
    total = math.comb(h + w - 2, h - 1)
    through = math.comb(r + c - 2, r - 1) * math.comb(h - r + w - c, h - r)
    return f"{(total - through) % MOD}\n"


def make_case(rng: random.Random) -> str:
    h = rng.randint(1, 30)
    w = rng.randint(1, 30)
    return f"{h} {w} {rng.randint(1, h)} {rng.randint(1, w)}\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for i in range(args.count):
        case = make_case(rng)
        (args.out_dir / f"case_{i:03d}.in").write_text(case)
        (args.out_dir / f"case_{i:03d}.out").write_text(solve(case))


if __name__ == "__main__":
    main()
