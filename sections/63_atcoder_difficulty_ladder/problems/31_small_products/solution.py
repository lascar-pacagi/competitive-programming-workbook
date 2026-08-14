import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data: return
    n, q = data[0], data[1]; log = max(1, n.bit_length()); index = 2
    up = [[0] * (n + 1) for _ in range(log)]; depth = [0] * (n + 1); root_sum = [0] * (n + 1)
    for node in range(2, n + 1):
        parent, weight = data[index], data[index + 1]; index += 2
        up[0][node] = parent; depth[node] = depth[parent] + 1; root_sum[node] = root_sum[parent] + weight
    for bit in range(1, log):
        for node in range(1, n + 1): up[bit][node] = up[bit - 1][up[bit - 1][node]]
    def lift(node: int, distance: int) -> int:
        for bit in range(log):
            if distance >> bit & 1: node = up[bit][node]
        return node
    def lca(left: int, right: int) -> int:
        if depth[left] < depth[right]: left, right = right, left
        left = lift(left, depth[left] - depth[right])
        if left == right: return left
        for bit in range(log - 1, -1, -1):
            if up[bit][left] != up[bit][right]: left, right = up[bit][left], up[bit][right]
        return up[0][left]
    output = []
    for _ in range(q):
        left, right = data[index], data[index + 1]; index += 2; common = lca(left, right)
        output.append(str(root_sum[left] + root_sum[right] - 2 * root_sum[common]))
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__": main()
