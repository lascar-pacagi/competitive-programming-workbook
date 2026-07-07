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

    def union(self, a: int, b: int) -> int:
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return self.size[a]
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return self.size[a]


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    it = iter(data)
    n = next(it)
    m = next(it)
    dsu = DSU(n)
    components = n
    largest = 1
    out: list[str] = []
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        if dsu.find(u) != dsu.find(v):
            largest = max(largest, dsu.union(u, v))
            components -= 1
        out.append(f"{components} {largest}")
    return "\n".join(out) + "\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 80)
    m = rng.randint(1, 160)
    lines = [f"{n} {m}"]
    for _ in range(m):
        lines.append(f"{rng.randint(1, n)} {rng.randint(1, n)}")
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

