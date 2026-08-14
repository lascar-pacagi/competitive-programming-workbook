import sys


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    q = data[0]
    values = iter(data[1:])
    answer: list[str] = []
    for _ in range(q):
        a = next(values)
        b = next(values)
        m = next(values)
        g, coefficient, _ = extended_gcd(a, m)
        if b % g:
            answer.append("-1")
            continue
        reduced_modulus = m // g
        answer.append(str((coefficient * (b // g)) % reduced_modulus))
    sys.stdout.write("\n".join(answer) + "\n")


if __name__ == "__main__":
    main()
