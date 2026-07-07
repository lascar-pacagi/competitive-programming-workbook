from __future__ import annotations

import argparse
import random
from pathlib import Path


def divisors(x: int) -> int:
    ans = 1
    d = 2
    while d * d <= x:
        if x % d == 0:
            exp = 0
            while x % d == 0:
                exp += 1
                x //= d
            ans *= exp + 1
        d += 1
    if x > 1:
        ans *= 2
    return ans


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    q = data[0]
    return "\n".join(str(divisors(x)) for x in data[1 : 1 + q]) + "\n"


def make_case(rng: random.Random) -> str:
    q = rng.randint(1, 60)
    lines = [str(q)]
    for _ in range(q):
        lines.append(str(rng.randint(1, 5000)))
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
