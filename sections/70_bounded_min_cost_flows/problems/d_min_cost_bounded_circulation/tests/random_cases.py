import argparse
import itertools
import random
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=30)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    for case in range(args.count):
        n = rng.randint(1, 5)
        m = rng.randint(0, 7)
        edges = []
        for _ in range(m):
            u = rng.randrange(n)
            v = rng.randrange(n)
            while n > 1 and v == u:
                v = rng.randrange(n)
            high = rng.randint(0, 3)
            low = rng.randint(0, high)
            cost = rng.randint(0, 7)
            edges.append((u, v, low, high, cost))

        best = None
        ranges = [range(low, high + 1) for _, _, low, high, _ in edges]
        for flows in itertools.product(*ranges):
            balance = [0] * n
            cost = 0
            for flow, (u, v, _, _, price) in zip(flows, edges):
                balance[u] -= flow
                balance[v] += flow
                cost += flow * price
            if all(amount == 0 for amount in balance):
                best = cost if best is None else min(best, cost)

        text = f"{n} {m}\n"
        text += "".join(
            f"{u+1} {v+1} {low} {high} {cost}\n"
            for u, v, low, high, cost in edges
        )
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(text)
        expected = "IMPOSSIBLE" if best is None else str(best)
        stem.with_suffix(".out").write_text(expected + "\n")


if __name__ == "__main__":
    main()
