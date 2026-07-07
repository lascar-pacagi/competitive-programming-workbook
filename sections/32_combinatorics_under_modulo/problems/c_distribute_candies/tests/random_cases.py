from __future__ import annotations

import argparse
import math
import random
from pathlib import Path


MOD = 1_000_000_007


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    q = data[0]
    idx = 1
    out = []
    for _ in range(q):
        n, s = data[idx], data[idx + 1]
        idx += 2
        out.append(str(math.comb(n + s - 1, n - 1) % MOD))
    return "\n".join(out) + "\n"


def make_case(rng: random.Random) -> str:
    q = rng.randint(1, 50)
    lines = [str(q)]
    for _ in range(q):
        lines.append(f"{rng.randint(1, 40)} {rng.randint(0, 40)}")
    return "\n".join(lines) + "\n"


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
