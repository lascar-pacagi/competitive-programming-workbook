import argparse
import random
from pathlib import Path


def make_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 55)
    q = rng.randint(1, 100)
    labels = "".join(rng.choice("abcde") for _ in range(n))
    graph = [[] for _ in range(n)]
    edges = []
    for v in range(1, n):
        parent = rng.randrange(v)
        edges.append((parent, v))
        graph[parent].append(v)
        graph[v].append(parent)
    parent = [-1] * n
    depth = [0] * n
    order = [0]
    for u in order:
        for v in graph[u]:
            if v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)

    def path_string(u, v):
        left = []
        right = []
        while depth[u] > depth[v]:
            left.append(labels[u])
            u = parent[u]
        while depth[v] > depth[u]:
            right.append(labels[v])
            v = parent[v]
        while u != v:
            left.append(labels[u])
            right.append(labels[v])
            u = parent[u]
            v = parent[v]
        return "".join(left) + labels[u] + "".join(reversed(right))

    queries = []
    answers = []
    for _ in range(q):
        u, v, x, y = [rng.randrange(n) for _ in range(4)]
        first = path_string(u, v)
        second = path_string(x, y)
        lcp = 0
        while lcp < min(len(first), len(second)) and first[lcp] == second[lcp]:
            lcp += 1
        comparison = (first > second) - (first < second)
        queries.append((u, v, x, y))
        answers.append((lcp, comparison))
    text = f"{n} {q}\n{labels}\n"
    text += "".join(f"{u + 1} {v + 1}\n" for u, v in edges)
    text += "".join(f"{u + 1} {v + 1} {x + 1} {y + 1}\n"
                    for u, v, x, y in queries)
    return text, "".join(f"{lcp} {comparison}\n" for lcp, comparison in answers)


def main() -> None:
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
