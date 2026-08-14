import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q = data[0], data[1]
    diff = [0] * (n + 2)
    index = 2
    for _ in range(q):
        left, right, value = data[index:index + 3]
        index += 3
        diff[left] += value
        diff[right + 1] -= value
    current = 0
    best = -10**30
    position = 1
    for i in range(1, n + 1):
        current += diff[i]
        if current > best:
            best, position = current, i
    print(best, position)


if __name__ == "__main__":
    main()
