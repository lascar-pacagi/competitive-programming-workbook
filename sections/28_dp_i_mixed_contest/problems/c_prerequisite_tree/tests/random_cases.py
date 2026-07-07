from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    it = iter(data)
    n = next(it)
    budget = next(it)
    time = [0] * n
    value = [0] * n
    for i in range(n):
        time[i] = next(it)
        value[i] = next(it)
    parent = [-1] * n
    children = [[] for _ in range(n)]
    for child in range(1, n):
        p = next(it) - 1
        parent[child] = p
        children[p].append(child)

    if n <= 18:
        best = 0
        for mask in range(1 << n):
            total_t = total_v = 0
            ok = True
            for u in range(n):
                if (mask >> u) & 1:
                    if parent[u] != -1 and not ((mask >> parent[u]) & 1):
                        ok = False
                        break
                    total_t += time[u]
                    total_v += value[u]
            if ok and total_t <= budget:
                best = max(best, total_v)
        return f"{best}\n"

    neg = -10**18
    order = [0]
    for u in order:
        order.extend(children[u])
    dp = [[neg] * (budget + 1) for _ in range(n)]
    for u in reversed(order):
        if time[u] <= budget:
            dp[u][time[u]] = value[u]
        for v in children[u]:
            merged = dp[u][:]
            for used in range(budget + 1):
                if dp[u][used] <= neg // 2:
                    continue
                for add in range(1, budget - used + 1):
                    if dp[v][add] <= neg // 2:
                        continue
                    merged[used + add] = max(merged[used + add], dp[u][used] + dp[v][add])
            dp[u] = merged
    return f"{max(0, max(dp[0]))}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 12)
    budget = rng.randint(1, 35)
    lines = [f"{n} {budget}"]
    for _ in range(n):
        lines.append(f"{rng.randint(1, min(12, budget))} {rng.randint(1, 100)}")
    parents = [rng.randint(1, child) for child in range(1, n)]
    if parents:
        lines.append(" ".join(map(str, parents)))
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
