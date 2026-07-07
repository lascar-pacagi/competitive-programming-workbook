from __future__ import annotations

import argparse
import random
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    it = iter(data)
    n = next(it)
    m = next(it)
    inf = 10**30
    prev = [inf] * m
    for r in range(n):
        cur = [inf] * m
        for c in range(m):
            x = next(it)
            if r == 0 and c == 0:
                cur[c] = x
            else:
                best = prev[c]
                if c:
                    best = min(best, cur[c - 1])
                cur[c] = best + x
        prev = cur
    return f"{prev[-1]}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 35)
    m = rng.randint(1, 35)
    lines = [f"{n} {m}"]
    for _ in range(n):
        row = [rng.randint(0, 2000) for _ in range(m)]
        lines.append(" ".join(map(str, row)))
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

