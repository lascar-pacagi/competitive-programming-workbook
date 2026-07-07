from __future__ import annotations

import argparse
import random
from pathlib import Path


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    it = iter(data)
    n = next(it)
    f = next(it)
    p = next(it)
    dsu = DSU(n)
    components = n
    for _ in range(f):
        u = next(it) - 1
        v = next(it) - 1
        if dsu.union(u, v):
            components -= 1
    edges = []
    for _ in range(p):
        u = next(it) - 1
        v = next(it) - 1
        w = next(it)
        edges.append((w, u, v))
    edges.sort()
    total = 0
    for w, u, v in edges:
        if components == 1:
            break
        if dsu.union(u, v):
            total += w
            components -= 1
    return (str(total) if components == 1 else "IMPOSSIBLE") + "\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 60)
    f = rng.randint(0, 90)
    p = rng.randint(0, 120)
    lines = [f"{n} {f} {p}"]
    for _ in range(f):
        lines.append(f"{rng.randint(1,n)} {rng.randint(1,n)}")
    for _ in range(p):
        lines.append(f"{rng.randint(1,n)} {rng.randint(1,n)} {rng.randint(0,1000)}")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for i in range(args.count):
        case = make_case(rng)
        (args.out_dir / f"case_{i:03d}.in").write_text(case)
        (args.out_dir / f"case_{i:03d}.out").write_text(solve(case))


if __name__ == "__main__":
    main()

