from __future__ import annotations

import argparse
import random
from collections import deque
from pathlib import Path


def solve(case: str) -> str:
    lines = case.strip().splitlines(); n, m = map(int, lines[0].split()); grid = [list(x) for x in lines[1:]]
    start = goal = (-1,-1)
    for r in range(n):
        for c in range(m):
            if grid[r][c] == "S": start = (r,c)
            if grid[r][c] == "G": goal = (r,c)
    inf = 10**9; dist = [[inf]*m for _ in range(n)]; dist[start[0]][start[1]] = 0; dq = deque([start])
    while dq:
        r,c = dq.popleft(); d = dist[r][c]
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr,nc = r+dr,c+dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != "#" and d < dist[nr][nc]:
                dist[nr][nc] = d; dq.appendleft((nr,nc))
        for dr in range(-2,3):
            for dc in range(-2,3):
                nr,nc = r+dr,c+dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != "#" and d+1 < dist[nr][nc]:
                    dist[nr][nc] = d+1; dq.append((nr,nc))
    ans = dist[goal[0]][goal[1]]
    return f"{-1 if ans == inf else ans}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(2, 20); m = rng.randint(2, 20)
    cells = [(r,c) for r in range(n) for c in range(m)]
    start, goal = rng.sample(cells, 2)
    grid = [["." if rng.random() > 0.27 else "#" for _ in range(m)] for _ in range(n)]
    grid[start[0]][start[1]] = "S"; grid[goal[0]][goal[1]] = "G"
    return "\n".join([f"{n} {m}"] + ["".join(row) for row in grid]) + "\n"


def main() -> None:
    p = argparse.ArgumentParser(); p.add_argument("--count", type=int, required=True); p.add_argument("--seed", type=int, required=True); p.add_argument("--out-dir", type=Path, required=True)
    args = p.parse_args(); rng = random.Random(args.seed); args.out_dir.mkdir(parents=True, exist_ok=True)
    for i in range(args.count):
        case = make_case(rng)
        (args.out_dir / f"case_{i:03d}.in").write_text(case)
        (args.out_dir / f"case_{i:03d}.out").write_text(solve(case))


if __name__ == "__main__":
    main()

