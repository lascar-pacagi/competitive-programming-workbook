import math
import sys


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, index, delta):
        while index <= self.n:
            self.bit[index] += delta
            index += index & -index

    def prefix_sum(self, index):
        result = 0
        while index > 0:
            result += self.bit[index]
            index -= index & -index
        return result


class GcdTree:
    def __init__(self, values):
        self.size = 1
        while self.size < len(values):
            self.size *= 2
        self.tree = [0] * (2 * self.size)
        self.tree[self.size:self.size + len(values)] = values
        for node in range(self.size - 1, 0, -1):
            self._pull(node)

    def _pull(self, node):
        self.tree[node] = math.gcd(
            self.tree[2 * node],
            self.tree[2 * node + 1],
        )

    def add(self, position, delta):
        node = self.size + position
        self.tree[node] += delta
        node //= 2
        while node:
            self._pull(node)
            node //= 2

    def query(self, left, right):
        answer = 0
        left += self.size
        right += self.size
        while left < right:
            if left & 1:
                answer = math.gcd(answer, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                answer = math.gcd(answer, self.tree[right])
            left //= 2
            right //= 2
        return answer


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, q = data[0], data[1]
    array = data[2:2 + n]
    pointer = 2 + n

    difference = [array[0]]
    difference.extend(array[i] - array[i - 1] for i in range(1, n))

    values = Fenwick(n)
    for index, delta in enumerate(difference, 1):
        values.add(index, delta)
    differences = GcdTree(difference)

    output = []
    for _ in range(q):
        operation = data[pointer]
        left = data[pointer + 1] - 1
        right = data[pointer + 2]
        pointer += 3

        if operation == 1:
            delta = data[pointer]
            pointer += 1
            differences.add(left, delta)
            values.add(left + 1, delta)
            if right < n:
                differences.add(right, -delta)
                values.add(right + 1, -delta)
        else:
            first_value = values.prefix_sum(left + 1)
            inside = differences.query(left + 1, right)
            output.append(str(math.gcd(abs(first_value), abs(inside))))

    print('\n'.join(output))


if __name__ == '__main__':
    main()
