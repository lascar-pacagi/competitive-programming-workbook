import sys


MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    idx = 1
    none = 1
    for _ in range(n):
        p, q = data[idx], data[idx + 1]
        idx += 2
        none = none * ((q - p) % MOD) % MOD * pow(q, MOD - 2, MOD) % MOD
    print((1 - none) % MOD)


if __name__ == "__main__":
    main()
