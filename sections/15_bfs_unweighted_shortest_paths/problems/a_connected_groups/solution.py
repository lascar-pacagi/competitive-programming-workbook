from collections import deque
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    t = next(it)
    out: list[str] = []
    for _ in range(t):
        n = next(it)
        m = next(it)
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = next(it) - 1
            v = next(it) - 1
            adj[u].append(v)
            adj[v].append(u)

        seen = [False] * n
        sizes: list[int] = []
        for start in range(n):
            if seen[start]:
                continue
            seen[start] = True
            q = deque([start])
            size = 0
            while q:
                u = q.popleft()
                size += 1
                for v in adj[u]:
                    if not seen[v]:
                        seen[v] = True
                        q.append(v)
            sizes.append(size)

        sizes.sort()
        out.append(str(len(sizes)))
        out.append(" ".join(map(str, sizes)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

