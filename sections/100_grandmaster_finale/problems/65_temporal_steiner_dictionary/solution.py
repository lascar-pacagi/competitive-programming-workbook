import bisect
import sys
from array import array


def main() -> None:
    data = array("q", map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    index = 0
    n, m, q = data[index:index + 3]
    index += 3
    values = data[index:index + n]
    index += n
    coordinates = sorted(set(values))
    edges = []
    for _ in range(m):
        u, v, weight = data[index] - 1, data[index + 1] - 1, data[index + 2]
        index += 3
        edges.append((weight, u, v))
    edges.sort()

    capacity = 2 * n + 1
    dsu = array("i", range(capacity))
    tree_parent = array("i", [-1]) * capacity
    merge_weight = array("q", [-(1 << 60)]) * capacity
    child_left = array("i", [-1]) * capacity
    child_right = array("i", [-1]) * capacity

    def find(x):
        root = x
        while dsu[root] != root:
            root = dsu[root]
        while dsu[x] != x:
            x, dsu[x] = dsu[x], root
        return root

    nodes = n
    for weight, u, v in edges:
        first, second = find(u), find(v)
        if first == second:
            continue
        parent = nodes
        nodes += 1
        merge_weight[parent] = weight
        child_left[parent] = first
        child_right[parent] = second
        tree_parent[first] = tree_parent[second] = parent
        dsu[first] = dsu[second] = parent
        dsu[parent] = parent

    roots = [node for node in range(nodes) if tree_parent[node] == -1]
    left = array("i", [0]) * nodes
    right = array("i", [0]) * nodes
    leaf_order = []
    timer = 0
    for root in roots:
        stack = [(root, 0)]
        while stack:
            node, phase = stack.pop()
            if phase:
                right[node] = timer
                continue
            left[node] = timer
            stack.append((node, 1))
            if node < n:
                leaf_order.append(node)
                timer += 1
            else:
                first, second = child_left[node], child_right[node]
                stack.append((second, 0))
                stack.append((first, 0))

    log = max(1, nodes.bit_length())
    up = [array("i", (
        node if tree_parent[node] == -1 else tree_parent[node]
        for node in range(nodes)
    ))]
    for bit in range(1, log):
        previous = up[bit - 1]
        up.append(array("i", (previous[previous[node]] for node in range(nodes))))

    segment_left = array("i", [0])
    segment_right = array("i", [0])
    segment_count = array("i", [0])

    def clone(node):
        segment_left.append(segment_left[node])
        segment_right.append(segment_right[node])
        segment_count.append(segment_count[node])
        return len(segment_count) - 1

    def insert(previous, position):
        root = clone(previous)
        old, current = previous, root
        low, high = 0, len(coordinates)
        while True:
            segment_count[current] += 1
            if high - low == 1:
                return root
            middle = (low + high) // 2
            if position < middle:
                old_child = segment_left[old]
                new_child = clone(old_child)
                segment_left[current] = new_child
                old, current, high = old_child, new_child, middle
            else:
                old_child = segment_right[old]
                new_child = clone(old_child)
                segment_right[current] = new_child
                old, current, low = old_child, new_child, middle

    prefix_root = array("i", [0])
    for vertex in leaf_order:
        compressed = bisect.bisect_left(coordinates, values[vertex])
        prefix_root.append(insert(prefix_root[-1], compressed))

    output = []
    for _ in range(q):
        vertex, threshold, k = data[index] - 1, data[index + 1], data[index + 2]
        index += 3
        component = vertex
        for bit in range(log - 1, -1, -1):
            ancestor = up[bit][component]
            if ancestor != component and merge_weight[ancestor] <= threshold:
                component = ancestor
        a, b = prefix_root[right[component]], prefix_root[left[component]]
        low, high = 0, len(coordinates)
        while high - low > 1:
            count_left = (segment_count[segment_left[a]]
                          - segment_count[segment_left[b]])
            middle = (low + high) // 2
            if k <= count_left:
                a, b = segment_left[a], segment_left[b]
                high = middle
            else:
                k -= count_left
                a, b = segment_right[a], segment_right[b]
                low = middle
        output.append(str(coordinates[low]))
    print("\n".join(output))


if __name__ == "__main__":
    main()
