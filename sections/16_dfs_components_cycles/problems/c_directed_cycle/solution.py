import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append(v)

    color = [0] * n
    for start in range(n):
        if color[start] != 0:
            continue
        color[start] = 1
        stack = [(start, 0)]
        while stack:
            u, i = stack[-1]
            if i == len(adj[u]):
                color[u] = 2
                stack.pop()
                continue
            v = adj[u][i]
            stack[-1] = (u, i + 1)
            if color[v] == 0:
                color[v] = 1
                stack.append((v, 0))
            elif color[v] == 1:
                print("CYCLIC")
                return
    print("ACYCLIC")


if __name__ == "__main__":
    main()

