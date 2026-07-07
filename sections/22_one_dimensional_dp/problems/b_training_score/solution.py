import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    a = data[1:1 + n]
    prev2 = 0
    prev1 = 0
    for x in a:
        cur = max(prev1, prev2 + x)
        prev2, prev1 = prev1, cur
    print(prev1)


if __name__ == "__main__":
    main()

