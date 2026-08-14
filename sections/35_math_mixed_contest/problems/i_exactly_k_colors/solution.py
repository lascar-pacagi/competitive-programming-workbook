import sys


MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    q = data[0]
    queries = [tuple(data[i:i + 3]) for i in range(1, 1 + 3 * q, 3)]
    maximum_m = max(m for _, m, _ in queries)

    factorial = [1] * (maximum_m + 1)
    for i in range(1, maximum_m + 1):
        factorial[i] = factorial[i - 1] * i % MOD
    inverse_factorial = [1] * (maximum_m + 1)
    inverse_factorial[-1] = pow(factorial[-1], MOD - 2, MOD)
    for i in range(maximum_m, 0, -1):
        inverse_factorial[i - 1] = inverse_factorial[i] * i % MOD

    def choose(n: int, k: int) -> int:
        return (
            factorial[n]
            * inverse_factorial[k]
            * inverse_factorial[n - k]
            % MOD
        )

    output = []
    for length, colors, used in queries:
        onto = 0
        for missing in range(used + 1):
            term = (
                choose(used, missing)
                * pow(used - missing, length, MOD)
                % MOD
            )
            onto += -term if missing & 1 else term
        answer = choose(colors, used) * (onto % MOD) % MOD
        output.append(str(answer))
    print("\n".join(output))


if __name__ == "__main__":
    main()
