import sys

MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    q = data[0]
    queries = data[1:1 + q]
    maximum = max(queries, default=1)

    phi = list(range(maximum + 1))
    for p in range(2, maximum + 1):
        if phi[p] != p:
            continue
        for multiple in range(p, maximum + 1, p):
            phi[multiple] -= phi[multiple] // p

    prefix = [0] * (maximum + 1)
    for value in range(1, maximum + 1):
        prefix[value] = (prefix[value - 1] + phi[value]) % MOD

    print("\n".join(str(prefix[n]) for n in queries))


if __name__ == "__main__":
    main()
