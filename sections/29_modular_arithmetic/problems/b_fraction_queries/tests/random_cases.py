from __future__ import annotations

import argparse
import random
from pathlib import Path


PRIMES = [2, 3, 5, 7, 11, 17, 97, 1000000007]


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    p, q = data[0], data[1]
    idx = 2
    out = []
    for _ in range(q):
        a, b = data[idx], data[idx + 1]
        idx += 2
        out.append(str((a % p) * pow(b % p, p - 2, p) % p))
    return "\n".join(out) + "\n"


def make_case(rng: random.Random) -> str:
    p = rng.choice(PRIMES)
    q = rng.randint(1, 40)
    lines = [f"{p} {q}"]
    for _ in range(q):
        a = rng.randint(0, 10**12)
        b = rng.randint(1, 10**12)
        while b % p == 0:
            b = rng.randint(1, 10**12)
        lines.append(f"{a} {b}")
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
