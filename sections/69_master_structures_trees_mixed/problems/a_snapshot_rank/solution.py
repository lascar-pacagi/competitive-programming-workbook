import sys


def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    idx = 0
    maximum = int(tokens[idx])
    q = int(tokens[idx + 1])
    idx += 2
    log = (q + 1).bit_length()
    up = [[0] * (q + 1) for _ in range(log)]
    roots = [0] * (q + 1)
    depth = [0] * (q + 1)
    left = [0]
    right = [0]
    count = [0]
    versions = 0

    def add(old, lo, hi, pos):
        node = len(count)
        left.append(left[old])
        right.append(right[old])
        count.append(count[old] + 1)
        if lo != hi:
            mid = (lo + hi) // 2
            if pos <= mid:
                left[node] = add(left[old], lo, mid, pos)
            else:
                right[node] = add(right[old], mid + 1, hi, pos)
        return node

    def ancestor(v, steps):
        bit = 0
        while steps:
            if steps & 1:
                v = up[bit][v]
            steps //= 2
            bit += 1
        return v

    def kth(before, after, k):
        lo, hi = 1, maximum
        while lo != hi:
            amount = count[left[after]] - count[left[before]]
            mid = (lo + hi) // 2
            if k <= amount:
                before = left[before]
                after = left[after]
                hi = mid
            else:
                k -= amount
                before = right[before]
                after = right[after]
                lo = mid + 1
        return lo

    out = []
    for _ in range(q):
        kind = tokens[idx].decode()
        idx += 1
        if kind == "A":
            v = int(tokens[idx])
            x = int(tokens[idx + 1])
            idx += 2
            versions += 1
            depth[versions] = depth[v] + 1
            up[0][versions] = v
            for j in range(1, log):
                up[j][versions] = up[j - 1][up[j - 1][versions]]
            roots[versions] = add(roots[v], 1, maximum, x)
        else:
            v, l, r, k = map(int, tokens[idx : idx + 4])
            idx += 4
            rv = ancestor(v, depth[v] - r)
            lv = ancestor(v, depth[v] - l + 1)
            out.append(str(kth(roots[lv], roots[rv], k)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
