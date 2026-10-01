import argparse
import random
from pathlib import Path


def mst(n, edges, weight):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    total = 0
    for i in sorted(range(len(edges)), key=lambda i: weight[i]):
        a, b = find(edges[i][0]), find(edges[i][1])
        if a != b:
            parent[a] = b
            total += weight[i]
    return total


def make_case(rng):
    n = rng.randint(1, 8)
    m = rng.randint(max(1, n - 1), 14)
    edges = [(rng.randrange(v), v) for v in range(1, n)]
    while len(edges) < m:
        edges.append((rng.randrange(n), rng.randrange(n)))  # loops allowed
    rng.shuffle(edges)
    top = rng.choice([3, 20, 10**9])
    weight = [rng.randint(1, top) for _ in edges]
    q = rng.randint(1, 20)
    lines = [f"{n} {m} {q}"]
    lines += [f"{u + 1} {v + 1} {w}" for (u, v), w in zip(edges, weight)]
    answers = []
    for _ in range(q):
        e = rng.randrange(m)
        w = rng.randint(1, top)
        weight[e] = w
        lines.append(f"{e + 1} {w}")
        answers.append(mst(n, edges, weight))
    return "\n".join(lines) + "\n", "\n".join(map(str, answers)) + "\n"


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
