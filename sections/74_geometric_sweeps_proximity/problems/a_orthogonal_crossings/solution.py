import bisect, sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    h, v = next(it), next(it)
    events = []
    ys = []
    for _ in range(h):
        x1, x2, y = next(it), next(it), next(it)
        x1, x2 = sorted((x1, x2))
        events.extend(((x1, 0, y, y, 1), (x2, 2, y, y, -1)))
        ys.append(y)
    for _ in range(v):
        x, y1, y2 = next(it), next(it), next(it)
        y1, y2 = sorted((y1, y2))
        events.append((x, 1, y1, y2, 1))
        ys.extend((y1, y2))
    ys = sorted(set(ys))
    bit = [0] * (len(ys) + 1)

    def add(i, x):
        i += 1
        while i < len(bit):
            bit[i] += x
            i += i & -i

    def pref(i):
        s = 0
        while i:
            s += bit[i]
            i -= i & -i
        return s

    ans = 0
    for _, kind, y1, y2, w in sorted(events):
        if kind != 1:
            add(bisect.bisect_left(ys, y1), w)
        else:
            ans += w * (
                pref(bisect.bisect_right(ys, y2))
                - pref(bisect.bisect_left(ys, y1))
            )
    print(ans)


if __name__ == "__main__":
    main()
