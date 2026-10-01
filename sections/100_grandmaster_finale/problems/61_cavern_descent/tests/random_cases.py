import argparse
import random
from pathlib import Path


def solve(n, a, b, parent):
    children = [[] for _ in range(n)]
    for v in range(1, n):
        children[parent[v]].append(v)
    dp = [0] * n
    # parent[v] < v, so reverse index order is a post-order.
    for v in range(n - 1, -1, -1):
        if not children[v]:
            continue
        best = None
        stack = list(children[v])
        while stack:
            u = stack.pop()
            value = a[v] * b[u] + dp[u]
            if best is None or value < best:
                best = value
            stack.extend(children[u])
        dp[v] = best
    return dp


def make_case(rng):
    n = rng.randint(1, 12)
    span = rng.choice([3, 50, 100000])
    a = [rng.randint(-span, span) for _ in range(n)]
    b = [rng.randint(-span, span) for _ in range(n)]
    shape = rng.random()
    parent = [0] * n
    for v in range(1, n):
        parent[v] = v - 1 if shape < 0.3 else rng.randrange(v)
    perm = list(range(1, n))
    rng.shuffle(perm)
    label = [0] + perm  # vertex v is printed as label[v] + 1; root stays 1
    dp = solve(n, a, b, parent)
    out_a = [0] * n
    out_b = [0] * n
    out_dp = [0] * n
    for v in range(n):
        out_a[label[v]] = a[v]
        out_b[label[v]] = b[v]
        out_dp[label[v]] = dp[v]
    edges = [(label[v] + 1, label[parent[v]] + 1) for v in range(1, n)]
    rng.shuffle(edges)
    edges = [(u, v) if rng.random() < 0.5 else (v, u) for u, v in edges]
    text = f"{n}\n{' '.join(map(str, out_a))}\n{' '.join(map(str, out_b))}\n"
    text += "".join(f"{u} {v}\n" for u, v in edges)
    return text, " ".join(map(str, out_dp)) + "\n"


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
