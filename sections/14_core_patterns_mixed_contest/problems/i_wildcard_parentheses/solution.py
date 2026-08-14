import sys


def possible(s):
    if len(s) % 2:
        return False
    low = high = 0
    for index, char in enumerate(s):
        if char == 40:
            low += 1
            high += 1
        elif char == 41:
            low -= 1
            high -= 1
        else:
            low -= 1
            high += 1
        if low < 0:
            low = (index + 1) & 1
        if high < 0:
            return False
    return low == 0


def main() -> None:
    data = sys.stdin.buffer.read().split()
    print("\n".join("YES" if possible(s) else "NO" for s in data[1:]))


if __name__ == "__main__":
    main()
