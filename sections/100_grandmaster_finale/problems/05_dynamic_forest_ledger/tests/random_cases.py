import argparse
import collections
import random
from pathlib import Path

MOD = 1_000_000_007


def make_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(2, 10)
    q = rng.randint(15, 80)
    values = [rng.randrange(50) for _ in range(n)]
    initial = values.copy()
    edges = set()
    operations = []
    answers = []

    def graph():
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

    def path(u, v):
        adj = graph()
        parent = [-1] * n
        parent[u] = u
        queue = collections.deque([u])
        while queue:
            x = queue.popleft()
            if x == v:
                break
            for y in adj[x]:
                if parent[y] == -1:
                    parent[y] = x
                    queue.append(y)
        if parent[v] == -1:
            return None
        result = []
        while v != u:
            result.append(v)
            v = parent[v]
        result.append(u)
        return result

    for _ in range(q):
        disconnected = [(u, v) for u in range(n) for v in range(u + 1, n)
                        if path(u, v) is None]
        connected = [(u, v) for u in range(n) for v in range(u, n)
                     if path(u, v) is not None]
        choice = rng.random()
        if disconnected and choice < 0.23:
            u, v = rng.choice(disconnected)
            edges.add((u, v))
            operations.append(f"LINK {u + 1} {v + 1}")
        elif edges and choice < 0.38:
            u, v = rng.choice(list(edges))
            edges.remove((u, v))
            operations.append(f"CUT {u + 1} {v + 1}")
        elif choice < 0.70:
            u, v = rng.choice(connected)
            m, b = rng.randrange(8), rng.randrange(15)
            for x in path(u, v):
                values[x] = (m * values[x] + b) % MOD
            operations.append(f"AFFINE {u + 1} {v + 1} {m} {b}")
        else:
            u, v = rng.choice(connected)
            answers.append(sum(values[x] for x in path(u, v)) % MOD)
            operations.append(f"SUM {u + 1} {v + 1}")
    return (f"{n} {q}\n" + " ".join(map(str, initial)) + "\n"
            + "\n".join(operations) + "\n",
            "\n".join(map(str, answers)) + ("\n" if answers else ""))


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
