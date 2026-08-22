import sys
from pathlib import Path

SECTION_65 = Path(__file__).resolve().parents[3] / "65_polynomial_algorithms_recurrences"
sys.path.insert(0, str(SECTION_65))
from ntt import convolution


def correlation(left: list[int], right: list[int]) -> list[int]:
    n = len(left)
    product = convolution(left[::-1], right + right)
    return product[n - 1 : 2 * n - 1]


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    s, t = data[1].decode(), data[2].decode()
    both = correlation([c != "?" for c in s], [c != "?" for c in t])
    matches = [0] * n
    for letter in "ACGT":
        same = correlation([c == letter for c in s], [c == letter for c in t])
        for shift in range(n):
            matches[shift] += same[shift]
    valid = [shift for shift in range(n) if both[shift] == matches[shift]]
    print(len(valid), valid[0] if valid else -1)


if __name__ == "__main__":
    main()
