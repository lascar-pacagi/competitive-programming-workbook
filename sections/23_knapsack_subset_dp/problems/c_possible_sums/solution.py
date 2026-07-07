import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    a = data[1:1 + n]
    total = sum(a)
    possible = [False] * (total + 1)
    possible[0] = True
    current = 0
    for x in a:
        for s in range(current, -1, -1):
            if possible[s]:
                possible[s + x] = True
        current += x
    ans = [i for i in range(1, total + 1) if possible[i]]
    print(len(ans))
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

