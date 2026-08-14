import argparse
import random
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        n = rng.randint(1, 20)
        edges = [(u, v) for u in range(n) for v in range(u + 1, n) if rng.random() < .15]
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        for u, v in edges:
            a, b = find(u), find(v)
            if a != b: parent[a] = b
        sizes = {}
        for i in range(n): sizes[find(i)] = sizes.get(find(i), 0) + 1
        lines = [f"{n} {len(edges)}"] + [f"{u+1} {v+1}" for u, v in edges]
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text("\n".join(lines) + "\n")
        stem.with_suffix(".out").write_text(f"{len(sizes)} {len(sizes)-1} {max(sizes.values())}\n")


if __name__ == "__main__":
    main()
