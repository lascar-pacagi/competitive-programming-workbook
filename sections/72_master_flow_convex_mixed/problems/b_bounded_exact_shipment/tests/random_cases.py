import argparse
import itertools
import random
from pathlib import Path


def brute(n, edges, exact):
    best = None
    ranges = [range(low, high + 1) for _, _, low, high, _ in edges]
    for flow in itertools.product(*ranges):
        balance = [0] * n
        cost = 0
        for amount, (u, v, _, _, edge_cost) in zip(flow, edges):
            balance[u] -= amount
            balance[v] += amount
            cost += amount * edge_cost
        if balance[0] != -exact or balance[-1] != exact:
            continue
        if any(balance[v] for v in range(1, n - 1)):
            continue
        best = cost if best is None else min(best, cost)
    return "IMPOSSIBLE" if best is None else str(best)


def make_case(rng):
    n = rng.randint(2, 5)
    possible = [(u, v) for u in range(n) for v in range(n) if u != v]
    rng.shuffle(possible)
    m = rng.randint(1, min(7, len(possible)))
    edges = []
    for u, v in possible[:m]:
        high = rng.randint(0, 2)
        low = rng.randint(0, high)
        edges.append((u, v, low, high, rng.randint(0, 6)))
    exact = rng.randint(0, 2)
    lines = [f"{n} {m} {exact}", f"1 {n}"]
    lines.extend(
        f"{u + 1} {v + 1} {low} {high} {cost}"
        for u, v, low, high, cost in edges
    )
    return "\n".join(lines) + "\n", brute(n, edges, exact) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case_id in range(args.count):
        case, expected = make_case(rng)
        stem = f"case_{case_id:03d}"
        (args.out_dir / f"{stem}.in").write_text(case)
        (args.out_dir / f"{stem}.out").write_text(expected)


if __name__ == '__main__':
    main()
