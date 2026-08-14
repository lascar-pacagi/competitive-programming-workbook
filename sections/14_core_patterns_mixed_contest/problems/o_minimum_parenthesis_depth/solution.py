import sys


def feasible(s: str, limit: int) -> bool:
    low = high = 0
    for prefix, char in enumerate(s, 1):
        if char == "(":
            low += 1
            high += 1
        elif char == ")":
            low -= 1
            high -= 1
        else:
            low -= 1
            high += 1
        parity = prefix & 1
        if low < 0:
            low = parity
        high = min(high, limit)
        if high & 1 != parity:
            high -= 1
        if low > high:
            return False
    return low == 0


def main() -> None:
    s = sys.stdin.buffer.readline().strip().decode()
    if len(s) % 2 or not feasible(s, len(s)):
        print(-1)
        return
    low, high = 1, len(s)
    while low < high:
        middle = (low + high) // 2
        if feasible(s, middle):
            high = middle
        else:
            low = middle + 1
    print(low)


if __name__ == "__main__":
    main()
