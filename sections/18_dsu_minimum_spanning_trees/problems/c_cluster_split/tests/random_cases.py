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
    m = next(it)
    k = next(it)
    edges = []
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        w = next(it)
        edges.append((w, u, v))
    edges.sort()
    dsu = DSU(n)
    components = n
    total = 0
    for w, u, v in edges:
        if components == k:
            break
        if dsu.union(u, v):
            components -= 1
            total += w
    return ("IMPOSSIBLE\n" if components != k else f"{total}\n")


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 70)
    k = rng.randint(1, n)
    m = rng.randint(0, 180)
    lines = [f"{n} {m} {k}"]
    for _ in range(m):
        u = rng.randint(1, n)
        v = rng.randint(1, n)
        w = rng.randint(0, 1000)
        lines.append(f"{u} {v} {w}")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for index in range(args.count):
        case = make_case(rng)
        (args.out_dir / f"case_{index:03d}.in").write_text(case, encoding="utf-8")
        (args.out_dir / f"case_{index:03d}.out").write_text(solve(case), encoding="utf-8")


if __name__ == "__main__":
    main()

