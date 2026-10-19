import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, q = map(int, data[:2])
    s = bytearray(data[2])
    size = 1 << (n - 1).bit_length()
    total = [0] * (2 * size)
    low = [0] * (2 * size)
    for i, c in enumerate(s):
        total[size + i] = 1 if c == 40 else -1
        low[size + i] = min(0, total[size + i])
    for v in range(size - 1, 0, -1):
        total[v] = total[2*v] + total[2*v+1]
        low[v] = min(low[2*v], total[2*v] + low[2*v+1])
    out = []
    pos = 3
    for _ in range(q):
        op = data[pos]; pos += 1
        if op == b'T':
            i = int(data[pos]) - 1; pos += 1
            v = size + i
            total[v] = -total[v]; low[v] = min(0, total[v])
            v //= 2
            while v:
                total[v] = total[2*v] + total[2*v+1]
                low[v] = min(low[2*v], total[2*v] + low[2*v+1])
                v //= 2
        else:
            l, r = int(data[pos]) - 1 + size, int(data[pos+1]) + size
            pos += 2
            ls = lm = rs = rm = 0
            while l < r:
                if l & 1:
                    lm = min(lm, ls + low[l]); ls += total[l]; l += 1
                if r & 1:
                    r -= 1
                    rm = min(low[r], total[r] + rm); rs += total[r]
                l //= 2; r //= 2
            out.append('YES' if ls + rs == 0 and min(lm, ls + rm) >= 0 else 'NO')
    print('\n'.join(out))


if __name__ == '__main__':
    main()
