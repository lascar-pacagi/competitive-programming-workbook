from __future__ import annotations

import argparse
import random
from pathlib import Path


MOD = 1_000_000_007


def fast_answer(a: int, b: int, x: int, k: int) -> int:
    a %= MOD
    b %= MOD
    x %= MOD
    if k == 0:
        return x
    ak = pow(a, k, MOD)
    if a == 1:
        geom = k % MOD
    else:
        geom = (ak - 1) * pow(a - 1, MOD - 2, MOD) % MOD
    return (ak * x + b * geom) % MOD


def brute_answer(a: int, b: int, x: int, k: int) -> int:
    a %= MOD
    b %= MOD
    x %= MOD
    for _ in range(k):
        x = (a * x + b) % MOD
    return x


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    q = data[0]
    idx = 1
    out = []
    for _ in range(q):
        a, b, x, k = data[idx], data[idx + 1], data[idx + 2], data[idx + 3]
        idx += 4
        if k <= 60:
            out.append(str(brute_answer(a, b, x, k)))
        else:
            out.append(str(fast_answer(a, b, x, k)))
    return "\n".join(out) + "\n"


def make_case(rng: random.Random) -> str:
    q = rng.randint(1, 40)
    lines = [str(q)]
    for _ in range(q):
        if rng.random() < 0.7:
            k = rng.randint(0, 60)
        else:
            k = rng.randint(0, 10**12)
        lines.append(
            f"{rng.randint(0, 10**12)} {rng.randint(0, 10**12)} "
            f"{rng.randint(0, 10**12)} {k}"
        )
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
