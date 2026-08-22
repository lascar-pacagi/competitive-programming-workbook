import sys

MOD = 1_000_000_007


class RollbackParityDSU:
    def __init__(self, n: int) -> None:
        self.parent = [-1] * n
        self.parity = [0] * n
        self.components = n
        self.contradictions = 0
        self.history = []

    def find(self, x: int) -> tuple[int, int]:
        parity = 0
        while self.parent[x] >= 0:
            parity ^= self.parity[x]
            x = self.parent[x]
        return x, parity

    def add(self, u: int, v: int, required: int) -> None:
        root_u, parity_u = self.find(u)
        root_v, parity_v = self.find(v)
        if root_u == root_v:
            if parity_u ^ parity_v != required:
                self.contradictions += 1
                self.history.append((1,))
            else:
                self.history.append((0,))
            return
        if -self.parent[root_u] < -self.parent[root_v]:
            root_u, root_v = root_v, root_u
            parity_u, parity_v = parity_v, parity_u
        self.history.append((2, root_v, root_u, self.parent[root_u],
                             self.parent[root_v], self.parity[root_v]))
        self.parent[root_u] += self.parent[root_v]
        self.parent[root_v] = root_u
        self.parity[root_v] = parity_u ^ parity_v ^ required
        self.components -= 1

    def rollback(self, target: int) -> None:
        while len(self.history) > target:
            change = self.history.pop()
            if change[0] == 1:
                self.contradictions -= 1
            elif change[0] == 2:
                _, child, root, root_size, child_size, child_parity = change
                self.parent[root] = root_size
                self.parent[child] = child_size
                self.parity[child] = child_parity
                self.components += 1


def main() -> None:
    lines = sys.stdin.buffer.readlines()
    if not lines:
        return
    n, q = map(int, lines[0].split())
    size = 1
    while size < q:
        size *= 2
    timeline = [[] for _ in range(2 * size)]
    queries = [False] * q
    start = [-1] * q
    inserted = [None] * q

    def add_interval(left: int, right: int, constraint: tuple[int, int, int]) -> None:
        left += size
        right += size
        while left < right:
            if left & 1:
                timeline[left].append(constraint)
                left += 1
            if right & 1:
                right -= 1
                timeline[right].append(constraint)
            left //= 2
            right //= 2

    for time, raw in enumerate(lines[1:q + 1]):
        parts = raw.split()
        if parts[0] == b"+":
            constraint = (int(parts[1]) - 1, int(parts[2]) - 1, int(parts[3]))
            inserted[time] = constraint
            start[time] = time
        elif parts[0] == b"-":
            identifier = int(parts[1]) - 1
            add_interval(start[identifier], time, inserted[identifier])
            start[identifier] = -1
        else:
            queries[time] = True
    for identifier in range(q):
        if start[identifier] != -1:
            add_interval(start[identifier], q, inserted[identifier])

    powers = [1] * (n + 1)
    for i in range(1, n + 1):
        powers[i] = powers[i - 1] * 2 % MOD

    dsu = RollbackParityDSU(n)
    output = []
    stack = [(1, 0, size, 0)]
    snapshots = {}
    while stack:
        node, left, right, phase = stack.pop()
        if phase == 0:
            saved = len(dsu.history)
            snapshots[node] = saved
            for u, v, parity in timeline[node]:
                dsu.add(u, v, parity)
            if right - left == 1:
                if left < q and queries[left]:
                    output.append("0" if dsu.contradictions
                                  else str(powers[dsu.components]))
                dsu.rollback(saved)
            else:
                middle = (left + right) // 2
                stack.append((node, left, right, 1))
                stack.append((node * 2 + 1, middle, right, 0))
                stack.append((node * 2, left, middle, 0))
        else:
            dsu.rollback(snapshots.pop(node))
    print("\n".join(output))


if __name__ == "__main__":
    main()
