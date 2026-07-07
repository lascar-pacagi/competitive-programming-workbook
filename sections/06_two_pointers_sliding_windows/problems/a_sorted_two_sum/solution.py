"""Reference solution for A. Sorted Two Sum."""

import sys


def exists_pair(values: list[int], target: int) -> bool:
    left = 0
    right = len(values) - 1
    while left < right:
        total = values[left] + values[right]
        if total == target:
            return True
        if total < target:
            left += 1
        else:
            right -= 1
    return False


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        target = data[idx + 1]
        idx += 2
        values = data[idx:idx + n]
        idx += n
        out.append("YES" if exists_pair(values, target) else "NO")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

