import math
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    q = data[0]
    idx = 1
    out = []
    for _ in range(q):
        a, b = data[idx], data[idx + 1]
        idx += 2
        g = math.gcd(a, b)
        out.append(f"{g} {a // g * b}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
