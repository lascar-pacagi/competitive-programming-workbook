import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    target = data[1]
    values = sorted(data[2:])
    covered = index = patches = 0
    while covered < target:
        if index < len(values) and values[index] <= covered + 1:
            covered += values[index]
            index += 1
        else:
            covered += covered + 1
            patches += 1
    print(patches)


if __name__ == "__main__":
    main()
