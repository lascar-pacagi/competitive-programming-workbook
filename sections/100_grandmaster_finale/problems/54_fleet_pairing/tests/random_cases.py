import argparse
import random
from pathlib import Path


def solve(n, edges):
    weight = {}
    for u, v, w in edges:
        if u != v:
            key = (min(u, v), max(u, v))
            weight[key] = max(weight.get(key, 0), w)
    adj = [[] for _ in range(n)]
    for (u, v), w in weight.items():
        adj[u].append((v, w))
        adj[v].append((u, w))
    best = [0] * (1 << n)
    # best[mask] = optimum using only vertices in mask; lowest vertex is either
    # unmatched or matched to a neighbour inside the mask.
    for mask in range(1, 1 << n):
        low = (mask & -mask).bit_length() - 1
        rest = mask ^ (1 << low)
        value = best[rest]
        for v, w in adj[low]:
            if rest >> v & 1:
                value = max(value, w + best[rest ^ (1 << v)])
        best[mask] = value
    return best[(1 << n) - 1]


def make_case(rng):
    n = rng.randint(1, 12)
    m = rng.randint(0, 40)
    top = rng.choice([1, 3, 10, 10**6])
    edges = [(rng.randrange(n), rng.randrange(n), rng.randint(1, top)) for _ in range(m)]
    text = f"{n} {m}\n" + "".join(f"{u + 1} {v + 1} {w}\n" for u, v, w in edges)
    return text, f"{solve(n, edges)}\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        case_input, case_output = make_case(rng)
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(case_input)
        stem.with_suffix(".out").write_text(case_output)


if __name__ == "__main__":
    main()
