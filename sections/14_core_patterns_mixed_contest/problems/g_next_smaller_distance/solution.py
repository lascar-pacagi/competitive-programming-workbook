import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, values = data[0], data[1:]
    answer = [0] * n
    stack = []
    for index, value in enumerate(values):
        while stack and value < values[stack[-1]]:
            previous = stack.pop()
            answer[previous] = index - previous
        stack.append(index)
    print(" ".join(map(str, answer)))


if __name__ == "__main__":
    main()
