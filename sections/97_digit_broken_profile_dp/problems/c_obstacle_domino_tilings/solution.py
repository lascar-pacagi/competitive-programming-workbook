import sys
MOD = 1000000007

def main():
    data = sys.stdin.buffer.read().split()
    n, m = map(int, data[:2])
    grid = [x.decode() for x in data[2:]]
    dp = {0: 1}
    for row in range(n):
        blocked = sum(((grid[row][c] == '#') << c for c in range(m)))
        nd = {}
        for incoming, value in dp.items():
            if incoming & blocked:
                continue

            def fill(c, used, out):
                if c == m:
                    nd[out] = (nd.get(out, 0) + value) % MOD
                    return
                bit = 1 << c
                if (used | blocked) & bit:
                    fill(c + 1, used, out)
                else:
                    if c + 1 < m and (not (used | blocked) >> c + 1 & 1):
                        fill(c + 2, used | bit | bit << 1, out)
                    if row + 1 < n and grid[row + 1][c] == '.':
                        fill(c + 1, used | bit, out | bit)
            fill(0, incoming, 0)
        dp = nd
    print(dp.get(0, 0))
if __name__ == '__main__':
    main()
