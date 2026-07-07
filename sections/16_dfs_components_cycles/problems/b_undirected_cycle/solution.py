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
        adj[v].append(u)

    seen = [False] * n
    for start in range(n):
        if seen[start]:
            continue
        seen[start] = True
        stack = [(start, -1)]
        while stack:
            u, parent = stack.pop()
            for v in adj[u]:
                if v == parent:
                    continue
                if seen[v]:
                    print("CYCLIC")
                    return
                seen[v] = True
                stack.append((v, u))
    print("ACYCLIC")


if __name__ == "__main__":
    main()

