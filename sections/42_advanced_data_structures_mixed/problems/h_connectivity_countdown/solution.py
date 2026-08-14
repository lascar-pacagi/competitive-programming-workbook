import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n, m, q = map(int, data[:3])
    index = 3
    edges = []
    for _ in range(m):
        u, v = map(int, data[index:index+2]); index += 2
        edges.append((u-1, v-1))
    operations = []
    deleted = [False] * m
    for _ in range(q):
        operation = data[index]; index += 1
        if operation == b'D':
            edge = int(data[index]) - 1; index += 1
            operations.append((operation, edge, -1)); deleted[edge] = True
        else:
            u, v = map(int, data[index:index+2]); index += 2
            operations.append((operation, u-1, v-1))
    parent = list(range(n)); size = [1] * n
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]; u = parent[u]
        return u
    def join(u, v):
        u, v = find(u), find(v)
        if u == v: return
        if size[u] < size[v]: u, v = v, u
        parent[v] = u; size[u] += size[v]
    for edge, (u, v) in enumerate(edges):
        if not deleted[edge]: join(u, v)
    answers = []
    for operation, x, y in reversed(operations):
        if operation == b'D': join(*edges[x])
        else: answers.append('YES' if find(x) == find(y) else 'NO')
    print('\n'.join(reversed(answers)))

if __name__ == "__main__":
    main()
