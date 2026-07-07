import math
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    d = data[2 : 2 + m]
    answer = 0
    for mask in range(1, 1 << m):
        lcm = 1
        bits = 0
        ok = True
        for i in range(m):
            if (mask >> i) & 1:
                bits += 1
                g = math.gcd(lcm, d[i])
                lcm = lcm // g * d[i]
                if lcm > n:
                    ok = False
                    break
        if not ok:
            continue
        count = n // lcm
        answer += count if bits % 2 == 1 else -count
    print(answer)


if __name__ == "__main__":
    main()
