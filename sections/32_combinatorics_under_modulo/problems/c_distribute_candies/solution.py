import sys


MOD = 1_000_000_007


def prepare(limit: int) -> tuple[list[int], list[int]]:
    fact = [1] * (limit + 1)
    for i in range(1, limit + 1):
        fact[i] = fact[i - 1] * i % MOD
    invfact = [1] * (limit + 1)
    invfact[limit] = pow(fact[limit], MOD - 2, MOD)
    for i in range(limit, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD
    return fact, invfact


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    q = data[0]
    queries = [(data[i], data[i + 1]) for i in range(1, 2 * q + 1, 2)]
    limit = max(n + s - 1 for n, s in queries)
    fact, invfact = prepare(limit)
    out = []
    for n, s in queries:
        total = n + s - 1
        choose = n - 1
        out.append(str(fact[total] * invfact[choose] % MOD * invfact[total - choose] % MOD))
    print("\n".join(out))


if __name__ == "__main__":
    main()
