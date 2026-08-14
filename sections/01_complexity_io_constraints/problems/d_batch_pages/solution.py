import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    q = data[0]
    out = []
    index = 1
    for _ in range(q):
        n, k = data[index], data[index + 1]
        index += 2
        if n == 0:
            out.append("0 0")
            continue
        pages = (n - 1) // k + 1
        out.append(f"{pages} {pages * k - n}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
