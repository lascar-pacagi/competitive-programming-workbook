import argparse
import itertools
import random
from pathlib import Path

MOD = 998244353


def solve(n, K, edges):
    counts = [0] * ((n - 1) * K + 1)
    for chosen in itertools.combinations(range(len(edges)), n - 1):
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        ok = True
        total = 0
        for i in chosen:
            u, v, w = edges[i]
            a, b = find(u), find(v)
            if a == b:
                ok = False
                break
            parent[a] = b
            total += w
        if ok:
            counts[total] += 1
    return [c % MOD for c in counts]


def make_case(rng):
    n = rng.randint(1, 6)
    K = rng.randint(0, 4)
    m = rng.randint(0, 10)
    edges = [(rng.randrange(n), rng.randrange(n), rng.randint(0, K)) for _ in range(m)]
    text = f"{n} {m} {K}\n" + "".join(f"{u + 1} {v + 1} {w}\n" for u, v, w in edges)
    return text, " ".join(map(str, solve(n, K, edges))) + "\n"


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
