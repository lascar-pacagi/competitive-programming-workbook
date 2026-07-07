import sys


MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    idx = 1
    ans = 0
    for _ in range(n):
        p, q, v = data[idx], data[idx + 1], data[idx + 2]
        idx += 3
        ans = (ans + v % MOD * p % MOD * pow(q, MOD - 2, MOD)) % MOD
    print(ans)


if __name__ == "__main__":
    main()
