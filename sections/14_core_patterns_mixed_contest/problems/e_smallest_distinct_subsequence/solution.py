import sys


def solve(s: str) -> str:
    remaining = [0] * 26
    for char in s:
        remaining[ord(char) - 97] += 1
    used = [False] * 26
    stack = []
    for char in s:
        index = ord(char) - 97
        remaining[index] -= 1
        if used[index]:
            continue
        while stack and stack[-1] > char and remaining[ord(stack[-1]) - 97]:
            used[ord(stack.pop()) - 97] = False
        stack.append(char)
        used[index] = True
    return "".join(stack)


def main() -> None:
    data = sys.stdin.read().split()
    print("\n".join(solve(s) for s in data[1:]))


if __name__ == "__main__":
    main()
