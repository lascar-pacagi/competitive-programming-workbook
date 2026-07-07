"""Reference solution for C. Pair Sum Count."""

from collections import defaultdict
import sys


def count_pairs(values: list[int], target: int) -> int:
    seen: defaultdict[int, int] = defaultdict(int)
    answer = 0
    for value in values:
        answer += seen[target - value]
        seen[value] += 1
    return answer


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
        out.append(str(count_pairs(values, target)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

