import math
import sys


MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, k = data

    answer = 0
    for missing in range(k + 1):
        term = math.comb(k, missing) * pow(k - missing, n, MOD)
        if missing % 2 == 0:
            answer += term
        else:
            answer -= term
    print(answer % MOD)


if __name__ == "__main__":
    main()
