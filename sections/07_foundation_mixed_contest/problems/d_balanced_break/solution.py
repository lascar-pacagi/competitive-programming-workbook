import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    index, out = 1, []
    for _ in range(data[0]):
        n = data[index]
        index += 1
        a = data[index:index + n]
        index += n
        total = sum(a)
        left, best, position = 0, None, 1
        for i in range(n - 1):
            left += a[i]
            diff = abs(left - (total - left))
            if best is None or diff < best:
                best, position = diff, i + 1
        out.append(f"{best} {position}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
