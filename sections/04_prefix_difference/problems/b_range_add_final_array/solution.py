"""Reference solution for B. Range Add Final Array."""

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
        diff = [0] * (n + 2)
        for _ in range(q):
            l = data[idx]
            r = data[idx + 1]
            x = data[idx + 2]
            idx += 3
            diff[l] += x
            diff[r + 1] -= x
        cur = 0
        values: list[str] = []
        for i in range(1, n + 1):
            cur += diff[i]
            values.append(str(cur))
        out.append(" ".join(values))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

