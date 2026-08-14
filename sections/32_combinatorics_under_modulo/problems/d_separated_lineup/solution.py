import sys

MOD = 1_000_000_007


def prepare(limit: int) -> tuple[list[int], list[int]]:
    fact = [1] * (limit + 1)
    for value in range(1, limit + 1):
        fact[value] = fact[value - 1] * value % MOD
    invfact = [1] * (limit + 1)
    invfact[limit] = pow(fact[limit], MOD - 2, MOD)
    for value in range(limit, 0, -1):
        invfact[value - 1] = invfact[value] * value % MOD
    return fact, invfact


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    q = data[0]
    queries = [(data[index], data[index + 1]) for index in range(1, 2 * q + 1, 2)]
    limit = max(max(red, blue + 1) for red, blue in queries)
    fact, invfact = prepare(limit)

    output: list[str] = []
    for red, blue in queries:
        if red > blue + 1:
            output.append("0")
            continue
        slots = fact[blue + 1] * invfact[red] % MOD * invfact[blue + 1 - red] % MOD
        output.append(str(slots * fact[red] % MOD * fact[blue] % MOD))
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
