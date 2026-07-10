import heapq
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    tasks = [(data[i], data[i + 1]) for i in range(1, 2 * n + 1, 2)]
    tasks.sort(key=lambda task: task[1])
    chosen: list[int] = []
    total = 0
    for duration, deadline in tasks:
        total += duration
        heapq.heappush(chosen, -duration)
        if total > deadline:
            total += heapq.heappop(chosen)
    print(len(chosen))


if __name__ == "__main__":
    main()
