import sys
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[:2]
    values = data[2:]
    grid = [values[r*m:(r+1)*m] for r in range(n)]
    neg = -10**30
    previous = [[neg, neg] for _ in range(m)]
    for r in range(n):
        current = [[neg, neg] for _ in range(m)]
        for c in range(m):
                if r == 0 and c == 0:
                    current[c][0] = grid[r][c]
                for used in range(2):
                    if r and previous[c][used] != neg:
                        current[c][used] = max(current[c][used], previous[c][used] + grid[r][c])
                    if c and current[c-1][used] != neg:
                        current[c][used] = max(current[c][used], current[c-1][used] + grid[r][c])
                if r and c and previous[c-1][0] != neg:
                    current[c][1] = max(current[c][1], previous[c-1][0] + grid[r][c])
        previous = current
    print(-1 if previous[-1][1] == neg else previous[-1][1])
if __name__ == "__main__":
    main()
