from __future__ import annotations

import argparse
import math
import random
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    n = data[0]
    a = data[1 : 1 + n]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if math.gcd(a[i], a[j]) == 1:
                ans += 1
    return f"{ans}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 30)
    arr = [rng.randint(1, 200) for _ in range(n)]
    return f"{n}\n" + " ".join(map(str, arr)) + "\n"


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
