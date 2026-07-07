from collections import deque
import sys


DIRS = [(1, 0, "D"), (-1, 0, "U"), (0, -1, "L"), (0, 1, "R")]


def main() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    inf = 10**9
    dist = [[inf] * m for _ in range(n)]
    dist[0][0] = 0
    dq = deque([(0, 0)])
    while dq:
        r, c = dq.popleft()
        for dr, dc, ch in DIRS:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            w = 0 if grid[r][c] == ch else 1
            nd = dist[r][c] + w
            if nd < dist[nr][nc]:
                dist[nr][nc] = nd
                if w == 0:
                    dq.appendleft((nr, nc))
                else:
                    dq.append((nr, nc))
    print(dist[n - 1][m - 1])


if __name__ == "__main__":
    main()

