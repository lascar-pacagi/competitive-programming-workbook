import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    index = 0
    n = data[index]
    index += 1
    cost = data[index:index + n]
    index += n
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = data[index] - 1, data[index + 1] - 1
        index += 2
        graph[u].append(v)
        graph[v].append(u)

    parent = [-2] * n
    parent[0] = -1
    order = [0]
    for u in order:
        for v in graph[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            order.append(v)

    infinity = 10**30
    dp = [[0, 0, 0] for _ in range(n)]

    for u in reversed(order):
        selected = cost[u]
        covered_base = 0
        force_guard_child = infinity
        awaiting_parent = 0

        for v in graph[u]:
            if parent[v] != u:
                continue
            selected += min(dp[v])
            best_covered_child = min(dp[v][0], dp[v][1])
            covered_base += best_covered_child
            force_guard_child = min(
                force_guard_child, dp[v][0] - best_covered_child)
            awaiting_parent += dp[v][1]

        dp[u][0] = selected
        dp[u][1] = covered_base + force_guard_child
        dp[u][2] = awaiting_parent

    print(min(dp[0][0], dp[0][1]))


if __name__ == "__main__":
    main()
