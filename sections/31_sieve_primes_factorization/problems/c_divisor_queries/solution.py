import sys


def spf_table(n: int) -> list[int]:
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    for p in range(2, n + 1):
        if spf[p] == p and p * p <= n:
            for x in range(p * p, n + 1, p):
                if spf[x] == x:
                    spf[x] = p
    return spf


def divisors(x: int, spf: list[int]) -> int:
    ans = 1
    while x > 1:
        p = spf[x]
        exp = 0
        while x % p == 0:
            exp += 1
            x //= p
        ans *= exp + 1
    return ans


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    q = data[0]
    values = data[1 : 1 + q]
    spf = spf_table(max(values))
    print("\n".join(str(divisors(x, spf)) for x in values))


if __name__ == "__main__":
    main()
