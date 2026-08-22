import sys


def main():
    s = sys.stdin.buffer.readline().decode().strip()
    n = len(s)
    first, second, offset = 0, 1, 0
    while first < n and second < n and offset < n:
        a, b = s[(first + offset) % n], s[(second + offset) % n]
        if a == b:
            offset += 1
            continue
        if a > b:
            first += offset + 1
            if first == second:
                first += 1
        else:
            second += offset + 1
            if first == second:
                second += 1
        offset = 0
    start = min(first, second)
    print(s[start:] + s[:start])
    print(start + 1)


if __name__ == "__main__":
    main()
