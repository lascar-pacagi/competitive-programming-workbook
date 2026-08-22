import argparse
import random
from pathlib import Path


def make_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 35)
    q = rng.randint(1, 60)
    values = [rng.randint(-30, 30) for _ in range(n)]
    edges = []
    graph = [[] for _ in range(n)]
    for v in range(1, n):
        parent = rng.randrange(v)
        edges.append((parent, v))
        graph[parent].append(v)
        graph[v].append(parent)

    parent = [-1] * n
    depth = [0] * n
    stack = [0]
    for u in stack:
        for v in graph[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            stack.append(v)

    def path(u: int, v: int) -> list[int]:
        left = []
        right = []
        while depth[u] > depth[v]:
            left.append(u)
            u = parent[u]
        while depth[v] > depth[u]:
            right.append(v)
            v = parent[v]
        while u != v:
            left.append(u)
            right.append(v)
            u = parent[u]
            v = parent[v]
        return left + [u] + right[::-1]

    queries = []
    answers = []
    for _ in range(q):
        u = rng.randrange(n)
        v = rng.randrange(n)
        ordered = sorted(values[x] for x in path(u, v))
        median = ordered[(len(ordered) - 1) // 2]
        cost = sum(abs(x - median) for x in ordered)
        queries.append((u, v))
        answers.append((median, cost))

    text = [f"{n} {q}", " ".join(map(str, values))]
    text += [f"{u + 1} {v + 1}" for u, v in edges]
    text += [f"{u + 1} {v + 1}" for u, v in queries]
    output = "".join(f"{median} {cost}\n" for median, cost in answers)
    return "\n".join(text) + "\n", output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for index in range(args.count):
        case_input, case_output = make_case(rng)
        stem = args.out_dir / f"case{index:03d}"
        stem.with_suffix(".in").write_text(case_input)
        stem.with_suffix(".out").write_text(case_output)


if __name__ == "__main__":
    main()
