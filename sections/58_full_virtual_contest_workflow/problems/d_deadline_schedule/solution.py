import heapq
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    tasks = [(data[index + 1], data[index]) for index in range(1, 2 * n + 1, 2)]
    tasks.sort()

    kept: list[int] = []  # Negative durations make Python's min-heap a max-heap.
    total = 0
    for deadline, duration in tasks:
        heapq.heappush(kept, -duration)
        total += duration
        if total > deadline:
            total += heapq.heappop(kept)
    print(len(kept))


if __name__ == "__main__":
    main()
