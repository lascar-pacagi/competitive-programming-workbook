from __future__ import annotations

import argparse
import random
from collections import deque
from pathlib import Path

DIRS = [(1, 0, "D"), (-1, 0, "U"), (0, -1, "L"), (0, 1, "R")]


def solve(case: str) -> str:
    lines = case.strip().splitlines(); n, m = map(int, lines[0].split()); grid = lines[1:]
    inf = 10**9; dist = [[inf]*m for _ in range(n)]; dist[0][0] = 0; dq = deque([(0,0)])
    while dq:
        r,c = dq.popleft()
        for dr,dc,ch in DIRS:
            nr,nc = r+dr,c+dc
            if 0 <= nr < n and 0 <= nc < m:
                w = 0 if grid[r][c] == ch else 1
                nd = dist[r][c] + w
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    (dq.appendleft if w == 0 else dq.append)((nr,nc))
    return f"{dist[n-1][m-1]}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 25); m = rng.randint(1, 25)
    lines = [f"{n} {m}"]
    for _ in range(n):
        lines.append("".join(rng.choice("UDLR") for _ in range(m)))
    return "\n".join(lines) + "\n"


def main() -> None:
    p = argparse.ArgumentParser(); p.add_argument("--count", type=int, required=True); p.add_argument("--seed", type=int, required=True); p.add_argument("--out-dir", type=Path, required=True)
    args = p.parse_args(); rng = random.Random(args.seed); args.out_dir.mkdir(parents=True, exist_ok=True)
    for i in range(args.count):
        case = make_case(rng)
        (args.out_dir / f"case_{i:03d}.in").write_text(case)
        (args.out_dir / f"case_{i:03d}.out").write_text(solve(case))


if __name__ == "__main__":
    main()

