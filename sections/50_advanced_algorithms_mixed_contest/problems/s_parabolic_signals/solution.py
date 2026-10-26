import sys


class LiChao:
    def __init__(self, coordinates):
        self.x = sorted(set(coordinates))
        self.tree = [None] * (4 * len(self.x))

    @staticmethod
    def value(line, x):
        return line[0] * x + line[1]

    def add(self, line, node=1, left=0, right=None):
        if right is None:
            right = len(self.x) - 1
        if self.tree[node] is None:
            self.tree[node] = line
            return
        middle = (left + right) // 2
        if (self.value(line, self.x[middle])
                < self.value(self.tree[node], self.x[middle])):
            self.tree[node], line = line, self.tree[node]
        if left == right:
            return
        if (self.value(line, self.x[left])
                < self.value(self.tree[node], self.x[left])):
            self.add(line, 2 * node, left, middle)
        elif (self.value(line, self.x[right])
                < self.value(self.tree[node], self.x[right])):
            self.add(line, 2 * node + 1, middle + 1, right)

    def query(self, x):
        answer = 10**30
        node, left, right = 1, 0, len(self.x) - 1
        while True:
            if self.tree[node] is not None:
                answer = min(answer, self.value(self.tree[node], x))
            if left == right:
                return answer
            middle = (left + right) // 2
            if x <= self.x[middle]:
                node, right = 2 * node, middle
            else:
                node, left = 2 * node + 1, middle + 1


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n, q = next(data), next(data)
    stations = [(next(data), next(data)) for _ in range(n)]
    queries = [next(data) for _ in range(q)]
    hull = LiChao(queries)
    for position, power in stations:
        hull.add((-2 * position, position * position - power))
    print('\n'.join(str(-hull.query(x) - x * x) for x in queries))


if __name__ == '__main__':
    main()
