import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    p, q = data[0], data[1]
    idx = 2
    out = []
    for _ in range(q):
        a, b = data[idx], data[idx + 1]
        idx += 2
        out.append(str((a % p) * pow(b % p, p - 2, p) % p))
    print("\n".join(out))


if __name__ == "__main__":
    main()
