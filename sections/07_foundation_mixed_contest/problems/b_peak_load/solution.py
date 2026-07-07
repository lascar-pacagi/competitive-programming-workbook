"""Reference solution for B. Peak Load."""

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
        m = data[idx + 1]
        idx += 2
        diff = [0] * (m + 2)
        for _ in range(n):
            l = data[idx]
            r = data[idx + 1]
            w = data[idx + 2]
            idx += 3
            diff[l] += w
            diff[r + 1] -= w
        cur = 0
        best = None
        best_time = 1
        for time in range(1, m + 1):
            cur += diff[time]
            if best is None or cur > best:
                best = cur
                best_time = time
        out.append(f"{best} {best_time}")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

