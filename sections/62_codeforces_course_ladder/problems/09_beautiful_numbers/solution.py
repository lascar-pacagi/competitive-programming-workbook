import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    index = 0
    tests = data[index]
    index += 1
    out: list[str] = []
    for _ in range(tests):
        n = data[index]
        index += 1
        intervals = [(data[index + 2 * i], data[index + 2 * i + 1]) for i in range(n)]
        index += 2 * n
        intervals.sort(key=lambda interval: (interval[1], interval[0]))

        last_day: int | None = None
        answer = 0
        for left, right in intervals:
            if last_day is None or last_day < left:
                answer += 1
                last_day = right
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
