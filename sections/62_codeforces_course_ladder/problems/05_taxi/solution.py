import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    index = 1
    out = []
    for _ in range(data[0]):
        n, k = data[index], data[index + 1]
        index += 2
        values = sorted(data[index:index + n])
        index += n
        out.append(str(min(values[left + k - 1] - values[left] for left in range(n - k + 1))))
    print("\n".join(out))


if __name__ == "__main__":
    main()
