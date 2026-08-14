import sys


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    q = data[0]
    output = []
    index = 1

    for _ in range(q):
        r1, m1, r2, m2 = data[index:index + 4]
        index += 4
        g, inverse, _ = extended_gcd(m1, m2)
        difference = r2 - r1
        if difference % g:
            output.append("-1")
            continue

        reduced_modulus = m2 // g
        multiplier = (difference // g * inverse) % reduced_modulus
        period = m1 // g * m2
        answer = (r1 + m1 * multiplier) % period
        output.append(str(answer))

    print("\n".join(output))


if __name__ == "__main__":
    main()
