from __future__ import annotations

import argparse
import random
from pathlib import Path


def egcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    q = data[0]
    idx = 1
    out = []
    for _ in range(q):
        a, b, c = data[idx], data[idx + 1], data[idx + 2]
        idx += 3
        g, x, y = egcd(a, b)
        if c % g:
            out.append("IMPOSSIBLE")
        else:
            scale = c // g
            out.append(f"{x * scale} {y * scale}")
    return "\n".join(out) + "\n"


def make_case(rng: random.Random) -> str:
    q = rng.randint(1, 60)
    lines = [str(q)]
    for _ in range(q):
        lines.append(f"{rng.randint(1, 10**6)} {rng.randint(1, 10**6)} {rng.randint(1, 10**6)}")
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
