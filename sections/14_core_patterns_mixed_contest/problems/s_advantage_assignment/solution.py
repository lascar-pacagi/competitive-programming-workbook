import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = sorted(data[1:n + 1])
    b = sorted(data[n + 1:])
    target = wins = 0
    for value in a:
        if value > b[target]:
            target += 1
            wins += 1
            if target == n:
                break
    print(wins)


if __name__ == "__main__":
    main()
