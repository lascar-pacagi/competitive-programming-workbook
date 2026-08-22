import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n, q = map(int, data[:2])
    idx = 2
    a = [0] + list(map(int, data[idx : idx + n]))
    idx += n
    left = [0]
    right = [0]
    total = [0]
    lazy = [0]

    def new(old=0):
        left.append(left[old])
        right.append(right[old])
        total.append(total[old])
        lazy.append(lazy[old])
        return len(total) - 1

    def build(lo, hi):
        node = new()
        if lo == hi:
            total[node] = a[lo]
        else:
            mid = (lo + hi) // 2
            left[node] = build(lo, mid)
            right[node] = build(mid + 1, hi)
            total[node] = total[left[node]] + total[right[node]]
        return node

    def update(old, lo, hi, ql, qr, value):
        node = new(old)
        if ql <= lo and hi <= qr:
            total[node] += value * (hi - lo + 1)
            lazy[node] += value
            return node
        mid = (lo + hi) // 2
        if ql <= mid:
            left[node] = update(left[old], lo, mid, ql, qr, value)
        if qr > mid:
            right[node] = update(right[old], mid + 1, hi, ql, qr, value)
        total[node] = (
            total[left[node]] + total[right[node]] + lazy[node] * (hi - lo + 1)
        )
        return node

    def query(node, lo, hi, ql, qr, carry=0):
        if ql <= lo and hi <= qr:
            return total[node] + carry * (hi - lo + 1)
        carry += lazy[node]
        mid = (lo + hi) // 2
        answer = 0
        if ql <= mid:
            answer += query(left[node], lo, mid, ql, qr, carry)
        if qr > mid:
            answer += query(right[node], mid + 1, hi, ql, qr, carry)
        return answer

    roots = [build(1, n)]
    out = []
    for _ in range(q):
        kind = data[idx].decode()
        v, l, r = map(int, data[idx + 1 : idx + 4])
        idx += 4
        if kind == "A":
            value = int(data[idx])
            idx += 1
            roots.append(update(roots[v], 1, n, l, r, value))
        else:
            out.append(str(query(roots[v], 1, n, l, r)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
