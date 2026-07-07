"""Reference solution for C. Subarray Sum Count."""

from collections import defaultdict
import sys


def count_subarrays(values: list[int], target: int) -> int:
    freq = defaultdict(int)
    freq[0] = 1
    prefix = 0
    answer = 0
    for value in values:
        prefix += value
        answer += freq[prefix - target]
        freq[prefix] += 1
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
        out.append(str(count_subarrays(values, target)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

