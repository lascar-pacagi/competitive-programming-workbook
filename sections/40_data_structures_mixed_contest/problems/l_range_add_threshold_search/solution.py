import sys

def main():
    d = sys.stdin.buffer.read().split()
    if not d:
        return
    n, q = map(int, d[:2])
    a = list(map(int, d[2:2 + n]))
    maximum = [0] * (4 * n)
    lazy = [0] * (4 * n)

    def build(node, left, right):
        if right - left == 1:
            maximum[node] = a[left]
            return
        middle = (left + right) // 2
        build(2 * node, left, middle)
        build(2 * node + 1, middle, right)
        maximum[node] = max(maximum[2 * node], maximum[2 * node + 1])

    def apply(node, delta):
        maximum[node] += delta
        lazy[node] += delta

    def push(node):
        delta = lazy[node]
        if delta:
            apply(2 * node, delta)
            apply(2 * node + 1, delta)
            lazy[node] = 0

    def add(node, left, right, query_left, query_right, delta):
        if right <= query_left or query_right <= left:
            return
        if query_left <= left and right <= query_right:
            apply(node, delta)
            return
        push(node)
        middle = (left + right) // 2
        add(2 * node, left, middle, query_left, query_right, delta)
        add(2 * node + 1, middle, right, query_left, query_right, delta)
        maximum[node] = max(maximum[2 * node], maximum[2 * node + 1])

    def first(node, left, right, query_left, query_right, threshold):
        if (right <= query_left or query_right <= left
                or maximum[node] < threshold):
            return -1
        if right - left == 1:
            return left
        push(node)
        middle = (left + right) // 2
        answer = first(
            2 * node, left, middle, query_left, query_right, threshold
        )
        if answer != -1:
            return answer
        return first(
            2 * node + 1, middle, right, query_left, query_right, threshold
        )

    build(1, 0, n)
    out = []
    p = 2 + n
    for _ in range(q):
        operation = d[p]
        left, right, x = map(int, d[p + 1:p + 4])
        p += 4
        left -= 1
        if operation == b'A':
            add(1, 0, n, left, right, x)
        else:
            answer = first(1, 0, n, left, right, x)
            out.append(str(answer + 1 if answer != -1 else -1))
    print('\n'.join(out))
if __name__ == '__main__':
    main()
