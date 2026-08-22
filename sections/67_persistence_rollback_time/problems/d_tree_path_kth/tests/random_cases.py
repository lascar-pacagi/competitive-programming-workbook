import argparse
import random
from collections import deque
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=30)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    for case in range(args.count):
        n = rng.randint(1, 18)
        values = [rng.randint(-8, 8) for _ in range(n)]
        edges = [(rng.randrange(v), v) for v in range(1, n)]
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        queries = []
        answers = []
        for _ in range(rng.randint(1, 35)):
            source = rng.randrange(n)
            target = rng.randrange(n)
            parent = [-1] * n
            parent[source] = source
            queue = deque([source])
            while queue:
                u = queue.popleft()
                if u == target:
                    break
                for v in graph[u]:
                    if parent[v] == -1:
                        parent[v] = u
                        queue.append(v)
            path = []
            current = target
            while current != source:
                path.append(current)
                current = parent[current]
            path.append(source)
            ordered = sorted(values[u] for u in path)
            k = rng.randint(1, len(ordered))
            queries.append((source, target, k))
            answers.append(ordered[k - 1])

        input_text = f"{n} {len(queries)}\n"
        input_text += " ".join(map(str, values)) + "\n"
        input_text += "".join(f"{u+1} {v+1}\n" for u, v in edges)
        input_text += "".join(f"{u+1} {v+1} {k}\n" for u, v, k in queries)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(input_text)
        stem.with_suffix(".out").write_text("\n".join(map(str, answers)) + "\n")


if __name__ == "__main__":
    main()
