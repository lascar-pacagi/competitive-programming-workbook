import sys


MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        p, q = data[idx], data[idx + 1]
        idx += 2
        out.append(str(q % MOD * pow(p, MOD - 2, MOD) % MOD))
    print("\n".join(out))


if __name__ == "__main__":
    main()
