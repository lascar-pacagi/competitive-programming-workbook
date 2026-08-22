import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from ntt import MOD, convolution


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    s, t = data[1].decode(), data[2].decode()
    code = {char: index for index, char in enumerate("ACGT")}
    scores = [n] * n
    for feature in range(3):
        left = [0] * n
        right = [0] * (2 * n)
        for i, (x, y) in enumerate(zip(s, t)):
            a, b = code[x], code[y]
            bit_a = (a & 1) if feature == 0 else (a >> 1) if feature == 1 else ((a & 1) ^ (a >> 1))
            bit_b = (b & 1) if feature == 0 else (b >> 1) if feature == 1 else ((b & 1) ^ (b >> 1))
            left[n - 1 - i] = MOD - 1 if bit_a else 1
            value = MOD - 1 if bit_b else 1
            right[i] = right[i + n] = value
        product = convolution(left, right)
        for shift in range(n):
            scores[shift] = (scores[shift] + product[n - 1 + shift]) % MOD
    inverse_four = pow(4, MOD - 2, MOD)
    matches = [value * inverse_four % MOD for value in scores]
    best = max(matches)
    print(best, matches.index(best))


if __name__ == "__main__":
    main()
