import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q = data[0], data[1]
    size = 1
    while size < n:
        size *= 2

    tree = [-1] * (2 * size)
    tree[size : size + n] = data[2 : 2 + n]
    for node in range(size - 1, 0, -1):
        tree[node] = max(tree[2 * node], tree[2 * node + 1])

    pointer = 2 + n
    output = []
    for _ in range(q):
        operation = data[pointer]
        pointer += 1
        if operation == 1:
            index, capacity = data[pointer], data[pointer + 1]
            pointer += 2
            node = size + index - 1
            tree[node] = capacity
            node //= 2
            while node:
                tree[node] = max(tree[2 * node], tree[2 * node + 1])
                node //= 2
        else:
            need = data[pointer]
            pointer += 1
            if tree[1] < need:
                output.append("0")
                continue
            node = 1
            while node < size:
                if tree[2 * node] >= need:
                    node *= 2
                else:
                    node = 2 * node + 1
            output.append(str(node - size + 1))
    print("\n".join(output))


if __name__ == "__main__":
    main()
