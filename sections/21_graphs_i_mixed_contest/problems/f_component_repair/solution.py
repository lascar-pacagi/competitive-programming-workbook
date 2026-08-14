import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[:2]
    graph = [[] for _ in range(n)]
    index = 2
    for _ in range(m):
        u, v = data[index] - 1, data[index + 1] - 1
        index += 2
        graph[u].append(v); graph[v].append(u)
    seen = [False] * n
    sizes = []
    for start in range(n):
        if seen[start]:
            continue
        seen[start] = True
        stack = [start]
        size = 0
        while stack:
            u = stack.pop()
            size += 1
            for v in graph[u]:
                if not seen[v]:
                    seen[v] = True
                    stack.append(v)
        sizes.append(size)
    print(len(sizes), len(sizes) - 1, max(sizes))


if __name__ == "__main__":
    main()
