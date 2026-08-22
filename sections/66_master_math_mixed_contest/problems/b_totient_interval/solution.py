import sys

MOD = 1_000_000_007
LIMIT = 1_000_000


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    prefix = list(range(LIMIT + 1))
    for prime in range(2, LIMIT + 1):
        if prefix[prime] == prime:
            for multiple in range(prime, LIMIT + 1, prime):
                prefix[multiple] -= prefix[multiple] // prime
    for value in range(1, LIMIT + 1):
        prefix[value] = (prefix[value] + prefix[value - 1]) % MOD
    memo: dict[int, int] = {}

    def sum_phi(n: int) -> int:
        if n <= 0:
            return 0
        if n <= LIMIT:
            return prefix[n]
        if n in memo:
            return memo[n]
        answer = n * (n + 1) // 2 % MOD
        left = 2
        while left <= n:
            quotient = n // left
            right = n // quotient
            answer = (answer - (right - left + 1) * sum_phi(quotient)) % MOD
            left = right + 1
        memo[n] = answer
        return answer

    output = []
    index = 1
    for _ in range(data[0]):
        left, right = data[index : index + 2]
        index += 2
        output.append(str((sum_phi(right) - sum_phi(left - 1)) % MOD))
    print("\n".join(output))


if __name__ == "__main__":
    main()
