import sys


def egcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    q = data[0]
    idx = 1
    out = []
    for _ in range(q):
        a, b, c = data[idx], data[idx + 1], data[idx + 2]
        idx += 3
        g, x, y = egcd(a, b)
        if c % g != 0:
            out.append("IMPOSSIBLE")
        else:
            scale = c // g
            out.append(f"{x * scale} {y * scale}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
