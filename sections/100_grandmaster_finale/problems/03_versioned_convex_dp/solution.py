import bisect
import sys


def main() -> None:
    lines = sys.stdin.buffer.readlines()
    if not lines:
        return
    q = int(lines[0])
    parent = [0] * (q + 1)
    kind = [b""] * (q + 1)
    first = [0] * (q + 1)
    second = [0] * (q + 1)
    children = [[] for _ in range(q + 1)]
    coordinates = []
    for version, raw in enumerate(lines[1:q + 1], 1):
        parts = raw.split()
        parent[version] = int(parts[0])
        kind[version] = parts[1]
        first[version] = int(parts[2])
        if parts[1] == b"A":
            second[version] = int(parts[3])
        else:
            coordinates.append(first[version])
        children[parent[version]].append(version)
    coordinates = sorted(set(coordinates)) or [0]
    tree = [None] * (4 * len(coordinates) + 4)
    history = []

    def key(line: tuple[int, int, int], x: int) -> tuple[int, int]:
        return line[0] * x + line[1], line[2]

    def better(a, b, x: int) -> bool:
        return a is not None and (b is None or key(a, x) < key(b, x))

    def assign(node: int, line) -> None:
        history.append((node, tree[node]))
        tree[node] = line

    def insert(line) -> None:
        node, left, right = 1, 0, len(coordinates)
        while True:
            if tree[node] is None:
                assign(node, line)
                return
            middle = (left + right) // 2
            if better(line, tree[node], coordinates[middle]):
                displaced = tree[node]
                assign(node, line)
                line = displaced
            if right - left == 1:
                return
            if better(line, tree[node], coordinates[left]):
                node *= 2
                right = middle
            elif better(line, tree[node], coordinates[right - 1]):
                node = node * 2 + 1
                left = middle
            else:
                return

    def query(position: int):
        node, left, right = 1, 0, len(coordinates)
        answer = None
        while True:
            if better(tree[node], answer, coordinates[position]):
                answer = tree[node]
            if right - left == 1:
                return answer
            middle = (left + right) // 2
            if position < middle:
                node *= 2
                right = middle
            else:
                node = node * 2 + 1
                left = middle

    insert((0, 0, 0))
    history.clear()
    answers = [None] * (q + 1)
    stack = [(version, 0, 0) for version in reversed(children[0])]
    while stack:
        version, phase, snapshot = stack.pop()
        if phase == 0:
            snapshot = len(history)
            if kind[version] == b"A":
                insert((first[version], second[version], version))
            else:
                position = bisect.bisect_left(coordinates, first[version])
                line = query(position)
                answers[version] = key(line, first[version])
            stack.append((version, 1, snapshot))
            stack.extend((child, 0, 0) for child in reversed(children[version]))
        else:
            while len(history) > snapshot:
                node, old_line = history.pop()
                tree[node] = old_line
    print("\n".join(f"{answers[i][0]} {answers[i][1]}"
                    for i in range(1, q + 1) if kind[i] == b"Q"))


if __name__ == "__main__":
    main()
