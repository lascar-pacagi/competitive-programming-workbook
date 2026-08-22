import sys


def possible(a, x):
    n = len(a)
    match = [-1] * n

    def dfs(u, seen):
        for v in range(n):
            if a[u][v] <= x and not seen[v]:
                seen[v] = 1
                if match[v] < 0 or dfs(match[v], seen):
                    match[v] = u
                    return True
        return False

    return all(dfs(u, [False] * n) for u in range(n))


def main():
    d = list(map(int, sys.stdin.buffer.read().split()))
    n = d[0]
    a = [d[1 + i * n : 1 + (i + 1) * n] for i in range(n)]
    values = sorted(set(d[1:]))
    l = -1
    r = len(values) - 1
    while r - l > 1:
        m = (l + r) // 2
        if possible(a, values[m]):
            r = m
        else:
            l = m
    print(values[r])


if __name__ == "__main__":
    main()
