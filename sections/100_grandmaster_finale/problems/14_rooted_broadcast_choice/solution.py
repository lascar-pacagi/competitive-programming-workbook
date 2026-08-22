import sys


def directed_mst(vertices: int, root: int,
                 edges: list[tuple[int, int, int]]) -> int | None:
    answer = 0
    infinity = 10**40
    while True:
        incoming = [infinity] * vertices
        parent = [-1] * vertices
        for u, v, cost in edges:
            if u != v and cost < incoming[v]:
                incoming[v] = cost
                parent[v] = u
        incoming[root] = 0
        if any(cost == infinity for cost in incoming):
            return None
        answer += sum(incoming)

        component = [-1] * vertices
        seen = [-1] * vertices
        cycles = 0
        for start in range(vertices):
            v = start
            while seen[v] != start and component[v] == -1 and v != root:
                seen[v] = start
                v = parent[v]
            if v != root and component[v] == -1:
                u = parent[v]
                while u != v:
                    component[u] = cycles
                    u = parent[u]
                component[v] = cycles
                cycles += 1
        if cycles == 0:
            return answer

        for v in range(vertices):
            if component[v] == -1:
                component[v] = cycles
                cycles += 1
        contracted = []
        for u, v, cost in edges:
            new_u, new_v = component[u], component[v]
            if new_u != new_v:
                cost -= incoming[v]
            contracted.append((new_u, new_v, cost))
        root = component[root]
        vertices = cycles
        edges = contracted


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[:2]
    activation = data[2:2 + n]
    edges = []
    index = 2 + n
    for _ in range(m):
        u, v, cost = data[index:index + 3]
        index += 3
        edges.append((u - 1, v - 1, cost))

    penalty = (n + 1) * 10**9 + 1
    super_root = n
    edges.extend((super_root, v, penalty + activation[v]) for v in range(n))
    encoded = directed_mst(n + 1, super_root, edges)
    if encoded is None or encoded // penalty != 1:
        print(-1)
    else:
        print(encoded % penalty)


if __name__ == "__main__":
    main()
