"""Reference solution for A. Range Sum Queries."""

import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        q = data[idx + 1]
        idx += 2
        prefix = [0]
        for value in data[idx:idx + n]:
            prefix.append(prefix[-1] + value)
        idx += n
        for _ in range(q):
            l = data[idx]
            r = data[idx + 1]
            idx += 2
            out.append(str(prefix[r] - prefix[l - 1]))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

