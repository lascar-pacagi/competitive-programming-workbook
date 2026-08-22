import sys
MOD = 1000000007

def main():
    data = sys.stdin.buffer.read().split()
    n, m = map(int, data[:2])
    grid = [x.decode() for x in data[2:]]
    valid = [x for x in range(1 << m) if not x & x << 1]
    dp = {0: 1}
    for row in grid:
        blocked = sum(((row[c] == '#') << c for c in range(m)))
        nd = {}
        for mask in valid:
            if mask & blocked:
                continue
            nd[mask] = sum((value for old, value in dp.items() if not mask & old)) % MOD
        dp = nd
    print(sum(dp.values()) % MOD)
if __name__ == '__main__':
    main()
