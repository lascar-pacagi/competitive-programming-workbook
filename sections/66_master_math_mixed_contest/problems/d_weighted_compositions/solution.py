import heapq
import sys
from pathlib import Path

SECTION_65 = Path(__file__).resolve().parents[3] / "65_polynomial_algorithms_recurrences"
sys.path.insert(0, str(SECTION_65))
from ntt import convolution


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, target = data[:2]
    heap: list[tuple[int, int, list[int]]] = []
    index = 2
    serial = 0
    for _ in range(n):
        weight, cap = data[index : index + 2]
        index += 2
        maximum = min(target, weight * cap)
        polynomial = [0] * (maximum + 1)
        for value in range(0, maximum + 1, weight):
            polynomial[value] = 1
        if len(polynomial) > 1:
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
