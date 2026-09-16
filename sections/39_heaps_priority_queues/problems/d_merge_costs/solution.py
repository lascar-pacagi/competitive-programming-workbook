import heapq
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    sizes = data[1:]
    heapq.heapify(sizes)

    answer = 0
    while len(sizes) > 1:
        first = heapq.heappop(sizes)
        second = heapq.heappop(sizes)
        merged = first + second

        answer += merged
        heapq.heappush(sizes, merged)

    print(answer)


if __name__ == "__main__":
    main()
