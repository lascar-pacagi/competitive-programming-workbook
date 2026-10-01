import argparse
import random
from pathlib import Path


def steiner(n, parent, weight, order, l, r):
    marked = [0] * (n + 1)
    for v in range(l, r + 1):
        marked[v] = 1
    total_marked = r - l + 1
    below = marked[:]
    answer = 0
    for v in reversed(order):
        if parent[v]:
            if 0 < below[v] < total_marked:
                answer += weight[v]
            below[parent[v]] += below[v]
    return answer


def make_case(rng):
    n = rng.randint(1, 10)
    top = rng.choice([1, 9, 10**9])
    edges = []
    for v in range(2, n + 1):
        p = v - 1 if rng.random() < 0.3 else rng.randint(1, v - 1)
        edges.append((p, v, rng.randint(1, top)))
    # relabel all vertices (vertex 1 need not be special)
    perm = list(range(1, n + 1))
    rng.shuffle(perm)
    edges = [(perm[a - 1], perm[b - 1], w) for a, b, w in edges]
    rng.shuffle(edges)
    adj = [[] for _ in range(n + 1)]
    for a, b, w in edges:
        adj[a].append((b, w))
        adj[b].append((a, w))
    parent = [0] * (n + 1)
    weight = [0] * (n + 1)
    order = [1]
    seen = [False] * (n + 1)
    seen[1] = True
    for v in order:
        for w, c in adj[v]:
            if not seen[w]:
                seen[w] = True
                parent[w] = v
                weight[w] = c
                order.append(w)
    q = rng.randint(1, 15)
    queries = []
    for _ in range(q):
        l = rng.randint(1, n)
        queries.append((l, rng.randint(l, n)))
    text = f"{n} {q}\n" + "".join(f"{a} {b} {w}\n" for a, b, w in edges)
    text += "".join(f"{l} {r}\n" for l, r in queries)
    answers = [steiner(n, parent, weight, order, l, r) for l, r in queries]
    return text, "\n".join(map(str, answers)) + "\n"


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
