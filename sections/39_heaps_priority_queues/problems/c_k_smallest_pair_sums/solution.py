import heapq
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m, k = data[0], data[1], data[2]
    a = data[3:3 + n]
    b = data[3 + n:3 + n + m]
    heap = [(a[i] + b[0], i, 0) for i in range(n)]
    heapq.heapify(heap)
    out = []
    for _ in range(k):
        s, i, j = heapq.heappop(heap)
        out.append(str(s))
        if j + 1 < m:
            heapq.heappush(heap, (a[i] + b[j + 1], i, j + 1))
    print(" ".join(out))

if __name__ == "__main__":
    main()
