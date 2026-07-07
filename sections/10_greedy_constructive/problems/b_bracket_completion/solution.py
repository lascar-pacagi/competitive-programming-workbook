"""Reference solution for B. Bracket Completion."""

import sys


def complete(s: str) -> str:
    n = len(s)
    if n % 2:
        return "IMPOSSIBLE"
    need_open = n // 2 - s.count("(")
    need_close = n // 2 - s.count(")")
    if need_open < 0 or need_close < 0:
        return "IMPOSSIBLE"

    chars = list(s)
    for i, ch in enumerate(chars):
        if ch == "?":
            if need_open > 0:
                chars[i] = "("
                need_open -= 1
            else:
                chars[i] = ")"
                need_close -= 1

    balance = 0
    for i, ch in enumerate(chars):
        balance += 1 if ch == "(" else -1
        if balance < 0:
            return "IMPOSSIBLE"
        if i + 1 < n and balance == 0:
            return "IMPOSSIBLE"
    if balance != 0:
        return "IMPOSSIBLE"
    return "".join(chars)


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    t = int(data[0])
    out: list[str] = []
    for i in range(1, t + 1):
        out.append(complete(data[i].decode()))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

