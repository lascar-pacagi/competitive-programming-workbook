import sys
from array import array

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, q = data[:2]
    next_vertex = array('i', (x - 1 for x in data[2:2 + n]))
    value = data[2 + n:2 + 2 * n]
    index = 2 + 2 * n
    levels = 61
    up = [next_vertex]
    first_minimum = (value[next_vertex[v]] for v in range(n))
    minimum = [array('q', first_minimum)]
    for level in range(1, levels):
        previous_up = up[level - 1]
        previous_minimum = minimum[level - 1]
        next_up = (previous_up[previous_up[v]] for v in range(n))
        up.append(array('i', next_up))
        next_minimum = (
            min(
                previous_minimum[v],
                previous_minimum[previous_up[v]],
            )
            for v in range(n)
        )
        minimum.append(array('q', next_minimum))
    output = []
    for _ in range(q):
        vertex = data[index] - 1
        steps = data[index + 1]
        index += 2
        answer = value[vertex]
        bit = 0
        while steps:
            if steps & 1:
                answer = min(answer, minimum[bit][vertex])
                vertex = up[bit][vertex]
            steps //= 2
            bit += 1
        output.append(f'{vertex + 1} {answer}')
    sys.stdout.write('\n'.join(output))
if __name__ == '__main__':
    main()
