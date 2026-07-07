import heapq
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    low, high = [], []
    out = []
    for x in data[1:1 + n]:
        if not low or x <= -low[0]:
            heapq.heappush(low, -x)
        else:
            heapq.heappush(high, x)
        if len(low) < len(high):
            heapq.heappush(low, -heapq.heappop(high))
        if len(low) > len(high) + 1:
            heapq.heappush(high, -heapq.heappop(low))
        out.append(str(-low[0]))
    print(" ".join(out))

if __name__ == "__main__":
    main()
