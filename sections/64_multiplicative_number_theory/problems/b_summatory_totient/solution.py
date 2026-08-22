import sys

MOD = 1_000_000_007
LIMIT = 1_000_000


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    phi = list(range(LIMIT + 1))
    for prime in range(2, LIMIT + 1):
        if phi[prime] == prime:
            for multiple in range(prime, LIMIT + 1, prime):
                phi[multiple] -= phi[multiple] // prime
    for value in range(1, LIMIT + 1):
        phi[value] = (phi[value] + phi[value - 1]) % MOD

    memo: dict[int, int] = {}

    def summatory(n: int) -> int:
        if n <= LIMIT:
            return phi[n]
        if n in memo:
            return memo[n]
        answer = n * (n + 1) // 2 % MOD
        left = 2
        while left <= n:
            quotient = n // left
            right = n // quotient
            answer -= (right - left + 1) * summatory(quotient)
            answer %= MOD
            left = right + 1
        memo[n] = answer
        return answer

    print("\n".join(str(summatory(n)) for n in data[1 : 1 + data[0]]))


if __name__ == "__main__":
    main()
