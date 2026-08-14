import sys
from collections import deque


class Dinic:
    def __init__(self, size: int) -> None:
        self.graph: list[list[list[int]]] = [[] for _ in range(size)]
        self.level = [-1] * size
        self.next_edge = [0] * size

    def add_edge(self, start: int, end: int, capacity: int) -> None:
        self.graph[start].append([end, len(self.graph[end]), capacity])
        self.graph[end].append([start, len(self.graph[start]) - 1, 0])

    def build_levels(self, source: int, sink: int) -> bool:
        self.level = [-1] * len(self.graph)
        self.level[source] = 0
        queue = deque([source])
        while queue:
            vertex = queue.popleft()
            for target, _, capacity in self.graph[vertex]:
                if capacity > 0 and self.level[target] == -1:
                    self.level[target] = self.level[vertex] + 1
                    queue.append(target)
        return self.level[sink] != -1

    def send_flow(self, vertex: int, sink: int, pushed: int) -> int:
        if vertex == sink:
            return pushed
        while self.next_edge[vertex] < len(self.graph[vertex]):
            edge = self.graph[vertex][self.next_edge[vertex]]
            target, reverse, capacity = edge
            if capacity > 0 and self.level[target] == self.level[vertex] + 1:
                flow = self.send_flow(target, sink, min(pushed, capacity))
                if flow:
                    edge[2] -= flow
                    self.graph[target][reverse][2] += flow
                    return flow
            self.next_edge[vertex] += 1
        return 0

    def max_flow(self, source: int, sink: int) -> int:
        total = 0
        while self.build_levels(source, sink):
            self.next_edge = [0] * len(self.graph)
            while pushed := self.send_flow(source, sink, 10**30):
                total += pushed
        return total


def main() -> None:
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    if not tokens:
        return
    n, m = tokens[0], tokens[1]
    profit = tokens[2 : 2 + n]
    pointer = 2 + n
    positive_total = sum(value for value in profit if value > 0)
    source, sink = n, n + 1
    flow = Dinic(n + 2)
    inf = positive_total + 1
    for project, value in enumerate(profit):
        if value > 0:
            flow.add_edge(source, project, value)
        elif value < 0:
            flow.add_edge(project, sink, -value)
    for _ in range(m):
        project, prerequisite = tokens[pointer] - 1, tokens[pointer + 1] - 1
        pointer += 2
        flow.add_edge(project, prerequisite, inf)
    print(positive_total - flow.max_flow(source, sink))


if __name__ == "__main__":
    sys.setrecursionlimit(300_000)
    main()
