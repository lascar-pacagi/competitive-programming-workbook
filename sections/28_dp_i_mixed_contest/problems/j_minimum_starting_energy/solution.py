import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[:2]
    values = data[2:]
    grid = [values[row * m:(row + 1) * m] for row in range(n)]
    infinity = 10**30
    need = [infinity] * m

    for row in range(n - 1, -1, -1):
        for column in range(m - 1, -1, -1):
            if row == n - 1 and column == m - 1:
                need[column] = max(0, -grid[row][column])
                continue
            after = infinity
            if row + 1 < n:
                after = min(after, need[column])
            if column + 1 < m:
                after = min(after, need[column + 1])
            need[column] = max(0, after - grid[row][column])

    print(need[0])


if __name__ == "__main__":
    main()
