import sys
from collections import deque


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n, m = map(int, data[:2])
    grid = [row.decode() for row in data[2:2 + n]]
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
    expanded = [False] * 26
    dist[start] = 0
    dq = deque([start])

    while dq:
        cell_id = dq.popleft()
        r, c = divmod(cell_id, m)
        current = dist[cell_id]
        cell = grid[r][c]

        if "a" <= cell <= "z":
            letter = ord(cell) - ord("a")
            if not expanded[letter]:
                expanded[letter] = True
                for other in portals[letter]:
                    if current < dist[other]:
                        dist[other] = current
                        dq.appendleft(other)

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != "#":
                other = nr * m + nc
                if current + 1 < dist[other]:
                    dist[other] = current + 1
                    dq.append(other)

    print(-1 if dist[goal] == inf else dist[goal])


if __name__ == "__main__":
    main()
