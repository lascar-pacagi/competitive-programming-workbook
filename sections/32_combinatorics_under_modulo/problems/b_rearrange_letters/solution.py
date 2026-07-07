import sys


MOD = 1_000_000_007


def main() -> None:
    data = sys.stdin.buffer.read().strip()
    if not data:
        return
    n = len(data)
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    counts = [0] * 26
    for ch in data:
        counts[ch - 97] += 1
    answer = fact[n]
    for c in counts:
        answer = answer * pow(fact[c], MOD - 2, MOD) % MOD
    print(answer)


if __name__ == "__main__":
    main()
