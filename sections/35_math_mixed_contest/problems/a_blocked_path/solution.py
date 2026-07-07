import sys


MOD = 1_000_000_007


def prepare(n: int) -> tuple[list[int], list[int]]:
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    invfact = [1] * (n + 1)
    invfact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD
    return fact, invfact


def comb(n: int, k: int, fact: list[int], invfact: list[int]) -> int:
    if k < 0 or k > n:
        return 0
    return fact[n] * invfact[k] % MOD * invfact[n - k] % MOD


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    h, w, r, c = data
    fact, invfact = prepare(h + w)
    total = comb(h + w - 2, h - 1, fact, invfact)
    through = comb(r + c - 2, r - 1, fact, invfact) * comb(h - r + w - c, h - r, fact, invfact) % MOD
    print((total - through) % MOD)


if __name__ == "__main__":
    main()
