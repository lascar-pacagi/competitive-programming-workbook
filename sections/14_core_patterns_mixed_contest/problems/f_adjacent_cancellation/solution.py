import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    output = []
    for token in data[1:]:
        stack = []
        for char in token:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        output.append(bytes(stack).decode() if stack else "EMPTY")
    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()
