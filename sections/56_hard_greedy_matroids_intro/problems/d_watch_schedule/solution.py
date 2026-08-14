import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    intervals = sorted(((data[index], data[index + 1]) for index in range(1, len(data), 2)), key=lambda item: item[1])
    answer = 0
    available_from = -1
    for start, end in intervals:
        if start >= available_from:
            answer += 1
            available_from = end
    print(answer)


if __name__ == "__main__":
    main()
