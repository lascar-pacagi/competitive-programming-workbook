import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    values = data[1:]

    # Indices of strict prefix minima: all useful left endpoints.
    candidates: list[int] = []
    for i in range(n):
        if not candidates or values[i] < values[candidates[-1]]:
            candidates.append(i)

    answer = 0
    for j in range(n - 1, -1, -1):
        while candidates and values[candidates[-1]] <= values[j]:
            answer = max(answer, j - candidates.pop())

    print(answer)


if __name__ == "__main__":
    main()
