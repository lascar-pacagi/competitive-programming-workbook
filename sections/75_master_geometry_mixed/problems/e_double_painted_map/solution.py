import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    events = []
    ys = []
    for _ in range(n):
        x1, y1, x2, y2 = next(it), next(it), next(it), next(it)
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        if x1 != x2 and y1 != y2:
            events.extend(((x1, y1, y2, 1), (x2, y1, y2, -1)))
            ys.extend((y1, y2))
    if not events:
        print(0)
        return
    ys = sorted(set(ys))
    index = {y: i for i, y in enumerate(ys)}
    m = len(ys) - 1
    cover = [0] * (4 * m)
    one = [0] * (4 * m)
    two = [0] * (4 * m)

    def update(x, l, r, ql, qr, d):
        if qr <= l or r <= ql:
            return
        if ql <= l and r <= qr:
            cover[x] += d
        else:
            mid = (l + r) // 2
            update(2 * x, l, mid, ql, qr, d)
            update(2 * x + 1, mid, r, ql, qr, d)
        full = ys[r] - ys[l]
        child1 = 0 if r - l == 1 else one[2 * x] + one[2 * x + 1]
        child2 = 0 if r - l == 1 else two[2 * x] + two[2 * x + 1]
        if cover[x] >= 2:
            one[x] = two[x] = full
        elif cover[x] == 1:
            one[x], two[x] = full, child1
        else:
            one[x], two[x] = child1, child2

    events.sort()
    ans = 0
    last = events[0][0]
    i = 0
    while i < len(events):
        x = events[i][0]
        ans += (x - last) * two[1]
        while i < len(events) and events[i][0] == x:
            _, y1, y2, d = events[i]
            update(1, 0, m, index[y1], index[y2], d)
            i += 1
        last = x
    print(ans)


if __name__ == "__main__":
    main()
