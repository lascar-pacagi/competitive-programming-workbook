import sys


def sieve(n: int) -> list[bool]:
    is_prime = [True] * (n + 1)
    if n >= 0:
        is_prime[0] = False
    if n >= 1:
        is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for x in range(p * p, n + 1, p):
                is_prime[x] = False
        p += 1
    return is_prime


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q = data[0], data[1]
    is_prime = sieve(n)
    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + int(is_prime[i])
    idx = 2
    out = []
    for _ in range(q):
        l, r = data[idx], data[idx + 1]
        idx += 2
        out.append(str(pref[r] - pref[l - 1]))
    print("\n".join(out))


if __name__ == "__main__":
    main()
