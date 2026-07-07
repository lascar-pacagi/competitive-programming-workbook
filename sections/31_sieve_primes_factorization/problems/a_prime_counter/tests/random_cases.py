from __future__ import annotations

import argparse
import random
from pathlib import Path


def is_prime_slow(x: int) -> bool:
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    n, q = data[0], data[1]
    prime = [False] + [is_prime_slow(i) for i in range(1, n + 1)]
    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + int(prime[i])
    idx = 2
    out = []
    for _ in range(q):
        l, r = data[idx], data[idx + 1]
        idx += 2
        out.append(str(pref[r] - pref[l - 1]))
    return "\n".join(out) + "\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 300)
    q = rng.randint(1, 60)
    lines = [f"{n} {q}"]
    for _ in range(q):
        l = rng.randint(1, n)
        r = rng.randint(l, n)
        lines.append(f"{l} {r}")
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
