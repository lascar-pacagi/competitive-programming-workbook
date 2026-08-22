import argparse
import collections
import random
from pathlib import Path

MOD = 998244353


def make_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 48)
    colors = [rng.randrange(2) for _ in range(n)]
    graph = [[] for _ in range(n)]
    edges = []
    for v in range(1, n):
        parent = rng.randrange(v)
        edges.append((parent, v))
        graph[parent].append(v)
        graph[v].append(parent)
    answer = [0] * n
    for source in range(n):
        distance = [-1] * n
        distance[source] = 0
        queue = collections.deque([source])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if distance[v] == -1:
                    distance[v] = distance[u] + 1
                    queue.append(v)
        for target in range(source + 1, n):
            if colors[source] == colors[target]:
                answer[distance[target]] += 1
    text = f"{n}\n" + " ".join(map(str, colors)) + "\n"
    text += "".join(f"{u + 1} {v + 1}\n" for u, v in edges)
    return text, " ".join(str(x % MOD) for x in answer) + "\n"


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
