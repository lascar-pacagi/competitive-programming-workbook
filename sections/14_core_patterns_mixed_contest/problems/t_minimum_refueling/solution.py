import heapq
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    destination, reachable, n = data[:3]
    stations = sorted(zip(data[3::2], data[4::2]))
    available = []
    index = stops = 0
    while reachable < destination:
        while index < n and stations[index][0] <= reachable:
            heapq.heappush(available, -stations[index][1])
            index += 1
        if not available:
            print(-1)
            return
        reachable -= heapq.heappop(available)
        stops += 1
    print(stops)


if __name__ == "__main__":
    main()
