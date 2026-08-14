import sys

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    q = data[0]
    index = 1
    answers = []
    for _ in range(q):
        r1, m1, r2, m2, earliest = data[index:index+5]
        index += 5
        g, coefficient, _ = extended_gcd(m1, m2)
        difference = r2 - r1
        if difference % g:
            answers.append("-1")
            continue
        period = m1 // g * m2
        k = coefficient * (difference // g) % (m2 // g)
        first = (r1 + m1 * k) % period
        if first < earliest:
            first += (earliest - first + period - 1) // period * period
        answers.append(str(first))
    print("\n".join(answers))

if __name__ == "__main__":
    main()
