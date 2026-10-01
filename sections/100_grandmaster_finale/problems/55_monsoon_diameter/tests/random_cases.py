import argparse
import random
from pathlib import Path


def solve(n, m, edges):
    adj = [[] for _ in range(n)]
    for u, v, a, b in edges:
        adj[u].append((v, a, b))
        adj[v].append((u, a, b))
    points = set()
    for s in range(n):
        stack = [(s, -1, 0, 0)]
        while stack:
            v, p, A, B = stack.pop()
            points.add((A, B))
            for w, a, b in adj[v]:
                if w != p:
                    stack.append((w, v, A + a, B + b))
    return [max(A * t + B for A, B in points) for t in range(m)]


def make_case(rng):
    n = rng.randint(1, 10)
    m = rng.randint(1, 12)
    top_a = rng.choice([0, 3, 100000])
    top_b = rng.choice([0, 10, 10**9])
    edges = []
    for v in range(1, n):
        p = rng.randrange(v) if rng.random() < 0.6 else 0  # stars stress binarization
        edges.append((p, v, rng.randint(0, top_a), rng.randint(0, top_b)))
    perm = list(range(n))
    rng.shuffle(perm)
    edges = [(perm[u], perm[v], a, b) for u, v, a, b in edges]
    rng.shuffle(edges)
    text = f"{n} {m}\n" + "".join(f"{u + 1} {v + 1} {a} {b}\n" for u, v, a, b in edges)
    return text, " ".join(map(str, solve(n, m, edges))) + "\n"


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
