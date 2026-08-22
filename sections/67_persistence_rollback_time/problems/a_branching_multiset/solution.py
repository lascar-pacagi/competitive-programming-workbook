import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    maximum, q = map(int, data[:2])
    index = 2
    left = [0]
    right = [0]
    count = [0]
    roots = [0]

    def update(old, lo, hi, pos, delta):
        node = len(count)
        left.append(left[old])
        right.append(right[old])
        count.append(count[old] + delta)
        if lo != hi:
            mid = (lo + hi) // 2
            if pos <= mid:
                left[node] = update(left[old], lo, mid, pos, delta)
            else:
                right[node] = update(right[old], mid + 1, hi, pos, delta)
        return node

    def prefix(node, lo, hi, x):
        if not node or x < lo:
            return 0
        if hi <= x:
            return count[node]
        mid = (lo + hi) // 2
        return prefix(left[node], lo, mid, x) + prefix(right[node], mid + 1, hi, x)

    def kth(node, lo, hi, k):
        while lo != hi:
            mid = (lo + hi) // 2
            amount = count[left[node]]
            if k <= amount:
                node = left[node]
                hi = mid
            else:
                k -= amount
                node = right[node]
                lo = mid + 1
        return lo

    output = []
    for _ in range(q):
        kind = data[index].decode()
        version = int(data[index + 1])
        x = int(data[index + 2])
        index += 3
        if kind in "IE":
            roots.append(
                update(roots[version], 1, maximum, x, 1 if kind == "I" else -1)
            )
        elif kind == "K":
            output.append(str(kth(roots[version], 1, maximum, x)))
        else:
            output.append(str(prefix(roots[version], 1, maximum, x)))
    print("\n".join(output))


if __name__ == "__main__":
    main()
