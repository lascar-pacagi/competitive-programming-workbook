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
        a, m = data[idx], data[idx + 1]
        idx += 2
        if m == 1:
            out.append("0")
            continue
        g, x, _ = egcd(a, m)
        out.append(str(x % m) if g == 1 else "-1")
    print("\n".join(out))


if __name__ == "__main__":
    main()
