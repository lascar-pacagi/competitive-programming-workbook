import sys


def spf_table(n: int) -> list[int]:
    spf = list(range(n + 1))
    if n >= 0:
        spf[0] = 0
    if n >= 1:
        spf[1] = 1
    for p in range(2, n + 1):
        if spf[p] == p and p * p <= n:
            for x in range(p * p, n + 1, p):
                if spf[x] == x:
                    spf[x] = p
    return spf


def signature(x: int, spf: list[int]) -> tuple[int, int, int]:
    if x == 1:
        return 0, 0, 1
    distinct = total = 0
    largest = 1
    while x > 1:
        p = spf[x]
        distinct += 1
        largest = p
        while x % p == 0:
            total += 1
            x //= p
    return distinct, total, largest


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    q = data[0]
    values = data[1 : 1 + q]
    spf = spf_table(max(values))
    out = []
    for x in values:
        out.append("{} {} {}".format(*signature(x, spf)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
