import argparse
import itertools
import random
from pathlib import Path


def make_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 7)
    activation = [rng.randint(1, 20) for _ in range(n)]
    possible = [(u, v) for u in range(n) for v in range(n) if u != v]
    m = 0 if not possible else rng.randint(0, min(14, len(possible) + 3))
    edges = []
    for _ in range(m):
        u, v = rng.choice(possible)
        edges.append((u, v, rng.randint(1, 20)))

    answer = None
    if n == 1:
        answer = activation[0]
    else:
        for subset in itertools.combinations(range(m), n - 1):
            indegree = [0] * n
            graph = [[] for _ in range(n)]
            cost = 0
            for i in subset:
                u, v, edge_cost = edges[i]
                indegree[v] += 1
                graph[u].append(v)
                cost += edge_cost
            roots = [v for v in range(n) if indegree[v] == 0]
            if len(roots) != 1 or any(degree > 1 for degree in indegree):
                continue
            root = roots[0]
            seen = {root}
            stack = [root]
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if v not in seen:
                        seen.add(v)
                        stack.append(v)
            if len(seen) == n:
                total = cost + activation[root]
                answer = total if answer is None else min(answer, total)

    text = f"{n} {m}\n" + " ".join(map(str, activation)) + "\n"
    text += "".join(f"{u + 1} {v + 1} {cost}\n" for u, v, cost in edges)
    return text, f"{-1 if answer is None else answer}\n"


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
