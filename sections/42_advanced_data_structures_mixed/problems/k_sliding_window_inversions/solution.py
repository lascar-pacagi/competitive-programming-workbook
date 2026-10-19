import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = data[:2]
    a = data[2:]
    rank = {x: i + 1 for i, x in enumerate(sorted(set(a)))}
    a = [rank[x] for x in a]
    m = len(rank)
    bit = [0] * (m + 1)

    def add(i, delta):
        while i <= m:
            bit[i] += delta
            i += i & -i

    def prefix(i):
        total = 0
        while i:
            total += bit[i]
            i -= i & -i
        return total

    inversions = 0
    out = []
    for i, x in enumerate(a):
        if i >= k:
            old = a[i - k]
            inversions -= prefix(old - 1)
            add(old, -1)
        present = min(i, k - 1)
        inversions += present - prefix(x)
        add(x, 1)
        if i >= k - 1:
            out.append(inversions)
    print(" ".join(map(str, out)))


if __name__ == "__main__":
    main()
