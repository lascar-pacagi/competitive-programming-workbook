import argparse
import itertools
import random
from pathlib import Path


def brute(n, edges, edge_count, wanted):
    best = None
    for chosen in itertools.combinations(range(len(edges)), edge_count):
        parent = list(range(n))

        def find(value):
            while value != parent[value]:
                value = parent[value]
            return value

        total = red_count = 0
        valid = True
        for index in chosen:
            u, v, weight, red = edges[index]
            u, v = find(u), find(v)
            if u == v:
                valid = False
                break
            parent[u] = v
            total += weight
            red_count += red
        if valid and red_count == wanted:
            best = total if best is None else min(best, total)
    return "IMPOSSIBLE" if best is None else str(best)


def make_case(rng):
    n = rng.randint(2, 7)
    possible = [(u, v) for u in range(n) for v in range(u + 1, n)]
    rng.shuffle(possible)
    m = rng.randint(1, min(10, len(possible)))
    edges = [
        (u, v, rng.randint(-10, 15), rng.randrange(2))
        for u, v in possible[:m]
    ]
    components = rng.randint(1, n)
    edge_count = n - components
    wanted = rng.randint(0, edge_count)
    lines = [f"{n} {m} {components} {wanted}"]
    lines.extend(
        f"{u + 1} {v + 1} {weight} {'R' if red else 'B'}"
        for u, v, weight, red in edges
    )
    expected = brute(n, edges, edge_count, wanted)
    return "\n".join(lines) + "\n", expected + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case_id in range(args.count):
        case, expected = make_case(rng)
        stem = f"case_{case_id:03d}"
        (args.out_dir / f"{stem}.in").write_text(case)
        (args.out_dir / f"{stem}.out").write_text(expected)


if __name__ == '__main__':
    main()
