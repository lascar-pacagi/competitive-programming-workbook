import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    budget = next(it)
    time = [0] * n
    value = [0] * n
    for i in range(n):
        time[i] = next(it)
        value[i] = next(it)
    children = [[] for _ in range(n)]
    for child in range(1, n):
        parent = next(it) - 1
        children[parent].append(child)

    order = [0]
    for u in order:
        order.extend(children[u])

    neg = -10**30
    dp = [[neg] * (budget + 1) for _ in range(n)]
    for u in reversed(order):
        if time[u] <= budget:
            dp[u][time[u]] = value[u]
        for v in children[u]:
            merged = dp[u][:]
            for used in range(budget + 1):
                if dp[u][used] <= neg // 2:
                    continue
                for add in range(1, budget - used + 1):
                    if dp[v][add] <= neg // 2:
                        continue
                    candidate = dp[u][used] + dp[v][add]
                    if candidate > merged[used + add]:
                        merged[used + add] = candidate
            dp[u] = merged
    answer = max(0, max(dp[0]))
    print(answer)


if __name__ == "__main__":
    main()
