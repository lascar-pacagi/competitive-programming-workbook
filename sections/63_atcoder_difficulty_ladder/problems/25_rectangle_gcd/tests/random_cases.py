from __future__ import annotations

import argparse
import itertools
import math
import random
from pathlib import Path


MOD = 1_000_000_007


def exhaustive_count(n: int, k: int) -> int:
    """Independent tiny oracle: enumerate every local string."""
    target = (1 << k) - 1
    answer = 0
    for word in itertools.product(range(k), repeat=n):
        used = 0
        for symbol in word:
            used |= 1 << symbol
        answer += used == target
    return answer


def scale_formula(n: int, k: int) -> int:
    """Direct expected output only for the deliberately non-enumerable case."""
    answer = 0
    for missing in range(k + 1):
        term = math.comb(k, missing) * pow(k - missing, n, MOD)
        answer += term if missing % 2 == 0 else -term
    return answer % MOD


def make_small_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 6)
    k = rng.randint(1, 4)
    return f"{n} {k}\n", f"{exhaustive_count(n, k)}\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for index in range(args.count):
        if index == 0:
            n, k = 10**18 - 12345, 20
            case, expected = f"{n} {k}\n", f"{scale_formula(n, k)}\n"
        else:
            case, expected = make_small_case(rng)
        (args.out_dir / f"case_{index:03d}.in").write_text(case)
        (args.out_dir / f"case_{index:03d}.out").write_text(expected)


if __name__ == "__main__":
    main()
