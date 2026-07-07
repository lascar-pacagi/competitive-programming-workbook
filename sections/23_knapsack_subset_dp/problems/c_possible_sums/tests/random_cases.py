from __future__ import annotations

import argparse
import random
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    n = data[0]
    a = data[1:1 + n]
    total = sum(a)
    possible = [False] * (total + 1)
    possible[0] = True
    current = 0
    for x in a:
        for s in range(current, -1, -1):
            if possible[s]:
                possible[s + x] = True
        current += x
    ans = [i for i in range(1, total + 1) if possible[i]]
    return f"{len(ans)}\n" + " ".join(map(str, ans)) + "\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 35)
    a = [rng.randint(1, 80) for _ in range(n)]
    return f"{n}\n" + " ".join(map(str, a)) + "\n"


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

