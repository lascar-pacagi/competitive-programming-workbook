import argparse
import random
from pathlib import Path

MOD = 998244353


def mat_mul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) % MOD for j in range(n)] for i in range(n)]


def walks(n, edges, N, s, t):
    A = [[0] * n for _ in range(n)]
    for u, v in edges:
        A[u][v] += 1
    R = [[int(i == j) for j in range(n)] for i in range(n)]
    while N:
        if N & 1:
            R = mat_mul(R, A)
        A = mat_mul(A, A)
        N >>= 1
    return R[s][t]


def make_case(rng):
    n = rng.randint(1, 6)
    m = rng.randint(0, 14)
    edges = [(rng.randrange(n), rng.randrange(n)) for _ in range(m)]
    if rng.random() < 0.3:
        edges = [(i, (i + 1) % n) for i in range(n)] + edges[: m // 3]  # periodic
    N = rng.choice([rng.randint(0, 3 * n + 3), rng.randint(0, 10**18)])
    s, t = rng.randrange(n), rng.randrange(n)
    text = f"{n} {len(edges)} {N} {s + 1} {t + 1}\n" + "".join(f"{u + 1} {v + 1}\n" for u, v in edges)
    return text, f"{walks(n, edges, N, s, t)}\n"


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
