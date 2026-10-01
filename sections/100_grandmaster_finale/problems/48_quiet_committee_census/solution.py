import sys

MOD = 1_000_000_007


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]
    w = data[2:2 + n]
    adj = [0] * n
    pos = 2 + n
    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    h = n // 2          # first half A = vertices 0..h-1, second half B = h..n-1
    b = n - h
    full_b = (1 << b) - 1
    # best[mask] / ways[mask]: optimum and number of optimal independent sets
    # inside the B-subset `mask`.  Split on the lowest vertex v of the mask:
    # either v is unused, or v is used and its neighbours are removed.
    nb_b = [(adj[h + i] >> h) | (1 << i) for i in range(b)]
    best = [0] * (1 << b)
    ways = [1] * (1 << b)
    wb = w[h:]
    for mask in range(1, 1 << b):
        v = (mask & -mask).bit_length() - 1
        a = mask ^ (1 << v)
        c = mask & ~nb_b[v]
        x = best[a]
        y = best[c] + wb[v]
        if x > y:
            best[mask] = x
            ways[mask] = ways[a]
        elif y > x:
            best[mask] = y
            ways[mask] = ways[c]
        else:
            best[mask] = x
            ways[mask] = (ways[a] + ways[c]) % MOD
    # Enumerate independent subsets S of A; each leaves B minus N(S) free.
    adj_a = [adj[i] & ((1 << h) - 1) for i in range(h)]
    to_b = [adj[i] >> h for i in range(h)]
    size = 1 << h
    ok = bytearray(size)
    ok[0] = 1
    total_w = [0] * size
    forbidden = [0] * size
    top = -1
    count = 0
    for mask in range(size):
        if mask:
            v = (mask & -mask).bit_length() - 1
            rest = mask ^ (1 << v)
            if not ok[rest] or adj_a[v] & rest:
                continue
            ok[mask] = 1
            total_w[mask] = total_w[rest] + w[v]
            forbidden[mask] = forbidden[rest] | to_b[v]
        free = full_b & ~forbidden[mask]
        value = total_w[mask] + best[free]
        if value > top:
            top = value
            count = ways[free]
        elif value == top:
            count += ways[free]
    print(top, count % MOD)


if __name__ == "__main__":
    main()
