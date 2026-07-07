import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q = data[0], data[1]
    LOG = max(1, (n + 5).bit_length())
    up = [[0] * (n + 1) for _ in range(LOG)]
    idx = 2
    for v in range(2, n + 1):
        up[0][v] = data[idx]
        idx += 1
    for k in range(1, LOG):
        for v in range(1, n + 1):
            up[k][v] = up[k - 1][up[k - 1][v]]
    out = []
    for _ in range(q):
        v, dist = data[idx], data[idx + 1]
        idx += 2
        bit = 0
        while dist and v:
            if dist & 1:
                v = up[bit][v] if bit < LOG else 0
            dist >>= 1
            bit += 1
        out.append(str(v if v else -1))
    print("\n".join(out))

if __name__ == "__main__":
    main()
