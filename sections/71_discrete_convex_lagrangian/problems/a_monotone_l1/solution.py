import heapq
import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    heap = []
    answer = 0
    for x in data[1:]:
        heapq.heappush(heap, -x)
        heapq.heappush(heap, -x)
        answer += -heapq.heappop(heap) - x
    print(answer)


if __name__ == "__main__":
    main()
