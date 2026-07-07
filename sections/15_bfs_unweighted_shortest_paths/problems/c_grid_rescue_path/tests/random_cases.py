from __future__ import annotations

import argparse
import random
from collections import deque
from pathlib import Path


DIRS = [(1, 0, "D"), (0, -1, "L"), (0, 1, "R"), (-1, 0, "U")]


def solve(case: str) -> str:
    lines = case.strip().splitlines()
    n, m = map(int, lines[0].split())
    grid = [list(row) for row in lines[1:]]
    start = goal = (-1, -1)
    for r in range(n):
        for c in range(m):
            if grid[r][c] == "S":
                start = (r, c)
            elif grid[r][c] == "G":
                goal = (r, c)
    dist = [[-1] * m for _ in range(n)]
    parent = [[None] * m for _ in range(n)]
    sr, sc = start
    gr, gc = goal
    dist[sr][sc] = 0
    q = deque([start])
    while q:
        r, c = q.popleft()
        for dr, dc, move in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != "#" and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                parent[nr][nc] = (r, c, move)
                q.append((nr, nc))
    if dist[gr][gc] == -1:
        return "NO\n"
    path: list[str] = []
    r, c = goal
    while (r, c) != start:
        pr, pc, move = parent[r][c]
        path.append(move)
        r, c = pr, pc
    path.reverse()
    return f"YES\n{len(path)}\n{''.join(path)}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(2, 18)
    m = rng.randint(2, 18)
    cells = [(r, c) for r in range(n) for c in range(m)]
    start, goal = rng.sample(cells, 2)
    grid = [["." for _ in range(m)] for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if (r, c) not in (start, goal) and rng.random() < 0.28:
                grid[r][c] = "#"
    sr, sc = start
    gr, gc = goal
    grid[sr][sc] = "S"
    grid[gr][gc] = "G"
    lines = [f"{n} {m}"] + ["".join(row) for row in grid]
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

