import sys
from collections import deque


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m, need = data[:3]
    raw = [data[i:i + 4] for i in range(3, len(data), 4)]
    color_values = {edge[2] for edge in raw}
    color_id = {color: i for i, color in enumerate(color_values)}
    edges = [(u - 1, v - 1, color_id[color], weight)
             for u, v, color, weight in raw]
    weights = sorted({edge[3] for edge in edges})

    def feasible(limit: int) -> bool:
        allowed = [weight <= limit for _, _, _, weight in edges]
        chosen = [False] * m
        for _ in range(need):
            forest = [[] for _ in range(n)]
            color_edge = [-1] * len(color_values)
            for i, (u, v, color, _) in enumerate(edges):
                if chosen[i]:
                    forest[u].append((v, i))
                    forest[v].append((u, i))
                    color_edge[color] = i

            exchange = [[] for _ in range(m)]
            source = [False] * m
            target = [False] * m
            for y, (start, goal, color, _) in enumerate(edges):
                if not allowed[y] or chosen[y]:
                    continue
                parent_vertex = [-1] * n
                parent_edge = [-1] * n
                parent_vertex[start] = start
                queue = deque([start])
                while queue and parent_vertex[goal] == -1:
                    u = queue.popleft()
                    for v, index in forest[u]:
                        if parent_vertex[v] == -1:
                            parent_vertex[v] = u
                            parent_edge[v] = index
                            queue.append(v)
                if parent_vertex[goal] == -1:
                    source[y] = True
                else:
                    v = goal
                    while v != start:
                        exchange[parent_edge[v]].append(y)
                        v = parent_vertex[v]

                same = color_edge[color]
                if same == -1:
                    target[y] = True
                else:
                    exchange[y].append(same)

            parent = [-2] * m
            queue = deque()
            for i in range(m):
                if source[i]:
                    parent[i] = -1
                    queue.append(i)
            finish = -1
            while queue and finish == -1:
                u = queue.popleft()
                if target[u]:
                    finish = u
                    break
                for v in exchange[u]:
                    if parent[v] == -2:
                        parent[v] = u
                        queue.append(v)
            if finish == -1:
                return False
            while finish != -1:
                chosen[finish] = not chosen[finish]
                finish = parent[finish]
        return True

    if not weights or not feasible(weights[-1]):
        print(-1)
        return
    low, high = 0, len(weights) - 1
    while low < high:
        middle = (low + high) // 2
        if feasible(weights[middle]):
            high = middle
        else:
            low = middle + 1
    print(weights[low])


if __name__ == "__main__":
    main()
