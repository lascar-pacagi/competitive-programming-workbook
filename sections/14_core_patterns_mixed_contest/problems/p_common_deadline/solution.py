import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    limit = data[1]
    total = answer = 0
    for duration in sorted(data[2:]):
        if total + duration > limit:
            break
        total += duration
        answer += 1
    print(answer)


if __name__ == "__main__":
    main()
