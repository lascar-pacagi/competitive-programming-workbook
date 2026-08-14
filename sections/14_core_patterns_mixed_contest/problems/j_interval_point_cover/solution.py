import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    intervals = list(zip(data[1::2], data[2::2]))
    intervals.sort(key=lambda interval: (interval[1], interval[0]))
    last = None
    answer = 0
    for left, right in intervals:
        if last is None or last < left:
            last = right
            answer += 1
    print(answer)


if __name__ == "__main__":
    main()
