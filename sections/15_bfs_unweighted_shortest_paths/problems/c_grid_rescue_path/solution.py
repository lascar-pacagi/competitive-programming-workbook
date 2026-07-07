from collections import deque
import sys


DIRS = [(1, 0, "D"), (0, -1, "L"), (0, 1, "R"), (-1, 0, "U")]


def main() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]
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
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if grid[nr][nc] == "#" or dist[nr][nc] != -1:
                continue
            dist[nr][nc] = dist[r][c] + 1
            parent[nr][nc] = (r, c, move)
            q.append((nr, nc))

    if dist[gr][gc] == -1:
        print("NO")
        return

    path: list[str] = []
    r, c = goal
    while (r, c) != start:
        pr, pc, move = parent[r][c]
        path.append(move)
        r, c = pr, pc
    path.reverse()
    print("YES")
    print(len(path))
    print("".join(path))


if __name__ == "__main__":
    main()

