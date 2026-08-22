import argparse
import random
from pathlib import Path


def make_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 11)
    query_count = rng.randint(1, 30)
    edges = []
    for v in range(1, n):
        edges.append((rng.randrange(v), v, rng.randint(1, 15)))
    queries = []
    answers = []
    for _ in range(query_count):
        terminals = rng.sample(range(n), rng.randint(1, n))
        terminal_set = set(terminals)
        best = None
        for mask in range(1 << len(edges)):
            parent = list(range(n))

            def find(x):
                while parent[x] != x:
                    x = parent[x]
                return x

            cost = count = 0
            for i, (u, v, weight) in enumerate(edges):
                if mask >> i & 1:
                    cost += weight
                    count += 1
                else:
                    a, b = find(u), find(v)
                    parent[a] = b
            component_counts = {}
            valid = True
            for terminal in terminal_set:
                root = find(terminal)
                component_counts[root] = component_counts.get(root, 0) + 1
                if component_counts[root] > 1:
                    valid = False
                    break
            if valid and (best is None or (cost, count) < best):
                best = cost, count
        queries.append(terminals)
        answers.append(best)
    text = f"{n} {query_count}\n"
    text += "".join(f"{u + 1} {v + 1} {w}\n" for u, v, w in edges)
    text += "".join(f"{len(query)} " + " ".join(str(v + 1) for v in query) + "\n"
                    for query in queries)
    return text, "".join(f"{cost} {count}\n" for cost, count in answers)


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
