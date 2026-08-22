import heapq
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, low, high = data[:3]
    heap = []
    answer = 0
    at = 3

    for _ in range(n):
        target, weight = data[at : at + 2]
        at += 2
        x = min(high, max(low, target))
        answer += weight * abs(target - x)

        heapq.heappush(heap, (-x, 2 * weight))
        remove = weight
        while remove:
            negative_position, mass = heapq.heappop(heap)
            position = -negative_position
            take = min(remove, mass)
            answer += (position - x) * take
            remove -= take
            mass -= take
            if mass:
                heapq.heappush(heap, (-position, mass))

    print(answer)


if __name__ == "__main__":
    main()
