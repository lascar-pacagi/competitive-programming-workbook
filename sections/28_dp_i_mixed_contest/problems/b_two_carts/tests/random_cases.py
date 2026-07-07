from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    it = iter(data)
    n = next(it)
    cap_a = next(it)
    cap_b = next(it)
    items = [(next(it), next(it)) for _ in range(n)]
    if n <= 12:
        best = 0
        for choices in itertools.product(range(3), repeat=n):
            wa = wb = value = 0
            ok = True
            for choice, (w, v) in zip(choices, items):
                if choice == 1:
                    wa += w
                    value += v
                elif choice == 2:
                    wb += w
                    value += v
                if wa > cap_a or wb > cap_b:
                    ok = False
                    break
            if ok:
                best = max(best, value)
        return f"{best}\n"
    dp = [[0] * (cap_b + 1) for _ in range(cap_a + 1)]
    for weight, value in items:
        for a in range(cap_a, -1, -1):
            for b in range(cap_b, -1, -1):
                cur = dp[a][b]
                if a + weight <= cap_a:
                    dp[a + weight][b] = max(dp[a + weight][b], cur + value)
                if b + weight <= cap_b:
                    dp[a][b + weight] = max(dp[a][b + weight], cur + value)
    return f"{max(max(row) for row in dp)}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 10)
    cap_a = rng.randint(1, 20)
    cap_b = rng.randint(1, 20)
    lines = [f"{n} {cap_a} {cap_b}"]
    for _ in range(n):
        lines.append(f"{rng.randint(1, 20)} {rng.randint(1, 100)}")
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
