from collections import deque
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
        limit = data[index + 1]
        index += 2
        values = data[index:index + n]
        index += n

        maximum: deque[int] = deque()
        minimum: deque[int] = deque()
        left = 0
        answer = 0
        for right, value in enumerate(values):
            while maximum and values[maximum[-1]] <= value:
                maximum.pop()
            maximum.append(right)
            while minimum and values[minimum[-1]] >= value:
                minimum.pop()
            minimum.append(right)

            while values[maximum[0]] - values[minimum[0]] > limit:
                if maximum[0] == left:
                    maximum.popleft()
                if minimum[0] == left:
                    minimum.popleft()
                left += 1
            answer += right - left + 1
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
