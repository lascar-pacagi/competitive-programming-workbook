import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    graph = [[] for _ in range(n)]
    pointer = 2
    for _ in range(m):
        start, end = data[pointer] - 1, data[pointer + 1] - 1
        pointer += 2
        graph[start].append(end)

    match_right = [-1] * n

    def augment(left: int, seen: list[bool]) -> bool:
        for right in graph[left]:
            if seen[right]:
                continue
            seen[right] = True
            if match_right[right] == -1 or augment(match_right[right], seen):
                match_right[right] = left
                return True
        return False

    matching = 0
    for left in range(n):
        matching += augment(left, [False] * n)
    print(n - matching)


if __name__ == "__main__":
    sys.setrecursionlimit(10_000)
    main()
