import sys


MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    q = data[0]
    idx = 1
    out = []
    for _ in range(q):
        a, b, x, k = data[idx], data[idx + 1], data[idx + 2], data[idx + 3]
        idx += 4
        a %= MOD
        b %= MOD
        x %= MOD
        if k == 0:
            out.append(str(x))
            continue
        ak = pow(a, k, MOD)
        if a == 1:
            geom = k % MOD
        else:
            geom = (ak - 1) * pow(a - 1, MOD - 2, MOD) % MOD
        out.append(str((ak * x + b * geom) % MOD))
    print("\n".join(out))


if __name__ == "__main__":
    main()
