from collections import deque
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, m = map(int, data[:2])
    rows = data[2:2 + n]
    # Two wall cells around every border make every 5-by-5 warp offset safe.
    stride = m + 4
    border = b'#' * stride
    grid = border * 2 + b''.join(b'##' + row + b'##' for row in rows) + border * 2
    start = goal = -1
    for r, row in enumerate(rows):
        c = row.find(b'S')
        if c >= 0: start = (r + 2) * stride + c + 2
        c = row.find(b'G')
        if c >= 0: goal = (r + 2) * stride + c + 2
    inf = 10**9
    dist = [inf] * len(grid)
    dist[start] = 0
    dq = deque([(start, 0)])
    walks = (stride, -stride, 1, -1)
    warps = tuple(
        dr * stride + dc
        for dr in range(-2, 3)
        for dc in range(-2, 3)
    )
    while dq:
        cell, distance = dq.popleft()
        if distance != dist[cell]:
            continue
        if cell == goal:
            print(distance)
            return
        for offset in walks:
            other = cell + offset
            if distance < dist[other] and grid[other] != 35:
                dist[other] = distance
                dq.appendleft((other, distance))
        next_distance = distance + 1
        for offset in warps:
            other = cell + offset
            if next_distance < dist[other] and grid[other] != 35:
                dist[other] = next_distance
                dq.append((other, next_distance))
    print(-1)


if __name__ == '__main__':
    main()
