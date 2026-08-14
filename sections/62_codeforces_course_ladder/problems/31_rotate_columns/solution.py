import sys


def build_spf(limit: int) -> list[int]:
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for prime in range(2, int(limit**0.5) + 1):
        if spf[prime] == prime:
            for multiple in range(prime * prime, limit + 1, prime):
                if spf[multiple] == multiple:
                    spf[multiple] = prime
    return spf


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    values = data[1:1 + data[0]]
    spf = build_spf(max(values))
    out = []
    for value in values:
        remaining = value
        multiplier = 1
        while remaining > 1:
            prime = spf[remaining]
            odd_exponent = False
            while remaining % prime == 0:
                odd_exponent = not odd_exponent
                remaining //= prime
            if odd_exponent:
                multiplier *= prime
        out.append(str(multiplier))
    print("\n".join(out))


if __name__ == "__main__":
    main()
