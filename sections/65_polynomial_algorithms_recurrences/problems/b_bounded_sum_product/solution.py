import heapq
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from ntt import convolution


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, target = data[:2]
    heap: list[tuple[int, int, list[int]]] = []
    serial = 0
    for bound in data[2 : 2 + n]:
        if bound > 0:
            polynomial = [1] * (min(bound, target) + 1)
            heapq.heappush(heap, (len(polynomial), serial, polynomial))
            serial += 1
    if not heap:
        print(int(target == 0))
        return
    while len(heap) > 1:
        _, _, left = heapq.heappop(heap)
        _, _, right = heapq.heappop(heap)
        product = convolution(left, right, target + 1)
        heapq.heappush(heap, (len(product), serial, product))
        serial += 1
    answer = heap[0][2]
    print(answer[target] if target < len(answer) else 0)


if __name__ == "__main__":
    main()
