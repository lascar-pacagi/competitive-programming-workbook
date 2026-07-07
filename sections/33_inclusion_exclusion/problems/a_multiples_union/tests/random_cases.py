from __future__ import annotations

import argparse
import random
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    n, m = data[0], data[1]
    d = data[2 : 2 + m]
    count = 0
    for x in range(1, n + 1):
        if any(x % v == 0 for v in d):
            count += 1
    return f"{count}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 300)
    m = rng.randint(1, 8)
    d = [rng.randint(1, 40) for _ in range(m)]
    return f"{n} {m}\n" + " ".join(map(str, d)) + "\n"


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
