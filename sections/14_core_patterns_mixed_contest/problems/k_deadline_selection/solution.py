import heapq
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    jobs = list(zip(data[1::2], data[2::2]))
    jobs.sort(key=lambda job: (job[1], job[0]))
    selected = []
    total = 0
    for duration, deadline in jobs:
        heapq.heappush(selected, -duration)
        total += duration
        if total > deadline:
            total += heapq.heappop(selected)
    print(len(selected))


if __name__ == "__main__":
    main()
