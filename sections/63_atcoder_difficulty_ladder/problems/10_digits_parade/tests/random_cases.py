from __future__ import annotations

import argparse
import heapq
import random
from pathlib import Path


def dijkstra(grid: list[str]) -> int:
    n = len(grid)
    m = len(grid[0])
    portals = [[] for _ in range(26)]
    start = goal = -1
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            cell_id = r * m + c
            if cell == "S":
                start = cell_id
            elif cell == "G":
                goal = cell_id
            elif "a" <= cell <= "z":
                portals[ord(cell) - ord("a")].append(cell_id)

    inf = 10**9
    dist = [inf] * (n * m)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        current, cell_id = heapq.heappop(heap)
        if current != dist[cell_id]:
            continue
        r, c = divmod(cell_id, m)
        cell = grid[r][c]

        if "a" <= cell <= "z":
            for other in portals[ord(cell) - ord("a")]:
                if current < dist[other]:
                    dist[other] = current
                    heapq.heappush(heap, (current, other))

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != "#":
                other = nr * m + nc
                if current + 1 < dist[other]:
                    dist[other] = current + 1
                    heapq.heappush(heap, (current + 1, other))
    return -1 if dist[goal] == inf else dist[goal]


def scale_case() -> tuple[list[str], int]:
    n = m = 1000
    grid = ["." * m for _ in range(n)]
    grid[0] = "S" + "." * (m - 1)
    grid[-1] = "." * (m - 1) + "G"
    return grid, 1998


def small_case(rng: random.Random) -> tuple[list[str], int]:
    n = rng.randint(1, 7)
    m = rng.randint(1, 7)
    while n * m == 1:
        n = rng.randint(1, 7)
        m = rng.randint(1, 7)

    cells = ["#" if rng.random() < 0.22 else "." for _ in range(n * m)]
    for index in range(n * m):
        if cells[index] != "#" and rng.random() < 0.32:
            cells[index] = rng.choice("abc")
    start, goal = rng.sample(range(n * m), 2)
    cells[start] = "S"
    cells[goal] = "G"
    grid = ["".join(cells[r * m:(r + 1) * m]) for r in range(n)]
    return grid, dijkstra(grid)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for index in range(args.count):
        if index == 0:
            grid, answer = scale_case()
        else:
            grid, answer = small_case(rng)
        prefix = args.out_dir / f"case{index:03d}"
        prefix.with_suffix(".in").write_text(
            f"{len(grid)} {len(grid[0])}\n" + "\n".join(grid) + "\n",
            encoding="utf-8",
        )
        prefix.with_suffix(".out").write_text(f"{answer}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
