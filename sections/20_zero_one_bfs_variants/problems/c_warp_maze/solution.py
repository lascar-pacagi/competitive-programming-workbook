from collections import deque
import sys


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
    inf = 10**9
    dist = [[inf] * m for _ in range(n)]
    sr, sc = start
    dist[sr][sc] = 0
    dq = deque([start])
    while dq:
        r, c = dq.popleft()
        d = dist[r][c]
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != "#" and d < dist[nr][nc]:
                dist[nr][nc] = d
                dq.appendleft((nr, nc))
        for dr in range(-2, 3):
            for dc in range(-2, 3):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != "#" and d + 1 < dist[nr][nc]:
                    dist[nr][nc] = d + 1
                    dq.append((nr, nc))
    gr, gc = goal
    print(-1 if dist[gr][gc] == inf else dist[gr][gc])


if __name__ == "__main__":
    main()

