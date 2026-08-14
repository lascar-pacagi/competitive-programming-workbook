import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    s, k = data[0].decode(), int(data[1])
    removals = len(s) - k
    answer = []
    for char in s:
        while removals and answer and answer[-1] > char:
            answer.pop()
            removals -= 1
        answer.append(char)
    print("".join(answer[:k]))


if __name__ == "__main__":
    main()
