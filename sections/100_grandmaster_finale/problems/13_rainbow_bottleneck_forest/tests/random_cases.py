import argparse
import itertools
import random
from pathlib import Path


def make_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(2, 8)
    m = rng.randint(0, min(15, n * (n - 1)))
    need = rng.randint(1, n - 1)
    edges = []
    for _ in range(m):
        u = rng.randrange(n)
        v = rng.randrange(n - 1)
        if v >= u:
            v += 1
        edges.append((u, v, rng.randint(1, max(1, n - 2)), rng.randint(1, 20)))

    answer = None
    for subset in itertools.combinations(range(m), need):
        if len({edges[i][2] for i in subset}) != need:
            continue
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        valid = True
        for i in subset:
            u, v, _, _ = edges[i]
            u, v = find(u), find(v)
            if u == v:
                valid = False
                break
            parent[u] = v
        if valid:
            bottleneck = max(edges[i][3] for i in subset)
            answer = bottleneck if answer is None else min(answer, bottleneck)

    text = f"{n} {m} {need}\n"
    text += "".join(f"{u + 1} {v + 1} {color} {weight}\n"
                    for u, v, color, weight in edges)
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
