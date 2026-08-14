import sys
from collections import deque


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, minimum_length, maximum_length = data[:3]
    values = data[3:]
    prefix = [0] * (n + 1)
    for index, value in enumerate(values, 1):
        prefix[index] = prefix[index - 1] + value

    candidates: deque[int] = deque()
    answer = -10**30
    for right in range(1, n + 1):
        entering = right - minimum_length
        if entering >= 0:
            while candidates and prefix[candidates[-1]] >= prefix[entering]:
                candidates.pop()
            candidates.append(entering)
        while candidates and candidates[0] < right - maximum_length:
            candidates.popleft()
        if candidates:
            answer = max(answer, prefix[right] - prefix[candidates[0]])

    print(answer)


if __name__ == "__main__":
    main()
