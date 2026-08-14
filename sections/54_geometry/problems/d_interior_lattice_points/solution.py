import math
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    polygon = [(data[index], data[index + 1]) for index in range(1, 2 * n + 1, 2)]

    signed_double_area = 0
    boundary = 0
    for index, (x1, y1) in enumerate(polygon):
        x2, y2 = polygon[(index + 1) % n]
        signed_double_area += x1 * y2 - y1 * x2
        boundary += math.gcd(abs(x2 - x1), abs(y2 - y1))
    interior = (abs(signed_double_area) - boundary + 2) // 2
    print(interior)


if __name__ == "__main__":
    main()
