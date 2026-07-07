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


def comb(n: int, r: int, fact: list[int], invfact: list[int]) -> int:
    if r < 0 or r > n:
        return 0
    return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    q = data[0]
    queries = [(data[i], data[i + 1], data[i + 2]) for i in range(1, 3 * q + 1, 3)]
    limit = max(n + s for n, s, _ in queries)
    fact, invfact = prepare(limit)
    out = []
    for n, s, b in queries:
        ans = 0
        step = b + 1
        for bad in range(0, min(n, s // step) + 1):
            remaining = s - bad * step
            term = comb(n, bad, fact, invfact) * comb(remaining + n - 1, n - 1, fact, invfact) % MOD
            ans += term if bad % 2 == 0 else -term
        out.append(str(ans % MOD))
    print("\n".join(out))


if __name__ == "__main__":
    main()
