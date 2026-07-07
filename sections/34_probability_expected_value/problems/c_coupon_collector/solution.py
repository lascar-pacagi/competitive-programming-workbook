import sys


MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    q = data[0]
    values = data[1 : 1 + q]
    limit = max(values)
    inv = [0] * (limit + 1)
    harmonic = [0] * (limit + 1)
    for i in range(1, limit + 1):
        inv[i] = pow(i, MOD - 2, MOD)
        harmonic[i] = (harmonic[i - 1] + inv[i]) % MOD
    print("\n".join(str(n * harmonic[n] % MOD) for n in values))


if __name__ == "__main__":
    main()
