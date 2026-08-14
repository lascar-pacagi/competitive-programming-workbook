import collections
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    values = sorted(data[1:])
    remaining = collections.Counter(values)
    need = collections.Counter()
    for value in values:
        if remaining[value] == 0:
            continue
        if need[value] > 0:
            remaining[value] -= 1
            need[value] -= 1
            need[value + 1] += 1
        elif remaining[value + 1] > 0 and remaining[value + 2] > 0:
            remaining[value] -= 1
            remaining[value + 1] -= 1
            remaining[value + 2] -= 1
            need[value + 3] += 1
        else:
            print("NO")
            return
    print("YES")


if __name__ == "__main__":
    main()
