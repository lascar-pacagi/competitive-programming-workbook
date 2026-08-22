import sys


def arborescence(n, root, edges):
    answer = 0
    while True:
        incoming = [10**30] * n
        pre = [-1] * n
        for u, v, w in edges:
            if u != v and w < incoming[v]:
                incoming[v] = w
                pre[v] = u
        incoming[root] = 0
        if any(x == 10**30 for x in incoming):
            return None
        answer += sum(incoming)
        component = [-1] * n
        seen = [-1] * n
        count = 0
        for start in range(n):
            v = start
            while seen[v] != start and component[v] < 0 and v != root:
                seen[v] = start
                v = pre[v]
            if v != root and component[v] < 0:
                u = pre[v]
                component[v] = count
                while u != v:
                    component[u] = count
                    u = pre[u]
                count += 1
        if count == 0:
            return answer
        for v in range(n):
            if component[v] < 0:
                component[v] = count
                count += 1
        edges = [
            (component[u], component[v], w - incoming[v]) for u, v, w in edges
        ]
        root = component[root]
        n = count


def main():
    d = list(map(int, sys.stdin.buffer.read().split()))
    n, m, root = d[:3]
    edges = []
    for i in range(3, 3 + 3 * m, 3):
        edges.append((d[i] - 1, d[i + 1] - 1, d[i + 2]))
    answer = arborescence(n, root - 1, edges)
    print("IMPOSSIBLE" if answer is None else answer)


if __name__ == "__main__":
    main()
