import sys


def main() -> None:
    s = sys.stdin.buffer.readline().strip().decode()
    n = len(s)
    prefix_low = [0] * (n + 1)
    prefix_high = [0] * (n + 1)
    for i, char in enumerate(s):
        if prefix_low[i] > prefix_high[i]:
            prefix_low[i + 1], prefix_high[i + 1] = 1, 0
            continue
        low, high = prefix_low[i], prefix_high[i]
        if char == "(":
            low += 1
            high += 1
        elif char == ")":
            low -= 1
            high -= 1
        else:
            low -= 1
            high += 1
        if low < 0:
            low = (i + 1) & 1
        prefix_low[i + 1] = low
        prefix_high[i + 1] = high

    if n % 2 or not prefix_low[n] <= 0 <= prefix_high[n]:
        print("IMPOSSIBLE")
        return

    suffix_low = [0] * (n + 1)
    suffix_high = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        if suffix_low[i + 1] > suffix_high[i + 1]:
            suffix_low[i], suffix_high[i] = 1, 0
            continue
        low, high = suffix_low[i + 1], suffix_high[i + 1]
        if s[i] == "(":
            low = 1 if low == 0 else low - 1
            high -= 1
        elif s[i] == ")":
            low += 1
            high += 1
        else:
            low = 1 if low == 0 else low - 1
            high += 1
        suffix_low[i], suffix_high[i] = low, high

    answer = list(s)
    for i, char in enumerate(s):
        if char != "?":
            continue
        after_low, after_high = suffix_low[i + 1], suffix_high[i + 1]
        can_open = max(prefix_low[i] + 1, after_low) <= min(
            prefix_high[i] + 1, after_high)
        closing_low = max(prefix_low[i], 1) - 1
        can_close = max(closing_low, after_low) <= min(
            prefix_high[i] - 1, after_high)
        if can_open and not can_close:
            answer[i] = "("
        elif can_close and not can_open:
            answer[i] = ")"
    print("".join(answer))


if __name__ == "__main__":
    main()
