import heapq
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    intervals = [(data[i], data[i + 1]) for i in range(1, 2 * n + 1, 2)]
    intervals.sort()
    heap = []
    ans = 0
    for l, r in intervals:
        while heap and heap[0] <= l:
            heapq.heappop(heap)
        heapq.heappush(heap, r)
        ans = max(ans, len(heap))
    print(ans)

if __name__ == "__main__":
    main()
