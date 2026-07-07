"""Reference solution for C. Deadline Schedule."""

import heapq
import sys


def solve_case(tasks: list[tuple[int, int]]) -> int:
    tasks.sort(key=lambda p: (p[1], p[0]))
    total = 0
    chosen: list[int] = []
    for duration, deadline in tasks:
        total += duration
        heapq.heappush(chosen, -duration)
        if total > deadline:
            total += heapq.heappop(chosen)
    return len(chosen)


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        tasks: list[tuple[int, int]] = []
        for _ in range(n):
            duration = data[idx]
            deadline = data[idx + 1]
            idx += 2
            tasks.append((duration, deadline))
        out.append(str(solve_case(tasks)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

