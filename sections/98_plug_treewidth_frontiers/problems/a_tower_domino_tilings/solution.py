import sys
MOD = 1000000007

def mul(a, b):
    n = len(a)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for k, x in enumerate(a[i]):
            if x:
                for j, y in enumerate(b[k]):
                    c[i][j] = (c[i][j] + x * y) % MOD
    return c

def main():
    h, w = map(int, sys.stdin.buffer.read().split())
    size = 1 << w
    mat = [[0] * size for _ in range(size)]
    for incoming in range(size):

        def fill(c, used, out):
            if c == w:
                mat[incoming][out] += 1
                return
            bit = 1 << c
            if used & bit:
                fill(c + 1, used, out)
            else:
                if c + 1 < w and (not used & bit << 1):
                    fill(c + 2, used | bit | bit << 1, out)
                fill(c + 1, used | bit, out | bit)
        fill(0, incoming, 0)
    result = [[int(i == j) for j in range(size)] for i in range(size)]
    while h:
        if h & 1:
            result = mul(result, mat)
        mat = mul(mat, mat)
        h //= 2
    print(result[0][0])
if __name__ == '__main__':
    main()
